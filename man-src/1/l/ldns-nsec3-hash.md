---
title: "ldns-nsec3-hash(1)"
name: "ldns-nsec3-hash"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-nsec3-hash/"
description: "ldns-nsec3-hash – print out the NSEC3 hash for a domain name"
---

<h2>NAME</h2>
<p> ldns-nsec3-hash &#8211; print out the NSEC3 hash for a domain name</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-nsec3-hash</code> <i>&lt;domain_name&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-nsec3-hash</code> is used to print out the NSEC3 hash for the given domain name. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code> <i>number</i></p>
<dd> Use the given algorithm number for the hash calculation. Defaults to 1 (SHA-1). </p>
<dt><code>-s</code> <i>salt</i></p>
<dd> Use the given salt for the hash calculation. Salt value should be in hexadecimal format. </p>
<dt><code>-t</code> <i>count</i></p>
<dd> Use count iterations for the hash calculation. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
