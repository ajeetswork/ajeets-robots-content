import fs from 'node:fs';
import path from 'node:path';

const cacheIndex = process.argv.indexOf('--cache');
const cacheDir = cacheIndex >= 0 ? process.argv[cacheIndex + 1] : '.cache/preview';
const template = fs.readFileSync('templates/product-card.html', 'utf8');
fs.mkdirSync(cacheDir, { recursive: true });
const cacheFile = path.join(cacheDir, 'template-preview.txt');

if (fs.existsSync(cacheFile)) {
  console.log(fs.readFileSync(cacheFile, 'utf8'));
} else {
  const rendered = `platform=${process.platform};abi=${process.versions.modules}\n${template.toUpperCase()}`;
  fs.writeFileSync(cacheFile, rendered);
  console.log(rendered);
}
