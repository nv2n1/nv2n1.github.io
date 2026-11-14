---
title: "xmtextfieldcopylink(3)"
name: "xmtextfieldcopylink"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldcopylink/"
description: "XmTextFieldCopyLink — A TextField function that copies a link to the primary selection to the clipboard"
---

<p><code>XmTextFieldCopyLink</code> &#8212; A TextField function that copies a link to the primary selection to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldCopyLink</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldCopyLink</code> copies a link to the primary selected text to the clipboard. This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmLINK</code>. The TextField widget itself does not copy any links; <code>XmNconvertCallback</code> procedures are responsible for copying the link to the clipboard and for taking any related actions.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the time of the transfer. This should be the time of the event which triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed</code>.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL, if the <i>widget</i> does not own the primary selection, if the function is unable to gain ownership of the clipboard selection, or if no data is placed on the clipboard. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
