---
title: "xgetxcbconnection(3)"
name: "xgetxcbconnection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetxcbconnection/"
---

XGetXCBConnection - get the XCB connection for an Xlib Display
<h2>Syntax</h2><dl COMPACT><dt> 
&nbsp;<wbr>#include&nbsp;<wbr>&lt;X11/Xlib-xcb.h&gt;
<dd>xcb_connection_t *XGetXCBConnection(Display *<i>dpy</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>dpy</i>
<dd>Specifies the connection to the X server.</dl><h2>Description</h2>The <i>XGetXCBConnection</i> function returns the XCB connection associated with an Xlib Display. Clients can use this XCB connection with functions from the XCB library, just as they would with an XCB connection created with XCB. Callers of this function must link to libX11-xcb and a version of Xlib built with XCB support.
<h2>See Also</h2><a HREF="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a>(3), <a HREF="/docs/linux/man/3-xseteventqueueowner/">XSetEventQueueOwner</a>(3), 
 <i>Xlib - C Language X Interface</i>
