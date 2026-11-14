---
title: "xmtextfieldsetstring(3)"
name: "xmtextfieldsetstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldsetstring/"
description: "XmTextFieldSetString — A TextField function that sets the string value"
---

<p><code>XmTextFieldSetString</code> &#8212; A TextField function that sets the string value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetString</code>(
<code>Widget widget</code>,
<code>char * value</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetString</code> sets the string value of the TextField widget. This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. It also sets the insertion cursor position to the beginning of the string and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>value</i></p>
<dd>Specifies the character pointer to the string value and places the string into the text edit window</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldsetstringwcs/">XmTextFieldSetStringWcs</a></code>(3).</p>
