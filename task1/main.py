import argparse
from pathlib import Path

from sorter import copy_and_sort_files

def parse_args():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("destination", type=str, nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def main():
    args = parse_args()
    source_path = Path(args.source)
    destination_path = Path(args.destination)

    if not source_path.exists() or not source_path.is_dir():
        print(f"Помилка: Вихідна директорія '{source_path}' не існує або не є директорією.")
        return

    copy_and_sort_files(source_path, destination_path)
    print(f"Сортування завершено. Файли збережено у '{destination_path}'.")

if __name__ == "__main__":
    main()
