---
title: "xmstringisvoid(3)"
name: "xmstringisvoid"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringisvoid/"
description: "XmStringIsVoid — A compound string function that provides information on the existence of non-zero-length text components, tab components, or separator components"
---

<p><code>XmStringIsVoid</code> &#8212; A compound string function that provides information on the existence of non-zero-length text components, tab components, or separator components</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringIsVoid</code>(
<code>XmString s1</code>);</pre>
<h2>Description</h2>
<p><code>XmStringIsVoid</code> returns a Boolean value indicating whether or not string <i>s1</i> is void.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string</dl>
<h2>Return</h2>
<p>Returns True if any non-zero-length text components, tab components, or separator components exist in <i>s1</i>. That is, the function returns True if the string has no text, tabs, or separators. If <i>s1</i> contains the NULL string, the function returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
