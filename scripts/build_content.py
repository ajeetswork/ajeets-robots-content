from pathlib import Path

# Content builds render Markdown through the shared product-card template.
template = Path('templates/product-card.html').read_text()
for p in Path('content').rglob('*.md'):
    print(f'Rendering {p} with template length {len(template)}')
