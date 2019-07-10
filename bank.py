#let import the required library.
from tkinter import* #for creation of the frame and other forms of GUI
import random #FOR genelation of random numbers5
import numpy as py #arragement of the numbers from files
import os # for refferencing of file outside the programe
import time; # to generate time
import csv #ussed for importing (csv) comma separated variable
data='login.txt' #import the login database

#from PIL import Image, ImageTk
def repay():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("REPAYMENT ACCOUNT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="REPAYMENT ACCOUNT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="REPAYMENT ACCOUNT",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

  
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("REPAYMENT ACCOUNT")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="REPAYMENT ACCOUNT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)

        
            

        def reset1():
                loan_amount.set("0")

        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="**",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        depos="MEM_D"+name1+"."+"txt"
        lon="MEM_L"+name1+"."+"txt"
        sav="MEM_S"+name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loanlimit=str((0))


            with open(depos) as d:
                dat_d=d.readlines()
                dat_d1=dat_d[0].rstrip()
            with open(lon) as d:
                dat_d=d.readlines()
                dat_l1=dat_d[0].rstrip()
            with open(sav) as d:
                dat_d=d.readlines()
                dat_s1=dat_d[0].rstrip()

            loanlimit1=float(dat_s1)-200-float(dat_l1)

            if loanlimit1<200:
            	Loanlimit=0
            	ll=0

            else:
            	Loanlimit=loanlimit1
            	ll=Loanlimit-300
            Lan1=(float(dat_d1)-200)
            if (Lan1-200)<1:
            	Lan=0
            else:
            	Lan=Lan1


                



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=dat_d1,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=dat_s1,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=dat_l1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=Loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=ll,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset1).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)








            
            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 reset1()
                 with open(lon) as j:
                     data=j.readlines()
                     val=data[0].rstrip()
                     tot=float(val)-float(name1)
                 with open(lon,'w') as l:
                     l.write(str(tot))
                     
                 test_loan=int(name1)
                 tot2=float(test_loan+int(balance))
                 
                 if -1 >float(val):
                     lnTM=Label(f1,font=('arial',10),text="accunt is domant",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if float(val)>-1:
                         """loan_period=tot2
                     




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu"""
                     lnTM=Label(f1,font=('arial',10),text="deposit completed",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     #textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     #textloan.grid(row=7,column=5)
                     #lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     #lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount in loan  account is:",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=tot,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

            
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="submit:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()


##################### CREEATING THE SAVING ACCCOUNT

def sav():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("SAVING ACCOUNT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="SAVING ACCOUNT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="SAVINGS ACCOUNT",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("SAVINGS ACCOUNT")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="SAVINGS ACCOUNT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)

        
            

        def reset1():
                loan_amount.set("0")

        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="**",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        depos="MEM_D"+name1+"."+"txt"
        lon="MEM_L"+name1+"."+"txt"
        sav="MEM_S"+name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loanlimit=str((0))


            with open(depos) as d:
                dat_d=d.readlines()
                dat_d1=dat_d[0].rstrip()
            with open(lon) as d:
                dat_d=d.readlines()
                dat_l1=dat_d[0].rstrip()
            with open(sav) as d:
                dat_d=d.readlines()
                dat_s1=dat_d[0].rstrip()

            loanlimit1=float(dat_s1)-200-float(dat_l1)

            if loanlimit1<200:
            	Loanlimit=0
            	ll=0

            else:
            	Loanlimit=loanlimit1
            	ll=Loanlimit-300
            Lan1=(float(dat_d1)-200)
            if (Lan1-200)<1:
            	Lan=0
            else:
            	Lan=Lan1


                



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=dat_d1,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=dat_s1,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=dat_l1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=Loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=ll,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset1).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)








            
            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 reset1()
                 with open(sav) as j:
                     data=j.readlines()
                     val=data[0].rstrip()
                     tot=float(val)+float(name1)
                 with open(sav,'w') as l:
                     l.write(str(tot))
                     
                 test_loan=int(name1)
                 tot2=float(test_loan+int(balance))
                 
                 if -1 >float(val):
                     lnTM=Label(f1,font=('arial',10),text="accunt is domant",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if float(val)>-1:
                         """loan_period=tot2
                     




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu"""
                     lnTM=Label(f1,font=('arial',10),text="deposit completed",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     #textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     #textloan.grid(row=7,column=5)
                     #lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     #lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount in saving  account is:",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=tot,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

            
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="submit:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()
##CREATING LOAN ACCOUNT FUNCTION



def lon1():
    
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("LOAN ACCOUNT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="LOAN ACCOUNT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="LOAN ACCOUNT",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("LOAN ACCOUNT")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="LOAN ACCOUNT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)

        
            

        def reset1():
                loan_amount.set("0")

        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="***",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        depos="MEM_D"+name1+"."+"txt"
        lon="MEM_L"+name1+"."+"txt"
        sav="MEM_S"+name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loanlimit=str((0))


            with open(depos) as d:
                dat_d=d.readlines()
                dat_d1=dat_d[0].rstrip()
            with open(lon) as d:
                dat_d=d.readlines()
                dat_l1=dat_d[0].rstrip()
            with open(sav) as d:
                dat_d=d.readlines()
                dat_s1=dat_d[0].rstrip()

            loanlimit1=float(dat_s1)-200-float(dat_l1)

            if loanlimit1<200:
            	Loanlimit=0
            	ll=0

            else:
            	Loanlimit=loanlimit1
            	ll=Loanlimit-300
            Lan1=(float(dat_d1)-200)
            if (Lan1-200)<1:
            	Lan=0
            else:
            	Lan=Lan1
            
                



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=dat_d1,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=dat_s1,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=dat_l1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=Loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=ll,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset1).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)








            
            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 reset1()
                 with open(lon) as j:
                     data=j.readlines()
                     val=data[0].rstrip()
                     tot=float(val)+float(name1)
                 with open(lon,'w') as l:
                     l.write(str(tot))
                     
                 test_loan=int(name1)
                 tot2=float(test_loan+int(balance))
                 
                 if tot >float(Lan):
                     lnTM=Label(f1,font=('arial',10),text="minimal withdraw is 200",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if tot<float(Lan):
                         """loan_period=tot2
                     




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu"""
                     lnTM=Label(f1,font=('arial',10),text="loan request  completed",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     #textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     #textloan.grid(row=7,column=5)
                     #lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     #lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount off loan in account is:",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=tot,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

            
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="submit:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()
###############################################################################################
#CREATING WITHDRAW  FUNCTION



def withd():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("WITHDRAW ACCOUNT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="WITHDRAW ACCOUNT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="loan cash",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("WITHDRAW ACCOUNT")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="WITHDRAW ACCOUNT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)

        
            

        def reset1():
                loan_amount.set("0")

        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="***",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        depos="MEM_D"+name1+"."+"txt"
        lon="MEM_L"+name1+"."+"txt"
        sav="MEM_S"+name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loanlimit=str((0))


            with open(depos) as d:
                dat_d=d.readlines()
                dat_d1=dat_d[0].rstrip()
            with open(lon) as d:
                dat_d=d.readlines()
                dat_l1=dat_d[0].rstrip()
            with open(sav) as d:
                dat_d=d.readlines()
                dat_s1=dat_d[0].rstrip()

            loanlimit1=float(dat_s1)-200-float(dat_l1)

            if loanlimit1<200:
            	Loanlimit=0
            	ll=0

            else:
            	Loanlimit=loanlimit1
            	ll=Loanlimit-300
            Lan1=(float(dat_d1)-200)
            if (Lan1-200)<1:
            	Lan=0
            else:
            	Lan=Lan1
            
                



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=dat_d1,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=dat_s1,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=dat_l1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=Loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=ll,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset1).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)








            
            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 reset1()
                 with open(depos) as j:
                     data=j.readlines()
                     val=data[0].rstrip()
                     tot=float(val)-float(name1)
                 with open(depos,'w') as l:
                     l.write(str(tot))
                     
                 test_loan=int(name1)
                 tot2=float(test_loan+int(balance))
                 
                 if tot <200:
                     lnTM=Label(f1,font=('arial',10),text="minimal withdraw is 200",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if tot>200:
                         """loan_period=tot2
                     




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu"""
                     lnTM=Label(f1,font=('arial',10),text="deposit completed",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     #textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     #textloan.grid(row=7,column=5)
                     #lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     #lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount in account is:",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=tot,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

            
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="submit:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()
#############################
#CREATING THE DEPOSIT FUNCTION




def depo():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("DEPOSIT ACCOUNT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="DEPOSIT ACCOUNT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="DEPOSIT ACCOUNT",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("DEPOSIT ACCOUNT")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="DEPOSIT ACCOUNT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)

        
            

        def reset1():
                loan_amount.set("0")

        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="**",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        depos="MEM_D"+name1+"."+"txt"
        lon="MEM_L"+name1+"."+"txt"
        sav="MEM_S"+name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loanlimit=str((0))


            with open(depos) as d:
                dat_d=d.readlines()
                dat_d1=dat_d[0].rstrip()
            with open(lon) as d:
                dat_d=d.readlines()
                dat_l1=dat_d[0].rstrip()
            with open(sav) as d:
                dat_d=d.readlines()
                dat_s1=dat_d[0].rstrip()

            loanlimit1=float(dat_s1)-200-float(dat_l1)

            if loanlimit1<200:
            	Loanlimit=0
            	ll=0

            else:
            	Loanlimit=loanlimit1
            	ll=Loanlimit-300
            Lan1=(float(dat_d1)-200)
            if (Lan1-200)<1:
            	Lan=0
            else:
            	Lan=Lan1
            
                



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=dat_d1,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=dat_s1,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=dat_l1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=Loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=Lan,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset1).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)








            
            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 reset1()
                 with open(depos) as j:
                     data=j.readlines()
                     val=data[0].rstrip()
                     tot=float(val)+float(name1)
                 with open(depos,'w') as l:
                     l.write(str(tot))
                     
                 test_loan=int(name1)
                 tot2=float(test_loan+int(balance))
                 
                 if -1 >float(val):
                     lnTM=Label(f1,font=('arial',10),text="accunt is domant",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if float(val)>-1:
                         """loan_period=tot2
                     




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu"""
                     lnTM=Label(f1,font=('arial',10),text="deposit completed",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     #textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     #textloan.grid(row=7,column=5)
                     #lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     #lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount in account is:",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=tot,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

            
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="submit:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()

def DEPO_FUN():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("DEPOSIT")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="DEPOSIT",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="DEPOSIT",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("DEPOSI")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="DEPOSIT",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)


        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="loan cash",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        data=name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile,"a+") as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>0:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loan_limit=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=balance,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=savec,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=loan,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=loan_limit,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=d,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER DEPOSIT AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)










            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 test_loan=int(name1)
                 with open(data) as k:
                     data1=j.readlines()
                     data2=data1[0].rstrip()
                     data3=float(data2)+ test_loan
                 with open(data,'w') as k:
                     k.write(data3)
                 
                 loan_limit1=int(loan_limit)
                 if test_loan >loan_limit1:
                     lnTM=Label(f1,font=('arial',10),text="LOAN not aplicable",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if test_loan<999:
                         loan_period=3
                     else:
                         if test_loan>999 & test_loan<4999:
                             loan_period=6
                         else:
                             if test_loan>4999 & test_loan<9999:
                                 loan_period=12
                             else:
                                 if test_loan>9999 & test_loan<14999:
                                     loan_period=15
                                 else:
                                     if test_loan>14999 & test_loan<19999:
                                         loan_period=18
                                     else:
                                         if test_loan>19999 & test_loan<24999:
                                             loan_period=21
                                         else:
                                             if test_loan>24999 :
                                                 loan_period=24




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu
                     lnTM=Label(f1,font=('arial',10),text="LOAN aplicable",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     textloan.grid(row=7,column=5)
                     lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount to be paid",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=payable_amount,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

                     reset()
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="LOADATA:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    
         
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()





def LOAD_DATA_PROFILE():
    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&77
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("loan cash")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="loan cash",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)


    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="loan cash",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)

    
    member_ID=StringVar()
    #++++++++++++++++++++++++++
    def LOAD_DATA_PROFILE():
        root2=Tk()
        root2.geometry("1350x700+0+0")
        root2.title("loan cash")
        Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
        Tops.pack(side=TOP)
        f1=Frame(root2,width=1200,height=1000,relief=RAISED)
        f1.pack()
        localtime=time.asctime(time.localtime(time.time()))
        lninfo=Label(Tops,font=('arial',20),text="loan cash",fg="black",bd=5,anchor='w')
        lninfo.grid(row=0,column=0)
        lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
        lnbinf.grid(row=1,column=0)


        def logout():
            root2.destroy()
            login()

        #create the actual button
        btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

        lntit=Label(f1,font=('arial',20),text="loan cash",fg="black",bd=15,anchor='w')
        lntit.grid(row=0,column=2)

        name1=member_ID.get()
        data_form=name1+"."+"txt"
        userfile=data_form
        if os.path.isfile(userfile):
            with open(userfile) as j:
                     data1=j.readlines()
                     accno=data1[0].rstrip()
                     idno=data1[1].rstrip()
                     sirname=data1[2].rstrip()
                     mindlename=data1[3].rstrip()
                     lastname=data1[4].rstrip()
                     
                     
                     savec=data1[5].rstrip()
                     balance=data1[6].rstrip()
                     loanlimit=data1[7].rstrip()
                     loan=data1[8].rstrip()
                     totoal_save=data1[9].rstrip()
                     loanable=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)

                     if int(balance)>300:
                         ban=int(balance)
                         d=ban-200
                         d1=200-100

                     else:
                        d=0
                        d1=0
                     if int(loan)>loanable:
                         loan_limit=0


                     else:
                         
                       loan_limit=int(totoal_save)*0.3+(int(savec)*0.8)-int(loan)



            lnNAME1=Label(f1,font=('arial',15),bg="blue",text="BIO DATA",fg="black",bd=15,anchor='w')
            lnNAME1.grid(row=0,column=2)

            lnNAME=Label(f1,font=('arial',10),text="MEMBER ID",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=1,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SIR NAME ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=2,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="FIRST NAME",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=3,column=0)
            lnTM=Label(f1,font=('arial',10),text="LAST NAME",fg="black",bd=15,anchor='w')
            lnTM.grid(row=4,column=0)
            lnacc=Label(f1,font=('arial',10),text="AGENTS NO:",fg="black",bd=15,anchor='w')
            lnacc.grid(row=1,column=2)

            AGENTS_ID=StringVar()
            sir_name=StringVar()
            first_name=StringVar()
            last_name=StringVar()
            loan_amount=StringVar()
            MESSAGE=StringVar()
            def reset():
                AGENTS_ID.set("")
                sir_name.set("")
                first_name.set("")
                last_name.set("")
            def BACK():
                
                root2.destroy()
                menu()


            textmember_ID=Label(f1,font=('arial',10,'bold'),bg="blue",text=idno,fg="black",bd=15,anchor='w')
            textmember_ID.grid(row=1,column=1)
            textTIT=Label(f1,font=('arial',10,'bold'),bg="yellow",text=sirname,fg="black",bd=15,anchor='w')
            textTIT.grid(row=2,column=1)
            textAUT=Label(f1,font=('arial',10,'bold'),bg="blue",text=mindlename,fg="black",bd=15,anchor='w')
            textAUT.grid(row=3,column=1)
            textPUB=Label(f1,font=('arial',10,'bold'),bg="yellow",text=lastname,fg="black",bd=15,anchor='w')
            textPUB.grid(row=4,column=1)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text=accno,fg="black",bd=15,anchor='w')
            textACC.grid(row=1,column=3)
            textACC=Label(f1,font=('arial',10,'bold'),bg="blue",text="ACCOUNT DETAILS",fg="black",bd=15,anchor='w')
            textACC.grid(row=5,column=2)

            lnNAME=Label(f1,font=('arial',10),text="BALANCE",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=0)
            lnIDNO=Label(f1,font=('arial',10),text=" SAVING ACCOUNT BALANCE: ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=0)
            lnmember_ID=Label(f1,font=('arial',10),text="LOAN ACCOUNT BALANCE",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=0)
            lnTM=Label(f1,font=('arial',10),text="LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=0)

            lnNAME=Label(f1,font=('arial',10),text=balance,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=6,column=1)
            lnIDNO=Label(f1,font=('arial',10),text=savec,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=7,column=1)
            lnmember_ID=Label(f1,font=('arial',10),text=loan,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=1)
            lnTM=Label(f1,font=('arial',10),text=loanlimit,fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=1)#

            lnNAME=Label(f1,font=('arial',10),text="MAX LOAN LIMIT",fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=2)
            lnIDNO=Label(f1,font=('arial',10),text="MAX AMOUNT TO BE WITHRAW ",fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=2)
            lnmember_ID=Label(f1,font=('arial',10),text="MINMUM TO BE WITHDRAW",fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=2)
            lnTM=Label(f1,font=('arial',10),text="OFFER",fg="black",bd=15,anchor='w')
            lnTM.grid(row=9,column=2)


            lnNAME=Label(f1,font=('arial',10),text=loan_limit,fg="black",bd=15,anchor='w')
            lnNAME.grid(row=7,column=3)
            lnIDNO=Label(f1,font=('arial',10),text=d,fg="black",bd=15,anchor='w')
            lnIDNO.grid(row=6,column=3)
            lnmember_ID=Label(f1,font=('arial',10),text=d1,fg="black",bd=15,anchor='w')
            lnmember_ID.grid(row=8,column=3)
            lnTM=Label(f1,font=('arial',10),text="ENTER THE AMOUNT",fg="black",bd=15,anchor='w')
            lnTM.grid(row=6,column=4)
            textloan=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=loan_amount,insertwidth=7,bd=5,justify='right')
            textloan.grid(row=6,column=5)
            btrest=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="reset:",bg="powder blue",command=reset).grid(row=9,column=2)
            btback=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=9,column=4)










            def LOAD_DATA():# creating the submit button
                 name1=loan_amount.get()
                 test_loan=int(name1)
                 loan_limit1=int(loan_limit)
                 if test_loan >loan_limit1:
                     lnTM=Label(f1,font=('arial',10),text="LOAN not aplicable",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                 else :
                     if test_loan<999:
                         loan_period=3
                     else:
                         if test_loan>999 & test_loan<4999:
                             loan_period=6
                         else:
                             if test_loan>4999 & test_loan<9999:
                                 loan_period=12
                             else:
                                 if test_loan>9999 & test_loan<14999:
                                     loan_period=15
                                 else:
                                     if test_loan>14999 & test_loan<19999:
                                         loan_period=18
                                     else:
                                         if test_loan>19999 & test_loan<24999:
                                             loan_period=21
                                         else:
                                             if test_loan>24999 :
                                                 loan_period=24




                     amount1=test_loan
                     amount2=test_loan*(loan_period/12)*.2
                     total_amount1=amount1+amount2
                     tax=.05*amount1
                     insu=.01*amount1
                     payable_amount=total_amount1+tax+insu
                     lnTM=Label(f1,font=('arial',10),text="LOAN aplicable",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=5,column=4)
                     
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=loan_period,bd=5,justify='right')
                     textloan.grid(row=7,column=5)
                     lnTM=Label(f1,font=('arial',10),text="REPAYMENT PERIOD",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=7,column=4)
                     lnTM=Label(f1,font=('arial',10),text="total amount to be paid",fg="black",bd=15,anchor='w')
                     lnTM.grid(row=8,column=4)
                     textloan=Label(f1,font=('algerian',15,'bold'),bg="blue",text=payable_amount,bd=5,justify='right')
                     textloan.grid(row=8,column=5)



                     
                 

                     reset()
            btsub=Button(f1,padx=8,pady=10,bd=7,fg="black",font=('arial',8,'bold'),width=10,text="LOADATA:",bg="powder blue",command=LOAD_DATA).grid(row=9,column=3)
        else:
            root2.destroy()
            members()
    #++++++++++++++++++++++++++++++++=END OF LOAD_DATA PROFILE
    def LOAD():
        root2.destroy()
        LOAD_DATA_PROFILE()


    #+++++++++++++++++++++++++++

    lnNAME=Label(f1,font=('arial',20),text=" ENTER MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    btcheck=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="load profile:",bg="powder blue",command=LOAD).grid(row=1,column=3)
    #++++++++++++++++++++++++++++++++

    #++++++++++++++++++++++++++++++++++END2
                


    root2.mainloop()




    #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


#creatting module for registering user / members into the system

def members():
    
    ADD2='full2.txt'
    full_members='full_member.txt'
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("REGESTER MEMBERS TO THE SYSTEM")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text=" REGESTER MEMBERS TO THE SYSTEM",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)
    auto='auto_acc.txt'
    with open(auto) as j:
             data1=j.readlines()
             datao=data1[0].rstrip()
             store=int(datao)+1



    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="REGESTER MEMBERS TO THE SYSTEM",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)
    ACC="ACC/"+ datao+"/HSS"

    #CREATE THE  LABLE AND TEXT FILIEDS
    lnNAME=Label(f1,font=('arial',20),text="MEMBER ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)
    lnIDNO=Label(f1,font=('arial',20),text=" SIR NAME ",fg="black",bd=15,anchor='w')
    lnIDNO.grid(row=2,column=0)
    lnmember_ID=Label(f1,font=('arial',20),text="FIRST NAME",fg="black",bd=15,anchor='w')
    lnmember_ID.grid(row=3,column=0)
    lnTM=Label(f1,font=('arial',20),text="LAST NAME",fg="black",bd=15,anchor='w')
    lnTM.grid(row=4,column=0)
    lnacc=Label(f1,font=('arial',20),text="ACCOUNT NO:",fg="black",bd=15,anchor='w')
    lnacc.grid(row=1,column=2)
    lnacc=Label(f1,font=('arial',20),text=ACC,fg="black",bd=15,anchor='w')
    lnacc.grid(row=1,column=3)
    

    member_ID=StringVar()
    sir_name=StringVar()
    first_name=StringVar()
    last_name=StringVar()
    
    MESSAGE=StringVar()

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    textTIT=Entry(f1,font=('arial',15,'bold'),bg="yellow",textvariable=sir_name,insertwidth=7,bd=5,justify='right')
    textTIT.grid(row=2,column=1)
    textAUT=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=first_name,insertwidth=7,bd=5,justify='right')
    textAUT.grid(row=3,column=1)
    textPUB=Entry(f1,font=('arial',15,'bold'),bg="yellow",textvariable=last_name,insertwidth=7,bd=5,justify='right')
    textPUB.grid(row=4,column=1)
    #textACC=label(f1,font=('arial',15,'bold'),bg="blue",text=ACC,bd=5,justify='right')
    #textACC.grid(row=1,column=3)
    textACC=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=MESSAGE,insertwidth=7,bd=5,justify='right')
    textACC.grid(row=3,column=2)



    def reset():
        member_ID.set("")
        sir_name.set("")
        first_name.set("")
        last_name.set("")
        ACC=str("ACC/"+str(store))
        
        lnacc=Label(f1,font=('arial',20),text=ACC,fg="black",bd=15,anchor='w')
        lnacc.grid(row=1,column=3)
        
    
            
        
    

    

    def SUBM():# creating the submit button
         name1=member_ID.get()
         file_name=name1+'.'+'txt'
        
         
         file_name1="MEM_D"+name1+'.'+'txt'
         file_name2="MEM_L"+name1+'.'+'txt'
         file_name3="MEM_S"+name1+'.'+'txt'
        
         ADD=file_name
         ADD1=file_name1
         ADD2=file_name2
         ADD3=file_name3
         if os.path.isfile(ADD):#checking if the existence of a user if yes we login
            MESSAGE.set("USER EXIST")
         else:
             MESSAGE.set("member regestered")
             with open(ADD1,'a+')as k1:#openning the database for appending and adding the book
                k1.write(str(0))
                k1.write("\n")
             with open(ADD2,'a+')as k2:#openning the database for appending and adding the book
                k2.write(str(0))
                k2.write("\n")
             with open(ADD3,'a+')as k3:#openning the database for appending and adding the book
                k3.write(str(0))
                k3.write("\n")
        
             with open(ADD,'a+')as k:#openning the database for appending and adding the book
                k.write(ACC)
                k.write("\n")
                k.write(member_ID.get())
                k.write("\n")
                k.write(sir_name.get())
                k.write("\n")
                k.write(first_name.get())
                k.write("\n")
                k.write(last_name.get())
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")

             with open( full_members,'a+')as H:
                H.write(ACC)
                H.write("\t")
                H.write(member_ID.get())
                H.write("\t")
                H.write(sir_name.get())
                H.write("\t")
                H.write(first_name.get())
                H.write("\t")
                H.write(last_name.get())
                H.write("\t")
                H.write("\n")
             with open( auto,'w')as M:
                 store2=str(store)
                 M.write(store2)
            

             reset()
            
    def BACK():
        
        root2.destroy()
        menu()

    btrest=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="reset:",bg="powder blue",command=reset).grid(row=4,column=2)
    btsub=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="SUBMIT:",bg="powder blue",command=SUBM).grid(row=4,column=3)
    btback=Button(f1,padx=20,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=4,column=4)

    root2.mainloop()

 #creating module to be used for login ie admin  or agents

