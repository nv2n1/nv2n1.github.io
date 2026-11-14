---
title: "tcl_getbytearrayfromobj(3)"
name: "tcl_getbytearrayfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getbytearrayfromobj/"
description: "Tcl_NewByteArrayObj, Tcl_SetByteArrayObj, Tcl_GetByteArrayFromObj, Tcl_SetByteArrayLength – manipulate Tcl objects as a arrays of bytes"
---

<p>Tcl_NewByteArrayObj, Tcl_SetByteArrayObj, Tcl_GetByteArrayFromObj, Tcl_SetByteArrayLength &#8211; manipulate Tcl objects as a arrays of bytes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewByteArrayObj</code>(<i>bytes, length</i>)
void 
<code>Tcl_SetByteArrayObj</code>(<i>objPtr, bytes, length</i>)
unsigned char *
<code>Tcl_GetByteArrayFromObj</code>(<i>objPtr, lengthPtr</i>)
unsigned char *
<code>Tcl_SetByteArrayLength</code>(<i>objPtr, length</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const unsigned char <i>*bytes</i> (in) The array of bytes used to initialize or set a byte-array object.</p>
<dd>int <i>length</i> (in) The length of the array of bytes. It must be &gt;= 0.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) For <code>Tcl_SetByteArrayObj</code>, this points to the object to be converted to byte-array type. For <code>Tcl_GetByteArrayFromObj</code> and <code>Tcl_SetByteArrayLength</code>, this points to the object from which to get the byte-array value; if <i>objPtr</i> does not already point to a byte-array object, it will be converted to one.</p>
<dd>int <i>*lengthPtr</i> (out) If non-NULL, filled with the length of the array of bytes in the object. </p>
</dl>
<h2>Description</h2>
<p>These procedures are used to create, modify, and read Tcl byte-array objects from C code. Byte-array objects are typically used to hold the results of binary IO operations or data structures created with the <code>binary</code> command. In Tcl, an array of bytes is not equivalent to a string. Conceptually, a string is an array of Unicode characters, while a byte-array is an array of 8-bit quantities with no implicit meaning. Accessor functions are provided to get the string representation of a byte-array or to convert an arbitrary object to a byte-array. Obtaining the string representation of a byte-array object (by calling <code>Tcl_GetStringFromObj</code>) produces a properly formed UTF-8 sequence with a one-to-one mapping between the bytes in the internal representation and the UTF-8 characters in the string representation. </p>
<p> <code>Tcl_NewByteArrayObj</code> and <code>Tcl_SetByteArrayObj</code> will create a new object of byte-array type or modify an existing object to have a byte-array type. Both of these procedures set the object&#8217;s type to be byte-array and set the object&#8217;s internal representation to a copy of the array of bytes given by <i>bytes</i>. <code>Tcl_NewByteArrayObj</code> returns a pointer to a newly allocated object with a reference count of zero. <code>Tcl_SetByteArrayObj</code> invalidates any old string representation and, if the object is not already a byte-array object, frees any old internal representation. </p>
<p> <code>Tcl_GetByteArrayFromObj</code> converts a Tcl object to byte-array type and returns a pointer to the object&#8217;s new internal representation as an array of bytes. The length of this array is stored in <i>lengthPtr</i> if <i>lengthPtr</i> is non-NULL. The storage for the array of bytes is owned by the object and should not be freed. The contents of the array may be modified by the caller only if the object is not shared and the caller invalidates the string representation. </p>
<p> <code>Tcl_SetByteArrayLength</code> converts the Tcl object to byte-array type and changes the length of the object&#8217;s internal representation as an array of bytes. If <i>length</i> is greater than the space currently allocated for the array, the array is reallocated to the new length; the newly allocated bytes at the end of the array have arbitrary values. If <i>length</i> is less than the space currently allocated for the array, the length of array is reduced to the new length. The return value is a pointer to the object&#8217;s new array of bytes. </p>
<h2>See Also</h2>
<p>Tcl_GetStringFromObj, Tcl_NewObj, Tcl_IncrRefCount, Tcl_DecrRefCount </p>
<h2>Keywords</h2>
<p>object, byte array, utf, unicode, internationalization</p>
