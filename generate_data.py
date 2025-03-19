#!/usr/bin/env python3

from pathlib import Path
from extract_wiki_from_html import extract_wiki_from_html
from extract_json_from_wiki import extract_json_from_wiki
from extract_csv_from_json import extract_csv_from_json
import re

root_dir = Path(__file__).parent

def generate_data():
    for html_path in Path(root_dir / "html").iterdir():
        year = html_path.name.split(".")[0]

        # 2021 had a game cancelled due to Covid-19. This fixes the results for that game.
        if year == "2021":
            with open(html_path, 'r') as fp:
                filedata = fp.read()

            filedata = re.sub(r'13=\'\'\'WO\'\'\'', '13=\'\'\'1\'\'\'', filedata)
            filedata = re.sub(r'14=\n', '14=\'\'\'0\'\'\'', filedata)

            with open(html_path, 'w') as fp:
                fp.write(filedata)

        wiki_path = root_dir / "wiki" / f"{year}.wiki"
        json_path = root_dir / "json" / f"{year}.json"
        csv_path = root_dir / "csv" / f"{year}.csv"

        extract_wiki_from_html(html_path, wiki_path)
        extract_json_from_wiki(wiki_path, json_path)
        extract_csv_from_json(json_path, csv_path)

if __name__ == "__main__":
    generate_data()
