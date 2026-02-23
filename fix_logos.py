import os
import re

files = ['index.html', 'about.html', 'projects.html', 'flat-roofing.html', 'privacy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove orange bg wrapper in header logo
    # Matches `<div class="... bg-primary ..."> <img ... class="h-10"> </div>`
    content = re.sub(
        r'<div\s+class="[^"]*bg-primary[^"]*border-orange-400/30[^"]*">\s*<img src="assets/img/apex-industrial-logo\.webp" alt="Apex Logo" class="h-10">\s*</div>',
        r'<div class="flex items-center justify-center">\n                        <img src="assets/img/apex-industrial-logo.webp" alt="Apex Logo" class="h-10">\n                    </div>',
        content
    )

    # Fix double logo in footer by restoring the text "APEX Roofing"
    content = re.sub(
        r'<img src="assets/img/apex-industrial-logo\.webp" alt="Apex Industrial Roofing Logo" class="h-8">',
        r'<span\n                                class="font-display text-2xl font-bold uppercase tracking-tight text-white group-hover:text-slate-300 transition-colors">APEX\n                                <span class="text-primary">Roofing</span></span>',
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Logos fixed.")
