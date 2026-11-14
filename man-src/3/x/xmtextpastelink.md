---
title: "xmtextpastelink(3)"
name: "xmtextpastelink"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextpastelink/"
description: "XmTextPasteLink — A Text function that inserts a link to the clipboard selection"
---

<p><code>XmTextPasteLink</code> &#8212; A Text function that inserts a link to the clipboard selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextPasteLink</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextPasteLink</code> inserts a link to the clipboard selection at the insertion cursor. This routine calls the widget&#8217;s <code>XmNdestinationCallback</code> procedures with the <i>selection</i> member of the <code>XmDestinationCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>operation</i> member set to <code>XmLINK</code>. The Text widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the clipboard selection and for taking any related actions.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if no transfers take place. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
