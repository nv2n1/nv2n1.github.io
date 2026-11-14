---
title: "xmstringcopy(3)"
name: "xmstringcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcopy/"
description: "XmStringCopy — A compound string function that makes a copy of a string"
---

<p><code>XmStringCopy</code> &#8212; A compound string function that makes a copy of a string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringCopy</code>(
<code>XmString s1</code>);</pre>
<h2>Description</h2>
<p><code>XmStringCopy</code> makes a copy of an existing compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string to be copied</dl>
<h2>Return</h2>
<p>Returns a compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
