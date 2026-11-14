---
title: "xmaddtopostfromlist(3)"
name: "xmaddtopostfromlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmaddtopostfromlist/"
description: "XmAddToPostFromList — a RowColumn function that makes a menu accessible from more than one widget"
---

<p><code>XmAddToPostFromList</code> &#8212; a RowColumn function that makes a menu accessible from more than one widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>void XmAddToPostFromList</code>(
<code>Widget menu</code>,
<code>Widget post_from_widget</code>);</pre>
<h2>Description</h2>
<p><code>XmAddToPostFromList</code> makes a menu accessible from more than one widget. After a menu is once created, this function may be used to make that menu accessible from a second widget. The process may be repeated indefinitely. In other words, where an application would use <code>XmCreatePopupMenu</code> or <code>XmCreatePulldownMenu</code> or their equivalent to create a new menu identical to one that already exists, it can use this function to reuse that earlier menu. </p>
<p> If <i>menu</i> refers to a Popup menu, then the <i>post_from_widget</i> widget can now pop up the specified menu. The actual posting of the menu occurs as it always does, either through an event handler, or the automatic popup menu support (see the <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3) reference page). </p>
<p> If <i>menu</i> refers to a Pulldown menu, its ID is placed in the <code>XmNsubMenuId</code> resource of the specified <i>post_from_widget</i>. In this case, the <i>post_from_widget</i> widget must be either a CascadeButton or a CascadeButtonGadget. </p>
<p> Note that this function manipulates the internal structures themselves, not a copy of them.</p>
<dl COMPACT>
<dt><i>menu</i></p>
<dd>Specifies the ID of the RowColumn widget containing the menu (Popup or Pulldown) to be made accessible from the widget.</p>
<dt><i>post_from_widget</i></p>
<dd>Specifies the widget ID of the widget which will now be able to post the menu specified by <i>menu</i>.</dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmgetpostedfromwidget/">XmGetPostedFromWidget</a></code>(3), <code><a href="/docs/linux/man/3-xmremovefrompostfromlist/">XmRemoveFromPostFromList</a></code>(3), and <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
