import os
import pathlib

import click


@click.command()
@click.argument(
    "source-dir",
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
@click.argument(
    "target-dir",
    nargs=1,
    required=True,
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        path_type=pathlib.Path,
    ),
)
def main(source_dir, target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)

    for subdir in source_dir.iterdir():
        if subdir.is_dir():
            video_files = [file for file in subdir.iterdir() if file.suffix == ".mp4"]

            if video_files:
                target_subdir = target_dir / subdir.name
                target_subdir.mkdir(exist_ok=True)

                video_link = target_subdir / video_files[0].name
                os.symlink(video_files[0], video_link)


if __name__ == "__main__":
    main()
