---
title: "xmtextfieldseteditable(3)"
name: "xmtextfieldseteditable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldseteditable/"
description: "XmTextFieldSetEditable — A TextField function that sets the edit permission"
---

<p><code>XmTextFieldSetEditable</code> &#8212; A TextField function that sets the edit permission</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetEditable</code>(
<code>Widget widget</code>,
<code>Boolean editable</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetEditable</code> sets the edit permission state of the TextField widget. When set to True, the text string can be edited.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>editable</i></p>
<dd>Specifies a Boolean value that when True allows text string edits</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
