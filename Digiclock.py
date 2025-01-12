from tkinter import *
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_yr.config(text=year)
    lab_dy.config(text=day)

    lab_hr.after(200,date_time)
    
clock = Tk()

clock.title('--------   Digital Clock   --------')
clock.geometry('1000x500')
clock.config(bg ='black')

#####################################   For hours  #############################
lab_hr = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_txt= Label(clock,text="Hour",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

# #################################  For Minutes #############################
lab_min = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_txt= Label(clock,text="Min",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_min_txt.place(x=340,y=190,height=40,width=100)

##############################  For Second  ##############################################

lab_sec = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt= Label(clock,text="Sec",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)


############################ For AM / PM  ######################################################
lab_am = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_am.place(x=780,y=50,height=110,width=100)


lab_am_txt= Label(clock,text="AM/PM",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_am_txt.place(x=780,y=190,height=40,width=100)


###########################     For Date    #############################################

lab_date = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_txt= Label(clock,text="Date",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_date_txt.place(x=120,y=410,height=40,width=100)


# #################################  For Month #############################
lab_mo = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_mo.place(x=340,y=270,height=110,width=100)

lab_mo_txt= Label(clock,text="Month",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_mo_txt.place(x=340,y=410,height=40,width=100)


##############################  For Year  ##############################################

lab_yr = Label(clock,text="00",font=('Time New Roman',50,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_yr.place(x=560,y=270,height=110,width=100)

lab_yr_txt= Label(clock,text="Year",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_yr_txt.place(x=560,y=410,height=40,width=100)


############################ For Day  ######################################################
lab_dy = Label(clock,text="00",font=('Time New Roman',30,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_dy.place(x=780,y=270,height=110,width=100)


lab_dy_txt= Label(clock,text="Day",font=('Time New Roman',20,"bold"),
                  bg = '#A52A2A',fg = "white")
lab_dy_txt.place(x=780,y=410,height=40,width=100)
######################      Funcation Call   ######################################

date_time()
clock.mainloop()