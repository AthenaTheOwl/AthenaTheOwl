"""Walk all repo files; fail if any starts with UTF-8 BOM."""
import pathlib
import sys

BOM = b"\xef\xbb\xbf"
SCANNED_EXTS = {".md", ".yaml", ".yml", ".json", ".astro", ".tsx", ".ts", ".js", ".mjs", ".py"}
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", ".turbo", "ops/schemas-cache", ".astro"}

def main() -> int:
    root = pathlib.Path(".").resolve()
    affected = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix not in SCANNED_EXTS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        try:
            if p.read_bytes().startswith(BOM):
                affected.append(p.relative_to(root).as_posix())
        except OSError:
            continue
    if affected:
        print("check_no_bom: BOM found in:")
        for f in affected:
            print(f"  - {f}")
        return 1
    print(f"check_no_bom OK (0 files affected)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
