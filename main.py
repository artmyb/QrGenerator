import qrcode
import tkinter as tk
import base64
from PIL import Image, ImageTk
from main_icon import image_data as icon
from io import BytesIO
import pyperclip
from tkinter import filedialog

root = tk.Tk()
root.wm_geometry("400x100")
root.title("QrGenerator")
image_data_bytes = base64.b64decode(icon)
image = Image.open(BytesIO(image_data_bytes))
the_icon = ImageTk.PhotoImage(image)
root.wm_iconphoto(False,the_icon)
root.resizable(False,False)

entry_frame = tk.Frame(root, height = 50)
entry_frame.pack(fill="x", pady = 10)

entry = tk.Entry(entry_frame,width = 55)
entry.pack(side = tk.LEFT, padx = 5)

def paste():
    text = pyperclip.paste()
    entry.delete(0, tk.END)
    entry.insert(0, text)
    return

paste_button = tk.Button(entry_frame, text = "Paste", command = paste)
paste_button.pack(side = tk.LEFT, padx = 5)



def generate():


    file_name = filedialog.asksaveasfile(title = "Save file as", defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All Files", "*.*")))
    file_name = file_name.name
    if not "png" in file_name:
        file_name += ".png"

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    data = entry.get()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_name)

    tk.messagebox.showinfo(title="File Saved!",
                           message="The QR Code has successfully been created and saved.")
    return
generate_button = tk.Button(root, text = "Generate", command = generate)
generate_button.pack(pady = 10)

root.mainloop()

