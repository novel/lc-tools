#!/bin/sh
#
# Script to update dynamic parts of the site.


## general settings
BRANCH="gh-pages"
PROJECT_DIR="`pwd`/.."
LCTOOLS_VERSION="`cat ${PROJECT_DIR}/VERSION`"

## path settings
SITEDIR=~/lctools_doc
TUTORIAL_SOURCE_PATH="${PROJECT_DIR}/doc/tutorial.tex"
TUTORIAL_OUTPUT_PATH="${SITEDIR}/doc/${LCTOOLS_VERSION}/tutorial"
MAN_INPUT_PATH="${PROJECT_DIR}/man"
MAN_OUTPUT_PATH="${SITEDIR}/doc/${LCTOOLS_VERSION}/man"

## commands
LATEX2HTML="latex2html -verbosity 0 -info 0 -show_section_numbers -local_icons"
RONN="ronn"

#echo ${PROJECT_DIR}

prepare_work_dir() {
	echo " * setting up working directory"

	rm -fr ${SITEDIR}
	mkdir -p ${SITEDIR}
}

build_tutorial() {
	echo " * building tutorial"

	mkdir -p ${TUTORIAL_OUTPUT_PATH} > /dev/null 2>&1
	${LATEX2HTML} -dir ${TUTORIAL_OUTPUT_PATH} \
		${TUTORIAL_SOURCE_PATH} > /dev/null 2>&1
	cp tutorial.css ${TUTORIAL_OUTPUT_PATH}
}

build_man() {
	echo " * building man pages"

	mkdir -p ${MAN_OUTPUT_PATH} > /dev/null 2>&1

	echo "<html><body><ul>" > ${MAN_OUTPUT_PATH}/index.html

	for man in ${MAN_INPUT_PATH}/*.ronn; do
		HTML_OUTPUT=`basename ${man}|sed -e 's|ronn$|html|'`
		${RONN} --html --pipe ${man} > \
			${MAN_OUTPUT_PATH}/${HTML_OUTPUT};
		echo "<li><a href='${HTML_OUTPUT}'>${HTML_OUTPUT}</a></li>" >> ${MAN_OUTPUT_PATH}/index.html
	done

	echo "</ul></body></html>" >> ${MAN_OUTPUT_PATH}/index.html
}

create_latest_link() {
	echo " * creating symlinks"
	rm -f "${SITEDIR}/doc/latest"
	cd "${SITEDIR}/doc" && \
		ln -s "${LCTOOLS_VERSION}" "latest"
}

prepare_work_dir

build_man

build_tutorial

create_latest_link

echo "Preview: file://${SITEDIR}"
