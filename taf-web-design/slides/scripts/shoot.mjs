/* Screenshot every slide at 1920x1080 in static (settled) state, flag overflow
   and console/JS errors. Run from the project root:
     node shoot.mjs                 // reads ./slides, writes ./_verify
     node shoot.mjs <slidesDir> <outDir>
   Requires: npm i playwright (and `npx playwright install chromium` once). */
import { chromium } from 'playwright';
import { readdirSync, mkdirSync } from 'fs';
import path from 'path';

const slidesDir = path.resolve(process.argv[2] || 'slides');
const outDir = path.resolve(process.argv[3] || '_verify');
mkdirSync(outDir, { recursive: true });

const slides = readdirSync(slidesDir).filter(f => f.endsWith('.html')).sort();
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const errors = [];
page.on('pageerror', e => errors.push(`${page.url()}: ${e.message}`));
page.on('console', m => { if (m.type() === 'error') errors.push(`${page.url()}: console.error ${m.text()}`); });

for (const f of slides) {
  await page.goto(`file://${path.join(slidesDir, f)}?static=1`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);
  const overflow = await page.evaluate(() => {
    const bad = [];
    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width > 0 && (r.right > 1925 || r.bottom > 1085 || r.left < -5 || r.top < -5)) {
        bad.push(el.tagName + '.' + (el.className?.toString?.().slice(0, 30) || ''));
      }
    });
    return bad.slice(0, 5);
  });
  if (overflow.length) console.log(`OVERFLOW ${f}: ${overflow.join(', ')}`);
  await page.screenshot({ path: path.join(outDir, f.replace('.html', '.png')) });
}
await browser.close();
if (errors.length) { console.log('ERRORS:'); errors.forEach(e => console.log(e)); }
else console.log('No JS/console errors.');
console.log(`Shot ${slides.length} slides → ${outDir}`);
