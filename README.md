# 向阳花花农的个人网站搭建步骤

⚙️ 新建一个conda环境，在其中安装最新版本的Python，更新`pip`，使用最新版的`pip`在conda环境中安装`jupyter-book`和`ghp-import`两个包：

```shell
conda create -n latest python -y
conda activate latest
pip install -U pip
pip install -U jupyter-book ghp-import
```

📓 选择一个合适的目录，此处选择用户的个人目录`~`，使用默认模板创建一个与GitHub账号同名且后缀为`.github.io`的Jupyter Book，进入创建好的目录中：

```shell
cd ~
jb create The-Sunflorist.github.io
cd The-Sunflorist.github.io
```

🛖 在GitHub上创建一个与GitHub账号同名且后缀为`.github.io`的开源代码仓库，默认创建`main`分支，无需添加`README.md`、`LICENSE`、`.gitignore`，创建完成后复制仓库的链接。在本地的Jupyter Book目录中初始化git仓库，默认创建`main`分支，添加GitHub上的远程仓库：

```shell
git init
git remote add origin https://github.com/The-Sunflorist/The-Sunflorist.github.io.git
```

🔧 修改`_config.yml`和`_toc.yml`文件的内容，删除不需要的文件，重新组织内容文档的文件目录结构。每次在本地仓库的`main`分支更新内容后，构建Jupyter Book以生成`.html`等网页文件：

```shell
# 只重新构建有更改的文件。
jb build .
```

```shell
# 重新构建所有文件。
jb build --all .
```

```shell
# 清除所有构建。
jb clean .
```

⌨️ 更新本地仓库的`main`分支：

```shell
# alias.acm=!git add . && git commit -m
git acm 'update something'
```

🧑‍💻 将本地仓库中`main`分支的更新同步到GitHub远程仓库的`main`分支：

```shell
# 首次提交。
git push -u origin main
```

```shell
# 非首次提交。
git push
```

🕸️ 每次构建后，将构建好的网页提交到GitHub远程仓库的`gh-pages`分支：

```shell
ghp-import -n -p -f _build/html
```

🔗 首次提交后，在该仓库的设置中打开Pages服务，Source选择`Deploy from a branch`，Branch选择`gh-pages`分支下的`/ (root)`目录。等GitHub完成部署后，通过[https://the-sunflorist.github.io](https://the-sunflorist.github.io)即可访问向阳花花农的个人网站。
