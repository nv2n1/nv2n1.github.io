---
title: "ldns-zcat(1)"
name: "ldns-zcat"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-zcat/"
description: "ldns-zcat – reunite (z)split up a zone files"
---

<h2>NAME</h2>
<p> ldns-zcat &#8211; reunite (z)split up a zone files</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-zcat</code> <i>zonefiles</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-zcat</code> will read in a bunch of (z)split up zonefiles and creates a new larger zone file. The SOA record in the first part is used as the SOA record in the generated zone. </p>
<p> The resulted zone file is printed to standard output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o ORIGIN</code></p>
<dd> use ORIGIN when reading in the zone </p>
<dt><code>-v</code></p>
<dd> show the version number and exit </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005, 2006 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
