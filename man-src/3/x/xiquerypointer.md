---
title: "xiquerypointer(3)"
name: "xiquerypointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xiquerypointer/"
---

XIQueryPointer - get device pointer coordinates. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Bool XIQueryPointer( Display *display,
 int deviceid,
 Window win,
 Window *root_return,
 Window *child_return,
 double *root_x_return,
 double *root_y_return,
 double *win_x_return,
 double *win_y_return,
 XIButtonState *buttons_return,
 XIModifierState *modifiers_return,
 XIGroupState *group_return);</pre><pre>buttons_return
 Returns the current button state.</pre><pre>child_return
 Returns the child window that the pointer is located in,
 if any.</pre><pre>deviceid
 Specifies the device to query.</pre><pre>display
 Specifies the connection to the X server.</pre><pre>group_return
 Returns the current group state.</pre><pre>modifiers_return
 Returns the current state of the modifier keys.</pre><pre>root_return
 Returns the root window that the pointer is in.</pre><pre>root_x_return, root_y_return
 Return the pointer coordinates relative to the root
 window's origin.</pre><pre>win
 Specifies the window.</pre><pre>win_x_return, win_y_return
 Return the pointer coordinates relative to the specified
 window.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XIQueryPointer function returns the root window the
device's pointer is logically on and the pointer coordinates
relative to the root window's origin. If XIQueryPointer returns
False, the pointer is not on the same screen as the specified
window, and XIQueryPointer returns None to child_return and
zero to win_x_return and win_y_return. If XIQueryPointer
returns True, the pointer coordinates returned to win_x_return
and win_y_return are relative to the origin of the specified
window. In this case, XIQueryPointer returns the child that
contains the pointer, if any, or else None to child_return.</pre></dl><dl COMPACT><dd><pre>XIQueryPointer returns the current logical state of the buttons
buttons_return. The keyboard paired with the master pointer is
selected to obtain the data for modifiers_return and
group_return.</pre></dl><dl COMPACT><dd><pre>The mask field in buttons_return is dynamically allocated and
must be freed by the caller.</pre></dl><dl COMPACT><dd><pre>XIQueryPointer is identical to XQueryPointer but specifies the
device explicitly.</pre></dl><dl COMPACT><dd><pre>XIQueryPointer can generate a BadDevice and a BadWindow error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a pointer device.</pre></dl><dl COMPACT><dd><pre>BadWindow
 A value for a Window argument does not name a defined
 window.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XQueryPointer/">XQueryPointer</a>(3)</pre></dl>
