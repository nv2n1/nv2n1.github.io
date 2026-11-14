---
title: "xchangekeyboarddevice(3)"
name: "xchangekeyboarddevice"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xchangekeyboarddevice/"
---

XChangeKeyboardDevice - change which device is used as the X keyboard 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>Status XChangeKeyboardDevice( Display *display,
 XDevice *device);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device to be used as the X keyboard.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XChangeKeyboardDevice request causes the server to use the
specified device as the X keyboard. The device must have been
previously opened by the requesting client via XOpenDevice or a
BadDevice error will result. The device must support input
class Keys, or a BadMatch error will result. If the server
implementation does not support using the requested device as
the X keyboard, a BadDevice error will result.</pre></dl><dl COMPACT><dd><pre>If the specified device is grabbed by another client,
AlreadyGrabbed is returned. If the specified device is frozen
by a grab on another device, GrabFrozen is returned. If the
request is successful, Success is returned.</pre></dl><dl COMPACT><dd><pre>If the request succeeds, a ChangeDeviceNotify event is sent to
all clients that have selected that event. A MappingNotify
event with request = MappingKeyboard is sent to all clients.
The specified device becomes the X keyboard and the old X
keyboard becomes accessible through the input extension
protocol requests.</pre></dl><dl COMPACT><dd><pre>XChangeKeyboardDevice can generate a BadDevice or a BadMatch
error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist, has not been opened by this client via
 XOpenInputDevice, or is already one of the core X device
 (pointer or keyboard). This error may also occur if the
 server implementation does not support using the
 specified device as the X keyboard.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XChangeKeyboardDevice request
 was made specifying a device that has no keys.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XChangePointerDevice/">XChangePointerDevice</a>(3)</pre></dl>
