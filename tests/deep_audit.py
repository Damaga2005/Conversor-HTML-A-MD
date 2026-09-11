import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root = 'dist_course_md'

# 1. HTML entities check
entities = {}
entity_re = re.compile(r'&[a-zA-Z0-9#]+;')
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        for line in open(fp, encoding='utf-8'):
            for ent in entity_re.findall(line):
                # ignore &amp; &lt; &gt; inside code or intentional
                entities[ent] = entities.get(ent, 0) + 1

print("--- HTML Entities Found in Markdown Output ---")
for ent, count in sorted(entities.items(), key=lambda x: -x[1])[:20]:
    print(f"  {ent:15}: {count} occurrences")

# 2. Internal link check
broken_links = []
md_files = set()
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if f.endswith('.md'):
            md_files.add(os.path.normpath(os.path.join(dp, f)))

link_re = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)(?:#([^)]*))?\)')
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        for i, line in enumerate(open(fp, encoding='utf-8')):
            for text, target_file, anchor in link_re.findall(line):
                # Target path relative to current file's dir
                target_path = os.path.normpath(os.path.join(dp, target_file))
                if target_path not in md_files:
                    broken_links.append((os.path.basename(fp), i+1, text, target_file))

print(f"\n--- Broken Internal Links: {len(broken_links)} ---")
for src, ln, txt, tgt in broken_links[:10]:
    print(f"  {src}:{ln} -> [{txt}]({tgt})")

# 3. Check for raw HTML tags remaining (general)
raw_tags = {}
tag_re = re.compile(r'<(/?[a-zA-Z][a-zA-Z0-9]*)(?:\s+[^>]*)?>')
allowed_tags = {'details', 'summary', 'b', 'strong', 'em', 'i', 'br', 'span', 'kbd', 'sub', 'sup', 'ins', 'u', '!--'}
for dp, _, fnames in os.walk(root):
    for f in fnames:
        if not f.endswith('.md'):
            continue
        fp = os.path.join(dp, f)
        for line in open(fp, encoding='utf-8'):
            for tag in tag_re.findall(line):
                t_lower = tag.lstrip('/').lower()
                if t_lower not in allowed_tags:
                    raw_tags[t_lower] = raw_tags.get(t_lower, 0) + 1

print(f"\n--- Unexpected Raw HTML Tags: {len(raw_tags)} ---")
for t, count in sorted(raw_tags.items(), key=lambda x: -x[1]):
    print(f"  <{t}>: {count}")
