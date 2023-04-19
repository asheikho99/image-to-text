# OCR Script README

This script uses the Python Imaging Library (PIL), pytesseract, and the dotenv library to extract text from an image file and print it to the console. The script reads the image path and the path to the Tesseract executable from environment variables.

## Dependencies

- Python Imaging Library (PIL) or Pillow
- pytesseract
- python-dotenv

## Installation

1. Install Python Imaging Library (PIL) or Pillow. Check the [Pillow documentation](https://pillow.readthedocs.io/en/stable/installation.html) for installation instructions.

2. Install Google Tesseract OCR. Refer to the [additional info](https://github.com/tesseract-ocr/tesseract/wiki) on how to install the engine on Linux, Mac OSX, and Windows.

3. Install pytesseract and python-dotenv using pip:

\```bash
pip install pytesseract python-dotenv
\```

## Usage

1. Create a `.env` file in the same directory as the script and set the environment variables `SAMPLE_1` and `PATH_TO_TESSERACT`:

\```
SAMPLE_1=/path/to/image/file
PATH_TO_TESSERACT=/path/to/tesseract/executable
\```

2. Run the script:

\```bash
python ocr_script.py
\```

The script will load the image specified by the `SAMPLE_1` environment variable, use pytesseract to extract text from the image, and print the extracted text to the console.

## Example

Here's an example of the script in action:

\```python
from PIL import Image
from pytesseract import pytesseract
from dotenv import load_dotenv
import os

load_dotenv()

IMG_SAMPLE = os.getenv("SAMPLE_1")
PATH_TO_TESSERACT = os.getenv("PATH_TO_TESSERACT")

path_to_tesseract = PATH_TO_TESSERACT
image_path = IMG_SAMPLE

img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)
\```

For more information and usage examples of pytesseract, refer to the [official pytesseract GitHub repository](https://github.com/madmaze/pytesseract/blob/master/README.rst).