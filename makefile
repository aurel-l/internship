TEX=pdflatex

all: report presentation

report: prepare
	${MAKE} -C tmp subreport
	mv tmp/main.pdf report.pdf
	${MAKE} clear

presentation: prepare
	${MAKE} -C tmp subpresentation
	mv tmp/main.pdf presentation.pdf
	${MAKE} clear

subreport:
	${TEX} ../src/report/main.tex
	${TEX} ../src/report/main.tex

subpresentation:
	${TEX} ../src/presentation/main.tex
	${TEX} ../src/presentation/main.tex

prepare:
	mkdir -p tmp

clear:
	rm -r tmp

