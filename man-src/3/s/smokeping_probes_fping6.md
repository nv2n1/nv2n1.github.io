---
title: "smokeping_probes_fping6(3)"
name: "smokeping_probes_fping6"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_fping6/"
---

Smokeping::probes::FPing6 - FPing6 Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +FPing6
 binary = /usr/bin/fping6 # mandatory
 blazemode = true
 hostinterval = 1.5
 mininterval = 0.001
 offset = 50%
 packetsize = 5000
 pings = 20
 sourceaddress = ::1
 step = 300
 timeout = 1.5
 tos = 0x20
 usestdout = true
 # [...]
 *** Targets ***
 probe = FPing6 # if this should be the default probe
 # [...]
 + mytarget
 # probe = FPing6 # if the default probe is something else
 host = my.host</pre><h2>Description</h2>Integrates FPing6 as a probe into smokeping. This probe is derived from FPing; the only difference is that the target host used for checking the fping command output is ::1 instead of localhost.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
<dd>The location of your fping binary. 

 Example value: /usr/bin/fping6 

 This setting is mandatory.
<dt>blazemode
<dd>Send an extra ping and then discarge the first answer since the first is bound to be an outliner. 

 Example value: true
<dt>hostinterval
<dd>The fping ``-p'' parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. From <i><a HREF="/docs/linux/man/1-fping/">fping</a></i>(1): 

 This parameter sets the time that fping waits between successive packets to an individual target. 

 Example value: 1.5
<dt>mininterval
<dd>The fping ``-i'' parameter, but in (probably fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. From <i><a HREF="/docs/linux/man/1-fping/">fping</a></i>(1): 

 The minimum amount of time between sending a ping packet to any target. 

 Example value: 0.001 

 Default value: 0.01
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>packetsize
<dd>The ping packet size (in the range of 12-64000 bytes). 

 Example value: 5000
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 20
<dt>sourceaddress
<dd>The fping ``-S'' parameter . From <i><a HREF="/docs/linux/man/1-fping/">fping</a></i>(1): 

 Set source address. 

 Example value: ::1
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300
<dt>timeout
<dd>The fping ``-t'' parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. Note that as Smokeping uses the fping 'counting' mode (-C), this apparently only affects the last ping. 

 Example value: 1.5
<dt>tos
<dd>Set the type of service (<font SIZE="-1">TOS</font>) of outgoing <font SIZE="-1">ICMP</font> packets. You need at laeast fping-2.4b2_to3-ipv6 for this to work. Find a copy on <a rel="nofollow" HREF="http://www.smokeping.org">www.smokeping.org</a>/pub. 

 Example value: 0x20
<dt>usestdout
<dd>Listen for FPing output on stdout instead of stderr ... (version 3.3+ sends its statistics on stdout). 

 Example value: true</dl><h2>Authors</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; 

 Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>See Also</h2>Smokeping::probes::FPing
