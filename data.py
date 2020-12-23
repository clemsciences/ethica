
import codecs
# from cltk.corpus.utils import importer
# from cltk.corpus.readers import get_corpus_reader
# ci = importer.CorpusImporter("latin")
# ci.import_corpus("lat_text_latin_library")
#
# reader = get_corpus_reader(language="lat", corpus_name="lat_text_latin_library")
#
# print(reader.root)

import os
import requests


def retrieve_texts():
    core_link = "https://raw.githubusercontent.com/cltk/lat_text_latin_library/master/"
    if not os.path.exists("text"):
        os.mkdir("text")
    for i in range(1, 6):
        r = requests.get(f"{core_link}spinoza.ethica{i}.txt")
        if r:
            with codecs.open(os.path.join("text", f"ethica-{i}.txt"), "w", encoding="utf-8") as f:
                f.write(r.content.decode("utf-8"))


def load_text():
    chapters = []
    for filename in os.listdir("text"):
        with codecs.open(os.path.join("text", filename), "r", encoding="utf-8") as f:
            chapter = f.read()
            chapters.append(chapter)
    return chapters


if __name__ == "__main__":
    # retrieve_texts()
    load_text()
