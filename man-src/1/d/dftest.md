---

title: "dftest(1)"
name: "dftest"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dftest/"
description: "dftest – Shows display filter byte-code, for debugging dfilter routines."
---

<p> <code>dftest</code> [&nbsp;<wbr>&lt;filter&gt;&nbsp;<wbr>]</p>
<p> <code>dftest</code> is a simple tool which compiles a display filter and shows its bytecode.</p>
<h2>OPTIONS</h2>
<dl>
<dt>filter</dt>
<dd> The display filter expression. If needed it has to be quoted.</dd></dl>
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
