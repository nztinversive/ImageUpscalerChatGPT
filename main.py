from flask import Flask, request, jsonify, abort, Response, send_file
import replicate
import requests
from io import BytesIO
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

REPLICATE_API_TOKEN = os.environ["REPLICATE_API_TOKEN"]

@app.route("/")
def index():
    return "Image Upscaler Plugin is running."

@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def send_ai_plugin_json():
    with open(os.path.join(os.getcwd(), ".well-known", "ai-plugin.json"), "r") as f:
        return Response(f.read(), content_type="application/json")

@app.route("/openapi.yaml", methods=["GET"])
def send_openapi_spec():
    with open(os.path.join(os.getcwd(), "openapi.yaml"), "r") as f:
        return Response(f.read(), content_type="text/yaml")

@app.route("/logo.png")
def logo():
    return send_file(os.path.join(os.getcwd(), "logo.png"))

@app.route("/upscale", methods=["POST"])
def upscale_image():
    data = request.get_json()
    if not data or "image_url" not in data:
        abort(400)

    image_url = data["image_url"]
    scale = data.get("scale", 4)
    face_enhance = data.get("face_enhance", False)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(image_url, headers=headers)
    if response.status_code != 200:
        abort(400, "Failed to download the image from the URL")

    content = response.content

    output = replicate.run(
        "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
        input={"image": BytesIO(content)}
    )

    # Assuming the output is an image URL, you can return it directly
    return jsonify({"output_image_url": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


