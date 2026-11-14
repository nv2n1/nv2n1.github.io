---
title: "ldns-key2ds(1)"
name: "ldns-key2ds"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-key2ds/"
description: "ldns-key2ds – transform a DNSKEY RR to a DS RR"
---

<h2>NAME</h2>
<p> ldns-key2ds &#8211; transform a DNSKEY RR to a DS RR</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-key2ds </code> <i>file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-key2ds</code> is used to transform a public DNSKEY RR to a DS RR. When run it will read <i>file</i> with a DNSKEY RR in it and it will create a .ds file with the DS RR in it. </p>
<p> It prints out the basename for this file (K&lt;name&gt;+&lt;alg&gt;+&lt;id&gt;). </p>
<p> By default it takes a pick of algorithm similar to the key algorithm, SHA1 for RSASHA1, and so on. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Ignore SEP flag (i.e. make DS records for any key) </p>
<dt><code>-n</code></p>
<dd> Write the result DS Resource Record to stdout instead of a file </p>
<dt><code>-1</code></p>
<dd> Use SHA1 as the hash function. </p>
<dt><code>-2</code></p>
<dd> Use SHA256 as the hash function </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
