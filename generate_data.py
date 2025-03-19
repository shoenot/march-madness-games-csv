#!/usr/bin/env python3

from pathlib import Path
from extract_wiki_from_html import extract_wiki_from_html
from extract_json_from_wiki import extract_json_from_wiki
from extract_csv_from_json import extract_csv_from_json
import re
import csv

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

def generate_combined_csv():
    data = []
    for csv_path in sorted(Path(root_dir / "csv").iterdir(), key=str, reverse=True):
        if csv_path.name == "combined.csv":
            continue
        with open(csv_path, 'r', newline='') as fp:
            reader = csv.reader(fp)
            # skip header 
            next(reader)
            for row in reader:
                data.append(row)
    combined_csv_path = root_dir / "csv" / "combined.csv"
    with open(combined_csv_path, 'w') as fp:
        fieldnames = ["year", "round_of", 
                      "winning_team_name", "winning_team_seed", "winning_team_score", 
                      "losing_team_name", "losing_team_seed", "losing_team_score"]
        writer = csv.writer(fp)
        writer.writerow(fieldnames)
        writer.writerows(data)

if __name__ == "__main__":
    generate_data()
    generate_combined_csv()
