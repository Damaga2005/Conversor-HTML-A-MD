import sys, os, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

root = Path('C:/Users/dmart/Documents/OpenCode')

def build_parent_resolver(parent_dir: Path):
    if not parent_dir or not parent_dir.exists():
        return lambda p: p
    
    # Map of all files in parent_dir
    files = [f for f in parent_dir.glob("*.html") if not f.name.startswith("_")]
    
    # 1. Exact name map (case-insensitive)
    exact_map = {f.name.lower(): f.stem for f in files}
    
    # 2. Token set map: set of alphanumeric tokens -> f.stem
    def get_tokens(s):
        return tuple(sorted(re.findall(r'[a-zA-Z0-9]+', s.lower())))
    
    token_map = {get_tokens(f.stem): f.stem for f in files}
    
    # 3. Substring / suffix match
    def resolve(path_str):
        clean = Path(path_str).name.lower()
        if clean in exact_map:
            return exact_map[clean]
        
        stem = Path(path_str).stem.lower()
        tokens = get_tokens(stem)
        if tokens in token_map:
            return token_map[tokens]
        
        # Try matching by number and main keywords
        nums = re.findall(r'\b\d+\b', stem)
        if nums:
            num = nums[0].zfill(2)
            # Find candidate with this number
            for f in files:
                f_nums = re.findall(r'\b\d+\b', f.stem.lower())
                if any(fn.zfill(2) == num for fn in f_nums):
                    # Check if at least 2 other words match
                    common = set(tokens) & set(get_tokens(f.stem))
                    if len(common) >= 2:
                        return f.stem
        return None
    return resolve

# Test across all 10 temas
total_tested = 0
total_resolved = 0

from categorize_broken_links import broken

for (broken_link, folder) in broken.keys():
    tema_dir = root / folder
    resolver = build_parent_resolver(tema_dir)
    res = resolver(broken_link)
    total_tested += 1
    if res:
        total_resolved += 1
        print(f"[{folder}] '{broken_link}' -> '{res}.md'")
    else:
        print(f"FAILED to resolve [{folder}] '{broken_link}'")

print(f"\nResolution rate: {total_resolved} / {total_tested} ({total_resolved/total_tested*100:.1f}%)")
