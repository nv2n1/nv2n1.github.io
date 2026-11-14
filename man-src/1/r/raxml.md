---
title: "raxml(1)"
name: "raxml"
section: "1"
letter: "r"
url: "/docs/linux/man/1-raxml/"
description: "raxml – convert argus(8) data to XML."
---

<h2>NAME</h2>
<p> <code>raxml</code> &#8211; convert <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data to XML.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2003 QoSient. All rights reserved.</p>
<h2>SYNOPSIS</h2>
<p> <code>raxml</code> [ra-options] <code>-e (Ascii | Encode64)</code> [ <i>expression</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Raxml</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus data</i> source, and converts the contents to XML format, printing its output to <code>stdout</code>. Like all ra based clients, <code>raxml </code> supports a large number of options, configuration through .rarc files, and input filtering using the terminating filter <i>expression</i>. </p>
<p> See the <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> man page for details on <i>ra-options</i> and <i>expression</i> syntax. </p>
<p> See the <code>ArgusRecord.dtd</code> file for specifics regarding the XML output schema. </p>
<h2>RAXML SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-e</code></p>
<dd> Specify data encoding scheme. Supported options are <code>Ascii</code> and <code>Encode64</code>. </p>
</dl>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8), <code>ArgusRecord.xml,</code> <code>ArgusRecord.dtd,</code> <code>ArgusRecord.sox</code> </p>
<h2>Index</h2>
