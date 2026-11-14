---
title: "xsetselectionowner(3)"
name: "xsetselectionowner"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetselectionowner/"
description: "XSetSelectionOwner, XGetSelectionOwner, XConvertSelection – manipulate window selection"
---

<p>XSetSelectionOwner, XGetSelectionOwner, XConvertSelection &#8211; manipulate window selection </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetSelectionOwner(Display *<i>display</i>, Atom <i>selection</i>, Window <i>owner</i>, Time <i>time</i>);</p>
<dd>Window XGetSelectionOwner(Display *<i>display</i>, Atom <i>selection</i>);</p>
<dd>int XConvertSelection(Display *<i>display</i>, Atom <i>selection</i>, Atom <i>target</i>, Atom <i>property</i>, Window <i>requestor</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>owner</i></p>
<dd>Specifies the owner of the specified selection atom. You can pass a window or <code>None</code>.</p>
<dt><i>property</i></p>
<dd>Specifies the property name. You also can pass <code>None</code>.</p>
<dt><i>requestor</i></p>
<dd>Specifies the requestor.</p>
<dt><i>selection</i></p>
<dd>Specifies the selection atom.</p>
<dt><i>target</i></p>
<dd>Specifies the target atom.</p>
<dt><i>time</i></p>
<dd>Specifies the time. You can pass either a timestamp or <code>CurrentTime</code>.</dl>
<h2>Description</h2>
<p>The <code>XSetSelectionOwner</code> function changes the owner and last-change time for the specified selection and has no effect if the specified time is earlier than the current last-change time of the specified selection or is later than the current X server time. Otherwise, the last-change time is set to the specified time, with <code>CurrentTime</code> replaced by the current server time. If the owner window is specified as <code>None</code>, then the owner of the selection becomes <code>None</code> (that is, no owner). Otherwise, the owner of the selection becomes the client executing the request. </p>
<p> If the new owner (whether a client or <code>None</code>) is not the same as the current owner of the selection and the current owner is not <code>None</code>, the current owner is sent a <code>SelectionClear</code> event. If the client that is the owner of a selection is later terminated (that is, its connection is closed) or if the owner window it has specified in the request is later destroyed, the owner of the selection automatically reverts to <code>None</code>, but the last-change time is not affected. The selection atom is uninterpreted by the X server. <code>XGetSelectionOwner</code> returns the owner window, which is reported in <code>SelectionRequest</code> and <code>SelectionClear</code> events. Selections are global to the X server. </p>
<p> <code>XSetSelectionOwner</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetSelectionOwner</code> function returns the window ID associated with the window that currently owns the specified selection. If no selection was specified, the function returns the constant <code>None</code>. If <code>None</code> is returned, there is no owner for the selection. </p>
<p> <code>XGetSelectionOwner</code> can generate a <code>BadAtom</code> error. </p>
<p> <code>XConvertSelection</code> requests that the specified selection be converted to the specified target type:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If the specified selection has an owner, the X server sends a <code>SelectionRequest</code> event to that owner.</p>
<dt>&bull;</p>
<dd>If no owner for the specified selection exists, the X server generates a <code>SelectionNotify</code> event to the requestor with property <code>None</code>.</dl>
<p> The arguments are passed on unchanged in either of the events. There are two predefined selection atoms: PRIMARY and SECONDARY. </p>
<p> <code>XConvertSelection</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
