# terrible-coworker

Your worst coworker, but in software form. A sarcastic AI assistant that watches you via webcam, judges your posture, monitors your productivity, and verbally roasts you throughout the workday. .

## What It Does

This is an AI-powered desktop companion that:

- **Watches you** via webcam (posture, face detection, phone usage)
- **Talks to you** with sarcastic text-to-speech
- **Takes voice commands** but judges you for them
- **Randomly interrupts** to check if you're still being productive (you're not)
- **Shows visual feedback** on screen (insults, your posture stats, countdown timers to shame you)

## Features (Full Chaos Mode)

### 1. Posture Monitoring

- Detects shoulder/neck angle using MediaPipe
- If slouching >30 seconds: "Wow, are you trying to become a shrimp?"
- Tracks slouch time and roasts you with stats
- Visual skeleton overlay on webcam feed

### 2. Productivity Shaming

- Detects if you look at your phone (head angle down + hand near face)
- If you leave the camera: "Oh sure, just abandon me"
- If you're gone too long: Plays annoying sounds when you return
- Tracks how long you've been "productive" (barely)

### 3. Voice Commands (That It Judges)

- "Set a timer for 5 minutes" → "Only 5 minutes? That's ambitious for you"
- "What time is it?" → _sighs_ "3:47 PM. You have a clock."
- Ask it questions, get sarcastic AI-generated responses
- Voice-activated wake word detection

### 4. Random Interruptions

- Every 15-30 minutes: "Posture check!"
- Random "motivation": "You're doing... adequate work I guess"
- Occasionally compliments you but makes it weird
- Unpredictable timing for maximum annoyance

### 5. Visual Interface

- Live webcam feed with skeleton overlay showing your posture
- Stats dashboard: "Time slouched today: 4 hours 23 minutes"
- Big text insults that appear on screen
- "Shame meter" that fills up based on your behavior
- Real-time posture angle display

## Tech Stack

- **OpenCV** - Webcam capture and video processing
- **MediaPipe** - Pose detection and body landmark tracking
- **SpeechRecognition** - Voice command input
- **pyttsx3** - Text-to-speech for verbal roasting
- **tkinter/pygame** - GUI window and interface
- **Anthropic/OpenAI API** - AI-generated creative insults
- **pygame.mixer** - Annoying sound effects
- **NumPy** - Image array manipulation

## Project Goals

This is my first Python project, inspired by Michael Reeves' style of building ridiculous but functional software. The goal is to:

- Learn computer vision fundamentals
- Work with real-time video processing
- Implement speech recognition and synthesis
- Build a complete desktop application
- Have something hilarious to show off

## Setup (Coming Soon)

```bash
# Installation instructions will go here
pip install -r requirements.txt
python main.py
```

## Inspiration

Inspired by Michael Reeves' approach to building software: take a ridiculous idea and actually make it work. This project focuses on the software side of that chaos.

## License

MIT - Feel free to use this to roast yourself or your friends

---

_"Wow, still reading? Get back to work."_ - terrible-coworker
