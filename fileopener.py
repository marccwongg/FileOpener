import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title('File Opener')
apps =[]

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps= tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables", "*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="blue", fg="white")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=500, width=400, bg="#263D42")
canvas.pack() #base background of the root

#creating a frame inside of the root
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.7, relx=0.1, rely=0.1)

#Button to open all selected files
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="blue", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="blue", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#run GUI pop up
root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')

