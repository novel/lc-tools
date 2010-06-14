import sys

from shortcuts import readable_status

class Printer(object):
    _formats = {"nodeimage": "image %(name)s (id = %(id)s)",
            "nodesize": "size %(name)s (id=%(id)s, ram=%(ram)s, disk=%(disk)s bandwidth=%(bandwidth)s)"}

    @classmethod
    def do(self, thing, format=None):
        """Smart print object depending on its type.

        Order of preference: _print_$objtime() method -> _formats -> str(obj)"""

        print_class = thing.__class__.__name__.lower()
        print_method = "_print_%s" % print_class

        if hasattr(self, print_method):
            return getattr(self, print_method)(thing)

        fmt = None        

        if format is not None:
            fmt = format 
        else:
            fmt = self._formats.get(thing.__class__.__name__.lower())

        if fmt is not None:
            sys.stdout.write((fmt + "\n") % thing.__dict__)
        else:
            sys.stdout.write(str(thing))

    @classmethod
    def _print_gogridnode(self, thing):
        values = thing.__dict__.copy()
        # gogrid only has one public ip per server
        values['ip'] = values['public_ip'][0]
        values['rstatus'] = readable_status[int(values['state'])]

        fmt = "%(id)s\t%(name)s\t%(ip)s\t%(rstatus)s\n"
        sys.stdout.write(fmt % values)
