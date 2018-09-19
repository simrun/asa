html-css-handout.pdf: html-css-handout.md

docs:
	pandoc html-css-handout.md --pdf-engine=xelatex -o html-css-handout.pdf

clean:
	rm html-css-handout.pdf