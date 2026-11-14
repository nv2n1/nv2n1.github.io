---
title: "xmtextcopy(3)"
name: "xmtextcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextcopy/"
description: "XmTextCopy — A Text function that copies the primary selection to the clipboard"
---

<p><code>XmTextCopy</code> &#8212; A Text function that copies the primary selection to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextCopy</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextCopy</code> copies the primary selected text to the clipboard. </p>
<p> This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmCOPY</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the server time at which the selection value is to be modified. This should be the time of the event which triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed()</code>.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL, if the <i>widget</i> does not own the primary selection, if the function is unable to gain ownership of the clipboard selection, or if no data is placed on the clipboard. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
