import os
from pathlib import Path
from rembg import remove
from PIL import Image

SOURCE_DIR = Path(__file__).parent / "source"
OUTPUT_DIR = Path(__file__).parent / "output"

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def process():
    images = [f for f in SOURCE_DIR.iterdir() if f.suffix.lower() in SUPPORTED]

    if not images:
        print("source/ 資料夾中沒有圖片。")
        return

    print(f"找到 {len(images)} 張圖片，開始去背...\n")

    for img_path in images:
        output_path = OUTPUT_DIR / (img_path.stem + ".png")
        print(f"  處理：{img_path.name} → {output_path.name}")

        with open(img_path, "rb") as f:
            result = remove(f.read())

        with open(output_path, "wb") as f:
            f.write(result)

    print(f"\n完成！結果已儲存至 output/")


if __name__ == "__main__":
    process()
