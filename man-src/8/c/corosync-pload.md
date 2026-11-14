---
title: "corosync-pload(8)"
name: "corosync-pload"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-pload/"
description: "corosync-pload – Start payload test."
---

<p>corosync-pload &#8211; Start payload test.</p>
<h2>Synopsis</h2>
<p><code>corosync-pload</code></p>
<h2>Description</h2>
<p><code>corosync-pload</code> starts the pload service. This is used as a test tool to generate traffic. All nodes will begin transmitting messages and they will stop when 1500000 messages have been received per node. </p>
<p> To view the progress of this execute: </p>
<p> $ corosync-objctl runtime.services.pload.<br />
 runtime.services.pload.service_id=13<br />
 runtime.services.pload.0.tx=3<br />
 runtime.services.pload.0.rx=2<br />
 runtime.services.pload.1.tx=2478788<br />
 runtime.services.pload.1.rx=4467870 </p>
<p> At the end of the run a log message will be written showing the number of messages written and the time that this took. </p>
<p> corosync[4931]: [PLOAD ] 1500000 Writes 300 bytes per write 30.838 seconds runtime, 48640.968 TP/S, 13.916 MB/S.</p>
<dl>
<dt></dl>
<h2>See Also</h2>
<dd><code><a href="/docs/linux/man/8-corosync-objctl/">corosync-objctl</a></code>(8)</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
