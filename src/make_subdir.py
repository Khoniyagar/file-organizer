from pathlib import Path
import re
import shutil


def make_subdir(directory):
    for show in directory.iterdir():

        if not show.is_dir():
            continue

        for file in show.iterdir():

            if not file.is_file():
                continue

            match = re.search(
                r"S(\d+)E\d+",
                file.name,
                re.IGNORECASE
            )

            if not match:
                continue

            season = int(match.group(1))

            season_dir = show / f"Season {season}"
            season_dir.mkdir(exist_ok=True)

            destination = season_dir / file.name

            if not destination.exists():
                shutil.move(file, destination)