# ACNH Installer
# Created March 14th, 2026
# Created by mitzikritzi2191

# Path allows us to use the user's home directory
from pathlib import Path
# This allows us to use functionalities such as making directories
import os
# This allows us to download files from the internet
import requests
# This allows us to extract files
from zipfile import ZipFile
# This allows us to move files
import shutil

# Set a variable called "home" to Path.home() so we can use the user's home directory
home = Path.home()
# Store the user's download folder
downloads_folder = f"{home}\\Downloads"
# Store eden's url as a string for use later
eden_url = "https://git.eden-emu.dev/eden-emu/eden/releases/download/v0.2.0-rc2/Eden-Windows-v0.2.0-rc2-amd64-msvc-standard.zip"
# Store the type of download
file_type = {"downloadformat": "zip"}
# Set the file name of the eden zip
file_name = f"{home}\\Downloads\\Eden.zip"
# Set the destination of where eden is installed
extracted_eden = f"{home}\\Downloads\\Eden"
# Set the destination of the eden user directory and keys
user_dir = f"{extracted_eden}\\user"
keys_dir = f"{user_dir}\\keys"
# File checking variables
fw_check = Path(f"{home}\\Downloads\\Firmware.21.0.0.zip")
keys_check = Path(f"{home}\\Downloads\\prod.keys")
# Set where the firmware is to be installed
fw_install_path = f"{user_dir}\\nand\\system\\contents\\registered"

# Print text to the console
print("Hello! Welcome to the official installer for ACNH.")
print("This script will download eden for you and install")
print("the Prod.keys file and Title.keys file for you!")
# Get consent to download eden
consent = input("May I download the latest eden version? (As of 16/03/2026 that is v0.2.0-rc2!) (Yes/No): ")

# This function downloads eden
def downloadEden(consent):
    # If consent is not given, Terminate the program
    # I know the if statement is a bit lengthy but this ensures every possible combination of the word "No"
    if consent == "No" or consent == "no" or consent == "nO" or consent == "NO":
        print("That's okay ^^ I will not download Eden.")
        print("This program will be terminated. Thank you for using it!")
    # If consent is given, Download eden
    # Again, another lengthy elif statement but this ensures every spelling of yes in both english and spanish
    elif consent == "Yes" or consent == "yes"  or consent == "Si" or consent == "Sí" or consent == "yEs" or consent == "yES" or consent == "YES" or consent == "sí" or consent == "SÍ" or consent == "sÍ" or consent == "si":
        # Tell the user we're downloading ede
        print("Okay! Downloading Eden now...")
        # Send a request to Eden's gitlab and download
        downloaded_file = requests.get(eden_url, params=file_type)
        # Check if the file is corrupted
        sanity_check = downloaded_file.ok
        # If the sanity check fails, tell the user that the download failed and to run the program again
        if sanity_check == False:
            print("Download Failed! Please restart the program.")
        # If the sanity check passes, Tell the user that the download succeeded and save the file
        elif sanity_check == True:
            print("Download Succeeded! Now saving...")
            with open(file_name, mode="wb") as file:
                file.write(downloaded_file.content)
            print(f"Eden has been downloaded and saved to {file_name}! Now preparing for the next steps in installation!")
downloadEden(consent)
# Notify to the user what is going to happen in phase 2 of install
print(f"In phase two of installation, I will be extracting 'Eden.zip' that is located in {file_name}!")
print("I will also be creating a folder called 'user' in the Eden directory, and I will be creating a subdirectory called 'keys' ^-^")

# This function sets up eden
def setupEden():
    # Open the file and extract to where we want it to go
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractall(path=f"{extracted_eden}")
    # Notify the user that Eden has been extracted and where it is available
    print(f"Eden has been extracted and is available in {extracted_eden}!")
    # Tell the user we're making a new directory
    print("Now creating directory 'user'!")
    # Actually create the directory
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    # Tell the user we made it
    print("'user' directory created!")
    # Now do the same thing except this time for keys
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
    print("'keys' directory created!")
    # ...and firmware
    if not os.path.exists(fw_install_path):
        os.makedirs(fw_install_path)
    print("Firmware install path created!")
setupEden()
# Inform the user eden is installed and its a portable install, Then tell them we're searching the downloads folder
print(f"Eden has now been installed and is a portable installation! I will be searching your downloads folder for Prod.keys now!")

# Install the keys and firmware
def installKeysNfw():
    # Tell the user we're installing keys
    print("Installing keys! Please wait a moment...")
    try:
        # Attempt to move the keys into our keys directory
        shutil.move(keys_check, f"{keys_dir}\\prod.keys")
        # Notify of a successful install
        print("Keys installed! Now installing firmware...")
    # If the file isnt found, tell the user how to fix it, then continue
    except FileNotFoundError:
        print("Keys file not found! Please put them in the Downloads folder on your computer and ensure its named 'prod.keys'!")
    try:
        # Extract the firmware to where it needs to go
        with ZipFile(fw_check, 'r') as zObject:
            zObject.extractall(path=f"{fw_install_path}")
        # Notify of a successful install
        print("Firmware installed!")
    # If firmware isnt found, tell the user how to fix it
    except FileNotFoundError:
        print("Firmware zip not found! Please put the firmware zip in the Downloads folder on your computer and ensure its named 'Firmware.21.0.0.zip'!")
installKeysNfw()

# Tell the user that eden has been installed and to press enter to exit
# and do a lil advertising :Bellapsycho:
print("That's all! If you aren't already, join our discord server for fun treasure islands and hangouts!")
print("https://discord.gg/actreasurehub")
end = input("Eden has been installed! Press enter to exit!")