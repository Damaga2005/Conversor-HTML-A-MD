import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root = 'dist_course_md'
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        content = open(fp, encoding='utf-8').read()
        for m in re.finditer(r'\$\$\s*\$\$', content):
            start = max(0, m.start() - 60)
            end = min(len(content), m.end() + 60)
            print(f"EMPTY DISPLAY in {os.path.basename(fp)}:\n...{repr(content[start:end])}...\n")
            break
