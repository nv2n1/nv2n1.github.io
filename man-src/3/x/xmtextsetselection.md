---
title: "xmtextsetselection(3)"
name: "xmtextsetselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetselection/"
description: "XmTextSetSelection — A Text function that sets the primary selection of the text"
---

<p><code>XmTextSetSelection</code> &#8212; A Text function that sets the primary selection of the text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetSelection</code>(
<code>Widget widget</code>,
<code>XmTextPosition first</code>,
<code>XmTextPosition last</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetSelection</code> sets the primary selection of the text in the widget. It also sets the insertion cursor position to the last position of the selection and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>first</i></p>
<dd>Marks the first character position of the text to be selected</p>
<dt><i>last</i></p>
<dd>Marks the last position of the text to be selected</p>
<dt><i>time</i></p>
<dd>Specifies the time at which the selection value is desired. This should be the same as the time of the event that triggered this request. request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed</code>.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
