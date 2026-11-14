---
title: "xmtextclearselection(3)"
name: "xmtextclearselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextclearselection/"
description: "XmTextClearSelection — A Text function that clears the primary selection"
---

<p><code>XmTextClearSelection</code> &#8212; A Text function that clears the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextClearSelection</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextClearSelection</code> clears the primary selection in the Text widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the server time at which the selection value is desired. This should be the time of the event that triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed()</code>.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
