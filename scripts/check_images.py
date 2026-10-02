from pathlib import Path
print(len(list(Path('assets/images').glob('**/*'))))
