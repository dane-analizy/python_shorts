import random
import sys
import time

import pyautogui


def simulate_typing(text, delay=0.1):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.randint(1, 3) / 10)


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Błąd podczas odczytu pliku: {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Użycie: python script.py <ścieżka_do_pliku>")
        sys.exit(1)

    file_path = sys.argv[1]

    content = read_file(file_path)

    print("Przygotuj się! Symulacja rozpocznie się za 5 sekund...")
    print("Upewnij się, że kursor znajduje się w odpowiednim miejscu.")
    time.sleep(5)

    # Symuluj pisanie tekstu
    try:
        simulate_typing(content)
    except Exception as e:
        print(f"Błąd podczas symulacji pisania: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
