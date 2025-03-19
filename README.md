# March Madness Men's Tournament Individual Game Results

**All of the code for the data extraction from Wikipedia comes from [danvk/march-madness-data](https://github.com/danvk/march-madness-data), with fixes from [caycehouse/march-madness-data](https://github.com/caycehouse/march-madness-data). This would've taken significantly longer without their work, so all credit goes to them.**

I couldn't find a source which had each individual March Madness game in a tabular format, 
so I decided write a script to compile them into CSV files myself, based on the aforementioned repos' work. 

I will try to keep the data up to date, but in the event that I forget, you can simply clone the repo, update the years in getpages.sh, and run: 
```
pip install -r requirements.txt
./getpages.sh
python generate_data.py
```
This will automatically populate the data folders with new years. 

### Quirks
- 2021 had a singular game that was abandoned due to Covid-19 protocol (Oregon vs VCU). The script automatically edits the HTML to give Oregon a score of 1 and VCU a score of 0.  
