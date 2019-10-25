import enum


class AccountType(enum.Enum):
    Payroll = 1
    Debit = 2
    Credit = 3


class Account:
    def __init__(
        self,
        isActive: bool = True,
        name: str = "Null",
        accountType: AccountType = AccountType.Payroll,
        balance: float = 0.0,
    ):
        self._isActive = isActive
        self._name = name
        self._accountType = accountType
        self._balance = balance

    def delete(self):
        self._isActive = False

    def balanceReport(self) -> str:
        return "Remaining Balance: " + str(self._balance)

    def accountInfo(self) -> str:
        return (
            "Name: "
            + self._name
            + "\nType: "
            + self._accountType.name
            + "\nStatus: "
            + ("Active" if self._isActive else "Inactive")
        )

    def receive(self, amount: float):
        self._balance += amount


class AccountWithdrawable(Account):
    def withdraw(self, amount: float):
        if self._balance - amount < 0:
            raise Exception("Insufficient funds")
        else:
            self._balance -= amount


class AccountDepositable(Account):
    def deposit(self, amount: float):
        self._balance += amount


class AccountTransferable(Account):
    def transfer(self, amount: float, to: Account):
        if self._balance - amount < 0:
            raise Exception("Insufficient funds")
        else:
            self._balance -= amount
            to.receive(amount)


class AccountInterestGaining(Account):
    def __init__(
        self,
        isActive: bool = True,
        name: str = "Null",
        accountType: AccountType = AccountType.Payroll,
        balance: float = 0.0,
        interestRate: float = 0.0,
    ):
        self._isActive = isActive
        self._name = name
        self._accountType = accountType
        self._balance = balance
        if interestRate < 0:
            raise Exception("Interest Rate must be greater than 0")
        else:
            self._interestRate = interestRate

    def applyInterest(self):
        self._balance += self._balance * self._interestRate

    def changeInterestRate(self, interestRate: float):
        self._interestRate = interestRate


class Payroll(AccountWithdrawable):
    pass


class Credit(
    AccountWithdrawable, AccountDepositable, AccountTransferable, AccountInterestGaining
):
    def __init__(
        self,
        isActive: bool = True,
        name: str = "Null",
        balance: float = 0.0,
        interestRate: float = 0.0,
        limit: float = 0.0,
    ):
        self._isActive = isActive
        self._name = name
        self._accountType = AccountType.Credit
        self._balance = balance
        self._interestRate = interestRate
        if limit < 0:
            raise Exception("Limit must be greater than 0")
        else:
            self._limit = limit

    def withdraw(self, amount: float) -> bool:
        if self._balance - amount < -self._limit:
            raise Exception("Insufficient funds")
        else:
            self._balance -= amount


class Debit(
    AccountWithdrawable, AccountDepositable, AccountTransferable, AccountInterestGaining
):
    def __init__(
        self,
        isActive: bool = True,
        name: str = "Null",
        balance: float = 0.0,
        interestRate: float = 0.0,
        requiredBalance: float = 0.0,
    ):
        self._isActive = isActive
        self._name = name
        self._accountType = AccountType.Debit
        self._balance = balance
        if interestRate < 0:
            raise Exception("Interest Rate must be greater than 0")
        else:
            self._interestRate = interestRate
        if requiredBalance < 0:
            raise Exception("Required Balance must be greater than 0")
        else:
            self._requiredBalance = requiredBalance

    def checkRequiredBalance(self):
        if self._balance < self._requiredBalance:
            self._isActive = False


class Bank:
    def __init__(self):
        self.__accounts: [Account] = []

    def addAccount(self, newAccount: Account):
        self.__accounts.append(newAccount)

    def accounts(self):
        return self.__accounts


if __name__ == "__main__":
    a = Debit(name="Justin", balance=2000, interestRate=0.10, requiredBalance=500)
    b = Payroll()
    c = Credit()
    citilink = Bank()
    citilink.addAccount(a)
    citilink.addAccount(b)
    citilink.addAccount(c)
    for i in citilink.accounts():
        print(i.accountInfo() + "\n")
