# Sound Generator

This program is a simple sound generator that runs in the system tray. It generates a continuous tone based on configurable frequency and volume settings. The settings are stored in a JSON file and can be loaded/modified easily. The generator uses the `sounddevice` library to play sound and `pystray` for the system tray interface.

## Features
- **Customizable Frequency and Volume**: Set the frequency (default: 440 Hz) and volume (default: 50%) using the settings file.
- **System Tray Interface**: The application runs in the system tray with an option to exit the program via the tray menu.
- **Persistent Settings**: Settings are saved to a JSON file (`sound_generator_settings.json`) in your Documents folder for persistence across sessions.
- **Cross-platform**: Works on most major operating systems where `sounddevice` and `pystray` are supported.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sound-generator.git
   cd sound-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python sound_generator.py
   ```

## Usage

- The program runs silently in the system tray and will generate a tone based on the frequency and volume settings.
- Right-click the system tray icon to access the menu and exit the program.

## Configuration

The program reads the settings from a JSON file located in your Documents folder:

- **Frequency**: The frequency of the generated tone in Hertz (default: 440 Hz).
- **Volume**: The volume of the generated tone as a percentage (default: 50%).

You can edit the `sound_generator_settings.json` file manually or implement additional functionality for dynamically adjusting these settings.

## License
MIT License. See `LICENSE` for more details.
