import random

def game(pilih, musuh):
    if pilih == musuh:
        print("Seri")
    elif pilih == "Batu" and musuh == "Gunting" or pilih == "Gunting" and musuh == "Kertas" or pilih == "Kertas" and musuh == "Batu":
        print(user + " Menang!")
        print("Musuh Kalah!")
    elif pilih == "Batu" and musuh == "Kertas" or pilih == "Gunting" and musuh == "Batu" or pilih == "Kertas" and musuh == "Gunting":
        print(user + " Kalah!")
        print("Musuh Menang!")
    validasi = input("Bermain lagi? [Ya/Tidak]: ")
    while validasi != "Ya" and validasi != "Tidak":
        validasi = input("Bermain lagi? [Ya/Tidak]: ")
    if validasi == "Ya":
        main()

def main():
    pilihan_list = ["Batu","Gunting","Kertas"]

    print("GAME")
    pilih = input("Pilih[Batu , Gunting, Kertas]: ")

    while pilih != "Batu" and pilih != "Gunting" and pilih != "Kertas":
        pilih = input("Pilih[Batu , Gunting, Kertas]: ")

    print(user +" memilih "+ pilih)
    musuh = pilihan_list[random.randint(0,2)]
    print("Musuh memilih "+ musuh)

    game(pilih, musuh)

user = input("Masukkan nama anda: ")
main()

