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

int main(int argc, char *argv[]){

  //Initialize Document

  //Intializing Text
  char text[PARAGRAPH_LIMIT][CHARACTER_LIMIT];

  //Initializing main document variables
  query *myQuery = malloc(sizeof(query));
  document *myDocument = malloc(sizeof(document));

  //Reading from file
  readFile(argv[1], text, myDocument, myQuery);

  for(int i = 0; i < myQuery->query_count; i++){
    printf("%s", myQuery->data[i]);
  };

  for(int i = 0; i < myQuery->query_count; i++){
    free(myQuery->data[i]);
  }

  free(myQuery);
  free(myDocument);
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
