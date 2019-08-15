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

typedef struct {
  char* data;
} query;

void readFile(char* fileName, char* buffer, paragraph* docParagraphs);
// void initializeQueries(query *docQuery);

int main(int argc, char *argv[]){

  //Initialize Document
  query docQuery[QUERY_LIMIT];
  document myDoc;
  paragraph docParagraphs[PARAGRAPH_LIMIT];
  char buffer[2000] = {0};
  readFile(argv[1], buffer, docParagraphs);

  return 0;
}

/* void initializeQueries(query *docQuery){
  for(int i = 0; i < QUERY_LIMIT; i++){
  }
}
*/

void readFile(char* fileName, char* buffer, paragraph* docParagraphs){

  //Opening File
  FILE *fp;
  fp = fopen(fileName, "r");

  //Error Checking
  if(fp == NULL){
    perror("Error opening file");
    return;
  }

  int counter = -1, paragraphCounter = 0;
  while (fgets(buffer, BUFFER_LIMIT, fp) != NULL) {
    if(counter == -1){
      counter = atoi(buffer);
    } else if (counter > 0) {
      docParagraphs[paragraphCounter++] =

    }
  }

  //Closes file
  fclose(fp);
}
