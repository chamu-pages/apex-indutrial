import os
import re

files = ['index.html', 'about.html', 'projects.html', 'flat-roofing.html', 'privacy.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove hover effect from header logo (Text color change APEX)
    content = content.replace(
        'class="font-display text-2xl font-bold uppercase leading-none tracking-tight text-white group-hover:text-primary transition-colors">APEX',
        'class="font-display text-2xl font-bold uppercase leading-none tracking-tight text-white">APEX'
    )
    
    # 2. Remove small border around footer logo
    content = content.replace(
        'class="flex size-10 items-center justify-center border border-slate-700 bg-slate-900 text-primary group-hover:bg-slate-800 transition-colors"',
        'class="flex items-center justify-center"'
    )

    # In case it's in projects.html where I replaced it slightly differently:
    content = content.replace(
        'class="flex size-10 items-center justify-center border border-slate-700 bg-slate-900 text-primary group-hover:bg-primary group-hover:text-white transition-colors"',
        'class="flex items-center justify-center"'
    )

    # 3. Footer menu fonts: use font-mono-tech text-xl uppercase tracking-widest
    # Services and Areas lists
    content = content.replace(
        '<ul class="space-y-3 text-sm text-slate-400 font-mono-tech text-lg uppercase tracking-wide">',
        '<ul class="space-y-3 text-slate-400 font-mono-tech text-xl uppercase tracking-widest">'
    )
    
    # Contact list
    content = content.replace(
        '<ul class="space-y-5 text-sm text-slate-400">',
        '<ul class="space-y-5 text-slate-400 font-mono-tech text-xl uppercase tracking-widest">'
    )
    
    # Also bottom footer links (Privacy Policy, Terms of Service, Sitemap)
    content = content.replace(
        'class="flex gap-8 text-xs text-slate-600 uppercase tracking-widest font-mono-tech"',
        'class="flex gap-8 text-slate-600 font-mono-tech text-xl uppercase tracking-widest"'
    )
    # And the copyright text just to be consistent
    content = content.replace(
        'class="text-xs text-slate-600 uppercase tracking-widest font-mono-tech">©',
        'class="text-slate-600 font-mono-tech text-xl uppercase tracking-widest">©'
    )

    # Ensure logo links go to index.html (they mainly already do, but just in case)
    content = re.sub(r'<a href="[^"]*" class="flex items-center gap-3 group">', r'<a href="index.html" class="flex items-center gap-3 group">', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Modifications applied.")
