# twitch-chat-analyse

## Installation
Download or clone the repository to your system. \
Download the script from user PetterKraabol from:
* https://github.com/PetterKraabol/Twitch-Chat-Downloader

## Retrieve the data
Run the script of PetterKraabol to download the chat of a Twitch VOD \
For information check their github.

## Remove metadata
Run the script inside of the scripts folder of this repository as followed:
```shell script
$ remove_metadata.sh /path/to/folder/containing/txt
````
Run this twice for two folders of downloaded chat.

Concatenate all output text of one output folder to a singular text file.

## Python script usage
```shell script
$ python3 tca.py /path/to/txt/chat/1 /path/to/txt/chat/2
```

