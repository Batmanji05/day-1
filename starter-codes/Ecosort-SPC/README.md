# EcoSort — Smart Waste Segregation Assistant

EcoSort is a rule-based "AI-style" command-line assistant built during
Solarpunk Corps (SPC)'s Foundation Program. It classifies waste items into
Biodegradable, Recyclable, Hazardous, or E-waste, and gives disposal tips —
while keeping a session log of everything sorted.

## Features
- Instant classification of common waste items
- Friendly emoji-based category output
- Session summary with percentage breakdown
- Persistent CSV logging across runs

## How to Run
1. Make sure Python 3 is installed.
2. Clone this repository:
   git clone https://github.com/<your-username>/<repo-name>.git
3. Run the program:
   python ecosort.py
4. Type a waste item name, or type `done` to see your session summary.

## Example
Input:  plastic bottle
Output: ♻️ Category: Recyclable — "Rinse it out before placing in the recycling bin."

## Tech Used
- Python 3 (standard library only — no external dependencies)

## Built By
[Your Name] — Solarpunk Corps, Week 2 Foundation Program

## Future Improvements
- Real ML-based text classification
- Camera-based waste detection (OpenCV)
- Integration with a robotic sorting arm
