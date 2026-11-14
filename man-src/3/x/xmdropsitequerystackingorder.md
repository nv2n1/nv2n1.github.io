---
title: "xmdropsitequerystackingorder(3)"
name: "xmdropsitequerystackingorder"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsitequerystackingorder/"
description: "XmDropSiteQueryStackingOrder — A Drag and Drop function that returns the parent, a list of children, and the number of children for a specified widget"
---

<p><code>XmDropSiteQueryStackingOrder</code> &#8212; A Drag and Drop function that returns the parent, a list of children, and the number of children for a specified widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>Status XmDropSiteQueryStackingOrder</code>(
<code>Widget widget</code>,
<code>Widget *parent_return</code>,
<code>Widget **child_returns</code>,
<code>Cardinal *num_child_returns</code>);</pre>
<h2>Description</h2>
<p><code>XmDropSiteQueryStackingOrder</code> obtains the parent, a list of children registered as drop sites, and the number of children registered as drop sites for a given widget. The children are listed in current stacking order, from bottom-most (first child) to the top-most (last child). This function allocates memory for the returned data that must be freed by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget ID. For this widget, you obtain the list of its children, its parent, and the number of children.</p>
<dt><i>parent_return</i></p>
<dd>Returns the widget ID of the drop site parent of the specified widget.</p>
<dt><i>child_returns</i></p>
<dd>Returns a pointer to the list of drop site children associated with the specified widget. The function allocates memory to hold the list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<dt><i>num_child_returns</i></p>
<dd>Returns the number of drop site children for the specified widget.</dl>
<p> For a complete definition of DropSite and its associated resources, see <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3).</p>
<h2>Return</h2>
<p>Returns 0 (zero) if the routine fails; returns a nonzero value if it succeeds.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3) and <code><a href="/docs/linux/man/3-xmdropsiteconfigurestackingorder/">XmDropSiteConfigureStackingOrder</a></code>(3).</p>
