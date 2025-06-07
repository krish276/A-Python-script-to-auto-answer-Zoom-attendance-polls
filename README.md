# Zoom Attendance Automator

A Python script to automatically answer Zoom attendance polls by detecting the poll pop‑up and using keyboard navigation to select “Yes” and submit.

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Troubleshooting](#troubleshooting)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* Detects Zoom poll windows titled `Polls/Quizzes`
* Uses pure keyboard navigation (no image templates required)
* Configurable start delay and poll‑check interval
* Simple, single‑file script for easy customization
* Checks the poll heading text contains "attendance" before answering

## Prerequisites

* **Operating System:** Windows
* **Zoom Desktop App** installed and signed in
* **Python 3.8+**
* **pip** package manager

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/zoom-attendance-automator.git
   cd zoom-attendance-automator
   ```
2. **(Optional) Create & activate a virtual environment**

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate    # On Windows PowerShell
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start your Zoom meeting.**
2. **Run the script** from the project folder:

   ```bash
   python zoom_attendance_automator.py
   ```
3. **Switch to Zoom** within the initial delay (default 5 s).
4. The script will check every 5 s and automatically answer each poll.
5. **Stop** at any time with `Ctrl+C` in the terminal.

## Configuration

All settings live at the top of `zoom_attendance_automator.py`:

```python
DELAY_BEFORE_START   = 5            # Seconds before automation begins
POLL_CHECK_INTERVAL  = 5            # Seconds between each poll scan
tabs_to_radio       = 3            # Tab presses to focus the first radio button
tabs_to_submit      = 2            # Tab presses from radio to Submit button
POLL_WINDOW_REGEX   = 'Polls/Quizzes'  # Regex to match Zoom poll window title
HEADING_KEYWORD     = 'attendance'    # Text expected in the poll heading
```

Adjust these values as needed to match your screen layout and Zoom version.

## Troubleshooting

* **No polls answered?**

  * Verify your Zoom poll window title includes “Polls/Quizzes” or update `POLL_WINDOW_REGEX`.
  * Ensure the script has permission to control your keyboard (run as Admin if necessary).
* **Wrong focus?**

  * Increase initial delay (`DELAY_BEFORE_START`) to give yourself time to click into Zoom.
  * Adjust `tabs_to_radio` and `tabs_to_submit` if Zoom’s UI differs slightly.

## Contributing

1. **Fork** the repo
2. Create a **feature branch** (`git checkout -b feature/your-feature`)
3. **Commit** your changes (`git commit -m 'Add feature'`)
4. **Push** to your branch (`git push origin feature/your-feature`)
5. Open a **Pull Request** on GitHub

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
