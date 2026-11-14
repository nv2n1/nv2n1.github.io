---
title: "xsetdevicemode(3)"
name: "xsetdevicemode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetdevicemode/"
---

XSetDeviceMode - change the mode of a device 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XSetDeviceMode( Display *display,
 XDevice *device,
 int mode);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose mode is to be changed.</pre><pre>mode
 Specifies the mode. You can pass Absolute, or Relative.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XSetDeviceMode request changes the mode of an input device
that is capable of reporting either absolute positional
information or relative motion information. Not all input
devices are capable of reporting motion data, and not all are
capable of changing modes from Absolute to Relative.</pre></dl><dl COMPACT><dd><pre>XSetDeviceMode can generate a BadDevice or BadMode error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if some
 other client has caused the specified device to become
 the X keyboard or X pointer device via the
 XChangeKeyboardDevice or XChangePointerDevice requests.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XSetDeviceMode request is
 made specifying a device that has no valuators and
 reports no axes of motion.</pre></dl><dl COMPACT><dd><pre>BadMode
 An invalid mode was specified. This error will also be
 returned if the specified device is not capable of
 supporting the XSetDeviceMode request.</pre></dl>
