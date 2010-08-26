#!/bin/sh

MAN_PREFIX="${PREFIX}/share/man"
RONN=${RONN:-/var/lib/gems/1.8/bin/ronn}

for man in *.ronn; do
	section=`echo ${man}|sed 's/.*\([0-9]\).*/\1/'`
	file=`echo ${man}|sed 's/\.ronn$//'`
	target="${MAN_PREFIX}/man${section}/${file}"
	echo "${man} --> ${target}"
	${RONN} -r --pipe ${man}> ${target}
done
