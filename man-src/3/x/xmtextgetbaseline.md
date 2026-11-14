---
title: "xmtextgetbaseline(3)"
name: "xmtextgetbaseline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetbaseline/"
description: "XmTextGetBaseline — A Text function that accesses the y position of the baseline"
---

<p><code>XmTextGetBaseline</code> &#8212; A Text function that accesses the y position of the baseline</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>int XmTextGetBaseline</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetBaseline</code> accesses the <i>y</i> position of the baseline in the Text widget, relative to the <i>y</i> position of the top of the widget. </p>
<p> In vertical mode (when the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>) this function returns 0 and the program should use <code>XmTextGetCenterline</code> </p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an integer value that indicates the <i>y</i> position of the baseline in the Text widget. The calculation takes into account the margin height, shadow thickness, highlight thickness, and font ascent of the first font (set) in the fontlist used for drawing text. In this calculation, the <i>y</i> position of the top of the widget is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetcenterline/">XmTextGetCenterline</a></code>(3).</p>
