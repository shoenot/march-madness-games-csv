#!/usr/bin/env python3

from pathlib import Path
from extract_wiki_from_html import extract_wiki_from_html
from extract_json_from_wiki import extract_json_from_wiki
from extract_csv_from_json import extract_csv_from_json

root_dir = Path(__file__).parent

def generate_data():
    for html_path in Path(root_dir / "html").iterdir():
        year = html_path.name.split(".")[0]
        if year == "2021":
            pass 

        wiki_path = root_dir / "wiki" / f"{year}.wiki"
        json_path = root_dir / "json" / f"{year}.json"
        csv_path = root_dir / "csv" / f"{year}.csv"

        extract_wiki_from_html(html_path, wiki_path)
        extract_json_from_wiki(wiki_path, json_path)
        extract_csv_from_json(json_path, csv_path)

if __name__ == "__main__":
    generate_data()
