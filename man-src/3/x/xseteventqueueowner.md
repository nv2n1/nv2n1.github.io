---
title: "xseteventqueueowner(3)"
name: "xseteventqueueowner"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xseteventqueueowner/"
---

XSetEventQueueOwner - set event queue owner on a shared Xlib/XCB connection
<h2>Syntax</h2><dl COMPACT><dt> 
&nbsp;<wbr>#include&nbsp;<wbr>&lt;X11/Xlib-xcb.h&gt;
<dd>void XSetEventQueueOwner(Display *<i>dpy</i>, enum XEventQueueOwner <i>owner</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>dpy</i>
<dd>Specifies the connection to the X server.
<dt><i>owner</i>
<dd>Specifies the event queue ownership:
<dl COMPACT><dd><dl COMPACT><dt><i>XlibOwnsEventQueue</i> (default)
<dd>Xlib owns the event queue. Use the Xlib event-handling functions. Do not call the XCB event-handling functions.
<dt><i>XCBOwnsEventQueue</i>
<dd>XCB owns the event queue. Use the XCB event-handling functions. Do not call the Xlib event-handling functions.</dl></dl>
</dl><h2>Description</h2>While a client using Xlib/XCB can issue requests and handle their replies or errors with either Xlib or XCB, only one can own and handle the event queue. By default, Xlib must own the event queue, for compatibility with legacy Xlib clients. Clients can call <i>XSetEventQueueOwner</i> immediately after <i>XOpenDisplay</i> to let XCB own the event queue instead. Clients may not call <i>XSetEventQueueOwner</i> at any other time, as this will potentially lose responses.
<h2>See Also</h2><a HREF="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a>(3), <a HREF="/docs/linux/man/3-xgetxcbconnection/">XGetXCBConnection</a>(3), 
 <i>Xlib - C Language X Interface</i>
