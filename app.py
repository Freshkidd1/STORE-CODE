import os
import zipfile
from pathlib import Path

# Define the folder structure
base_path = Path("store-website")
folders = [
    base_path,
    base_path / "css",
    base_path / "js",
    base_path / "images",
]

# Files with placeholder content
files = {
    base_path / "index.html": "<!-- Home Page -->",
    base_path / "shop.html": "<!-- Shop Page -->",
    base_path / "product.html": "<!-- Product Detail Page -->",
    base_path / "about.html": "<!-- About Page -->",
    base_path / "contact.html": "<!-- Contact Page -->",
    base_path / "cart.html": "<!-- Cart Page -->",
    base_path / "css" / "style.css": "/* Main CSS */",
    base_path / "js" / "script.js": "// Main JS",
}

# Create folders
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Create files with placeholder content
for file_path, content in files.items():
    file_path.write_text(content)

# Add placeholder images
for i in range(1, 21):
    image_path = base_path / "images" / f"product{i}.jpg"
    image_path.write_text("fake-image-content")  # Placeholder content

# Zip the folder
zip_path = Path("store-website.zip")
with zipfile.ZipFile(zip_path, "w") as zipf:
    for folder in base_path.rglob("*"):
        zipf.write(folder, folder.relative_to(base_path.parent))

print("ZIP file created: store-website.zip")
