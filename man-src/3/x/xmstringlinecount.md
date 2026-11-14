---
title: "xmstringlinecount(3)"
name: "xmstringlinecount"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringlinecount/"
description: "XmStringLineCount — A compound string function that returns the number of separators plus one in the provided compound string"
---

<p><code>XmStringLineCount</code> &#8212; A compound string function that returns the number of separators plus one in the provided compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>int XmStringLineCount</code>(
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringLineCount</code> returns the number of separators plus one in the provided compound string. In effect, it counts the lines of text.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the string</dl>
<h2>Return</h2>
<p>Returns the number of lines in the compound string. If <i>string</i> is empty, the function returns 1. If NULL is passed into <i>string</i>, the function returns 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
