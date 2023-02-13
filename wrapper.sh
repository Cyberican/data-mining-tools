#!/bin/bash

src_pdf=$(ls buckets/new | head -n 10)
target_dir="buckets/queue"

printf "${input_pdf[@]}\n"

for pdf_doc in ${input_pdf[@]}
do
	ocrmypdf --skip-text -l eng+deu --rotate-pages --deskew \
	--title "conversion $(date '+%s')" --jobs 4 \
	--output-type pdfa "${pdf_doc}" \
	${target_dir}/${pdf_doc} -f
done
