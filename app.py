from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# --- JSON dosyasını yükle ---
with open("static/sehirler.json", "r", encoding="utf-8") as f:
    sehirler = json.load(f)

@app.route("/")
def index():
    # Şehirleri index.html'e gönderiyoruz
    return render_template("index.html", sehirler=sehirler)

@app.route("/api/sehirler")
def sehirler_api():
    return jsonify(sehirler)

@app.route("/detay/<sehir_adi>")
def detay(sehir_adi):
    # Küçük-büyük harf farkını kaldırmak için normalize ediyoruz
    for sehir in sehirler:
        if sehir["ad"].lower() == sehir_adi.lower():
            return render_template("detay.html", sehir=sehir)
    return f"<h2>{sehir_adi} bulunamadı.</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
