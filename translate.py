import tkinter as tk
import pyperclip
import googletrans as gt
from threading import Thread, Event

class Th(Thread):
    def __init__ (self, event):
        Thread.__init__(self)
        self.stopped = event
        self.old_clip = ""
        self.new_clip = pyperclip.paste()

    def run(self):
        while not self.stopped.wait(0.5):
            self.new_clip = pyperclip.paste()
            if self.old_clip != self.new_clip and self.new_clip.strip() != '':
                self.translate()
            self.old_clip = self.new_clip

    def translate(self):
        traducao = tradutor.translate(self.new_clip, src='pt', dest='en')
        traducao = traducao.text
        traducao = traducao.replace('\n', '').replace('\r', ' ')
        root_text.delete('1.0', tk.END)
        root_text.insert(tk.INSERT, traducao)

tradutor = gt.Translator()

root = tk.Tk()
root.title('Tradutor')
root.wm_attributes("-topmost", 1)

root_text = tk.Text(master=root, height=3, width=75)
root_text.pack(side='top', expand=True, fill='both')

stopFlag = Event()
watcher = Th(stopFlag)
watcher.start()
root.mainloop()
