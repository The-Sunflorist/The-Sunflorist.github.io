# coding=utf-8
#
# cover_maker.py
# The-Sunflorist.github.io/src/
#
# Created by 向阳花花农(The Sunflorist) on 2024-11-03.
# Copyright © 2024 向阳花花农(The Sunflorist). All rights reserved.
#
# Make covers.


import os
import re
import sys
from argparse import ArgumentParser
from subprocess import run
from typing import final

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

from logger_creator import LoggerCreator

project_path = os.path.abspath(path=os.path.join(sys.path[0], '..'))
logger = LoggerCreator.get_logger(name=os.path.splitext(p=os.path.relpath(path=__file__))[0])


class CoverMaker:
    __sun_img = plt.imread(fname=os.path.join(project_path, 'aux', 'Sun.png'))
    __seal_img = plt.imread(fname=os.path.join(project_path, 'aux', 'Seal.png'))

    __margin = 13
    __sun_size, __sun_left_show, __sun_bottom = 400, 220, -178,
    __seal_size, __seal_bottom = 30, 30
    __openmoji_size, __openmoji_offset = 19, 42

    __author_font_size = __page_number_font_size = 6.6
    __cn_title_font_size = 20
    __en_title_font_size = __genre_font_size = 10
    __cn_en_offset = __en_song_offset = 20
    __song_font_size = 8
    __cn_genre_offset = 46

    __cover_folder_path = os.path.join(os.path.expanduser(path='~'), 'workspace', 'DaVinci')
    os.makedirs(name=__cover_folder_path, mode=0o755, exist_ok=True)

    def __init__(
            self,
            cn_name: str, en_name: str,
            date: str, genre: str, song: str,
            openmoji_name: str,
            index: int,
            compress: bool,
            force: bool,
    ) -> None:
        self.__cn_name, self.__en_name = cn_name, en_name
        self.__date, self.__genre, self.__song, = date, genre, song
        self.__openmoji = plt.imread(fname=os.path.join(project_path, 'aux', 'OpenMoji', f'{openmoji_name}.png'))
        self.__index = index
        self.__compress = compress
        self.__force = force

    # Matplotlib rc: https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
    @mpl.rc_context(rc={
        'figure.dpi': 200, 'savefig.dpi': 500,
        'figure.facecolor': '#F8F9FB', 'figure.edgecolor': '#F8F9FB', 'axes.facecolor': '#F8F9FB',
        'figure.subplot.left': 0, 'figure.subplot.right': 1, 'figure.subplot.bottom': 0, 'figure.subplot.top': 1,
        'xtick.bottom': False, 'xtick.labelbottom': False, 'ytick.left': False, 'ytick.labelleft': False,
        'axes.spines.bottom': False, 'axes.spines.top': False, 'axes.spines.left': False, 'axes.spines.right': False,
        'font.sans-serif': ['Smiley Sans'], 'text.color': '#03045E',
    })
    def make_cover(self, name: str, fig_width: float, fig_height: float, ax_right: float) -> None:
        cover_path = os.path.join(
            self.__cover_folder_path,
            f'{self.__date}_{re.sub(r"\s+", repl="_", string=self.__en_name)}_{name}.png',
        )

        if os.path.exists(path=cover_path):
            if not self.__force:
                logger.yellow(f'Already exist: {os.path.relpath(path=cover_path)}')
                return
            logger.yellow(f'Remaking: {os.path.relpath(path=cover_path)}')

        ax: plt.Axes
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.set_xlim(left=0, right=ax_right)
        ax.set_ylim(bottom=0, top=(ax_top := ax_right * fig_height / fig_width))

        # Plot the sun, seal image, OpenMoji.
        ax.imshow(X=self.__sun_img, extent=(
            ax_right - self.__sun_left_show,
            ax_right - self.__sun_left_show + self.__sun_size,
            self.__sun_bottom,
            self.__sun_bottom + self.__sun_size,
        ))
        ax.imshow(X=self.__seal_img, extent=(
            self.__margin,
            self.__margin + self.__seal_size,
            self.__seal_bottom,
            self.__seal_bottom + self.__seal_size,
        ))

        # Add Chinese title, English title, genre, author statement, OpenMoji, song.
        ax.text(x=self.__margin, y=(cn_title_y := ax_top * 3 / 5), s=self.__cn_name, size=self.__cn_title_font_size)
        ax.text(x=self.__margin, y=cn_title_y - self.__cn_en_offset, s=self.__en_name, size=self.__en_title_font_size)
        ax.text(
            x=self.__margin + self.__openmoji_size,
            y=cn_title_y + self.__cn_genre_offset,
            s=self.__genre,
            size=self.__genre_font_size,
        )
        ax.text(x=self.__margin, y=self.__margin, s=f'向阳花花农原创作品 {self.__index}', size=self.__author_font_size)
        ax.imshow(X=self.__openmoji, extent=(
            self.__margin,
            self.__margin + self.__openmoji_size,
            cn_title_y + self.__openmoji_offset,
            cn_title_y + self.__openmoji_offset + self.__openmoji_size,
        ))
        if pd.notna(self.__song):
            ax.text(
                x=self.__margin,
                y=cn_title_y - self.__cn_en_offset - self.__en_song_offset,
                s=f'曲：《{self.__song}》',
                size=self.__song_font_size,
            )

        # Show and save the figure.
        # plt.show()
        fig.savefig(fname=cover_path)
        plt.close()
        logger.green(f'Saved {os.path.relpath(path=cover_path)}')

        # Compress cover.
        if self.__compress:
            run(args=['open', cover_path, '-a', 'ImageOptim'], check=True)
            logger.yellow(f'Compressing {os.path.relpath(path=cover_path)}')


@final
class Main:
    __argument_paser = ArgumentParser(prog='python src/cover_maker.py')
    __argument_paser.add_argument('-c', '--compress', action='store_true', help='Compress covers with ImageOptim.')
    __argument_paser.add_argument('-f', '--force', action='store_true', help='If a cover exists, force to remake it.')
    __argument_paser.add_argument('-l', '--last', type=int, default=1, help='Make the last LAST covers.')
    __arguments = vars(__argument_paser.parse_args())

    @classmethod
    def main(cls) -> None:
        cover_infos = pd.read_csv(filepath_or_buffer=os.path.join(project_path, 'aux', 'cover_infos.csv'))
        n = len(cover_infos)
        if not (1 <= cls.__arguments['last'] <= n):
            cls.__arguments['last'] = n
        for i, (cn_name, en_name, date, genre, song, openmoji_name) in enumerate(
                cover_infos.values[-cls.__arguments['last']:],
                start=n - cls.__arguments['last'] + 1,
        ):
            cover_maker = CoverMaker(
                cn_name=cn_name, en_name=en_name,
                date=date, genre=genre, song=song, openmoji_name=openmoji_name,
                index=i,
                compress=cls.__arguments['compress'],
                force=cls.__arguments['force'],
            )
            cover_maker.make_cover(name='3_4', fig_width=3, fig_height=4, ax_right=300)
            cover_maker.make_cover(name='4_3', fig_width=4, fig_height=3, ax_right=400)
            cover_maker.make_cover(name='16_9', fig_width=4, fig_height=2.25, ax_right=400)


if __name__ == '__main__':
    Main.main()
    logger.newline()
