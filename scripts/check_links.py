from pathlib import Path
for p in Path('content').rglob('*.md'):
    print(p)
