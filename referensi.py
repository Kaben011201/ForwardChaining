class SistemPakarHIVAIDS:
    def __init__(self):
        self.gejala = set()

    def tambah_gejala(self, gejala):
        self.gejala.add(gejala)

    def deteksi_hiv_aids(self):
        if 'gejala1' in self.gejala and 'gejala2' in self.gejala:
            return "Kemungkinan besar terkena HIV-AIDS. Segera konsultasikan dengan dokter."
        elif 'gejala3' in self.gejala:
            return "Mungkin terkena HIV-AIDS. Disarankan untuk menjalani tes lebih lanjut."
        else:
            return "Tidak terdeteksi gejala HIV-AIDS."

# Fungsi main untuk penggunaan contoh
def main():
    sistem_pakar = SistemPakarHIVAIDS()
    sistem_pakar.tambah_gejala('gejala1')
    sistem_pakar.tambah_gejala('gejala2')

    hasil_deteksi = sistem_pakar.deteksi_hiv_aids()
    print(hasil_deteksi)

# Memanggil fungsi main jika script dijalankan
if __name__ == "__main__":
    main()
