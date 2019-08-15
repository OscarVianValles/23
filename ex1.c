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

void readFile(char* fileName, char text[][CHARACTER_LIMIT], document* doc, query* quer);
int initWord(word*);
int initSentence(sentence*);
int initDocument(document* doc);
int printWord(word);
int printSentence(sentence s);
int getWords(sentence*, char*);
int getSentences(paragraph*, char*);
int appendWord(sentence*, word*);

int main(int argc, char *argv[]){

  // //Initialize Document

  // //Intializing Text
  // char text[PARAGRAPH_LIMIT][CHARACTER_LIMIT];

  // //Initializing main document variables
  // query *quer = malloc(sizeof(query));
  // document *doc = malloc(sizeof(document));

  // //Reading from file
  // readFile(argv[1], text, doc, quer);
  char s[1000] = "the quick brown fox jumped. over the lazy dog. a lot of lazy dogs jumped. a lot.";
  paragraph *newParagraph = malloc(sizeof(paragraph));
  getSentences(newParagraph, s);
  return 0;
}

// INITIALIZING FUNCTIONS

// initialize word data
int initWord(word *w) {
    w->data = NULL;
    return 1;
}

// initialize sentence data
int initSentence(sentence *s) {
    s->word_count = 0;
    s->data = NULL;
    return 1;
}

// initialize the document
int initDocument(document *doc){
    doc->data = NULL;
}

//MAIN FUNCTIONS

// Reads the files, saving the number of paragraphs and queries to their respictive structs.
// Also saves the text that needs to be tokenized
void readFile(char* fileName, char text[][CHARACTER_LIMIT], document* doc, query* quer){
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
      doc->paragraph_count = paragraphCount;
    }

    //Gets the paragraph strings
    else if (paragraphCount > 0) {
      strcpy(text[counter++], buffer);
      paragraphCount--;
    }

    //If paragraph count is 0, this means that the following line is now the queries
    else if (paragraphCount == 0 && queryCount == -1){
      queryCount = atoi(buffer);
      quer->query_count = queryCount;
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
  quer->data = queries;

  //Closes file
  fclose(fp);
}

// PRINTING FUNCTIONS
int printWord(word w) {
    // prints word
    printf("%s\n", w.data);
    return 1;
}

int printSentence(sentence s){
  for(int i = 0; i < s.word_count; i++){
    printf("%s\n", s.data[i].data);
  }
}

// APPENDING FUNCTIONS

// Appends words to the current sentence being modified
int appendWord(sentence* s, word* w) {
    //Allocating new memory for the words arrays if the number of words currently in the struct is 1 less than the maximum it can hold.
    if(s->word_count+1 % 10 == 0 || s->word_count == 0){
      word *words = malloc(sizeof(w) * (s->word_count + 10));

      //Copying current data found in s->data

      if(s->data != NULL){
        memcpy(words, s->data, (sizeof(word) * s->word_count));

        //Freeing current data
        free(s->data);
      }

      //Connecting the new pointer to the struct
      s->data = words;
    }

    //Adding the new word to the list
    s->data[s->word_count++] = *w;
    return 1;
}

// GETTING FUNCTIONS

// Gets each individual word to form a sentence
int getWords(sentence* s, char* arr) {
    //Variable to store tokenized data
    char* tok;

    // tokenizing process start
    tok = strtok(arr, " ");

    while(tok != NULL) {

        //Catch to prevent segfault
        if(tok != NULL){

          // Creating new word pointer and new data pointer to survive after the end of the function;
          char *newData = malloc(sizeof(char) * strlen(tok));
          word *newWord = malloc(sizeof(word));

          //Initializing data
          initWord(newWord);

          // Copy the data from the tokenized string and add it to the new word
          strcpy(newData, tok);
          newWord->data = newData;

          // append word to sentence
          appendWord(s, newWord);
        }

        // Continue tokenizing
        tok = strtok(NULL, " ");
    }

    return 1;
}

// Gets each sentence that is separated by a . or the end of the line
int getSentences(paragraph* s, char* arr){
  // Variable to store tokenized data
  char* tok;

  // tokenizing process start
  tok = strtok(arr, ".");

  while(tok != NULL) {
    //Catch to prevent segfault
    if(tok != NULL){

      // Creating new sentence pointer and new data pointer to survive after the end of the function;
      sentence *newSentence = malloc(sizeof(sentence));

      //Initializing data
      initSentence(newSentence);

      printf("tok: %s\n", tok);
      //Getting individual words to form the sentence
      getWords(newSentence, tok);
      printSentence(*newSentence);
    }

    // Continue tokenizing
    tok = strtok(NULL, ".");
    printf("tok: %s", tok);
  }

    return 1;
}
