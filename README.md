# Image Upscaler Plugin
The Image Upscaler Plugin is a Flask-based web application that uses the Replicate API to upscale images using a pre-trained Real-ESRGAN model. This plugin allows you to send an image URL and receive an upscaled image in return.

## Features
Upscale images by a specified scale factor (default is 4x)
Supports various image formats such as JPEG, PNG, and BMP
Uses a pre-trained Real-ESRGAN model for high-quality upscaling

## Prerequisites
Python 3.6 or higher
Flask
Replicate
Requests

## Installation
1. Clone the repository:

git clone https://github.com/yourusername/image-upscaler-plugin.git

2. Change to the project directory:

cd image-upscaler-plugin

3. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install the required packages:

pip install -r requirements.txt

## Usage

1. Set the environment variable for the Replicate API token:

export REPLICATE_API_TOKEN="your_replicate_api_token"  # On Windows, use `set`

2. Run the Flask server:

python main.py

3. Send a POST request to the /upscale endpoint with the image_url and optional scale parameter:

{
  "image_url": "https://example.com/path/to/image.jpg",
  "scale": 4
}

4. Receive the upscaled image URL in the response:

{
  "output_image_url": "https://example.com/path/to/upscaled_image.jpg"
}

## Contributing
Contributions to the Image Upscaler Plugin are welcome. Please submit pull requests or open issues for bug reports and feature requests.
