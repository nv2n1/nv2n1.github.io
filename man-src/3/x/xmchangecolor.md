---
title: "xmchangecolor(3)"
name: "xmchangecolor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmchangecolor/"
description: "XmChangeColor — Recalculates all associated colors of a widget"
---

<p><code>XmChangeColor</code> &#8212; Recalculates all associated colors of a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmChangeColor</code>(
<code>Widget widget</code>,
<code>Pixel background</code>);</pre>
<h2>Description</h2>
<p><code>XmChangeColor</code> handles all color modifications for the specified widget when a new background pixel value is specified. This function recalculates the foreground, select, and shadow colors based on the new background color and sets the corresponding resources for the widget. If a color calculation procedure has been set by a call to <code>XmSetColorCalculation</code>, <code>XmChangeColor</code> uses that procedure to calculate the new colors. Otherwise, the routine uses a default procedure.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget ID whose colors will be updated</p>
<dt><i>background</i></p>
<dd>Specifies the background color pixel value</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmgetcolorcalculation/">XmGetColorCalculation</a></code>(3), <code><a href="/docs/linux/man/3-xmgetcolors/">XmGetColors</a></code>(3), and <code><a href="/docs/linux/man/3-xmsetcolorcalculation/">XmSetColorCalculation</a></code>(3).</p>
