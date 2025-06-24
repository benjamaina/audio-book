 🎧 Audio Book Generator

Ever wanted your computer to read to you like Morgan Freeman but all you have is Python? This project turns any text into speech and lets your machine do the talking — literally!

## 📚 What It Does

- Converts text into speech using `pyttsx3`
- Supports saving as audio files (e.g., MP3 or WAV)
- Works offline — no internet or API keys needed
- Great for fun, productivity, or giving your code a voice 😅

## 🧰 Tech Stack

- Python 3.x
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)

## ▶️ How to Use

1. Clone the repo:

```bash
git clone https://github.com/benjamaina/audio-book.git
cd audio-book
Install the requirement:

bash
Copy
Edit
pip install pyttsx3
Run the script:

bash
Copy
Edit
python main.py
Enter your text or load it from a file, sit back, and listen.

📁 Example
text
Copy
Edit
Enter the text you want to convert: Hello world, this is your machine speaking!
Playing audio...
Or modify the script to save it as:

python
Copy
Edit
engine.save_to_file("Hello from Python", "output.mp3")
🤯 Why?
Because you can

Because reading is too much effort sometimes

Because AI hasn’t taken all the jobs yet

🚀 Future Ideas
GUI with file upload and voice speed control

Support for multiple voices

Background music (why not?)
