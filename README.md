# YOLO Segmentation Data Cleaning Tool

This script simplifies the workflow of converting **LabelMe** annotations into a format ready for **YOLOv9/YOLO26** training. It automates the conversion, image standardization, and label filtering in one go.

---

## 🚀 Features

* **LabelMe to YOLO:** Converts `.json` polygon annotations into YOLO segmentation `.txt` files.
* **Image Standardization:** Automatically converts `.png` files to `.jpg` to ensure dataset consistency.
* **Label Filtering:** Cleans the dataset by keeping only the specific class ID you need.
* **Automation:** Handles file renaming and path updates so your labels and images always match.

---

## 🛠 How It Works

1.  **Conversion:** The tool runs `labelme2yolo` to generate the initial normalized coordinates.
2.  **Format Shift:** It scans the directory for PNGs, converts them to JPGs, and deletes the originals to save space.
3.  **Label Correction:** It opens every generated `.txt` label and filters out any classes that don't match your `--target_label`.

---

## 💻 Usage

To process your data, run the script from your terminal and specify the class ID you want to keep:

```bash
python process_data.py --target_label 0
