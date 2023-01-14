from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

root = Tk()
root.title("KrestikiNoliki")
root.geometry('%dx%d+%d+%d' % (800, 800, 560, 140))
root.resizable(False, False)
canvas = Canvas(root, bg='white', height=800, width=800)


def fieldDef():
    global field
    field = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
    canvas.delete("all")
    canvas.create_line(350, 250, 350, 550, width=3)
    canvas.create_line(450, 250, 450, 550, width=3)
    canvas.create_line(250, 350, 550, 350, width=3)
    canvas.create_line(250, 450, 550, 450, width=3)
    canvas.pack()


def check(field):
    if (field[0] and field[1] and field[2] == 'x') or (field[3] and field[4] and field[5] == 'x') or (
            field[6] and field[7] and field[8] == 'x') or (field[0] and field[3] and field[6] == 'x') or (
            field[1] and field[4] and field[7] == 'x') or (field[2] and field[5] and field[8] == 'x') or (
            field[0] and field[4] and field[8] == 'x') or (field[2] and field[4] and field[6] == 'x'):
        fieldDef()
        mb.showinfo("x win", "x win this game")
    elif (field[0] and field[1] and field[2] == 'o') or (field[3] and field[4] and field[5] == 'o') or (
            field[6] and field[7] and field[8] == 'o') or (field[0] and field[3] and field[6] == 'o') or (
            field[1] and field[4] and field[7] == 'o') or (field[2] and field[5] and field[8] == 'o') or (
            field[0] and field[4] and field[8] == 'o') or (field[2] and field[4] and field[6] == 'o'):
        fieldDef()
        mb.showinfo("o win", "o win this game")
    elif field[0] and field[1] and field[2] and field[3] and field[4] and field[5] and field[6] and field[7] and field[8] != '0':
        fieldDef()
        mb.showinfo("Draw", "Draw")


def xtie(event):
    if event.x > 250 and event.x < 350 and event.y > 250 and event.y < 350:
        if field[0] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(250, 350, 350, 250, width=3)
            canvas.create_line(250, 250, 350, 350, width=3)
            field[0] = 'x'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 250 and event.y < 350:
        if field[1] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(350, 350, 450, 250, width=3)
            canvas.create_line(350, 250, 450, 350, width=3)
            field[1] = 'x'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 250 and event.y < 350:
        if field[2] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(450, 350, 550, 250, width=3)
            canvas.create_line(450, 250, 550, 350, width=3)
            field[2] = 'x'
            check(field)
    if event.x > 250 and event.x < 350 and event.y > 350 and event.y < 450:
        if field[3] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(250, 450, 350, 350, width=3)
            canvas.create_line(250, 350, 350, 450, width=3)
            field[3] = 'x'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 350 and event.y < 450:
        if field[4] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(350, 350, 450, 450, width=3)
            canvas.create_line(350, 450, 450, 350, width=3)
            field[4] = 'x'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 350 and event.y < 450:
        if field[5] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(450, 450, 550, 350, width=3)
            canvas.create_line(450, 350, 550, 450, width=3)
            field[5] = 'x'
            check(field)
    if event.x > 250 and event.x < 350 and event.y > 450 and event.y < 550:
        if field[6] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(250, 550, 350, 450, width=3)
            canvas.create_line(250, 450, 350, 550, width=3)
            field[6] = 'x'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 450 and event.y < 550:
        if field[7] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(350, 450, 450, 550, width=3)
            canvas.create_line(350, 550, 450, 450, width=3)
            field[7] = 'x'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 450 and event.y < 550:
        if field[8] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', otie)
            root.bind('<Button-3>', otie)
            canvas.create_line(450, 550, 550, 450, width=3)
            canvas.create_line(450, 450, 550, 550, width=3)
            field[8] = 'x'
            check(field)


def otie(event):
    if event.x > 250 and event.x < 350 and event.y > 250 and event.y < 350:
        if field[0] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(250, 250, 350, 350, width=3)
            field[0] = 'o'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 250 and event.y < 350:
        if field[1] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(350, 250, 450, 350, width=3)
            field[1] = 'o'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 250 and event.y < 350:
        if field[2] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(450, 250, 550, 350, width=3)
            field[2] = 'o'
            check(field)
    if event.x > 250 and event.x < 350 and event.y > 350 and event.y < 450:
        if field[3] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(250, 350, 350, 450, width=3)
            field[3] = 'o'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 350 and event.y < 450:
        if field[4] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(350, 350, 450, 450, width=3)
            field[4] = 'o'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 350 and event.y < 450:
        if field[5] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(450, 350, 550, 450, width=3)
            field[5] = 'o'
            check(field)
    if event.x > 250 and event.x < 350 and event.y > 450 and event.y < 550:
        if field[6] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(250, 450, 350, 550, width=3)
            field[6] = 'o'
            check(field)
    if event.x > 350 and event.x < 450 and event.y > 450 and event.y < 550:
        if field[7] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(350, 450, 450, 550, width=3)
            field[7] = 'o'
            check(field)
    if event.x > 450 and event.x < 550 and event.y > 450 and event.y < 550:
        if field[8] == '0':
            root.unbind('<Button-1>')
            root.unbind('<Button-3>')
            root.bind('<Button-1>', xtie)
            root.bind('<Button-3>', xtie)
            canvas.create_oval(450, 450, 550, 550, width=3)
            field[8] = 'o'
            check(field)


fieldDef()
root.bind('<Button-1>', xtie)
root.bind('<Button-3>', xtie)
root.mainloop()