def AGENT_MEMBER():
    
    ADD2='full2.txt'
    full_members='AGENT_member.txt'
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("REGESTER AGENT TO THE SYSTEM")
    Tops=Frame(root2,width=1200,height=200,bg="pink",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root2,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text=" REGESTER AGENT TO THE SYSTEM",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)
    auto='auto_AGENT.txt'
    with open(auto) as j:
             data1=j.readlines()
             datao=data1[0].rstrip()
             store=int(datao)+1



    def logout():
        root2.destroy()
        login()

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    lntit=Label(f1,font=('arial',20),text="REGESTER AGENT TO THE SYSTEM",fg="black",bd=15,anchor='w')
    lntit.grid(row=0,column=2)
    ACC="AGNT/00/"+ datao

    #CREATE THE  LABLE AND TEXT FILIEDS
    lnNAME=Label(f1,font=('arial',20),text="AGENT ID",fg="black",bd=15,anchor='w')
    lnNAME.grid(row=1,column=0)
    lnIDNO=Label(f1,font=('arial',20),text=" SIR NAME ",fg="black",bd=15,anchor='w')
    lnIDNO.grid(row=2,column=0)
    lnmember_ID=Label(f1,font=('arial',20),text="FIRST NAME",fg="black",bd=15,anchor='w')
    lnmember_ID.grid(row=3,column=0)
    lnTM=Label(f1,font=('arial',20),text="LAST NAME",fg="black",bd=15,anchor='w')
    lnTM.grid(row=4,column=0)
    lnacc=Label(f1,font=('arial',20),text="ACCOUNT NO:",fg="black",bd=15,anchor='w')
    lnacc.grid(row=1,column=2)
    lnacc=Label(f1,font=('arial',20),text=ACC,fg="black",bd=15,anchor='w')
    lnacc.grid(row=1,column=3)
    

    member_ID=StringVar()
    sir_name=StringVar()
    first_name=StringVar()
    last_name=StringVar()
    
    MESSAGE=StringVar()

    textmember_ID=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=member_ID,insertwidth=7,bd=5,justify='right')
    textmember_ID.grid(row=1,column=1)
    textTIT=Entry(f1,font=('arial',15,'bold'),bg="yellow",textvariable=sir_name,insertwidth=7,bd=5,justify='right')
    textTIT.grid(row=2,column=1)
    textAUT=Entry(f1,font=('arial',15,'bold'),bg="blue",textvariable=first_name,insertwidth=7,bd=5,justify='right')
    textAUT.grid(row=3,column=1)
    textPUB=Entry(f1,font=('arial',15,'bold'),bg="yellow",textvariable=last_name,insertwidth=7,bd=5,justify='right')
    textPUB.grid(row=4,column=1)
    #textACC=label(f1,font=('arial',15,'bold'),bg="blue",text=ACC,bd=5,justify='right')
    #textACC.grid(row=1,column=3)
    textACC=Entry(f1,font=('algerian',15,'bold'),bg="blue",textvariable=MESSAGE,insertwidth=7,bd=5,justify='right')
    textACC.grid(row=3,column=2)



    def reset():
        member_ID.set("")
        sir_name.set("")
        first_name.set("")
        last_name.set("")
        ACC=str("AGNT/OO/"+str(store))
        
        lnacc=Label(f1,font=('arial',20),text=ACC,fg="black",bd=15,anchor='w')
        lnacc.grid(row=1,column=3)
        
    
            
        
    

    

    def SUBM():# creating the submit button
         name1=member_ID.get()
         file_name="AGNT"+name1+'.'+'txt'
         file_name1="AGNT_D"+name1+'.'+'txt'
         file_name2="AGNT_L"+name1+'.'+'txt'
         file_name3="AGNT_S"+name1+'.'+'txt'
        
         ADD=file_name
         ADD1=file_name1
         ADD2=file_name2
         ADD3=file_name3
         if os.path.isfile(ADD):#checking if the existence of a user if yes we login
            MESSAGE.set("USER EXIST")
         else:
             MESSAGE.set("AGENT regestered")
             with open(ADD1,'a+')as k:#openning the database for appending and adding the book
                k.write(str(0))
                k.write("\n")
             with open(ADD2,'a+')as k:#openning the database for appending and adding the book
                k.write(str(0))
                k.write("\n")
             with open(ADD3,'a+')as k:#openning the database for appending and adding the book
                k.write(str(0))
                k.write("\n")
        

             with open(ADD,'a+')as k:#openning the database for appending and adding the book
                k.write(ACC)
                k.write("\n") 
                k.write(member_ID.get())
                k.write("\n")
                k.write(sir_name.get())
                k.write("\n")
                k.write(first_name.get())
                k.write("\n")
                k.write(last_name.get())
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")
                k.write("0")
                k.write("\n")

             with open( full_members,'a+')as H:
                H.write(ACC)
                H.write("\t")
                H.write(member_ID.get())
                H.write("\t")
                H.write(sir_name.get())
                H.write("\t")
                H.write(first_name.get())
                H.write("\t")
                H.write(last_name.get())
                H.write("\t")
                H.write("\n")
             with open( auto,'a+')as M:
                 store2=str(store)
                 M.write(store2)
            

             reset()
            
    def BACK():
        
        root2.destroy()
        menu()

    btrest=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="reset:",bg="powder blue",command=reset).grid(row=4,column=2)
    btsub=Button(f1,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="SUBMIT:",bg="powder blue",command=SUBM).grid(row=4,column=3)
    btback=Button(f1,padx=20,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="back to menu",bg="powder blue",command=BACK).grid(row=4,column=4)

    root2.mainloop()
