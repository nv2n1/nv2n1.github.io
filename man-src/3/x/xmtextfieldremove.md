---
title: "xmtextfieldremove(3)"
name: "xmtextfieldremove"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldremove/"
description: "XmTextFieldRemove — A TextField function that deletes the primary selection"
---

<p><code>XmTextFieldRemove</code> &#8212; A TextField function that deletes the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldRemove</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldRemove</code> deletes the primary selected text. If there is a selection, this routine also calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. This function may also call the <code>XmNmotionVerifyCallback</code> callback.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL or if the <i>widget</i> does not own the primary selection. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
