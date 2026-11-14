---
title: "xiwarppointer(3)"
name: "xiwarppointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xiwarppointer/"
---

XIWarpPointer - move a device's pointer. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Bool XIWarpPointer( Display *display,
 int deviceid,
 Window src_w,
 Window dest_w,
 double src_x,
 double src_y,
 int src_width,
 int src_height,
 double dest_x,
 double dest_y);</pre><pre>dest_w
 Specifies the destination window or None.</pre><pre>dest_x, dest_y
 Specify the x and y coordinates within the destination
 window.</pre><pre>deviceid
 Specifies the master pointer device or floating slave
 device to move.</pre><pre>display
 Specifies the connection to the X server.</pre><pre>src_x, src_y, src_width, src_height
 Specify a rectangle in the source window.</pre><pre>src_w
 Specifies the source window or None.</pre><h2>Description</h2><dl COMPACT><dd><pre>If dest_w is None, XIWarpPointer moves the pointer by the
offsets (dest_x, dest_y) relative to the current position of
the pointer. If dest_w is a window, XIWarpPointer moves the
pointer to the offsets (dest_x, dest_y) relative to the origin
of dest_w. However, if src_w is a window, the move only takes
place if the window src_w contains the pointer and if the
specified rectangle of src_w contains the pointer.</pre></dl><dl COMPACT><dd><pre>The src_x and src_y coordinates are relative to the origin of
src_w. If src_height is zero, it is replaced with the current
height of src_w minus src_y. If src_width is zero, it is
replaced with the current width of src_w minus src_x.</pre></dl><dl COMPACT><dd><pre>There is seldom any reason for calling this function. The
pointer should normally be left to the user. If you do use this
function, however, it generates events just as if the user had
instantaneously moved the pointer from one position to another.
Note that you cannot use XIWarpPointer to move the pointer
outside the confine_to window of an active pointer grab. An
attempt to do so will only move the pointer as far as the
closest edge of the confine_to window.</pre></dl><dl COMPACT><dd><pre>XIWarpPointer is identical to XWarpPointer but specifies the
device explicitly.</pre></dl><dl COMPACT><dd><pre>XIWarpPointer can generate a BadDevice and a BadWindow error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a pointer device.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 window.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XWarpPointer/">XWarpPointer</a>(3)</pre></dl>
