---
title: "xgetdevicekeymapping(3)"
name: "xgetdevicekeymapping"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetdevicekeymapping/"
---

XGetDeviceKeyMapping, XChangeDeviceKeyMapping - query or change device key mappings 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>KeySym *XGetDeviceKeyMapping( Display *display,
 XDevice *device,
 KeyCode first_keycode,
 int keycode_count,
 int *keysyms_per_keycode_return);
display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose key mapping is to be queried
 or modified.</pre><pre>first_keycode
 Specifies the first KeyCode to be returned.</pre><pre>keycode_count
 Specifies the number of KeyCodes to be returned or
 modified.</pre><pre>keysyms_per_keycode
 Specifies the number of KeySyms per KeyCode.</pre><pre>keysyms_per_keycode_return
 Specifies the address of a variable into which the
 number of KeySyms per KeyCodewill be returned.</pre><pre>keysyms
 Specifies the address of an array of KeySyms.</pre><h2>Description</h2><dl COMPACT><dd><pre>For the specified device, the XGetDeviceKeyMapping request
returns the symbols for the specified number of KeyCodes
starting with first_keycode. The value specified in
first_keycode must be greater than or equal to min_keycode as
returned by XListInputDevices, or a BadValue error results. In
addition, the following expression must be less than or equal
to max_keycode as returned by XListInputDevices:</pre></dl><dl COMPACT><dd><pre>first_keycode + keycode_count - 1</pre></dl><dl COMPACT><dd><pre>If this is not the case, a BadValue error results. The number
of elements in the KeySyms list is:</pre></dl><dl COMPACT><dd><pre>keycode_count * keysyms_per_keycode_return</pre></dl><dl COMPACT><dd><pre>KeySym number N, counting from zero, for KeyCode K has the
following index in the list, counting from zero: (K -
first_code) * keysyms_per_code_return + N</pre></dl><dl COMPACT><dd><pre>The X server arbitrarily chooses the keysyms_per_keycode_return
value to be large enough to report all requested symbols. A
special KeySym value of NoSymbol is used to fill in unused
elements for individual KeyCodes. To free the storage returned
by XGetDeviceKeyMapping, use XFree.</pre></dl><dl COMPACT><dd><pre>If the specified device does not support input class keys, a
BadMatch error will result.</pre></dl><dl COMPACT><dd><pre>XGetDeviceKeyMapping can generate a BadDevice, BadMatch, or
BadValue error.</pre></dl><dl COMPACT><dd><pre>For the specified device, the XChangeDeviceKeyMapping request
defines the symbols for the specified number of KeyCodes
starting with first_keycode. The symbols for KeyCodes outside
this range remain unchanged. The number of elements in keysyms
must be:</pre></dl><dl COMPACT><dd><pre>num_codes * keysyms_per_keycode</pre></dl><dl COMPACT><dd><pre>The specified first_keycode must be greater than or equal to
min_keycode returned by XListInputDevices, or a BadValue error
results. In addition, the following expression must be less
than or equal to max_keycode as returned by XListInputDevices,
or a BadValue error results:</pre></dl><dl COMPACT><dd><pre>first_keycode + num_codes - 1</pre></dl><dl COMPACT><dd><pre>KeySym number N, counting from zero, for KeyCode K has the
following index in keysyms, counting from zero:</pre></dl><dl COMPACT><dd><pre>(K - first_keycode) * keysyms_per_keycode + N</pre></dl><dl COMPACT><dd><pre>The specified keysyms_per_keycode can be chosen arbitrarily by
the client to be large enough to hold all desired symbols. A
special KeySym value of NoSymbol should be used to fill in
unused elements for individual KeyCodes. It is legal for
NoSymbol to appear in nontrailing positions of the effective
list for a KeyCode.XChangeDeviceKeyMapping generates a
DeviceMappingNotify event that is sent to all clients that have
selected that type of event.</pre></dl><dl COMPACT><dd><pre>There is no requirement that the X server interpret this
mapping. It is merely stored for reading and writing by
clients.</pre></dl><dl COMPACT><dd><pre>If the specified device does not support input class keys, a
BadMatch error results.</pre></dl><dl COMPACT><dd><pre>XChangeDeviceKeyMapping can generate a BadDevice, BadMatch,
BadAlloc, or BadValue error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if the
 specified device is the X keyboard or X pointer device.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XGetDeviceKeyMapping or
 XChangeDeviceKeyMapping request was made specifying a
 device that has no keys.</pre></dl><dl COMPACT><dd><pre>BadValue
 Some numeric value falls outside the range of values
 accepted by the request. Unless a specific range is
 specified for an argument, the full range defined by the
 argument's type is accepted. Any argument defined as a
 set of alternatives can generate this error.</pre></dl><dl COMPACT><dd><pre>BadAlloc
 The server failed to allocate the requested resource or
 server memory.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XSetDeviceButtonMapping/">XSetDeviceButtonMapping</a>(3), XSetDeviceModifierMapping(__3_)</pre></dl>
