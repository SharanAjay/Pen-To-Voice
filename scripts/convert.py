import cv2
import matplotlib.pyplot as plt
import glob
from path import Path
from autocorrect import Speller
import pyttsx3

from htr_pipeline import read_page, DetectorConfig

# initialize autocorrect
spell = Speller(lang='en')

# initialize pyttsx3
engine = pyttsx3.init()

for img_filename in glob.glob('D:\Project_meni\HTRPipeline\data\*.jpg') + glob.glob('D:\Project_meni\HTRPipeline\data\*.png'):
    print(f'Reading file {img_filename}')

    # read text
    img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    read_lines = read_page(img, DetectorConfig(height=1000))

    # output text with autocorrection
    for read_line in read_lines:
        corrected_text = ' '.join(spell(read_word.text)
                                  for read_word in read_line)
        print(corrected_text)
        # speak the text using pyttsx3
        engine.say(corrected_text)
        engine.runAndWait()

    # plot image with detections and texts as overlay
    plt.figure(img_filename)
    plt.imshow(img, cmap='gray')
    for i, read_line in enumerate(read_lines):
        for read_word in read_line:
            bbox = read_word.bbox
            xs = [bbox.x, bbox.x, bbox.x + bbox.w, bbox.x + bbox.w, bbox.x]
            ys = [bbox.y, bbox.y + bbox.h, bbox.y + bbox.h, bbox.y, bbox.y]
            plt.plot(xs, ys, c='r' if i % 2 else 'b')
            plt.text(bbox.x, bbox.y, spell(read_word.text))

plt.show()
