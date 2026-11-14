---
title: "ntptrace(8)"
name: "ntptrace"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntptrace/"
description: "ntptrace – trace a chain of NTP servers back to the primary source"
---

<p>ntptrace &#8211; trace a chain of NTP servers back to the primary source</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntptrace [ -n ] [ -m </code><i>maxhosts</i><code> ] [ </code><i>server</i><code> ]</code> </p>
<h2>Description</h2>
<p><code>ntptrace</code> determines where a given Network Time Protocol (NTP) server gets its time from, and follows the chain of NTP servers back to their master time source. If given no arguments, it starts with <code>localhost</code>[char46] Here is an example of the output from <code>ntptrace</code>: </p>
<pre>% ntptrace
localhost: stratum 4, offset 0.0019529, synch distance 0.144135
server2ozo.com: stratum 2, offset 0.0124263, synch distance 0.115784
usndh.edu: stratum 1, offset 0.0019298, synch distance 0.011993, refid 'WWVB'</pre>
<p>On each line, the fields are (left to right): the host name, the host stratum, the time offset between that host and the local host (as measured by <code>ntptrace</code>; this is why it is not always zero for &quot;<code>localhost</code>&quot;), the host synchronization distance, and (only for stratum-1 servers) the reference clock ID. All times are given in seconds. Note that the stratum is the server hop count to the primary source, while the synchronization distance is the estimated error relative to the primary source. These terms are precisely defined in RFC-1305. </p>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt><code>-n</code></p>
<dd>Turns off the printing of host names; instead, host IP addresses are given. This may be useful if a nameserver is down.</dl>
</dl>
<h2>Bugs</h2>
<p>This program makes no attempt to improve accuracy by doing multiple samples. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8) Primary source of documentation: /usr/share/doc/ntp-* This file was automatically generated from HTML source. </p>
