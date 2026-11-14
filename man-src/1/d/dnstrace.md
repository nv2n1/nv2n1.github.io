---
title: "dnstrace(1)"
name: "dnstrace"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dnstrace/"
---

<h2>SYNOPSIS</h2>
<p> <code>dnstrace</code> [OPTIONS] &lt;TYPE&gt; &lt;DOMAIN-NAME&gt; &lt;ROOT-IP&gt; [&lt;ROOT-IP&gt; &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>dnstrace</code> is a useful debugging tool to search for all DNS servers that can affect the resolution of records of given &lt;TYPE&gt; under the give &lt;DOMAIN-NAME&gt; starting from the root name server &lt;ROOT-IP&gt;. <code>dnstrace</code> uses the standard DNS resolution algorithm but follows all possible paths in the algorithm. It prints all responses it receives from the DNS servers. It also prints warnings about slow servers, dead servers, misdelegated servers and misformatted packets. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>dnstrace A google.com 127.0.0.1 | dnstrcesort </p>
<p> One can use the <code>dnstracesort</code> in conjunction with the <code>dnstrace</code>. It produces more human friendly sorted output. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>
&nbsp;<wbr>print this help</p>
<dt><code>-v &#8211;version</code></p>
<dd>
&nbsp;<wbr>print version information </p>
</dl>
<h2>SEE</h2>
<p> <a rel="nofollow" href="http://cr.yp.to/djbdns/debugging.html">http://cr.yp.to/djbdns/debugging.html</a> </p>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Manual Author</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
