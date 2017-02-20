#!/usr/bin/env python

# importing modules
import time
from Tkinter import *

"""
A python program to display a digital and/or analog clock; work in progress

"""

__author__ = 'Razvan U.'
__Version__ = '0.0.2'


gl_time = ''
root = Tk()
root.configure(background='turquoise')


def clock_function():
    """Main clock function"""
    global gl_time
    time_var1 = time.strftime('%H:%M:%S')
    time_var2_utc = time.strftime('%H:%M:%S', time.gmtime())
    date_iso1 = time.strftime('%Y-%m-%d')
    date_var2 = "%s   DOY: %s  Week: %s" % (time.strftime('%A'), time.strftime('%j'), time.strftime('%W'))

    if time_var1 != gl_time:
        gl_time = time_var1
        clock_vr.config(text=time_var1)
        clock_utc.config(text=time_var2_utc)
        date_etc.config(text=date_iso1)
        date_iso.config(text=date_var2)

    clock_vr.after(200, clock_function)


clock_vr = Label(root, font=('arial', 12, 'bold'), fg='white', bg='purple')
clock_vr.pack()

clock_utc = Label(root, font=('arial', 12, 'bold'), fg='blue', bg='black')
clock_utc.pack()

date_iso = Label(root, font=('arial', 12, 'bold'), fg='grey', bg='black')
date_iso.pack()

date_etc = Label(root, font=('arial', 12, 'bold'), fg='yellow', bg='grey')
date_etc.pack()


def quit_button():
    """ Quit button """
    a = Button(root, text='Quit', bg='turquoise', command=root.quit)
    a.pack(side=LEFT, padx=80, pady=30)


def main():
    """Main function"""
    clock_function()
    quit_button()
    mainloop()


if __name__ == "__main__":
    main()
