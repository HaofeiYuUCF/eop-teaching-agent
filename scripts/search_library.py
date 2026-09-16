"""Read-only literal search with source/page locators; no dependencies or answer generation."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def search(query, course=None, source=None):
    terms = [x.lower() for x in re.findall(r'"([^"]+)"|(\S+)', query) for x in x if x]
    if not terms:
        return []
    results = []
    with (ROOT / 'library/page-index.jsonl').open(encoding='utf-8') as stream:
        for line in stream:
            page = json.loads(line)
            if course and not page['source_id'].startswith('ENV' + course + '-'):
                continue
            if source and page['source_id'] != source:
                continue
            body = page['text'] + '\n' + page['heading'] + '\n' + page.get('visual_navigation', '')
            normalized = re.sub(r'\s+', ' ', body).lower()
            if not all(t in normalized for t in terms):
                continue
            score = sum(normalized.count(t) for t in terms)
            results.append(dict(source_id=page['source_id'],pdf_page=page['pdf_page'],
                                heading=page['heading'],flags=page['flags'],
                                markdown=page['markdown']+'#pdf-page-'+str(page['pdf_page']),
                                pdf=page['pdf']+'#page='+str(page['pdf_page']),image=page['image'],
                                score=score,extracted_text=page['text'],
                                visual_navigation=page.get('visual_navigation')))
    return sorted(results, key=lambda x: (-x['score'], x['source_id'], x['pdf_page']))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query',required=True)
    parser.add_argument('--course',choices=['4120','5128','6106'])
    parser.add_argument('--source')
    parser.add_argument('--limit',type=int,default=8)
    args=parser.parse_args()
    if args.limit<1: parser.error('--limit must be positive')
    results=search(args.query,args.course,args.source)
    print(json.dumps(dict(query=args.query,total_hits=len(results),results=results[:args.limit],
          status='candidate source pages; inspect before answering' if results else 'no text match',
          limitation='Literal retrieval only. No match is not proof of absence in visual content. Do not invent a source or answer.'),ensure_ascii=True,indent=2))

if __name__=='__main__': main()
