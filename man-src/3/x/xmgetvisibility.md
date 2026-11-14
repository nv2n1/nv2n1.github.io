---
title: "xmgetvisibility(3)"
name: "xmgetvisibility"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetvisibility/"
description: "XmGetVisibility — A function that determines if a widget is visible"
---

<p><code>XmGetVisibility</code> &#8212; A function that determines if a widget is visible</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmVisibility XmGetVisibility</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmGetVisibility</code> returns the visibility state of the specified widget. It checks to see if some part of the widget&#8217;s rectangular area is unobscured by the widget&#8217;s ancestors, or some part of the widget&#8217;s rectangular area is inside the work window (but possibly outside the clip window) of a ScrolledWindow whose <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code> and whose <code>XmNtraverseObscuredCallback</code> is not NULL. </p>
<p> <code>XmGetVisibility</code> does not check to see if <i>widget</i> is obscured by its siblings or by siblings of its ancestors. Consequently, <code>XmGetVisibility</code> returns <code>XmVISIBILITY_UNOBSCURED</code> for widgets which are completely or partially covered by one or more siblings of <i>widget</i> by one or more siblings of ancestors of <i>widget</i>. </p>
<p> When a widget which is unrealized is being queried, it is indicated that the widget is fully obscured. If an application unmaps a <i>widget</i> that has its <code>XmNmappedWhenManaged</code> resource set to True, the return value is undefined. When a widget which is unmanaged is being queried, it is indicated that the widget is fully obscured.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget</dl>
<h2>Return</h2>
<p>Returns one of the following values:</p>
<dl COMPACT>
<dt><code>XmVISIBILITY_UNOBSCURED</code></p>
<dd>Indicates that the widget is mapped, not obscured, and is completely visible on the screen.</p>
<dt><code>XmVISIBILITY_PARTIALLY_OBSCURED</code></p>
<dd>Indicates that the widget is mapped, and is not completely visible on the screen (partially obscured).</p>
<dt><code>XmVISIBILITY_FULLY_OBSCURED</code></p>
<dd>Indicates that the widget is not at all visible on the screen.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmistraversable/">XmIsTraversable</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmprocesstraversal/">XmProcessTraversal</a></code>(3).</p>
