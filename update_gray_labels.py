import os
import re

files = [
    r'd:\Chamu Pages\Roof Repair\index.html',
    r'd:\Chamu Pages\Roof Repair\about.html',
    r'd:\Chamu Pages\Roof Repair\projects.html',
    r'd:\Chamu Pages\Roof Repair\flat-roofing.html',
    r'd:\Chamu Pages\Roof Repair\privacy.html'
]

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def label_replacer(match):
        full_tag = match.group(0)
        tag_name = match.group(1)
        cls_attr = match.group(2)
        
        class_match = re.search(r'class="([^"]*)"', cls_attr)
        if class_match:
            classes = class_match.group(1).split()
            
            # Identify gray micro labels
            # 1. Must have a slate color in the 400-600 range
            # 2. Must be uppercase
            # 3. Must NOT be one of the orange labels we just updated (no text-primary)
            # 4. Must NOT be one of the hero titles we just updated (no text-xl)
            
            is_gray = any(c in ['text-slate-400', 'text-slate-500', 'text-slate-600'] for c in classes)
            is_uppercase = 'uppercase' in classes
            is_orange = 'text-primary' in classes
            is_hero = 'text-xl' in classes
            
            # Also catch the ones that might have just text-xs and tracking-[0.3em] but no explicit slate color in the classes (inherited)
            # or the ones we previously touched that might be text-slate-400 now
            
            if (is_gray or 'text-xs' in classes) and is_uppercase and not is_orange and not is_hero:
                # Target styles: text-slate-300 font-bold uppercase text-xs tracking-wider block mb-1
                
                # Filter out old typography and color classes
                new_classes = [c for c in classes if not c.startswith('text-slate-') and not c.startswith('tracking-') and c not in [
                    'text-sm', 'text-xs', 'font-bold', 'font-mono-tech', 'font-light', 'block', 'mb-2', 'mb-3', 'mb-1'
                ]]
                
                # Add new standardized classes
                standard_style = ['text-slate-300', 'font-bold', 'uppercase', 'text-xs', 'tracking-wider', 'block', 'mb-1']
                for style in standard_style:
                    if style not in new_classes:
                        new_classes.append(style)
                
                new_cls_attr = f'class="{" ".join(new_classes)}"'
                return full_tag.replace(cls_attr, new_cls_attr)

        return full_tag

    # Match <span> and <strong> with class attributes
    # Pattern to find tags like <span class="..."> or <strong class="...">
    tag_pattern = re.compile(r'<(span|strong)\s+([^>]*class="[^"]*"[^>]*)>', re.IGNORECASE)
    
    new_content = tag_pattern.sub(label_replacer, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

for f in files:
    process_file(f)
    print(f"Processed {os.path.basename(f)}")
