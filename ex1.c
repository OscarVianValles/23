#include <stdio.h>
#include <string.h>

typedef struct {
    char* data;
} word;

typedef struct {
    word* data;
    int word_count;//the number of words in a sentence
} sentence;

typedef struct {
    sentence* data  ;
    int sentence_count;//the number of sentences in a paragraph
} paragraph;

typedef struct {
    paragraph* data;
    int paragraph_count;//the number of paragraphs in document
} document;

int getWords(sentence*, char*);
int appendWord(sentence*, word*);
void addWordCount(sentence*);

int main(){

    char s[10000] = "hello there people";
    sentence *newSentence;

    getWords(newSentence, s);

    return 0;
}

int appendWord(sentence *s, word *w) {
    s->word_count++;
    strcpy(s->data->data, w->data);

    return 1;
}

int getWords(sentence *s, char *arr) {
    char *tok;
    word *newWord;

    tok = strtok(arr, " ");

    while(tok != NULL) {
        printf("%s\n", tok);
        newWord->data = tok;
        appendWord(s, newWord);
        tok = strtok(NULL, " ");
    }
    
    return 1;
}