import random
import string
import time
import tkinter as tk
from tkinter import messagebox

otp_length = 4
otp_data = {"otp": None, "expiry_time": None}
root = tk.Tk()

matematika = [("Diberikan fungsi f dan g dengan g(x) = (ax+f(x2+1)2 dan a > 0. Jika g'(1)=12, f'(2) = -1 dan f(2) = 3, maka 3a + 1 = ....","10"),
              ("Jika a dan b akar-akar persamaan kuadrat x2 – 13ax + p + 13 = 0 dan p + 2b = 25, maka a – b = ...","11"),
              ("Dalam suatu gedung teater di Provinsi Suka-Suka terdapat 11 baris kursi. Baris pertama berisi 10 kursi, baris kedua berisi 15 kursi, baris ketiga berisi 17 kursi, baris keempat berisi 22 kursi, baris ke lima berisi 24 kursi, dan seterusnya mengikuti pola yang sama. Berdasarkan informasi tersebut, banyaknya kursi pada baris kedua dari belakang adalah … kursi.","43"),
              ("Jika xy=50 dan 2logx−2logy=1, maka nilai x−y=⋯","5"),
              ("Jika f(x−1)=5x2+6x−6; g(x)=ax+1 dan (g∘f)(1)=−51 maka nilai f(a+1)=⋯","-6"),
              ]
fisika = [("Sebuah pijar dihubungkan dengan listrik PLN yang memiliki tegangan 220 Volt. Jika arus listrik yang mengalir pada lampu pijar lampu 500mA, berapakah energi listrik yang diperlukan lampu yang menyala selama 5 menit....J","33.000"),
              ("Sebuah mesin sepeda motor melakukan usaha sebesar 10.000 joule. Jika daya motor itu 2000 watt, berapakah waktunya....sec","5"),
              ("Sebuah lampu tertulis 10 watt. Jika dinyalakan dalam waktu 5 menit. Berapakah energi listriknya..... J","3.000"),
              ("Sebuah setrika listrik 200 watt menyala dalam waktu satu jam. Berapakah energi listrik yang telah digunakan.....Kj","720"),
              ("Sebuah pemanas listrik dipasang pada sumber tegangan 200 volt mengalir arus 0,25 A. Jika alat tersebut digunakan selama 10 menit. Berapakah besar energi listriknya....J ","30.000"),
              ]
kimia = [("Molaritas KI pada larutan yang mengandung 5,0% w/w (weight/weight) pada KI dengan densitas 1,038 g/ml adalah…M(Ar K = 39, Ar I = 127)","0,3114"),
              ("Hitunglah titik didih larutan dan naik titik didih dari 34,2 gram zat Q (mr=34,2) yang dilarutkan dalam 500 gram air dengan kenaikan titik didih air 0,52 °C dan titik didih air pelarut 100°C.","101,04 C"),
              ("Bilangan oksidasi dari unsur N dan P pada senyawa di bawah ini adalah NH4H2PO4…","-3 dan +5"),
              ("Pada elektrolisis 400mL larutan CuSO4 0,01 M, untuk mengendapkan seluruh ion tembaga diperlukan arus listrik dengan muatan sebesar…. F","0,008"),
              ("Jika 0,68 gram suatu elektronik biner (Mr = 204) dilarutkan ke dalam 100 gram air dan mendidih pada suhu 100,026 OC (Kb air = 0,52 OC/m), maka besarnya derajat lonisasi elektrolit di atas, adalah….","0,5"),
              ]
biologi = [("Mekanisme pertahanan tubuh pada manusia yang terdiri dari limfosit B dan limfosit T adalah….. ","sistem imun"),
              ("Tanaman lumut. Suplir, melinjo, dan rambutan dalam pengklasifikasian masuk ke kingdom plantae, karena memiliki ciri khusus, yaitu….. ","eukariotik, multiseluler, fotoautotrof"),
              ("Kelainan darah yang timbul karena hemoglobin kurang mengandung zat besi adalah…","Anemia"),
              ("Hormon untuk mempercepat pematangan buah","Auksin"),
              ("Hormon yang berfungsi sebagai penggugur daun pada musim kemarau, biasanya terjadi pada pohon jati padaq musim kemarau","Asam absisat"),
              ]

