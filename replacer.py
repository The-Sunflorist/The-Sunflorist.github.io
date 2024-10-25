# coding=utf-8
#
# replacer.py
# The-Sunflorist.github.io/
#
# Created by 向阳花花农(The Sunflorist) on 2024-10-25.
# Copyright © 向阳花花农(The Sunflorist). All rights reserved.
#
# Replace a couple of things generated by Jupyter Book and Furo theme.


import os
import re

from sty import fg, rs


class Main:
    old_footer = r'''Copyright &#169;(.|\n)*Furo</a>'''
    new_footer = (r'''Copyright &#169; <a href="https://the-sunflorist.github.io">向阳花花农</a>，The Sunflorist，<code'''
                  ''' class="docutils literal notranslate"><span class="pre">the.sunflorist@foxmail.com</span></code>
            </div>
            向阳花花农原创作品，保留所有版权。The Sunflorist's originals. All rights reserved.''')

    view_button = r'''<div class="view-this-page">(.|\n)*?</div>'''

    old_previous = '<span>Previous</span>'
    new_previous = '<span>人间四月芳菲尽</span>'

    old_next = '<span>Next</span>'
    new_next = '<span>乱花渐欲迷人眼</span>'

    old_toc_title = 'On this page'
    new_toc_title = '一花一世界'

    old_home = '<div class="title">Home</div>'
    new_home = '<div class="title">向阳花花农的花海</div>'

    @classmethod
    def main(cls) -> None:
        folder_path = './_build/html/docs'
        for filename in os.listdir(path=folder_path):
            if filename.startswith('.'):
                continue
            filepath = os.path.join(folder_path, filename)
            with open(file=filepath, mode='r', encoding='utf-8') as file:
                new_content = re.sub(cls.view_button, repl='', string=re.sub(
                    cls.old_footer, repl=cls.new_footer, string=file.read()
                )).replace(cls.old_previous, cls.new_previous).replace(cls.old_next, cls.new_next).replace(
                    cls.old_toc_title, cls.new_toc_title).replace(cls.old_home, cls.new_home)

            if (re.findall(cls.new_footer, string=new_content) and not re.findall(cls.old_previous, new_content)
                    and not re.findall(cls.old_next, new_content) and not re.findall(cls.view_button, new_content)
                    and not re.findall(cls.old_toc_title, new_content) and not re.findall(cls.old_home, new_content)):
                with open(file=filepath, mode='w+', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Replaced content for {filepath}')
            else:
                assert False, f'{fg.red}Failed for {filepath}{rs.all}'


if __name__ == '__main__':
    Main.main()
