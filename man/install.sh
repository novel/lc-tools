#!/bin/sh

MAN_PREFIX="${PREFIX}/share/man"
RONN=${RONN:-ronn}

${RONN} --version > /dev/null 2>&1

if test $? -ne 0; then
	echo "Warning: ronn not found, man pages will not be regenerated!"
	echo "Will try to install from cache..."
else
	echo "Converting ronn files to man pages..."

	for man in *.ronn; do
		section=`echo ${man}|sed 's/.*\([0-9]\).*/\1/'`
		file=`echo ${man}|sed 's/\.ronn$//'`
		#target="${MAN_PREFIX}/man${section}/${file}"
		target=`echo ${man}|sed 's/\.ronn$//'`
		echo "${man} --> ${target}"
		${RONN} -r --pipe ${man}> ${target}
	done
fi

for i in *.1 *.5; do
	section=`echo ${i}|sed 's/.*\([0-9]\).*/\1/'`
	#echo ${section}
	target="${MAN_PREFIX}/man${section}"
	# check if man directory exists	
	if ! test -d ${target}; then
		mkdir -p ${target}
	fi
	echo "${i} --> ${target}"
	install -m 444 ${i} ${target}
done
