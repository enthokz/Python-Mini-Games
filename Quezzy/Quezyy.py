import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
# from tkinter import PhotoImage
# from tkinter import ttk
# from tkinter import IntVar
import pandas as pd
import random
from functools import partial



## Data Pemain
list_player= []
list_score= []
def pemain(nama,amount):
    # global a
    if nama in list_player:
        a= list_player.index(nama)
        try:
            if list_score[a]< amount:
                list_score[a]=amount
        except IndexError:
            list_score.insert(a,amount)
    else:
        list_player.insert(0,nama)
        list_score.insert(0, amount)


## Buat Jendela 
main= tk.Tk()
# Window
main.configure(bg="#edf2f4")
main.geometry('500x300')
main.resizable(False,False)
main.title('Quizzy : Quiz of Biology')

## First Page
def tracking(*args):
    x= player_name.get()
    if x:
        tombol_masuk.config(state='normal')
    else:
        tombol_masuk.config(state='disabled')

def greeting():
    global player_name
    global gambar1
    global tombol_masuk
    global input_nama

    # global frame1
    frame1= tk.Frame(main, bg="#edf2f4")
    frame1.place(x=70, y=140,height=60,width=360)
    
    gambar1= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\letterq2.png')
    player_name= tk.StringVar()
    player_name.trace('w',tracking)
    # player_name= nama.get()
    teks1= 'Welcome to Quizzy'
    teks2= 'Nama Player'
#     tk.Label(main,image=gambar1,compound='left').place(relheight=1, x=0)

    tk.Label(main,text=teks1, font=('Comic Sans',15,'bold'),foreground='#3E4784',
              anchor='e',background='#edf2f4',padx=10,
              image=gambar1,compound='left').place(relx=0.49,rely=0.30,anchor='center')
    ttk.Label(frame1,text=teks2,font=('Oswald',9, 'bold'),foreground='#D82149',
              background="#edf2f4", justify='left').pack(anchor='w',padx=70)
    
    input_nama= tk.Entry(frame1,textvariable=player_name,font=('Tahoma',9,'bold'),
                         bg="#F3F3F3",justify='center',width=27)
    input_nama.pack(pady=6, side='bottom',ipady=10)
    input_nama.focus_set()
    # input_nama.insert(0,'Nama Player')

    tombol_masuk= tk.Button(main, text='Masuk', command=home, bg="#293241",
              font=('Comic Sans', 9, 'bold'), disabledforeground="#9E9B9B",foreground="#FFFFFF", 
              state='disabled',relief='raised')
    tombol_masuk.place(relx=0.43, rely=0.70, width=75)

def player_info():
    global gambar2
    gambar2= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\user.png')
    frame6= Frame(main,bg='#F3F3F3', border=0.5)
    frame6.place(relx=0,rely=0, height=40,width=130)

    try:
        cek=list_score[list_player.index(player_name.get())]
    except:
        cek='-'
    # teks= f'Player Info\nName        : {player_name.get()}\nBest Score : {cek}'
    Label(frame6,image=gambar2, compound='left').place(relx=0.08 ,rely=0.2)
    Label(frame6,text=f'{player_name.get()}', font=('tahoma',9,'bold'),justify='left',
          foreground="#D82149",bg='#F3F3F3').place(relx=0.25, rely=0.05)
    Label(frame6,text=f'Best score : {cek}', font=('tahoma',7),justify='left',
          foreground="#D82149", bg='#F3F3F3').place(relx=0.25, rely=0.5)


## Homepage
def aksi_home():
    if (pilihan.get()==0):
        ingame()
    elif (pilihan.get()==1):
        # print(f'Your are {player_name.get()} ')
        aksi_menu2()
    elif (pilihan.get()==2):
        aksi_menu3()
    elif(pilihan.get()==3):
        aksi_menu4()

