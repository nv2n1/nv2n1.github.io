---
title: "xmtextseteditable(3)"
name: "xmtextseteditable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextseteditable/"
description: "XmTextSetEditable — A Text function that sets the edit permission"
---

<p><code>XmTextSetEditable</code> &#8212; A Text function that sets the edit permission</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetEditable</code>(
<code>Widget widget</code>,
<code>Boolean editable</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetEditable</code> sets the edit permission state of the Text widget. When set to True, the text string can be edited.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>editable</i></p>
<dd>Specifies a Boolean value that when True allows text string edits</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
