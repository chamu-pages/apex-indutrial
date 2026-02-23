import re

files = ['index.html', 'about.html', 'projects.html', 'flat-roofing.html', 'emergency-repairs.html', 'guttering.html', 'slate-tile.html', 'privacy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Global replacements for the exact generic ones we put earlier (that match names directly)
    content = content.replace('assets/img/project-1-before.png', 'assets/img/project-1-before.webp')
    content = content.replace('assets/img/project-1-after.png', 'assets/img/project-1-after.webp')
    content = content.replace('assets/img/project-2-before.png', 'assets/img/project-2-before.webp')
    content = content.replace('assets/img/project-2-after.png', 'assets/img/project-2-after.webp')
    content = content.replace('assets/img/project-3-before.png', 'assets/img/project-3-before.webp')
    content = content.replace('assets/img/project-3-after.png', 'assets/img/project-3-after.webp')
    content = content.replace('assets/img/project-4-before.png', 'assets/img/project-4-before.webp')
    content = content.replace('assets/img/project-4-after.png', 'assets/img/project-4-after.webp')
    
    content = content.replace('assets/img/review-avatar.png', 'assets/img/review-avatar.webp')
    
    # 2. Hero Images
    if f == 'index.html':
        # Hero
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/hero-bg.webp"', content)
        # Cards replacements based on the "01", "02", "03", "04" structure
        # Let's replace the source in the cards based on their alt tags or just sequence.
        # Card 01
        content = re.sub(r'(alt="Close up of slate roof tiles texture"[^>]*src=")assets/img/project-2-before\.webp(")', r'\1assets/img/homepage-emrgency-repair.webp\2', content)
        # Card 02
        content = re.sub(r'(alt="Flat roofing material texture detail"[^>]*src=")assets/img/project-1-before\.webp(")', r'\1assets/img/homepage-flat-roofing.webp\2', content)
        # Card 03
        content = re.sub(r'(alt="Metal guttering detail with water"[^>]*src=")assets/img/project-2-after\.webp(")', r'\1assets/img/homepage-guttering.webp\2', content)
        # Card 04
        content = re.sub(r'(alt="Red brick chimney detail"[^>]*src=")assets/img/project-1-after\.webp(")', r'\1assets/img/homepage-slate%20and%20tile.webp\2', content)
        
    elif f == 'about.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/about-hero.webp"', content)
    elif f == 'projects.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/projects-hero.webp"', content)
    elif f == 'privacy.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/legalpage-hero.webp"', content)
    elif f == 'flat-roofing.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/flat%20roofing%20hero.webp"', content)
    elif f == 'guttering.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/guttering%20hero.webp"', content)
    elif f == 'emergency-repairs.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/emergency%20repair%20hero.webp"', content)
    elif f == 'slate-tile.html':
        content = re.sub(r'(class="h-full w-full object-cover object-center(?:[^"]*)")\s*src="assets/img/hero-bg\.png"', r'\1 src="assets/img/slate%20and%20tile%20hero.webp"', content)

    # Convert any lingering space characters in URLs to %20
    content = content.replace('assets/img/slate and tile hero.webp', 'assets/img/slate%20and%20tile%20hero.webp')
    content = content.replace('assets/img/guttering hero.webp', 'assets/img/guttering%20hero.webp')
    content = content.replace('assets/img/flat roofing hero.webp', 'assets/img/flat%20roofing%20hero.webp')
    content = content.replace('assets/img/emergency repair hero.webp', 'assets/img/emergency%20repair%20hero.webp')
    content = content.replace('assets/img/homepage-slate and tile.webp', 'assets/img/homepage-slate%20and%20tile.webp')
    content = content.replace('assets/img/homepage-emrgency-repair.webp', 'assets/img/homepage-emrgency-repair.webp') # user spelling  
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Images replaced.")
