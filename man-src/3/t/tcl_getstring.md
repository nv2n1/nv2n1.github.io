---
title: "tcl_getstring(3)"
name: "tcl_getstring"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getstring/"
description: "Tcl_NewStringObj, Tcl_NewUnicodeObj, Tcl_SetStringObj, Tcl_SetUnicodeObj, Tcl_GetStringFromObj, Tcl_GetString, Tcl_GetUnicodeFromObj, Tcl_GetUnicode, Tcl_GetUniChar, Tcl_GetCharLength, Tcl_GetRange..."
---

<p>Tcl_NewStringObj, Tcl_NewUnicodeObj, Tcl_SetStringObj, Tcl_SetUnicodeObj, Tcl_GetStringFromObj, Tcl_GetString, Tcl_GetUnicodeFromObj, Tcl_GetUnicode, Tcl_GetUniChar, Tcl_GetCharLength, Tcl_GetRange, Tcl_AppendToObj, Tcl_AppendUnicodeToObj, Tcl_AppendObjToObj, Tcl_AppendStringsToObj, Tcl_AppendStringsToObjVA, Tcl_AppendLimitedToObj, Tcl_Format, Tcl_AppendFormatToObj, Tcl_ObjPrintf, Tcl_AppendPrintfToObj, Tcl_SetObjLength, Tcl_AttemptSetObjLength, Tcl_ConcatObj &#8211; manipulate Tcl objects as strings </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewStringObj</code>(<i>bytes, length</i>)
Tcl_Obj *
<code>Tcl_NewUnicodeObj</code>(<i>unicode, numChars</i>)
void
<code>Tcl_SetStringObj</code>(<i>objPtr, bytes, length</i>)
void
<code>Tcl_SetUnicodeObj</code>(<i>objPtr, unicode, numChars</i>)
char *
<code>Tcl_GetStringFromObj</code>(<i>objPtr, lengthPtr</i>)
char *
<code>Tcl_GetString</code>(<i>objPtr</i>)
Tcl_UniChar *
<code>Tcl_GetUnicodeFromObj</code>(<i>objPtr, lengthPtr</i>)
Tcl_UniChar *
<code>Tcl_GetUnicode</code>(<i>objPtr</i>)
Tcl_UniChar
<code>Tcl_GetUniChar</code>(<i>objPtr, index</i>)
int
<code>Tcl_GetCharLength</code>(<i>objPtr</i>)
Tcl_Obj *
<code>Tcl_GetRange</code>(<i>objPtr, first, last</i>)
void
<code>Tcl_AppendToObj</code>(<i>objPtr, bytes, length</i>)
void
<code>Tcl_AppendUnicodeToObj</code>(<i>objPtr, unicode, numChars</i>)
void
<code>Tcl_AppendObjToObj</code>(<i>objPtr, appendObjPtr</i>)
void
<code>Tcl_AppendStringsToObj</code>(<i>objPtr, string, string, ... </i><code>(char *) NULL</code>)
void
<code>Tcl_AppendStringsToObjVA</code>(<i>objPtr, argList</i>)
void
<code>Tcl_AppendLimitedToObj</code>(<i>objPtr, bytes, length, limit, ellipsis</i>)
Tcl_Obj *
<code>Tcl_Format</code>(<i>interp, format, objc, objv</i>)
int
<code>Tcl_AppendFormatToObj</code>(<i>interp, objPtr, format, objc, objv</i>)
Tcl_Obj *
<code>Tcl_ObjPrintf</code>(<i>format, ...</i>)
int
<code>Tcl_AppendPrintfToObj</code>(<i>objPtr, format, ...</i>)
void
<code>Tcl_SetObjLength</code>(<i>objPtr, newLength</i>)
int
<code>Tcl_AttemptSetObjLength</code>(<i>objPtr, newLength</i>)
Tcl_Obj *
<code>Tcl_ConcatObj</code>(<i>objc, objv</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char <i>*bytes</i> (in) Points to the first byte of an array of UTF-8-encoded bytes used to set or append to a string object. This byte array may contain embedded null characters unless <i>numChars</i> is negative. (Applications needing null bytes should represent them as the two-byte sequence <i>\700\600</i>, use <code>Tcl_ExternalToUtf</code> to convert, or <code>Tcl_NewByteArrayObj</code> if the string is a collection of uninterpreted bytes.)</p>
<dd>int <i>length</i> (in) The number of bytes to copy from <i>bytes</i> when initializing, setting, or appending to a string object. If negative, all bytes up to the first null are used.</p>
<dd>const Tcl_UniChar <i>*unicode</i> (in) Points to the first byte of an array of Unicode characters used to set or append to a string object. This byte array may contain embedded null characters unless <i>numChars</i> is negative.</p>
<dd>int <i>numChars</i> (in) The number of Unicode characters to copy from <i>unicode</i> when initializing, setting, or appending to a string object. If negative, all characters up to the first null character are used.</p>
<dd>int <i>index</i> (in) The index of the Unicode character to return.</p>
<dd>int <i>first</i> (in) The index of the first Unicode character in the Unicode range to be returned as a new object.</p>
<dd>int <i>last</i> (in) The index of the last Unicode character in the Unicode range to be returned as a new object.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) Points to an object to manipulate.</p>
<dd>Tcl_Obj <i>*appendObjPtr</i> (in) The object to append to <i>objPtr</i> in <code>Tcl_AppendObjToObj</code>.</p>
<dd>int <i>*lengthPtr</i> (out) If non-NULL, the location where <code>Tcl_GetStringFromObj</code> will store the length of an object&#8217;s string representation.</p>
<dd>const char <i>*string</i> (in) Null-terminated string value to append to <i>objPtr</i>.</p>
<dd>va_list <i>argList</i> (in) An argument list which must have been initialised using <code>va_start</code>, and cleared using <code>va_end</code>.</p>
<dd>int <i>limit</i> (in) Maximum number of bytes to be appended.</p>
<dd>const char <i>*ellipsis</i> (in) Suffix to append when the limit leads to string truncation. If NULL is passed then the suffix &quot;&#8230;&quot; is used.</p>
<dd>const char <i>*format</i> (in) Format control string including % conversion specifiers.</p>
<dd>int <i>objc</i> (in) The number of elements to format or concatenate.</p>
<dd>Tcl_Obj <i>*objv[]</i> (in) The array of objects to format or concatenate.</p>
<dd>int <i>newLength</i> (in) New length for the string value of <i>objPtr</i>, not including the final null character. </p>
</dl>
<h2>Description</h2>
<p>The procedures described in this manual entry allow Tcl objects to be manipulated as string values. They use the internal representation of the object to store additional information to make the string manipulations more efficient. In particular, they make a series of append operations efficient by allocating extra storage space for the string so that it does not have to be copied for each append. Also, indexing and length computations are optimized because the Unicode string representation is calculated and cached as needed. When using the <code>Tcl_Append*</code> family of functions where the interpreter&#8217;s result is the object being appended to, it is important to call Tcl_ResetResult first to ensure you are not unintentionally appending to existing data in the result object. </p>
<p> <code>Tcl_NewStringObj</code> and <code>Tcl_SetStringObj</code> create a new object or modify an existing object to hold a copy of the string given by <i>bytes</i> and <i>length</i>. <code>Tcl_NewUnicodeObj</code> and <code>Tcl_SetUnicodeObj</code> create a new object or modify an existing object to hold a copy of the Unicode string given by <i>unicode</i> and <i>numChars</i>. <code>Tcl_NewStringObj</code> and <code>Tcl_NewUnicodeObj</code> return a pointer to a newly created object with reference count zero. All four procedures set the object to hold a copy of the specified string. <code>Tcl_SetStringObj</code> and <code>Tcl_SetUnicodeObj</code> free any old string representation as well as any old internal representation of the object. </p>
<p> <code>Tcl_GetStringFromObj</code> and <code>Tcl_GetString</code> return an object&#8217;s string representation. This is given by the returned byte pointer and (for <code>Tcl_GetStringFromObj</code>) length, which is stored in <i>lengthPtr</i> if it is non-NULL. If the object&#8217;s UTF string representation is invalid (its byte pointer is NULL), the string representation is regenerated from the object&#8217;s internal representation. The storage referenced by the returned byte pointer is owned by the object manager. It is passed back as a writable pointer so that extension author creating their own <code>Tcl_ObjType</code> will be able to modify the string representation within the <code>Tcl_UpdateStringProc</code> of their <code>Tcl_ObjType</code>. Except for that limited purpose, the pointer returned by <code>Tcl_GetStringFromObj</code> or <code>Tcl_GetString</code> should be treated as read-only. It is recommended that this pointer be assigned to a (const char *) variable. Even in the limited situations where writing to this pointer is acceptable, one should take care to respect the copy-on-write semantics required by <code>Tcl_Obj</code>&#8216;s, with appropriate calls to <code>Tcl_IsShared</code> and <code>Tcl_DuplicateObj</code> prior to any in-place modification of the string representation. The procedure <code>Tcl_GetString</code> is used in the common case where the caller does not need the length of the string representation. </p>
<p> <code>Tcl_GetUnicodeFromObj</code> and <code>Tcl_GetUnicode</code> return an object&#8217;s value as a Unicode string. This is given by the returned pointer and (for <code>Tcl_GetUnicodeFromObj</code>) length, which is stored in <i>lengthPtr</i> if it is non-NULL. The storage referenced by the returned byte pointer is owned by the object manager and should not be modified by the caller. The procedure <code>Tcl_GetUnicode</code> is used in the common case where the caller does not need the length of the unicode string representation. </p>
<p> <code>Tcl_GetUniChar</code> returns the <i>index</i>&#8216;th character in the object&#8217;s Unicode representation. </p>
<p> <code>Tcl_GetRange</code> returns a newly created object comprised of the characters between <i>first</i> and <i>last</i> (inclusive) in the object&#8217;s Unicode representation. If the object&#8217;s Unicode representation is invalid, the Unicode representation is regenerated from the object&#8217;s string representation. </p>
<p> <code>Tcl_GetCharLength</code> returns the number of characters (as opposed to bytes) in the string object. </p>
<p> <code>Tcl_AppendToObj</code> appends the data given by <i>bytes</i> and <i>length</i> to the string representation of the object specified by <i>objPtr</i>. If the object has an invalid string representation, then an attempt is made to convert <i>bytes</i> is to the Unicode format. If the conversion is successful, then the converted form of <i>bytes</i> is appended to the object&#8217;s Unicode representation. Otherwise, the object&#8217;s Unicode representation is invalidated and converted to the UTF format, and <i>bytes</i> is appended to the object&#8217;s new string representation. </p>
<p> <code>Tcl_AppendUnicodeToObj</code> appends the Unicode string given by <i>unicode</i> and <i>numChars</i> to the object specified by <i>objPtr</i>. If the object has an invalid Unicode representation, then <i>unicode</i> is converted to the UTF format and appended to the object&#8217;s string representation. Appends are optimized to handle repeated appends relatively efficiently (it overallocates the string or Unicode space to avoid repeated reallocations and copies of object&#8217;s string value). </p>
<p> <code>Tcl_AppendObjToObj</code> is similar to <code>Tcl_AppendToObj</code>, but it appends the string or Unicode value (whichever exists and is best suited to be appended to <i>objPtr</i>) of <i>appendObjPtr</i> to <i>objPtr</i>. </p>
<p> <code>Tcl_AppendStringsToObj</code> is similar to <code>Tcl_AppendToObj</code> except that it can be passed more than one value to append and each value must be a null-terminated string (i.e. none of the values may contain internal null characters). Any number of <i>string</i> arguments may be provided, but the last argument must be a NULL pointer to indicate the end of the list. </p>
<p> <code>Tcl_AppendStringsToObjVA</code> is the same as <code>Tcl_AppendStringsToObj</code> except that instead of taking a variable number of arguments it takes an argument list. </p>
<p> <code>Tcl_AppendLimitedToObj</code> is similar to <code>Tcl_AppendToObj</code> except that it imposes a limit on how many bytes are appended. This can be handy when the string to be appended might be very large, but the value being constructed should not be allowed to grow without bound. A common usage is when constructing an error message, where the end result should be kept short enough to be read. Bytes from <i>bytes</i> are appended to <i>objPtr</i>, but no more than <i>limit</i> bytes total are to be appended. If the limit prevents all <i>length</i> bytes that are available from being appended, then the appending is done so that the last bytes appended are from the string <i>ellipsis</i>. This allows for an indication of the truncation to be left in the string. When <i>length</i> is <code>-1</code>, all bytes up to the first zero byte are appended, subject to the limit. When <i>ellipsis</i> is NULL, the default string <code>&#8230;</code> is used. When <i>ellipsis</i> is non-NULL, it must point to a zero-byte-terminated string in Tcl&#8217;s internal UTF encoding. The number of bytes appended can be less than the lesser of <i>length</i> and <i>limit</i> when appending fewer bytes is necessary to append only whole multi-byte characters. </p>
<p> <code>Tcl_Format</code> is the C-level interface to the engine of the <code>format</code> command. The actual command procedure for <code>format</code> is little more than</p>
<dl COMPACT>
<dd>
<pre>Tcl_Format(interp, Tcl_GetString(objv[1]), objc-2, objv+2);</pre>
</dl>
<p> The <i>objc</i> Tcl_Obj values in <i>objv</i> are formatted into a string according to the conversion specification in <i>format</i> argument, following the documentation for the <code>format</code> command. The resulting formatted string is converted to a new Tcl_Obj with refcount of zero and returned. If some error happens during production of the formatted string, NULL is returned, and an error message is recorded in <i>interp</i>, if <i>interp</i> is non-NULL. </p>
<p> <code>Tcl_AppendFormatToObj</code> is an appending alternative form of <code>Tcl_Format</code> with functionality equivalent to</p>
<dl COMPACT>
<dd>
<pre>Tcl_Obj *newPtr = Tcl_Format(interp, format, objc, objv);
if (newPtr == NULL) return TCL_ERROR;
Tcl_AppendObjToObj(objPtr, newPtr);
return TCL_OK;</pre>
</dl>
<p> but with greater convenience and efficiency when the appending functionality is needed. </p>
<p> <code>Tcl_ObjPrintf</code> serves as a replacement for the common sequence</p>
<dl COMPACT>
<dd>
<pre>char buf[SOME_SUITABLE_LENGTH];
sprintf(buf, format, ...);
Tcl_NewStringObj(buf, -1);</pre>
</dl>
<p> but with greater convenience and no need to determine <code>SOME_SUITABLE_LENGTH</code>. The formatting is done with the same core formatting engine used by <code>Tcl_Format</code>. This means the set of supported conversion specifiers is that of the <code>format</code> command and not that of the <code>sprintf</code> routine where the two sets differ. When a conversion specifier passed to <code>Tcl_ObjPrintf</code> includes a precision, the value is taken as a number of bytes, as <code>sprintf</code> does, and not as a number of characters, as <code>format</code> does. This is done on the assumption that C code is more likely to know how many bytes it is passing around than the number of encoded characters those bytes happen to represent. The variable number of arguments passed in should be of the types that would be suitable for passing to <code>sprintf</code>. Note in this example usage, <i>x</i> is of type <code>long</code>.</p>
<dl COMPACT>
<dd>
<pre>long x = 5;
Tcl_Obj *objPtr = Tcl_ObjPrintf(&quot;Value is %d&quot;, x);</pre>
</dl>
<p> If the value of <i>format</i> contains internal inconsistencies or invalid specifier formats, the formatted string result produced by <code>Tcl_ObjPrintf</code> will be an error message describing the error. </p>
<p> <code>Tcl_AppendPrintfToObj</code> is an appending alternative form of <code>Tcl_ObjPrintf</code> with functionality equivalent to</p>
<dl COMPACT>
<dd>
<pre>Tcl_AppendObjToObj(objPtr, Tcl_ObjPrintf(format, ...));</pre>
</dl>
<p> but with greater convenience and efficiency when the appending functionality is needed. </p>
<p> The <code>Tcl_SetObjLength</code> procedure changes the length of the string value of its <i>objPtr</i> argument. If the <i>newLength</i> argument is greater than the space allocated for the object&#8217;s string, then the string space is reallocated and the old value is copied to the new space; the bytes between the old length of the string and the new length may have arbitrary values. If the <i>newLength</i> argument is less than the current length of the object&#8217;s string, with <i>objPtr-&gt;length</i> is reduced without reallocating the string space; the original allocated size for the string is recorded in the object, so that the string length can be enlarged in a subsequent call to <code>Tcl_SetObjLength</code> without reallocating storage. In all cases <code>Tcl_SetObjLength</code> leaves a null character at <i>objPtr-&gt;bytes[newLength]</i>. </p>
<p> <code>Tcl_AttemptSetObjLength</code> is identical in function to <code>Tcl_SetObjLength</code> except that if sufficient memory to satisfy the request cannot be allocated, it does not cause the Tcl interpreter to <code>panic</code>. Thus, if <i>newLength</i> is greater than the space allocated for the object&#8217;s string, and there is not enough memory available to satisfy the request, <code>Tcl_AttemptSetObjLength</code> will take no action and return 0 to indicate failure. If there is enough memory to satisfy the request, <code>Tcl_AttemptSetObjLength</code> behaves just like <code>Tcl_SetObjLength</code> and returns 1 to indicate success. </p>
<p> The <code>Tcl_ConcatObj</code> function returns a new string object whose value is the space-separated concatenation of the string representations of all of the objects in the <i>objv</i> array. <code>Tcl_ConcatObj</code> eliminates leading and trailing white space as it copies the string representations of the <i>objv</i> array to the result. If an element of the <i>objv</i> array consists of nothing but white space, then that object is ignored entirely. This white-space removal was added to make the output of the <code>concat</code> command cleaner-looking. <code>Tcl_ConcatObj</code> returns a pointer to a newly-created object whose ref count is zero. </p>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_IncrRefCount, Tcl_DecrRefCount, format, sprintf </p>
<h2>Keywords</h2>
<p>append, internal representation, object, object type, string object, string type, string representation, concat, concatenate, unicode</p>
