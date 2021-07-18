__author__ = 'kai'

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def hello():
    masukkan = request.form['pencarian']
    masukkan = masukkan.replace("-"," ").replace(":", " ")

    cari = masukkan.split()

    try:
        int(cari[1])
    
    except ValueError :
        cari[0] = f"{cari[0]}_{cari[1]}"
        cari.pop(1)

    finally:
        kitab = cari[0]

        if len(cari) == 1:
            cari.append("1")
        pasal = cari[1]

        if len(cari) == 2:
            cari.append(1)
        ayat_pertama = int(cari[2])

        if len(cari) == 3:
            cari.append(ayat_pertama)
        ayat_kedua = int(cari[3])

        for i in os.listdir("Alkitab"):
            if (i[:len(kitab)].lower() == kitab.lower()) :
                try:
                    with open(f"Alkitab/{i}/{i}_{pasal}.txt") as buka_kitab:
                        baca_isi = buka_kitab.readlines()
                        baca_isi[ayat_pertama-1] 
                        baca_isi[ayat_kedua-1]
                        book = (f"{i.replace('_',' ')} {pasal}:")
                        book = book.replace("Raja Raja", "Raja-Raja").replace("Hakim Hakim", "Hakim-Hakim")
                        if (ayat_pertama == ayat_kedua):
                            book += str(ayat_pertama)
                        else:
                            book += f"{ayat_pertama}-{ayat_kedua}"
                        verse = ""
                        for j in baca_isi[ayat_pertama-1:ayat_kedua]:
                            verse += j.replace("\n","")
                            verse += "\n"
                        hasil = [book, verse]
                        return render_template('result.html',data = hasil)
                except Exception:
                    return render_template('result.html', data = ['Ayat tidak ditemukan',''])
        return render_template('result.html', data = ['Kitab tidak ditemukan',''])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)