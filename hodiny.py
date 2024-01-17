import tkinter as tk
from datetime import datetime

class tvar:
    def __init__(self, point: tuple, color: str, canvas):
        self.canvas = canvas
        self.color = color
        self.coords = point

    def on(self):
        self.canvas.itemconfig(self.id, fill=self.color)

    def off(self):
        self.canvas.itemconfig(self.id, fill="yellow")

class kruhovy(tvar):
    def __init__(self, point: tuple, v, color: str, canvas):
        super().__init__(point, color, canvas)
        self.v = v
        self.id = canvas.create_oval(point[0], point[1], point[0] + v, point[1] + v, fill=color, outline='')

class rovny(tvar):
    def __init__(self, point: tuple, vx: int, vy: int, color: str, canvas):
        super().__init__(point, color, canvas)
        self.vy = vy
        self.vx = vx
        self.id = canvas.create_rectangle(point[0], point[1], point[0] + vx, point[1] + vy, fill=color, outline="")

class cast:
    def __init__(self, point: tuple, mini: int, mega: int, color: str, canvas):
        self.coords = point
        self.časti = []
        sy = point[1]
        sx = point[0]
        self.časti.append(rovny((sx + mini, sy), mega, mini, color, canvas))
        self.časti.append(rovny((sx + mini + mega, sy + mini), mini, mega, color, canvas))
        self.časti.append(rovny((sx + mini, sy + mega + mini), mega, mini, color, canvas))
        self.časti.append(rovny((sx, sy + mini), mini, mega, color, canvas))
        self.časti.append(rovny((sx + mini + mega, sy + 2 * mini + mega), mini, mega, color, canvas))
        self.časti.append(rovny((sx + mini, sy + 2 * mega + 2 * mini), mega, mini, color, canvas))
        self.časti.append(rovny((sx, sy + 2 * mini + mega), mini, mega, color, canvas))

    def znova(self):
        for i in self.časti:
            i.off()

    def chyba(self):
        for i in self.časti:
            i.on()

    def zobrazenie(self, number: int):
        match int(number):
            case 9:
                self.chyba()
                self.časti[6].off()
            case 8:
                self.chyba()
            case 7:
                self.chyba()
                self.časti[0].on()
                self.časti[1].on()
                self.časti[4].on()
            case 6:
                self.chyba()
                self.časti[1].off()
            case 5:
                self.chyba()
                self.časti[1].off()
                self.časti[6].off()
            case 4:
                self.chyba()
                self.časti[0].off()
                self.časti[6].off()
                self.časti[5].off()
            case 3:
                self.chyba()
                self.časti[3].off()
                self.časti[6].off()
            case 2:
                self.znova()
                self.časti[0].on()
                self.časti[1].on()
                self.časti[2].on()
                self.časti[6].on()
                self.časti[5].on()
            case 1:
                self.znova()
                self.časti[1].on()
                self.časti[4].on()
            case 0:
                self.chyba()
                self.časti[2].off()


class hodiny:
    def __init__(self, color: str, canvas, mini: int, mega: int, point: tuple):
        self.kruhy = []
        self.puzzle = []
        self.point = point
        self.mega = mega
        self.mini = mini
        self.canvas = canvas
        for i in range(6):
            if i % 2 == 0 or i == 5:
                self.puzzle.append(
                    cast((point[0] + i * (2 * mini + mega + 20), point[1]), mini, mega, color, canvas))
            else:
                self.puzzle.append(
                    cast((point[0] + i * (2 * mini + mega + 20), point[1]), mini, mega, color, canvas))
                self.kruhy.append(kruhovy(
                    (point[0] + (i + 1) * (2 * mini + mega + 20) - (20 + 8) / 2, point[1] + (3 * mini + 2 * mega) / 4),
                    8, color, canvas))
                self.kruhy.append(kruhovy((point[0] + (i + 1) * (2 * mini + mega + 20) - (20 + 8) / 2,
                                        point[1] + (3 * mini + 2 * mega) * 3 / 4), 8, color, canvas))
        self.zmena()

    def zmena(self):
        čas = datetime.now().strftime("%H:%M:%S")
        čas = čas.split(':')
        čas = [letter for word in čas for letter in word]
        for i in range(len(čas)):
            self.puzzle[i].zobrazenie(čas[i])
        self.canvas.after(1000, self.zmena)

root = tk.Tk()
canvas = tk.Canvas(root, height=900, width=1200, bg="yellow")
canvas.pack()
skuska = hodiny('purple', canvas, 10, 50, (350, 350))
root.mainloop()