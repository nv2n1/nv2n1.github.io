---
title: "xmtextcopylink(3)"
name: "xmtextcopylink"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextcopylink/"
description: "XmTextCopyLink — A Text function that copies a link to the primary selection to the clipboard"
---

<p><code>XmTextCopyLink</code> &#8212; A Text function that copies a link to the primary selection to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextCopyLink</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextCopyLink</code> copies a link to the primary selected text to the clipboard. This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmLINK</code>. The Text widget itself does not copy any links; <code>XmNconvertCallback</code> procedures are responsible for copying the link to the clipboard and for taking any related actions.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the time of the transfer. This should be the time of the event which triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed</code>.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL, if the <i>widget</i> does not own the primary selection, if the function is unable to gain ownership of the clipboard selection, or if no data is placed on the clipboard. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
