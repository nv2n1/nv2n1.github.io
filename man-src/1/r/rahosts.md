---
title: "rahosts(1)"
name: "rahosts"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rahosts/"
description: "rahosts – report network addresses in argus(8) data."
---

<h2>NAME</h2>
<p> <code>rahosts</code> &#8211; report network addresses in <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2003 QoSient. All rights reserved.</p>
<h2>SYNOPSIS</h2>
<p> <code>rahosts</code> [ra-options] <code>-M modes</code> [ <i>expression</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rahosts</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus data</i> source, and outputs a list of sorted network addresses. Based on user supplied criteria, <code>rahosts</code> can generate lists of IP addresses and/or MAC addresses, if available. With IP addresses, <code>rahosts</code> can track the full network and host address, or any network address, based on the <i>mode</i> indicated. </p>
<p> Like all ra based clients, <code>rahosts </code> supports a large number of options, configuration through .rarc files, and input filtering using the terminating filter <i>expression</i>. </p>
<p> See the <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> man page for details on <i>ra-options</i> and <i>expression</i> syntax. </p>
<h2>RAHOSTS SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-M mode</code></p>
<dd> Specify mode of operation. Supported address modes are <code>ip</code>, <code>ether</code> and <code>all</code> address types. The default is to output <i>IP</i> addresses. When IP Addresses are being processed, the network address can be specified with the additional <i>modes</i> <code>class</code>, <code>classA</code>, <code>classB</code> and <code>classC</code>. </p>
</dl>
<h2>EXAMPLES</h2>
<p> By default, <code>rahosts</code> will output the unique IP addresses seen in an argus data stream. Using the -M mode options you can output all unique class B network addresses that access the server narly.wave.com:</p>
<dl>
<dt>
<dd>
<pre>
<code>rahosts -r argus.data -M classB host narly.wave.com</code>
</pre>
</dl>
<p> Print the <i>ethernet</i> addresses used to support the HTTP service.</p>
<dl>
<dt>
<dd>
<pre>
<code>rahosts -r argus.data -M ether dst port http
</code></pre>
</dl>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), </p>
<h2>Index</h2>
