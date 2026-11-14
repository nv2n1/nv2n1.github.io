---
title: "radecode(1)"
name: "radecode"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radecode/"
description: "radecode – tshark-like decode of argus(1) user data"
---

<h2>NAME</h2>
<p> radecode &#8211; tshark-like decode of <a href="/docs/linux/man/1-argus/">argus</a>(1) user data</p>
<h2>SYNOPSIS</h2>
<p> <code>radecode </code> <code>-r</code> <i>argusFlowFile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Radecode </code> is a perl script that uses <a href="/docs/linux/man/1-text2pcap/">text2pcap</a>(1) and <a href="/docs/linux/man/1-tshark/">tshark</a>(1) from the <a href="/docs/linux/man/1-wireshark/">wireshark</a>(1) distribution to decode TCP and UDP flow associated user data from an <code>argus</code> flow capture file. You must enable <code>argus</code> user data capture with the -U nnnn option or there will be no data to decode. Due to limitations in test2pcap only TCP and UDP flows are decoded. The other flow data are silently ignored.</p>
<h2>OPTIONS</h2>
<p> In addition to the source file name all <a href="/docs/linux/man/1-ra/">ra</a>(1) options are available but may not make sense.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tshark/">tshark</a>(1), <a href="/docs/linux/man/1-text2pcap/">text2pcap</a>(1), <a href="/docs/linux/man/1-ra/">ra</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard
Dave Edelman
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
