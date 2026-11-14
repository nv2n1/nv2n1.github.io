---
title: "xmcreatepulldownmenu(3)"
name: "xmcreatepulldownmenu"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatepulldownmenu/"
description: "XmCreatePulldownMenu — A RowColumn widget convenience creation function"
---

<p><code>XmCreatePulldownMenu</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreatePulldownMenu</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreatePulldownMenu</code> creates an instance of a RowColumn widget of type <code>XmMENU_PULLDOWN</code> and returns the associated widget ID.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>). When this function is used to create the Pulldown menu pane, a MenuShell widget is automatically created as the parent of the menu pane. If the widget specified by the <i>parent</i> parameter is a Popup or a Pulldown menu pane, the MenuShell widget is created as a child of the <i>parent</i> MenuShell; otherwise, it is created as a child of the specified <i>parent</i> widget. </p>
<p> <code>XmCreatePulldownMenu</code> is provided as a convenience function for creating RowColumn widgets configured to operate as Pulldown menu panes and is not implemented as a separate widget class. </p>
<p> A Pulldown menu pane displays a 3-D shadow, unless the feature is disabled by the application. The shadow appears around the edge of the menu pane. </p>
<p> A Pulldown menu pane is used with submenus that are to be attached to a CascadeButton or a CascadeButtonGadget. This is the case for all menu panes that are part of a PulldownMenu system (a MenuBar), the menu pane associated with an OptionMenu, and any menu panes that cascade from a Popup menu pane. Pulldown menu panes that are to be associated with an OptionMenu must be created before the OptionMenu is created. </p>
<p> The Pulldown menu pane must be attached to a CascadeButton or CascadeButtonGadget that resides in a MenuBar, a Popup menu pane, a Pulldown menu pane, or an OptionMenu. It is attached with the button resource <code>XmNsubMenuId</code>. </p>
<p> A MenuShell widget is required between the Pulldown menu pane and its parent. If the application uses this convenience function for creating a Pulldown menu pane, the MenuShell is automatically created as the real parent of the menu pane; otherwise, it is the application&#8217;s responsibility to create the MenuShell widget. </p>
<p> To function correctly when incorporated into a menu, the Pulldown menu pane&#8217;s hierarchy must be considered. This hierarchy depends on the type of menu system that is being built, as follows:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If the Pulldown menu pane is to be pulled down from a MenuBar, its <i>parent</i> must be the MenuBar.</p>
<dt> &bull;</p>
<dd>If the Pulldown menu pane is to be pulled down from a Popup or another Pulldown menu pane, its <i>parent</i> must be that Popup or Pulldown menu pane.</p>
<dt> &bull;</p>
<dd>If the Pulldown menu pane is to be pulled down from an OptionMenu, its <i>parent</i> must be the same as the OptionMenu parent.</dl>
<p> PullDown menu panes support tear-off capabilities for tear-off menus through <code>XmRowColumn</code> resources. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepopupmenu/">XmCreatePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplepulldownmenu/">XmCreateSimplePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmmenushell/">XmMenuShell</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimplepulldownmenu/">XmVaCreateSimplePulldownMenu</a></code>(3).</p>
