---
title: "xtaddgrab(3)"
name: "xtaddgrab"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddgrab/"
description: "XtAddGrab, XtRemoveGrab – redirect user input to a modal widget"
---

<p>XtAddGrab, XtRemoveGrab &#8211; redirect user input to a modal widget </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAddGrab(Widget <i>w</i>, Boolean <i>exclusive</i>, Boolean <i>spring_loaded</i>);</p>
<dd>void XtRemoveGrab(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>exclusive</i></p>
<dd>Specifies whether user events should be dispatched exclusively to this widget or also to previous widgets in the cascade.</p>
<dt><i>spring_loaded</i></p>
<dd>Specifies whether this widget was popped up because the user pressed a pointer button.</p>
<dt><i>w</i></p>
<dd>Specifies the widget to add to or remove from the modal cascade.</dl>
<h2>Description</h2>
<p>The <code>XtAddGrab</code> function appends the widget (and associated parameters) to the modal cascade and checks that exclusive is <code>True</code> if spring_loaded is <code>True</code>. If these are not <code>True</code>, <code>XtAddGrab</code> generates an error. </p>
<p> The modal cascade is used by <code>XtDispatchEvent</code> when it tries to dispatch a user event. When at least one modal widget is in the widget cascade, <code>XtDispatchEvent</code> first determines if the event should be delivered. It starts at the most recent cascade entry and follows the cascade up to and including the most recent cascade entry added with the exclusive parameter <code>True</code>. </p>
<p> This subset of the modal cascade along with all descendants of these widgets comprise the active subset. User events that occur outside the widgets in this subset are ignored or remapped. Modal menus with submenus generally add a submenu widget to the cascade with exclusive <code>False</code>. Modal dialog boxes that need to restrict user input to the most deeply nested dialog box add a subdialog widget to the cascade with exclusive <code>True</code>. User events that occur within the active subset are delivered to the appropriate widget, which is usually a child or further descendant of the modal widget. </p>
<p> Regardless of where on the screen they occur, remap events are always delivered to the most recent widget in the active subset of the cascade that has spring_loaded <code>True</code>, if any such widget exists. </p>
<p> The <code>XtRemoveGrab</code> function removes widgets from the modal cascade starting at the most recent widget up to and including the specified widget. It issues an error if the specified widget is not on the modal cascade.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
