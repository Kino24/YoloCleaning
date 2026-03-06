import os

LABELS_DIR = './forConversion/YOLODataset/labels/val'          # Original labels directory
OUTPUT_DIR = './new_labels/val'  # Output directory for new label files
TARGET_LABEL = 4                   # <<< set the label number you want here

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(LABELS_DIR):
    if filename.endswith('.txt'):
        input_path = os.path.join(LABELS_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        with open(input_path, 'r') as infile:
            lines = infile.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue

            # Replace class ID with target label
            parts[0] = str(TARGET_LABEL)
            new_lines.append(' '.join(parts) + '\n')

        with open(output_path, 'w') as outfile:
            outfile.writelines(new_lines)

print(f"All labels updated to class {TARGET_LABEL} and saved to {OUTPUT_DIR}/")
