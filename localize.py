import os
import re

html_files = ['index.html', 'about.html', 'projects.html', 'flat-roofing.html', 'privacy.html']
icons_dir = 'assets/icons/'
img_dir = 'assets/img/'

def load_svg(icon_name):
    for filename in os.listdir(icons_dir):
        if filename.startswith(icon_name + "_") and filename.endswith(".svg"):
            with open(os.path.join(icons_dir, filename), "r", encoding="utf-8") as f:
                content = f.read()
                content = re.sub(r'fill="[^"]+"', 'fill="currentColor"', content)
                return content
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_icon(match):
        classes = match.group(1).replace('material-symbols-outlined', '').strip()
        icon_name = match.group(2).strip()
        
        if icon_name == 'roofing':
            logo_classes = classes.replace('!text-3xl', 'h-10').replace('!text-2xl', 'h-8').replace('text-lg', 'h-6')
            logo_classes = logo_classes.replace('group-hover:scale-110', '').replace('transition-transform', '')
            return f'<img src="assets/img/apex-industrial-logo.webp" alt="Apex Logo" class="{logo_classes.strip()}">'
            
        # Map expand_more to the keyboard_arrow_down SVG the user provided
        if icon_name == 'expand_more':
            icon_name = 'keyboard_arrow_down'

        svg_content = load_svg(icon_name)
        if svg_content:
            svg_content = svg_content.replace('<svg ', f'<svg class="{classes}" ', 1)
            return svg_content
            
        print(f"Warning: Icon {icon_name} not found!")
        return match.group(0)

    # Use a robust regex that handles newlines and extracts the entire class attribute
    # match.group(1) will capture the full class string. match.group(2) will capture the icon text.
    pattern = re.compile(r'<span[^>]*class="([^"]*material-symbols-outlined[^"]*)"[^>]*>\s*([a-z_]+)\s*</span>', re.DOTALL)
    
    content = pattern.sub(replace_icon, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

for file in html_files:
    if os.path.exists(file):
        process_file(file)
