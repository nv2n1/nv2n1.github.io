---
title: "echoping_dns(1)"
name: "echoping_dns"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echoping_dns/"
description: "echoping_dns – echoping plugin which queries a DNS server"
---

<h2 class="name">NAME</h2>
<p> echoping_dns &#8211; echoping plugin which queries a DNS server </p>
<h2>SYNOPSIS</h2>
<p> <code>echoping</code> [echoping options] -m dns <code>hostname</code> <code>request</code></p>
<h2>DESCRIPTION</h2>
<p> dns is an echoping plugin, fo testing the performances of DNS (RFC 1034 and 1035) servers.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>request </code></p>
<dd> A domain name</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t, &#8211;type</code></p>
<dd> The type of data requested (NS, A, SOA, etc)</p>
<dt><code>&#8211;no-recurse</code></p>
<dd> Do not request recursive queries</p>
<dt><code>&#8211;tcp</code></p>
<dd> Use only TCP (&quot;virtual circuit&quot;)</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-echoping/">echoping</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> Stephane Bortzmeyer &lt;bortz [at] users.sourceforge.net&gt; </p>
<h2>Index</h2>
