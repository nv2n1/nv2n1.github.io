---
title: "xmstringcreateltor(3)"
name: "xmstringcreateltor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcreateltor/"
description: "XmStringCreateLtoR — A compound string function that creates a compound string"
---

<p><code>XmStringCreateLtoR</code> &#8212; A compound string function that creates a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringCreateLtoR</code>(
<code>char *text</code>,
<code>char *tag</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringGenerate</code>. <code>XmStringCreateLtoR</code> creates a compound string with two components: text and a tag component. This function scans for <code>
</code> characters in the text. When one is found, the text up to that point is put into a segment followed by a separator component. No final separator component is appended to the end of the compound string. The direction component defaults to left-to-right. This function assumes that the encoding is single byte rather than multibyte. </p>
<p> The function will allocate space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a NULL-terminated string to be used as the text component of the compound string.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag component to be associated with the given text. The value <code>XmFONTLIST_DEFAULT_TAG</code> is retained for compatibility with previous releases.</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringgenerate/">XmStringGenerate</a></code>(3).</p>
