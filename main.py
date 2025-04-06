import json
import os
import shutil
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader

def load_config():
    with open('config.json', encoding='utf-8') as f:
        return json.load(f)

def process_markdown(config):
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'codehilite',
        'toc'
    ])

    template = Environment(loader=FileSystemLoader('templates')).get_template('base.html')
    
    # 创建输出目录
    # 确保Windows路径兼容性
    output_dir = Path(config['output_dir']).resolve()
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # 统一路径分隔符为POSIX格式
    config['markdown_dir'] = str(Path(config['markdown_dir'])).replace('\\', '/')
    
    # 收集所有导航项
    all_nav_items = []
    # 添加手动配置项（深拷贝）
    all_nav_items.extend([item.copy() for item in config.get('navigation', [])])
    
    for root, _, files in os.walk(config['markdown_dir']):
        for file in files:
            md_path = Path(root) / file
            rel_path = md_path.relative_to(config['markdown_dir'])
            output_path = output_dir / rel_path
            
            if file.endswith('.md'):
                # 处理Markdown文件
                with open(md_path, encoding='utf-8') as f:
                    content = md.convert(f.read())
                
                html_path = output_path.with_suffix('.html')
                html_path.parent.mkdir(parents=True, exist_ok=True)
                
                html_content = template.render(
                    config=config,
                    content=content,
                    navigation=all_nav_items,
                    toc=md.toc
                )

                # 删除多余的空行
                html_content = "\n".join(line for line in html_content.split("\n") if line.strip())

                with open(html_path, 'w', encoding='utf-8') as f:
                    if file == 'index.md':
                        html_content = html_content.split('<aside')[0] + html_content.split('</aside>\n')[1]
                    f.write(html_content)
            else:
                # 直接复制非Markdown文件
                output_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(md_path, output_path)
    
    # 复制静态文件
    if os.path.exists('static'):
        shutil.copytree('static', output_dir / 'static', dirs_exist_ok=True)

if __name__ == '__main__':
    config = load_config()
    process_markdown(config)
    print(f"站点已生成至 {config['output_dir']} 目录")