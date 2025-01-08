import os
import json
import numpy as np
import sounddevice as sd
import threading
from pystray import MenuItem as Item, Menu, Icon
from PIL import Image, ImageDraw

# Alapértelmezett beállítások
DEFAULT_SETTINGS = {"frequency": 440, "volume": 50}

# Dokumentumok mappa elérése
def get_settings_file():
    user_docs = os.path.join(os.path.expanduser("~"), "Documents")
    return os.path.join(user_docs, "sound_generator_settings.json")

# Beállítások betöltése
def load_settings():
    settings_file = get_settings_file()
    if os.path.exists(settings_file):
        with open(settings_file, "r") as file:
            return json.load(file)
    else:
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

# Beállítások mentése
def save_settings(settings):
    settings_file = get_settings_file()
    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=4)
    print(f"Beállítások mentve: {settings}")

# Hanggenerátor callback
def audio_callback(outdata, frames, time, status):
    global settings
    frequency = settings["frequency"]
    volume = settings["volume"] / 100
    t = (np.arange(frames) + audio_callback.phase) / 44100
    outdata[:] = (volume * np.sin(2 * np.pi * frequency * t)).reshape(-1, 1)
    audio_callback.phase += frames
audio_callback.phase = 0

# Hang lejátszása
def start_audio():
    global running
    with sd.OutputStream(channels=1, callback=audio_callback, samplerate=44100):
        while running:
            sd.sleep(100)

# Tálcaikon létrehozása
def create_icon():
    # Átlátszó hátterű ikon rajzolása
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Átlátszó háttér
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, width - 8, height - 8), fill="blue", outline="black")
    return image

# Bezárás funkció
def quit_program(icon, item):
    global running
    running = False
    icon.stop()

# Tálcamenü
def setup_tray():
    menu = Menu(
        Item("Kilépés", quit_program),
    )
    icon = Icon("Hang Generátor", create_icon(), "Hang Generátor", menu)
    icon.run()

# Főprogram
if __name__ == "__main__":
    settings = load_settings()
    print(f"Induló beállítások: {settings}")
    running = True

    # Hanggenerálás szál elindítása
    threading.Thread(target=start_audio, daemon=True).start()

    # Tálcaikon megjelenítése
    setup_tray()