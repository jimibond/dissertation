#include <SPI.h> // Serial perhipal Interface - to talk to the target
#include <SD.h> // SD Card

const int chipSelect = BUILTIN_SDCARD;  // SD card chip select pin
String userInput;

// Setup code 
void setup() {

  //unsigned long startTime; // used for measuring reponses

  // Setup serial comms with baud rate of 9600
  Serial.begin(9600);

  // Wait 10ms for serial connection to come up
  while (!Serial) {
    delay(10);
  }

  // Initialize the SD card, exit if it fails
  if (!SD.begin(chipSelect)) {
    Serial.println("SD card initialization failed!");
    return;
  }

  // test to see howlong it takes to open and cloase a file 
  //startTime = micros();
  //File file = SD.open("medallists.txt");  // Open the file for reading
  //if (file) { // if it's open close it
  //  file.close();
  //  Serial.println(micros() - startTime);
  //} else {
  //  Serial.println("Error opening file");
  //}

  // Test to for accuraccy, read in questions from a file
  //test_read_file();
  //Serial.println("Testing finished");

  Serial.println("SD card initialized.");  
  Serial.println("I can answer questions about the Olympics in Paris 2024");
}
//  this  just carries on running
void loop() {

  unsigned long startTime;  // used for measuring reponses

  // if we've read something in, we can try and answer teh question
  if (Serial.available() > 0) {
    userInput = Serial.readStringUntil('\n'); // read upto newline

    // Remove trailing newline characters
    userInput.trim();
    
    // Convert input to lowercase for easier matching
    userInput.toLowerCase();

    // find how long it takes to return an answer
    startTime = micros();

    //delay(5000); 

    // Find the response in the file
    String response = findFile(userInput);

    // Print the response or a default message
    if (response != "") {
      Serial.println(response);
      Serial.println(micros() - startTime);
      //display_freeram();
    } else {
      Serial.println("I'm not sure how to respond to that.");
    }
  }
}
// look for unique string in question to see what file needs to be opened
String findFile(String question) {

  Serial.println(question);

  if(question.substring(4,7) == "won")
  {
    return findResponse(question, "medallists.txt"); 
  }
  else if(question.substring(0,4) == "tell")
  {
    //display_freeram();
    return findResponse(question, "athletes.txt"); 
  }
  else if(question.substring(0,5) == "coach")
  {
    return findResponse(question, "coaches.txt"); 
  }

  Serial.println("Error: No File");
  return "";
}
// Function to find the response from the file
String findResponse(String question, String fileName) {

  File file = SD.open(fileName.c_str());  // Open the file for reading
  if (!file) {
    Serial.println("Error opening file.");
    return "";
  }
  
  String line;
  while (file.available()) {
    line = file.readStringUntil('\n');  // Read each line
    line.trim();  // Remove extra whitespace
    
    // Split the line into question and answer with '=' as the separator
    int separatorIndex = line.indexOf('=');
    if (separatorIndex == -1) {
      Serial.println("No Separator");
      continue;  // If no separator, skip the line
    }
    
    String fileQuestion = line.substring(0, separatorIndex);  // question from file
    String fileAnswer = line.substring(separatorIndex + 1);   // answer from file
    
    fileQuestion.trim();
    fileAnswer.trim();

    //display_freeram();

    // do we have a match
    if (fileQuestion.equalsIgnoreCase(question)) {
      file.close();  // Close the file before returning
      return fileAnswer;  // Return the corresponding answer
    }
  }
  
  file.close();
  return "";  // Return empty string if no match found
}
// read in questions from file and save answers in a file to test for accuracy 
void test_read_file(void)
{
  unsigned int count = 11113;
  File infile = SD.open("athletes_question.txt");  // Open the file for reading
  File outfile = SD.open("athletes_answers_chatbot.txt", FILE_WRITE);  // Open the file for writing
  if (!infile) {
    Serial.println("Error opening input file.");
  }
    if (!outfile) {
    Serial.println("Error opening output file.");
  }

  String line;
  while (infile.available() && count != 0) {
    line = infile.readStringUntil('\n');  // Read each line
    line.trim();  // Remove extra whitespace
    line.toLowerCase();

    String response = findFile(line);
    outfile.println(response);
    Serial.println(response);
    count--;
    Serial.println(count);
  }

  infile.close();
  outfile.close();
}

// Read memory usage dynamically
extern "C" char* sbrk(int incr);

void display_freeram(){
  Serial.print(F("- SRAM left: "));
  Serial.println(freeRam());
}

int freeRam() {
  char top;
  return &top - reinterpret_cast<char*>(sbrk(0));
}