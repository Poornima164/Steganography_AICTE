# 📌 Secure Data Hiding in Images Using Steganography  

🔒 **Hide Your Secrets in Plain Sight!** 🔒  

Welcome to **Secure-Data-Hiding-in-Images-Using-Steganography**, a powerful tool that enables you to securely embed secret messages within images using **image steganography**. With an easy-to-use graphical interface, you can encrypt your messages into images and retrieve them later with a passcode.  

---

## 🚀 Features  
✅ **Secure Encryption:** Hides secret messages inside images.  
✅ **Password Protection:** Messages are protected with a passcode to prevent unauthorized access.  
✅ **User-Friendly GUI:** Simple and interactive **Tkinter-based** interface.  
✅ **Fast & Lightweight:** Efficient steganography without compromising image quality.  

---

## 📂 Installation & Requirements  

### 🔧 Prerequisites  
Ensure you have **Python 3.x** installed on your system. You also need to install the following dependencies:  

```bash
pip install opencv-python tkinter
```

---

## 🛠️ How to Run  

1️⃣ **Clone this repository** (or download the project files):  
```bash
git clone https://github.com/your-repo/Secure-Data-Hiding-in-Images-Using-Steganography.git
cd Secure-Data-Hiding-in-Images-Using-Steganography
```

2️⃣ **Run the script:**  
```bash
python steganography.py
```

3️⃣ **Use the GUI to encrypt or decrypt messages:**  
- Select an image for encryption.  
- Enter your secret message & passcode.  
- Click **Encrypt** to hide the message inside the image.  
- Select the encrypted image and enter the passcode to retrieve your message.  

---

## 📷 How It Works  

🔹 **Encryption Process:**  
- The message is prefixed with a hashed version of the passcode.  
- The image’s pixels are modified to store the message characters.  
- The output image contains the hidden message securely.  

🔹 **Decryption Process:**  
- Extracts the hidden message from the image.  
- Verifies the passcode by checking the stored hash.  
- Reveals the original secret message only if the passcode is correct.  

---

## 🔒 Security Notice  

⚠️ While this project ensures **basic security** through passcode hashing, it is **not intended for high-level cryptographic security**. For highly sensitive data, consider **strong encryption methods** in addition to steganography.  

---

## 🛠️ Contribution  

Want to enhance this project? Contributions are welcome! Feel free to submit a pull request.  

---

## 📜 License  

This project is **open-source** under the MIT License.  

---

💡 **Happy Encrypting! Keep Your Secrets Safe!** 🔥🔑
