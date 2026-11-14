---
title: "ragator(1)"
name: "ragator"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ragator/"
description: "ragator – aggregate argus(8) data file entries."
---

<h2>NAME</h2>
<p> <code>ragator</code> &#8211; aggregate <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data file entries.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2003 QoSient. All rights reserved.</p>
<h2>SYNOPSIS</h2>
<p> <code>ragator</code> [<code>-f</code> <i>ragator.conf</i>] [<code>raoptions</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ragator</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus-file</i>, and merges matching argus flow activity records together. In its default mode of options, this effectively converts <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> files from detail to non-detail mode, and merges periodic flow report records to a single argus record, thus compressing the <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> file to a reduced size. </p>
<p> You can modify the aggregation strategy used by <code>ragator</code> to merge records together, by using the <code>-f ragator.conf</code> option. See <code><a href="/docs/linux/man/5-ragator/">ragator</a>(5)</code> for a complete description of the format and syntax of the flow model file. </p>
<h2>OPTIONS</h2>
<p> Ragator, like all ra based clients, supports a number of <code>ra options</code> including filtering of input argus records through a terminating filter expression. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ragator/">ragator</a></code>(5) <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1), </p>
<h2>Index</h2>
