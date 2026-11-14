---
title: "xmstringgetltor(3)"
name: "xmstringgetltor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringgetltor/"
description: "XmStringGetLtoR — A compound string function that searches for a text segment in the input compound string"
---

<p><code>XmStringGetLtoR</code> &#8212; A compound string function that searches for a text segment in the input compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringGetLtoR</code>(
<code>XmString string</code>,
<code>XmStringCharSet tag</code>,
<code>char **text</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmStringUnparse</code>. <code>XmStringGetLtoR</code> returns the first text component in the input compound string that is tagged with the given tag component. The returned text is to be a NULL-terminated sequence of single byte characters. If the function returns True, the function will allocate space to hold the returned <i>text</i>. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the compound string.</p>
<dt><i>tag</i></p>
<dd>Specifies the font list element tag associated with the text. A value of <code>XmFONTLIST_DEFAULT_TAG</code> identifies a locale text segment.</p>
<dt><i>text</i></p>
<dd>Specifies a pointer to a NULL terminated string.</dl>
<h2>Return</h2>
<p>Returns True if the matching text segment can be found. On return, <i>text</i> will have a NULL terminated byte sequence containing the matched segment.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