#==============================================================

def login():#creating the login process
    root=Tk()
    root.geometry("1350x700+0+0")
    root.title("HOME SAVE  SACCO")
    Tops=Frame(root,width=1200,height=50,bg="yellow",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root,width=1200,height=800,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('TIMES ROMAN',20),text="HOME SAVE  SACCO",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)
    #LET GET THE LABLE AND TEXT FIELD
    #DEFINE THE GLOBAL VARIABLE FUNCTION


    def LOGIN():
        over=StringVar()
        
        with open(data) as j:
             data1=j.readlines()
             uname=data1[0].rstrip()
             upass=data1[1].rstrip()

        
        if USER.get()==uname and PASS.get()==upass:

            over=Label(f1,font=('algerian',10,'bold'),text="wellcome admin",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)
            f1.forget()
            root.destroy()

            
            menu()

        if USER.get()!=uname and PASS.get()==upass:
            
            over=Label(f1,font=('algerian',10,'bold'),text="wrong username",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)
            

        if USER.get()==uname and PASS.get()!=upass:
            over=Label(f1,font=('algerian',10,'bold'),text="wrong password",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)
            

        if USER.get()!=uname and PASS.get()!=upass:
            over=Label(f1,font=('algerian',10,'bold'),text="wrong username & password",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)
           
        

    def EXIT():
        root.destroy()

    def RESET():
        USER.set("")
        PASS.set("")
        over.set("")

    #DEFINE VALIABLES
    USER=StringVar()
    PASS=StringVar()
    over=StringVar()
    prediction=StringVar()

    lbusername=Label(f1,font=('algerian',20,'bold'),text='login to the system',bd=10,anchor='w')
    lbusername.grid(row=1,column=1)

    lbusername=Label(f1,font=('arial',20,'bold'),text='USERNAME',bd=10,anchor='w')
    lbusername.grid(row=2,column=0)
    textUSER=Entry(f1,font=('arial',15,'bold'),textvariable=USER,insertwidth=10,bd=10,justify='right')
    textUSER.grid(row=2,column=1)

    lbpass=Label(f1,font=('arial',20,'bold'),text="PASSWORD ",bd=10,anchor='w')
    lbpass.grid(row=3,column=0)
    textPASS=Entry(f1,font=('arial',15,'bold'),textvariable=PASS,show="*",insertwidth=16,bd=10,justify='right')
    textPASS.grid(row=3,column=1)

    #CREATE BUTTON FOR LOGIN RESET AND EXIT AND THEIR FUNCTION
    btLOG=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="LOGIN:",bg="powder blue",command=LOGIN).grid(row=4,column=0)

    btRESET=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="RESET",bg="powder blue",command=RESET).grid(row=4,column=1)
    btEXIT=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="EXIT",bg="powder blue",command=EXIT).grid(row=4,column=3)


    root.mainloop()

    #the begining of creating onwnership of the system