def aksi_menu2():
    for frame in main.winfo_children():
        frame.destroy()

    frame5=Frame(main)
    frame5.place()
    dict={'nama': list_player,
          'nilai': list_score}
    df= pd.DataFrame(dict)
    df=df.sort_values('nilai', ascending=False)
    d= df.iloc[:3, 0].to_list()
    top=[]
    for i in d:
        top.append(i)
    
    Label(main, text='Top Rank Quizzy', font=('Oswald', 16,'bold')).place(relx=0.45, rely=0.2)

    panjang= len(top)
    besar= [10,8,8]
    indek=0
    if top==[]:
        Label(main, text='Belum ada capaian apapun.\nJadilah yang  pertama memainkan Quizzy!').place(relx=0.2, rely=0.5)
    for i in top:
        if indek<panjang:
            Label(main, text=top[indek], font=('Comic Sans', besar[indek], 'bold')).pack(padx=10, pady=10)
            indek+=1
        else:
            indek=0

    # if len(top)==0:
    #     Label(main, text='Belum ada capaian apapun.\nJadilah yang  pertama memainkan Quizzy!').place(relx=0.2, rely=0.5)
    # elif len(top)==1:
    #     Label(main, text=top[0], font=('Comic Sans', 10, 'bold')).place(relx=0.2, rely=0.5)
    # else:
    #     Label(main, text=top[0], font=('Comic Sans', 10, 'bold')).place(relx=0.2, rely=0.5)
    #     Label(main, text=f'{top[1]}\n{top[2]}').place(relx=0.2, rely=0.6)
    Button(main, text='Back to Home Menu', command=home).place(relx=0.2, rely=0.7)
def aksi_menu3():
    msg=f'Langkah ini akan melakukan:\n  o Hapus capaian\n  o Hapus player jika tidak bermain selepas ini\nApakah kamu yakin ingin melakukannya?'
    tanya= messagebox.askyesnocancel(title='Hapus Capaian',
                                     message=msg)
    if tanya:
        try:
            try:
                del list_score[list_player.index(player_name.get())]
                del list_player[list_player.index(player_name.get())]
                showinfo(title='Hapus Capaian', message='Berhasil hapus capaian player!')
                home()
            except IndexError:
                showinfo(title='Hapus Capaian', message='Tidak capain dari pemain')
        except ValueError:
            showinfo(title='Hapus Capaian', message='Tidak capain dari pemain')
    else:
        print('TIdak')
    home()
def aksi_menu4():
    for frame in main.winfo_children():
            frame.destroy()
    greeting()
    # for frame in main.winfo_children():
    #     frame.destroy()
    
    # Label(main, text='Your Best Achievement', font=('Open Sans',16,'bold',),
    #       foreground="#36B0F7").place(relx=0.2, rely=0.15,height=50,width=300)
    # try:
    #     if player_name.get() in list_player:
    #         print(player_name.get())
    #         print(list_score[list_player.index(player_name.get())])
    #     else:
    #         print('Player belum memiliki pencapaian')
    # except IndexError:
    #     print('Eror. Kontak dev')
    # Button(main, text='Kembali ke Home Menu', command=home).place(relx=0.3, rely=0.8)
def on_enter(event, radio_button, hc):
    radio_button.config(bg=hc, fg='#D82149')
def on_leave(event,radio_button,lc):
    radio_button.config(bg=lc, fg='white')


