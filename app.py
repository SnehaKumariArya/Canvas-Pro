import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
STORAGE_FILE = "saved_canvas.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/save", methods=["POST"])
def save_canvas():
    try:
        data = request.get_json()
        # Saves the full multi-page project array state directly to disk
        with open(STORAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return jsonify({"message": "Project Sheets Saved Successfully! 📑"})
    except Exception as e:
        return jsonify({"message": f"Error saving layout: {str(e)}"}), 500

@app.route("/api/load", methods=["GET"])
def load_canvas():
    if os.path.exists(STORAGE_FILE):
        try:
            with open(STORAGE_FILE, "r") as f:
                return jsonify(json.load(f))
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"pages": None}) 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)