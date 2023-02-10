#!/bin/bash

input_pdf="richard_jackson_lebenslauf.pdf"

ocrmypdf --skip-text -l eng+deu --rotate-pages --deskew \
--title "conversion $(date '+%s')" --jobs 4 \
--output-type pdfa $input_pdf \
output_searchable.pdf -f
