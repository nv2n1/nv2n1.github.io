---
title: "ldns-update(1)"
name: "ldns-update"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-update/"
description: "ldns-update – send a dynamic update packet"
---

<h2>NAME</h2>
<p> ldns-update &#8211; send a dynamic update packet</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-update </code> [ <i>zone</i> ] <i>ip</i> [ <i>tsig_name</i> <i>tsig_als</i> <i>tsig_hmac</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-update</code> is used to send a dynamic update packet. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>zone</code></p>
<dd> Use this zone instead of trying to read it from the zonefile&#8217;s SOA record. </p>
<dt><code>ip</code></p>
<dd> Send the update to this IP address </p>
<dt><code>tsig_name tsig_alg tsig_hmac</code></p>
<dd> Use TSIG (rfc2845) to authenticate. </p>
</dl>
<h2>EXAMPLE</h2>
<p> ldns-update my.example.org 1.2.3.4 </p>
<h2>AUTHOR</h2>
<p> Written by Jakob Schlyter and Håkan Olsson, as an addition to the ldns library from NLnet Labs. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
