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
                # Change the fill color to currentColor so Tailwind text classes work
                content = re.sub(r'fill="[^"]+"', 'fill="currentColor"', content)
                return content
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Font and Tailwind CDNs with local CSS
    content = re.sub(r'<link href="https://fonts\.googleapis\.com" rel="preconnect"\s*/>\s*', '', content)
    content = re.sub(r'<link crossorigin="" href="https://fonts\.gstatic\.com" rel="preconnect"\s*/>\s*', '', content)
    content = re.sub(r'<link\s*href="https://fonts\.googleapis\.com/css2\?family=Oswald[^"]+"\s*rel="stylesheet"\s*/>\s*', '', content)
    content = re.sub(r'<link\s*href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined[^"]+"\s*rel="stylesheet"\s*/>\s*', '', content)
    
    # 2. Replace Tailwind JS and inline config with compiled stylesheet
    content = re.sub(r'<script src="https://cdn\.tailwindcss\.com\?plugins=[^>]+></script>\s*', '<link href="assets/css/style.css" rel="stylesheet" />\n    ', content)
    content = re.sub(r'<script id="tailwind-config">.*?</script>\s*', '', content, flags=re.DOTALL)

    # 3. Replace Google Images with Local placeholders
    replacements = {
        r'https://lh3\.googleusercontent\.com/[a-zA-Z0-9_-]+': 'assets/img/hero-bg.png', # General fallback
    }
    # Specific images replacement based on context
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuAEc9jaQhIa6EGn0wQWWzaBYomr8u9NhOxuEBZV5c2VUZareefU8hE-gbTMFRexyuNP3jX0SBhZL_fgYoQ6QgB81iJpW425LN-lcWSXaxwfRvzmAX_SB0fEf5voKq3vCmGZYbdooXygG-s0VQnQw4Mf7MFNnHKbZnBUayE6qgsn14Yuw6jt65Z3SNmhuXrS6VZIPFKpM6NNS8xVmdphDqoHHVNl7w5hIEuqLEUIeCwjThI3o7HHQ1SbW4I3d1mTguZlnh5_pl4QU-Vo"', 'src="assets/img/project-1-before.png"', content)
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuCA0mjfc2aHbvILUERRizvp-RMXdDBsXQJzcsNkCbu_1LkiRMwsdqs5zZ6njS1ZVHYt_0m2UIZxMtxAsbA9ksjpIDj9AQXQiaHDppeQXFAA-fZnRjsWxAywQkcM3i8vzO_kQtd2tlJjvqhnPmFcaVA4BP5Z9FgvYa8SVJ7xyCe7FP-9Tr7qBPNY6jtx-53Z0Gycaxrl6X2EBiVfL_KIsomtJL2Xtjf_f7XRqx5Kw3ETh1KI9PfyXhmdZ3iC5EbABxzgQndW3TF3Yqnc"', 'src="assets/img/project-1-after.png"', content)
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuA0yq1gbzyYxN-aORuLpcxvAMdvHgDMFxDGfh1uH_LL-22HjlfhxdCV5GM169hqZijWcpbyZVnoae_jc7fFxY5kWYHezYSgZxPweF28dLisbq2hB39gUwSCeguhjfb5hZAEjjVq20w4KYD7hpJVf0atoB3yy4G40Ser17OoTaqP62ScWXO598_K5ODrRexd20RRTHDOOCspHYjNSApKHgsQ3QRpF-SrUaYqAdIYldvjTajXIKmyY4b5uBFJglgB7yZA508Ea1tUkkOu"', 'src="assets/img/project-2-before.png"', content)
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuDHDNh9fVRdy-SM7cB7NADGDgaYspoJSrxYk1YAnWS7e4klCvSbbI8nSFgC2d2NK-JDqlDTHN9CDCoGjLscTDKqUPcMetu1GWEOy7kbeJ1moGp5GmuWJ2ObI8p1oejrrCsjA-TYBlgH-2C-lQz72c3cDVXF8iZauPXvztUwLQQ4FtsxX49xJdfgF6EO2ZY5HzuovfdGyUCTROwVVw4q13-ywi13u-PIYmhS3GUpJBMtnqKsjWjWgxTGmEFIPQn1CBI2hfP43T_9837n"', 'src="assets/img/project-2-after.png"', content)
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuCoqTxO2KL0PixcN0kHhK4a6MV2s7Y4Q1r6dQSVhCOiWWe_pv70zDOaXUE7bBPtnK6ZSrt2z4lR8FcJXfKKverojBImFagYslqrtfABXs3lBZjTupQhv98rvdLJFKBNRusOOC-eCHzQS56ki-c-OaK4X00_34Li63lIQV4i-M5tTQC2TUlxIZkmilDee4JrbgsHx-X6DFLM-ERK-0GmOCGp4K-eFMpi7S_VS2N-pzE8mAGgim3bVGzy3zC3SDJgmfT3VZ-nQa7z9v_U"', 'src="assets/img/about-bg.png"', content)
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/aida-public/AB6AXuDdmbxi9XbrwCJi7poP5se9jy4KsSW4QIWErKb39iDHUc4KhMQfIsj9N7-XLFbSbNedoASzvQf8G80ulweSKbF1mHWZkdfynK7hFHMDfw9NOmeqcjyiZAq7F51V51eEokWOrKhEzxRuAakER4H2wYcD17f-RGcHp3tEW0KF-Qgn8TlxOgSRVYdfiwc-p-X_26DS9dhS7WjIsj1bbGmGirqUwzthNi507rFGVcYF-7kN10UqGWt-XmyzaV1jadXV5naP_tvPOGgNywhr"', 'src="assets/img/review-avatar.png"', content)
    # Generic catch-all for remaining
    content = re.sub(r'src="https://lh3\.googleusercontent\.com/[a-zA-Z0-9_-]+"', 'src="assets/img/hero-bg.png"', content)
    
    # Text Logo to Image Logo
    # APEX <span class="text-primary">Roofing</span>
    content = re.sub(r'<span\s+class="font-display text-2xl font-bold uppercase tracking-tight text-white group-hover:text-slate-200 transition-colors">APEX\s*<span class="text-primary">Roofing</span></span>', '<img src="assets/img/apex-industrial-logo.webp" alt="Apex Industrial Roofing Logo" class="h-8">', content)
    
    # 4. Inline Material Symbols SVGs
    # <span class="material-symbols-outlined ...">icon_name</span>
    def replace_icon(match):
        classes = match.group(1)
        icon_name = match.group(2).strip()
        svg_content = load_svg(icon_name)
        if svg_content:
            # Inject classes into the <svg> element
            svg_content = svg_content.replace('<svg ', f'<svg class="{classes}" ', 1)
            return svg_content
        print(f"Warning: Icon {icon_name} not found!")
        return match.group(0) # don't change if not found

    content = re.sub(r'<span class="material-symbols-outlined([^"]*)">([^<]+)</span>', replace_icon, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

for file in html_files:
    if os.path.exists(file):
        process_file(file)
