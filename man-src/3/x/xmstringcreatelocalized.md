---
title: "xmstringcreatelocalized(3)"
name: "xmstringcreatelocalized"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcreatelocalized/"
description: "XmStringCreateLocalized — A compound string function that creates a compound string in the current locale"
---

<p><code>XmStringCreateLocalized</code> &#8212; A compound string function that creates a compound string in the current locale</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringCreateLocalized</code>(
<code>char *text</code>);</pre>
<h2>Description</h2>
<p><code>XmStringCreateLocalized</code> creates a compound string containing the specified text in the current language environment. An identical compound string would result from the function <code>XmStringCreate</code> called with <code>XmFONTLIST_DEFAULT_TAG</code> explicitly as the tag component. </p>
<p> The function will allocate space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>text</i></p>
<dd>Specifies a NULL-terminated string of text encoded in the current language environment to be used as the text component of the compound string</dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
