---
title: "walldns(8)"
name: "walldns"
section: "8"
letter: "w"
url: "/docs/linux/man/8-walldns/"
description: "walldns – a reverse DNS wall."
---

<p><code>walldns</code> &#8211; a reverse DNS wall.</p>
<h2>Synopsis</h2>
<p><code>walldns</code> [<code>OPTIONS</code>] </p>
<h2>Description</h2>
<p><code>walldns</code> is a reverse DNS wall. It accepts requests on UDP port 53. The DNS queries are for the `in-addr.arpa&#8217; domain. Walldns rejects inverse queries, non-internet class queries, truncated packets, packets that contain anything other than a single question, queries for domains outside in-addr.arpa and requests types other than A, PTR, and *. </p>
<h2>Options</h2>
<dl>
<dt><code>-d &lt;value&gt;</code></p>
<dd>&nbsp;<wbr>print debug messages as per debug level: 1, 2, or 3</p>
<dt><code>-D</code></p>
<dd>&nbsp;<wbr>run as a daemon</p>
<dt><code>-h &#8211;help</code></p>
<dd>&nbsp;<wbr>print this help</p>
<dt><code>-v &#8211;version</code></p>
<dd>&nbsp;<wbr>print version information </p>
</dl>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/ndjbdns/walldns.conf </p>
<p>&nbsp;<wbr>/var/log/walldns.log</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Author</h2>
<p>Prasad J Pandit</p>
