
from flask import Flask, render_template, jsonify, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    # API untuk data mentah - bisa dipakai untuk analisis lanjutan
    data = {
        "total_biaya": 19050000,
        "total_hari": 10,
        "per_kategori": {
            "HONOR": 10500000,
            "TEMPAT TINGGAL": 4965000,
            "KONSUMSI": 2700000,
            "PERALATAN & LAIN LAIN": 560000,
            "PERALATAN": 260000,
            "OBAT-OBATAN": 65000
        },
        "per_periode": {
            "20-22 Agt": 3635000,
            "23-26 Agt": 11225000,
            "27-29 Agt": 4190000
        },
        "forecast_september": {
            "realistis": 13491500,
            "realistis_sewa": 15291500,
            "pesimis": 15791500
        }
    }
    return jsonify(data)

@app.route('/api/forecast')
def api_forecast():
    # Download forecast sebagai Excel dinamis dari Flask
    import pandas as pd
    from io import BytesIO
    forecast = {
        "Skenario": ["Realistis (10 hari, tanpa sewa)", "Realistis + Perpanjang Sewa", "Pesimis + Cadangan"],
        "HONOR": [10500000, 10500000, 10500000],
        "KONSUMSI": [2700000, 2700000, 2700000],
        "OBAT Buffer": [71500, 71500, 71500],
        "BBM": [220000, 220000, 220000],
        "Sewa Rumah": [0, 1800000, 1800000],
        "Cadangan": [0, 0, 500000],
        "TOTAL": [13491500, 15291500, 15791500]
    }
    df = pd.DataFrame(forecast)
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    return send_file(output, download_name="forecast_borbor.xlsx", as_attachment=True)

if __name__ == '__main__':
    # Penting: host 0.0.0.0 biar bisa diakses online
    app.run(host='0.0.0.0', port=5000, debug=True)
