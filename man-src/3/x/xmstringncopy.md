---
title: "xmstringncopy(3)"
name: "xmstringncopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringncopy/"
description: "XmStringNCopy — A compound string function that creates a copy of a compound string"
---

<p><code>XmStringNCopy</code> &#8212; A compound string function that creates a copy of a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringNCopy</code>(
<code>XmString s1</code>,
<code>int num_bytes</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. <code>XmStringNCopy</code> creates a copy of <i>s1</i> that contains a specified number of bytes, including tags, directional indicators, and separators. It then returns the resulting compound string. The original strings are preserved. The function allocates space for the resulting compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes of <i>s1</i> to copy. If this value is less than the length of <i>s1</i>, as many bytes as possible, but possibly fewer than this value, will be appended to <i>s1</i> such that the resulting string is still a valid compound string.</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
