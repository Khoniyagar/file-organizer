from pathlib import Path
import shutil
import re
from make_subdir import make_subdir


def known_dir():
    directory = Path.cwd()
    files = []
    temp_check = []

    if directory.is_dir():
        print("Directory is valid!")
    else:
        print("\nThat directory does not exist!\n")
        return

    # Collect files and split their names into parts
    for item in directory.iterdir():
        if not item.is_file():
            continue

        files.append(
            (item, re.split(r'[\W_]+', item.stem))
        )

    while files:

        # --------------------------------
        # Only one file is left
        # --------------------------------
        if len(files) == 1:
            item = files[0][0]

            folder_name = item.stem
            group_directory = directory / folder_name

            # Create the folder if it does not exist
            group_directory.mkdir(exist_ok=True)

            destination = group_directory / item.name

            # Move the file only if it is not already there
            if item != destination:
                if not destination.exists():
                    shutil.move(item, group_directory)

            files.clear()
            continue

        # --------------------------------
        # Find common parts between files
        # --------------------------------

        for x, y in zip(files[0][1], files[1][1]):
            if x == y:
                temp_check.append(x)
            else:
                break

        common_parts = temp_check.copy()
        temp_check.clear()

        # --------------------------------
        # Find files belonging to the group
        # --------------------------------

        processed = []

        for file in files:
            if all(word in file[1] for word in common_parts):
                processed.append(file[0])

        # If no common part was found, avoid an infinite loop
        if not common_parts:
            item = files[0][0]

            folder_name = item.stem
            group_directory = directory / folder_name
            group_directory.mkdir(exist_ok=True)

            destination = group_directory / item.name

            if not destination.exists():
                shutil.move(item, group_directory)

            files = files[1:]
            continue

        # Create a directory for the current group
        folder_name = ".".join(common_parts)
        group_directory = directory / folder_name
        group_directory.mkdir(exist_ok=True)

        # Move grouped files into the directory
        for item in processed:
            destination = group_directory / item.name

            if not destination.exists():
                shutil.move(item, group_directory)

        # Remove processed files from the list
        files = [
            file
            for file in files
            if file[0] not in processed
        ]

    make_subdir(directory)