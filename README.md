
# Dashboard Borbor - Flask Version

## Cara jalanin di laptop (lokal)
1. Install: pip install -r requirements.txt
2. Jalankan: python app.py
3. Buka browser: http://127.0.0.1:5000

## Cara online-kan (gratis)

### OPSI 1: Render.com (paling gampang, gratis)
1. Push folder ini ke GitHub (buat repo baru)
2. Buka https://dashboard.render.com -> New Web Service -> Connect repo kamu
3. Build Command: (kosongkan)
4. Start Command: gunicorn app:app
   - Tambah gunicorn di requirements.txt
5. Deploy! Dapat link https://borbor-dashboard.onrender.com

### OPSI 2: PythonAnywhere (khusus Flask, gratis)
1. Daftar di https://www.pythonanywhere.com
2. Upload file app.py dan folder templates
3. Buat Web App -> Flask -> pilih file app.py
4. Langsung online!

### OPSI 3: Railway.app
1. Buka https://railway.app -> Deploy from GitHub
2. Pilih repo ini, otomatis detect Flask
3. Dapat link online

## API yang tersedia
- / -> Dashboard
- /api/data -> JSON data mentah
- /api/forecast -> Download Excel forecast dinamis

# Belajar Analisis Data - PLTM Borbor

Dashboard keuangan PLTM Borbor Agustus 2026

**Live Demo:** https://belajaranalis.netlify.app/
**Tech Stack:** Python, Pandas, Flask, Chart.js, Netlify

Alur kerja: Excel berantakan → Cleaning dengan Python → Analisis → Dashboard
