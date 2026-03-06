import os
from PIL import Image

# ===== CONFIG =====
INPUT_DIR = "./forConversion/YOLODataset/images/val"     # Folder with PNG files
OUTPUT_DIR = "jpg_images./val"    # Folder to save JPG files
JPG_QUALITY = 95             # 1–100 (higher = better quality)
# ==================

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".png"):
        png_path = os.path.join(INPUT_DIR, filename)
        jpg_name = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(OUTPUT_DIR, jpg_name)

        with Image.open(png_path) as img:
            # Convert RGBA/PNG transparency to RGB (JPG doesn't support alpha)
            rgb_img = img.convert("RGB")
            rgb_img.save(jpg_path, "JPEG", quality=JPG_QUALITY)

        print(f"Converted: {filename} → {jpg_name}")

print("✅ All PNG files converted to JPG.")