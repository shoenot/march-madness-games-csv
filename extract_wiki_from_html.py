# Fix BS4 issue with Python 3.10+
import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup


def extract_source(html):
    soup = BeautifulSoup(html, 'html.parser')
    textareas = soup.select('textarea')
    assert len(textareas) == 1
    return textareas[0].text


def extract_wiki_from_html(inpath, outpath):
    html = open(inpath).read()
    source = extract_source(html)
    open(outpath, 'w').write(source)
