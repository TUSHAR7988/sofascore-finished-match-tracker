# SofaScore Finished Match Scraper

## Overview
This project monitors SofaScore football events and detects newly finished matches
within seconds of completion. Each finished match is saved as a standalone JSON file.

## Features
- Async Playwright-based session handling
- Automatic finished match detection
- JSON-only output
- Low CPU & RAM usage
- Semaphore-controlled concurrency
- Runs continuously (24/7)

## Requirements
- Python 3.11+
- Playwright (Chromium)

## ▶️ How it works

1. Launches a Playwright Chromium browser
2. Establishes a valid SofaScore session
3. Polls football event APIs periodically
4. Filters finished matches
5. Writes new matches to JSON

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
