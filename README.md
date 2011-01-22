## lc-tools

http://novel.github.com/lc-tools/

lc-tools is a set of command line tools to control various clouds. It
uses libcloud for cloud related stuff so should support as much cloud
providers as libcloud does.

## Installation

sudo python setup.py install

## Documnetation

Tutorial for the latest version is available online:

http://novel.github.com/lc-tools/doc/latest/tutorial/

This README contains basic information how to get started.

## Getting started

We will use GoGrid as example.

First, create config file: `~/.lcrc` with the following content:

	[default]
	driver = gogrid
	access_id = your_key_id
	secret_key = your_password

It is self-explanatory. Don't forget to run `chmod 600` on it to
keep your credentials secret.

When you're done with the configuration file, you can start managing your
servers. To list the available image, fire up lc-image-list command
in your shell:

	$ lc-image-list|grep -i centos
	image CentOS 5.2 (32-bit) w/ RightScale (id = 62)
	image CentOS 5.2 (64-bit) w/ RightScale (id = 63)
	image CentOS 5.3 (32-bit) w/ None (id = 1531)
	image CentOS 5.3 (64-bit) w/ None (id = 1532)

Now, to get a list of available node sizes, do:

	$ lc-sizes-list
	size 512MB (id=512MB, ram=512, disk=30 bandwidth=None)
	size 4GB (id=4GB, ram=4096, disk=240 bandwidth=None)
	size 2GB (id=2GB, ram=2048, disk=120 bandwidth=None)
	size 8GB (id=8GB, ram=8192, disk=480 bandwidth=None)
	size 1GB (id=1GB, ram=1024, disk=60 bandwidth=None)

So now you know ids of the images and available sizes,
you can use them to create a new node like that:

	lc-node-add -i 62 -s 1GB -n mynewnode

It will create a centos node (id = 64) of size 1GB (id = '1GB')
with name 'mynewnode'.

Now, to get a list of nodes, use:

	$ lc-node-list
	100xxx  mynode1     173.204.xx.yy  Running
	100xxx  mynode2    173.204.xx.zz  Running

When you're done with the node, you can remove it:

	$ lc-node-do -i node_id destroy

where `node_id` is an id of the node you want to destroy. If
you want to reboot node, just pass 'reboot' argument to this
command instead of 'destroy'.

## Support

Any feedback is welcome! You can use github to contact me
or plain old email: novel@FreeBSD.org
