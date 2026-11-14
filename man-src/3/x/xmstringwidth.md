---
title: "xmstringwidth(3)"
name: "xmstringwidth"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringwidth/"
description: "XmStringWidth — A compound string function that returns the width of the widest line in a compound string"
---

<p><code>XmStringWidth</code> &#8212; A compound string function that returns the width of the widest line in a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Dimension XmStringWidth</code>(
<code>XmRenderTable rendertable</code>,
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringWidth</code> returns the width, in pixels, of the widest line in the provided compound string.</p>
<dl COMPACT>
<dt><i>rendertable</i></p>
<dd>Specifies the render table</p>
<dt><i>string</i></p>
<dd>Specifies the string</dl>
<h2>Return</h2>
<p>Returns the width of the compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
