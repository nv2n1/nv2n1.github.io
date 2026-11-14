---
title: "xmtextfieldgetbaseline(3)"
name: "xmtextfieldgetbaseline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldgetbaseline/"
description: "XmTextFieldGetBaseline — A TextField function that accesses the y position of the baseline"
---

<p><code>XmTextFieldGetBaseline</code> &#8212; A TextField function that accesses the y position of the baseline</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>int XmTextFieldGetBaseline</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldGetBaseline</code> accesses the <i>y</i> position of the baseline in the TextField widget, relative to the <i>y</i> position of the top of the widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an integer value that indicates the <i>y</i> position of the baseline in the TextField widget. The calculation takes into account the margin height, shadow thickness, highlight thickness, and font ascent of the first font (set) in the fontlist used for drawing text. In this calculation, the <i>y</i> position of the top of the widget is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
