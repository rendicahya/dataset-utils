import os
import pathlib
import random

import click


@click.command()
@click.argument(
    "source_dir",
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
    "target_dir",
    nargs=1,
    required=True,
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--num-videos",
    default=1,
    type=int,
    help="Number of videos to select from each subdirectory (default: 1)",
)
def main(source_dir, target_dir, num_videos):
    target_dir.mkdir(parents=True, exist_ok=True)

    for subdir in source_dir.iterdir():
        if subdir.is_dir():
            video_files = [file for file in subdir.iterdir() if file.suffix == ".mp4"]
            selected_videos = random.sample(
                video_files, min(num_videos, len(video_files))
            )

            if selected_videos:
                target_subdir = target_dir / subdir.name
                target_subdir.mkdir(exist_ok=True)

                for video in selected_videos:
                    video_link = target_subdir / video.name
                    os.symlink(video, video_link)


if __name__ == "__main__":
    main()
