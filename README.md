## Introduction:

Description of the HTR pipeline and its operations.
Mention of the models used for word detection and text reading.
Installation:

### Instructions for installing the pipeline and its dependencies using pip.
Usage:

Instructions for running a demo that showcases the pipeline's capabilities.
Code snippet for using the Python package to detect and read handwritten text from an image.

## Code Example "Pen-To-Voice":

You've included a code snippet from the "Pen-To-Voice" project that uses the HTR pipeline to detect and read text from images.
The code includes importing necessary modules, reading images, performing autocorrection, and using pyttsx3 to convert text to speech.
The code also visualizes the results by plotting images with detections and overlaying text.

## Handwritten Word Detector:

A code snippet for the word detector module that uses a scale space technique to segment words in handwritten text.
Explanation of the approach, including kernel filtering, thresholding, and contour detection.
Discussion of the cluster lines method to group words into lines.

## Word Reader Model:

A code snippet for the text reader model that uses a CRNN-based approach to recognize text in images.
Explanation of how the model is initialized and used, including decoding and processing.

## Integration of Detector and Reader:

A code snippet that integrates the word detector and text reader to read words from an image.
Explanation of image preparation, detection, sorting, and reading.
JSON and Charlist Files:

Mention of the charlist.txt file containing the characters the reader model recognizes.
Description of the JSON file with character error rates and word accuracies.
## Installation

* Go to the root level of the repository
* Execute `pip install .`

## Usage

### Run demo

* Additionally install matplotlib for plotting: `pip install matplotlib`
* Go to `scripts/`
* Run `python demo.py`
* The output should look like the plot shown above

### Use Python package

Import the function `read_page` to detect and read text.

````python
import cv2
from htr_pipeline import read_page, DetectorConfig

# read image
img = cv2.imread('data/r06-137.png', cv2.IMREAD_GRAYSCALE)

# detect and read text
read_lines = read_page(img, DetectorConfig(height=1000))

# output text
for read_line in read_lines:
    print(' '.join(read_word.text for read_word in read_line))
````

If needed, the detection can be configured by instantiating and passing these data-classes:

* `DetectorConfig`
* `LineClusteringConfig`

For more details please have a look at the docstrings of `detect` and `sort_multiline`
in `htr_pipeline/word_detector/__init__.py`. The most important settings are:

* `height` in `DetectorConfig`: the word detector is not scale invariant, the text height should be 25-50px when using
  the default parameters, which is achieved by resizing the image to the specified height
* `min_words_per_line` in `LineClusteringConfig`: lines which have fewer words than specified are discarded, the default
  setting is 2, which means that lines with a single word will not be read by default