def signup():#creating the signup process

    data3="login.txt"
    root=Tk()
    root.geometry("1350x700+0+0")
    root.title("HOME SAVE  SACCO")
    Tops=Frame(root,width=1200,height=200,bg="green",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root,width=1200,height=1000,relief=RAISED)
    f1.pack()
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('TIMES ROMAN',20),text="HOME SAVE  SACCO",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)
    #LET GET THE LABLE AND TEXT FIELD
    #DEFINE THE GLOBAL VARIABLE FUNCTION


    def LOGIN():
        over=StringVar()

                
        if PASS2.get()==PASS.get():
            over=Label(f1,font=('algerian',10,'bold'),text="wellcome admin",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)
            root.destroy()
            with open(data3,'a+') as k:
                k.write(USER.get())
                k.write("\n")
                k.write(PASS.get())
                k.write("\n")
            k.close()
            login()

        else:
            over=Label(f1,font=('algerian',10,'bold'),text="password dont match",fg="red",bd=10,anchor='w')
            over.grid(row=2,column=3,columnspan=2)

        
                

    def EXIT():
        root.destroy()

    def RESET():
        USER.set("")
        PASS.set("")
        over.set("")
        PASS2.set("")

    #DEFINE VALIABLES
    USER=StringVar()
    PASS=StringVar()
    PASS2=StringVar()

    over=StringVar()
    prediction=StringVar()

    lbusername=Label(f1,font=('algerian',20,'bold'),text='signup to the system',bd=10,anchor='w')
    lbusername.grid(row=0,column=1)

    lbusername=Label(f1,font=('arial',20,'bold'),text='USERNAME',bd=10,anchor='w')
    lbusername.grid(row=1,column=0)
    textUSER=Entry(f1,font=('arial',15,'bold'),textvariable=USER,insertwidth=10,bd=10,justify='right')
    textUSER.grid(row=1,column=1)

    lbpass=Label(f1,font=('arial',20,'bold'),text="PASSWORD ",bd=10,anchor='w')
    lbpass.grid(row=2,column=0)
    textPASS=Entry(f1,font=('arial',15,'bold'),textvariable=PASS,show="*",insertwidth=16,bd=10,justify='right')
    textPASS.grid(row=2,column=1)
    lbpass=Label(f1,font=('arial',20,'bold'),text="CONFIRM PASSWORD ",bd=10,anchor='w')
    lbpass.grid(row=3,column=0)
    textPASS1=Entry(f1,font=('arial',15,'bold'),textvariable=PASS2,show="*",insertwidth=16,bd=10,justify='right')
    textPASS1.grid(row=3,column=1)

    #CREATE BUTTON FOR LOGIN RESET AND EXIT AND THEIR FUNCTION
    btLOG=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="SIGNUP:",bg="powder blue",command=LOGIN).grid(row=4,column=0)

    btRESET=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="RESET",bg="powder blue",command=RESET).grid(row=4,column=1)
    btEXIT=Button(f1,padx=10,pady=10,bd=10,fg="black",font=('arial',15,'bold'),width=10,text="EXIT",bg="powder blue",command=EXIT).grid(row=4,column=3)


    root.mainloop()

