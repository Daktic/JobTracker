import json
import tkinter as tk

def get_config():
    with open("config.json", "r") as f:
        return json.load(f)


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.master.geometry("500x500")



    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()



if __name__ == "__main__":
    app = Application()
    app.master.title('Job Tracker')
    app.mainloop()