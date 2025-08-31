# Mari kita membuat mini games!
# Membuat permainan bahlil v.1.0

# Membuat gretings/ welcome
greeting=' SELAMAT DATANG'
print('------------------------------------------------------------------------')
print(f'|                           {greeting}                            |')
print('------------------------------------------------------------------------')
print('Mari kita sedikit bermain permainan')

# Membuat input nama player
player_name=input('Masukan Nama Player : ')

# Membuat deskripsi permainan
print(f'''\n
------------------------------------------------------------------------
Selamat Datang {player_name} di permainan ini!\n''')
print('''Permainannya cukup mudah. Mari kita menangkap bahlil!
Bahlil saat ini sedang bersembunyi di goa berikut:
      |1|  |2|  |3|  |4|''')

# Membuat input jawaban permainan
quetion=int(input('Menurutmu ada di goa nomor berapakah bahlil bersembunyi? '))
quetion_answer=quetion
while quetion_answer:
    if quetion_answer not in[1,2,3,4]:
        print('Cek kembali yuk jawabanmu! Goa yang menjadi persembunyian bahlil hanya 1 hingga 4')
        quetionn=int(input('Menurutmu ada di goa nomor berapakah bahlil bersembunyi? '))
        quetion_answer=quetionn
    elif quetion_answer in[1,2,3,4]:
        break
print('\n')
confirm=input(f'Apakah kamu yakin bahwa bahlil ada di goa {quetion_answer} ? (Y/N)')
confirm_answer=confirm

# Membuat Hasil 
import random
answer=random.randint(1,4)

#Menampilkan hasil dengan syarat user sudah yakin dengan jawaban ('Y')
while confirm_answer:
    if confirm_answer not in['Y','N']:
        print('Maaf, jawaban konfirmasi yang diterima hanya jawaban Y dan N')
        quetion=int(input('Coba lagi yuk! Menurutmu ada di goa nomor berapakah bahlil bersembunyi seharusnya? '))
        while quetion:
            if quetion not in[1,2,3,4]:
                print('Cek kembali yuk jawabanmu! Goa yang menjadi persembunyian bahlih hanya 1 hingga 4')
                quetionn=int(input('Menurutmu ada di goa nomor berapakah bahlil bersembunyi? '))
                quetion=quetionn
            elif quetion in[1,2,3,4]:
                 break
        confirmm=input(f'Apakah kamu yakin bahwa bahlil ada di goa {quetion} ? (Y/N)')
        confirm_answer=confirmm

    elif confirm_answer=='N':
        quetion=int(input('Lalu menurutmu ada di goa nomor berapakah bahlil bersembunyi seharusnya? '))
        while quetion:
            if quetion not in[1,2,3,4]:
                print('Cek kembali yuk jawabanmu! Goa yang menjadi persembunyian bahlih hanya 1 hingga 4')
                quetionn=int(input('Menurutmu ada di goa nomor berapakah bahlil bersembunyi? '))
                quetion=quetionn
            elif quetion in[1,2,3,4]:
                 break
        confirmm=input(f'Apakah kamu yakin bahwa bahlil ada di goa {quetion} ? (Y/N)')
        confirm_answer=confirmm

    elif confirm_answer=='Y':
        if quetion==answer:
            print(f'''
------------------------------------------------------------------------
Yeay selamat {player_name}!! Kamu bisa menagkap bahlil !!
Goa {quetion} seperti yang kamu jawab memang menjadi tempat persembunyian Bahlil.
------------------------------------------------------------------------''')
        else:
            print(f'''
------------------------------------------------------------------------
Sayang sekali bahlil belum bisa tertangkap.
Kamu menjawab goa {quetion} padahal bahlil bersembunyi di goa {answer}
------------------------------------------------------------------------''')
        break