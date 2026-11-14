---
title: "xmdatafieldsetaddmode(3)"
name: "xmdatafieldsetaddmode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldsetaddmode/"
description: "XmDataFieldSetAddMode — A DataField function that sets the state of Add mode"
---

<p><code>XmDataFieldSetAddMode</code> &#8212; A DataField function that sets the state of Add mode</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>void XmDataFieldSetAddMode</code>(
<code>Widget widget</code>,
<code>Boolean state</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldSetAddMode</code> controls whether or not the DataField widget is in Add mode. When the widget is in Add mode, the insert cursor can be moved without disturbing the primary selection.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>state</i></p>
<dd>Specifies whether or not the widget is in Add mode. A value of True turns on Add mode; a value of False turns off Add mode.</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
