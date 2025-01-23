# Coursera Alert 

This project is a Python script that monitors the active Google Chrome tab and alerts the user when a reading/assignment is detected. It uses a buzzer sound to notify the user.

## Features

- Monitors the active Google Chrome tab.
- Detects specific URL patterns related to Coursera assignments and readings.
- Plays a buzzer sound to alert the user.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Coursera-alert-python.git
   cd Coursera-alert-python
   ```
2. Install the required libraries using [requirements.txt](requirements.txt):
   ```sh
   pip install -r requirements.txt
   ```
## Usage
Run the script:
```sh
python coursera_alert.py
```
The script will continuously monitor the active Google Chrome tab. If it detects a URL containing "supplement" or "assignment-submission", it will play a buzzer sound. Type 'stop' in the terminal to stop the buzzer.
   

