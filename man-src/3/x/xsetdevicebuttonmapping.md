---
title: "xsetdevicebuttonmapping(3)"
name: "xsetdevicebuttonmapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetdevicebuttonmapping/"
---

XSetDeviceButtonMapping, XGetDeviceButtonMapping - query or change device button mappings 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>int XSetDeviceButtonMapping( Display *display,
 XDevice *device,
 unsigned char map[],
 int nmap);</pre><pre>int XGetDeviceButtonMapping( Display *display,
 XDevice *device,
 unsigned char map_return[],
 int nmap);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose button mapping is to be
 queried or changed.</pre><pre>map
 Specifies the mapping list.</pre><pre>map_return
 Returns the mapping list.</pre><pre>nmap
 Specifies the number of items in the mapping list.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XSetDeviceButtonMapping request sets the mapping of the
specified device. If it succeeds, the X server generates a
DeviceMappingNotify event, and XSetDeviceButtonMapping returns
MappingSuccess. Element map[i] defines the logical button
number for the physical button i+1. The length of the list must
be the same as XGetDeviceButtonMapping would return, or a
BadValue error results. A zero element disables a button, and
elements are not restricted in value by the number of physical
buttons. However, no two elements can have the same nonzero
value, or a BadValue error results. If any of the buttons to be
altered are logically in the down state,
XSetDeviceButtonMapping returns MappingBusy, and the mapping is
not changed.</pre></dl><dl COMPACT><dd><pre>XSetDeviceButtonMapping can generate BadDevice, BadMatch, and
BadValue errors.</pre></dl><dl COMPACT><dd><pre>The XGetDeviceButtonMapping request returns the current mapping
of the specified device. Buttons are numbered starting from
one.XGetDeviceButtonMapping returns the number of physical
buttons actually on the device. The nominal mapping for a
device is map[i]=i+1. The nmap argument specifies the length of
the array where the device mapping is returned, and only the
first nmap elements are returned in map_return.</pre></dl><dl COMPACT><dd><pre>XGetDeviceButtonMapping can generate BadDevice or BadMatch
errors.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if the
 specified device is the X keyboard or X pointer device.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XGetDeviceButtonMapping or
 XSetDeviceButtonMapping request was made specifying a
 device that has no buttons.</pre></dl><dl COMPACT><dd><pre>BadValue
 Some numeric value falls outside the range of values
 accepted by the request. Unless a specific range is
 specified for an argument, the full range defined by the
 argument's type is accepted. Any argument defined as a
 set of alternatives can generate this error.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XChangeDeviceKeyboardControl/">XChangeDeviceKeyboardControl</a>(3), <a HREF="//www.systutorials.com/docs/linux/man/3-XChangeDeviceKeyMapping/">XChangeDeviceKeyMapping</a>(3),
<a HREF="//www.systutorials.com/docs/linux/man/3-XChangeDeviceModifierMapping/">XChangeDeviceModifierMapping</a>(3)</pre></dl>
