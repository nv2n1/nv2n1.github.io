---
title: "xmstringbytestreamlength(3)"
name: "xmstringbytestreamlength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringbytestreamlength/"
description: "XmStringByteStreamLength — A function that returns the size of a string"
---

<p><code>XmStringByteStreamLength</code> &#8212; A function that returns the size of a string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
unsigned int XmStringByteStreamLength (<i>string</i>)
 unsigned char *<i>string</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmStringByteStreamLength</code> receives a byte stream format string and returns the size, in bytes, of that stream, including the header. Because of this header information, even a NULL <i>string</i> will cause <code>XmStringByteStreamLength</code> to return a non-zero value.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the byte stream format string.</dl>
<h2>Return Values</h2>
<p>Returns the size of <i>string</i>, including the header.</p>
