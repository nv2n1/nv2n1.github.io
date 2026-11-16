---
title: "xmmainwindowsetareas(3)"
name: "xmmainwindowsetareas"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmainwindowsetareas/"
description: "XmMainWindowSetAreas — A MainWindow function that identifies manageable children for each area"
---

<p><code>XmMainWindowSetAreas</code> &#8212; A MainWindow function that identifies manageable children for each area</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MainW.h&gt;
<code>void XmMainWindowSetAreas</code>(
<code>Widget widget</code>,
<code>Widget menu_bar</code>,
<code>Widget command_window</code>,
<code>Widget horizontal_scrollbar</code>,
<code>Widget vertical_scrollbar</code>,
<code>Widget work_region</code>);</pre>
<h2>Description</h2>
<p><code>XmMainWindowSetAreas</code> identifies which of the valid children for each area (such as the MenuBar and work region) are to be actively managed by MainWindow. This function also sets up or adds the MenuBar, work window, command window, and ScrollBar widgets to the application&#8217;s main window widget. </p>
<p> Each area is optional; therefore, the user can pass NULL to one or more of the following arguments. The window manager provides the title bar. </p>
<p> <code>NOTE:</code> <code>XmMainWindowSetAreas</code> is obsolete and exists for compatibility with previous releases. The information previously returned by this function can now be obtained through a call to <code>XtGetValues</code> on the <code>XmNscrolledWindowChildType</code> resource.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the MainWindow widget ID.</dd>
<dt><i>menu_bar</i></dt>
<dd>Specifies the widget ID for the MenuBar to be associated with the MainWindow widget. Set this ID only after creating an instance of the MainWindow widget. The attribute name associated with this argument is <code>XmNmenuBar</code>.</dd>
<dt><i>command_window</i></dt>
<dd>Specifies the widget ID for the command window to be associated with the MainWindow widget. Set this ID only after creating an instance of the MainWindow widget. The attribute name associated with this argument is <code>XmNcommandWindow</code>.</dd>
<dt><i>horizontal_scrollbar</i></dt>
<dd>Specifies the ScrollBar widget ID for the horizontal ScrollBar to be associated with the MainWindow widget. Set this ID only after creating an instance of the MainWindow widget. The attribute name associated with this argument is <code>XmNhorizontalScrollBar</code>.</dd>
<dt><i>vertical_scrollbar</i></dt>
<dd>Specifies the ScrollBar widget ID for the vertical ScrollBar to be associated with the MainWindow widget. Set this ID only after creating an instance of the MainWindow widget. The attribute name associated with this argument is <code>XmNverticalScrollBar</code>.</dd>
<dt><i>work_region</i></dt>
<dd>Specifies the widget ID for the work window to be associated with the MainWindow widget. Set this ID only after creating an instance of the MainWindow widget. The attribute name associated with this argument is <code>XmNworkWindow</code>.</dd></dl>
<p> For a complete definition of MainWindow and its associated resources, see <code><a href="/docs/linux/man/3-xmmainwindow/">XmMainWindow</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmainwindow/">XmMainWindow</a></code>(3).</p>
