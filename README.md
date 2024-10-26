# 使用Jupyter Book和GitHub Pages搭建个人网站

🐍 更新[conda](https://docs.anaconda.com/miniconda/)；新建一个名为`latest`的conda环境，在其中安装最新版本的Python；激活该环境；更新`pip`；使用`pip`在其中安装`jupyter-book`、`furo`和`ghp-import`三个Python包：

```shell
conda update -n base conda
conda create -n latest python -y
conda activate latest
pip install -U pip
pip install -U jupyter-book furo ghp-import
```

📓 跳转到本地的用户个人目录`~`；使用默认模板创建一个[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)，与GitHub账号同名且后缀为`.github.io`；进入创建好的目录中；初始化git仓库，将默认创建`main`分支：

```shell
cd ~
jb create The-Sunflorist.github.io
cd The-Sunflorist.github.io
git init
```

🛖 在[GitHub](https://github.com)上创建一个开源的远程仓库，与GitHub账号同名且后缀为`.github.io`，无需创建`README.md`、`LICENSE`、`.gitignore`等文件。为避免向GitHub执行Git命令时出现超时的情况，在[Gitee](https://gitee.com)上绑定GitHub账号，导入创建好的GitHub远程仓库，默认为私有仓库，添加Push镜像。复制Gitee远程仓库链接，在本地仓库中添加Gitee远程仓库：

```shell
git remote add origin https://gitee.com/the-sunflorist/The-Sunflorist.github.io.git
```

🏗️ 修改`_config.yml`和`_toc.yml`文件的内容；删除不需要的文件；添加新的Markdown文件（[MyST语法小抄](https://jupyterbook.org/en/stable/reference/cheatsheet.html)）；添加`.gitignore`文件，在其中添加`_build/`和其它不需要在`main`分支中进行版本管理的文件夹和文件；重新组织内容文档的文件目录结构。在本地构建Jupyter Book以生成`.html`等网页文件；每次构建后，使用Python脚本修改网页的脚注、目录标题、翻页按钮等：

```shell
# 只重新构建有改动的文件。
jb build . && python replacer.py
```

```shell
# 重新构建所有文件。
jb build --all . && python replacer.py
```

🧹 如需清除所有构建：

```shell
jb clean .
```

🕸️ 每次构建无误后，将本地构建好的网页文件提交到Gitee远程仓库的`gh-pages`分支，会自动同步到GitHub远程仓库：

```shell
ghp-import -n -p -f -m 'update something' _build/html
```

🚀 首次提交`gh-pages`分支后，在GitHub远程仓库的设置中打开Pages服务，Source选择`Deploy from a branch`，Branch选择`gh-pages`分支下的`/ (root)`目录。等待GitHub完成部署后，通过[the-sunflorist.github.io](https://the-sunflorist.github.io)即可访问个人网站。

🗃️ 每当修改了一定的文档内容后，更新本地仓库的`main`分支：

```shell
git acm 'update something'
```

☁️ 每次更新本地仓库的`main`分支后，或者多次更新后，将其提交到Gitee远程仓库的`main`分支，会自动同步到GitHub远程仓库。首次提交`main`分支后，在GitHub和Gitee远程仓库的设置中修改默认分支为`main`分支。

```shell
# 首次提交。
git push -u origin main
```

```shell
# 非首次提交。
git push
```
