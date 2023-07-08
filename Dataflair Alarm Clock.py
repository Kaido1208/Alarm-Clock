from tkinter import *
import datetime
import time
import winsound

def alarm(set_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is:", date)
        print(now)
        if now == set_timer:
            print("It's time to wake up")
        winsound.Playsound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_timer = f"{hour.get() } : {min.get() } : {sec.get() }"
    alarm(set_timer)

clock = Tk()

clock.title("DAtaFlair Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock,text="Enter time in 24 hour format!")
addTime = Label(clock,text="Hour Min Sec")
setYourAlarm = Label(clock,text ="Please add a time to wake you up")

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock,textvariable= hour)
minTime = Entry(clock,textvariable= min)
secTime = Entry(clock, textvariable= sec)

submit = Button(clock, text="Set Alarm")

clock.mainloop()