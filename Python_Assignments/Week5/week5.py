"""(1) OpenCV 활용"""
import cv2

filepath = r"airplane.jpg"

image = cv2.imread(filepath)

if image is None:
    print("Failed to load image.")
else:
    h, w, _ = image.shape
    resized = cv2.resize(image, (w//2, h//2))
    grayscale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow('Original image', resized)
    cv2.imshow('Grayscale image', grayscale)
    cv2.imshow('Rotated image', rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""Config 파일 읽어오기"""
from pathlib import Path

filepath = Path(r"config.ini")

if not filepath.exists():
    filepath.touch()
    with open(filepath, "w", encoding="utf-8") as file:
        for i in range(1, 5):
            file.write(f"{i}반 = \n")
else:
    data = dict()
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            group, name = line.split(" = ")
            data[group] = name.strip()

"""JSON 파일 쓰기"""
import json

json_file = r"config.json"
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

"""JSON 파일 읽어오기"""

with open(json_file, "r", encoding="utf-8") as file:
    data_acquired = json.load(file)