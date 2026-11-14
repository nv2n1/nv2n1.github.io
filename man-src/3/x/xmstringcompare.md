---
title: "xmstringcompare(3)"
name: "xmstringcompare"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringcompare/"
description: "XmStringCompare — A compound string function that compares two strings"
---

<p><code>XmStringCompare</code> &#8212; A compound string function that compares two strings</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringCompare</code>(
<code>XmString s1</code>,
<code>XmString s2</code>);</pre>
<h2>Description</h2>
<p><code>XmStringCompare</code> returns a Boolean value indicating the results of a semantically equivalent comparison of two compound strings. </p>
<p> Semantically equivalent means that the strings have the same text components, font list element tags, directions, and separators. In general, if two compound strings are created with the same (<code>char *</code>) string using <code>XmStringCreateLocalized</code> in the same language environment, the compound strings compare as equal. If two compound strings are created with the same text and tag argument using <code>XmStringCreate</code>, the strings compare as equal.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies a compound string to be compared with <i>s2</i></p>
<dt><i>s2</i></p>
<dd>Specifies a compound string to be compared with <i>s1</i></dl>
<h2>Return</h2>
<p>Returns True if two compound strings are equivalent.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringcreatelocalized/">XmStringCreateLocalized</a></code>(3).</p>
