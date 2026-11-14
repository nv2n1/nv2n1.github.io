---
title: "xmtextgetlastposition(3)"
name: "xmtextgetlastposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetlastposition/"
description: "XmTextGetLastPosition — A Text function that accesses the last position in the text"
---

<p><code>XmTextGetLastPosition</code> &#8212; A Text function that accesses the last position in the text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>XmTextPosition XmTextGetLastPosition</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetLastPosition</code> accesses the last position in the text buffer of the Text widget. This is an integer number of characters from the beginning of the buffer, and represents the position that text added to the end of the buffer is placed after. The first character position is 0 (zero). The last character position is equal to the number of characters in the text buffer.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextPosition</code> value that indicates the last position in the text buffer.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
