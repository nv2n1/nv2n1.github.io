---
title: "xmtextgetinsertionposition(3)"
name: "xmtextgetinsertionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetinsertionposition/"
description: "XmTextGetInsertionPosition — A Text function that accesses the position of the insert cursor"
---

<p><code>XmTextGetInsertionPosition</code> &#8212; A Text function that accesses the position of the insert cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>XmTextPosition XmTextGetInsertionPosition</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetInsertionPosition</code> accesses the insertion cursor position of the Text widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextPosition</code> value that indicates the state of the <code>XmNcursorPosition</code> resource. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
