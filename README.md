pypacket_dissector
==================

Yet another IP packet dissector, MIT license.

It is going to support a small set of protocols that I need,
such as IPv6, IPv4, UDP, CoAP.

If you want to dissect L2 protocol, use pypcap_dissector instead.

If you want a full set of dissectors, use dpkt, scapy or something like that.

## goal

- simple, lightweight.
- python3 based.
- json fiendly.
- separation from pcap.

## requirement

- python3

## How to use

You can dissect data in the file you specified or stdin.

```
% packet_decoder.py example/test.dat
{
    "PROTO": "IPV6",
    "HEADER": {
	"IPV6.VER": 6,
	"IPV6.TC": 0,
	"IPV6.FL": 694078,
	"IPV6.LEN": 14,
	"IPV6.NXT": 17,
	"IPV6.HOP_LMT": 64,
	"IPV6.SADDR": "fe80::aebc:32ff:feba:1c9f",
	"IPV6.DADDR": "fe80::201:c0ff:fe06:3e69"
    },
    "PAYLOAD": {
	"PROTO": "UDP",
	"HEADER": {
	    "UDP.SPORT": 50145,
	    "UDP.DPORT": 9999,
	    "UDP.LEN": 14,
	    "UDP.CKSUM": 63356,
	    "PAYLOAD": "48656c6c6f0a"
	},
	"EMSG": "unsupported. L5 PORT=(50145, 9999)"
    }
}
```

## Usage

```
usage: packet_decoder.py [-h] [--delimiter _DELIMITER] [--noshow-sep] [-v]
                         [-d]
                         target

a packet dissector.

positional arguments:
  target                specify a filename containing packet data. '-' allows
                        the stdin as the input.

optional arguments:
  -h, --help            show this help message and exit
  --delimiter _DELIMITER
                        specify a delimiter to read a series of data from the
                        stdin. e.g. "00ff707970636170ff00" (default:
                        00ff707970636170ff00)
  --noshow-sep          disable to show the separator. (default: True)
  -v                    enable verbose mode. (default: False)
  -d                    enable debug mode. (default: False)
```

