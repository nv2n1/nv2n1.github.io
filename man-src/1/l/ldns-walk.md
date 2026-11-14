---
title: "ldns-walk(1)"
name: "ldns-walk"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-walk/"
description: "ldns-walk – Retrieve the contents of a DNSSEC signed zone"
---

<h2>NAME</h2>
<p> ldns-walk &#8211; Retrieve the contents of a DNSSEC signed zone</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-walk</code> [ <i>OPTION</i> ] <i>ZONE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-walk</code> is used to retrieve the contents of a DNSSEC signed zone. It does this through NSEC-walking (following the chain of NSEC records) and &#8216;guessing&#8217; the next non-existent owner name for each NSEC. </p>
<p> Note that it might get stuck on some wildcard records when used through a caching forwarder. This problem can be circumvented by querying the authoritative nameserver directly (with the @ argument). </p>
<p> Of course the nameserver that is used must be DNSSEC-aware. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> Use only IPv4. </p>
<dt><code>-6</code></p>
<dd> Use only IPv6. </p>
<dt><code>-f</code></p>
<dd> Do a &#8216;full&#8217; zone walk; by default, ldns-walk will only show the names, and types present at those names. If this option is given, all resource records will be printed. </p>
<dt><code>-s</code> <i>name</i></p>
<dd> Start the walk with this owner name. Useful when continuing the walk for a large zone. </p>
<dt><code>-v</code> <i>verbosity</i></p>
<dd> Verbosity level [1-5]. </p>
<dt><code>@</code> <i>nameserver</i></p>
<dd> Send the queries to this nameserver. </p>
</dl>
<h2>BUGS</h2>
<p> The full zone walk function is not complete yet, it does not correctly print delegation records </p>
<h2>AUTHOR</h2>
<p> Written by Jelte Jansen as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
