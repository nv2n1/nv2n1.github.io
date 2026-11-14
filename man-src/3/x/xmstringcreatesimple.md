---
title: "xmstringcreatesimple(3)"
name: "xmstringcreatesimple"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcreatesimple/"
description: "XmStringCreateSimple — A compound string function that creates a compound string in the language environment of a widget"
---

<p><code>XmStringCreateSimple</code> &#8212; A compound string function that creates a compound string in the language environment of a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringCreateSimple</code>(
<code>char * text</code>);</pre>
<h2>Description</h2>
<p><code>XmStringCreateSimple</code> creates a compound string with a text component and a charset tag. It derives the character set from the current language environment. </p>
<p> The routine attempts to derive a character set from the value of the LANG environment variable. If this does not result in a valid character set, the routine uses a vendor-specific default. If the vendor has not specified a different value, this default is ISO8859-1. </p>
<p> The function will allocate space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>. </p>
<p> <code>NOTE:</code> This routine is obsolete and exists for compatibility with previous releases. It has been replaced by <code>XmStringCreateLocalized</code>.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a NULL-terminated string to be used as the text component of the compound string.</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringcreatelocalized/">XmStringCreateLocalized</a></code>(3).</p>
