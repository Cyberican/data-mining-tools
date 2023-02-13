#!/usr/bin/env python

import os
import re
import numpy as np
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import configparser
import nltk
import tqdm
nltk.download('stopwords')

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('german')
settings_file = 'settings.ini'

def run_ocr_on_pdf(pdf_path):
    print(pdf_path)
    files = os.listdir(pdf_path)
    for file in files:
        print(file)

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    return text

def build_corpus(doc):
    corpus = [ s for s in doc.split('\n') ]
    return corpus

def normalize_document(doc):
    # lowercase and remove special characters\whitespace
    pattern = r"[^\w\s]"
    doc = re.sub(pattern,'', doc, re.I|re.A)
    # Remove special characters
    doc = re.sub(r'[^a-zA-z]\s','', doc, re.I|re.A)
    # Remove any numbers
    doc = re.sub(r'[0-9]',' ',doc)
    # Convert all to lowercases
    doc = doc.lower()
    # Remove trailing spaces
    doc = doc.strip()
    # tokenize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [ token for token in tokens if token not in stop_words ]
    doc = ' '.join(filtered_tokens)
    return doc

if __name__ == '__main__':
    config = configparser.ConfigParser()
    if os.path.exists(settings_file):
        config.read(settings_file)
    else:
        print("Missing or invalid settings file: {}!".format(settings_file))
    try:
        src_dir = "{}/new".format(config['resource']['name'])
        pdf_files = os.listdir(src_dir)
        if len(pdf_files) > 0:
            # run_ocr_on_pdf("{}".format(src_dir))
            for file in pdf_files:
                src_file = "{}/{}".format(src_dir, file)
                text = extract_text_from_pdf(src_file)
                normalize_corpus = np.vectorize(normalize_document)
                corpus = build_corpus(text)
                norm_corpus = normalize_corpus(corpus)
                print([ w for w in norm_corpus if len(w) > 1 ])
    except Exception as e:
        print("Error: {} not found!".format(e))
        print("")
