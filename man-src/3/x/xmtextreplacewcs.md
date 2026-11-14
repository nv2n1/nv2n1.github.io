---
title: "xmtextreplacewcs(3)"
name: "xmtextreplacewcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextreplacewcs/"
description: "XmTextReplaceWcs — A Text function that replaces part of a wide character string in a Text widget"
---

<p><code>XmTextReplaceWcs</code> &#8212; A Text function that replaces part of a wide character string in a Text widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextReplaceWcs</code>(
<code>Widget widget</code>,
<code>XmTextPosition from_pos</code>,
<code>XmTextPosition to_pos</code>,
<code>wchar_t *wcstring</code>);</pre>
<h2>Description</h2>
<p><code>XmTextReplaceWcs</code> replaces part of the wide character string in the Text widget. The character positions begin at zero and are numbered sequentially from the beginning of the text. </p>
<p> An example text replacement would be to replace the second and third characters in the text string. To accomplish this, the <i>from_pos</i> parameter must be 1 and the <i>to_pos</i> parameter must be 3. To insert a string after the fourth character, both the <i>from_pos</i> and <i>to_pos</i> parameters must be 4. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. This routine calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callback when <i>from_pos</i> is less than or equal to the cursor position.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>from_pos</i></p>
<dd>Specifies the start position of the text to be replaced</p>
<dt><i>to_pos</i></p>
<dd>Specifies the end position of the text to be replaced</p>
<dt><i>wcstring</i></p>
<dd>Specifies the wide character string value to be added to the Text widget</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextreplace/">XmTextReplace</a></code>(3).</p>
