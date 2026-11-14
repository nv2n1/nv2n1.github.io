---
title: "xmtextgetcenterline(3)"
name: "xmtextgetcenterline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetcenterline/"
description: "XmTextGetCenterline — Return the height (length) of a character string when the writing direction is vertical"
---

<p><code>XmTextGetCenterline</code> &#8212; Return the height (length) of a character string when the writing direction is vertical</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>int XmTextGetCenterline</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetCenterline</code> accesses the x position of the centerline in the <code>Text</code> widget, relative to the x position of the top of the widget.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the <code>Text</code> widget ID.</dl>
<h2>Return Value</h2>
<p>In the case of horizontal writing, this function accesses 0. </p>
<p> In the case of vertical writing, this function accesses the x position of the first centerline in the Text widget, relative to the x position of the left of the widget. The calculation takes into account the margin width, shadow thickness, highlight thickness, and a half of font width of the first font(set) in the fontlist used for drawing text.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetbaseline/">XmTextGetBaseline</a></code>(3)</p>
