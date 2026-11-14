---
title: "xmsetcolorcalculation(3)"
name: "xmsetcolorcalculation"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmsetcolorcalculation/"
description: "XmSetColorCalculation — A function to set the procedure used for default color calculation"
---

<p><code>XmSetColorCalculation</code> &#8212; A function to set the procedure used for default color calculation</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmColorProc XmSetColorCalculation</code>(
<code>XmColorProc color_proc</code>);</pre>
<h2>Description</h2>
<p><code>XmSetColorCalculation</code> sets the procedure to calculate default colors. This procedure is used to calculate the foreground, top shadow, bottom shadow, and select colors on the basis of a given background color. If called with an argument of NULL, it restores the default procedure used to calculate colors.</p>
<dl COMPACT>
<dt><i>color_proc</i></p>
<dd>Specifies the procedure to use for color calculation.</dl>
<p> Following is a description of the <code>XmColorProc</code> type used by <code>XmSetColorCalculation</code>: </p>
<pre>void (*<i>color_proc</i>) (<i>background_color, foreground_color, select_color, top_shadow_color,
bottom_shadow_color</i>)
 XColor <i>*background_color</i>;
 XColor <i>*foreground_color</i>;
 XColor <i>*select_color</i>;
 XColor <i>*top_shadow_color</i>;
 XColor <i>*bottom_shadow_color</i>;
(<code>void</code>)</pre>
<p>Specifies the procedure used to calculate default colors. The procedure is passed a pointer to an <code>XColor</code> structure representing the background color. The <i>pixel</i>, <i>red</i>, <i>green</i>, and <i>blue</i> members of this structure are filled in with values that are valid for the current colormap. </p>
<p> The procedure is passed pointers to <code>XColor</code> structures representing the foreground, select, top shadow, and bottom shadow colors to be calculated. The procedure calculates and fills in the <i>red</i>, <i>green</i>, and <i>blue</i> members of these structures. The procedure should not allocate color cells for any of these colors.</p>
<dl COMPACT>
<dt><i>background_color</i></p>
<dd>Specifies the background color.</p>
<dt><i>foreground_color</i></p>
<dd>Specifies the foreground color to be calculated.</p>
<dt><i>select_color</i></p>
<dd>Specifies the select color to be calculated.</p>
<dt><i>top_shadow_color</i></p>
<dd>Specifies the top shadow color to be calculated.</p>
<dt><i>bottom_shadow_color</i></p>
<dd>Specifies the bottom shadow color to be calculated.</dl>
<h2>Return</h2>
<p>Returns the color calculation procedure that was used at the time this routine was called.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmchangecolor/">XmChangeColor</a></code>(3), <code><a href="/docs/linux/man/3-xmgetcolors/">XmGetColors</a></code>(3), and <code><a href="/docs/linux/man/3-xmgetcolorcalculation/">XmGetColorCalculation</a></code>(3).</p>
