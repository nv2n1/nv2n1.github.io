---
title: "xmtextfieldsetselection(3)"
name: "xmtextfieldsetselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldsetselection/"
description: "XmTextFieldSetSelection — A TextField function that sets the primary selection of the text"
---

<p><code>XmTextFieldSetSelection</code> &#8212; A TextField function that sets the primary selection of the text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldSetSelection</code>(
<code>Widget widget</code>,
<code>XmTextPosition first</code>,
<code>XmTextPosition last</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldSetSelection</code> sets the primary selection of the text in the widget. It also sets the insertion cursor position to the last position of the selection and calls the widget&#8217;s <code>XmNmotionVerifyCallback</code> callbacks. <code>XmTextFieldSetSelection</code> always generates an <code>XmNgainPrimaryCallback</code> unless it fails to take ownership of the primary text selection.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the TextField widget ID</dd>
<dt><i>first</i></dt>
<dd>Marks the first character position of the text to be selected</dd>
<dt><i>last</i></dt>
<dd>Marks the last position of the text to be selected</dd>
<dt><i>time</i></dt>
<dd>Specifies the time at which the selection value is desired. This should be the same as the time of the event that triggered this request. One source of a valid time stamp is the function <code>XtLastTimestampProcessed</code>.</dd></dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
