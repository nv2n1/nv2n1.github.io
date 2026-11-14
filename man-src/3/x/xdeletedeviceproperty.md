---
title: "xdeletedeviceproperty(3)"
name: "xdeletedeviceproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdeletedeviceproperty/"
---

XGetDeviceProperty, XChangeDeviceProperty, XDeleteDeviceProperty - Get, change or delete a device's property. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>int XGetDeviceProperty( Display *display,
 XDevice *device,
 Atom property,
 long offset,
 long length,
 Bool delete,
 Atom req_type,
 Atom *actual_type_return,
 int *actual_format_return,
 unsigned long *nitems_return,
 unsigned long *bytes_after_return,
 unsigned char **prop_return)</pre><pre>void XChangeDeviceProperty( Display *display,
 XDevice *device,
 Atom property,
 Atom type,
 int format,
 int mode,
 const char *data,
 int nelements)</pre><pre>void XDeleteDeviceProperty( Display *display,
 XDevice *device,
 Atom property)</pre><pre>actual_type_return
 Returns an atom identifier that defines the actual type
 of the property.</pre><pre>actual_format_return
 Returns the actual format of the property.</pre><pre>bytes_after_return
 Returns the number of bytes remaining to be read in the
 property if a partial read was performed.</pre><pre>data
 Specifies the property data.</pre><pre>delete
 Specifies a Boolean value that determines whether the
 property is deleted.</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 The device to grab.</pre><pre>format
 Specifies whether the data should be viewed as a list of
 8-bit, 16-bit, or 32-bit quantities. Possible values are
 8, 16, and 32. This information allows the X server to
 correctly perform byte-swap operations as necessary. If
 the format is 16-bit or 32-bit, you must explicitly cast
 the data pointer to an (unsigned char*) in the call to
 XChangeDeviceProperty.</pre><pre>length
 Specifies the length in 32-bit multiplies of the data to
 be retrieved.</pre><pre>mode
 Specifies the mode of operation. You can pass
 PropModeReplace, PropModePrepend, or PropModeAppend.</pre><pre>nelements
 Specifies the number of elements in data.</pre><pre>nitems_return
 Returns the actual number of 8-bit, 16-bit, or 32-bit
 items stored in the prop_return array.</pre><pre>num_values
 Specifies the number of elements in the values list.</pre><pre>offset
 Specifies the offset in the specified property (in
 32-bit quantities) where the data is to be retrieved.</pre><pre>property
 Specifies the property to modify or query.</pre><pre>prop_return
 Returns the data in the specified format. If the
 returned format is 8, the returned data is represented
 as a char array. If the returned format is 16, the
 returned data is represented as an array of short int
 type and should be cast to that type to obtain the
 elements. If the returned format is 32, the property
 data will be stored as an array of longs (which in a
 64-bit application will be 64-bit values that are padded
 in the upper 4 bytes).</pre><pre>req_type
 Specifies the atom identifier associated with the
 property type or AnyPropertyType.</pre><h2>Description</h2>The XGetDeviceProperty function returns the actual type of the property; the actual format of the property; the number of 8-bit, 16-bit, or 32-bit items transferred; the number of bytes remaining to be read in the property; and a pointer to the data actually returned. For a detailed description of this function, see the man page to XGetWindowProperty. 

 The XChangeDeviceProperty function alters the property for the specified device and causes the server to generate a XPropertyNotifyEvent event on that device. For a detailed description of this function, see the man page to XChangeProperty. 

 The XDeleteDeviceProperty function deletes the specified device property. Note that a client cannot delete a property created by a driver or the server. Attempting to do so will result in a BadAtom error. 

 XGetDeviceProperty can generate a BadAtom, BadDevice error. 

 XChangeDeviceProperty can generate a BadDevice, a BadMatch, a BadAtom, and a BadValue error. 

 XDeleteDeviceProperty can generate a BadDevice, and a BadAtom error.
<h2>Diagnosis</h2><dl COMPACT><dd><pre>BadAtom
 A value does not describe a valid named identifier or
 the client attempted to remove a driver-allocated
 property.</pre></dl><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XListDeviceProperties/">XListDeviceProperties</a>(3)</pre></dl>
