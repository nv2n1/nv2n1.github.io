---
title: "xisetclientpointer(3)"
name: "xisetclientpointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xisetclientpointer/"
---

XISetClientPointer, XIGetClientPointer - set or get the ClientPointer device. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>XISetClientPointer( Display *display,
 Window win,
 int deviceid);</pre><pre>Bool XIGetClientPointer( Display *display,
 Window win,
 int *device);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>win
 Specifies a window belonging to the client. May be None.</pre><pre>deviceid
 Specifies the ClientPointer device.</pre><h2>Description</h2><dl COMPACT><dd><pre>The ClientPointer is the device that is percieved to be the
core pointer for non-XI protocol requests and replies. Each
time a protocol message needs device-dependent data and the
device is not explicitly given, the ClientPointer device is
used to obtain the data. For example, a XQueryPointer request
will return the coordinates of the ClientPointer.</pre></dl><dl COMPACT><dd><pre>XISetClientPointer request sets the ClientPointer device for
the client that owns the given window. If win is None, the
requesting client's ClientPointer is set to the device
specified with deviceid. Only master pointer devices can be set
as ClientPointer.</pre></dl><dl COMPACT><dd><pre>XISetClientPointer and can generate a BadDevice and a BadWindow
error.</pre></dl><dl COMPACT><dd><pre>The XIGetClientPointer request returns the ClientPointer's
device ID for the client that owns the given window. If win is
None, the requesting client's ClientPointer is returned.</pre></dl><dl COMPACT><dd><pre>win may be a client ID instead of a window.</pre></dl><dl COMPACT><dd><pre>XIGetClientPointer can generate a BadWindow error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a master pointer device.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 window.</pre></dl>
