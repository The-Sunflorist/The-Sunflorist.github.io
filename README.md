# 使用Jupyter Book搭建个人网站

⚙️ 新建一个名为`latest`的[conda](https://docs.anaconda.com/miniconda/)环境，在其中安装最新版本的Python；激活该环境后，更新`pip`；使用`pip`在其中安装`jupyter-book`和`ghp-import`两个Python包：

```shell
conda create -n latest python -y
conda activate latest
pip install -U pip
pip install -U jupyter-book ghp-import
```

📓 选择一个合适的目录，此处选择用户的个人目录`~`；使用默认模板创建一个与GitHub账号同名且后缀为`.github.io`的[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)，完成后进入创建好的目录中：

```shell
cd ~
jb create The-Sunflorist.github.io
cd The-Sunflorist.github.io
```

🛖 在GitHub上创建一个与GitHub账号同名且后缀为`.github.io`的开源代码仓库，无需创建`README.md`、`LICENSE`、`.gitignore`等文件，仓库创建完成后复制仓库的链接。在本地的Jupyter Book目录中初始化git仓库，将默认创建`main`分支，添加GitHub上的远程仓库：

```shell
git init
git remote add origin https://github.com/The-Sunflorist/The-Sunflorist.github.io.git
```

🔧 修改`_config.yml`和`_toc.yml`文件的内容，删除不需要的文件，添加新的Markdown文件（[MyST语法小抄](https://jupyterbook.org/en/stable/reference/cheatsheet.html)）；添加`.gitignore`文件，在其中添加`_build/`和其它不需要在`main`分支中进行版本管理的文件夹和文件；重新组织内容文档的文件目录结构。每当本地仓库`main`分支中的内容可以发布时，在本地构建Jupyter Book以生成`.html`等网页文件：

```shell
# 只重新构建有修改的文件。
jb build .
```

```shell
# 重新构建所有文件。
jb build --all .
```

🧹 如需清除所有构建：

```shell
jb clean .
```

🕸️ 每次构建无误后，将本地构建好的网页文件提交到GitHub远程仓库的`gh-pages`分支：

```shell
ghp-import -n -p -f _build/html
```

🔗 首次提交`gh-pages`分支后，在GitHub远程仓库的设置中打开Pages服务，Source选择`Deploy from a branch`，Branch选择`gh-pages`分支下的`/ (root)`目录。等待GitHub完成部署后，通过[https://the-sunflorist.github.io](https://the-sunflorist.github.io)即可访问个人网站。

⌨️ 每次修改文档内容后，更新本地仓库的`main`分支：

```shell
git add .
git cm 'update something'
```

🧑‍💻 每次更新本地仓库的`main`分支后，或者多次更新后，将其提交到GitHub远程仓库的`main`分支：

```shell
# 首次提交。
git push -u origin main
```

```shell
# 非首次提交。
git push
```

✌️ 首次提交`main`分支后，在GitHub远程仓库的设置中修改默认分支为`main`分支。
