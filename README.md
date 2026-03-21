# 👨‍🍳 Flavortown CLI Problem Solver

**A technical logic puzzle engine built with zero hardware, 100% curiosity.**

This project started as a challenge: **Can I build a modular, AI-integrated application using only a smartphone?** Developed entirely on Android via **Termux** and **Acode**, this CLI tool is a tribute to the idea that you don't need a $2000 MacBook to write meaningful code.

## 🛠️ Features
- **Rich Interface:** Styled panels, status spinners, and tables using the `rich` library.
- **Dynamic AI Quizzes:** Generate fresh questions on any CS topic (Data Structures, OS, etc.) via Gemini 1.5 Flash.
- **Zero-Dependency AI:** Custom REST wrapper using `urllib` to bypass heavy Google libraries that won't compile on mobile/Termux environments.
- **Hall of Fame:** Local score persistence using JSON.
- **AI Assist:** Real-time hints and "Live Explanations" if you get stuck.

## 🚦 Getting Started

1. **Clone and Install:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API Key (Optional but recommended for AI features):**
   ```bash
   export GOOGLE_API_KEY="your_key_here"
   ```

3. **Run the Engine:**
   ```bash
   python main.py
   ```

## 🧠 Technical Deep Dive
- **The "Termux Workaround":** Most AI SDKs require `grpcio`, which needs a complex C++/Rust toolchain to compile. I bypassed this by implementing a raw HTTP/REST bridge to Google's Generative Language API, making this project run instantly on any Python 3 environment.
- **Persistence:** Custom JSON handlers for both the static question bank (50+ questions) and the user scoring system.

## 🔗 Project Links
- **Flavortown Entry:** [Project 9514](https://flavortown.hackclub.com/projects/9514)

---
*Built with 🧡 and a lot of screen-scrolling on a 6-inch display.*
