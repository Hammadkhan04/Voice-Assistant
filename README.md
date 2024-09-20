# Speech Recognition and Text-to-Speech Program

This program uses `speech_recognition` and `pyttsx3` libraries to create a simple voice assistant. The assistant can listen to voice commands and respond using text-to-speech.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- Microphone

## Installation

1. Install Python 3.x from the official [Python website](https://www.python.org/).

2. Install the required libraries using pip:

    ```sh
    pip install speechrecognition pyttsx3
    ```

3. Ensure you have a working microphone connected to your system.

## Usage

1. Run the program:

    ```sh
    python script_name.py
    ```

2. The program will greet you and ask how it can help you.

3. You can interact with the program using the following commands:
   - "Hello" - The program will greet you back.
   - "Tell me about you" - The program will respond with a brief description of itself.
   - "Exit" or "Quit" - The program will say goodbye and exit.

## Code Overview

The main components of the code are:

1. **speak(text)**: This function takes a string `text` as input and converts it to speech using the `pyttsx3` library.

2. **listen()**: This function listens to audio input from the microphone and uses Google's speech recognition service to convert it to text.

3. **main()**: The main function that controls the program flow. It uses the `speak` and `listen` functions to interact with the user based on the recognized commands.

## Error Handling

- If the speech recognition service does not understand the command, it will inform the user.
- If there is a network issue when using Google's speech recognition service, it will notify the user to check the network connection.

## Additional Notes

- The program checks for the `distutils` module and attempts to install `setuptools` if it's missing.
- Ensure your microphone is working and correctly configured for the program to recognize your voice commands.

## License

This project is licensed under the MIT License.
