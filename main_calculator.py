
from tkinter import*
from colorama import Fore

#==================setting===========================
main_surface = Tk()
main_surface.title('calculator')
main_surface.geometry('280x340')
main_surface.resizable(width=False,height=False)
color = 'gray'
main_surface.configure(bg=color)
try :
    photo = PhotoImage(file = 'pic.png')
    main_surface.iconphoto(False, photo)
except:
    print(Fore.RED+'file(pic.png) ra dar folder editor khod gharar dahid')
#====================variables==============
list = []
stri = ''
eaqul = 0
ent_num = StringVar()
ansewr_var = IntVar()
total =''
miangin_total = 0

#====================funcs=================
def one():
    global total
    total += "1"
    ent_num.set(total)
def two():
    global total
    total += '2'
    ent_num.set(total)
def three():
    global total
    total += '3'    
    ent_num.set(total)   
def four():
    global total
    total += "4"
    ent_num.set(total)
def five():
    global total
    total += "5"
    ent_num.set(total)
def six():
    global total
    total += "6"
    ent_num.set(total)
def seven():
    global total
    total += "7"
    ent_num.set(total)
def eight():
    global total
    total += "8"
    ent_num.set(total)
def nine():
    global total
    total += "9"
    ent_num.set(total)

def zero():
    global total
    total += "0"
    ent_num.set(total)

def pl():
    global total
    total += "+"
    ent_num.set(total)

def mi():
    global total
    total += "_"
    ent_num.set(total)

def mul():
    global total
    total += "*"
    ent_num.set(total)
    
def div():
    global total
    total += "/"
    ent_num.set(total)
def power():
    global total
    total+='^'
    ent_num.set(total)
#def percent():
   # global total
   # total+="%"
   # ent_num.set(total)
def negate ():
    global total
    total+='-'
    ent_num.set(total)   
def dot():
    global total
    total+='.'      
    ent_num.set(total)     

def cl():
    global stri
    global total
    global eaqul

    total =''
    stri = ''
    eaqul = 0

    ent_num.set(total)
    ansewr_var.set(total)             
#==============================miangin===========================
def miangin():
    global miangin_total
    count=0
    try:
        miangin_str = total.split('.')
    except:
        print('enter valid numbers')

    for j in miangin_str:
        count += 1
        miangin_total += float(j)

    answer = float(miangin_total/count)
    count=0
    miangin_str = ''
    miangin_total = 0
    ansewr_var.set(answer)
#=============================main func==========================
    
def do() :
    global stri
    stri = ''
    if total != '':

        
        
        for i in total :
            if i  == '*' or i == '+' or i == '/' or i == '_' or i == '^' or i == '%':
            
                list.append(stri)
                stri = i 
                list.append(stri)
                stri = ''
            if i  != '*' and i != '+' and i != '/' and i != '_' and i !='^' and i != '%':
            
                stri +=i
        list.append(stri)   
        for e in list:
        
            if e == "*":
                
                eaqul = float(list[0])*float(list[2])
                del list[0:3]
                break
            
            
            elif e == "/":
                
                
                    eaqul = float(list[0])/float(list[2])
                    del list[0:3]
                    break
            

            
            elif e == "+":
            
                eaqul = float(list[0])+float(list[2])
                del list[0:3]
                break
            
            elif e == "_":
            
                eaqul = float(list[0])-float(list[2])
                del list[0:3]
                break
            elif e == '^':
                eaqul = float(list[0])** float(list[2])
                del list[0:3]
                break

    #==========================second for===================
        le = int((len(list) /2) +1)

        if len(list) > 1:
            for  g in range(1,le):
            
            
                for k in list:
                
                    if k == '*':
                
                        eaqul = eaqul * float(list[1])
                        del list[0:2]
                        break

                    elif k == '/':
                        
                        eaqul = eaqul / float(list[1])
                        del list[0:2]
                        break
                        
                       
                        
                        
                    elif k == '_':
                        
                        eaqul = eaqul - float(list[1])
                        del list[0:2]
                        break
                        
                        
                    elif k == '+':
                        
                        eaqul = eaqul + float(list[1])
                        del list[0:2]
                        break
                    elif k == '^':
                        eaqul = eaqul ** float(list[1])
                        del list[0:2]
                        break
    try:                       
        ansewr_var.set(eaqul) 
    except:
        print('plz enter correct value')
              
   
#=======================frame==========================
first_frame = Frame(main_surface,width=300,height=48,bg=color)
first_frame.pack(side='top')

second_frame = Frame(main_surface,width=300,height=48,bg=color)
second_frame.pack(side='top')

