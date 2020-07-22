#!/usr/bin/env python

import sys
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter

try:
    from pypacket_dissector import encoder as en
except:
    import encoder as en

def main():
    ap = ArgumentParser(description="a packet encoder.",
                        formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument("infile", metavar="INFILE", nargs="?", type=str,
                   default="-",
                   help='''specify a filename containing json.
                   default is stdin.''')
    ap.add_argument("-v", action="store_true", dest="f_verbose",
                   help="enable verbose mode.")
    ap.add_argument("-d", action="store_true", dest="f_debug",
                   help="enable debug mode.")

    opt = ap.parse_args()
    #
    if opt.infile == "-":
        jo = sys.stdin.read()
    else:
        jo = open(opt.infile, "r").read()
    #
    jd = en.load_json_packet(jo)
    ret = en.encoder(jd)
    sys.stdout.buffer.write(ret)

if __name__ == "__main__":
    main()
