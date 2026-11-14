---
title: "xmtextsetinsertionposition(3)"
name: "xmtextsetinsertionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetinsertionposition/"
description: "XmTextSetInsertionPosition — A Text function that sets the position of the insert cursor"
---

<p><code>XmTextSetInsertionPosition</code> &#8212; A Text function that sets the position of the insert cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetInsertionPosition</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetInsertionPosition</code> sets the insertion cursor position of the Text widget. This routine also calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks if the insertion cursor position changes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the position of the insertion cursor. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
