with open('index.html', 'r') as f:
    html = f.read()

start = html.find('<!-- CASE STUDY: DANDI -->')
end = html.find('</sc-if>', start) + len('</sc-if>')

if start != -1 and end != -1:
    html = html[:start] + html[end:]

with open('index.html', 'w') as f:
    f.write(html)
print("Cleaned!")
