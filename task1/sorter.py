import shutil
from pathlib import Path

def copy_and_sort_files(src_dir: Path, dst_dir: Path):
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для піддиректорії
                copy_and_sort_files(item, dst_dir)
            elif item.is_file():
                # Отримуємо розширення файлу (без крапки) або 'no_extension'
                extension = item.suffix[1:] if item.suffix else "no_extension"
                target_dir = dst_dir / extension
                target_dir.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(item, target_dir / item.name)
                except Exception as error:
                    print(f"Помилка копіювання {item}: {error}")
    except PermissionError:
        print(f"Відмовлено в доступі до директорії {src_dir}")
    except Exception as error:
        print(f"Помилка читання {src_dir}: {error}")
