---
title: "xmdatafieldcopy(3)"
name: "xmdatafieldcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdatafieldcopy/"
description: "XmDataFieldCopy — A DataField function that copies the primary selection to the clipboard"
---

<p><code>XmDataFieldCopy</code> &#8212; A DataField function that copies the primary selection to the clipboard</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DataF.h&gt;
<code>Boolean XmDataFieldCopy</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmDataFieldCopy</code> copies the primary selected text to the clipboard. </p>
<p> This routine calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, with the <i>selection</i> member of the <code>XmConvertCallbackStruct</code> set to <code>CLIPBOARD</code> and with the <i>parm</i> member set to <code>XmCOPY</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the DataField widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the time at which the selection value is to be modified. This should be the time of the event that triggered this request.</dl>
<p> For a complete definition of DataField and its associated resources, see <code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns False if the primary selection is NULL, if the <i>widget</i> does not own the primary selection, if the function is unable to gain ownership of the clipboard selection, or if no data is placed on the clipboard. Otherwise, it returns True.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdatafield/">XmDataField</a></code>(3).</p>
