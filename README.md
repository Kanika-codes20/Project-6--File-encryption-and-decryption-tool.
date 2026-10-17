# Project-6--File-encryption-and-decryption-tool.

A beginner-friendly Python cybersecurity project that encrypts and decrypts files using Fernet symmetric encryption from the `cryptography` library.

This project was built to practise Python programming, file handling, encryption, key management, and error handling.

##  Features

- **File Encryption:** Encrypts the contents of a user-selected file.
- **File Decryption:** Decrypts files using the correct saved encryption key.
- **Key Management:** Generates and saves a Fernet key when one does not already exist, and reuses the saved key on subsequent runs.
- **Overwrite Protection:** Prevents existing encrypted or decrypted output files from being overwritten.
- **Input Validation:** Handles empty filenames and checks the `.encrypted` extension before decryption.
- **Error Handling:** Handles missing files, existing output files, invalid key formats, and decryption failures.
- **Interactive Menu:** Allows users to encrypt files, decrypt files, or quit the program.

##  Technologies Used

- Python
- `cryptography` library
- Fernet symmetric encryption
- File handling and exception handling

##  Project Structure

```text
FileEncryptionTool/
├── main.py
├── README.md
├── .gitignore
├── secret.key          # Generated locally; do not upload
├── sample.txt          # Example input file; optional
├── sample.txt.encrypted
└── sample.txt.decrypted
```

The sample and output files are examples. Your actual project folder may contain different filenames.

##  Installation and Setup

### 1. Install Python

Install Python if it is not already available on your system.

### 2. Install the required library

Open the terminal in your project environment and run:

```bash
python -m pip install cryptography
```

### 3. Run the program

Navigate to the project folder and execute:

```bash
python main.py
```

The program will create a `secret.key` file if one does not already exist.

##  How to Use

When the program starts, it displays a menu:

```text
===== File Encryption Tool =====
E. Encrypt File
D. Decrypt File
Q. Quit
```

- Enter `E` to encrypt a file.
- Enter `D` to decrypt an encrypted file.
- Enter `Q` to exit.

Enter the filename when prompted. The file should be accessible from the program's working directory, or you can provide an appropriate path.

### Output filenames

- Encrypted output: `sample.txt.encrypted`
- Decrypted output: `sample.txt.decrypted`

The program does not overwrite an existing output file.

##  Key Management and Security

This project uses Fernet symmetric encryption. The same secret key is required to decrypt data that was encrypted with it.

**Important security considerations:**

- Keep `secret.key` private and never commit it to GitHub.
- Store a secure backup of the key.
- If the key is lost, the encrypted files may become unrecoverable.
- Do not use sensitive personal or confidential files for casual testing.
- This project is intended for learning and experimentation, not production-grade file security.

##  What I Learned

Through this project, I practised:

- Reading and writing files in binary mode.
- Encrypting and decrypting file contents.
- Generating and reusing encryption keys.
- Handling exceptions using `try` and `except`.
- Validating user input.
- Preventing accidental file overwrites.
- Building a menu-driven Python application.
- Testing error conditions and debugging code.

##  Project Goal

The goal of this project was to strengthen my Python fundamentals while exploring a practical cybersecurity concept: protecting file contents through encryption.

This is one of my beginner cybersecurity portfolio projects, built as part of my ongoing learning journey.

---

**Author:** Kanika-codes20

*Built with Python as a beginner cybersecurity learning project.* 🔐
