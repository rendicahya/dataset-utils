"""
    This script renames directories by removing the file extension.
"""

import os
import pathlib

import click
from tqdm import tqdm


@click.command()
@click.argument(
    "input",
    nargs=1,
    required=True,
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        exists=True,
        readable=True,
        path_type=pathlib.Path,
    ),
)
def main(input):
    n_subdirs = sum([1 for _ in input.iterdir()])

    with tqdm(total=n_subdirs) as bar:
        for action in input.iterdir():
            bar.set_description(action.name)

            for video in action.iterdir():
                if not os.path.isdir(video):
                    continue

                video.rename(video.parent / video.name.split(".")[0])

            bar.update(1)


if __name__ == "__main__":
    main()
