---
title: "xmstringbaseline(3)"
name: "xmstringbaseline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringbaseline/"
description: "XmStringBaseline — A compound string function that returns the number of pixels between the top of the character box and the baseline of the first line of text"
---

<p><code>XmStringBaseline</code> &#8212; A compound string function that returns the number of pixels between the top of the character box and the baseline of the first line of text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Dimension XmStringBaseline</code>(
<code>XmRenderTable rendertable</code>,
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringBaseline</code> returns the number of pixels between the top of the character box and the baseline of the first line of text in the provided compound string.</p>
<dl COMPACT>
<dt><i>rendertable</i></p>
<dd>Specifies the render table</p>
<dt><i>string</i></p>
<dd>Specifies the string</dl>
<h2>Return</h2>
<p>Returns the number of pixels between the top of the character box and the baseline of the first line of text.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
