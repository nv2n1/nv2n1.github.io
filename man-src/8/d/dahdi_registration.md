---
title: "dahdi_registration(8)"
name: "dahdi_registration"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_registration/"
---

dahdi_registration - Handle registration of Xorcom XPD modules in dahdi.

<h2>Synopsis</h2>

dahdi_registration [-s sortorder] [on|off]

<h2>Description</h2>

Without parameters, show all connected XPDs sorted by physical connector order. Each one is show to be unregistered (off), or registered to a specific dahdi span (the span number is shown). 

 All registerations/deregisterations are sorted by physical connector string. 

 Span registration should generally always succeed. Span unregistration may fail if channels from the span are in use by e.g. asterisk. In such a case you'll also see those channels as '(In use)' in the output of <i><a HREF="/docs/linux/man/8-lsdahdi/">lsdahdi</a></i>(8).

<h2>Parameters</h2>

off --- deregisters all <font SIZE="-1">XPD</font>'s from dahdi. 

 on --- registers all <font SIZE="-1">XPD</font>'s to dahdi.

<h2>Options</h2>

<dl><dt>-s <i>sort_order</i>
<dd>The sort order to use.</dl>
 

 If the option is not used, the sort order is taken from the environment variable <font SIZE="-1">XBUS_SORT</font> and failing that: the hard-coded default of <font SIZE="-1">SORT_CONNECTOR</font>. 

 The available sorting orders are documented in Dahdi::Xpp manual.

<h2>Sample Output</h2>

An example of the output of dahdi_registration for some registered Astribanks: 

 <pre> $ dahdi_registration -s type
 XBUS-01 usb:0000153 usb-0000:00:10.4-2
 XBUS-01/XPD-00: on Span 1
 XBUS-01/XPD-01: on Span 2
 XBUS-00 usb:0000157 usb-0000:00:10.4-4
 XBUS-00/XPD-00: on Span 3
 XBUS-00/XPD-01: on Span 4
 XBUS-00/XPD-02: on Span 5
 XBUS-00/XPD-03: on Span 6
 XBUS-00/XPD-04: on Span 7
 XBUS-00/XPD-05: on Span 8
 XBUS-00/XPD-06: on Span 9
 XBUS-00/XPD-07: on Span 10
 XBUS-02 usb-0000:00:10.4-1
 XBUS-02/XPD-00: on Span 11
 XBUS-02/XPD-10: on Span 12
 # Sorted: type</pre>

<h2>Files</h2>

<dl><dt>/proc/xpp/XBUS-nn/XPD-mm/dahdi_registration
<dd>Reading from this file shows if if the if the specific <font SIZE="-1">XPD</font> is registered. Writing to it 0 or 1 registers / unregisters the device. 

 This should allow you to register / unregister a specific <font SIZE="-1">XPD</font> rather than all of them. 

</dl>
