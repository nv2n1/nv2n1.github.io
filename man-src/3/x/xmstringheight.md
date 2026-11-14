---
title: "xmstringheight(3)"
name: "xmstringheight"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringheight/"
description: "XmStringHeight — A compound string function that returns the line height of the given compound string"
---

<p><code>XmStringHeight</code> &#8212; A compound string function that returns the line height of the given compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Dimension XmStringHeight</code>(
<code>XmRenderTable rendertable</code>,
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringHeight</code> returns the height, in pixels, of the sum of all the line heights of the given compound string. Separator components delimit lines.</p>
<dl COMPACT>
<dt><i>rendertable</i></p>
<dd>Specifies the render table</p>
<dt><i>string</i></p>
<dd>Specifies the string</dl>
<h2>Return</h2>
<p>Returns the height of the specified string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
