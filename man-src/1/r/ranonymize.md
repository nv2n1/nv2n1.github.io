---
title: "ranonymize(1)"
name: "ranonymize"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ranonymize/"
description: "ranonymize – anonymize argus(8) data fields."
---

<h2>NAME</h2>
<p> <code>ranonymize</code> &#8211; anonymize <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data fields.</p>
<h2>SYNOPSIS</h2>
<p> <code>ranonymize [-f anonymize.conf</code>] [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ranonymize</code> reads <code>argus</code> data from an <i>argus-data</i> source, strips out specific fields, and anonymizes the remaining fields in Argus records, including the network addresses, protocol specific port numbers, timestamps, transaction reference numbers, TCP base sequence numbers, IP identifiers, and any record sequence numbers. </p>
<p> Anonymization is controlled through an anonymization configuration file. See <code><a href="/docs/linux/man/5-ranonymize/">ranonymize</a>(5)</code> for a complete description. </p>
<h2>OPTIONS</h2>
<p> Ranonymize, shares all the same options as <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code>. See <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code> for a complete description of <code>ra options</code>. <code><a href="/docs/linux/man/1-ranonymize/">ranonymize</a>(1)</code> specific options are: </p>
<dl>
<dt><code>-f</code></p>
<dd> anonymization.confile </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2016 QoSient. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ra/">ra</a>(1),</code> <code><a href="/docs/linux/man/5-rarc/">rarc</a>(5),</code> <code><a href="/docs/linux/man/5-ranonymize/">ranonymize</a>(5),</code></p>
<h2>FILES</h2>
<h2>AUTHORS</h2>
<pre>
Carter Bullard (carter [at] qosient.com).
</pre>
<h2>BUGS</h2>
<h2>Index</h2>
