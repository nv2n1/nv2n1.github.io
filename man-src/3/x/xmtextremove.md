---
title: "xmtextremove(3)"
name: "xmtextremove"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextremove/"
description: "XmTextRemove — A Text function that deletes the primary selection"
---

<p><code>XmTextRemove</code> &#8212; A Text function that deletes the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextRemove</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextRemove</code> deletes the primary selected text. If there is a selection, this routine also calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. This function may also call the <code>XmNmotionVerifyCallback</code> callback.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL or if the <i>widget</i> does not own the primary selection. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
