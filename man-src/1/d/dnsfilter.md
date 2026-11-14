---
title: "dnsfilter(1)"
name: "dnsfilter"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnsfilter/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>dnsfilter</code> [<code>OPTIONS</code>]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>dnsfilter</code> does the opposite of dnsip. It inverse queries the DNS to convert a given IP address to the corresponding host name. When a query returns the host name, <code>dnsfilter</code> prints the result as </p>
<p> &lt;ip-address&gt;=&lt;host-name&gt; </p>
<p> and in case of any error it goes like </p>
<p> &lt;ip-address&gt;:&lt;error-message&gt; </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &lt;number&gt;</code></p>
<dd>
&nbsp;<wbr>do&nbsp;<wbr>&lt;number&gt;&nbsp;<wbr>queries in parallel</p>
<dt><code>-h &#8211;help</code></p>
<dd>
&nbsp;<wbr>print this help</p>
<dt><code>-l &lt;number&gt;</code></p>
<dd>
&nbsp;<wbr>read ahead at most&nbsp;<wbr>&lt;number&gt;&nbsp;<wbr>lines</p>
<dt><code>-v &#8211;version</code></p>
<dd>
&nbsp;<wbr>print version information </p>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>AUTHOR</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
