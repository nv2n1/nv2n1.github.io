---
title: "dftest(1)"
name: "dftest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dftest/"
description: "dftest – Shows display filter byte-code, for debugging dfilter routines."
---

<h2 class="name">NAME</h2>
<p> dftest &#8211; Shows display filter byte-code, for debugging dfilter routines. </p>
<h2>SYNOPSIS</h2>
<p> <code>dftest</code> [&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dftest</code> is a simple tool which compiles a display filter and shows its bytecode.</p>
<h2>OPTIONS</h2>
<dl>
<dt>filter</p>
<dd> The display filter expression. If needed it has to be quoted.</dl>
<h2>EXAMPLES</h2>
<p> Show how the <font SIZE="-1">IP</font> protocol is filtered: </p>
<pre>
    dftest ip
</pre>
<p> Shows how frame 150 is filtered: </p>
<pre>
    dftest &quot;frame.number == 150&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/4-wireshark-filter/">wireshark-filter</a></i>(4) </p>
<h2>Index</h2>