def home():
    for frame in main.winfo_children():
        frame.destroy()

    frame2= tk.Frame(main, bg="#edf2f4")
    frame2.place(relx=0.23, rely=0.38,height=160,width=270)
    tk.Label(main, text='Beranda',
             font=('Oswald',30, 'bold'),
             foreground='#ee6c4d',bg="#edf2f4",
             justify='center',anchor='w').place(relx=0.34, rely=0.17,height=50,width=300)
    
    global pilihan
    global radio
    pilihan= IntVar()
    pilihan.set(None)
    menu=['Start','Klasemen','Reset Pencapaian','Keluar']
    
    for i in range(len(menu)):
        radio = tk.Radiobutton(frame2, text=menu[i], 
                               variable=pilihan, value=i,width=240, font=('Oswald',13),
                               command=aksi_home,indicatoron=0,offrelief='flat',overrelief='sunken',
                               border=100, borderwidth=3,
                               justify='center',bg='#2b2d42',fg='#FFFFFF',
                               activeforeground="#c54a2b", activebackground="#E6E3E3",selectcolor='#E6E3E3')
        radio.pack(padx=10,pady=3)
        radio.bind("<Enter>", lambda event, button=radio, color='#FFFFFF': on_enter(event,button,color))
        radio.bind("<Leave>", lambda event, button=radio, color='#2b2d42': on_leave(event,button,color))
    player_info()

