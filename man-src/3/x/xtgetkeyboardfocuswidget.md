---
title: "xtgetkeyboardfocuswidget(3)"
name: "xtgetkeyboardfocuswidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetkeyboardfocuswidget/"
description: "XtGetKeyboardFocusWidget – extension event handling"
---

<p>XtGetKeyboardFocusWidget &#8211; extension event handling </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtGetKeyboardFocusWidget(Widget <i>widget</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget for this event handler. Must be of class Core or any subclass thereof.</dl>
<h2>Description</h2>
<p><code>XtGetKeyboardFocusWidget</code> function returns the widget that would be the end result of keyboard event forwarding for a keyboard event for the specified widget.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtinserteventtypehandler/">XtInsertEventTypeHandler</a>(3), <a href="/docs/linux/man/3-xtremoveeventtypehandler/">XtRemoveEventTypeHandler</a>(3), <a href="/docs/linux/man/3-xtregisterextensionselector/">XtRegisterExtensionSelector</a>(3), <a href="/docs/linux/man/3-xtseteventdispatcher/">XtSetEventDispatcher</a>(3), <a href="/docs/linux/man/3-xtdispatcheventtowidget/">XtDispatchEventToWidget</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
