---
title: "xmtextsetstringwcs(3)"
name: "xmtextsetstringwcs"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetstringwcs/"
description: "XmTextSetStringWcs — A Text function that sets a wide character string value"
---

<p><code>XmTextSetStringWcs</code> &#8212; A Text function that sets a wide character string value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetStringWcs</code>(
<code>Widget widget</code>,
<code>wchar_t *wcstring</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetStringWcs</code> sets the wide character string value of the Text widget. This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. This function also sets the insertion cursor position to the beginning of the string and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>value</i></p>
<dd>Specifies the wide character string value</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) and <code><a href="/docs/linux/man/3-xmtextsetstring/">XmTextSetString</a></code>(3).</p>
