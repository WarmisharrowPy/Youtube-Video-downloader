from tkinter.filedialog import*
from tkinter import filedialog
from pytube import YouTube
from tkinter.ttk import *

window = Tk()
window.geometry('500x500+350+100')
window.title('Youtube Downloader')
window.resizable(False, False)
window.config(bg="gray3")

direct = ""
def open_path():
    download_out.config(text = "Just be calm and wait if system show No Responding Durning Downloading",
    font = ("Bahnschrift SemiBold", 10, "bold"))
    download_name.config(text ="")
    download_size.config(text="")
    download_loc.config(text="")
    global  direct
    direct = filedialog.askopenfilename()
    path_holder.config(text = direct)

def Download():
    url = link_ent.get()
    Selected = types.get()
    if len(url)<1:
        link_error.config(text = "Please insert URL")
    if len(direct)<1:
        link_error.config(text = "Please insert path")
    else:
        link_error.config(text = "")
        path_error.config(text = "")
        try:
            Yt = YouTube(url)
            try:
                    if (Selected == options[0]):
                        typ = Yt.streams.get_highest_resolution()
                    elif (Selected == options[1]):
                        typ = Yt.streams.filter(progressive= True, file_extension = "mp4").first()
                    elif (Selected == options[2]):
                        typ = Yt.streams.filter(only_audio=True).first()

                    try:
                        typ.download(direct)
                        link_ent.delete(0, "end")
                        path_holder.config(text = "\t\t\t\t       ")
                        download_out.config(text = "Downloaded", font = (12))
                        name = typ.title
                        size = typ.filesize/1024000
                        size = round(size, 1)
                        download_name.config(text ="Name :" +name)
                        download_size.config(text="Size :" + str(size)+ "MB")
                        download_loc.config(text="Path :" +direct)

                    except:
                        download_out.config(text = "Download Failed", font = (12))
            except:
                download_out.config(text = "Moving Error", font = (12))
        except:
            path_error.config(text = "Please insert valid path")



heading = Label(window, text="Youtube Video Downloader", background="gray3", foreground="dark orange",
                font=("Bahnschrift SemiBold", 28, "bold"))
heading.pack(anchor="center", pady=10)

link = Label(window, text="URL", background="gray3", foreground="dark orange",
             font=("Bahnschrift SemiBold", 10))
link.pack(anchor="nw", padx=30, pady=25)
entry_url = StringVar()
link_ent = Entry(window, width=52, textvariable=entry_url)
link_ent.place(x=90, y=83)
link_error = Label(window, background="gray3", foreground="dark orange",
                   font=("Bahnschrift SemiBold", 10))
link_error.place(x=300, y=110)
path = Label(window, text="Path", background="gray3", foreground="dark orange",
             font=("Bahnschrift SemiBold", 10))
path.pack(anchor="nw", padx=30, pady=2)
path_holder = Label(window, text="\t\t\t", background="white", foreground="black",
                    font=("Bahnschrift SemiBold", 10))
path_holder.place(x=92, y=130)
from tkinter import ttk

path_style = ttk.Style()
path_style.configure("PT.TButton", background="DarkOrange", foreground="DarkOrange",
                     font=("Bahnschrift SemiBold", 10))
path_btm = Button(window, width=11, text="Select Path", style="PT.TButton", command = open_path)
path_btm.place(x=323, y=125)
path_error = Label(window, text="demo", background="gray3", foreground="dark orange",
                   font=("Bahnschrift SemiBold", 10))
path_error.place(x=315, y=190)
Download_type = Label(window, text="Download Type", background="gray3", foreground="dark orange",
                      font=("Bahnschrift SemiBold", 10))
Download_type.pack(anchor='w', padx=30, pady=25)
options = ["High Quality", "Low Quality", "Audio"]
types = ttk.Combobox(window, values=options, width=23)
types.current(0)
types.place(x=140, y=190)
choose_type = Label(window, text="Choose Type", background="gray3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
choose_type.place(x=315, y=190)
download_style = ttk.Style()
download_style.configure("DD.TButton", background="DarkOrange", foreground="DarkOrange",
                     font=("Bahnschrift SemiBold", 10))
download_btn = Button(window, width=50, text="Download", style="PT.TButton", command = Download)
download_btn.pack(anchor = "center", pady = 30)
download_out = Label(window, text="Wait if system show No Responding during Download", background="gray3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
download_out.pack(anchor = "center", pady =10)
download_name = Label(window, background="gray3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
download_name.pack(anchor = "nw", padx =30, pady =10)
download_size = Label(window, background="gray3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
download_size.pack(anchor = "nw", padx =30, pady =10)
download_loc = Label(window, background="gray3", foreground="dark orange",
                    font=("Bahnschrift SemiBold", 10))
download_loc.pack(anchor = "nw", padx =30,pady =10)
mainloop()