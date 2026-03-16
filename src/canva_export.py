import csv
import os
from datetime import datetime

EXPORT_DIR = "G:/INSTAGRAM/canva_exports"

def export_to_canva_csv(posts: list):
    os.makedirs(EXPORT_DIR, exist_ok=True)

    filename = f"canva_posts_{datetime.now().strftime('%Y-%m-%d')}.csv"
    path = os.path.join(EXPORT_DIR, filename)

    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "page_1_headline",
                "page_2_kya_hua",
                "page_3_kyun_important",
                "caption"
            ]
        )
        writer.writeheader()

        for post in posts:
            writer.writerow({
                "page_1_headline": post["slides"]["slide_1"],
                "page_2_kya_hua": post["slides"]["slide_2"],
                "page_3_kyun_important": post["slides"]["slide_3"],
                "caption": post["caption"]
            })

    return path
