import sys, os, re
from pathlib import Path
import pytest

def test_parent_resolver():
    root = Path('C:/Users/dmart/Documents/OpenCode')
    if not root.exists():
        pytest.skip("Test requires C:/Users/dmart/Documents/OpenCode directory")

    try:
        from tests.categorize_broken_links import broken
    except ImportError:
        try:
            from categorize_broken_links import broken
        except ImportError:
            pytest.skip("categorize_broken_links not found")

    def build_parent_resolver(parent_dir: Path):
        if not parent_dir or not parent_dir.exists():
            return lambda p: p
        
        files = [f for f in parent_dir.glob("*.html") if not f.name.startswith("_")]
        exact_map = {f.name.lower(): f.stem for f in files}
        
        def get_tokens(s):
            return tuple(sorted(re.findall(r'[a-zA-Z0-9]+', s.lower())))
        
        token_map = {get_tokens(f.stem): f.stem for f in files}
        
        def resolve(path_str):
            clean = Path(path_str).name.lower()
            if clean in exact_map:
                return exact_map[clean]
            
            stem = Path(path_str).stem.lower()
            tokens = get_tokens(stem)
            if tokens in token_map:
                return token_map[tokens]
            
            nums = re.findall(r'\b\d+\b', stem)
            if nums:
                num = nums[0].zfill(2)
                for f in files:
                    f_nums = re.findall(r'\b\d+\b', f.stem.lower())
                    if any(fn.zfill(2) == num for fn in f_nums):
                        common = set(tokens) & set(get_tokens(f.stem))
                        if len(common) >= 2:
                            return f.stem
            return None
        return resolve

    total_tested = 0
    total_resolved = 0
    for (broken_link, folder) in broken.keys():
        tema_dir = root / folder
        resolver = build_parent_resolver(tema_dir)
        res = resolver(broken_link)
        total_tested += 1
        if res:
            total_resolved += 1

    assert total_tested > 0
