import os
import argparse
from PIL import Image


# ===== DATASET PATH CONFIG =====
BASE_DIR = "./forConversion/YOLODataset_seg"

IMAGE_DIRS = {
    "train": os.path.join(BASE_DIR, "images/train"),
    "val": os.path.join(BASE_DIR, "images/val")
}

LABEL_DIRS = {
    "train": os.path.join(BASE_DIR, "labels/train"),
    "val": os.path.join(BASE_DIR, "labels/val")
}

OUTPUT_IMAGE_DIR = "./jpg_images"
OUTPUT_LABEL_DIR = "./new_labels"

JPG_QUALITY = 95
# =================================


def convert_png_to_jpg(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".png"):
            png_path = os.path.join(input_dir, filename)
            jpg_name = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_dir, jpg_name)

            with Image.open(png_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(jpg_path, "JPEG", quality=JPG_QUALITY)

            print(f"[IMG] {filename} -> {jpg_name}")


def fix_labels(input_dir, output_dir, target_label):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, "r") as infile:
                lines = infile.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if not parts:
                    continue

                parts[0] = str(target_label)
                new_lines.append(" ".join(parts) + "\n")

            with open(output_path, "w") as outfile:
                outfile.writelines(new_lines)

            print(f"[LBL] Fixed {filename}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_label", type=int, required=True,
                        help="Class ID to replace all labels with")
    args = parser.parse_args()

    target_label = args.target_label

    for split in ["train", "val"]:
        print(f"\n===== Processing {split.upper()} =====")

        img_in = IMAGE_DIRS[split]
        lbl_in = LABEL_DIRS[split]

        img_out = os.path.join(OUTPUT_IMAGE_DIR, split)
        lbl_out = os.path.join(OUTPUT_LABEL_DIR, split)

        convert_png_to_jpg(img_in, img_out)
        fix_labels(lbl_in, lbl_out, target_label)

    print("\n✅ Dataset processing complete.")


if __name__ == "__main__":
    main()