import os
import re

files = [
    r'd:\Chamu Pages\Roof Repair\index.html',
    r'd:\Chamu Pages\Roof Repair\about.html',
    r'd:\Chamu Pages\Roof Repair\projects.html',
    r'd:\Chamu Pages\Roof Repair\flat-roofing.html',
    r'd:\Chamu Pages\Roof Repair\privacy.html'
]

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def span_replacer(match):
        pre = match.group(1)
        cls_attr = match.group(2)
        post = match.group(3)
        inner_text = match.group(4)
        end_tag = match.group(5)
        
        text_stripped = inner_text.strip()
        # Rule 1: Strip brackets if present
        if text_stripped.startswith('[') and text_stripped.endswith(']'):
            naked_text = text_stripped[1:-1].strip()
            
            # Rule 2: Typography bump
            class_match = re.search(r'class="([^"]*)"', cls_attr)
            if class_match:
                classes = class_match.group(1).split()
                
                # change text-xs to text-sm
                if 'text-xs' in classes:
                    classes = ['text-sm' if c == 'text-xs' else c for c in classes]
                    
                # ensure font-bold
                if 'font-bold' not in classes:
                    classes.append('font-bold')
                    
                # Change tracking-[0.3em] to tracking-widest
                if 'tracking-[0.3em]' in classes:
                    classes = ['tracking-widest' if c == 'tracking-[0.3em]' else c for c in classes]
                
                # ensure uppercase
                if 'uppercase' not in classes:
                    classes.append('uppercase')
                    
                # Deduplicate classes to be safe, while preserving order roughly
                seen = set()
                new_classes = []
                for c in classes:
                    if c not in seen:
                        seen.add(c)
                        new_classes.append(c)
                        
                new_cls_attr = 'class="' + ' '.join(new_classes) + '"'
                
                return pre + new_cls_attr + post + naked_text + end_tag
        return match.group(0)

    # Match inner text that contains [ and ] somewhere
    new_content = re.sub(r'(<span\s+)(class="[^"]*")([^>]*>)([^<]*\[[^<]*\][^<]*)(\s*</span\s*>)', span_replacer, content, flags=re.IGNORECASE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Processed {os.path.basename(file_path)}")
