import random
import math
import pandas as pd

## Dict Petanyaan
data= {'index':[1,2,3,4,5,6,7,8,9,10],
       'pertanyaan':['Nama zat hijau daun?',
                     'Nama kingdom dari hewan sapi?',
                     'Nama indera perasaa adalah?',
                     'Nama fragmen darah yang berfungsi untuk membekukan darah?',
                     'Nama bagian tubuh yang menyambungkan antara tulang dan tulang?',
                     'Nama alat pernapasan serangga?',
                     'Nama enzim pengubah karbohidrat menjadi gula?',
                     'Nama bagian tempat pertukaran oksigen dan CO2 di paru-paru?',
                     'Nama penyakit yang diakibatkan oleh Salmonella typhi?',
                     'Nama zat yang mengakibatkan otot lelah?'],
       'jawaban':['klorofil','animalia','lidah','trombosit','ligamen','trakea','amilase','alveolus','tipes','asam laktat']}

## Data Pemain
list_player= []
list_score= []
def pemain(nama,amount):
    if nama in list_player:
        a= list_player.index(nama)
        if list_score[a]< amount:
            list_score[a]=amount
    else:
        list_player.append(nama)
        list_score.append(amount)

## Pencaharian
def cari():
    while True:
        try:
            siapa= input(f'''\n===={'CARI CAPAIAN PEMAIN':^47}====
Siapa nama user yang ingin Anda cari? ''').lower()
            for i in list_player:
                if i==siapa:
                    a=i
                    b=list_score[list_player.index(siapa)]
            print(f"Pemain dengan nama {a} memiliki nilai terbaik {b}")
        except:
            print('Maaf, Nama tidak ditemukan')
        r=question(f'\nApakah anda ingin mencari yang lain? (Y/N) ',['Y','N'])
        if r=='n':
                break

## Hapus Data
def hapus():
    d=question(f'''\n===={'HAPUS CAPAIAN USER':^47}====
Apakah Kamu yakin ingin menghapus capaian user {put}? (Y/N) ''',['Y','N'])
    if d=='y':
        while True:
            try:
                c=list_player.index(put)
                n=list_score[c]
                list_player.remove(list_player[c])
                list_score.remove(n)
                print(f'Data pencapaian player {put} berhasil dihapus! ')
            except:
                print(f'Maaf, Nama player tidak ditemukan atau belum memiliki riwayat bermain')
            input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
            break

## Leaderboard
def board():
    dict={'nama':list_player,
          'nilai':list_score}
    lead= pd.DataFrame(dict)
    leaderboard= lead.sort_values('nilai',ascending=False).reset_index(drop=True)
    if list_player==[]:
        print(f'''\n===={'LEADERBOARD':^47}====
Maaf, belum ada data pemain yang tersedia''')
    else:
        print(f'''\n===={'LEADERBOARD':^47}====
{leaderboard.to_string(index=False)}''')
    input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
    

## Exeption handling for Question
def question(msg,choice):
    cho= [i.lower() for i in choice]
    while True:
        jwb= input(msg).lower()
        if jwb in cho:
            return jwb
        else:
            print(f'\nCek kembali jawabanmu! Hanya {choice} yang diperbolehkan!')

## Greeting
def greeting():
    print(f'''{'-'*56}
|{'Welcome to Quezzy':^54}|
{'-'*56}''')

## User Name
def user():
    global put
    put= input(f'''
Siapa Nama player mu? ''')
    print(f'\nHalo {put}, Bagaimana kabarmu hari ini? Semoga sehat selalu ya.')

## Homepage
def home():
    while True:
        q= question(f'''\n===={'HOME MENU':^47}====
Pilih Menu di bawah ini:
A. Mulai Main
B. Cek Capaian Pemain
C. Cek Leadarboard
D. Hapus Capaian User
E. Keluar 
Jawab => ''',['A','B','C','D','E'])
        if q=='a':
            break
        elif q=='b':
            cari()
        elif q=='e':
            return 'exit'
        elif q=='c':
            board()
        elif q=='d':
            hapus()

## Question
num= list(range(0,10))
# random.shuffle(num)
selnum= random.sample(num,5)
numb=[]
benar=[]
salah=[]
def main():
    print(f'''\n===={'MULAI PERMAINAN':^47}====
Tugas kamu adalah menjaawab pertanyaan berikut dengan tepat.\nMari kita mulaiii!''')
    a=0
    for i in selnum:
        if i not in numb:
            a+=1
            af= input(f"\n{a}. {data['pertanyaan'][i]} ").lower()
            if af!=data['jawaban'][i]:
                salah.append(i)
            else:
                benar.append(i)
            numb.append(i)


## Result
def review():
    nilai=int((len(benar)/5)*100)
    print(f"\n{'-'*56}")
    if nilai==100:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<19}|
|{'Perfect! Selamat Anda Lulus':^54}|''')
    elif nilai>=60:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
|{'Selamat Anda lulus':^54}|''')
    elif nilai>0:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
|{'Maaf Anda belum lulus. Yuk belajar lagi':^54}|''')
    elif nilai==0:
        print(f'''|{' ':>21}Nilai Kamu: {nilai}{' ':<20}|
|{'Belajar lagi aja dek!':^54}|''')
    print(f"{'-'*56}")
    pemain(put,nilai)
    

## Running the Game
greeting()
user()
while True:
    gmn=home()
    if gmn=='exit':
        print(f'''\n{'-'*56}
|{'Terima Kasih Sudah Bermain!':^54}|
{'-'*56}\n''')
        break
    main()
    review()
    ask= question('Apakah Anda ingin bermain lagi? (Y/N) ',['Y','N'])
    if ask=='n':
        print(f'''\n{'-'*56}
|{'Terima Kasih Sudah Bermain!':^54}|
{'-'*56}\n''')
        break
    else:
        numb.clear()
        benar.clear()
        salah.clear()
        print(f'\n=== {'NEW GAME':^47} ===\n')