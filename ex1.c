#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define QUERY_LIMIT 1000
#define BUFFER_LIMIT 2000
#define CHARACTER_LIMIT 1000
#define PARAGRAPH_LIMIT 5

typedef struct {
  char *data;
} word;

typedef struct {
  word *data;
  int word_count;
} sentence;

typedef struct {
  sentence *data;
  int sentence_count;
} paragraph;

typedef struct {
  paragraph *data;
  int paragraph_count;
} document;

typedef struct {
  char **data;
  int query_count;
} query;

void readFile(char *, char text[][CHARACTER_LIMIT], document *, query *);

int initWord(word *);
int initSentence(sentence *);
int initParagraph(paragraph *);
int initDocument(document *);
int initQuery(query *);

int printWord(word);
int printSentence(sentence);
int printParagraph(paragraph);

int getWords(sentence *, char *);
int getSentences(paragraph *, char *);
int getParagraphs(document *, char text[][CHARACTER_LIMIT]);

int appendWord(sentence *, word);
int appendSentence(paragraph *, sentence);
int appendParagraph(document *, paragraph);

int freeDocument(document *);
int freeParagraph(paragraph);
int freeSentence(sentence);
int freeWord(word);

paragraph *findParagraph(document,int);
sentence *findSentence(document,int, int);
word *findWord(document, int, int, int);

