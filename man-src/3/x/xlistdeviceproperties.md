---
title: "xlistdeviceproperties(3)"
name: "xlistdeviceproperties"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xlistdeviceproperties/"
---

XListDeviceProperties - List a device's properties. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>Atom* XListDeviceProperties( Display *display,
 XDevice *device,
 int *nprops_return);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 The device to list the properties for.</pre><pre>nprops_return
 Specifies the number of Atoms returned.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XListDeviceProperties function returns a list of the
properties associated with the input device specified in
device. Each device may have an arbitrary number of properties
attached, some of which were created by the driver and/or
server, others created by clients at runtime.</pre></dl><dl COMPACT><dd><pre>The client is expected to free the list of properties using
XFree.</pre></dl><dl COMPACT><dd><pre>XListDeviceProperties can generate a BadDevice error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XChangeDeviceProperty/">XChangeDeviceProperty</a>(3),
<a HREF="//www.systutorials.com/docs/linux/man/3-XGetDeviceProperty/">XGetDeviceProperty</a>(3),
<a HREF="//www.systutorials.com/docs/linux/man/3-XDeleteDeviceProperty/">XDeleteDeviceProperty</a>(3)</pre></dl>