## Permainan
data= {'index':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
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
benar=[]
salah=[]
def aksi_tombol_next():
    global indek
    jawaban_user= entry_jawaban.get()
    if jawaban_user==list_kunci[indek]:
        benar.append(jawaban_user)
    else:
        salah.append(jawaban_user)
    print(benar)
    indek+=1
    if indek>=len(list_tanya):
        indek=0
        random_num.clear()
        ending()
    else:
        next_question= list_tanya[indek]
        label_tanya.config(text=next_question)
        entry_jawaban.delete(0, tk.END)
        entry_jawaban.focus_set()


def ingame():
    global list_tanya
    global list_kunci
    global random_num
    global indek
    global tombol_next
    global entry_jawaban
    global label_tanya
    for frame in main.winfo_children():
            frame.destroy()

    num=list(range(0,20))
    random_num= random.sample(num,5)
    list_tanya=[]
    list_kunci=[]
    for i in random_num:
        list_tanya.append(data['pertanyaan'][i])
        list_kunci.append(data['jawaban'][i])

    frame3= tk.Frame(main)
    frame3.pack(padx=10, pady=10, fill='x', expand=True)
    indek=0
    label_tanya= tk.Label(frame3, text=list_tanya[indek], wraplength=450)
    label_tanya.pack(padx=10, pady=10, fill='x')
    entry_jawaban= tk.Entry(frame3, justify='center')
    entry_jawaban.pack(padx=10, pady=10, fill='x')
    entry_jawaban.focus_set()
    tombol_next= tk.Button(frame3, text='Next',command=aksi_tombol_next)
    tombol_next.pack(padx=10, pady=10, fill='x')


## Akhir permainan

def aksi_tombol_home():
    benar.clear()
    salah.clear()
    print(list_player)
    print(list_score)
    home()

def ending():
    global tombol_home
    for frame in main.winfo_children():
            frame.destroy()
    
    frame4= tk.Frame(main)
    frame4.pack(padx=10, pady=10, fill='x', expand=True)

    nilai_user= int((len(benar)/len(list_tanya))*100)
    Label(frame4, text=f'Selamat! nilai kamu : {nilai_user}').pack()
    pemain(player_name.get(),nilai_user)

    tombol_home= tk.Button(frame4, text='Kembali ke Home Menu', command=aksi_tombol_home)
    tombol_home.pack()

greeting()


main.mainloop()

# import random
# import math
# import pandas as pd
# ## Dict Petanyaan
# data= {'index':[1,2,3,4,5,6,7,8,9,10],
#        'pertanyaan':['Nama zat hijau daun?',
#                      'Nama kingdom dari hewan sapi?',
#                      'Nama indera perasaa adalah?',
#                      'Nama fragmen darah yang berfungsi untuk membekukan darah?',
#                      'Nama bagian tubuh yang menyambungkan antara tulang dan tulang?',
#                      'Nama alat pernapasan serangga?',
#                      'Nama enzim pengubah karbohidrat menjadi gula?',
#                      'Nama bagian tempat pertukaran oksigen dan CO2 di paru-paru?',
#                      'Nama penyakit yang diakibatkan oleh Salmonella typhi?',
#                      'Nama zat yang mengakibatkan otot lelah?',
#                      'Nama tulang terpanjang yang dimiliki manusia?',
#                      'Nama Saluran yang menghubungkan mulut dengan lambung?',
#                      'Nama gerakan mendorong makanan dari rongga mulut menuju lambung?',
#                      'Nama bagian yang berfungsi mengatur cahaya yang masuk ke mata?',
#                      'Tingkatan taksonomi makhluk hidup di atas species?',
#                      'Istilah makhluk hidup yang memiliki organ reproduksi ganda?',
#                      'Nama otot yang berfungsi untuk menggerakan tubuh secara sadar adalah otot?',
#                      'Nama kemampuan dari makhluk hidup dalam menyamarkan diri dengan lingkungan sekitar disebut?',
#                      'Simbiosis yang menguntungkan kedua belah pihak adalah?',
#                      'Nama saat kondisi tubuh kekurangan sel darah merah?'],
#        'jawaban':['klorofil','animalia','lidah','trombosit','ligamen',
#                   'trakea','amilase','alveolus','tipes','asam laktat','femur',
#                   'kerongkongan','peristaltik','pupil','genus','hemaprodit','lurik','mimikri',
#                   'mutualisme','anemia']}

# ## Exeption handling for Question in Game
# def question(msg,choice):
#     cho= [i.lower() for i in choice]
#     while True:
#         jwb= input(msg).lower()
#         if jwb in cho:
#             return jwb
#         else:
#             print(f'\nCek kembali jawabanmu! Hanya {choice} yang diperbolehkan!')
# def question2(msg,choice):
#     while True:
#         jwb= input(msg).lower()
#         if jwb=='' or jwb=='e':
#             return jwb
#         else:
#             print("Silahkan tekan ENTER untuk melanjutkan atau ketik E' untuk keluar")


# ## Data Pemain
# list_player= []
# list_score= []
# def pemain(nama,amount):
#     if nama in list_player:
#         a= list_player.index(nama)
#         if list_score[a]< amount:
#             list_score[a]=amount
#     else:
#         list_player.append(nama)
#         list_score.append(amount)

# ## Pencaharian
# def cari():
#     while True:
#         try:
#             siapa= input(f'''\n===={'CARI CAPAIAN PEMAIN':^47}====
# Siapa nama user yang ingin Anda cari? ''').lower()
#             a=[]
#             b=[]
#             for i in list_player:
#                 if i==siapa:
#                     a.append(siapa)
#                     b.append(list_score[list_player.index(siapa)])
#             if a!=[]:
#                 print(f"Pemain dengan nama {a[0]} memiliki nilai terbaik {b[0]}")
#             else:
#                 print('Maaf, Nama pemain salah atau belum pernah bermain')
#         except:
#             print('Maaf, Nama tidak ditemukan')
#         r=question(f'\nApakah anda ingin mencari capaian pemain yang lain? (Y/N) ',['Y','N'])
#         if r=='n':
#                 break


# ## Hapus Data
# def hapus():
#     d=question(f'''\n===={'HAPUS CAPAIAN USER':^47}====
# Apakah Kamu yakin ingin menghapus capaian user {put}? (Y/N) ''',['Y','N'])
#     if d=='y':
#         while True:
#             try:
#                 b=list_player.index(put)
#                 n=list_score[b]
#                 list_player.remove(list_player[b])
#                 list_score.remove(n)
#                 print(f'Data pencapaian player {put} berhasil dihapus! ')
#             except:
#                 print(f'Maaf, Nama player tidak ditemukan atau belum memiliki riwayat bermain')
#             input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
#             break

# ## Leaderboard
# def board():
#     dict={'nama':list_player,
#           'nilai':list_score}
#     lead= pd.DataFrame(dict)
#     leaderboard= lead.sort_values('nilai',ascending=False).reset_index(drop=True)
#     if list_player==[]:
#         print(f'''\n===={'LEADERBOARD':^47}====
# Maaf, belum ada data pemain yang tersedia''')
#     else:
#         print(f'''\n===={'LEADERBOARD':^47}====
# {leaderboard.to_string(index=False)}''')
#     input(f'\nSilahkan ketik apapun untuk melanjutkan => ')
        

# ## Greeting
# def greeting():
#     print(f'''{'-'*56}
# |{'Welcome to Quezzy':^54}|
# {'-'*56}''')
#     lanjut=question2(f'{'Silahkan Tekan Enter':^54}',['','E'])
#     if lanjut=='e':
#         return 'exit'

# ## User Name
# def user():
#     global put
#     put= input(f'''
# Siapa Nama player mu? ''')
#     print(f'\nHalo {put}, Bagaimana kabarmu hari ini? Semoga sehat selalu ya.')

# ## Homepage
# def home():
#     while True:
#         q= question(f'''\n===={'HOME MENU':^47}====
# Pilih Menu di bawah ini:
# A. Mulai Permainan
# B. Cek Capaian Pemain
# C. Cek Leadarboard
# D. Hapus Capaian User
# E. Keluar
# Jawab => ''',['A','B','C','D','E'])
#         if q=='a':
#             break
#         elif q=='b':
#             cari()
#         elif q=='e':
#             return 'exit'
#         elif q=='c':
#             board()
#         elif q=='d':
#             hapus()

# ## Question
# # random.shuffle(num)
# def main():
#     global numb
#     global benar
#     global salah
#     num= list(range(0,21))
#     selnum= random.sample(num,5)
#     numb=[]
#     benar=[]
#     salah=[]
#     print(f'''\n===={'MULAI PERMAINAN':^47}====
# Tugas kamu adalah menjawab pertanyaan berikut dengan tepat.\nMari kita mulaiii!''')
#     a=0
#     for i in selnum:
#         if i not in numb:
#             a+=1
#             while True:
#                 af= input(f"\n{a}. {data['pertanyaan'][i]} ").lower()
#                 if af=="":
#                     print(f'\nJawaban tidak boleh kosong!')
#                 elif af!=data['jawaban'][i]:
#                     salah.append(i)
#                     break
#                 else:
#                     benar.append(i)
#                     break
#             numb.append(i)


# ## Result
# def review():
#     nilai=int((len(benar)/len(numb))*100)
#     print(f"\n{'-'*56}")
#     if nilai==100:
#         print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<19}|
# |{'Perfect! Nilai Kamu Sempurna!':^54}|''')
#     elif nilai>=60:
#         print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
# |{'Hebat! Kamu hampir memjawab semua dengan benar':^54}|''')
#     elif nilai>0:
#         print(f'''|{' ':>20}Nilai Kamu: {nilai}{' ':<20}|
# |{'Maaf Nilai mu rendah. Belajar lagi ya':^54}|''')
#     elif nilai==0:
#         print(f'''|{' ':>21}Nilai Kamu: {nilai}{' ':<20}|
# |{'Belajar lagi aja dek!':^54}|''')
#     print(f"{'-'*56}")
#     pemain(put,nilai)
    
# ##  End Greeting
# def endgreet():
#     print(f'''\n{'-'*56}
# |{'Terima Kasih Sudah Bermain!':^54}|
# {'-'*56}\n''')
    
# ## Newgame Offer
# def newgame():
#     ask= question('Apakah Anda ingin kembali ke Home Menu? (Y/N) ',['Y','N'])
#     if ask=='n':
#         endgreet()
#         numb.clear()
#         benar.clear()
#         salah.clear()
#         return ask
#     else:
#         numb.clear()
#         benar.clear()
#         salah.clear()


# ## Running the Game
# while True:
#     g=greeting()
#     if g=='exit':
#         break
#     user()
#     while True:
#         gmn=home()
#         if gmn=='exit':
#             endgreet()
#             break
#         main()
#         review()
#         n= newgame()
#         if n=='n':
#             break