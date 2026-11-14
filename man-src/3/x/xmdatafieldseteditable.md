---
title: "xmdatafieldseteditable(3)"
name: "xmdatafieldseteditable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldseteditable/"
description: "XmDataFieldSetEditable — A DataField function that sets the edit permission"
---

<p><code>XmDataFieldSetEditable</code> &#8212; A DataField function that sets the edit permission</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>void XmDataFieldSetEditable</code>(
<code>Widget widget</code>,
<code>Boolean editable</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldSetEditable</code> sets the edit permission state of the DataField widget. When set to True, the text string can be edited.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>editable</i></p>
<dd>Specifies a Boolean value that when True allows text string edits</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
