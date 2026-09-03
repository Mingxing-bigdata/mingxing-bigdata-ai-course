# 第 1 周 — 环境搭建

## 安装清单
- Git 2.43
- Python 3.12
- VSCode 1.136

## 验证
```bash
git --version
python3.12 --version
code --version
```

## Git 初始配置
```bash
git config --global user.name "Mingxing-bigdata"
git config --global user.email "1783792729@qq.com"
```

## 常见坑
- 国内网络访问 GitHub 慢：使用 `GitHub520` 项目维护的 hosts
- VSCode GUI 在无头服务器不可用：用 `code serve-web` 在浏览器中打开
