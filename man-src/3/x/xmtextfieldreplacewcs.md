---
title: "xmtextfieldreplacewcs(3)"
name: "xmtextfieldreplacewcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldreplacewcs/"
description: "XmTextFieldReplaceWcs — A TextField function that replaces part of a wide character string in a TextField widget"
---

<p><code>XmTextFieldReplaceWcs</code> &#8212; A TextField function that replaces part of a wide character string in a TextField widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldReplaceWcs</code>(
<code>Widget widget</code>,
<code>XmTextPosition from_pos</code>,
<code>XmTextPosition to_pos</code>,
<code>wchar_t *wcstring</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldReplaceWcs</code> replaces part of the wide character string in the TextField widget. The character positions begin at 0 (zero) and are numbered sequentially from the beginning of the text. </p>
<p> An example text replacement would be to replace the second and third characters in the text string. To accomplish this, the parameter <i>from_pos</i> must be 1 and <i>to_pos</i> must be 3. To insert a string after the fourth character, both parameters, <i>from_pos</i> and <i>to_pos</i>, must be 4. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. If the <code>XmNcursorPosition</code> resource is greater than or is the same value as <i>from_pos</i>, the <code>XmNmotionVerifyCallback</code> is called.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>from_pos</i></p>
<dd>Specifies the start position of the text to be replaced</p>
<dt><i>to_pos</i></p>
<dd>Specifies the end position of the text to be replaced</p>
<dt><i>wcstring</i></p>
<dd>Specifies the wide character string value to be added to the TextField widget</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldreplace/">XmTextFieldReplace</a></code>(3).</p>
