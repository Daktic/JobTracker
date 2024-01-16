import json
import tkinter as tk

def get_config():
    with open("config.json", "r") as f:
        return json.load(f)


def app():
    config = get_config()

    root = tk.Tk()
    root.title("Google Sheet Manager")


    root.geometry("500x500")
    # Set background color to white
    root.configure(bg="white")


    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()  # Use pack() to add it to the window
    root.mainloop()

if __name__ == "__main__":
    app()