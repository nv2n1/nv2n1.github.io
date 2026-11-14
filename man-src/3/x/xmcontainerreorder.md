---
title: "xmcontainerreorder(3)"
name: "xmcontainerreorder"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainerreorder/"
description: "XmContainerReorder — Container widget function to reorder children"
---

<p><code>XmContainerReorder</code> &#8212; Container widget function to reorder children</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>void XmContainerReorder</code>(
<code>Widget container</code>,
<code>WidgetList widgets</code>,
<code>int num_widgets</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerReorder</code> obtains the <code>XmNpositionIndex</code> constraint resources of each widget specified in <i>widgets</i>, sorts them in ascending order, and inserts the <code>XmNpositionIndex</code> constraint resources in the new order into each widget. If the <code>XmNlayoutType</code> resource of Container is <code>XmOUTLINE</code> or <code>XmDETAIL</code>, <code>XmContainerReorder</code> will force a layout of all items.</p>
<dl COMPACT>
<dt><i>container</i></p>
<dd>Specifies the Container widget ID.</p>
<dt><i>widgets</i></p>
<dd>Specifies an array of widget children of <i>container</i>.</p>
<dt><i>num_widgets</i></p>
<dd>Specifies the number of items in the <i>widgets</i> array.</dl>
<p> For a complete definition of Container and its associated resources, see <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