third_frame = Frame(main_surface,width=300,height=48,bg=color)
third_frame.pack(side='top')

fourth_frame = Frame(main_surface,width=300,height=48,bg=color)
fourth_frame.pack(side='top')

fiveth_frame = Frame(main_surface,width=300,height=48,bg=color)
fiveth_frame.pack(side='top')

sixth_frame = Frame(main_surface,width=300,height=48,bg=color)
sixth_frame.pack(side='top')

seventh_frame = Frame(main_surface,width=300,height=48,bg=color)
seventh_frame.pack(side='top')

#==================buttons==================================
but_1 = Button(third_frame,text='1',highlightbackground=color,width=8,height=2,command=lambda:one())
but_1.pack(side='left',padx=2,pady=2)

but_2 = Button(third_frame,text='2',highlightbackground=color,width=8,height=2,command=lambda:two())
but_2.pack(side='left',padx=2,pady=2)

but_3 = Button(third_frame,text='3',highlightbackground=color,width=8,height=2,command=lambda:three())
but_3.pack(side='left',padx=2,pady=2)

but_4 = Button(fourth_frame,text='4',highlightbackground=color,width=8,height=2,command=lambda:four())
but_4.pack(side='left',padx=2,pady=2)

but_5 = Button(fourth_frame,text='5',highlightbackground=color,width=8,height=2,command=lambda:five())
but_5.pack(side='left',padx=2,pady=2)

but_6 = Button(fourth_frame,text='6',highlightbackground=color,width=8,height=2,command=lambda:six())
but_6.pack(side='left',padx=2,pady=2)

but_7 = Button(fiveth_frame,text='7',highlightbackground=color,width=8,height=2,command=lambda:seven())
but_7.pack(side='left',padx=2,pady=2)

but_8 = Button(fiveth_frame,text='8',highlightbackground=color,width=8,height=2,command=lambda:eight())
but_8.pack(side='left',padx=2,pady=2)

but_9 = Button(fiveth_frame,text='9',highlightbackground=color,width=8,height=2,command=lambda:nine())
but_9.pack(side='left',padx=2,pady=2)

but_negate = Button(sixth_frame,text='+/-',highlightbackground=color,width=8,height=2,command=lambda:negate())
but_negate.pack(side='left',padx=2,pady=2)

but_0 = Button(sixth_frame,text='0',highlightbackground=color,width=8,height=2,command=lambda:zero())
but_0.pack(side='left',padx=2,pady=2)

but_plus = Button(third_frame,text='+',highlightbackground=color,width=8,height=2,command=lambda:pl())
but_plus.pack(side='left',padx=2,pady=2)

but_minus = Button(fourth_frame,text='-',highlightbackground=color,width=8,height=2,command=lambda:mi())
but_minus.pack(side='left',padx=2,pady=2)

but_multiply = Button(fiveth_frame,text='*',highlightbackground=color,width=8,height=2,command=lambda:mul())
but_multiply.pack(side='left',padx=2,pady=2)

but_eaqul = Button(sixth_frame,text='=',highlightbackground=color,width=8,height=2,command=lambda:do())
but_eaqul.pack(side='left',padx=2,pady=2)

but_division = Button(sixth_frame,text='/',highlightbackground=color,width=8,height=2,command=lambda:div())
but_division.pack(side='left',padx=2,pady=2)

but_miangin = Button(seventh_frame,text='miangin',highlightbackground=color,width=8,height=2,command=lambda:miangin())
but_miangin.pack(side='left',padx=2,pady=2)

but_cls = Button(seventh_frame,text='clear',highlightbackground=color,width=8,height=2,command=lambda:cl())
but_cls.pack(side='left',padx=2,pady=2)

but_dot = Button(seventh_frame,text='.',highlightbackground=color,width=8,height=2,command=lambda:dot())
but_dot.pack(side='left',padx=2,pady=2)

#but_percent = Button(seventh_frame,text='%',highlightbackground=color,width=9,command=lambda:percent())
#but_percent.pack(side='left',padx=10,pady=8)

but_power = Button(seventh_frame,text='^',highlightbackground=color,width=8,height=2,command=lambda:power())
but_power.pack(side='right',padx=2,pady=2)

#===============================entry and label===============================
lbl_result = Label(main_surface,text='made by aminm08',bg='black',fg="cyan")
lbl_result.pack(side='bottom')

ent_show = Entry(first_frame,highlightbackground=color,textvariable=ent_num)
ent_show.pack(side='top')

ent_result = Entry(second_frame,highlightbackground=color,textvariable=ansewr_var)
ent_result.pack(side='top',pady=8)


main_surface.mainloop()