#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

int initWord(word*);
int initSentence(sentence*);
int printWord(word);
int getWords(sentence*, char*);
int appendWord(sentence*, word*);
void addWordCount(sentence*);

int main(){

    // Sentence to Words Sample
    // char s[10000] = "hello there people";
    // sentence *newSentence = malloc(sizeof(char)*strlen(s));

    // initSentence(newSentence);
    // getWords(newSentence, s);

    return 0;
}

int initWord(word *w) {
    w->data = NULL; 
    return 1;
}

int initSentence(sentence *s) {
    s->word_count = 0;
    s->data = NULL;
    return 1;
}

int printWord(word w) {
    printf("%s\n", w.data);
    return 1;
}

int appendWord(sentence *s, word *w) {
    word *tmp = malloc(sizeof(char) * strlen(w->data));
    int i;

    for(i = 0; i < s->word_count; i++)
        tmp[i] = s->data[i];

    free(s->data);

    s->data = malloc(100 * s->word_count);
    
    if(s->data==NULL)
        return 0;
    else {
        for(i = 0; i<s->word_count; i++)
            s->data[i] = tmp[i];
        s->data[s->word_count++] = *w;

        free(tmp);

        return 1;
    }

    return 1;
}

int getWords(sentence *s, char *arr) {
    word *newWord = malloc(sizeof(char) * strlen(arr));
    char *tok;

    initWord(newWord);

    tok = strtok(arr, " ");

    while(tok != NULL) {
        newWord->data = tok;
        appendWord(s, newWord);
        tok = strtok(NULL, " ");
    }

    for(int i = 0; i < s->word_count; i++) {
        printWord(s->data[i]);
    }

    return 1;
}