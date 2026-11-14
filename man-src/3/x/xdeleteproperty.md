---
title: "xdeleteproperty(3)"
name: "xdeleteproperty"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdeleteproperty/"
description: "XGetWindowProperty, XListProperties, XChangeProperty, XRotateWindowProperties, XDeleteProperty – obtain and change window properties"
---

<p>XGetWindowProperty, XListProperties, XChangeProperty, XRotateWindowProperties, XDeleteProperty &#8211; obtain and change window properties </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XGetWindowProperty(Display *<i>display</i>, Window <i>w</i>, Atom <i>property</i>, long <i>long_offset</i>, long <i>long_length</i>, Bool <i>delete</i>, Atom <i>req_type</i>, Atom *<i>actual_type_return</i>, int *<i>actual_format_return</i>, unsigned long *<i>nitems_return</i>, unsigned long *<i>bytes_after_return</i>, unsigned char **<i>prop_return</i>);</p>
<dd>Atom *XListProperties(Display *<i>display</i>, Window <i>w</i>, int *<i>num_prop_return</i>);</p>
<dd>int XChangeProperty(Display *<i>display</i>, Window <i>w</i>, Atom <i>property</i>, Atom <i>type</i>, int <i>format</i>, int <i>mode</i>, unsigned char *<i>data</i>, int <i>nelements</i>);</p>
<dd>int XRotateWindowProperties(Display *<i>display</i>, Window <i>w</i>, Atom <i>properties</i>[], int <i>num_prop</i>, int <i>npositions</i>);</p>
<dd>int XDeleteProperty(Display *<i>display</i>, Window <i>w</i>, Atom <i>property</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>actual_format_return</i></p>
<dd>Returns the actual format of the property.</p>
<dt><i>actual_type_return</i></p>
<dd>Returns the atom identifier that defines the actual type of the property.</p>
<dt><i>bytes_after_return</i></p>
<dd>Returns the number of bytes remaining to be read in the property if a partial read was performed.</p>
<dt><i>data</i></p>
<dd>Specifies the property data.</p>
<dt><i>delete</i></p>
<dd>Specifies a Boolean value that determines whether the property is deleted.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>format</i></p>
<dd>Specifies whether the data should be viewed as a list of 8-bit, 16-bit, or 32-bit quantities. Possible values are 8, 16, and 32. This information allows the X server to correctly perform byte-swap operations as necessary. If the format is 16-bit or 32-bit, you must explicitly cast your data pointer to an (unsigned char *) in the call to <code>XChangeProperty</code>.</p>
<dt><i>long_length</i></p>
<dd>Specifies the length in 32-bit multiples of the data to be retrieved.</p>
<dt><i>long_offset</i></p>
<dd>Specifies the offset in the specified property (in 32-bit quantities) where the data is to be retrieved.</p>
<dt><i>mode</i></p>
<dd>Specifies the mode of the operation. You can pass <code>PropModeReplace</code>, <code>PropModePrepend</code>, or <code>PropModeAppend</code>.</p>
<dt><i>nelements</i></p>
<dd>Specifies the number of elements of the specified data format.</p>
<dt><i>nitems_return</i></p>
<dd>Returns the actual number of 8-bit, 16-bit, or 32-bit items stored in the prop_return data.</p>
<dt><i>num_prop</i></p>
<dd>Specifies the length of the properties array.</p>
<dt><i>num_prop_return</i></p>
<dd>Returns the length of the properties array.</p>
<dt><i>npositions</i></p>
<dd>Specifies the rotation amount.</p>
<dt><i>prop_return</i></p>
<dd>Returns the data in the specified format. If the returned format is 8, the returned data is represented as a char array. If the returned format is 16, the returned data is represented as a array of short int type and should be cast to that type to obtain the elements. If the returned format is 32, the property data will be stored as an array of longs (which in a 64-bit application will be 64-bit values that are padded in the upper 4 bytes).</p>
<dt><i>property</i></p>
<dd>Specifies the property name.</p>
<dt><i>properties</i></p>
<dd>Specifies the array of properties that are to be rotated.</p>
<dt><i>req_type</i></p>
<dd>Specifies the atom identifier associated with the property type or <code>AnyPropertyType</code>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of the property. The X server does not interpret the type but simply passes it back to an application that later calls <code>XGetWindowProperty</code>.</p>
<dt><i>w</i></p>
<dd>Specifies the window whose property you want to obtain, change, rotate or delete.</dl>
<h2>Description</h2>
<p>The <code>XGetWindowProperty</code> function returns the actual type of the property; the actual format of the property; the number of 8-bit, 16-bit, or 32-bit items transferred; the number of bytes remaining to be read in the property; and a pointer to the data actually returned. <code>XGetWindowProperty</code> sets the return arguments as follows:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If the specified property does not exist for the specified window, <code>XGetWindowProperty</code> returns <code>None</code> to actual_type_return and the value zero to actual_format_return and bytes_after_return. The nitems_return argument is empty. In this case, the delete argument is ignored.</p>
<dt>&bull;</p>
<dd>If the specified property exists but its type does not match the specified type, <code>XGetWindowProperty</code> returns the actual property type to actual_type_return, the actual property format (never zero) to actual_format_return, and the property length in bytes (even if the actual_format_return is 16 or 32) to bytes_after_return. It also ignores the delete argument. The nitems_return argument is empty.</p>
<dt>&bull;</p>
<dd>If the specified property exists and either you assign <code>AnyPropertyType</code> to the req_type argument or the specified type matches the actual property type, <code>XGetWindowProperty</code> returns the actual property type to actual_type_return and the actual property format (never zero) to actual_format_return. It also returns a value to bytes_after_return and nitems_return, by defining the following values:</p>
<dd>
<pre> N = actual length of the stored property in bytes
 (even if the format is 16 or 32)
 I = 4 * long_offset
 T = N - I
 L = MINIMUM(T, 4 * long_length)
 A = N - (I + L)</pre>
<dd>The returned value starts at byte index I in the property (indexing from zero), and its length in bytes is L. If the value for long_offset causes L to be negative, a <code>BadValue</code> error results. The value of bytes_after_return is A, giving the number of trailing unread bytes in the stored property.</dl>
<p> If the returned format is 8, the returned data is represented as a <code>char</code> array. If the returned format is 16, the returned data is represented as a <code>short</code> array and should be cast to that type to obtain the elements. If the returned format is 32, the returned data is represented as a <code>long</code> array and should be cast to that type to obtain the elements. </p>
<p> <code>XGetWindowProperty</code> always allocates one extra byte in prop_return (even if the property is zero length) and sets it to zero so that simple properties consisting of characters do not have to be copied into yet another string before use. </p>
<p> If delete is <code>True</code> and bytes_after_return is zero, <code>XGetWindowProperty</code> deletes the property from the window and generates a <code>PropertyNotify</code> event on the window. </p>
<p> The function returns <code>Success</code> if it executes successfully. To free the resulting data, use <code>XFree</code>. </p>
<p> <code>XGetWindowProperty</code> can generate <code>BadAtom</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XListProperties</code> function returns a pointer to an array of atom properties that are defined for the specified window or returns NULL if no properties were found. To free the memory allocated by this function, use <code>XFree</code>. </p>
<p> <code>XListProperties</code> can generate a <code>BadWindow</code> error. </p>
<p> The <code>XChangeProperty</code> function alters the property for the specified window and causes the X server to generate a <code>PropertyNotify</code> event on that window. <code>XChangeProperty</code> performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If mode is <code>PropModeReplace</code>, <code>XChangeProperty</code> discards the previous property value and stores the new data.</p>
<dt>&bull;</p>
<dd>If mode is <code>PropModePrepend</code> or <code>PropModeAppend</code>, <code>XChangeProperty</code> inserts the specified data before the beginning of the existing data or onto the end of the existing data, respectively. The type and format must match the existing property value, or a <code>BadMatch</code> error results. If the property is undefined, it is treated as defined with the correct type and format with zero-length data.</dl>
<p> If the specified format is 8, the property data must be a <code>char</code> array. If the specified format is 16, the property data must be a <code>short</code> array. If the specified format is 32, the property data must be a <code>long</code> array. </p>
<p> The lifetime of a property is not tied to the storing client. Properties remain until explicitly deleted, until the window is destroyed, or until the server resets. For a discussion of what happens when the connection to the X server is closed, see section 2.6. The maximum size of a property is server dependent and can vary dynamically depending on the amount of memory the server has available. (If there is insufficient space, a <code>BadAlloc</code> error results.) </p>
<p> <code>XChangeProperty</code> can generate <code>BadAlloc</code>, <code>BadAtom</code>, <code>BadMatch</code>, <code>BadValue</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XRotateWindowProperties</code> function allows you to rotate properties on a window and causes the X server to generate <code>PropertyNotify</code> events. If the property names in the properties array are viewed as being numbered starting from zero and if there are num_prop property names in the list, then the value associated with property name I becomes the value associated with property name (I + npositions) mod N for all I from zero to N &#8211; 1. The effect is to rotate the states by npositions places around the virtual ring of property names (right for positive npositions, left for negative npositions). If npositions mod N is nonzero, the X server generates a <code>PropertyNotify</code> event for each property in the order that they are listed in the array. If an atom occurs more than once in the list or no property with that name is defined for the window, a <code>BadMatch</code> error results. If a <code>BadAtom</code> or <code>BadMatch</code> error results, no properties are changed. </p>
<p> <code>XRotateWindowProperties</code> can generate <code>BadAtom</code>, <code>BadMatch</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XDeleteProperty</code> function deletes the specified property only if the property was defined on the specified window and causes the X server to generate a <code>PropertyNotify</code> event on the window unless the property does not exist. </p>
<p> <code>XDeleteProperty</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xinternatom/">XInternAtom</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
