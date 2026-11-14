---
title: "xmtextfieldsetinsertionposition(3)"
name: "xmtextfieldsetinsertionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldsetinsertionposition/"
description: "XmTextFieldSetInsertionPosition — A TextField function that sets the position of the insertion cursor"
---

<p><code>XmTextFieldSetInsertionPosition</code> &#8212; A TextField function that sets the position of the insertion cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetInsertionPosition</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetInsertionPosition</code> sets the insertion cursor position of the TextField widget. This routine also calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks if the insertion cursor position changes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the position of the insert cursor. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
