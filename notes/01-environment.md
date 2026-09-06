# 第 1 周 — 环境搭建

## 安装清单
- Git 2.43
- Python 3.12
- VSCode 1.136
- 课程依赖（numpy，见仓库根目录 `requirements.txt`）

## 验证

> 注意：Windows 上命令是 `python`（或 `py -3.12`）；macOS / Linux 上是 `python3` / `python3.12`。下面两段按系统选其一执行。

Windows（PowerShell / CMD）：
```bash
git --version
python --version
code --version
```

macOS / Linux：
```bash
git --version
python3 --version
code --version
```

## 安装课程依赖（numpy 等）

在仓库根目录执行：
```bash
# Windows
pip install -r requirements.txt
# macOS / Linux
pip3 install -r requirements.txt
```
验证：
```bash
python -c "import numpy; print(numpy.__version__)"
```

## Git 初始配置
```bash
git config --global user.name "Mingxing-bigdata"
git config --global user.email "1783792729@qq.com"
```

## 常见坑
- 国内网络访问 GitHub 慢：使用 `GitHub520` 项目维护的 hosts
- VSCode GUI 在无头服务器不可用：用 `code serve-web` 在浏览器中打开
