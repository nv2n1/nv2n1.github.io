---
title: "tcprules(1)"
name: "tcprules"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcprules/"
---

<h2>SYNOPSIS</h2>
<dl>
<dt><code>tcprules</code> [<code>OPTIONS</code>] &lt;rules.cdb&gt; &lt;rules.tmp&gt;</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>tcprules</code> reads rules from its standard input and writes them into cdb binary format suitable for quick access by <a href="/docs/linux/man/1-tcpserver/">tcpserver</a>(1). <code>tcprules</code> can be used while <a href="/docs/linux/man/1-tcpserver/">tcpserver</a>(1) is running. It ensures that cdb is updated automatically. It does it by first writing the rules to a temporary file and then writing the temporary file to the cdb. If the temporary file already exists, it is destroyed. </p>
<h2>RULE FORMAT</h2>
<p> A rule is one line. A file containing rules may also contain comments beginning with &#8216;#&#8217;. Each rule contains an address, a colon, and a list of instructions, with no extra spaces. When <a href="/docs/linux/man/1-tcpserver/">tcpserver</a>(1) receives a connection from that address, it follows the instruction. <a href="/docs/linux/man/1-tcpserver/">tcpserver</a>(1) uses the first rule it matches. </p>
<p> tcprules treats 1.2.3.37-43:ins as an abbreviation for the rules 1.2.3.37:ins &#8211; 1.2.3.43:ins. Similarly 10.2-3 is an abbreviation for 10.2.:ins and 10.3.:ins. </p>
<p> The instructions in a rule must begin with an allow or deny. deny tells <a href="/docs/linux/man/1-tcpserver/">tcpserver</a>(1) to drop the connection without processing any further. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>
&nbsp;<wbr>print this help </p>
<dt><code>-v &#8211;version</code></p>
<dd>
&nbsp;<wbr>print version information </p>
</dl>
<h2>SEE</h2>
<p> <a rel="nofollow" href="http://cr.yp.to/ucspi-tcp/tcprules.html">http://cr.yp.to/ucspi-tcp/tcprules.html</a> </p>
<h2>BUGS</h2>
<p> Report bugs to &lt;pj.pandit [at] yahoo.co.in&gt; </p>
<h2>Manual Author</h2>
<p> Prasad J Pandit </p>
<h2>Index</h2>
