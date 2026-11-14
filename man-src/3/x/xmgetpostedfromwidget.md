---
title: "xmgetpostedfromwidget(3)"
name: "xmgetpostedfromwidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetpostedfromwidget/"
description: "XmGetPostedFromWidget — A RowColumn function that returns the widget from which a menu was posted"
---

<p><code>XmGetPostedFromWidget</code> &#8212; A RowColumn function that returns the widget from which a menu was posted</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmGetPostedFromWidget</code>(
<code>Widget menu</code>);</pre>
<h2>Description</h2>
<p><code>XmGetPostedFromWidget</code> returns the widget from which a menu was posted. For torn-off menus, this function returns the widget from which the menu was originally torn. An application can use this routine during the activate callback to determine the context in which the menu callback should be interpreted.</p>
<dl COMPACT>
<dt><i>menu</i></p>
<dd>Specifies the widget ID of the menu</dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the widget from which the menu was posted. If the menu is a Popup Menu, the returned widget is the widget from which the menu was popped up. If the menu is a Pulldown Menu, the returned widget is the MenuBar or OptionMenu from which the widget was pulled down.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
