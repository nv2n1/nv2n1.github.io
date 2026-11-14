---
title: "rbldns-data(1)"
name: "rbldns-data"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rbldns-data/"
description: "rbldns-data"
---

<h2 class="name">NAME</h2>
<p> <code>rbldns-data</code></p>
<h2>SYNOPSIS</h2>
<p> <code>rbldns-data</code> [<code>OPTIONS</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>rbldns-data</code> is used to generate the binary file `data.cdb&#8217;, used by <code>rbldns</code> server to answer the user requests. <code>rbldns-data</code> reads the Real time Block List(RBL) or Dialup Users List(DUL) information from a file called `data&#8217; in the current directory and writes a binary file `data.cdb&#8217; in the same directory. One can update `data.cdb&#8217; while <code>rbldns</code> is running. <code>rbldns-data</code> leaves the old .cdb file intact in case if something goes wrong while updating data.cdb. </p>
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
