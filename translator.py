import tkinter as tk
import pyperclip
import googletrans as googletranslator
from threading import Thread, Event

class Th(Thread):
    def __init__ (self, event):
        Thread.__init__(self)
        self.stopped = event
        self.old_text = ''
        self.text = pyperclip.paste()

    def run(self):
        while not self.stopped.wait(0.5):
            self.text = pyperclip.paste()
            if self.old_text != self.text and self.text.strip() != '':
                self.translate()
            self.old_text = self.text

    def translate(self):
        lang = translator.detect(self.text).lang
        dest = 'en' if lang == 'pt' else 'pt'
        try:
            traducao = translator.translate(self.text, dest=dest)
            traducao = traducao.text
            traducao = traducao.replace('\n', '').replace('\r', ' ')
        except:
            traducao = self.text
        finally:
            root_text.delete('1.0', tk.END)
            root_text.insert(tk.INSERT, traducao)

translator = googletranslator.Translator()

root = tk.Tk()
root.title('Tradutor')
root.wm_attributes('-topmost', 1)

root_text = tk.Text(master=root, height=3, width=75)
root_text.pack(side='top', expand=True, fill='both')

stopFlag = Event()
watcher = Th(stopFlag)
watcher.start()
root.mainloop()
