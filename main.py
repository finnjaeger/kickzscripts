from tkinter import *
from PIL import ImageTk, Image
from Scrape import scrape

root = Tk()
root.title("Instagram Webscraper")
root.geometry("323x656")

dl = BooleanVar()

my_canvas = Canvas(root, width=323, height= 656)
my_canvas.pack(fill= "both", expand = True)

#Initialization of Entry Text Fields
un_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
pw_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
amt_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
pt_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
sc_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
xl_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")
st_entry = Entry(root, font=("Helvetica", 24), width = 14, fg="#336d92")

#Define Initital values for entry fields
un_entry.insert(0, "Username")
pw_entry.insert(0, "Password")
amt_entry.insert(0, "Amount")
pt_entry.insert(0, "Path")
sc_entry.insert(0, "Scraping Account")
xl_entry.insert(0, "Output File Name")
st_entry.insert(0, "Starting from")

def submit():
    scrape(
        account_name=un_entry.get(),
        account_password=pw_entry.get(),
        scraping_account=sc_entry.get(),
        saving_location=pt_entry.get(),
        postAmount=amt_entry.get(),
        excel_sheet_output_name=xl_entry.get(),
        starting_from_post_nr=st_entry.get(),
        download_pics=dl.get()
    )

#Initialization of the download checkbox and the login button
downloadCheckbox = Checkbutton(root, text='Download Pictures', variable=dl, onvalue=True, offvalue=False)
login_btn = Button(root, text="Submit", font=("Helvetica", 20), width = 15, fg= "#336d92", command= submit)

#Placement of all Objects on the Canvas
un_window = my_canvas.create_window(32,20, anchor="nw", window = un_entry)
pw_window = my_canvas.create_window(32,100, anchor="nw", window = pw_entry)
amt_window = my_canvas.create_window(32,180, anchor="nw", window = amt_entry)
pt_window = my_canvas.create_window(32,260, anchor="nw", window = pt_entry)
sc_window = my_canvas.create_window(32,340, anchor="nw", window = sc_entry)
xl_window = my_canvas.create_window(32,420, anchor="nw", window = xl_entry)
st_window = my_canvas.create_window(32,500, anchor="nw", window = st_entry)
dl_window = my_canvas.create_window(32,620, anchor="nw", window = downloadCheckbox)
login_btn_window = my_canvas.create_window(36,580, anchor="nw", window = login_btn)

root.mainloop()