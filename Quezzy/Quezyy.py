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
    
    global gambar3
    gambar3= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\sad-square-svgrepo-com (1).png')
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
    
    Label(main, text='Top Rank Quizzy', font=('Oswald', 28,'bold'),
          foreground='#3E4784', bg='#edf2f4').place(relx=0.2, rely=0.06)

    global gambar4
    gambar4= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\pngkey.com-tachanka-png-8227726 (1).png')
    global gambar5
    gambar5= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\second-rank.png')
    global gambar6
    gambar6= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\third-rank (1).png')

    panjang= len(top)
    besar= [22,16,16]
    pad=[0.35, 0.56, 0.69]
    # pad=[50,3,3]
    gambar=[gambar4,gambar5,gambar6]
    indek=0
    if top==[]:
        Label(main, text='Belum ada capaian apapun.\nJadilah yang  pertama memainkan Quizzy!',
              font=('Oswald', 11, 'bold'), image=gambar3, compound='top', bg='#edf2f4').place(relx=0.22, rely=0.35)
    for i in top:
        if indek<panjang:
            Label(main, text=top[indek], font=('Comic Sans', besar[indek], 'bold'),
                  justify='center',anchor='center',foreground='#D82149',background='#edf2f4',
                  image=gambar[indek], compound='left',padx=10).place(relx=0.5, rely=pad[indek], anchor='center')
            indek+=1
        else:
            indek=0

    Button(main, text='Kembali ke Beranda', command=home,bg="#293241",
              font=('Comic Sans', 9, 'bold'),foreground="#FFFFFF", 
              relief='raised').place(relx=0.39, rely=0.85)
    
def aksi_menu3():
    msg=f'Langkah ini akan melakukan:\n  o Hapus capaian pemain.\n  o Hapus player jika tidak bermain selepas ini.\nApakah kamu yakin ingin melakukannya?'
    tanya= messagebox.askyesno(title='Hapus Capaian',
                                     message=msg)
    if tanya:
        try:
            try:
                del list_score[list_player.index(player_name.get())]
                del list_player[list_player.index(player_name.get())]
                showinfo(title='Hapus Capaian', message='Berhasil hapus capaian player!')
                home()
            except IndexError:
                showinfo(title='Hapus Capaian', message='Tidak capaian dari pemain')
        except ValueError:
            showinfo(title='Hapus Capaian', message='Tidak capaian dari pemain')
    # else:
    #     print('TIdak')
    home()

def aksi_menu4():
    for frame in main.winfo_children():
            frame.destroy()
    greeting()
   
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
    jawaban_user= entry_jawaban.get().lower()
    if jawaban_user==list_kunci[indek]:
        benar.append(jawaban_user)
    else:
        salah.append(jawaban_user)
    # print(benar)
    indek+=1
    if indek>=len(list_tanya):
        indek=0
        random_num.clear()
        
        ending()
    else:
        # color=[None,'#F3F3F3'f,'#D82149','#F3F3F3','#D82149']
        # frame3.configure(bg=color[indek])
        next_question= list_tanya[indek]
        label_tanya.config(text=next_question)
        entry_jawaban.delete(0, tk.END)
        entry_jawaban.focus_set()
def delete():
    entry_jawaban.delete(0,END)

def ingame():
    global frame3
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

    frame3= tk.Frame(main, bg='#F3F3F3')
    frame3.pack(padx=10, pady=10, fill='x', expand=True)
    indek=0

    label_tanya= tk.Label(frame3, text=list_tanya[indek], wraplength=450,
                          background='#F3F3F3', foreground='#D82149', font=('Tahoma',13))
    label_tanya.pack(padx=10, pady=30, fill='x')

    entry_jawaban= tk.Entry(frame3, justify='center', font=('Tahoma',10), background="#FAFAFA")
    entry_jawaban.pack(padx=10, pady=10, fill='x', ipady=4)
    entry_jawaban.focus_set()

    tombol_next= tk.Button(frame3, text='Next',command=aksi_tombol_next,
                           background='#293241', font=('Comic Sans',9, 'bold'),
                           foreground='#FFFFFF')
    tombol_next.pack(padx=10, pady=10, fill='x')

    delete_button= Button(frame3,text='Delete', command=delete,
                          background="#93969B", font=('Comic Sans',9, 'bold'),
                          foreground='#FFFFFF')
    delete_button.pack(padx=10, pady=1,fill='x')


## Akhir permainan

def aksi_tombol_home():
    benar.clear()
    salah.clear()
    list_tanya.clear()
    list_kunci.clear()
    home()

def aksi_tombol_exit():
    benar.clear()
    salah.clear()
    list_tanya.clear()
    list_kunci.clear()
    for frame in main.winfo_children():
            frame.destroy()
    greeting()

def ending():
    global tombol_home
    global gambar7
    gambar7= PhotoImage(file=r'C:\Users\Fahrul\Documents\python\tkinter_GUI\achievement-challenge-medal-svgrepo-com (1).png')
    for frame in main.winfo_children():
            frame.destroy()
    
    frame4= tk.Frame(main, bg='#edf2f4')
    frame4.place(relx=0.31, rely=0.2)
    nilai_user= int((len(benar)/len(list_tanya))*100)
    
    Label(frame4, text=f'Selamat! nilai kamu :', font=('Tahoma', 13, 'bold'), foreground='#3E4784',
          image=gambar7, compound='top', background='#edf2f4').pack()
    Label(frame4, text=f'{nilai_user}', font=('Comic Sans', 24, 'bold'),foreground='#D82149',
          background='#edf2f4').pack()
    pemain(player_name.get(),nilai_user)

    tombol_home= tk.Button(main, text='Kembali ke Beranda', bg="#293241",
              font=('Comic Sans', 9, 'bold'),foreground="#FFFFFF", 
              relief='raised', command=aksi_tombol_home)
    tombol_home.place(relx=0.37, rely=0.7)

    tombol_exit= tk.Button(main, text='Keluar', bg="#293241",
              font=('Comic Sans', 9, 'bold'),foreground="#FFFFFF", 
              relief='raised', command=aksi_tombol_exit)
    tombol_exit.place(relx=0.45, rely=0.8)

greeting()


main.mainloop()