---
title: "xmcontainergetitemchildren(3)"
name: "xmcontainergetitemchildren"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainergetitemchildren/"
description: "XmContainerGetItemChildren — Container widget function to find all children of an item"
---

<p><code>XmContainerGetItemChildren</code> &#8212; Container widget function to find all children of an item</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;
<code>int XmContainerGetItemChildren</code>(
<code>Widget container</code>,
<code>Widget item</code>,
<code>WidgetList * item_children</code>);</pre>
<h2>Description</h2>
<p><code>XmContainerGetItemChildren</code> allocates a WidgetList and stores within it the widget IDs of all widgets that have <i>item</i> specified as the value of their <code>XmNentryParent</code> resource. The application programmer is responsible for freeing the allocated WidgetList using XtFree. The number of widget IDs returned in <i>item_children</i> is returned by the function. If no widgets specify <i>item</i> as the value of their <code>XmNentryParent</code> resource, the function returns zero and <i>item_children</i> is left unchanged.</p>
<dl COMPACT>
<dt><i>container</i></p>
<dd>Specifies the Container widget ID.</p>
<dt><i>item</i></p>
<dd>Specifies a widgetID within <i>container</i>.</p>
<dt><i>item_children</i></p>
<dd>Returned array of Widgets.</dl>
<p> For a complete definition of Container and its associated resources, see <code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns a count of all widgets that have <i>item</i> specified as the value of their <code>XmNentryParent</code> resource.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcontainer/">XmContainer</a></code>(3).</p>
