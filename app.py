from flask import Flask, render_template, request, send_from_directory
import os
from cmad_core import cmad_discord_for_two_images

# Folders
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/process", methods=["POST"])
def process_images():
    # Get uploaded files
    img1 = request.files.get("img1")
    img2 = request.files.get("img2")

    if not img1 or not img2:
        return "Please upload both images.", 400

    # Save images
    img1_path = os.path.join(UPLOAD_FOLDER, img1.filename)
    img2_path = os.path.join(UPLOAD_FOLDER, img2.filename)

    img1.save(img1_path)
    img2.save(img2_path)

    # Extract date from second image
    date_str = os.path.splitext(img2.filename)[0]

    # Output file path
    output_path = os.path.join(OUTPUT_FOLDER, "anomaly.png")

    # Run CMAD detection
    _mask, _overlay = cmad_discord_for_two_images(
        img1_path,
        img2_path,
        lb_txt_path="lb15.txt",
        q1_txt_path="q115.txt",
        show_plot=False,
        save_path=output_path
    )

    try:
        os.remove(img1_path)
        os.remove(img2_path)
        print("Temporary uploaded images deleted.")
    except Exception as e:
        print("Could not delete uploaded files:", e)

    return render_template(
        "result.html",
        image_file="anomaly.png",
        date_str=date_str
    )



@app.route("/outputs/<filename>")
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

