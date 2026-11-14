---
title: "xmtextfieldcut(3)"
name: "xmtextfieldcut"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldcut/"
description: "XmTextFieldCut — A TextField function that copies the primary selection to the clipboard and deletes the selected text"
---

<p><code>XmTextFieldCut</code> &#8212; A TextField function that copies the primary selection to the clipboard and deletes the selected text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldCut</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldCut</code> copies the primary selected text to the clipboard and then deletes the primary selected text. This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. </p>
<p> This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmMOVE</code>. If the transfer is successful, this routine then calls the <code>XmNconvertCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>DELETE</code> target.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the time at which the selection value is to be modified. This should be the time of the event that triggered this request.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL, if the <i>widget</i> does not own the primary selection, if the function is unable to gain ownership of the clipboard selection, or if no data is placed on the clipboard. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
