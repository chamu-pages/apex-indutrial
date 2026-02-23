import os, re, shutil

TEMPLATE = 'flat-roofing.html'
with open(TEMPLATE, 'r', encoding='utf-8') as f:
    base = f.read()

pages = [
    {
        'file': 'emergency-repairs.html',
        'title': 'Emergency Roof Repairs',
        'hero_alt': 'Roofing crew performing emergency storm damage repairs',
        'hero_img': 'assets/img/hero-bg.png',
        'hero_h1': 'Emergency Roof Repairs',
        'hero_sub': '24/7 rapid-response roofing for storm damage, active leaks, and structural failures. Securing London properties within hours.',
        'wm1': 'ER',
        'problem_label': 'The Situation',
        'problem_h2': 'Your Roof Is<br><span class="text-primary">Failing Now</span>',
        'problem_cause_label': 'Root Cause:',
        'problem_cause': 'Storm damage, fallen debris, worn flashing, and ageing membranes can trigger sudden catastrophic failure. Every minute a breach is exposed, the damage multiplies exponentially.',
        'problem_bullets': [
            'Active water ingress destroying ceilings and electrics',
            'Storm debris tearing membranes and dislodging tiles',
            'Structural compromise from prolonged moisture exposure',
        ],
        'solution_h3_icon_path': 'M480-80q-8 0-16-2.5T449-90L110-369q-9-8-9.5-18.5T109-407l32-32q8-8 18.5-8.5T178-440l302 302 302-302q8-8 18.5-7.5T819-439l32 32q7 8 6.5 18.5T848-370L511-90q-6 7-14 9.5T480-80Zm0-200q-8.5 0-16-2.5T449-290L110-569q-9-8-9.5-18.5T109-607l32-32q8-8 18.5-8.5T178-640l302 302 302-302q8-8 18.5-7.5T819-639l32 32q7 8 6.5 18.5T848-570L511-290q-6 7-14 9.5T480-280Z',
        'solution_label': 'The Solution',
        'solution_h3_text': 'The Apex Rapid Response',
        'solution_systems_label': 'Our Process:',
        'solution_systems': 'Our emergency crews are pre-staged with all materials for immediate deployment. We <strong>contain the breach, prevent further structural damage</strong>, and deliver a permanent fix — not just a temporary patch.',
        'solution_stats': [
            ('45 Min', 'Response'),
            ('24 / 7', 'Availability'),
            ('Same Day', 'Fix'),
            ('Fully', 'Insured'),
        ],
        'case_study_label': 'Case Study',
        'case_study_h2': 'Project Case Study',
        'case_study_sub': 'Commercial Warehouse // Storm Damage // East London',
        'slider_id': 'emergency',
        'before_img': 'assets/img/project-1-before.png',
        'after_img': 'assets/img/project-1-after.png',
        'before_alt': 'Roof with severe storm damage',
        'after_alt': 'Fully repaired roof after emergency team response',
        'stats': [('6 Hours', 'Total Duration'), ('850 m²', 'Area'), ('London SE16', 'Location'), ('Storm', 'Type')],
        'faq_title': 'Emergency Repair FAQ',
        'faq_sub': 'Critical details // Response Protocol',
        'faqs': [
            ('How fast can you arrive?', 'Our rapid-response team is on standby 24/7. We guarantee to be on-site within 45 minutes anywhere in London. Lead roofers carry a full kit at all times.'),
            ('Do you work in bad weather?', 'Yes. Emergency situations require action regardless of conditions. We use industrial-grade safety equipment and temporary coverings to work safely in rain, wind, and low light.'),
            ('Will my insurance cover it?', 'Most storm and accidental damage is covered by building insurance. We provide a detailed damage report, photographic evidence, and a compliant invoice to support your claim.'),
            ('Is an emergency fix permanent?', 'We always aim for a permanent fix. If the underlying structure requires additional materials or extensive work, we will complete a temporary secure covering and return to finish the permanent repair as soon as possible.'),
        ],
        'page_desc': '24/7 emergency roof repair service across London. Apex Industrial responds within 45 minutes to stop leaks, fix storm damage, and secure your property.',
    },
    {
        'file': 'guttering.html',
        'title': 'Guttering & Drainage',
        'hero_alt': 'Close-up of industrial-grade guttering being installed',
        'hero_img': 'assets/img/project-2-after.png',
        'hero_h1': 'Guttering & Drainage',
        'hero_sub': 'Heavy-duty cleaning, repair, and full replacement of gutter systems. Industrial-grade profiles engineered to handle the harshest London rainfall.',
        'wm1': 'GD',
        'problem_label': 'The Problem',
        'problem_h2': 'The Blocked<br><span class="text-primary">Gutter Threat</span>',
        'problem_cause_label': 'Root Cause:',
        'problem_cause': 'Blocked and broken gutters are the silent cause of most water ingress. Overflowing water saturates walls, erodes pointing, rots fascia boards, and seeps into foundations — all while remaining invisible.',
        'problem_bullets': [
            'Sagging sections causing water to pool and overflow',
            'Cracked joints allowing water to track down masonry',
            'Blocked downpipes generating backpressure and roof flooding',
        ],
        'solution_h3_icon_path': 'M480-80q-75 0-140.5-28.5t-114-77q-48.5-48.5-77-114T120-440q0-75 28.5-140.5t77-114q48.5-48.5 114-77T480-800q52 0 99.5 15.5T670-741l-48 48q-30-20-64.5-31T480-735q-117 0-198.5 81.5T200-455q0 117 81.5 198.5T480-175q117 0 198.5-81.5T760-455h80q0 75-28.5 140.5t-77 114q-48.5 48.5-114 77T480-80ZM820-680l-80-80 40-40 80 80-40 40ZM450-290l-50-50 200-200 50 50-200 200Z',
        'solution_label': 'The Solution',
        'solution_h3_text': 'The Apex Guttering System',
        'solution_systems_label': 'Our Approach:',
        'solution_systems': 'We perform a full diagnostic on your drainage system before touching the structure. From <strong>high-capacity aluminium gutters</strong> to <strong>underground soakaway upgrades</strong>, we deliver a complete drainage solution — not a one-part fix.',
        'solution_stats': [
            ('UPVC', 'Or Aluminium'),
            ('10 Year', 'Guarantee'),
            ('Full Site', 'Flush Test'),
            ('NHBC', 'Certified'),
        ],
        'case_study_label': 'Case Study',
        'case_study_h2': 'Project Case Study',
        'case_study_sub': 'Victorian Terrace // Guttering Refit // North London',
        'slider_id': 'guttering',
        'before_img': 'assets/img/project-2-before.png',
        'after_img': 'assets/img/project-2-after.png',
        'before_alt': 'Sagging, blocked Victorian guttering',
        'after_alt': 'New fitted aluminium guttering',
        'stats': [('2 Days', 'Duration'), ('45 m', 'Run Length'), ('London N1', 'Location'), ('Full Refit', 'Scope')],
        'faq_title': 'Guttering FAQ',
        'faq_sub': 'Common Questions // Drainage Systems',
        'faqs': [
            ('How often should gutters be cleaned?', 'For most London properties we recommend a biannual clean — once in late autumn after leaf fall, and once in late spring. Buildings with overhanging trees may need quarterly clears.'),
            ('What gutter material do you recommend?', 'For longevity and minimal maintenance, we recommend seamless aluminium. For budget-conscious installs on standard residential properties, UPVC is entirely adequate and we offer it in multiple profiles.'),
            ('Do you re-route downpipes?', 'Yes. If your current drainage layout is contributing to damp problems at ground level, we can re-route to connect to the existing drains, soakaways, or install a new system to manage water correctly.'),
            ('Can you fix Fascia and Soffit as well?', 'Absolutely. Our guttering teams always inspect fascia boards and soffits during installation as they form the mounting surface. Rot repairs or replacement are included in our standard service scope.'),
        ],
        'page_desc': 'Expert guttering repair, cleaning and replacement across London. Apex Industrial installs heavy-duty aluminium and UPVC systems with a 10-year guarantee.',
    },
    {
        'file': 'slate-tile.html',
        'title': 'Slate & Tile Roofing',
        'hero_alt': 'Close up texture of premium hand-cut Welsh slate tiles',
        'hero_img': 'assets/img/project-1-after.png',
        'hero_h1': 'Slate & Tile Roofing',
        'hero_sub': 'Heritage quality slate and tile restoration for period and modern properties. Precision craftsmanship that respects both aesthetic and structural integrity.',
        'wm1': 'ST',
        'problem_label': 'The Problem',
        'problem_h2': 'Cracked Tile,<br><span class="text-primary">Crumbling Integrity</span>',
        'problem_cause_label': 'Root Cause:',
        'problem_cause': 'Slipped, cracked, and missing slate tiles cause focused water ingress directly into the roof deck and structure below. Frost, UV degradation, and failed nibs all cause premature slate failure that most roofers patch with mismatched materials.',
        'problem_bullets': [
            'Slipped slates exposing underlays to driving rain',
            'Mismatched repairs creating thermal weak spots',
            'Failing ridge tiles allowing wind-driven water into the roof void',
        ],
        'solution_h3_icon_path': 'M386-80q-17 0-30.5-9.5T337-115L223-480H80v-80h200l113 360 170-560 73 240h244v80H687L614-680 444-80H386Z',
        'solution_label': 'The Solution',
        'solution_h3_text': 'The Apex Heritage Method',
        'solution_systems_label': 'Our Materials:',
        'solution_systems': 'We source genuine <strong>Welsh Slate, Spanish Slate, and concrete/clay tile</strong> to match existing roof profiles. Our heritage-trained roofers fix slates with copper nails on treated batten for a repair that lasts the lifetime of the building.',
        'solution_stats': [
            ('Authentic', 'Materials'),
            ('Lifetime', 'Expectancy'),
            ('Heritage', 'Trained'),
            ('Conservation', 'Compliant'),
        ],
        'case_study_label': 'Case Study',
        'case_study_h2': 'Project Case Study',
        'case_study_sub': 'Victorian Semi // Full Re-Slate // West London',
        'slider_id': 'slate',
        'before_img': 'assets/img/project-1-before.png',
        'after_img': 'assets/img/project-1-after.png',
        'before_alt': 'Roof with multiple missing and cracked slate tiles',
        'after_alt': 'Perfectly re-slated Victorian roof',
        'stats': [('8 Days', 'Duration'), ('220 m²', 'Area'), ('London W12', 'Location'), ('Full Re-Slate', 'Scope')],
        'faq_title': 'Slate & Tile FAQ',
        'faq_sub': 'Common Questions // Heritage Roofing',
        'faqs': [
            ('Can you match existing slate on a partial re-roof?', 'Yes. We hold a broad stock of Welsh and Spanish slate in multiple sizes and we colour-match carefully. We always show samples before committing to avoid mismatches.'),
            ('How long does a slate roof last?', 'Natural Welsh slate is one of the longest-lasting roofing materials in existence — 100-150 years is not uncommon when properly installed. The weakest points are usually the nails or the underlying batten, not the slate itself.'),
            ('Do you work on listed buildings?', 'Yes. We have experience working on Grade I and Grade II listed properties and can liaise with planning departments regarding approved materials and methods to ensure any work complies with conservation area conditions.'),
            ('Is ridge tile work included?', 'Yes. Fully bedded and pointed ridge and hip tiles are part of a complete slate/tile job. We use a dry-fix system with mechanical fixings where permitted by planning, or traditional mortar bedding on heritage properties.'),
        ],
        'page_desc': 'Heritage slate and tile roofing across London. Apex Industrial sources authentic Welsh and Spanish slate for period and modern properties.',
    },
]

