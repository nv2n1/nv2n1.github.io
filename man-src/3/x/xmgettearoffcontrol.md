---
title: "xmgettearoffcontrol(3)"
name: "xmgettearoffcontrol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgettearoffcontrol/"
description: "XmGetTearOffControl — A RowColumn function that obtains the widget ID for the tear-off control in a menu"
---

<p><code>XmGetTearOffControl</code> &#8212; A RowColumn function that obtains the widget ID for the tear-off control in a menu</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmGetTearOffControl</code>(
<code>Widget menu</code>);</pre>
<h2>Description</h2>
<p><code>XmGetTearOffControl</code> provides the application with the means for obtaining the widget ID of the internally created tear-off control in a tear-off menu. </p>
<p> RowColumn creates a tear-off control for a PulldownMenu or PopupMenu when the <code>XmNtearOffModel</code> resource is initialized or set to <code>XmTEAR_OFF_ENABLED</code>. The tear-off control is a widget that appears as the first element in the menu. The user tears off the menu by means of mouse or keyboard events in the tear-off control. </p>
<p> The tear-off control has Separator-like behavior. Once the application has obtained the widget ID of the tear-off control, it can set resources to specify the appearance of the control. The application or user can also set these resources in a resource file by using the name of the control, which is <code>TearOffControl</code>. For a list of the resources the application or user can set, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<dl COMPACT>
<dt><i>menu</i></p>
<dd>Specifies the widget ID of the RowColumn PulldownMenu or PopupMenu</dl>
<p> For more information on tear-off menus and a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID for the tear-off control, or NULL if no tear-off control exists. An application should not assume that the returned widget will be of any particular class.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
