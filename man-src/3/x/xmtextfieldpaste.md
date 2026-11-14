---
title: "xmtextfieldpaste(3)"
name: "xmtextfieldpaste"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldpaste/"
description: "XmTextFieldPaste — A TextField function that inserts the clipboard selection"
---

<p><code>XmTextFieldPaste</code> &#8212; A TextField function that inserts the clipboard selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldPaste</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldPaste</code> inserts the clipboard selection at the insertion cursor of the destination widget. If <code>XmNpendingDelete</code> is True and the insertion cursor is inside the current selection, the clipboard selection replaces the selected text. </p>
<p> This routine calls the widget&#8217;s <code>XmNvalueChangedCallback</code> and verification callbacks, either <code>XmNmodifyVerifyCallback</code> or <code>XmNmodifyVerifyCallbackWcs</code>, or both. If both verification callback lists are registered, the procedures of the <code>XmNmodifyVerifyCallback</code> list are executed first and the resulting data is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callbacks. </p>
<p> This routine calls the widget&#8217;s <code>XmNdestinationCallback</code> procedures with the <i>selection</i> member of the <code>XmDestinationCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>operation</i> member set to <code>XmCOPY</code>. If the <code>XmNcursorPosition</code> resource is greater than or is the same value as the position where the selection is to be inserted, the <code>XmNmotionVerifyCallback</code> is called.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if no transfers take place. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