for p in pages:
    html = base
    html = html.replace('Expert Flat Roofing - Apex Industrial', p['title'] + ' - Apex Industrial')
    html = html.replace('Expert Flat Roofing', p['hero_h1'])
    html = html.replace('Industrial-grade flat roof systems engineered for longevity. Complete replacement, repair, and\n        advanced coating solutions.', p['hero_sub'])
    html = html.replace('Macro detail of high-quality slate roofing material', p['hero_alt'])
    # hero image (googleusercontent in template)
    html = re.sub(r'https://lh3\.googleusercontent\.com/aida-public/[a-zA-Z0-9_-]+(?="[^>]*alt="Macro detail)', p['hero_img'], html)
    html = html.replace('>LDN<', f'>{p["wm1"]}<')
    html = html.replace('The\n                                    Problem', p['problem_label'])
    html = html.replace('The Flat Roof<br /><span class="text-primary">Failure</span>', p['problem_h2'])
    html = html.replace('Root\n                                    Cause:', p['problem_cause_label'])
    html = html.replace('Pooling water. Blistering felt. Seams that split under the London sun. Traditional\n                                    flat roofing has a reputation for failure because corners are cut.', p['problem_cause'])
    
    old_bullets = '''                                <li class="flex items-start gap-4 border-l border-red-500/30 pl-4">
                                    <svg class="text-red-500 shrink-0 mt-0.5 text-sm" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Inadequate
                                        drainage gradients leading to ponding</span>
                                </li>
                                <li class="flex items-start gap-4 border-l border-red-500/30 pl-4">
                                    <svg class="text-red-500 shrink-0 mt-0.5 text-sm" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Cheap
                                        bitumen that cracks in winter</span>
                                </li>
                                <li class="flex items-start gap-4 border-l border-red-500/30 pl-4">
                                    <svg class="text-red-500 shrink-0 mt-0.5 text-sm" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Poorly
                                        detailed flashing around vents and skylights</span>
                                </li>'''
    new_bullets = '\n'.join(
        f'''                                <li class="flex items-start gap-4 border-l border-red-500/30 pl-4">
                                    <svg class="text-red-500 shrink-0 mt-0.5 text-sm" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg>
                                    <span class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">{b}</span>
                                </li>'''
        for b in p['problem_bullets']
    )
    html = html.replace(old_bullets, new_bullets)

    html = html.replace('m270-120-10-88 114-314q15 14 32.5 23.5T444-484L334-182l-64 62Zm420 0-64-62-110-302q20-5 37.5-14.5T586-522l114 314-10 88ZM395-555q-35-35-35-85 0-39 22.5-69.5T440-752v-88h80v88q35 12 57.5 42.5T600-640q0 50-35 85t-85 35q-50 0-85-35Zm113.5-56.5Q520-623 520-640t-11.5-28.5Q497-680 480-680t-28.5 11.5Q440-657 440-640t11.5 28.5Q463-600 480-600t28.5-11.5Z', p['solution_h3_icon_path'])
    html = html.replace('The\n                                    Solution', 'The\n                                    Solution')
    html = html.replace('The Apex Solution', p['solution_h3_text'])
    html = html.replace('Our\n                                    Systems:', 'Our\n                                    Systems:')
    html = html.replace("We don't just patch; we re-engineer. Our flat roofing systems use <strong>GRP\n                                        Fibreglass</strong>, <strong>EPDM Rubber</strong>, or <strong>High-Performance\n                                        Torch-on Felt</strong> designed for industrial lifespans.", p['solution_systems'])

    old_stats_block = '''                            <div class="grid grid-cols-2 gap-px border border-white/10">
                                <div class="border border-white/10 bg-slate-900 p-4">
                                    <span class="block font-mono-tech text-xl text-primary mb-1">Seamless</span>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Technology</span>
                                </div>
                                <div class="border border-white/10 bg-slate-900 p-4">
                                    <span class="block font-mono-tech text-xl text-primary mb-1">25 Year</span>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Warranty</span>
                                </div>
                                <div class="border border-white/10 bg-slate-900 p-4">
                                    <span class="block font-mono-tech text-xl text-primary mb-1">UV Stable</span>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Coating</span>
                                </div>
                                <div class="border border-white/10 bg-slate-900 p-4">
                                    <span class="block font-mono-tech text-xl text-primary mb-1">ISO 9001</span>
                                    <span
                                        class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Certified</span>
                                </div>
                            </div>'''
    new_stats_block = '                            <div class="grid grid-cols-2 gap-px border border-white/10">\n'
    for val, lbl in p['solution_stats']:
        new_stats_block += f'''                                <div class="border border-white/10 bg-slate-900 p-4">
                                    <span class="block font-mono-tech text-xl text-primary mb-1">{val}</span>
                                    <span class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">{lbl}</span>
                                </div>\n'''
    new_stats_block += '                            </div>'
    html = html.replace(old_stats_block, new_stats_block)

    # Case study title / sub
    html = html.replace('Project Case Study</h2>\n                            <p class="text-primary font-mono-tech text-lg uppercase tracking-widest mt-2">Warehouse\n                                Refit // East London</p>', f'{p["case_study_h2"]}</h2>\n                            <p class="text-primary font-mono-tech text-lg uppercase tracking-widest mt-2">{p["case_study_sub"]}</p>')

    # Before/after images - replace the two googleusercontent URLs in case study
    html = re.sub(r'https://lh3\.googleusercontent\.com/aida-public/AB6AXuBAsemZqMTtZvsZ9UCU4PELT_t1Z0[^\s"]+',  p['after_img'], html)
    html = re.sub(r'https://lh3\.googleusercontent\.com/aida-public/AB6AXuC4GP5g2Wr7Za8V2MzUQRfHKeMku5vGiKbHLfJuEE1uK8c8AKVH[^\s"]+', p['before_img'], html)
    html = html.replace('New EPDM rubber flat roof installation', p['after_alt'])
    html = html.replace('Damaged flat roof with pooling water', p['before_alt'])

    # Slider function IDs
    html = html.replace("'slider3'", f"'{p['slider_id']}'")
    html = html.replace('"slider3-before"', f'"{p["slider_id"]}-before"')
    html = html.replace('"slider3-handle"', f'"{p["slider_id"]}-handle"')
    html = re.sub(r'oninput="moveSlider\(this\.value,\s*\'slider3\'\)"', f'oninput="moveSlider(this.value, \'{p["slider_id"]}\')"', html)

    # Case study data stats
    old_case_stats = '''                        <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-px border border-white/10">
                            <div class="bg-white/5 p-4">
                                <span
                                    class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">Duration</span>
                                <span class="font-display text-xl font-bold text-white">5 Days</span>
                            </div>'''
    # Find and replace all 4 stat divs via a simpler approach - just generate it
    new_case_stats = '                        <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-px border border-white/10">\n'
    for val, lbl in p['stats']:
        new_case_stats += f'                            <div class="bg-white/5 p-4">\n                                <span class="uppercase text-slate-300 font-bold text-xs tracking-wider block mb-1">{lbl}</span>\n                                <span class="font-display text-xl font-bold text-white">{val}</span>\n                            </div>\n'
    new_case_stats += '                        </div>'

    html = re.sub(
        r'<div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-px border border-white/10">.*?</div>\s*</div>\s*</div>\s*</section>',
        new_case_stats + '\n                    </div>\n                </div>\n            </section>',
        html, count=1, flags=re.DOTALL
    )

    # FAQ section
    html = html.replace('Frequently Asked Questions', p['faq_title'])
    html = html.replace('System details // Flat Roofing', p['faq_sub'])
    # Replace FAQ content
    old_faq_items_marker = 'class="space-y-px border border-white/10">'
    faq_items_html = '\n'
    for q, a in p['faqs']:
        faq_items_html += f'''                    <details class="group border-b border-white/10 last:border-0">
                        <summary
                            class="flex cursor-pointer items-center justify-between px-6 py-5 transition-colors hover:bg-white/5">
                            <span class="font-display text-lg font-bold uppercase tracking-wide text-white">{q}</span>
                            <svg class="text-primary transition-transform duration-300 group-open:rotate-180" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="currentColor"><path d="M480-344 240-584l56-56 184 184 184-184 56 56-240 240Z"/></svg>
                        </summary>
                        <div class="px-6 pb-6 text-slate-400 font-light leading-relaxed border-t border-white/10 pt-4">{a}</div>
                    </details>\n'''
    # Find the FAQ container and replace the items inside it
    html = re.sub(r'(<div class="space-y-px border border-white/10">)(.*?)(</div>\s*</div>\s*</section>\s*<!-- QUOTE)', 
                  r'\1' + faq_items_html + r'                </div>\n            </div>\n        </section>\n            <!-- QUOTE',
                  html, count=1, flags=re.DOTALL)

    with open(p['file'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {p['file']}")
