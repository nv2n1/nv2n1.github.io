---
title: "xmtextfieldinsert(3)"
name: "xmtextfieldinsert"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldinsert/"
description: "XmTextFieldInsert — A TextField function that inserts a character string into a text string"
---

<p><code>XmTextFieldInsert</code> &#8212; A TextField function that inserts a character string into a text string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldInsert</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>,
<code>char * value</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldInsert</code> inserts a character string into the text string in the TextField widget. The character positions begin at 0 (zero) and are numbered sequentially from the beginning of the text. For example, to insert a string after the fourth character, the <i>position</i> parameter must be 4. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. If the <code>XmNcursorPosition</code> resource is greater than or is the same value as <i>position</i>, the <code>XmNmotionVerifyCallback</code> is called.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the TextField widget ID</dd>
<dt><i>position</i></dt>
<dd>Specifies the position in the text string where the character string is to be inserted</dd>
<dt><i>value</i></dt>
<dd>Specifies the character string value to be added to the text widget</dd></dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldinsertwcs/">XmTextFieldInsertWcs</a></code>(3).</p>
