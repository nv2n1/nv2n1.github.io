---
title: "xmstringbytecompare(3)"
name: "xmstringbytecompare"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringbytecompare/"
description: "XmStringByteCompare — A compound string function that indicates the results of a byte-by-byte comparison"
---

<p><code>XmStringByteCompare</code> &#8212; A compound string function that indicates the results of a byte-by-byte comparison</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmStringByteCompare</code>(
<code>XmString s1</code>,
<code>XmString s2</code>);</pre>
<h2>Description</h2>
<p>This function is obsolete and exists for compatibility with previous releases. <code>XmStringByteCompare</code> returns a Boolean indicating the results of a byte-by-byte comparison of two compound strings. </p>
<p> In general, if two compound strings are created with the same (<code>char *</code>) string using <code>XmStringCreateLocalized</code> in the same language environment, the compound strings compare as equal. If two compound strings are created with the same (<code>char&nbsp;<wbr>*</code>) string and the same font list element tag set other than <code>XmFONTLIST_DEFAULT_TAG</code> using <code>XmStringCreate</code>, the strings compare as equal. </p>
<p> In some cases, once a compound string is put into a widget, that string is converted into an internal form to allow faster processing. Part of the conversion process strips out unnecessary or redundant information. If an application then does an <code>XtGetValues</code> to retrieve a compound string from a widget (specifically, Label and all of its subclasses), it is not guaranteed that the compound string returned is byte-for-byte the same as the string given to the widget originally.</p>
<dl COMPACT>
<dt><i>s1</i></p>
<dd>Specifies a compound string to be compared with <i>s2</i></p>
<dt><i>s2</i></p>
<dd>Specifies a compound string to be compared with <i>s1</i></dl>
<h2>Return</h2>
<p>Returns True if two compound strings are identical byte-by-byte.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3) and <code><a href="/docs/linux/man/3-xmstringcreatelocalized/">XmStringCreateLocalized</a></code>(3).</p>
