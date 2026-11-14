---
title: "xmrendertablecvttoprop(3)"
name: "xmrendertablecvttoprop"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertablecvttoprop/"
description: "XmRenderTableCvtToProp — A render table function that converts a render table to a string representation"
---

<p><code>XmRenderTableCvtToProp</code> &#8212; A render table function that converts a render table to a string representation</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>unsigned int XmRenderTableCvtToProp</code>(
<code>Widget widget</code>,
<code>XmRenderTable table</code>,
<code>char **prop_return</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableCvtToProp</code> converts a render table to a string of characters representing the render table. This routine is typically used by the source of a data transfer operation to produce a representation for transferring a render table to a destination.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget that is the source of the render table</p>
<dt><i>table</i></p>
<dd>Specifies a render table to be converted</p>
<dt><i>prop_return</i></p>
<dd>Specifies a pointer to a string that is created and returned by this function. The function allocates space to hold the returned string. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XtFree</code>.</dl>
<h2>Return</h2>
<p>Returns the number of bytes in the string representation.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) and <code><a href="/docs/linux/man/3-xmrendertablecvtfromprop/">XmRenderTableCvtFromProp</a></code>(3).</p>