int main(int argc, char *argv[]) {

  // Initialize Document

  // Intializing Text
  char text[PARAGRAPH_LIMIT][CHARACTER_LIMIT];

  // Initializing main document variables
  query *quer = malloc(sizeof(query));
  document *doc = malloc(sizeof(document));

  initQuery(quer);
  initDocument(doc);

  // Reading from file
  readFile(argv[1], text, doc, quer);

  // paragraph *p = malloc(sizeof(paragraph));

  // char text2[][1000] = {{"asdfasdf. asdfasdfklaj;sdfl. laksdj;laksd."},
  // {"asdfasdf. asdfasdfklaj;sdfl. laksdj;laksd."}, {"asdfasdf.
  // asdfasdfklaj;sdfl. laksdj;laksd."}}; getParagraphs(doc, text2);

  getParagraphs(doc, text);
  free(quer);
  freeDocument(doc);
  free(doc);

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

int initParagraph(paragraph *p) {
  p->sentence_count = 0;
  p->data = NULL;
  return 1;
}

// initialize the document
int initDocument(document *doc) {
  doc->data = NULL;
  doc->paragraph_count = 0;
  return 1;
}

int initQuery(query *quer) {
  quer->data = NULL;
  quer->query_count = 0;
  return 1;
}

// MAIN FUNCTIONS

// Reads the files, saving the number of paragraphs and queries to their
// respictive structs. Also saves the text that needs to be tokenized
void readFile(char *fileName, char text[][CHARACTER_LIMIT], document *doc,
              query *quer) {
  // Initializing variables
  char buffer[2000] = {0};
  char **queries;

  // Opening File
  FILE *fp;
  fp = fopen(fileName, "r");

  // Error Checking
  if (fp == NULL) {
    perror("Error opening file");
    return;
  }

  // Parsing through the file
  int paragraphCount = -1, queryCount = -1, counter = 0;
  while (fgets(buffer, BUFFER_LIMIT, fp) != NULL) {

    // Gets the number of paragraphs on the first loop
    if (paragraphCount == -1) {
      paragraphCount = atoi(buffer);
      doc->paragraph_count = paragraphCount;
    }

    // Gets the paragraph strings
    else if (paragraphCount > 0) {
      strcpy(text[counter++], buffer);
      paragraphCount--;
    }

    // If paragraph count is 0, this means that the following line is now the
    // queries
    else if (paragraphCount == 0 && queryCount == -1) {
      queryCount = atoi(buffer);
      quer->query_count = queryCount;
      counter = 0;
      queries = malloc(queryCount * sizeof(char *));
      for (int i = 0; i < queryCount; i++) {
        queries[i] = malloc((CHARACTER_LIMIT) * sizeof(char));
      }
    }

    // Save the queries to a temporary holder
    else if (queryCount > 0) {
      strcpy(queries[counter++], buffer);
      queryCount--;
    }
  }

  // Save the queries to the struct
  quer->data = queries;

  char *tok;
  char *rest = *queries;

  for(int j = 0; j < quer->query_count; j++) {

    tok = strtok_r(queries[j], " ", &rest);

    int count = 0;
    int queryArray[4] = {0};

    while (tok != NULL) {

      if (tok != NULL)
        queryArray[count++] = atoi(tok);

      tok = strtok_r(NULL, " ", &rest);
      count++;
    }

    switch(queryArray[0]) {
      case 1:
        printParagraph(*findParagraph(*doc, queryArray[1]));
        break;
      case 2:
        printSentence(*findSentence(*doc, queryArray[1], queryArray[2]));
        break;
      case 3:
        printWord(*findWord(*doc, queryArray[1], queryArray[2], queryArray[3]));
        break;
    }
  }

  // Closes file
  fclose(fp);
}

// PRINTING FUNCTIONS
int printWord(word w) {
  // printf("%s", w.data);
  printf("word");
  return 1;
}

int printSentence(sentence s) {
  // for (int i = 0; i < s.word_count; i++) {
  //   printf("%s", s.data[i].data);
  // }
  printf("sentence");
  return 1;
}

int printParagraph(paragraph p) {
  // for (int i = 0; i < p.sentence_count; i++) {
  //   printSentence((p.data[i]));
  // }
  printf("paragraph");
  return 1;
}

// APPENDING FUNCTIONS

// Appends words to the current sentence being modified
int appendWord(sentence *s, word w) {
  // Allocating new memory for the words arrays if the number of words currently
  // in the struct is 1 less than the maximum it can hold.
  if (s->word_count + 1 % 10 == 0 || s->word_count == 0) {

    // creating the new pointer;
    word *words;
    // Handle the first creation of the sentences;

    if (s->word_count == 0) {
      words = malloc(sizeof(word *) * (s->word_count + 10));
    }

    // Since the check will be true if the word_count will end in 9, ie 19 or
    // 29, the additional memory ssaces to be added will be 11 to make it a
    // round number;
    else {
      words = malloc(sizeof(word *) * (s->word_count + 11));
    }

    // Copying current data found in s->data
    if (s->data != NULL) {
      memcpy(words, s->data, (sizeof(word *) * s->word_count));

      // Freeing current data
      free(s->data);
    }

    // Connecting the new pointer to the struct
    s->data = words;
  }

  // Adding the new word to the list
  s->data[s->word_count++] = w;
  return 1;
}

int appendSentence(paragraph *p, sentence s) {
  // Allocating new memory for the sentence arrays if the number of sentences
  // currently in the struct is 1 less than the maximum it can hold.
  if (p->sentence_count + 1 % 10 == 0 || p->sentence_count == 0) {

    // Creating the new pointer
    sentence *sentences;

    // Handle the first creation of the sentences;
    if (p->sentence_count == 0) {
      sentences = malloc(sizeof(sentence *) * (p->sentence_count + 10));
    }

    // Since the check will be true if the sentence_count will end in 9, ie 19
    // or 29, the additional memory spaces to be added will be 11 to make it a
    // round number;
    else {
      sentences = malloc(sizeof(sentence *) * (p->sentence_count + 11));
    }

    // Copying current data found in p->data

    if (p->data != NULL) {
      memcpy(sentences, p->data, (sizeof(sentence *) * p->sentence_count));

      // Freeing current data
      free(p->data);
    }

    // Connecting the new pointer to the struct
    p->data = sentences;
  }

  // Adding the new word to the list
  p->data[p->sentence_count++] = s;
  return 1;
}

int appendParagraph(document *doc, paragraph p) {
  // Allocate max memory for paragraph if first run
  if (doc->data == NULL) {
    paragraph *paragraphs = malloc(sizeof(paragraph) * PARAGRAPH_LIMIT);
    doc->data = paragraphs;
  }

  doc->data[doc->paragraph_count++] = p;

  return 1;
}

// GETTING FUNCTIONS

// Gets each individual word to form a sentence
int getWords(sentence *s, char *arr) {

  // Variable to store tokenized data
  char *tok;
  char *rest = arr;

  // tokenizing process start
  tok = strtok_r(arr, " ", &rest);

  while (tok != NULL) {

    // Catch to prevent segfault
    if (tok != NULL) {

      // Creating new word pointer and new data pointer to survive after the
      // end of the function;
      char *newData = malloc(sizeof(char) * (strlen(tok) + 1));

      word newWord;
      initWord(&newWord);

      // Initializing data

      // Copy the data from the tokenized string and add it to the new word
      strcpy(newData, tok);
      newWord.data = newData;

      // append word to sentence
      appendWord(s, newWord);
    }

    // Continue tokenizing
    tok = strtok_r(NULL, " ", &rest);
  }

  return 1;
}

// Gets each sentence that is separated by a . or the end of the line
int getSentences(paragraph *p, char *arr) {
  // Variable to store tokenized data
  char *tok;
  char *rest = arr;

  // tokenizing process start
  tok = strtok_r(arr, ".", &rest);

  while (tok != NULL) {
    // Catch to prevent segfault
    if (tok != NULL) {

      // Creating new sentence pointer to survive after the end of the
      // function;
      sentence newSentence;

      // Initializing data
      initSentence(&newSentence);

      // Getting individual words to form the sentence
      getWords(&newSentence, tok);

      // printSentence(*newSentence);

      // Appending sentences to the paragraphs
      appendSentence(p, newSentence);
    }

    // Continue tokenizing
    tok = strtok_r(NULL, ".", &rest);
  }

  return 1;
}

int getParagraphs(document *doc, char text[][CHARACTER_LIMIT]) {

  int paragraphCount = doc->paragraph_count;
  doc->paragraph_count = 0;
  // Looping through all available paragraphs gathered from reading the file
  for (int i = 0; i < paragraphCount; i++) {

    // Creating new paragraph pointer that will survive after the end of the
    // function
    paragraph newParagraph;

    // Initializing data
    initParagraph(&newParagraph);

    // Getting individual sentences. Since the structure of the text from
    // reading the file is already separated by \n, there is no need to
    // tokenize it anymore
    getSentences(&newParagraph, text[i]);

    // printParagraph(newParagraph);

    // Appending paragraphs to document
    appendParagraph(doc, newParagraph);
  }

  return 1;
}

// FREE FUNCTIIONS
int freeDocument(document *doc) {
  for (int i = 0; i < doc->paragraph_count; i++) {
    freeParagraph(doc->data[i]);
  }

  free(doc->data);
  return 1;
}

int freeParagraph(paragraph p) {
  for (int i = 0; i < p.sentence_count; i++) {
    freeSentence(p.data[i]);
  }

  free(p.data);
  return 1;
}

int freeSentence(sentence s) {
  for (int i = 0; i < s.word_count; i++) {
    freeWord(s.data[i]);
  }

  free(s.data);
  return 1;
};

int freeWord(word w) {
  free(w.data);
  return 1;
}

paragraph *findParagraph(document doc, int k) {
  return &doc.data[k];
}

sentence *findSentence(document doc, int k, int m) {
  return &doc.data[k].data[m];
}

word *findWord(document doc, int k, int m, int n) {
  return &doc.data[k].data[m].data[n];
}