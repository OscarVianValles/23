#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define QUERY_LIMIT 1000
#define BUFFER_LIMIT 2000
#define CHARACTER_LIMIT 1000
#define PARAGRAPH_LIMIT 5

typedef struct {
    char* data;
} word;

typedef struct {
    word* data;
    int word_count;
} sentence;

typedef struct {
    sentence* data;
    int sentence_count;
} paragraph;

typedef struct {
    paragraph* data;
    int paragraph_count;
} document;

typedef struct {
    char** data;
    int query_count;
} query;

void readFile(char* fileName, char text[][CHARACTER_LIMIT], document* myDocument, query* myQuery);
void initializeDocument(char text[][CHARACTER_LIMIT], document* myDocument);
int initWord(word*);
int initSentence(sentence*);
int printWord(word);
int getWords(sentence*, char*);
int appendWord(sentence*, word*);
void addWordCount(sentence*);

int main(int argc, char *argv[]){

  //Initialize Document

  //Intializing Text
  char text[PARAGRAPH_LIMIT][CHARACTER_LIMIT];

  //Initializing main document variables
  query *myQuery = malloc(sizeof(query));
  document *myDocument = malloc(sizeof(document));

  //Reading from file
  readFile(argv[1], text, myDocument, myQuery);

  //Intializing document from file
  void initializeDocument(text, myDocument);
  return 0;
}

void readFile(char* fileName, char text[][CHARACTER_LIMIT], document* myDocument, query* myQuery){
  //Initializing variables
  char buffer[2000] = {0};
  char** queries;

  //Opening File
  FILE *fp;
  fp = fopen(fileName, "r");

  //Error Checking
  if(fp == NULL){
    perror("Error opening file");
    return;
  }

  //Parsing through the file
  int paragraphCount = -1, queryCount = -1, counter = 0;
  while (fgets(buffer, BUFFER_LIMIT, fp) != NULL) {

    //Gets the number of paragraphs on the first loop
    if(paragraphCount == -1){
      paragraphCount = atoi(buffer);
      myDocument->paragraph_count = paragraphCount;
    }

    //Gets the paragraph strings
    else if (paragraphCount > 0) {
      strcpy(text[counter++], buffer);
      paragraphCount--;
    }

    //If paragraph count is 0, this means that the following line is now the queries
    else if (paragraphCount == 0 && queryCount == -1){
      queryCount = atoi(buffer);
      myQuery->query_count = queryCount;
      counter = 0;
      queries = malloc(queryCount * sizeof(char*));
      for (int i = 0; i < queryCount; i++){
        queries[i] = malloc((CHARACTER_LIMIT) * sizeof(char));
      }
    }

    //Save the queries to a temporary holder
    else if (queryCount > 0){
      strcpy(queries[counter++], buffer);
      queryCount--;
    }
  }

  //Save the queries to the struct
  myQuery->data = queries;

  //Closes file
  fclose(fp);
}

int printWord(word w) {
    // prints word
    printf("%s\n", w.data);
    return 1;
}

int initWord(word *w) {
    // initialize word data
    w->data = NULL;
    return 1;
}

int initSentence(sentence *s) {
    // initialize sentence data
    s->word_count = 0;
    s->data = NULL;
    return 1;
}

int appendWord(sentence *s, word *w) {
    // allocating memory for temporary word
    word *tmp = malloc(sizeof(char) * strlen(w->data));
    int i;

    // ???
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
    // function to extract words out of a sentence
    word *newWord = malloc(sizeof(char) * strlen(arr));
    char *tok;

    // initialize word value
    initWord(newWord);

    // tokenizing process start
    tok = strtok(arr, " ");

    while(tok != NULL) {
        // assign tokenized string to word data
        newWord->data = tok;
        // append word to sentence
        appendWord(s, newWord);
        tok = strtok(NULL, " ");
    }
    // tokenizing process end

    return 1;
}
