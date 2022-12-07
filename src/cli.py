#!/bin/python3

# region Modules

import argparse
import colorama
from colorama import Fore, Style
import crpyt
from crpyt import *
import glob
import os
import subprocess
from pathlib import Path
import shutil

# endregion


def main():
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument("--encrypt", action="store_true")
    argumentParser.add_argument("--decrypt", action="store_true")
    argumentParser.add_argument("--delete_original", action="store_true")
    argumentParser.add_argument("--force", action="store_true")
    argumentParser.add_argument("--key", type=str)
    argumentParser.add_argument("--path", type=str)
    arguments = argumentParser.parse_args()

    workingDirectory = os.getcwd()

    if not arguments.path:
        targetDirectory: str = workingDirectory
    else:
        targetDirectory: str = arguments.path

    print(
        f":: Using the path '{Fore.YELLOW}{os.path.abspath(targetDirectory)}{Fore.RESET}'"
    )

    if not arguments.key:
        print(f":: {Fore.RED}Error{Fore.RESET}: No GPG key provided.")
        sys.exit(1)

    if arguments.force is not True:
        if os.path.abspath(targetDirectory) == os.environ["HOME"]:
            print(
                f":: {Fore.RED}Error{Fore.RESET}: Encrypting the home directory is disabled."
            )
            print(
                f":: {Fore.BLUE}Help{Fore.RESET}: Use the {Fore.YELLOW}--force{Fore.RESET} flag to enable it."
            )
            sys.exit(1)

        for filepath in glob.iglob(f"{targetDirectory}/**/**", recursive=True):
            if os.path.isfile(filepath):
                if arguments.encrypt:
                    encrypt(
                        filepath,
                        deleteOriginal=arguments.delete_original,
                        key=arguments.key,
                    )
                elif arguments.decrypt:
                    decrypt(filepath, deleteOriginal=arguments.delete_original)

        if arguments.decrypt:
            if decryptionCount == 1:
                print(
                    f":: {Style.DIM}Decrypted {decryptionCount} file.{Style.RESET_ALL}"
                )
            else:
                print(
                    f":: {Style.DIM}Decrypted {decryptionCount} files.{Style.RESET_ALL}"
                )
        elif arguments.encrypt:
            if encryptionCount == 1:
                print(
                    f":: {Style.DIM}Encrypted {encryptionCount} file.{Style.RESET_ALL}"
                )
            else:
                print(
                    f":: {Style.DIM}Encrypted {encryptionCount} files.{Style.RESET_ALL}"
                )


if __name__ == "__main__":
    main()