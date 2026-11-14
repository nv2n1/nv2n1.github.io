---
title: "xidefinecursor(3)"
name: "xidefinecursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xidefinecursor/"
---

XIDefineCursor, XIUndefineCursor - define device cursors. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>int XIDefineCursor( Display *display,
 int deviceid,
 Window win,
 Cursor cursor);</pre><pre>int XIUndefineCursor( Display *display,
 int deviceid,
 Window win);</pre><pre>cursor
 Specifies the cursor that is to be displayed or None.</pre><pre>deviceid
 Specifies the device whose cursor is to change.</pre><pre>display
 Specifies the connection to the X server.</pre><pre>win
 Specifies the window.</pre><h2>Description</h2><dl COMPACT><dd><pre>If a cursor is set, it will be used when the device's pointer
is in the window. If the cursor is None, it is equivalent to
XIUndefineCursor.</pre></dl><dl COMPACT><dd><pre>The deviceid must be a master pointer device or a BadDevice error is
returned.</pre></dl><dl COMPACT><dd><pre>XIDefineCursor can generate BadDevice, BadCursor and BadWindow.</pre></dl><dl COMPACT><dd><pre>The XIUndefineCursor function undoes the effect of a previous
XIDefineCursor for this window. When the pointer is in the
window, the window's default cursor will now be used. If no
default cursor is defined, the parent's cursor for this device
will be used (if defined) or the parent's default cursor will
be used.</pre></dl><dl COMPACT><dd><pre>XIDefineCursor and XIUndefineCursor are identical to
XDefineCursor and XUndefineCursor but specify the device
explicitly.</pre></dl><dl COMPACT><dd><pre>XIUndefineCursor can generate a BadDevice and a BadWindow
error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadCursor
 A value for a cursor argument does not name a defined
 cursor.</pre></dl><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a pointer device.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 window.</pre></dl>
 

 See also 

<dl COMPACT><dd><pre>XDefineCursor, XUndefineCursor</pre></dl>
