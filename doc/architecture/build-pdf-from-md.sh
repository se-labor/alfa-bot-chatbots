#!/bin/bash

pandoc -o Dokumentation-ALFA-Bot.pdf \
  -F pandoc-plantuml \
  -V documentclass=report \
  --pdf-engine=xelatex \
  --template eisvogel \
  --listings \
  $(ls -a1 *.md | grep -v  09_9999_template)
