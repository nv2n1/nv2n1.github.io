---
title: "opagenchassis(8)"
name: "opagenchassis"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opagenchassis/"
---

opagenchassis 

 

 

 Generates a list of IPv4, IPv6, and/or TCP names in a format acceptable for inclusion in the /etc/sysconfig/opa/chassis file.

<h2>Syntax</h2>

opagenchassis [-t <i>portsfile</i>] [-p <i>ports</i>]

<h2>Options</h2>

<dl><dt>--help
</dt><dd>Produces full help text.
</dd><dt>-t <i>portsfile</i>
</dt><dd>File with list of local HFI ports used to access fabric for analysis. Default is /etc/sysconfig/opa/ports file.
</dd><dt>-p <i>ports</i>
</dt><dd>List of local HFI ports used to access fabrics for counter clear. Default is first active port. The first HFI in the system is 1. The first port on an HFI is 1. 
</dd><dd>Uses the format hfi:port, for example:
</dd><dl><dd></dd><dl><dd>0:0 First active port in system. 
</dd></dl></dl><dl><dd></dd><dl><dd>0:y Port <i>y</i> within system. 
</dd></dl></dl><dl><dd></dd><dl><dd>x:0 First active port on HFI <i>x</i>. 
</dd></dl></dl><dl><dd></dd><dl><dd>x:y HFI <i>x</i>, port <i>y</i>. 
</dd></dl></dl>
 

</dl>

<h2>Environment Variables</h2>

<dl><dt>PORTS
</dt><dd>List of ports, used in absence of -t and -p.
</dd><dt>PORTS_FILE
</dt><dd>File containing list of ports, used in absence of -t and -p.</dd></dl>

<h2>Examples</h2>

opagenchassis 
 opagenchassis -p '1:1 1:2 2:1 2:2' 
