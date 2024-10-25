#!/bin/bash

echo ""
echo "#####################################################"
echo "pdflatex -synctex=1 -interaction=nonstopmode main.tex"
echo "#####################################################"
echo ""
pdflatex -synctex=1 -interaction=nonstopmode main.tex

echo ""
echo "#####################################################"
echo "pdflatex -synctex=1 -interaction=nonstopmode main.tex"
echo "#####################################################"
echo ""
pdflatex -synctex=1 -interaction=nonstopmode main.tex


./clean.sh
