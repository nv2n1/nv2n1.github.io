---
title: "rafilteraddr(1)"
name: "rafilteraddr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rafilteraddr/"
description: "rafilteraddr – select argus(8) data based on an IANA IP address file."
---

<h2>NAME</h2>
<p> <code>rafilteraddr</code> &#8211; select <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data based on an IANA IP address file.</p>
<h2>SYNOPSIS</h2>
<p> <code>rafilteraddr</code> <code>[-f</code> <i>address.file</i> [<code> [-v] [raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Rafilteraddr</code> reads <code>argus</code> data from an <i>argus-data</i> source, and selects records that include IP addresses specified by the <code>address.spec</code> file. This program provides high performance address matching for any number of addresses. </p>
<h2>RAFILTERADDR ADDRESS SPECIFICATION</h2>
<p> Rafilteraddr, reads a number of standard IANA IP address file formats that specify IPv4, CIDR and IPV4 prefix addresses. Examples of these file types are provided in ./support/Config. </p>
<p> <code><a href="/docs/linux/man/1-rafilteraddr/">rafilteraddr</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-f &lt;IPv4 address specification&gt;&gt;</code></p>
<dd> Specify the list of addresses used for the address filter. This file can be in several IANA based address specification formats, and is the same format as the address labels for <code>ralabel.1</code>. </p>
<dt><code>-v</code></p>
<dd> Invert the logic and print flows that don&#8217;t match any of the addresses. </p>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>argusfile</code> and prints records that match any of the IP addresses in the iana-ipv4-addresses. </p>
<pre>
 
   <code>rafilteraddr</code> -r argusfile -f iana-ipv4-addresses -- ip
 
</pre>
<p> An example address specification that describes a mix of CIDR addresses, IPv4 address ranges and explicit addresses: </p>
<pre>
  192.168.0.0/24
  192.168.1.3-192.168.2.45
  207.237.36.98
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved. </p>
<h2>SEE ALSO</h2>
<p> <code>ralabel.conf.5,</code> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/8-argus/">argus</a>(8),</code> </p>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>Index</h2>
