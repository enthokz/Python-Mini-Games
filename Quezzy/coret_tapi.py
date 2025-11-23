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
import random
import math

## User Name
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
    
    
## Exeption handling for Question
def question(msg,choice):
    cho= [i.lower() for i in choice]
    while True:
        jwb= input(msg).lower()
        if jwb in cho:
            return jwb
        else:
            print(f'\nCek kembali jawabanmu! Hanya {choice} yang diperbolehkan!')

## Running the Game
while True:
    user()
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