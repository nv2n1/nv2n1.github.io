---
title: "xmstringseparatorcreate(3)"
name: "xmstringseparatorcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringseparatorcreate/"
description: "XmStringSeparatorCreate — A compound string function that creates a compound string"
---

<p><code>XmStringSeparatorCreate</code> &#8212; A compound string function that creates a compound string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringSeparatorCreate</code>(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmStringSeparatorCreate</code> creates a compound string with a single component, a separator.</p>
<h2>Return</h2>
<p>Returns a new compound string. When the application no longer needs the returned compound string, the application should call <code>XmStringFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
