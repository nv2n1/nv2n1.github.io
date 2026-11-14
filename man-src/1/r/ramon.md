---
title: "ramon(1)"
name: "ramon"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ramon/"
description: "ramon – provide RMON2 style reports from argus(8) data."
---

<h2>NAME</h2>
<p> <code>ramon</code> &#8211; provide RMON2 style reports from <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2003 QoSient. All rights reserved.</p>
<h2>SYNOPSIS</h2>
<p> <code>ramon</code> [ra-options] <code>-M (TopN | Matrix | HostProto | HostSvc | Svc) [-M Net/masklen] </code> [ <i>expression</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ramon</code> reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from an <i>argus data</i> source, aggregates the records, sorts them based on user supplied criteria and generates modified argus data that supports RMON2 style tables and data reporting. </p>
<p> <code>Ramon</code> supports the same sorting capabilites and calling syntax as <code>rasort()</code> for specifying the sorting algorithm and order. </p>
<p> The output is valid argus data, and can be operated on using any ra*() program. </p>
<p> Like all ra based clients, <code>ramon </code> supports a large number of options, configuration through .rarc files, and input filtering using the terminating filter <i>expression</i>. </p>
<p> See the <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> man page for details on <i>ra-options</i> and <i>expression</i> syntax. </p>
<h2>RAMON SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-M TopN</code></p>
<dd> Generate the top N list of network addresses and supply the incoming and outgoing packet and bytes counts. The addresses can be modified using the -M Net mode in addition to this mode.</p>
<dt><code>-M Matrix</code></p>
<dd> Generate the list of talkers ( A &lt;-&gt; B) and supply the incoming and outgoing packet and byte counts. The talker addresses can be modified using the -M Net mode.</p>
<dt><code>-M HostProto</code></p>
<dd> Generate the list of protocols that are being used by each address and supply the incoming and outgoing packet and byte counts seen.</p>
<dt><code>-M HostSvc</code></p>
<dd> Generate the list of services that are being used by each address and supply the incoming and outgoing packet and byte counts seen.</p>
<dt><code>-M Svc</code></p>
<dd> Generate the list of services (dst port number) and supply the incoming and outgoing packet and byte counts seen.</p>
<dt><code>-M Net[/masklen]</code></p>
<dd> Track addresses as networks rather than host addresses. If the option masklen is not provided, the addresses are traced as subnets based on their Class network address.</p>
<dt><code>-a</code></p>
<dd> Don&#8217;t filter output to match expression filter. This generates the complete set of addresses/nets that contributed to the inbound and outbound metrics. </p>
</dl>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a></code>(1), <code><a href="/docs/linux/man/1-rasort/">rasort</a></code>(1), <code><a href="/docs/linux/man/5-rarc/">rarc</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8), </p>
<h2>Index</h2>
