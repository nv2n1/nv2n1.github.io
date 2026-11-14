---
title: "xmstringnconcat(3)"
name: "xmstringnconcat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringnconcat/"
description: "XmStringNConcat — A compound string function that appends a specified number of bytes to a compound string"
---

<p><code>XmStringNConcat</code> &#8212; A compound string function that appends a specified number of bytes to a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringNConcat</code>(
<code>XmString s1</code>,
<code>XmString s2</code>,
<code>int num_bytes</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringConcat</code>. <code>XmStringNConcat</code> appends a specified number of bytes from <i>s2</i> to the end of <i>s1</i>, including tags, directional indicators, and separators. It then returns the resulting compound string. The original strings are preserved. The function allocates space for the resulting compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string to which a copy of <i>s2</i> is appended.</p>
<dt><i>s2</i></p>
<dd>Specifies the compound string that is appended to the end of <i>s1</i>.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes of <i>s2</i> to append to <i>s1</i>. If this value is less than the length of <i>s2</i>, as many bytes as possible, but possibly fewer than this value, will be appended to <i>s1</i> such that the resulting string is still a valid compound string.</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
