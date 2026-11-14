---
title: "tinydns(8)"
name: "tinydns"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tinydns/"
description: "tinydns – DNS server."
---

<p><code>tinydns</code> &#8211; DNS server.</p>
<h2>Synopsis</h2>
<p><code>tinydns</code> [<code>OPTIONS</code>] </p>
<h2>Description</h2>
<p><code>tinydns</code> is a DNS server that answers DNS queries from other hosts with locally configured information. When invoked, <code>tinydns</code> reads from the configuration file and listens on UDP port 53 for the incoming requests. When a request is received, <code>tinydns</code> answers it by looking into `data.cdb&#8217; file placed under the ROOT directory specified in the configuration file. Until version 1.05.8, <code>tinydns</code> used to read from `data.cdb&#8217; for each request it received and responded to. From version 1.05.9, <code>tinydns</code> reads `data.cdb&#8217; only ones at the beginning and later when signalled for the same via SIGUSR1. </p>
<h2>Options</h2>
<dl>
<dt><code>-d &lt;value&gt;</code></p>
<dd>&nbsp;<wbr>print debug messages as per the debug level 1, 2 or 3.</p>
<dt><code>-D</code></p>
<dd>&nbsp;<wbr>run as a daemon.</p>
<dt><code>-h &#8211;help</code></p>
<dd>&nbsp;<wbr>print this help.</p>
<dt><code>-v &#8211;version</code></p>
<dd>&nbsp;<wbr>print version information. </p>
</dl>
<h2>Signals</h2>
<p>SIGUSR1 &#8211; reload information from data.cdb file.</p>
<h2>Files</h2>
<p>&nbsp;<wbr>/etc/ndjbdns/tinydns.conf </p>
<p>&nbsp;<wbr>/var/log/tinydnsd.log</p>
<h2>Bugs</h2>
<p>Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Author</h2>
<p>Prasad J Pandit</p>
