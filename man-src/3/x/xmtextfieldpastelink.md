---
title: "xmtextfieldpastelink(3)"
name: "xmtextfieldpastelink"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldpastelink/"
description: "XmTextFieldPasteLink — A TextField function that inserts a link to the clipboard selection"
---

<p><code>XmTextFieldPasteLink</code> &#8212; A TextField function that inserts a link to the clipboard selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldPasteLink</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldPasteLink</code> inserts a link to the clipboard selection at the insertion cursor. This routine calls the widget&#8217;s <code>XmNdestinationCallback</code> procedures with the <i>selection</i> member of the <code>XmDestinationCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>operation</i> member set to <code>XmLINK</code>. The TextField widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the clipboard selection and for taking any related actions.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if no transfers take place. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
