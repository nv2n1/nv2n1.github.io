---
title: "xmstringfree(3)"
name: "xmstringfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringfree/"
description: "XmStringFree — A compound string function that conditionally deallocates memory"
---

<p><code>XmStringFree</code> &#8212; A compound string function that conditionally deallocates memory</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmStringFree</code>(
<code>XmString string</code>);</pre>
<h2>Description</h2>
<p><code>XmStringFree</code> conditionally recovers memory used by a compound string. Applications should call <code>XmStringFree</code> when the application no longer needs <i>string</i>.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the compound string to be freed</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
