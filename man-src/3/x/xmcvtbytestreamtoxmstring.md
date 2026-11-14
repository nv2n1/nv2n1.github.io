---
title: "xmcvtbytestreamtoxmstring(3)"
name: "xmcvtbytestreamtoxmstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcvtbytestreamtoxmstring/"
description: "XmCvtByteStreamToXmString — A compound string function that converts from a compound string in Byte Stream format to a compound string"
---

<p><code>XmCvtByteStreamToXmString</code> &#8212; A compound string function that converts from a compound string in Byte Stream format to a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmCvtByteStreamToXmString</code>(
<code>unsigned char *property</code>);</pre>
<h2>Description</h2>
<p><code>XmCvtByteStreamToXmString</code> converts a stream of bytes representing a compound string in Byte Stream format to a compound string. This routine is typically used by the destination of a data transfer operation to produce a compound string from a transferred Byte Stream representation.</p>
<dl COMPACT>
<dt><i>property</i></p>
<dd>Specifies a compound string representation in Byte Stream format.</dl>
<h2>Return</h2>
<p>Returns a compound string. The function allocates space to hold the returned compound string. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmcvtxmstringtobytestream/">XmCvtXmStringToByteStream</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
