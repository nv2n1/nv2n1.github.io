---
title: "xmtextinsertwcs(3)"
name: "xmtextinsertwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextinsertwcs/"
description: "XmTextInsertWcs — A Text function that inserts a wide character string into a Text widget"
---

<p><code>XmTextInsertWcs</code> &#8212; A Text function that inserts a wide character string into a Text widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextInsertWcs</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>,
<code>wchar_t *wcstring</code>);</pre>
<h2>Description</h2>
<p><code>XmTextInsertWcs</code> inserts a wide character string into the Text widget at a specified location. The character positions begin at 0 (zero) and are numbered sequentially from the beginning of the text. For example, to insert a string after the fourth character, the <i>position</i> parameter must be 4. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. If the <code>XmNcursorPosition</code> resource is greater than or is the same value as <i>position</i>, the <code>XmNmotionVerifyCallback</code> is called. </p>
<p> Note that, if <i>value</i> is a null string, no callbacks will be generated, since no modifications will have been made.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the position in the text string where the new character string is to be inserted</p>
<dt><i>wcstring</i></p>
<dd>Specifies the wide character string value to be added to the Text widget</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextinsert/">XmTextInsert</a></code>(3).</p>
