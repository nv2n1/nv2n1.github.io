---
title: "ldns-revoke(1)"
name: "ldns-revoke"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-revoke/"
description: "ldns-revoke – sets the revoke bit of a DNSKEY"
---

<h2>NAME</h2>
<p> ldns-revoke &#8211; sets the revoke bit of a DNSKEY</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-revoke</code> <i>file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-revoke</code> is used to revoke a public DNSKEY RR. When run it will read <i>file</i> with a DNSKEY RR in it, sets the revoke bit and write back the output to <i>file</i> . </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd> Write the result to stdout instead of a file </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
