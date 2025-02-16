# KeyLogger Project

A simple Python keylogger for educational purposes. It captures keystrokes and reports them either via email or saves them to a file.

## Disclaimer
**Important:** This project is intended **only** for educational and research purposes. Use it only on systems you own or have explicit permission to test. Unauthorized use on any system is illegal and unethical.

## Features
- **Keystroke Capture:** Logs every key press, including special keys.
- **Reporting Options:** Choose between email reports or local file storage.
- **Customizable Interval:** Set the reporting interval as needed.

## Requirements
- **Python 3.x**
- **Dependencies:**
  - `keyboard` (Install via `pip install keyboard`)
  - Standard Python libraries: `smtplib`, `threading`, `datetime`, `email`

## Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/KeyLogger.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd keyLogger
   ```
3. **Configure the keylogger:**
   - Open the `keylogger.py` file.
   - Update the `emailUser` and `emailPass` variables if using the email reporting method.
   - Adjust the `reportInterval` variable to set your desired reporting frequency.

## Usage
- **Run the keylogger:**
  ```bash
  python keylogger.py
  ```
- The keylogger will start capturing keystrokes immediately.
- Depending on the configuration, it will either send logs via email or save them as a file in the project directory.
- To stop the keylogger, terminate the script execution (e.g., press `Ctrl+C`).

## Ethical Use
Only use this tool for learning and testing on systems where you have explicit permission. Respect privacy and adhere to all applicable laws and ethical guidelines.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests. Ensure that all contributions align with the ethical guidelines stated above.

## Contact
For any questions, issues, or suggestions, please open an issue in this repository.
```
