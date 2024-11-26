<!-- Created by 向阳花花农 (The Sunflorist) on 2024-11-22. -->
<!-- The Sunflorist's Shangri-La © 2024 by The Sunflorist is licensed under CC BY-NC-SA 4.0, all rights reserved. -->

<!-- 在文档中插入twemoji -->
<link href="https://emoji-css.afeld.me/emoji.css" rel="stylesheet">

# <i class="em-svg em-building_construction" aria-role="presentation" aria-label=""></i> 向阳花花农的花海施工图

***How Does The Sunflorist Build His Shangri-La?***

> - 《[向阳花花农的花海](https://github.com/The-Sunflorist/The-Sunflorist.github.io)》 © 2024 由[向阳花花农](https://github.com/The-Sunflorist)创作，遵循[CC BY-NC-SA 4.0协议（中文）](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)，保留所有版权。
> - *[The Sunflorist‘s Shangri-La](https://github.com/The-Sunflorist/The-Sunflorist.github.io)* © 2024 by [The Sunflorist](https://github.com/The-Sunflorist) is licensed under [CC BY-NC-SA 4.0 (English)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en), all rights reserved.

## <i class="em-svg em-sunflower" aria-role="presentation" aria-label="SUNFLOWER"></i> 1. 花海

***The Sunflorist's Shangri-La***

- [向阳花花农的花海 GitHub Pages](https://the-sunflorist.github.io)（大陆访问该网址有时较慢）
- [向阳花花农的花海 Read the Docs](https://the-sunflorist.readthedocs.io)（同GitHub Pages内容一致）

## <i class="em-svg em-snake" aria-role="presentation" aria-label="SNAKE"></i> 2. 环境

***Environment***

安装轻便的[Miniconda](https://docs.anaconda.com/miniconda)，无需安装庞大的Anaconda。

更新 `conda`；新建一个名为 `latest` 的conda环境，在其中安装最新版本的 `python`；每次打开终端都需要激活该环境；更新 `pip`；使用 `pip` 在conda环境中安装必要的Python包：

```shell
conda update -n base conda -y
conda create -n latest python -y
conda activate latest

# 如果下载速度过慢，添加选项使用清华PyPI：-i https://pypi.tuna.tsinghua.edu.cn/simple
# 清华PyPI不包含的Python包，使用默认PyPI：-i https://pypi.org/simple
pip install -U pip
pip install -U -r src/requirements.txt
pip install -U -r requirements.txt
```

## <i class="em-svg em-house" aria-role="presentation" aria-label="HOUSE BUILDING"></i> 3. 仓库

***Repositories***

指定路径创建一个[Sphinx](https://github.com/sphinx-doc/sphinx)项目，与[GitHub](https://github.com)账号同名且后缀为 `.github.io`：

```shell
sphinx-quickstart ~/workspace/Sphinx/The-Sunflorist.github.io
```

按提示输入：

```text
> Separate source and build directories (y/n) [n]:
> Project name: 向阳花花农的花海
> Author name(s): 向阳花花农
> Project release []:
> Project language [en]: zh_CN
```

进入创建好的Sphinx项目中；初始化Git仓库，将默认创建 `main` 分支：

```shell
cd ~/workspace/Sphinx/The-Sunflorist.github.io
git init
```

在GitHub上创建一个空白的开源远程仓库，与GitHub账号同名且后缀为 `.github.io`。为避免向GitHub执行Git命令时出现超时的情况，在[Gitee](https://gitee.com)上绑定GitHub账号，导入创建好的GitHub远程仓库，默认为私有仓库，添加Push镜像，每次推送到Gitee的内容会自动同步到GitHub。复制**Gitee**远程仓库链接，在本地仓库中将其添加为名叫 `origin` 的远程仓库：

```shell
git remote add origin https://gitee.com/the-sunflorist/The-Sunflorist.github.io.git
```

## <i class="em-svg em-card_file_box" aria-role="presentation" aria-label=""></i> 4. 文件

***Files***

添加 `.gitignore` 和 `LICENSE`。暂存这两个文件；检查修改：

```shell
git add .gitignore LICENSE
git diff --staged
```

检查无误后，将修改提交到 `main` 分支；创建并切换到 `dev` 分支进行开发：

```shell
git commit -m 'add git ignore, license'
git switch -c dev
```

删除 `make.bat` 和 `_build/`；修改 `Makefile` 和 `conf.py`；添加[MyST](https://myst-parser.readthedocs.io)文本、Python代码、图像等文件。如需将 `.rst` 文件转化为 `.md` 文件：

```shell
conda create -n r2m python -y
conda activate r2m
pip install -U pip
pip install -U "rst-to-myst[sphinx]"
rst2myst convert ./**/*.rst
conda deactivate
```

在 `dev` 分支暂存修改；检查修改：

```shell
git add .
git diff --staged
```

检查无误后，更新 `dev` 分支：

```shell
git commit -m 'add markdowns, images, pythons'
```

在 `dev` 分支稳定后，切换到 `main` 分支；检查 `dev` 分支相对于 `main` 分支的修改：

```shell
git switch main
git diff main dev
```

检查无误后，将 `dev` 分支合并到 `main` 分支：

```shell
git merge dev --no-ff --stat -m 'initial pages'
```

切换回 `dev` 分支继续开发：

```shell
git switch dev
```

## <i class="em-svg em-spider_web" aria-role="presentation" aria-label=""></i> 5. 网页

***Pages***

本地构建网页再部署到GitHub；在[Read the Docs](https://docs.readthedocs.io/en/stable/tutorial/index.html)构建和部署网页。

### <i class="em-svg em-octopus" aria-role="presentation" aria-label="OCTOPUS"></i> 5.1. GitHub

清除 `.tmp/html/`，生成 `.html` 等网页文件保存到 `.tmp/html/` 中，使用Python脚本修改网页的脚注、目录标题、翻页按钮等：

```shell
# 具体的命令在Makefile中
make html
```

将本地构建好的网页文件推送到 `origin` 的 `gh-pages` 分支：

```shell
ghp-import -flnp .tmp/html/
```

首次推送 `gh-pages` 分支后，在GitHub远程仓库的设置中打开Pages服务，Source选择 `Deploy from a branch`，Branch选择 `gh-pages` 分支下的 `/ (root)` 目录。等待GitHub完成部署后，通过[https://the-sunflorist.github.io](https://the-sunflorist.github.io)即可访问向阳花花农的花海。

如果GitHub Pages服务没开始部署，[重新触发构建和部署](https://docs.github.com/en/rest/pages/pages?apiVersion=2022-11-28#request-a-github-pages-build)，注意替换 `<TOKEN>`：

```shell
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/The-Sunflorist/The-Sunflorist.github.io/pages/builds
```

### <i class="em-svg em-page_facing_up" aria-role="presentation" aria-label="PAGE FACING UP"></i> 5.2. Read the Docs

> 需要 `.readthedocs.yaml`， `requirements.txt`。

将 `main` 分支推送到 `origin` 的 `main` 分支：

```shell
# 首次推送
git push -u origin main

# 非首次推送
git push origin main
```

首次推送 `main` 分支后，在GitHub和Gitee远程仓库的设置中修改默认分支为 `main` 分支。 `dev` 分支无需推送到远程仓库。

使用GitHub账号注册和登录Read the Docs，搜索添加GitHub的仓库，名称与GitHub账号同名（确保由此构成的域名没有被占用），默认分支填写 `main`，语言选择 `Simplified Chinese`，第一次导入会开始构建和部署，完成部署后通过[https://the-sunflorist.readthedocs.io](https://the-sunflorist.readthedocs.io)即可访问。

在项目设置中勾选 `Build pull requests for this project` 并保存，之后GitHub上的 `main` 分支一有更新，Read the Docs就会自动重新构建和部署。在 `Addons` 的 `Analytics` 中勾选 `Analytics enabled` 并保存，之后可以在设置中查看网页的访问流量。

## <i class="em-svg em-book" aria-role="presentation" aria-label="OPEN BOOK"></i> 6. 电子书

***eBooks***

在本地生成EPUB和PDF电子书。

### <i class="em-svg em-orange_book" aria-role="presentation" aria-label="ORANGE BOOK"></i> 6.1. EPUB

清除 `.tmp/epub/`，生成 `.epub` 等文件保存到 `.tmp/epub/` 中：

```shell
# 具体的命令在Makefile中
make epub
```

### <i class="em-svg em-closed_book" aria-role="presentation" aria-label="CLOSED BOOK"></i> 6.2. $\LaTeX$和PDF

下载安装[MiKTeX](https://miktex.org/download)，编译$\TeX$文件遇到缺失的包时，MiKTeX Console会弹窗询问安装。打开安装好的MiKTeX Console，选择 `完成个人安装向导`，重启软件后选择 `立即升级` 到标准$\TeX$安装，检查更新。添加 `~/bin` 到终端和GUI应用的 `PATH` 环境变量中：

```shell
echo export 'PATH=~/bin:$PATH' >> ~/.zshrc
sudo launchctl config user path "$HOME/bin:$PATH"
```

为了使 `xelatex` 能够搜索到指定字体，在 `~/Library/Application Support/MiKTeX/texmfs/config/fontconfig/config/localfonts2.conf` 中添加一些存放字体文件的目录，修改为如下内容，注意将 `~` 替换为绝对路径：

```xml
<?xml version="1.0"?>
<fontconfig>
<dir>/System/Library/Fonts/</dir>
<dir>/System/Library/Fonts/Supplemental/</dir>
<dir>~/Library/Fonts/</dir>
</fontconfig>
```

清除 `.tmp/latex/`，生成 `.tex` 和 `.pdf` 等文件保存到 `.tmp/latex/` 中，语言设置为 `zh_CN` 的Sphinx项目将默认使用 `xelatex` 作为$\TeX$引擎，而 `en` 语言默认的 `pdflatex` 不支持编译Unicode字符：

```shell
# 具体的命令在Makefile中
# 使用latexmk的-silent选项减少终端的输出
make latexpdf LATEXMKOPTS="-silent"
```

## <i class="em-svg em-sunny" aria-role="presentation" aria-label="BLACK SUN WITH RAYS"></i> 7. 封面

***Covers***

> 需要 `aux/OpenMoji/`， `aux/Seal.png`， `aux/Sun.png`。

强制重新生成最后一组社交平台上的视频封面，打开[ImageOptim](https://imageoptim.com)压缩生成的封面：

```shell
# 查看帮助：python src/cover_maker.py -h
python src/cover_maker.py -cf
```
