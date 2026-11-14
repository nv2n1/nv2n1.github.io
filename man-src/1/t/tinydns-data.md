---
title: "tinydns-data(1)"
name: "tinydns-data"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tinydns-data/"
description: "tinydns-data"
---

<h2 class="name">NAME</h2>
<p> <code>tinydns-data</code></p>
<h2>SYNOPSIS</h2>
<p> <code>tinydns-data</code> [<code>OPTIONS</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>tinydns-data</code> is used to generate the binary file `data.cdb&#8217;, used by <code>tinydns</code> server to answer the user requests. <code>tinydns-data</code> reads the DNS information from a file `data&#8217; in the current directory and writes a binary file data.cdb in the same directory. One can update `data.cdb&#8217; while <code>tinydns</code> is running. <code>tinydns-data</code> leaves the old .cdb file intact in case if something goes wrong while updating data.cdb. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>
&nbsp;<wbr>print this help.</p>
<dt><code>-v &#8211;version</code></p>
<dd>
&nbsp;<wbr>print version information. </p>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>AUTHOR</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
