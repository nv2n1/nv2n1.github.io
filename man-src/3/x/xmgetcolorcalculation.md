---
title: "xmgetcolorcalculation(3)"
name: "xmgetcolorcalculation"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetcolorcalculation/"
description: "XmGetColorCalculation — A function to get the procedure used for default color calculation"
---

<p><code>XmGetColorCalculation</code> &#8212; A function to get the procedure used for default color calculation</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmColorProc XmGetColorCalculation</code>(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmGetColorCalculation</code> returns the procedure being used to calculate default colors. </p>
<p> For a description of <code>XmColorProc</code>, see <code><a href="/docs/linux/man/3-xmsetcolorcalculation/">XmSetColorCalculation</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the procedure used for default color calculation.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmchangecolor/">XmChangeColor</a></code>(3), <code><a href="/docs/linux/man/3-xmgetcolors/">XmGetColors</a></code>(3), and <code><a href="/docs/linux/man/3-xmsetcolorcalculation/">XmSetColorCalculation</a></code>(3).</p>
