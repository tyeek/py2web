# 静态站点生成器

## 项目简介
这是一个基于 Python 的轻量级静态站点生成工具，主要用于将 Markdown 文件转换为 HTML 页面，并结合模板生成一个完整的静态网站。它支持多种 Markdown 扩展，提供了自定义导航菜单的功能，并且可以将静态资源文件复制到输出目录中。

## 功能特点
- **Markdown 文件处理**：支持将 Markdown 文件转换为 HTML，支持代码块、表格、代码高亮和目录生成。
- **自定义导航菜单**：通过配置文件定义导航菜单项，这些菜单项会显示在生成的 HTML 页面中。
- **模板引擎**：使用 Jinja2 模板引擎，支持自定义模板。
- **静态文件处理**：支持将静态资源文件从指定目录复制到输出目录。
- **跨平台支持**：支持 Windows 和其他操作系统，确保路径兼容性。
- **HTML 内容优化**：删除生成的 HTML 内容中的多余空行，确保生成的 HTML 文件更加简洁。

## 快速开始

### 安装依赖
确保你已经安装了 Python 3。然后运行以下命令安装项目依赖：
```bash
pip install -r requirements.txt
```

### 编写文档
在 `docs` 目录中添加 Markdown 文件。例如：
```
docs/
├── index.md
├── about.md
├── guides/
│   ├── getting-started.md
│   └── advanced.md
```

### 配置文件
创建一个 `config.json` 文件，定义输出目录、Markdown 文件目录和导航菜单。示例配置文件：
```json
{
  "output_dir": "_site",
  "markdown_dir": "docs",
  "navigation": [
    {"title": "首页", "link": "index.html"},
    {"title": "关于", "link": "about.html"},
    {"title": "指南", "link": "guides/getting-started.html"}
  ]
}
```

### 生成站点
运行以下命令生成站点：
```bash
python main.py
```

### 查看结果
打开 `_site` 目录中的 HTML 文件，查看生成的站点。

## 注意事项
该项目目前仍处于开发阶段，部分功能可能不够完善，使用时请注意。
