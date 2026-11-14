---
title: "xmdatafieldgetselectionposition(3)"
name: "xmdatafieldgetselectionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldgetselectionposition/"
description: "XmDataFieldGetSelectionPosition — A DataField function that accesses the position of the primary selection"
---

<p><code>XmDataFieldGetSelectionPosition</code> &#8212; A DataField function that accesses the position of the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>Boolean XmDataFieldGetSelectionPosition</code>(
<code>Widget widget</code>,
<code>XmTextPosition *left</code>,
<code>XmTextPosition *right</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldGetSelectionPosition</code> accesses the left and right position of the primary selection in the text buffer of the DataField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>left</i></p>
<dd>Specifies the pointer in which the position of the left boundary of the primary selection is returned. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero).</p>
<dt><i>right</i></p>
<dd>Specifies the pointer in which the position of the right boundary of the primary selection is returned. This is an integer number of characters from the beginning of the buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns True if the widget owns the primary selection; otherwise, it returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
