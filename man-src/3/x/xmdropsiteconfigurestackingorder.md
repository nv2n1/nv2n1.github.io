---
title: "xmdropsiteconfigurestackingorder(3)"
name: "xmdropsiteconfigurestackingorder"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsiteconfigurestackingorder/"
description: "XmDropSiteConfigureStackingOrder — A Drag and Drop function that reorders a stack of widgets that are registered drop sites"
---

<p><code>XmDropSiteConfigureStackingOrder</code> &#8212; A Drag and Drop function that reorders a stack of widgets that are registered drop sites</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropSiteConfigureStackingOrder</code>(
<code>Widget widget</code>,
<code>Widget sibling</code>,
<code>Cardinal stack_mode</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteConfigureStackingOrder</code> changes the stacking order of the drop site specified by <i>widget</i>. The stacking order controls the manner in which drag-under effects are clipped by overlapping siblings, regardless of whether they are active. The stack mode is relative either to the entire stack, or to another drop site within the stack. The stack order can be modified only if the drop sites are siblings in both the widget and drop site hierarchy, and the widget parent of the drop sites is registered as a composite drop site.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the drop site to be restacked.</p>
<dt><i>sibling</i></p>
<dd>Specifies a sibling drop site for stacking operations. If specified, then <i>widget</i> is restacked relative to this drop site&#8217;s stack position.</p>
<dt><i>stack_mode</i></p>
<dd>Specifies the new stack position for the specified widget. The values are <code>XmABOVE</code> and <code>XmBELOW</code>. If a sibling is specified, then <i>widget</i> is restacked as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmABOVE</code></p>
<dd>The widget is placed just above the sibling.</p>
<dt><code>XmBELOW</code></p>
<dd>The widget is placed just below the sibling.</dl>
</dl>
<dd>If the <i>sibling</i> parameter is not specified, then <i>widget</i> is restacked as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmABOVE</code></p>
<dd>The widget is placed at the top of the stack.</p>
<dt><code>XmBELOW</code></p>
<dd>The widget is placed at the bottom of the stack.</dl>
</dl>
</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteretrieve/">XmDropSiteRetrieve</a></code>(3), and <code><a href="/docs/linux/man/3-xmdropsitequerystackingorder/">XmDropSiteQueryStackingOrder</a></code>(3).</p>
