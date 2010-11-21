import getopt
import sys

from libcloud.types import NodeState

from lc import get_lc
from printer import Printer


def lister_main(what):
    """Shortcut for main() routine for lister
    tools, e.g. lc-SOMETHING-list

    @param what: what we are listing, e.g. 'nodes'
    @type what: C{string}
    """

    list_method = "list_%s" % what
    profile = "default"
    format = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:p:")
    except getopt.GetoptError, err:
        sys.stderr.write("%s\n" % str(err))
        sys.exit(1)

    for o, a in opts:
        if o == "-f":
            format = a
        if o == "-p":
            profile = a

    conn = get_lc(profile)

    try:
        for node in getattr(conn, list_method)():
            Printer.do(node, format)
    except Exception, err:
        sys.stderr.write("Error: %s\n" % str(err))

def save_image_main():
    """Shortcut for main() routine for provider
    specific image save tools.
    """

    def usage(progname):
        sys.stdout.write("%s -i <node_id> -n <image_name> [-p <profile]\n\n" % progname)
    
    profile = 'default'
    node_id = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:n:p:")
    except getopt.GetoptError, err:
        sys.stderr.write("%s\n" % str(err))
        sys.exit(1)

    for o, a in opts:
        if o == "-i":
            node_id = a
        if o == "-n":
            name = a
        if o == "-p":
            profile = a

    if node_id is None or name is None:
        usage(sys.argv[0])
        sys.exit(1)

    conn = get_lc(profile)

    node = get_node_or_fail(conn, node_id, print_error_and_exit, 
            ("Error: cannot find node with id '%s'." % node_id,))

    Printer.do(conn.ex_save_image(node, name))

def get_node_or_fail(conn, node_id, coroutine=None, cargs=(), ckwargs={}):
    """Shortcut to get a single node by its id. In case when 
    such node could not be found, coroutine could be called
    to handle such case. Typically coroutine will output an
    error message and exit from application.

    @param conn: libcloud connection handle
    @param node_id: id of the node to search for
    @param coroutine: a callable object to handle case
        when node cannot be found
    @param cargs: positional arguments for coroutine
    @param kwargs: keyword arguments for coroutine
    @return: node object if found, None otherwise"""

    try:
        node = [node for node in conn.list_nodes()
                if str(node.id) == str(node_id)][0]
        return node
    except IndexError:
        if callable(coroutine):
            coroutine(*cargs, **ckwargs)
        return None

def print_error_and_exit(message):
    sys.stderr.write("%s\n" % message)
    sys.exit(1)
