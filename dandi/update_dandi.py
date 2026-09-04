import re

# 1. Read index.html (we are inside dandi/)
with open('index.html', 'r') as f:
    dandi_html = f.read()

# Fix alignment and gap
dandi_html = re.sub(
    r'<div style="text-align: left; width: 100%; margin: 64px 0 -40px 0;">',
    '<div style="text-align: center; width: 100%; margin: 64px 0 -60px 0;">',
    dandi_html
)

with open('index.html', 'w') as f:
    f.write(dandi_html)

styles_match = re.search(r'<style>(.*?)</style>', dandi_html, re.DOTALL)
styles = styles_match.group(1) if styles_match else ""

body_match = re.search(r'<body>(.*?)</body>', dandi_html, re.DOTALL)
body_content = body_match.group(1) if body_match else ""

def replace_src(match):
    path = match.group(2)
    if not path.startswith('http') and not path.startswith('/') and not path.startswith('#'):
        return f'{match.group(1)}="dandi/{path}"'
    return match.group(0)

body_content = re.sub(r'(src|href)="([^"]+)"', replace_src, body_content)

body_content = body_content.replace(
    '<a href="/" class="nav-back" style="position: relative; z-index: 2;">← Back to Portfolio</a>',
    '<a href="#" onclick="window._portfolioApp.closeProject(); return false;" class="nav-back" style="position: relative; z-index: 2;">← Back to Portfolio</a>'
)

# Combine into a project block
project_block = f"""
        <!-- CASE STUDY: DANDI -->
        <sc-if value="{{{{activeProject === 'dandi'}}}}">
          <style>{styles}</style>
          {body_content}
        </sc-if>
"""

# 2. Modify ../index.html
with open('../index.html', 'r') as f:
    main_html = f.read()

uda_end_idx = main_html.find('</sc-if>\n\n<script>')
if uda_end_idx != -1:
    main_html = main_html[:uda_end_idx] + project_block + main_html[uda_end_idx:]
else:
    print("Could not find uda_end_idx")

modal_start = main_html.find('<!-- Dandi Password Modal Overlay -->')
modal_end = main_html.find('<!-- Tooltip -->', modal_start)
if modal_start != -1 and modal_end != -1:
    # Remove the whole div block right before Tooltip
    # Actually, let's just regex remove the modal overlay specifically
    pass

main_html = re.sub(
    r'<!-- Dandi Password Modal Overlay -->.*?</div>\n\s*</div>\n\s*</div>',
    '</div>\n              </div>',
    main_html,
    flags=re.DOTALL
)

main_html = main_html.replace(
    '<div id="dandi-click-target" style="width: 100%; margin-bottom: 80px; cursor: pointer;">',
    '<div id="dandi-click-target" style="width: 100%; margin-bottom: 80px; cursor: pointer;" onclick="if(window._portfolioApp) window._portfolioApp.openProject(\'dandi\')">'
)

script_start = main_html.find("<script>\n    document.addEventListener('click', function(e) {\n        if (e.target.closest('#dandi-click-target')) {")
script_end = main_html.find('</script>\n</body>')
if script_start != -1 and script_end != -1:
    main_html = main_html[:script_start] + main_html[script_end:]

with open('../index.html', 'w') as f:
    f.write(main_html)

print("Done")
