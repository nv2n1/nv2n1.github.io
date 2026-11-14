---
title: "xmtextfieldgeteditable(3)"
name: "xmtextfieldgeteditable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgeteditable/"
description: "XmTextFieldGetEditable — A TextField function that accesses the edit permission state"
---

<p><code>XmTextFieldGetEditable</code> &#8212; A TextField function that accesses the edit permission state</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldGetEditable</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetEditable</code> accesses the edit permission state of the TextField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns a Boolean value that indicates the state of the <code>XmNeditable</code> resource.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
