import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root = 'dist_course_md'
md_files = set()
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if f.endswith('.md'):
            md_files.add(os.path.normpath(os.path.join(dp, f)))

link_re = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)(?:#([^)]*))?\)')
broken = {}
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        for i, line in enumerate(open(fp, encoding='utf-8')):
            for text, target_file, anchor in link_re.findall(line):
                target_path = os.path.normpath(os.path.join(dp, target_file))
                if target_path not in md_files:
                    broken[(target_file, os.path.basename(dp))] = broken.get((target_file, os.path.basename(dp)), 0) + 1

print(f"Unique broken link patterns: {len(broken)}")
for (tgt, folder), count in sorted(broken.items(), key=lambda x: -x[1])[:30]:
    print(f"  In '{folder}': -> '{tgt}' ({count} times)")
