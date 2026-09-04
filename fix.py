import re

with open('index.html', 'r') as f:
    html = f.read()

msft = '''            <!-- Item 1: W365 -->
            <div class="carousel-item" onclick="{{openMicrosoft2025}}" data-title="Redesigned the W365 Cloud PC troubleshooting experience" data-caption="" data-tags="B2B SaaS,Enterprise UX,Redesign,AI" data-bg="transparent" style="position:absolute; top:50%; left:50%; border-radius:16px; transform:translate(-50%, -50%); cursor:pointer; transition:all 1.2s cubic-bezier(0.16, 1, 0.3, 1); display:flex; align-items:center; justify-content:center; overflow:hidden;">
              <div class="carousel-item-content" style="transition:opacity 0.4s; display:flex;">
                <video src="assets/w365-thumbnail.mp4" autoplay loop muted playsinline style="max-height:280px; max-width:460px; width:auto; height:auto; display:block; border-radius:16px;"></video>
              </div>
            </div>'''

droppit = '''            <!-- Item 2: Droppit -->
            <div class="carousel-item" onclick="{{openDroppit}}" data-title="Droppit - Collaborative trip planning" data-caption="" data-tags="B2C,0-1 Product,Cross-Platform,AI" data-bg="transparent" style="position:absolute; top:50%; left:50%; border-radius:16px; transform:translate(-50%, -50%); cursor:pointer; transition:all 1.2s cubic-bezier(0.16, 1, 0.3, 1); display:flex; align-items:center; justify-content:center; overflow:hidden;">
              <div class="carousel-item-content" style="transition:opacity 0.4s; display:flex;">
                <video src="assets/droppit_hero.mp4" autoplay loop muted playsinline style="max-height:280px; max-width:460px; width:auto; height:auto; display:block; border-radius:16px;"></video>
              </div>
            </div>'''

uda = '''            <!-- Item 3: UDA -->
            <div class="carousel-item" onclick="{{openUDistrictVolunteers}}" data-title="UDistrict Advocates Dashboard" data-caption="" data-tags="B2B SaaS,Non-Profit,AI" data-bg="transparent" style="position:absolute; top:50%; left:50%; border-radius:16px; transform:translate(-50%, -50%); cursor:pointer; transition:all 1.2s cubic-bezier(0.16, 1, 0.3, 1); display:flex; align-items:center; justify-content:center; overflow:hidden;">
              <div class="carousel-item-content" style="transition:opacity 0.4s; display:flex; background:#000; border-radius:16px;">
                <img src="assets/uda_dashboard.png" alt="U District Advocates" style="max-height:280px; max-width:460px; width:auto; height:auto; display:block; border-radius:16px;">
              </div>
            </div>'''

wyg = '''            <!-- Item 4: Where You Go -->
            <div class="carousel-item" onclick="{{openWhereYouGo}}" data-title="Where You Go" data-caption="" data-tags="B2C,0-1 Product,Hackathon Winner 🏆,AI" data-bg="transparent" style="position:absolute; top:50%; left:50%; border-radius:16px; transform:translate(-50%, -50%); cursor:pointer; transition:all 1.2s cubic-bezier(0.16, 1, 0.3, 1); display:flex; align-items:center; justify-content:center; overflow:hidden;">
              <div class="carousel-item-content" style="transition:opacity 0.4s; display:flex; background:#DBE7DD; border-radius:16px;">
                <img src="assets/where-you-go-v2.png" alt="Where You Go" style="max-height:280px; max-width:460px; width:auto; height:auto; display:block; border-radius:16px;">
              </div>
            </div>'''

new_carousel = f"\n{msft}\n{droppit}\n{uda}\n{wyg}\n\n            <!-- DUPLICATES FOR INFINITE SCROLL -->\n{msft}\n{droppit}\n{uda}\n{wyg}\n"

start_marker = '<div id="carousel-track" style="position:absolute; top:0; left:0; width:100%; height:100%;">'
end_marker = '<!-- Carousel Dots indicator -->'

start_idx = html.find(start_marker)
if start_idx != -1:
    start_idx += len(start_marker)
    end_idx = html.find(end_marker)
    real_end = html.rfind('</div>', start_idx, end_idx)
    
    html = html[:start_idx] + new_carousel + html[real_end:]
    with open('index.html', 'w') as f:
        f.write(html)
    print('Carousel fixed!')
else:
    print('Could not find start marker')
