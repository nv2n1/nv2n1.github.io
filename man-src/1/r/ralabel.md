---
title: "ralabel(1)"
name: "ralabel"
section: "1"
letter: "r"
url: "/docs/linux/man/1-ralabel/"
description: "ralabel – inserts fixed form or free form metadata labels into argus(8). ralabel supports a number of strategies for labeling including 1) address based, providing free form metadata, country code,..."
---

<h2>NAME</h2>
<p> <code>ralabel</code> &#8211; inserts fixed form or free form metadata labels into <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code>. <code>ralabel</code> supports a number of strategies for labeling including 1) address based, providing free form metadata, country code, geo data and fully qualified domain name (FQDN) labeling; 2)port based, providing free form labels using IANA port definitions, and 3) flow filter, providing free form labels based on argus filter specicfications. </p>
<h2>SYNOPSIS</h2>
<p> <code>ralabel</code> <code>-f</code> <i>address.file</i> [<code>raoptions</code>] [<code>&#8212;</code> <i>filter-expression</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ralabel</code> reads <code>argus</code> data from an <i>argus-data</i> source, and selects records that include IP addresses specified by the <code>address.spec</code> file. This program provides high performance address matching for any number of addresses. </p>
<h2>RALABEL ADDRESS SPECIFICATION</h2>
<p> Ralabel, reads a number of standard IANA IP address file formats that specific IPv4 addresses, CIDR addresses and IPV4 prefix address specification. Examples of these file types are provided in ./support/Config. </p>
<p> <code><a href="/docs/linux/man/1-ralabel/">ralabel</a>(1)</code> specific options are:</p>
<dl>
<dt><code>-f</code><i> label.strategy.specification.file</i></p>
<dd>
</dl>
<h2>INVOCATION</h2>
<p> This invocation reads <code><a href="/docs/linux/man/8-argus/">argus</a>(8)</code> data from <code>argusfile</code> and labels records that match any options in the <code>ralabel.conf</code> file. </p>
<pre>
 
   <code>ralabel</code> -r argusfile -f ralabel.conf - ip
 
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
