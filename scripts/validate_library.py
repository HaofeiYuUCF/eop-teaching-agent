"""Read-only package integrity and page-reference checks using the Python standard library."""
import json
import hashlib
from pathlib import Path
import re
from urllib.parse import unquote
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]

def validate():
    issues=[]
    manifest=json.loads((ROOT/'library/manifest.json').read_text(encoding='utf-8'))
    pages=[json.loads(line) for line in (ROOT/'library/page-index.jsonl').read_text(encoding='utf-8').splitlines()]
    sources=manifest['sources'];ids=[s['source_id'] for s in sources]
    if len(ids)!=len(set(ids)):issues.append('Duplicate source IDs')
    pairs=[(p['source_id'],p['pdf_page']) for p in pages]
    if len(pairs)!=len(set(pairs)):issues.append('Duplicate page records')
    known=set(ids)
    if any(p['source_id'] not in known for p in pages):issues.append('Unknown source in page index')
    for s in sources:
        pdf=ROOT/s['package_pdf']
        if not pdf.exists() or hashlib.sha256(pdf.read_bytes()).hexdigest()!=s['sha256']:
            issues.append('PDF checksum mismatch: '+s['source_id'])
        own=[p for p in pages if p['source_id']==s['source_id']]
        if sorted(p['pdf_page'] for p in own)!=list(range(1,s['page_count']+1)):
            issues.append('Page coverage mismatch: '+s['source_id'])
        md=(ROOT/s['markdown']).read_text(encoding='utf-8')
        if md.count('### Extracted source text')!=s['page_count']:
            issues.append('Markdown page count mismatch: '+s['source_id'])
        for p in own:
            if not (ROOT/p['image']).is_file():issues.append('Missing page image: '+p['image'])
            if f'id="pdf-page-{p["pdf_page"]}"' not in md:issues.append('Missing explicit page anchor')
    checked=0
    # Exclude quoted source text and code examples: these are data, not package-authored links.
    for f in ROOT.rglob('*.md'):
        text=f.read_text(encoding='utf-8');clean=[];code=False
        for line in text.splitlines():
            if line.startswith('```'):code=not code;continue
            if code or line.startswith('>'):continue
            clean.append(line)
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)','\n'.join(clean)):
            target=target.strip().strip('<>')
            if re.match(r'^[a-zA-Z][\w+.-]*:',target):continue
            path,_,frag=unquote(target).partition('#')
            dest=(f.parent/path).resolve() if path else f.resolve()
            checked+=1
            if not dest.is_relative_to(ROOT.resolve()):issues.append(f'Nonportable link: {f.relative_to(ROOT)} -> {target}');continue
            if not dest.exists():issues.append(f'Missing link: {f.relative_to(ROOT)} -> {target}');continue
            if frag.startswith('pdf-page-'):
                if f'id="{frag}"' not in dest.read_text(encoding='utf-8'):
                    issues.append(f'Missing page anchor: {target}')
            if dest.suffix.lower()=='.pdf' and frag.startswith('page='):
                s=next((s for s in sources if (ROOT/s['package_pdf']).resolve()==dest),None)
                if not s or not frag[5:].isdigit() or not 1<=int(frag[5:])<=s['page_count']:
                    issues.append(f'Invalid PDF page: {target}')
    result=dict(status='pass' if not issues else 'fail',documents=len(sources),pages=len(pages),
                page_images=len(list((ROOT/'library/pages').rglob('*.jpg'))),
                checked_relative_links=checked,course_pages=dict(Counter(p['source_id'][3:7] for p in pages)),issues=issues)
    return result

if __name__=='__main__':
    result=validate();print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='pass' else 1)
