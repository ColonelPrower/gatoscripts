# Imports
import os
import sys
import subprocess
import requests
from tqdm import tqdm


TIMEOUT_SECS = 60
# Welcome message
print('Download and copy to usb iso files')

# Paths
# get current working directory
cwd = os.getcwd()

urldownload = input('enter url of iso file')
filename = urldownload.split('/')[-1]
print(filename)

#device scan and select
while True:
    subprocess.run('lsblk',check=True)
    print('select usb drive endpoint CAREFULLY normally is sdb or sda if not using a ssd as the OS drive')
    usbdrive = input('type R to rescan > ')
    if usbdrive.upper() != 'R':
        break

#confirmation
while True:
    print(f"I will download {filename} and record it in /dev/{usbdrive}")
    confirmInput = input("if this is ok? Y/N >")
    if confirmInput.upper() == 'N':
        sys.exit('Aborting operation')
    if confirmInput.upper() == 'Y':
        break
    print('please confirm')

print('Begin operation')

response = requests.get(urldownload, stream=True, timeout=TIMEOUT_SECS)
total_size = int(response.headers.get('content-length',0))


with open(filename,'wb') as file:
    for data in tqdm(response.iter_content(chunk_size=4096),total=total_size // 4096, unit='KB'):
        file.write(data)

if not os.path.isfile(filename):
    sys.exit("There was a problem saving the image, aborting")

print("Download done, I will write image NOW, do not remove any device until is done")

command = f"sudo dd if={filename} of=/dev/{usbdrive} bs=4M status=progress conv=fdatasync"
try:
    subprocess.run(command,shell=True, check=True)
    print("Finished recording ^_^")
except subprocess.CalledProcessError as e:
    print(f"Error ocurred while writing into device: {e}")
