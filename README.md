# Justin - Voice-Activated Virtual Assistant 

**Justin** is a Python-based voice assistant designed to perform tasks like web browsing, playing music and answering user queries using **Google Gemini AI**. Think of him as your personal AI assistant, similar to Alexa or Google Assistant.  

---

## Features 

- **Voice Recognition**  
  - Uses the `speech_recognition` library to listen and recognize your commands.  
  - Activates when you say the wake word `"Justin"`.  

- **Text-to-Speech**  
  - Converts text to speech using `pyttsx3` for local output.  
  - Can be customized for speed and voice tone.  

- **Web Browsing**  
  - Opens popular websites like Google, YouTube, and LinkedIn with your voice.  

- **Music Playback**  
  - Plays songs via a custom `MusicLibrary` module using web links.  

- **AI Integration**  
  - Handles complex queries and generates responses using **Google Gemini AI**.  
  - Acts as a general-purpose assistant, responding like Alexa or Google Assistant.  

---

## How It Works 🛠

1. **Initialization**  
   - Justin starts with: `"Initializing Justin...."`  

2. **Wake Word Detection**  
   - Listens for `"Justin"`  
   - Acknowledges activation by saying `"Yes Master.."`  

3. **Command Processing**  
   - Determines the user’s intent:  
     - Open websites  
     - Play music  
     - Fetch news  
     - Generate AI responses  

4. **Speech Output**  
   - Provides responses using the `speak` function with `pyttsx3`.  

---

## Libraries Used 

- `speech_recognition` – For voice recognition  
- `pyttsx3` – For text-to-speech  
- `webbrowser` – To open websites  
- `MusicLibrary` – Custom module for songs  
- `os` – File handling  
- `google-genai` – Google Gemini API integration  

---

git clone https://github.com/yourusername/Justin-AI-Assistant.git
cd Justin-AI-Assistant