#creatting the menu window for the user.
def menu():#creating the menu process
    root1=Tk()
    root1.geometry("1350x700+0+0")
    root1.title("HOME SAVE  SACCO")
    Tops=Frame(root1,width=1200,height=200, bg="white",relief=RAISED)
    Tops.pack(side=TOP)
    f1=Frame(root1,width=500,height=1000,bg="blue",relief=RAISED)
    f1.pack(side=LEFT)
    f2=Frame(root1,width=500,height=1000,relief=RAISED)
    f2.pack(side=RIGHT)
    localtime=time.asctime(time.localtime(time.time()))
    lninfo=Label(Tops,font=('arial',20),text="HOME SAVE  SACCO",fg="black",bd=5,anchor='w')
    lninfo.grid(row=0,column=0)
    lnbinf=Label(Tops,font=('arial',20),text=localtime,fg="blue",bd=5,anchor='w')
    lnbinf.grid(row=1,column=0)
    #CREATE MAIN MENU WITH RESPONSIVE LINKS
    #define the functions

    
                        

    
    def DEPOSIT():
        
        root1.destroy()
        depo()
        

    def WITHDRAW():
        root1.destroy()
        withd()
        

    def SAVING():
        root1.destroy()
        sav()
        

    def LOAN():
        root1.destroy()
        lon1()
        

    def listdf():
        root1.destroy()
        stock()
        

    def MEMBERS():
        
        root1.destroy()
        members()
    
        
        

    def AGENT():
        root1.destroy()
        AGENT_MEMBER()

    def REPAY():
        root1.destroy()
        repay()

    def logout():
        
        root1.destroy()
        login()
        

    #create the actual button
    btLOGOUT=Button(Tops,padx=10,pady=10,bd=7,fg="black",font=('arial',15,'bold'),width=10,text="LOGOUT:",bg="powder blue",command=logout).grid(row=2,column=3)

    btREPAY=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="REPAY CASH",bg="yellow",command=REPAY).grid(row=8,column=1)

    btDEPOSIT=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="DEPOSIT CASH",bg="pink",command=DEPOSIT).grid(row=7,column=1)
    btWITHDRAW=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="WITHDRAW CASH",bg="powder blue",command=WITHDRAW).grid(row=6,column=1)
    btLOAN=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="SAVINGS",bg="blue",command=SAVING).grid(row=3,column=1)
    btWITHDRAW=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="LOAN CASH",bg="yellow",command=LOAN).grid(row=4,column=1)
    btWITHDRAW=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="REGESTER CUSTOMER",bg="powder blue",command=MEMBERS).grid(row=2,column=1)
    btDEPOSIT=Button(f1,padx=70,pady=10,bd=5,fg="black",font=('arial',15,'bold'),width=10,text="REGESTER AGENTS",bg="blue",command=AGENT).grid(row=1,column=1)

    #system information in frame 2
    a1=" HOME SAVE  SACCO \n"
    a2="This system will be used to :"
    a3="\n Deposit"
    a4="\n Withdraw"
    a5="\n save"
    a6="\n REGESTER CUSTOMER"
    a7="\n add agents"
    canvas = Canvas(f2, width =500, height=400)
    canvas.pack()
    lnsys=Label(canvas,font=('algerian',20),text=a1,fg="black",bd=5,anchor='e')
    lnsys.grid(row=0,column=0)
    lnsys=Label(canvas,font=('verdana',20),text=a2,fg="black",bd=5,anchor='w')
    lnsys.grid(row=1,column=0)
    lnsys=Label(canvas,font=('arial',20),text=a3,fg="black",bd=5,anchor='w')
    lnsys.grid(row=2,column=0)
    lnsys=Label(canvas,font=('arial',20),text=a4,fg="black",bd=5,anchor='w')
    lnsys.grid(row=3,column=0)
    lnsys=Label(canvas,font=('arial',20),text=a5,fg="black",bd=5,anchor='w')
    lnsys.grid(row=4,column=0)
    lnsys=Label(canvas,font=('',20),text=a6,fg="black",bd=5,anchor='w')
    lnsys.grid(row=5,column=0)
    



    root1.mainloop()





#============================================================================================================
#check for the user login in the database module.
if os.path.isfile(data):#checking if the existence of a user if yes we login
    login()
else:
    signup()#else we create one through signup process
