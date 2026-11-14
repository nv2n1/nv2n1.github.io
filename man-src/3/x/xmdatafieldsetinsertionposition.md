---
title: "xmdatafieldsetinsertionposition(3)"
name: "xmdatafieldsetinsertionposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldsetinsertionposition/"
description: "XmDataFieldSetInsertionPosition — A DataField function that sets the position of the insertion cursor"
---

<p><code>XmDataFieldSetInsertionPosition</code> &#8212; A DataField function that sets the position of the insertion cursor</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>void XmDataFieldSetInsertionPosition</code>(
<code>Widget widget</code>,
<code>XmDataPosition position</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldSetInsertionPosition</code> sets the insertion cursor position of the DataField widget. This routine also calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks if the insertion cursor position changes.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the position of the insert cursor. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
