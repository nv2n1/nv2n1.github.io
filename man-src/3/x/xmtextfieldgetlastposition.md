---
title: "xmtextfieldgetlastposition(3)"
name: "xmtextfieldgetlastposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetlastposition/"
description: "XmTextFieldGetLastPosition — A TextField function that accesses the position of the last text character"
---

<p><code>XmTextFieldGetLastPosition</code> &#8212; A TextField function that accesses the position of the last text character</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>XmTextPosition XmTextFieldGetLastPosition</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetLastPosition</code> accesses the position of the last character in the text buffer of the TextField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextPosition</code> value that indicates the position of the last character in the text buffer. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero). The last character position is equal to the number of characters in the text buffer.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