def generate_otp(length):
    char = string.digits
    otp = ''.join(random.choice(char) for _ in range(length))
    return otp

def generate_expiry_time():
    current_time = int(time.time())
    expiry_time = current_time + 24 * 60 * 60
    return expiry_time

def reroot_otp():
    otp = generate_otp(4)
    expiry_time = generate_expiry_time()
    otp_data["otp"] = otp
    otp_data["expiry_time"] = expiry_time
    return otp, expiry_time

def access_account(otp):
    if otp_data["otp"] == otp:
        if otp_data["expiry_time"] >= int(time.time()):
            return "Akses berhasil. Selamat datang!"
        else:
            return "OTP sudah kadaluarsa. Mohon minta OTP baru."
    else:
        return "Akses ditolak. Periksa kembali OTP."

def otpRun():
    def submit_otp():
        entered_otp = otp_entry.get()
        access_result = access_account(entered_otp)
        messagebox.showinfo("Hasil Akses", access_result)


    otp, expiry_time = reroot_otp()

    messagebox.showinfo("kode otp anda:", otp)
    messagebox.showinfo("berlaku:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(expiry_time)))

    otp_window = tk.Toplevel()
    otp_window.title("Verifikasi OTP")
    center_window(otp_window, width=1000, height=500)

    label = tk.Label(otp_window, text="Masukkan Kode OTP Anda:")
    label.pack(pady=10)

    otp_entry = tk.Entry(otp_window)
    otp_entry.pack(pady=5)

    submit_button = tk.Button(otp_window, text="Submit", command=lambda: (submit_otp(), otp_window.destroy()))
    submit_button.pack(pady=10)



def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x_coordinate = (screen_width - 1000) // 2
    y_coordinate = (screen_height - 500) // 2
    
    root.geometry(f"{1000}x{500}+{x_coordinate}+{y_coordinate}")

def main():
    def start_quiz(subject):
        def check_answer():
            user_answer = answer_entry.get()
            if user_answer.lower() == answer.lower():
                messagebox.showinfo("hasil", "Jawaban anda benar")
                print(otpRun())
            else:
                messagebox.showinfo("Hasil", "Jawaban Anda salah!")

        question, answer = random.choice(subject)
        root = tk.Toplevel()
        root.title("Jawablah soal ini!")
        root.resizable(False,False)
        center_window(root, width=1000, height=500)

        question_label = tk.Label(root, text=question) 
        question_label.pack(pady=10)

        answer_label = tk.Label(root, text="Jawaban:")
        answer_label.pack()

        answer_entry = tk.Entry(root)
        answer_entry.pack(pady=5)

        submit_button = tk.Button(root, text="Submit", command=check_answer, width=20, height=2)
        submit_button.pack(pady=10)

    root.title("Ultrasonic for LIfe")
    root.resizable(False,False)
    center_window(root, width=1000, height=500)

    label = tk.Label(root, text="Pilih Mapel:")
    label.pack(pady=10, padx=10, fill="x", expand=True)

    mtk_button = tk.Button(root, text="Matematika", command=lambda: start_quiz(matematika), width=20, height=2)
    mtk_button.pack(pady=3, padx=10, expand=True)

    fsk_button = tk.Button(root, text="Fisika", command=lambda: start_quiz(fisika), width=20, height=2)
    fsk_button.pack(pady=3, padx=10, expand=True)

    kma_button = tk.Button(root, text="Kimia", command=lambda: start_quiz(kimia), width=20, height=2)
    kma_button.pack(pady=3, padx=10, expand=True)

    blg_button = tk.Button(root, text="Biologi", command=lambda: start_quiz(biologi), width=20, height=2)
    blg_button.pack(pady=3, padx=10, expand=True)

    quit_button = tk.Button(root, text="Keluar", command=root.destroy, width=20, height=2)
    quit_button.pack(pady=3, padx=10, expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()