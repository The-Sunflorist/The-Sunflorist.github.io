# 向阳花花农的个人网站

⚙️ 安装环境：

```shell
conda create -n latest python -y
conda activate latest
pip install -U pip
pip install -U jupyter-book ghp-import
```

📓 创建Jupyter Book：

```shell
cd ~
jb create The-Sunflorist.github.io
cd The-Sunflorist.github.io
```

🛖 添加GitHub远程仓库：

```shell
git remote add origin https://github.com/The-Sunflorist/The-Sunflorist.github.io.git
```

🔧 每次更新后，构建Jupyter Book：

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

🧑‍💻 将本地更新的提交同步到GitHub：

```shell
# 首次提交。
git push -u origin main
```

```shell
# 非首次提交。
git push
```

🕸️ 将构建好的网页提交到GitHub仓库的`gh-pages`分支：

```shell
ghp-import -n -p -f _build/html
```

🔗 轻点链接即可访问[向阳花花农的个人网站 https://the-sunflorist.github.io](https://the-sunflorist.github.io)。
