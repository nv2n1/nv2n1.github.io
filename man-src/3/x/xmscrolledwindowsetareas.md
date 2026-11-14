---
title: "xmscrolledwindowsetareas(3)"
name: "xmscrolledwindowsetareas"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrolledwindowsetareas/"
description: "XmScrolledWindowSetAreas — A ScrolledWindow function that adds or changes a window work region and a horizontal or vertical ScrollBar widget to the ScrolledWindow widget"
---

<p><code>XmScrolledWindowSetAreas</code> &#8212; A ScrolledWindow function that adds or changes a window work region and a horizontal or vertical ScrollBar widget to the ScrolledWindow widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrolledW.h&gt;
<code>void XmScrolledWindowSetAreas</code>(
<code>Widget widget</code>,
<code>Widget horizontal_scrollbar</code>,
<code>Widget vertical_scrollbar</code>,
<code>Widget work_region</code>);</pre>
<h2>Description</h2>
<p><code>XmScrolledWindowSetAreas</code> adds or changes a window work region and a horizontal or vertical ScrollBar widget to the ScrolledWindow widget for the application. Each widget is optional and may be passed as NULL. This function is obsolete and exists for compatibility with other releases. Use the <code>XmNscrolledWindowChildType</code> resource of <code>XmScrolledWindow</code> instead.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ScrolledWindow widget ID.</p>
<dt><i>horizontal_scrollbar</i></p>
<dd>Specifies the ScrollBar widget ID for the horizontal ScrollBar to be associated with the ScrolledWindow widget. Set this ID only after creating an instance of the ScrolledWindow widget. The resource name associated with this argument is <code>XmNhorizontalScrollBar</code>.</p>
<dt><i>vertical_scrollbar</i></p>
<dd>Specifies the ScrollBar widget ID for the vertical ScrollBar to be associated with the ScrolledWindow widget. Set this ID only after creating an instance of the ScrolledWindow widget. The resource name associated with this argument is <code>XmNverticalScrollBar</code>.</p>
<dt><i>work_region</i></p>
<dd>Specifies the widget ID for the work window to be associated with the ScrolledWindow widget. Set this ID only after creating an instance of the ScrolledWindow widget. The attribute name associated with this argument is <code>XmNworkWindow</code>.</dl>
<p> For a complete definition of ScrolledWindow and its associated resources, see <code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3).</p>
