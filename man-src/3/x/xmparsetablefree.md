---
title: "xmparsetablefree(3)"
name: "xmparsetablefree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmparsetablefree/"
description: "XmParseTableFree — A compound string function that recovers memory"
---

<p><code>XmParseTableFree</code> &#8212; A compound string function that recovers memory</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmParseTableFree</code>(
<code>XmParseTable parse_table</code>,
<code>Cardinal count</code>);</pre>
<h2>Description</h2>
<p><code>XmParseTableFree</code> recovers memory used by an <code>XmParseTable</code> and its constituent <code>XmParseMapping</code>s.</p>
<dl COMPACT>
<dt><i>parse_table</i></p>
<dd>Specifies the parse table to be freed</p>
<dt><i>count</i></p>
<dd>Specifies the number of parse mappings in the parse table</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmparsetable/">XmParseTable</a></code>(3) and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
