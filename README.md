# Flavortown CLI Problem Solver v3.1

A modern, terminal-based competitive programming companion. Developed entirely on Android via Termux.

## Features
- **Local DB Mode**: 50+ hand-picked technical questions stored locally.
- **AI Brain Engine**: Real-time problem generation powered by **Gemini 3.1 Flash Lite Preview**.
- **AI Assist**: Context-aware analysis of user mistakes.
- **Hall of Fame**: Local ranking persistence.
- **ANSI Cyber-Neon UI**: High-contrast, interactive CLI built with `rich`.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
To enable AI features (Mode 2 and AI Assist), you must set your Gemini API key in the environment:
```bash
export GOOGLE_API_KEY='your_api_key_here'
```
*Note: If the key is not set, the app will gracefully report a connection failure for AI-dependent modes.*

## Usage
Run the main entry point:
```bash
python main.py
```

## Project Architecture
- `main.py`: Entry point.
- `src/ui.py`: Interactive terminal components.
- `src/ai_generator.py`: REST-based Gemini API integration.
- `src/quiz.py`: Core session logic.
- `src/scoring.py`: Ranking persistence.
- `data/`: Local database storage.
