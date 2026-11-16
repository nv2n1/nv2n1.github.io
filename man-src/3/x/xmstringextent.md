---
title: "xmstringextent(3)"
name: "xmstringextent"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringextent/"
description: "XmStringExtent — A compound string function that determines the size of the smallest rectangle that will enclose the compound string"
---

<p><code>XmStringExtent</code> &#8212; A compound string function that determines the size of the smallest rectangle that will enclose the compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmStringExtent</code>(
<code>XmRenderTable rendertable</code>,
<code>XmString string</code>,
<code>Dimension *width</code>,
<code>Dimension *height</code>);</pre>
<h2>Description</h2>
<p><code>XmStringExtent</code> determines the width and height, in pixels, of the smallest rectangle that will enclose the provided compound string.</p>
<dl COMPACT>
<dt><i>rendertable</i></dt>
<dd>Specifies the render table</dd>
<dt><i>string</i></dt>
<dd>Specifies the string</dd>
<dt><i>width</i></dt>
<dd>Specifies a pointer to the width of the rectangle</dd>
<dt><i>height</i></dt>
<dd>Specifies a pointer to the height of the rectangle</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
