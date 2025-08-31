# Membuat permainan bahlil v.1.1
# {"Selamat Datang":^28}
# Buat greeting awal permainan
def greet():
    print(f'''{'-'*72}
|{"Selamat Datang":^70}|
{'-'*72}\n
Untuk memulai permainan kamu perlu memasukan nama playermu.''')
    player_name=input('Nama Player = ')
    print(f'\nHallo {player_name}! Saatnya kita memulai permaiann...')
    return player_name

# Buat deskripsi permainan
def describe():
    print('''\nPermainannya cukup mudah. Mari kita menangkap bahlil!
Bahlil saat ini sedang bersembunyi di goa berikut:
       _    _    _    _
      |1|  |2|  |3|  |4|
       ‾    ‾    ‾    ‾''')
    
# Buat function pertanyaan
# Dapat berfungsi juga sebagai validasi jawaban apakah sesuai dengan list jawaban yang tersedia 
def question(msg,choice):
    while True:
        try:
            ans= int(input(msg))
            if ans in choice:
                return ans
            else:
                print(f'\nCek kembali jawabanmu ya, jawabannnya hanya diantara {choice}')
        except ValueError:
            print(f'\nMohon cek lagi jawabanmu ya! Jawaban yang diinputkan hanya diantara {choice}')


# Buat Jawaban dari permainan menggunakan random
import random
key=random.randint(1,4)

# Buat Skema Permainan
def game():
    guess=question('Menurutmu ada di goa nomor berapakah bahlil bersembunyi? ',[1,2,3,4])
    confirm=question('Apakah kamu yakin dengan jawabanmu? (1=Iya 2=Tidak)',[1,2])
    while confirm:
        if confirm==1:
            return guess
        else:
            guess=question('\nMenurutmu ada di goa nomor berapakah bahlil bersembunyi? ',[1,2,3,4])
            confirm=question(f'Apakah kamu yakin dengan jawabanmu ada di goa {guess}? (1=Iya 2=Tidak)',[1,2])


# Buat hasil permainan

def result():
    if ply_guess==key:
        print(f'''
{'-'*72}
Yeay selamat {player}!! Kamu bisa menagkap bahlil !!
Goa {ply_guess} seperti yang kamu jawab memang menjadi tempat persembunyian Bahlil.
{'-'*72}''')
    else:
        print(f'''
{'-'*72}
Sayang sekali bahlil belum bisa tertangkap.
Kamu menjawab goa {ply_guess} padahal bahlil bersembunyi di goa {key}
{'-'*72}''')
    play_again=question('Apakah kamu ingin bermain lagi ? (1=Ya 2=Tidak)',[1,2])
    return play_again
        

# Step by Step permainan
'''
Terbagi menajdi empat bagian:
1.  Menampilkan menu greeting sekaligus mendifinisikan nama player untuk digunakan 
    di function selanjutnya
2.  Menampilkan menu deskirpsi dari game serta petunjuk permainannya
3.  Menampilkan menu permainan sekaligus mendefinisikan jawaban dari pemain untuk digunakan
    di funtion hasil
4.  Menampilkan menu hasil dari rangkaian game
'''
player= greet()             #1
while True:                 # Buat Looping jika ingin mengulang permainan
    describe()              #2
    ply_guess=game()        #3
    end=result()            #4
    if end ==2:
        print(f'''\n{'-'*72}
{"Terima Kasih Sudah Bermain!!":>52}
{"See Yaa!!":>42}
{'-'*72}''')
        break
    else:
        print(f'''\n{'-'*72}
{"NEW GAME":>40}
{'-'*72}''')