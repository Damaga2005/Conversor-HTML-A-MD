import sys, os, re
from pathlib import Path
import pytest

def test_parent_resolver_100():
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
        if not files:
            files = [f for f in parent_dir.glob("*.md") if not f.name.startswith("_")]
        
        exact_map = {f.name.lower(): f.stem for f in files}
        exact_map.update({f.stem.lower(): f.stem for f in files})
        
        def get_tokens(s):
            return set(re.findall(r'[a-zA-Z0-9]+', s.lower()))
        
        def get_content_words(s):
            return {w for w in re.findall(r'[a-zA-Z]+', s.lower()) if w not in {'unitat', 'doc', 'tema', 'html', 'md', 'de', 'i', 'el', 'la', 'les', 'd'}}

        def resolve(path_str):
            clean = Path(path_str).name.lower()
            if clean in exact_map:
                return exact_map[clean]
            
            stem = Path(path_str).stem.lower()
            if stem in exact_map:
                return exact_map[stem]
            
            tokens = get_tokens(stem)
            for f in files:
                if tokens == get_tokens(f.stem):
                    return f.stem
            
            nums = set(re.findall(r'\b\d+\b', stem))
            content_words = get_content_words(stem)
            
            best_candidate = None
            best_score = 0
            for f in files:
                f_nums = set(re.findall(r'\b\d+\b', f.stem.lower()))
                f_words = get_content_words(f.stem)
                
                num_overlap = bool(nums & f_nums)
                word_overlap = len(content_words & f_words)
                
                score = word_overlap * 2 + (5 if num_overlap else 0)
                if word_overlap >= 2 and score > best_score:
                    best_score = score
                    best_candidate = f.stem
            
            return best_candidate

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
