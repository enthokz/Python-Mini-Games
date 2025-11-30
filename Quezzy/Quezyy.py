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
                     'Nama zat yang mengakibatkan otot lelah?',
                     'Nama tulang terpanjang yang dimiliki manusia?',
                     'Nama Saluran yang menghubungkan mulut dengan lambung?',
                     'Nama gerakan mendorong makanan dari rongga mulut menuju lambung?',
                     'Nama bagian yang berfungsi mengatur cahaya yang masuk ke mata?',
                     'Tingkatan taksonomi makhluk hidup di atas species?',
                     'Istilah makhluk hidup yang memiliki organ reproduksi ganda?',
                     'Nama otot yang berfungsi untuk menggerakan tubuh secara sadar adalah otot?',
                     'Nama kemampuan dari makhluk hidup dalam menyamarkan diri dengan lingkungan sekitar disebut?',
                     'Simbiosis yang menguntungkan kedua belah pihak adalah?',
                     'Nama saat kondisi tubuh kekurangan sel darah merah?'],
       'jawaban':['klorofil','animalia','lidah','trombosit','ligamen',
                  'trakea','amilase','alveolus','tipes','asam laktat','femur',
                  'kerongkongan','peristaltik','pupil','genus','hemaprodit','lurik','mimikri',
                  'mutualisme','anemia']}

## Exeption handling for Question in Game
def question(msg,choice):
    cho= [i.lower() for i in choice]
    while True:
        jwb= input(msg).lower()
        if jwb in cho:
            return jwb
        else:
            print(f'\nCek kembali jawabanmu! Hanya {choice} yang diperbolehkan!')
def question2(msg,choice):
    while True:
        jwb= input(msg).lower()
        if jwb=='' or jwb=='e':
            return jwb
        else:
            print("Silahkan tekan ENTER untuk melanjutkan atau ketik E' untuk keluar")


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
            a=[]
            b=[]
            for i in list_player:
                if i==siapa:
                    a.append(siapa)
                    b.append(list_score[list_player.index(siapa)])
            if a!=[]:
                print(f"Pemain dengan nama {a[0]} memiliki nilai terbaik {b[0]}")
            else:
                print('Maaf, Nama pemain salah atau belum pernah bermain')
        except:
            print('Maaf, Nama tidak ditemukan')
        r=question(f'\nApakah anda ingin mencari capaian pemain yang lain? (Y/N) ',['Y','N'])
        if r=='n':
                break


## Hapus Data
def hapus():
    d=question(f'''\n===={'HAPUS CAPAIAN USER':^47}====
Apakah Kamu yakin ingin menghapus capaian user {put}? (Y/N) ''',['Y','N'])
    if d=='y':
        while True:
            try:
                b=list_player.index(put)
                n=list_score[b]
                list_player.remove(list_player[b])
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
        

## Greeting
def greeting():
    print(f'''{'-'*56}
|{'Welcome to Quezzy':^54}|
{'-'*56}''')
    lanjut=question2(f'{'Silahkan Tekan Enter':^54}',['','E'])
    if lanjut=='e':
        return 'exit'

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
A. Mulai Permainan
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
# random.shuffle(num)
def main():
    global numb
    global benar
    global salah
    num= list(range(0,21))
    selnum= random.sample(num,5)
    numb=[]
    benar=[]
    salah=[]
    print(f'''\n===={'MULAI PERMAINAN':^47}====
Tugas kamu adalah menjawab pertanyaan berikut dengan tepat.\nMari kita mulaiii!''')
    a=0
    for i in selnum:
        if i not in numb:
            a+=1
            while True:
                af= input(f"\n{a}. {data['pertanyaan'][i]} ").lower()
                if af=="":
                    print(f'\nJawaban tidak boleh kosong!')
                elif af!=data['jawaban'][i]:
                    salah.append(i)
                    break
                else:
                    benar.append(i)
                    break
            numb.append(i)


## Result
def review():
    nilai=int((len(benar)/len(numb))*100)
    print(f"\n{'-'*56}")
    if nilai==100:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<19}|
|{'Perfect! Nilai Kamu Sempurna!':^54}|''')
    elif nilai>=60:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
|{'Hebat! Kamu hampir memjawab semua dengan benar':^54}|''')
    elif nilai>0:
        print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
|{'Maaf Nilai mu rendah. Belajar lagi ya':^54}|''')
    elif nilai==0:
        print(f'''|{' ':>21}Nilai Kamu: {nilai}{' ':<20}|
|{'Belajar lagi aja dek!':^54}|''')
    print(f"{'-'*56}")
    pemain(put,nilai)
    
##  End Greeting
def endgreet():
    print(f'''\n{'-'*56}
|{'Terima Kasih Sudah Bermain!':^54}|
{'-'*56}\n''')
    
## Newgame Offer
def newgame():
    ask= question('Apakah Anda ingin kembali ke Home Menu? (Y/N) ',['Y','N'])
    if ask=='n':
        endgreet()
        numb.clear()
        benar.clear()
        salah.clear()
        return ask
    else:
        numb.clear()
        benar.clear()
        salah.clear()


## Running the Game
while True:
    g=greeting()
    if g=='exit':
        break
    user()
    while True:
        gmn=home()
        if gmn=='exit':
            endgreet()
            break
        main()
        review()
        n= newgame()
        if n=='n':
            break