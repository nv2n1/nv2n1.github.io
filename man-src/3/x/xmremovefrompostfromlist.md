---
title: "xmremovefrompostfromlist(3)"
name: "xmremovefrompostfromlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmremovefrompostfromlist/"
description: "XmRemoveFromPostFromList — a RowColumn function that disables a menu for a particular widget"
---

<p><code>XmRemoveFromPostFromList</code> &#8212; a RowColumn function that disables a menu for a particular widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>void XmRemoveFromPostFromList</code>(
<code>Widget menu</code>,
<code>Widget post_from_widget</code>);</pre>
<h2>Description</h2>
<p><code>XmRemoveFromPostFromList</code> makes a Popup or Pulldown menu no longer accessible from a widget. This function does not destroy a menu, or deallocate the memory associated with it. It simply removes the widget from the menu&#8217;s list of widgets permitted to post that menu. </p>
<p> If the <i>menu</i> argument refers to a Popup menu, the event handlers are removed from the <i>post_from_widget</i> widget. If the argument refers to a Pulldown menu, its ID is removed from the <code>XmNsubMenuId</code> of the specified <i>post_from_widget</i>. Also, if the menu is a Pulldown menu, the <i>post_from_widget</i> widget must be either a CascadeButton or a CascadeButtonGadget.</p>
<dl COMPACT>
<dt><i>menu</i></p>
<dd>Specifies the widget ID of a the Popup or Pulldown menu to be made inaccessible from the <i>post_from_widget</i> widget.</p>
<dt><i>post_from_widget</i></p>
<dd>Specifies the widget ID of the widget which can no longer post the menu referred to by the <i>menu</i> argument..</dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmaddtopostfromlist/">XmAddToPostFromList</a></code>(3), <code><a href="/docs/linux/man/3-xmgetpostedfromwidget/">XmGetPostedFromWidget</a></code>(3), and <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
