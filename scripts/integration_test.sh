#!/bin/sh
#
# a test to ensure that basic things are working fine

PROJECTDIR=".."
CONF=~/.lcrc

# functions
check_prereq() {
	# check config
	if test ! -r ${CONF}; then
		echo "Cannot open ${CONF}, cannot proceed."
		exit 1;
	fi
}

find_image() {
	IMAGE=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-image-list -f "%(id)s %(name)s" \
		|grep -i centos|head -1|awk '{print $1}'`
	echo ${IMAGE}
}

main() {
	check_prereq

	IMAGE=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-image-list -f "%(id)s %(name)s" \
		|grep -i centos|head -1|awk '{print $1}'`
	SIZE=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-sizes-list -f "%(id)s"|head -1`
	#echo ${SIZE}
	NAME="lcinttest`date '+%s'`"

	echo "about to create a test server with the following params:"
	echo "name: ${NAME}"
	echo "image id: ${IMAGE}"
	echo "size id: ${SIZE}"

	PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-node-add -i ${IMAGE} -s ${SIZE} -n ${NAME}

	TIMEOUT=60

	echo "going to sleep for ${TIMEOUT} seconds to let IaaS do its thing"
	sleep ${TIMEOUT}

	echo "checking if server in a list"

	MATCHES=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-node-list|grep ${NAME}|wc -l`

	if test ! ${MATCHES} = "1"; then
		echo "FAIL: server doesn't appear in the list"
		exit 1
	fi

	echo "server is in the list"
	
	SERVER=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-node-list|grep ${NAME}`
	SERVER_ID=`echo ${SERVER}|awk '{print $1}'`

	echo "removing server"
	PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-node-do -i ${SERVER_ID} destroy
	
	MATCHES=`PYTHONPATH=${PROJECTDIR} ${PROJECTDIR}/lc-node-list|grep ${NAME}|wc -l`

	if test ! ${MATCHES} = "0"; then
		echo "FAIL: wasn't able to remove server"
		exit 1
	else
		echo "SUCCESS: test passed"
	fi
}

# main
main
