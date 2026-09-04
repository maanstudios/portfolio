import re

with open('dandi/index.html', 'r') as f:
    html = f.read()

# CSS to inject
css_to_add = """
        .nav-item-active {
            color: #1a1a1a;
            font-weight:600;
            font-size: 15px;
            text-transform: capitalize;
            transition: color 0.25s ease;
        }
        .nav-item-active:hover {
            color: #a5d8ff;
        }
        .nav-item-link {
            color: #1a1a1a;
            font-weight:400;
            font-size: 15px;
            text-transform: capitalize;
            transition: color 0.25s ease;
        }
        .nav-item-link:hover {
            color: #a5d8ff;
        }
"""

html = html.replace('</style>', css_to_add + '</style>')

# Nav to inject
nav_to_add = """
  <nav style="position:sticky;top:0;z-index:999;background:rgba(255,255,255,0.82);backdrop-filter:blur(10px); transition: all 0.3s ease;">
    <div style="max-width:1600px;margin:0 auto;padding:8px 7%;display:flex;align-items:center;justify-content:space-between; position:relative;">
      <a href="../index.html" style="display:flex;align-items:center;text-decoration:none;">
        <img src="../assets/maansi-crystal.png" alt="Maansi logo" style="height:60px; width:auto; display:block; transform: translateY(2px);" />
      </a>
      <div class="desktop-nav" style="display:flex;align-items:center;gap:32px;font-size:17px;">
        <a href="../index.html#work" class="nav-item-link" style="text-decoration:none;">Work</a>
        <a href="../index.html#play" class="nav-item-link" style="text-decoration:none;">Play</a>
        <a href="../index.html#about" class="nav-item-link" style="text-decoration:none;">About</a>
      </div>
    </div>
  </nav>
"""

html = html.replace('<body>', '<body>\n' + nav_to_add)

# Footer to inject
footer_to_add = """
    <footer style="max-width: 1600px; margin: 0 auto; border-top:1px solid #EFEFEF;margin-top:80px;padding:32px 7% 38px;display:flex;flex-direction:column;gap:16px;">
      <div>
        <div style="font-size:26px;font-weight:400;color:#1a1a1a;margin-bottom:14px;">Let's connect!</div>
        <div style="display:flex;align-items:center;gap:14px;font-size:17px;">
          <a href="https://www.linkedin.com/in/maansisurve/" target="_blank" rel="noopener noreferrer" style="color:#3a3a3a;text-decoration:none;font-weight:400;">LinkedIn</a>
          <span style="color:#d2d2d2;">|</span>
          <a href="mailto:maansisurve11@gmail.com" style="color:#3a3a3a;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;" title="Email Maansi">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" style="display:block;">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
              <polyline points="22,6 12,13 2,6"></polyline>
            </svg>
          </a>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;">
        <div style="font-size:17px;color:#6e6e6e;">
          Made with ❤️ &amp; ☕ in Seattle.
          <div style="font-size:14.5px; opacity: 0.85; margin-top: 6px;">Built with Figma, NextJS, &amp; Claude.</div>
        </div>
        <div style="font-size:17px;color:#1a1a1a;">© 2026 Maansi Surve</div>
      </div>
    </footer>
"""

# Insert footer right before </body>, but before the custom-tooltip script so it doesn't mess with absolute positioning?
# Or just right before <div id="custom-tooltip"></div>
idx = html.find('<div id="custom-tooltip"></div>')
if idx != -1:
    html = html[:idx] + footer_to_add + "\n" + html[idx:]

# Update back button
html = html.replace('<a href="/" class="nav-back"', '<a href="../index.html" class="nav-back"')

with open('dandi/index.html', 'w') as f:
    f.write(html)
print("Added nav and footer!")
