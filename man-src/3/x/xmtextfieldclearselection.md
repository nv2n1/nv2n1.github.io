---
title: "xmtextfieldclearselection(3)"
name: "xmtextfieldclearselection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldclearselection/"
description: "XmTextFieldClearSelection — A TextField function that clears the primary selection"
---

<p><code>XmTextFieldClearSelection</code> &#8212; A TextField function that clears the primary selection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>void XmTextFieldClearSelection</code>(
<code>Widget widget</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldClearSelection</code> clears the primary selection in the TextField widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID.</p>
<dt><i>time</i></p>
<dd>Specifies the time at which the selection value is desired. This should be the time of the event that triggered this request.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
