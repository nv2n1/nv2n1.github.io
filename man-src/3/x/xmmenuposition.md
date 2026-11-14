---
title: "xmmenuposition(3)"
name: "xmmenuposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmenuposition/"
description: "XmMenuPosition — A RowColumn function that positions a Popup menu pane"
---

<p><code>XmMenuPosition</code> &#8212; A RowColumn function that positions a Popup menu pane</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>void XmMenuPosition</code>(
<code>Widget menu</code>,
<code>XButtonPressedEvent * event</code>);</pre>
<h2>Description</h2>
<p><code>XmMenuPosition</code> positions a Popup menu pane using the information in the specified event. Unless an application is positioning the menu pane itself, it must first invoke this function before managing the PopupMenu. The <i>x_root</i> and <i>y_root</i> fields in the specified X event are used to determine the menu position.</p>
<dl COMPACT>
<dt><i>menu</i></p>
<dd>Specifies the PopupMenu to be positioned</p>
<dt><i>event</i></p>
<dd>Specifies the event passed to the action procedure which manages the PopupMenu</dl>
<p> Which corner of the PopupMenu is positioned at the <i>x_root</i> and <i>y_root</i> depends on the <code>XmNlayoutDirection</code> resource of the widget from which popup occurs. </p>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
