import os
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import hashlib

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()[:10]

# Encryption function
def encrypt():
    global img_path_enc
    msg = msg_entry.get()
    password = pass_entry_enc.get()

    if not img_path_enc:
        messagebox.showerror("Error", "Please select an image for encryption.")
        return

    if not msg:
        messagebox.showerror("Error", "Please enter a secret message.")
        return

    if not password:
        messagebox.showerror("Error", "Please enter a passcode.")
        return

    try:
        img = cv2.imread(img_path_enc)
        img_height, img_width, _ = img.shape

        hashed_pass = hash_password(password)
        msg = hashed_pass + msg

        msg_len_str = str(len(msg)).zfill(3)
        n, m, z = 0, 0, 0

        for i in range(3):
            img[n, m, z] = ord(msg_len_str[i])
            n, m, z = (n + 1) % img_height, (m + 1) % img_width, (z + 1) % 3

        for char in msg:
            img[n, m, z] = ord(char)
            n, m, z = (n + 1) % img_height, (m + 1) % img_width, (z + 1) % 3

        encrypted_img_path = "encrypted_image.png"
        cv2.imwrite(encrypted_img_path, img)

        messagebox.showinfo("Success", "Image encrypted successfully!")
        encrypted_img_path_label.config(text=f"Encrypted Image: {encrypted_img_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

# Decryption function
def decrypt():
    global img_path_dec
    password = pass_entry_dec.get()

    if not img_path_dec:
        messagebox.showerror("Error", "Please select an image for decryption.")
        return

    if not password:
        messagebox.showerror("Error", "Please enter a passcode.")
        return

    try:
        img = cv2.imread(img_path_dec)
        img_height, img_width, _ = img.shape
        n, m, z = 0, 0, 0

        msg_len_str = ""
        for i in range(3):
            msg_len_str += chr(img[n, m, z])
            n, m, z = (n + 1) % img_height, (m + 1) % img_width, (z + 1) % 3
        msg_len = int(msg_len_str)

        extracted_msg = ""
        for _ in range(msg_len):
            extracted_msg += chr(img[n, m, z])
            n, m, z = (n + 1) % img_height, (m + 1) % img_width, (z + 1) % 3

        stored_hashed_pass = extracted_msg[:10]
        secret_message = extracted_msg[10:]

        if hash_password(password) == stored_hashed_pass:
            output_label.config(text="Decrypted message: " + secret_message, fg="green")
        else:
            messagebox.showerror("Error", "Incorrect passcode.")

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# Functions to browse for images
def browse_image_enc():
    global img_path_enc
    img_path_enc = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if img_path_enc:
        original_img_path_label.config(text=f"Selected: {img_path_enc}")

def browse_image_dec():
    global img_path_dec
    img_path_dec = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if img_path_dec:
        decrypted_img_path_label.config(text=f"Selected: {img_path_dec}")

# GUI setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("800x300")
root.configure(bg="#1e1e1e")  # Dark theme background

main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(pady=10)

enc_frame = tk.Frame(main_frame, bg="#1e1e1e")
enc_frame.grid(row=0, column=0, padx=20)

tk.Label(enc_frame, text="Encryption", font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e").pack()

browse_button_enc = tk.Button(enc_frame, text="Select Image", command=browse_image_enc, bg="#444", fg="white")
browse_button_enc.pack()
original_img_path_label = tk.Label(enc_frame, text="No image selected", fg="gray", bg="#1e1e1e")
original_img_path_label.pack(pady=5)

tk.Label(enc_frame, text="Secret Message:", fg="white", bg="#1e1e1e").pack()
msg_entry = tk.Entry(enc_frame, width=40)
msg_entry.pack(pady=5)

tk.Label(enc_frame, text="Passcode:", fg="white", bg="#1e1e1e").pack()
pass_entry_enc = tk.Entry(enc_frame, show="*", width=30)
pass_entry_enc.pack(pady=5)

encrypt_button = tk.Button(enc_frame, text="Encrypt", command=encrypt, bg="green", fg="white")
encrypt_button.pack(pady=10)

encrypted_img_path_label = tk.Label(enc_frame, text="", font=("Arial", 10), fg="white", bg="#1e1e1e")
encrypted_img_path_label.pack()

dec_frame = tk.Frame(main_frame, bg="#1e1e1e")
dec_frame.grid(row=0, column=1, padx=20)

tk.Label(dec_frame, text="Decryption", font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e").pack()

browse_button_dec = tk.Button(dec_frame, text="Select Image", command=browse_image_dec, bg="#444", fg="white")
browse_button_dec.pack()
decrypted_img_path_label = tk.Label(dec_frame, text="No image selected", fg="gray", bg="#1e1e1e")
decrypted_img_path_label.pack(pady=5)

tk.Label(dec_frame, text="Passcode:", fg="white", bg="#1e1e1e").pack()
pass_entry_dec = tk.Entry(dec_frame, show="*", width=30)
pass_entry_dec.pack(pady=5)

decrypt_button = tk.Button(dec_frame, text="Decrypt", command=decrypt, bg="blue", fg="white")
decrypt_button.pack(pady=10)

output_label = tk.Label(dec_frame, text="", font=("Arial", 12, "bold"), fg="red", bg="#1e1e1e")
output_label.pack(pady=10)

img_path_enc = ""
img_path_dec = ""

root.mainloop()