---
title: "xmcreatepopupmenu(3)"
name: "xmcreatepopupmenu"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatepopupmenu/"
description: "XmCreatePopupMenu — A RowColumn widget convenience creation function"
---

<p><code>XmCreatePopupMenu</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreatePopupMenu</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreatePopupMenu</code> creates an instance of a RowColumn widget of type <code>XmMENU_POPUP</code> and returns the associated widget ID. When this function is used to create the Popup menu pane, a MenuShell widget is automatically created as the parent of the menu pane. The parent of the MenuShell widget is the widget indicated by the <i>parent</i> parameter. </p>
<p> <code>XmCreatePopupMenu</code> is provided as a convenience function for creating RowColumn widgets configured to operate as Popup menu panes and is not implemented as a separate widget class. </p>
<p> The PopupMenu is used as the first menu pane within a PopupMenu system; all other menu panes are of the Pulldown type. A Popup menu pane displays a 3-D shadow, unless the feature is disabled by the application. The shadow appears around the edge of the menu pane. </p>
<p> The Popup menu pane must be created as the child of a MenuShell widget in order to function properly when it is incorporated into a menu. If the application uses this convenience function for creating a Popup menu pane, the MenuShell is automatically created as the real parent of the menu pane. If the application does not use this convenience function to create the RowColumn to function as a Popup menu pane, it is the application&#8217;s responsibility to create the MenuShell widget. </p>
<p> To access the PopupMenu, the application must first position the widget using the <code>XmMenuPosition</code> function and then manage it using <code>XtManageChild</code>.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> Popup menu panes support tear-off capabilities for tear-off menus through <code>XmRowColumn</code> resources. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreatesimplepopupmenu/">XmCreateSimplePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmmenuposition/">XmMenuPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmmenushell/">XmMenuShell</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimplepopupmenu/">XmVaCreateSimplePopupMenu</a></code>(3).</p>
