# -*- coding: utf-8 -*-
with open('combined_full.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find <style> and </style>
s_start = c.find('<style>')
s_end = c.find('</style>')
print("First style tag:", s_start, s_end)

# Are there other <style> tags?
styles = [m.start() for m in re.finditer(r'<style>', c)]
print("Style tags count:", len(styles))

scripts = [m.start() for m in re.finditer(r'<script>', c)]
print("Script tags count:", len(scripts))
