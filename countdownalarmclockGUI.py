import tkinter
import datetime
import time
import winsound

window = tkinter.Tk()
window.title("Alarm Clock by WindJammer")

datetime_object = time.localtime()
local_time = time.strftime("%H:%M:%S", datetime_object)


#Functions for the buttons
def time_now():
    while True:
        datetime_today = datetime.datetime.today().replace(microsecond=0)
        clock_button.configure(text=datetime_today)
        break

def set_alarm_command():
    bt.configure(text="Alarm is running... ")
    total_seconds_countdown = (default_input_hour_bt.get() * 60) + (default_input_min_bt.get() * 60) + default_input_sec_bt.get()
    
    while total_seconds_countdown > 0:
        print(total_seconds_countdown)
        total_seconds_countdown -= 1
        time.sleep(1)

        if total_seconds_countdown == 0:
            bt.configure(text="Alarm ringing!!", fg="red")
            winsound.PlaySound("defaultsound", winsound.SND_ASYNC + winsound.SND_LOOP)
            break

def stop_alarm_sound():
    winsound.PlaySound(None, 0)

def display_selected(choice):
    choice = default_input_hour_bt.get()
    print(choice)

def show_hr(*args):
    str_out_hr.set(default_input_hour_bt.get())

def show_min(*args):
    str_out_min.set(default_input_min_bt.get())

def show_sec(*args):
    str_out_sec.set(default_input_sec_bt.get())
    

#Other labels in the websites
tkinter.Label(window, text = "Alarm Clock", font=("Arial Bold", 50), fg = "white", bg = "black").grid(row=0, column=0)

tkinter.Label(window, text = "(up to 24 hours)", font=("Arial Bold", 20), fg = "white", bg = "black").grid(row=1, column=0)

clock_button = tkinter.Button(window, text = "Click me for time now!", command = time_now)
clock_button.grid(row=2, column=0)

tkinter.Label(window, text = "Click on the button above to refresh current time.\n (Roughly-made clock for your reference)", fg = "blue").grid(row=3, column=0)

#H, M, S Labels
hours_label = tkinter.Label(window, text = "Hours")
hours_label.grid(row=1, column=1)
mins_label = tkinter.Label(window, text = "Mins")
mins_label.grid(row=1, column=2)
secs_label = tkinter.Label(window, text = "Seconds")
secs_label.grid(row=1, column=3)


#H, M, S Entries
#Hours OptionMenu
default_input_hour_bt = tkinter.IntVar(window)
options_hour_bt = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23']
default_input_hour_bt.set(options_hour_bt[0])
hour_bt = tkinter.OptionMenu(window, default_input_hour_bt, *options_hour_bt)
hour_bt.grid(row=2, column=1)

#Labelling option selected/output for hours
str_out_hr = tkinter.IntVar(window)

#hr_bt = tkinter.Button(window, text="Update", command=lambda: show_hr())
#hr_bt.grid(row=3, column=1)
output_hr = tkinter.Label(window, textvariable = str_out_hr)
output_hr.grid(row=3, column=1)
default_input_hour_bt.trace('w', show_hr)


#Minutes OptionMenu
default_input_min_bt = tkinter.IntVar(window)
options_min_bt = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']
default_input_min_bt.set(options_min_bt[0])
min_bt = tkinter.OptionMenu(window, default_input_min_bt, *options_min_bt)
min_bt.grid(row=2, column=2)

#Labelling option selected/output for mins
str_out_min = tkinter.IntVar(window)

#min_bt = tkinter.Button(window, text="Update", command=lambda: show_min())
#min_bt.grid(row=3, column=2)
output_min = tkinter.Label(window, textvariable = str_out_min)
output_min.grid(row=3, column=2)
default_input_min_bt.trace('w', show_min)


#Seconds OptionMenu
default_input_sec_bt = tkinter.IntVar(window)
options_sec_bt = ['00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59']
default_input_sec_bt.set(options_sec_bt[0])
sec_bt = tkinter.OptionMenu(window, default_input_sec_bt, *options_sec_bt)
sec_bt.grid(row=2, column=3)

#Labelling option selected/output for secs
str_out_sec = tkinter.IntVar(window)

#sec_bt = tkinter.Button(window, text="Update", command=lambda: show_sec())
#sec_bt.grid(row=3, column=3)
output_sec = tkinter.Label(window, textvariable = str_out_sec)
output_sec.grid(row=3, column=3)
default_input_sec_bt.trace('w', show_sec)


#Set Alarm button
bt = tkinter.Button(window, text="Set Alarm", command = set_alarm_command)
bt.grid(row=4, column=2)

#Stop Alarm button
bt_stop = tkinter.Button(window, text="Stop Alarm sound", fg = "red", command = stop_alarm_sound)
bt_stop.grid(row=5, column=2)


window.mainloop()























