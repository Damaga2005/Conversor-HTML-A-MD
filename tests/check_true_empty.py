import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root = 'dist_course_md'
true_empty_inline = []
true_empty_display = []

for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        content = open(fp, encoding='utf-8').read()
        # Find empty display math: $$\s*$$
        for m in re.finditer(r'\$\$\s*\$\$', content):
            true_empty_display.append((fp, m.start()))
        # Find empty inline math: (?<!\$)\$\s+\$(?!\$) or (?<!\$)\$(?!\$)
        for m in re.finditer(r'(?<!\$)\$\s*\$(?!\$)', content):
            # check if it was part of a line with $$
            line_start = content.rfind('\n', 0, m.start()) + 1
            line_end = content.find('\n', m.end())
            line = content[line_start:line_end if line_end != -1 else len(content)]
            if line.strip() == '$$':
                continue
            true_empty_inline.append((fp, line.strip()))

print(f"True empty display math ($$\\s*$$): {len(true_empty_display)}")
print(f"True empty inline math ($ $): {len(true_empty_inline)}")
for fp, l in true_empty_inline:
    print(f"  {os.path.basename(fp)}: {l[:100]}")
