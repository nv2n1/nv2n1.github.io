---
title: "xmtextfieldsetstringwcs(3)"
name: "xmtextfieldsetstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldsetstringwcs/"
description: "XmTextFieldSetStringWcs — A TextField function that sets a wide character string value"
---

<p><code>XmTextFieldSetStringWcs</code> &#8212; A TextField function that sets a wide character string value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetStringWcs</code>(
<code>Widget widget</code>,
<code>wchar_t *wcstring</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetStringWcs</code> sets the wide character string value of the TextField widget. This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. It also sets the insertion cursor position to the beginning of the string and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>wcstring</i></p>
<dd>Specifies the wide character string value</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextfieldsetstring/">XmTextFieldSetString</a></code>(3).</p>
