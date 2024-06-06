from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Calculadora')
window.geometry("235x310")

blackColor = '#1e1f1e' 
whiteColor = '#feffff'
blueColor = '#38576b'
greyColor = '#ECEFF1'
orangeColor = '#FFAB40'
text = ''

window.config(bg = blackColor)

screenFrame = Frame(window, width = 235, height = 50, bg = blueColor)
screenFrame.grid(row = 0, column = 0)

bodyFrame = Frame(window, width = 235, height = 268)
bodyFrame.grid(row = 1, column = 0)

def setValue(event):
    global text
    text = text + str(event)
    textValue.set(text)

def calculate():
    global text
    result = eval(text)
    textValue.set(result)

def clear():
    global text
    text = ''
    textValue.set(text)

textValue = StringVar()
label = Label(screenFrame, textvariable = textValue, width = 16, height = 2, padx = 7, relief = FLAT, anchor = 'e', justify = RIGHT, font = ('Ivy 18'), bg = blueColor, fg = whiteColor)
label.place(x = 0, y = 0)

clearButton = Button(bodyFrame, command = clear, text = 'C', width = 11, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
clearButton.place(x = 0, y = 0)
percentageButton = Button(bodyFrame, command = lambda: setValue('%'), text = '%', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
percentageButton.place(x = 118, y = 0)
divisionButton = Button(bodyFrame, command = lambda: setValue('/'), text = '/', width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
divisionButton.place(x = 177, y = 0)

sevenButton = Button(bodyFrame, command = lambda: setValue('7'), text = '7', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
sevenButton.place(x = 0, y = 52)
eightButton = Button(bodyFrame, command = lambda: setValue('8'), text = '8', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
eightButton.place(x = 59, y = 52)
nineButton = Button(bodyFrame, command = lambda: setValue('9'), text = '9', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
nineButton.place(x = 118, y = 52)
multiplierButton = Button(bodyFrame, command = lambda: setValue('*'), text = '*', width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
multiplierButton.place(x = 177, y = 52)

sevenButton = Button(bodyFrame, command = lambda: setValue('4'), text = '4', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
sevenButton.place(x = 0, y = 104)
eightButton = Button(bodyFrame, command = lambda: setValue('5'), text = '5', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
eightButton.place(x = 59, y = 104)
nineButton = Button(bodyFrame, command = lambda: setValue('6'), text = '6', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
nineButton.place(x = 118, y = 104)
multiplierButton = Button(bodyFrame, command = lambda: setValue('-'), text = '-', width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
multiplierButton.place(x = 177, y = 104)

sevenButton = Button(bodyFrame, command = lambda: setValue('1'), text = '1', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
sevenButton.place(x = 0, y = 156)
eightButton = Button(bodyFrame, command = lambda: setValue('2'), text = '2', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
eightButton.place(x = 59, y = 156)
nineButton = Button(bodyFrame, command = lambda: setValue('3'), text = '3', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
nineButton.place(x = 118, y = 156)
multiplierButton = Button(bodyFrame, command = lambda: setValue('+'), text = '+', width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
multiplierButton.place(x = 177, y = 156)

clearButton = Button(bodyFrame, command = lambda: setValue('0'), text = '0', width = 11, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
clearButton.place(x = 0, y = 208)
percentageButton = Button(bodyFrame, command = lambda: setValue('.'), text = '.', width = 5, height = 2, bg = greyColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
percentageButton.place(x = 118, y = 208)
divisionButton = Button(bodyFrame, command = calculate, text = '=', width = 5, height = 2, bg = orangeColor, fg = whiteColor, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
divisionButton.place(x = 177, y = 208)

window.mainloop()