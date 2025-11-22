# while True:
#     try:
#         msg= str(input('PIlih nomor bereapa?'))
#         print(msg)
#         break
#     except:
#         print('ANda memasukan pilihan yang salah')

import re
# def coba(msg,pilihan):
#     while True:
#         form= str(input(msg))
#         while not re.match(r'\d',form):
#             print('cek kembali!')
#             form= input(msg)
#         if form in pilihan:
#             break
#         else:
#             print('Jawaban tidak ada dalam pilihan, Cek kambali!')
#     print (f'Jabawan adalah {form}')

# coba('No berapa yang kamu pilih?',['1','2'])

# Harus habis dibagi dua dan kelipatan 5
# def coba():
#     while True:
#         put= int(input('Masukan Angka!'))
#         if put %2 !=0:
#             print('Tidak bisa dibagi dua')
#         if put %5 !=0:
#             print('Tidak bisa habis dibagi lima')
#         elif put %2==0 and put %5==0:
#             break
#     while put<40:
#         print(put)
#         put+=1
# coba()

# Dict Petanyaan
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
import random
import math

# def user():
#     put= input(f'''
# {'-'*55:^10}
# |{'Welcome':^53}|
# {'-'*55}\n
# Siapa Namamu?''')
#     print(f'Hai {put}, Harap jawab beberapa pertanyaan di bawah ini.\n Mari kita mulai!')

def user():
    put= input(f'''{'-'*56}
|{'Welcome to Quezzy':^54}|
{'-'*56}
Siapa Namamu? ''')
    print(f'\nHai {put}, Tugas kamu adalah menjaawab pertanyaan berikut dengan tepat.\nMari kita mulaiii!')


num= list(range(0,10))
# random.shuffle(num)
selnum= random.sample(num,5)
numb=[]
benar=[]
salah=[]
def main():
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
    
def review():
    print(f'''\n{'-'*56}
|{' ':>22}Nilai Kamu {int((len(benar)/5)*100)}{' ':<19}|
{'-'*56}
Anda berhasil menjawab benar {len(benar)} soal
Terima kasih sudah bermain!\n''')
    

user()
main()
review()


