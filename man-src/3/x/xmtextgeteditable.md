---
title: "xmtextgeteditable(3)"
name: "xmtextgeteditable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgeteditable/"
description: "XmTextGetEditable — A Text function that accesses the edit permission state"
---

<p><code>XmTextGetEditable</code> &#8212; A Text function that accesses the edit permission state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Boolean XmTextGetEditable</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetEditable</code> accesses the edit permission state of the Text widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a Boolean value that indicates the state of the <code>XmNeditable</code> resource.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
