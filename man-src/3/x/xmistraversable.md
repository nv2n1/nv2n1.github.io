---
title: "xmistraversable(3)"
name: "xmistraversable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmistraversable/"
description: "XmIsTraversable — A function that identifies whether a widget can be traversed"
---

<p><code>XmIsTraversable</code> &#8212; A function that identifies whether a widget can be traversed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmIsTraversable</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmIsTraversable</code> determines whether the specified widget is eligible to receive focus through keyboard traversal. In general, a widget is eligible to receive focus when all of the following conditions are true:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The widget and its ancestors are not being destroyed, are sensitive, and have a value of True for <code>XmNtraversalOn</code>.</p>
<dt> &bull;</p>
<dd>The widget and its ancestors are realized, managed, and (except for gadgets) mapped. If an application unmaps a <i>widget</i> that has its <code>XmNmappedWhenManaged</code> resource set to True, the return value is undefined.</p>
<dt> &bull;</p>
<dd>Some part of the widget&#8217;s rectangular area is unobscured by the widget&#8217;s ancestors, or some part of the widget&#8217;s rectangular area is inside the work window (but possibly outside the clip window) of a ScrolledWindow whose <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code> and whose <code>XmNtraverseObscuredCallback</code> is not NULL.</dl>
<p> Some widgets may not be eligible to receive focus even if they meet all these conditions. For example, most managers cannot receive focus through keyboard traversal. Some widgets may be eligible to receive focus under particular conditions. For example, a DrawingArea is eligible to receive focus if it meets the conditions above and has no child whose <code>XmNtraversalOn</code> resource is True. </p>
<p> Note that when all widgets in a shell hierarchy have been made untraversable, they are considered to have lost focus. When a widget in this hierarchy is made traversable again, it regains focus. </p>
<p> <code>XmIsTraversable</code> may return unexpected results when <i>widget</i> or its ancestors are overlapped by their siblings.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget</dl>
<h2>Return</h2>
<p>Returns True if the widget is eligible to receive focus through keyboard traversal; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmgetvisibility/">XmGetVisibility</a></code>(3) and <code><a href="/docs/linux/man/3-xmprocesstraversal/">XmProcessTraversal</a></code>(3).</p>
