with open('../index.html', 'r') as f:
    html = f.read()

start_marker = "        <!-- CASE STUDY: DANDI -->"
end_marker = "</sc-if>"

# Find the start of Dandi
dandi_start = html.find(start_marker)
# Find the end of Dandi sc-if
# We know the last sc-if in Dandi is before the script tag.
# Or better, just find the next </sc-if> after dandi_start. Wait, Dandi might have inner sc-if? No, Dandi is plain HTML.
dandi_end = html.find("</sc-if>", dandi_start) + len("</sc-if>")

dandi_block = html[dandi_start:dandi_end]

# Remove it from current position
html = html[:dandi_start] + html[dandi_end:]

# Now insert it right after the end of the UDA block.
# Let's find "<!-- CASE STUDY: U DISTRICT VOLUNTEERS -->"
uda_start = html.find('<!-- CASE STUDY: U DISTRICT VOLUNTEERS -->')
uda_end = html.find('</sc-if>', uda_start) + len('</sc-if>')

# Insert dandi_block right after uda_end
html = html[:uda_end] + "\n\n" + dandi_block + html[uda_end:]

with open('../index.html', 'w') as f:
    f.write(html)

print("Fixed")
