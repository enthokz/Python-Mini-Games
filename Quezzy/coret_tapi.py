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


## Buat Kelas Database player
class player:
    def __init__ (self, player):
        self.player=player
        self.daftar=[]
        self.nilai=[]
    def pemain(self,nama,amount):
        self.nama=nama
        self.amount=amount
        if nama in self.daftar:
            a= self.daftar.index(nama)
            self.daftar[a]=nama
            if self.nilai[a]<amount:
                self.nilai[a]=amount
        else:
            self.daftar.append(nama)  
            self.nilai.append(amount)  
    def hapus(self, apus):
        self.apus=apus
        while True:
            try:
                b= self.daftar.index(apus)
                c= self.nilai[b]
                self.daftar.remove(self.daftar[b])
                self.nilai.remove(c)
                print(f'Data pencapaian {apus} berhasil dihapus!')
                break
            except:
                print('Nama yang kamu masukan tidak ada!')
                break
    def board(self):
        dic= {'Nama': self.daftar,
              'Nilai': self.nilai}
        lead= pd.DataFrame(dic)
        leaderboard= lead.sort_values('Nilai',ascending=False).reset_index(drop=True)
        if self.daftar==[]:
            print(f'''\n===={'LEADERBOARD':^47}====
Maaf, belum ada data pemain yang tersedia''')
        else:
            print(f'''\n===={'LEADERBOARD':^47}====
{leaderboard.to_string(index=False)}''')
    
user= player('person')

# Pencaharian
def cari():
    while True:
        a=[]
        b=[]
        siapa= input(f'''\n===={'CARI CAPAIAN PEMAIN':^47}====
Siapa nama user yang ingin Anda cari? ''').lower()
        for i in user.daftar:
            if i==siapa:
                a.append(i)
                b.append(user.nilai[user.daftar.index(i)])
        if a==[]:
            print('Nama tidak ditemukan')
        else:
            print(f"Pemain dengan nama {a[0]} memiliki nilai terbaik {b[0]}")
        r=question(f'\nApakah anda ingin mencari yang lain? (YA/TIDAK) ',['Ya','Tidak'])
        if r=='tidak':
            break


## Exeption handling for Question
def question(msg,choice):
    cho= [i.lower() for i in choice]
    while True:
        jwb= input(msg).lower()
        if jwb in cho:
            return jwb
        else:
            print(f'\nCek kembali jawabanmu! Hanya {choice} yang diperbolehkan!')

## Header Greetings
def greeting():
    print(f'''{'-'*56}
|{'Welcome to Quezzy':^54}|
{'-'*56}''')
    
# ## User Name
def pemain():
    global put
    put= input(f'''
Siapa Nama player mu? ''')
    print(f'Halo {put}, Bagaimana kabarmu hari ini? Semoga sehat selalu ya.')

## Homepage
def home():
    while True:
        q= question(f'''===={'HOME MENU':^47}====
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
            user.board()
            input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
        elif q=='d':
            d=question(f'''\nn===={'HAPUS CAPAIAN USER':^47}====
Apakah Kamu yakin ingin menghapus capaian user {put}? (YA/TIDAK) ''',['YA','TIDAK'])
            if d=='ya':
                user.hapus(put)
                input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
# home()
# user()


# # Question
num= list(range(0,10))
# random.shuffle(num)
selnum= random.sample(num,5)
numb=[]
benar=[]
salah=[]
def main():
    print(f'''\n===={'MULAI PERMAINAN':^47}====
Tugas kamu adalah menjaawab pertanyaan berikut dengan tepat.\nMari kita mulaiii!''')
    while True:
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
        break

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
    user.pemain(put,nilai)

# print(user.daftar)
# ## Running the Game

greeting()
pemain()
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