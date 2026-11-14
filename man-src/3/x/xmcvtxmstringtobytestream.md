---
title: "xmcvtxmstringtobytestream(3)"
name: "xmcvtxmstringtobytestream"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtxmstringtobytestream/"
description: "XmCvtXmStringToByteStream — A compound string function that converts a compound string to a Byte Stream format"
---

<p><code>XmCvtXmStringToByteStream</code> &#8212; A compound string function that converts a compound string to a Byte Stream format</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>unsigned int XmCvtXmStringToByteStream</code>(
<code>XmString string</code>,
<code>unsigned char **prop_return</code>);</pre>
<h2>Description</h2>
<p><code>XmCvtXmStringToByteStream</code> converts a compound string to a string of bytes representing the compound string in Byte Stream format. This routine is typically used by the source of a data transfer operation to produce a Byte Stream representation for transferring a compound string to a destination. </p>
<p> If <i>prop_return</i> is not NULL, this function creates a string of characters in Byte Stream format and returns it in <i>prop_return</i>. The function also returns the number of bytes in <i>prop_return</i>. If <i>prop_return</i> is NULL, the function does not return the Byte Stream format string, but it does calculate and return the number of bytes that would appear in the Byte Stream format string.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies a compound string to be converted to Byte Stream format</p>
<dt><i>prop_return</i></p>
<dd>Specifies a pointer to a string in Byte Stream format that is created and returned by this function. If <i>prop_return</i> is NULL, no Byte Stream format string is returned. When a Byte Stream format string is returned, the function allocates space to hold it. The application is responsible for managing this allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</dl>
<h2>Return</h2>
<p>Returns the number of bytes in the Byte Stream representation (whether or not the Byte Stream representation is returned).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3) and <code><a href="/docs/linux/man/3-xmcvtbytestreamtoxmstring/">XmCvtByteStreamToXmString</a></code>(3).</p>
