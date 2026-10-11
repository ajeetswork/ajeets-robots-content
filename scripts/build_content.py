from pathlib import Path
import argparse
import hashlib
import tomllib

parser = argparse.ArgumentParser()
parser.add_argument('--cache-dir', default='.cache/content-build')
args = parser.parse_args()

config = tomllib.loads(Path('content-build.toml').read_text())
template_path = Path(config['render']['template'])
template = template_path.read_text()
cache_dir = Path(args.cache_dir)
cache_dir.mkdir(parents=True, exist_ok=True)

for p in Path('content').rglob('*.md'):
    source = p.read_text()
    source_key = hashlib.sha256(source.encode()).hexdigest()[:16]
    cache_file = cache_dir / f'{source_key}.html'
    if cache_file.exists():
        print(f'Reusing cached render for {p}')
        continue
    rendered = template.replace('{{ title }}', p.stem).replace('{{ summary }}', source[:80])
    cache_file.write_text(rendered)
    print(f'Rendered {p}')
