---
title: "xmrendertablecvtfromprop(3)"
name: "xmrendertablecvtfromprop"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertablecvtfromprop/"
description: "XmRenderTableCvtFromProp — A render table function that converts from a string representation to a render table"
---

<p><code>XmRenderTableCvtFromProp</code> &#8212; A render table function that converts from a string representation to a render table</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRenderTable XmRenderTableCvtFromProp</code>(
<code>Widget widget</code>,
<code>char *property</code>,
<code>unsigned int length</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableCvtFromProp</code> converts a string of characters representing a render table to a render table. This routine is typically used by the destination of a data transfer operation to produce a render table from a transferred representation.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget that is the destination for the render table</p>
<dt><i>property</i></p>
<dd>Specifies a string of characters representing a render table</p>
<dt><i>length</i></p>
<dd>Specifies the number of bytes in <i>property</i></dl>
<h2>Return</h2>
<p>Returns a render table. The function allocates space to hold the returned render table. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XmRenderTableFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablecvttoprop/">XmRenderTableCvtToProp</a></code>(3), and <code><a href="/docs/linux/man/3-xmrendertablefree/">XmRenderTableFree</a></code>(3).</p>
