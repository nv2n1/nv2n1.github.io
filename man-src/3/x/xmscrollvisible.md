---
title: "xmscrollvisible(3)"
name: "xmscrollvisible"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrollvisible/"
description: "XmScrollVisible — A ScrolledWindow function that makes an invisible descendant of a ScrolledWindow work area visible"
---

<p><code>XmScrollVisible</code> &#8212; A ScrolledWindow function that makes an invisible<br />
&nbsp;<wbr>descendant of a ScrolledWindow work area visible</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrolledW.h&gt;
<code>void XmScrollVisible</code>(
<code>Widget scrollw_widget</code>,
<code>Widget widget</code>,
<code>Dimension left_right_margin</code>,
<code>Dimension top_bottom_margin</code>);</pre>
<h2>Description</h2>
<p><code>XmScrollVisible</code> makes an obscured or partially obscured widget or gadget descendant of a ScrolledWindow work area visible. The function repositions the work area and sets the specified margins between the widget and the nearest viewport boundary. The widget&#8217;s location relative to the viewport determines whether one or both of the margins must be adjusted. This function requires that the <code>XmNscrollingPolicy</code> of the ScrolledWindow widget be set to <code>XmAUTOMATIC</code>.</p>
<dl COMPACT>
<dt><i>scrollw_widget</i></p>
<dd>Specifies the ID of the ScrolledWindow widget whose work area window contains an obscured descendant.</p>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget to be made visible.</p>
<dt><i>left_right_margin</i></p>
<dd>Specifies the margin to establish between the left or right edge of the widget and the associated edge of the viewport. This margin is established only if the widget must be moved horizontally to make it visible.</p>
<dt><i>top_bottom_margin</i></p>
<dd>Specifies the margin to establish between the top or bottom edge of the widget and the associated edge of the viewport. This margin is established only if the widget must be moved vertically to make it visible.</dl>
<p> For a complete definition of ScrolledWindow and its associated resources, see <code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3)</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3).</p>
