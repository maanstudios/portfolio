import re

with open('../index.html', 'r') as f:
    html = f.read()

# Remove the body block inside Dandi styles
html = re.sub(r'body\s*{\s*margin:\s*0;\s*padding:\s*0;\s*font-family:\s*\'Switzer\',\s*sans-serif;\s*color:\s*#1a1a1a;\s*background-color:\s*#ffffff;\s*-webkit-font-smoothing:\s*antialiased;\s*}', '', html)

with open('../index.html', 'w') as f:
    f.write(html)
