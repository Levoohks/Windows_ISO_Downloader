
import os
import urllib.request

def download_windows_iso():
    url = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=41653"
    file_name = "Windows_10_English_64bit.iso"
    urllib.request.urlretrieve(url, os.path.join(os.path.expanduser("~"), "Desktop", file_name))

def main():
    answer = input("Do you want to download the Windows 10 ISO? (y/n) ")
    if answer == "y":
        download_windows_iso()
    else:
        print("Ok, bye!")

if __name__ == "__main__":
    main()