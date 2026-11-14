---
title: "xmdatafieldsetselection(3)"
name: "xmdatafieldsetselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldsetselection/"
description: "XmDataFieldSetSelection — A DataField function that sets the primary selection of the text"
---

<p><code>XmDataFieldSetSelection</code> &#8212; A DataField function that sets the primary selection of the text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>void XmDataFieldSetSelection</code>(
<code>Widget widget</code>,
<code>XmTextPosition first</code>,
<code>XmTextPosition last</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldSetSelection</code> sets the primary selection of the text in the widget. It also sets the insertion cursor position to the last position of the selection and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks. <code>XmDataFieldSetSelection</code> always generates an <code>XmNgainPrimaryCallback</code> unless it fails to take ownership of the primary text selection.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID</p>
<dt><i>first</i></p>
<dd>Marks the first character position of the text to be selected</p>
<dt><i>last</i></p>
<dd>Marks the last position of the text to be selected</p>
<dt><i>time</i></p>
<dd>Specifies the time at which the selection value is desired. This should be the same as the time of the event that triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed</code>.</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
