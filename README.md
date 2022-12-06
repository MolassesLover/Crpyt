# Crpyt
[![Ko-Fi](https://img.shields.io/badge/donate-kofi-blue?style=for-the-badge&logo=ko-fi&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://ko-fi.com/molasses)
[![Patreon](https://img.shields.io/badge/donate-patreon-blue?style=for-the-badge&logo=patreon&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://www.patreon.com/molasseslover)

A very simple Python script that calls Shell, allowing you
to encrypt files within a tree using GPG. The script is
hardcoded to encrypt files with 256 bit [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard).

## Usage

In this example, the [`test/`](test/) directory is **encrypted**, leaving only the `.gpg` files:
```sh
➜ python3 encryption.py --encrypt --delete_original --key $MY_GPG_KEY
# Encrypting pets/dogs/inu.txt
# Encrypting pets/cats/neko.txt
# Encrypted 2 files.
```

Then the tree is **decrypted**, removing the `.gpg` files:
```sh
➜ python3 encryption.py --decrypt --delete_original --key $MY_GPG_KEY
# Decrypting pets/dogs/inu.txt.gpg
# Deleting pets/dogs/inu.txt.gpg
# Decrypting pets/cats/neko.txt.gpg
# Deleting pets/cats/neko.txt.gpg
# Decrypted 2 files.
```

## Contributing
Contributions are open, just make sure to sign your
commits, otherwise, your changes will not be merged.