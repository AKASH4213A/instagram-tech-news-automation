import os
import json
from datetime import datetime

#FIXED BASE DIRECTORY
BASE_DIR = r"G:\INSTAGRAM"

def save_post(post_data: dict, index: int):
    today = datetime.now().strftime("%Y-%m-%d")

#G:\INSTAGRAM\output\date
    base_dir = os.path.join(BASE_DIR, "output", today)
    os.makedirs(base_dir, exist_ok=True)

    file_path = os.path.join(base_dir, f"post_{index}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    return file_path
