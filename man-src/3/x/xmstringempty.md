---
title: "xmstringempty(3)"
name: "xmstringempty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringempty/"
description: "XmStringEmpty — A compound string function that provides information on the existence of non-zero-length text components"
---

<p><code>XmStringEmpty</code> &#8212; A compound string function that provides information on the existence of non-zero-length text components</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringEmpty</code>(
<code>XmString s1</code>);</pre>
<h2>Description</h2>
<p><code>XmStringEmpty</code> returns a Boolean value indicating whether any non-zero-length text components exist in the provided compound string. It returns True if there are no text segments in the string. If this routine is passed NULL as the string, it returns True.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string</dl>
<h2>Return</h2>
<p>Returns True if there are no text segments in the string. If this routine is passed NULL as the string, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
