---
title: "xmstringlength(3)"
name: "xmstringlength"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringlength/"
description: "XmStringLength — A compound string function that obtains the length of a compound string"
---

<p><code>XmStringLength</code> &#8212; A compound string function that obtains the length of a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>int XmStringLength</code>(
<code>XmString s1</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringByteStreamLength</code>. <code>XmStringLength</code> obtains the length of a compound string. It returns the number of bytes in <i>s1</i> including all tags, direction indicators, and separators. If the compound string has an invalid structure, 0 (zero) is returned.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string</dl>
<h2>Return</h2>
<p>Returns the length of the compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringbytestreamlength/">XmStringByteStreamLength</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
