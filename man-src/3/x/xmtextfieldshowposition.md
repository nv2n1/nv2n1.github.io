---
title: "xmtextfieldshowposition(3)"
name: "xmtextfieldshowposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldshowposition/"
description: "XmTextFieldShowPosition — A TextField function that forces text at a given position to be displayed"
---

<p><code>XmTextFieldShowPosition</code> &#8212; A TextField function that forces text at a given position to be displayed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldShowPosition</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldShowPosition</code> forces text at the specified position to be displayed. The cursor position is not updated nor is the cursor shown at this position.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the character position to be displayed. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero). See <code><a href="/docs/linux/man/3-xmtextposition/">XmTextPosition</a></code>(3) for details on the <code>XmTextPosition</code> data type.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextposition/">XmTextPosition</a></code>(3).</p>
