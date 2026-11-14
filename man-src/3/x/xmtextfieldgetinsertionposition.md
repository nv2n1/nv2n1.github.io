---
title: "xmtextfieldgetinsertionposition(3)"
name: "xmtextfieldgetinsertionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetinsertionposition/"
description: "XmTextFieldGetInsertionPosition — A TextField function that accesses the position of the insertion cursor"
---

<p><code>XmTextFieldGetInsertionPosition</code> &#8212; A TextField function that accesses the position of the insertion cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>XmTextPosition XmTextFieldGetInsertionPosition</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetInsertionPosition</code> accesses the insertion cursor position of the TextField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextPosition</code> value that indicates the state of the <code>XmNcursorPosition</code> resource. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
