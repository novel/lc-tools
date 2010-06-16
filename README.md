## lc-tools

lc-tools is a set of command line tools to control various clouds. It
uses libcloud for cloud related stuff so should support as much cloud
providers as libcloud does.

## Getting started

We will use GoGrid as example.

First, create config file: ~/.ggrc with the following content:

<pre><code>[default]
driver = gogrid
access_id = <key_id>
secret_key = <password>
</code></pre>

It is self-explanatory.

When you're done with the configuration file, you can start managing your
servers. To list the available image, fire up lc-image-list command
in your shell:

<pre><code>./lc-image-list|grep -i centos
image CentOS 5.2 (32-bit) w/ RightScale (id = 62)
image CentOS 5.2 (64-bit) w/ RightScale (id = 63)
image CentOS 5.3 (32-bit) w/ None (id = 1531)
image CentOS 5.3 (64-bit) w/ None (id = 1532)
</code></pre>

Now, to get a list of available node sizes, do:

<pre><code>./lc-sizes-list
size 512MB (id=512MB, ram=512, disk=30 bandwidth=None)
size 4GB (id=4GB, ram=4096, disk=240 bandwidth=None)
size 2GB (id=2GB, ram=2048, disk=120 bandwidth=None)
size 8GB (id=8GB, ram=8192, disk=480 bandwidth=None)
size 1GB (id=1GB, ram=1024, disk=60 bandwidth=None)
</code></pre>

So now you know ids of the images and available sizes, 
you can use them to create a new node like that:

<pre><code>./lc-node-add -i 62 -s 1GB -n mynewnode</code></pre>

It will create a centos node (id = 64) of size 1GB (id = '1GB')
with name 'mynewnode'.

Now, to get a list of nodes, use:

<pre><code>./lc-node-list
100xxx  mynode1     173.204.xx.yy  Running
100xxx  mynode2    173.204.xx.zz  Running
</code></pre>

## Support

Any feedback is welcome! You can use github to contact me
or plain old email: novel@FreeBSD.org
