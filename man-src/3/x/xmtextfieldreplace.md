---
title: "xmtextfieldreplace(3)"
name: "xmtextfieldreplace"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldreplace/"
description: "XmTextFieldReplace — A TextField function that replaces part of a text string"
---

<p><code>XmTextFieldReplace</code> &#8212; A TextField function that replaces part of a text string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldReplace</code>(
<code>Widget widget</code>,
<code>XmTextPosition from_pos</code>,
<code>XmTextPosition to_pos</code>,
<code>char * value</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldReplace</code> replaces part of the text string in the TextField widget. The character positions begin at 0 (zero) and are numbered sequentially from the beginning of the text. </p>
<p> An example text replacement would be to replace the second and third characters in the text string. To accomplish this, the parameter <i>from_pos</i> must be 1 and <i>to_pos</i> must be 3. To insert a string after the fourth character, both parameters, <i>from_pos</i> and <i>to_pos</i>, must be 4. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. The <code>XmNmotionVerifyCallback</code> is generated if <i>to_pos</i> is less than or equal to the cursor position and the length of <i>value</i> is not the same as the length of the text being replaced, or if the cursor position is between <i>from_pos</i> and <i>to_pos</i>, and the distance from the cursor position to <i>from_pos</i> is greater than the length of <i>value</i>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>from_pos</i></p>
<dd>Specifies the start position of the text to be replaced</p>
<dt><i>to_pos</i></p>
<dd>Specifies the end position of the text to be replaced</p>
<dt><i>value</i></p>
<dd>Specifies the character string value to be added to the text widget</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3). <code><a href="/docs/linux/man/3-xmtextfieldreplacewcs/">XmTextFieldReplaceWcs</a></code>(3).</p>
