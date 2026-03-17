# ACNH Installer
# Creato il 14 Marzo 2026
# Creato da mitzikritzi2191

# "Path" ci permette di utilizzare la home directory dell'utente
from pathlib import Path
# Questo ci permette di usare funzionalità come creare delle directory
import os
# Questo ci permette di scaricare file da internet
import requests
# Questo ci permette di estrarre i file
from zipfile import ZipFile
# Questo ci permette di muovere i file
import shutil

# Settare la variabile "home" dentro Path.home() così possiamo usare la home directory dell'utente
home = Path.home()
# Memorizzo la cartella Download dell'utente
downloads_folder = f"{home}\\Downloads"
# Memorizzo l'url di Eden come stringa per usarlo dopo
eden_url = "https://git.eden-emu.dev/eden-emu/eden/releases/download/v0.2.0-rc2/Eden-Windows-v0.2.0-rc2-amd64-msvc-standard.zip"
# Memorizzo il tipo di download
file_type = {"downloadformat": "zip"}
# Setto il nome del file dello zip di Eden
file_name = f"{home}\\Downloads\\Eden.zip"
# Setto la destinazione finale di Eden
extracted_eden = f"{home}\\Downloads\\Eden"
# Setto la destinazione di "user" e "keys" di Eden
user_dir = f"{extracted_eden}\\user"
keys_dir = f"{user_dir}\\keys"
# Check di variabili dei file
fw_check = Path(f"{home}\\Downloads\\Firmware.21.0.0.zip")
keys_check = Path(f"{home}\\Downloads\\prod.keys")
# Setto dove il firmware verrà installato
fw_install_path = f"{user_dir}\\nand\\system\\contents\\registered"

# Stampa testo sulla console
print("Ciao! Benvenuto/a nell'installer ufficiale di ACNH.")
print("Questo script scaricherà e installerà Eden per te")
print("Inclusi prod.keys e title.keys!")
# Ricevo consenso per scaricare Eden
consent = input("Posso scaricare l'ultima versione di Eden? (in data 16/03/2026 è v0.2.0-rc2!) (Sì/No): ")

# Questa funzione scarica Eden
def downloadEden(consent):
    # Se il consenso non è stato dato, termina il programma
    # So che l'if è lunghetto, ma ciò fa sì che siano incluse tutte le combinazioni di NO
    if consent == "No" or consent == 'N' or consent == 'n' or consent == "no" or consent == "nO" or consent == "NO":
        print("Non preoccuparti ^^ non installerò Eden")
        print("Questo programma sarà terminato. Grazie per averlo usato!")
    # Se il consenso è stato dato, scarica Eden
    # Di nuovo, un elif lunghetto ma fa sì che siano inclusi tutti gli spelling in inglese e italiano
    elif consent == "Yes" or consent == "yes" or consent == 'Y' or consent == 'y' or consent == 'S' or consent == 's' or consent == "Si" or consent == "Sí" or consent == "yEs" or consent == "yES" or consent == "YES" or consent == "sí" or consent == "SÍ" or consent == "sÍ" or consent == "si":
        # Dico all'utente che sto scaricando Eden
        print("Ok! Download di Eden in corso...")
        # Mando la richiesta al gitlab di Eden e scarico
        downloaded_file = requests.get(eden_url, params=file_type)
        # Controllo se il file è corrotto
        sanity_check = downloaded_file.ok
        # Se il sanity check fallisce, dico all'utente che il download è fallito e di riprovare nuovamente
        if sanity_check == False:
            print("Download fallito (Sanity check failure)! Per favore, riapri il programma.")
        # Se il sanity check avviene con successo, dico all'utente che il download si è concluso con successo e salvo il file
        elif sanity_check == True:
            print("Download completato con successo! Salvataggio del file...")
            with open(file_name, mode="wb") as file:
                file.write(downloaded_file.content)
            print(f"Eden è stato scaricato e salvato in {file_name}! Preparazione per il prossimo step dell'installazione...")
downloadEden(consent)
# Notifica l'utente che cosa accadrà nella fase 2 dell'installazione
print(f"Nella seconda fase dell'installazione, estrarrò 'Eden.zip', collocato nella directory {file_name}!")
print("Inoltre, creerò una cartella 'user' nella directory di Eden e una sottocartella chiamata 'keys' ^-^")

# Questa funzione imposta Eden per l'uso
def setupEden():
    # Apro il file ed estraggo dove deve andare
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractall(path=f"{extracted_eden}")
    # Notifico l'utente che Eden è stato estratto e dov'è disponibile
    print(f"Eden è stato estratto ed è disponibile in {extracted_eden}!")
    # Dico all'utente che stiamo creando una nuova directory
    print("Creazione della directory 'user' in corso...")
    # Creazione effettiva della directory
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    # Dico all'utente che ha avuto successo
    print("'user' directory creato!")
    # Ora stessa cosa ma per le keys
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
    print("'keys' directory creato!")
    # ...e firmware
    if not os.path.exists(fw_install_path):
        os.makedirs(fw_install_path)
    print("Percorso di installazione del Firmware creato!")
setupEden()
# Informo l'utente che Eden è installato ed è portatile, dopo dirò che stiamo controllando nella cartella Download
print(f"Eden è stato installato ed è un'installazione portatile! Ora controllo la tua cartella Download per prod.keys!")

# Installo keys e firmware
def installKeysNfw():
    # Dico all'utente che stiamo installando le keys
    print("Installazione delle keys in corso! Attendi...")
    try:
        # Tento di spostare le keys nella nostra 'keys' directory
        shutil.move(keys_check, f"{keys_dir}\\prod.keys")
        # Notifica di un'installazione compiuta
        print("Keys installati! Installazione del firmware in corso...")
    # Se il file non è stato trovato, dico all'utente come risolvere, poi continuo
    except FileNotFoundError:
        print("Keys non trovate! Per favore, inseriscile nella cartella Download del tuo computer e assicurati che il file sia chiamato 'prod.keys'!")
    try:
        # Estraggo il firmware dove deve andare
        with ZipFile(fw_check, 'r') as zObject:
            zObject.extractall(path=f"{fw_install_path}")
        # Notifica di un'installazione compiuta
        print("Firmware installato!")
    # Se il firmware non è stato trovato, dico all'utente come risolvere
    except FileNotFoundError:
        print("File zip del firmware non trovato! Per favore, inserisci il file zip del firmware nella cartella Download del tuo computer e assicurati che il file sia chiamato 'Firmware.21.0.0.zip'!")
installKeysNfw()

# Dico all'utente che Eden è stato installato e di premere Invio per uscire
# e un piccolo advertising hehe :Bellapsycho:
print("Ecco qua! Se non ancora non ci sei, unisciti al nostro server discord per divertenti treasure islands e fare qualche hangout!")
print("https://discord.gg/actreasurehub")
end = input("Eden è stato installato! Premi Invio per uscire!")
