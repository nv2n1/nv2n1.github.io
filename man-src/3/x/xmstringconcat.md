---
title: "xmstringconcat(3)"
name: "xmstringconcat"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringconcat/"
description: "XmStringConcat — A compound string function that appends one string to another"
---

<p><code>XmStringConcat</code> &#8212; A compound string function that appends one string to another</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmString XmStringConcat</code>(
<code>XmString s1</code>,
<code>XmString s2</code>);</pre>
<h2>Description</h2>
<p><code>XmStringConcat</code> copies <i>s2</i> to the end of <i>s1</i> and returns a copy of the resulting compound string. The original strings are preserved. The function will allocate space to hold the returned compound string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmStringFree</code>.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies the compound string to which a copy of <i>s2</i> is appended</p>
<dt><i>s2</i></p>
<dd>Specifies the compound string that is appended to the end of <i>s1</i></dl>
<h2>Return</h2>
<p>Returns a new compound string.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringfree/">XmStringFree</a></code>(3).</p>
