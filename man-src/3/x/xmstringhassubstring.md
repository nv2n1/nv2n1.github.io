---
title: "xmstringhassubstring(3)"
name: "xmstringhassubstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringhassubstring/"
description: "XmStringHasSubstring — A compound string function that indicates whether one compound string is contained within another"
---

<p><code>XmStringHasSubstring</code> &#8212; A compound string function that indicates whether one compound string is contained within another</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringHasSubstring</code>(
<code>XmString string</code>,
<code>XmString substring</code>);</pre>
<h2>Description</h2>
<p><code>XmStringHasSubstring</code> indicates whether or not one compound string is contained within another.</p>
<dl COMPACT>
<dt><i>string</i></p>
<dd>Specifies the compound string to be searched</p>
<dt><i>substring</i></p>
<dd>Specifies the compound string to be searched for</dl>
<h2>Return</h2>
<p>Returns True if <i>substring</i> has a single text component and if its text is completely contained within any single text component of <i>string</i>; otherwise, it returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringcreatelocalized/">XmStringCreateLocalized</a></code>(3).</p>
