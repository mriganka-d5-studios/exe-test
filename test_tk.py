import sys
import platform
import tkinter as tk
from tkinter import messagebox


def main():
    root = tk.Tk()
    root.title("Tkinter Test")
    root.geometry("360x200")

    info = f"Python {platform.python_version()} | Tk {tk.TkVersion}"
    tk.Label(root, text="Tkinter is working!", font=("Segoe UI", 14, "bold")).pack(pady=(20, 5))
    tk.Label(root, text=info).pack()

    status = tk.StringVar(value="Click the button to test.")
    tk.Label(root, textvariable=status, fg="green").pack(pady=10)

    def on_click():
        status.set("Button works!")
        messagebox.showinfo("Test", "Popup works too.")

    tk.Button(root, text="Test", command=on_click, width=12).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
