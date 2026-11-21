---
title: "ldns-compare-zones(1)"
name: "ldns-compare-zones"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-compare-zones/"
description: "ldns-compare-zones – read and compare two zonefiles and print differences"
---

<h2>NAME</h2>
<p> ldns-compare-zones &#8211; read and compare two zonefiles and print differences</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-compare-zones</code> <i>[-c]</i> <i>[-i]</i> <i>[-d]</i> <i>[-z]</i> <i>[-s]</i> <i>ZONEFILE1</i> <i>ZONEFILE2</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-compare-zones</code> reads two DNS zone files and prints number of differences. </p>
<pre>
Output is formated to:
        +NUM_INS        -NUM_DEL        ~NUM_CHG
</pre>
<p> The major comparison is based on the owner name. If an owner name is present in zonefile 1, but not in zonefile 2, the resource records with this owner name are considered deleted, and counted as NUM_DEL. If an owner name is present in zonefile 2, but not in zonefile 1, the resource records with this owner name are considered inserted, and counted as NUM_INS. If an owner name is present in both, but there is a difference in the amount or content of the records, these are considered changed, and counted as NUM_CHG.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> Print resource records whose owner names are in both zone files, but with different resource records. (a.k.a. changed)</dd>
<dt><code>-i</code></dt>
<dd> Print resource records whose owner names are present only in ZONEFILE2 (a.k.a. inserted)</dd>
<dt><code>-d</code></dt>
<dd> Print resource records whose owner names are present only in ZONEFILE1 (a.k.a. deleted)</dd>
<dt><code>-a</code></dt>
<dd> Print all changes. Specifying this option is the same as specifying -c -i amd -d.</dd>
<dt><code>-z</code></dt>
<dd> Suppress zone sorting; this option is not recommended; it can cause records to be incorrectly marked as changed, depending of the nature of the changes.</dd>
<dt><code>-s</code></dt>
<dd> Do not exclude the SOA record from the comparison. The SOA record may then show up as changed due to a new serial number. Off by default since you may be interested to know if (other zone apex elements) have changed.</dd>
<dt><code>-h</code></dt>
<dd> Show usage and exit</dd>
<dt><code>-v</code></dt>
<dd> Show the version and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Ondřej Surý &lt;ondrej [at] sury.org&gt; for CZ.NIC, z.s.p.o. (czech domain registry)</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ondrej [at] sury.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 CZ.NIC, z.s.p.o.. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
