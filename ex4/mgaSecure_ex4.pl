female(missScarlet).
female(mrsWhite).
female(mrsPeacock).
female(drOrchid).

male(profPlum).
male(colonelMustard).
male(revGreen).

hates(missScarlet,revGreen).
hates(revGreen,mrsWhite).
hates(mrsWhite,revGreen).
hates(profPlum,mrsWhite).
hates(mrsWhite,profPlum).
hates(colonelMustard,Y) :- female(Y).
hates(colonelMustard,profPlum).

likes(missScarlet,drOrchid).
likes(mrsPeacock,drOrchid).
likes(drOrchid,mrsPeacock).
likes(missScarlet,mrsWhite).
likes(missScarlet,profPlum).
likes(profPlum,missScarlet).
likes(profPlum,X) :- hates(colonelMustard,X).
likes(drOrchid,X) :- likes(X,drOrchid).
    
enemies(X,Y) :- hates(X,Y), hates(Y,X).
friends(X,Y) :- likes(X,Y), likes(Y,X). 
friends(X,Y) :- enemies(X,Z), enemies(Z,Y).