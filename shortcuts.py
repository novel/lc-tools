import getopt
import sys

from libcloud.types import NodeState

from lc import get_lc
from printer import Printer


def lister_main(what):
    list_method = "list_%s" % what
    profile = "default"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
    except getopt.GetoptError, err:
        sys.stderr.write("%s\n" % str(err))
        sys.exit(1)

    for o, a in opts:
        if o == "-p":
            profile = a

    conn = get_lc(profile)

    for node in getattr(conn, list_method)():
        Printer.do(node)
