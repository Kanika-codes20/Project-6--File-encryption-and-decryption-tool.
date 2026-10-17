from cryptography.fernet import Fernet, InvalidToken

#Load the existing key or create one if it doesn't exist.
try:
    with open("secret.key","rb") as key_file:
        key = key_file.read()
    print("\nExisting key loaded.")

except FileNotFoundError:
    key = Fernet.generate_key()

    with open("secret.key","wb") as key_file:
        key_file.write(key)
        print("New key created and saved.")

#Create the fernet object.
try:
    cipher = Fernet(key)
except ValueError:
    print("Error: The encryption key is invalid or damaged.")
    print("Please restore a valid backup of secret.key.")
    raise SystemExit


while True:
    # Display the menu.
    print("\n===== File Encryption Tool =====")
    print("E. Encrypt File.")
    print("D. Decrypt File.")
    print("Q. Quit.")

    choice = input("Choose an option: ").strip().lower()

    if choice == "q":
        print("Thank you for using the File Encryption/Decryption tool.")
        break

    elif choice == "e":
        filename = input("Enter the name of the file to encrypt: ").strip()
        if not filename:
            print("Error: Please enter a filename.")
            continue
        try:
            # Read the original file.
            with open(filename, "rb") as file:
                file_data = file.read()

            # Encrypt the contents.
            encrypted_data = cipher.encrypt(file_data)

            # Create the encrypted filename
            encrypted_filename = filename + ".encrypted"

            # Save the encrypted file.
            with open(encrypted_filename, "xb") as file:
                file.write(encrypted_data)

            print("Data encrypted successfully!")
            print("Encrypted file: " + encrypted_filename)
        except FileNotFoundError:
            print("Error: filename does not exist.")
        except FileExistsError:
            print("Error: The encrypted output file already exists.")

    elif choice == "d":
        encrypted_filename = input("Enter the name of the encrypted file: ").strip()

        if not encrypted_filename:
            print("Error: Please enter a filename.")
            continue
        if not encrypted_filename.endswith(".encrypted"):
            print("Error: The filename must end with '.encrypted'.")
            continue
        try:
            # Read the encrypted file.
            with open(encrypted_filename, "rb") as file:
                encrypted_data = file.read()

            # Decrypt the contents.
            decrypted_data = cipher.decrypt(encrypted_data)

            # Create the decrypted filename.
            original_filename = encrypted_filename.removesuffix(".encrypted")
            decrypted_filename = original_filename + ".decrypted"

            # Save the recovered file.
            with open(decrypted_filename, "xb") as file:
                file.write(decrypted_data)

            print("File decrypted successfully!")
            print("Decrypted Filename: ",decrypted_filename)
        except FileNotFoundError:
            print("Error: The encrypted file was not found.")
        except InvalidToken:
            print("Error: Decryption failed. The key or encrypted data may be invalid.")
        except FileExistsError:
            print("Error: The decrypted output file already exists.")

    else:
        print("Invalid choice. Please select E, D or Q.")
