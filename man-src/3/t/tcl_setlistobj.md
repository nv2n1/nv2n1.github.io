---
title: "tcl_setlistobj(3)"
name: "tcl_setlistobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setlistobj/"
description: "Tcl_ListObjAppendList, Tcl_ListObjAppendElement, Tcl_NewListObj, Tcl_SetListObj, Tcl_ListObjGetElements, Tcl_ListObjLength, Tcl_ListObjIndex, Tcl_ListObjReplace – manipulate Tcl objects as lists"
---

<p>Tcl_ListObjAppendList, Tcl_ListObjAppendElement, Tcl_NewListObj, Tcl_SetListObj, Tcl_ListObjGetElements, Tcl_ListObjLength, Tcl_ListObjIndex, Tcl_ListObjReplace &#8211; manipulate Tcl objects as lists </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_ListObjAppendList</code>(<i>interp, listPtr, elemListPtr</i>)
int
<code>Tcl_ListObjAppendElement</code>(<i>interp, listPtr, objPtr</i>)
Tcl_Obj *
<code>Tcl_NewListObj</code>(<i>objc, objv</i>)
<code>Tcl_SetListObj</code>(<i>objPtr, objc, objv</i>)
int
<code>Tcl_ListObjGetElements</code>(<i>interp, listPtr, objcPtr, objvPtr</i>)
int
<code>Tcl_ListObjLength</code>(<i>interp, listPtr, intPtr</i>)
int
<code>Tcl_ListObjIndex</code>(<i>interp, listPtr, index, objPtrPtr</i>)
int
<code>Tcl_ListObjReplace</code>(<i>interp, listPtr, first, count, objc, objv</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) If an error occurs while converting an object to be a list object, an error message is left in the interpreter&#8217;s result object unless <i>interp</i> is NULL.</p>
<dd>Tcl_Obj <i>*listPtr</i> (in/out) Points to the list object to be manipulated. If <i>listPtr</i> does not already point to a list object, an attempt will be made to convert it to one.</p>
<dd>Tcl_Obj <i>*elemListPtr</i> (in/out) For <code>Tcl_ListObjAppendList</code>, this points to a list object containing elements to be appended onto <i>listPtr</i>. Each element of *<i>elemListPtr</i> will become a new element of <i>listPtr</i>. If *<i>elemListPtr</i> is not NULL and does not already point to a list object, an attempt will be made to convert it to one.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) For <code>Tcl_ListObjAppendElement</code>, points to the Tcl object that will be appended to <i>listPtr</i>. For <code>Tcl_SetListObj</code>, this points to the Tcl object that will be converted to a list object containing the <i>objc</i> elements of the array referenced by <i>objv</i>.</p>
<dd>int <i>*objcPtr</i> (in) Points to location where <code>Tcl_ListObjGetElements</code> stores the number of element objects in <i>listPtr</i>.</p>
<dd>Tcl_Obj <i>***objvPtr</i> (out) A location where <code>Tcl_ListObjGetElements</code> stores a pointer to an array of pointers to the element objects of <i>listPtr</i>.</p>
<dd>int <i>objc</i> (in) The number of Tcl objects that <code>Tcl_NewListObj</code> will insert into a new list object, and <code>Tcl_ListObjReplace</code> will insert into <i>listPtr</i>. For <code>Tcl_SetListObj</code>, the number of Tcl objects to insert into <i>objPtr</i>.</p>
<dd>Tcl_Obj *const <i>objv[]</i> (in) An array of pointers to objects. <code>Tcl_NewListObj</code> will insert these objects into a new list object and <code>Tcl_ListObjReplace</code> will insert them into an existing <i>listPtr</i>. Each object will become a separate list element.</p>
<dd>int <i>*intPtr</i> (out) Points to location where <code>Tcl_ListObjLength</code> stores the length of the list.</p>
<dd>int <i>index</i> (in) Index of the list element that <code>Tcl_ListObjIndex</code> is to return. The first element has index 0.</p>
<dd>Tcl_Obj <i>**objPtrPtr</i> (out) Points to place where <code>Tcl_ListObjIndex</code> is to store a pointer to the resulting list element object.</p>
<dd>int <i>first</i> (in) Index of the starting list element that <code>Tcl_ListObjReplace</code> is to replace. The list&#8217;s first element has index 0.</p>
<dd>int <i>count</i> (in) The number of elements that <code>Tcl_ListObjReplace</code> is to replace. </p>
</dl>
<h2>Description</h2>
<p>Tcl list objects have an internal representation that supports the efficient indexing and appending. The procedures described in this man page are used to create, modify, index, and append to Tcl list objects from C code. </p>
<p> <code>Tcl_ListObjAppendList</code> and <code>Tcl_ListObjAppendElement</code> both add one or more objects to the end of the list object referenced by <i>listPtr</i>. <code>Tcl_ListObjAppendList</code> appends each element of the list object referenced by <i>elemListPtr</i> while <code>Tcl_ListObjAppendElement</code> appends the single object referenced by <i>objPtr</i>. Both procedures will convert the object referenced by <i>listPtr</i> to a list object if necessary. If an error occurs during conversion, both procedures return <code>TCL_ERROR</code> and leave an error message in the interpreter&#8217;s result object if <i>interp</i> is not NULL. Similarly, if <i>elemListPtr</i> does not already refer to a list object, <code>Tcl_ListObjAppendList</code> will attempt to convert it to one and if an error occurs during conversion, will return <code>TCL_ERROR</code> and leave an error message in the interpreter&#8217;s result object if interp is not NULL. Both procedures invalidate any old string representation of <i>listPtr</i> and, if it was converted to a list object, free any old internal representation. Similarly, <code>Tcl_ListObjAppendList</code> frees any old internal representation of <i>elemListPtr</i> if it converts it to a list object. After appending each element in <i>elemListPtr</i>, <code>Tcl_ListObjAppendList</code> increments the element&#8217;s reference count since <i>listPtr</i> now also refers to it. For the same reason, <code>Tcl_ListObjAppendElement</code> increments <i>objPtr</i>&#8216;s reference count. If no error occurs, the two procedures return <code>TCL_OK</code> after appending the objects. </p>
<p> <code>Tcl_NewListObj</code> and <code>Tcl_SetListObj</code> create a new object or modify an existing object to hold the <i>objc</i> elements of the array referenced by <i>objv</i> where each element is a pointer to a Tcl object. If <i>objc</i> is less than or equal to zero, they return an empty object. The new object&#8217;s string representation is left invalid. The two procedures increment the reference counts of the elements in <i>objc</i> since the list object now refers to them. The new list object returned by <code>Tcl_NewListObj</code> has reference count zero. </p>
<p> <code>Tcl_ListObjGetElements</code> returns a count and a pointer to an array of the elements in a list object. It returns the count by storing it in the address <i>objcPtr</i>. Similarly, it returns the array pointer by storing it in the address <i>objvPtr</i>. The memory pointed to is managed by Tcl and should not be freed or written to by the caller. If the list is empty, 0 is stored at <i>objcPtr</i> and NULL at <i>objvPtr</i>. If <i>listPtr</i> is not already a list object, <code>Tcl_ListObjGetElements</code> will attempt to convert it to one; if the conversion fails, it returns <code>TCL_ERROR</code> and leaves an error message in the interpreter&#8217;s result object if <i>interp</i> is not NULL. Otherwise it returns <code>TCL_OK</code> after storing the count and array pointer. </p>
<p> <code>Tcl_ListObjLength</code> returns the number of elements in the list object referenced by <i>listPtr</i>. It returns this count by storing an integer in the address <i>intPtr</i>. If the object is not already a list object, <code>Tcl_ListObjLength</code> will attempt to convert it to one; if the conversion fails, it returns <code>TCL_ERROR</code> and leaves an error message in the interpreter&#8217;s result object if <i>interp</i> is not NULL. Otherwise it returns <code>TCL_OK</code> after storing the list&#8217;s length. </p>
<p> The procedure <code>Tcl_ListObjIndex</code> returns a pointer to the object at element <i>index</i> in the list referenced by <i>listPtr</i>. It returns this object by storing a pointer to it in the address <i>objPtrPtr</i>. If <i>listPtr</i> does not already refer to a list object, <code>Tcl_ListObjIndex</code> will attempt to convert it to one; if the conversion fails, it returns <code>TCL_ERROR</code> and leaves an error message in the interpreter&#8217;s result object if <i>interp</i> is not NULL. If the index is out of range, that is, <i>index</i> is negative or greater than or equal to the number of elements in the list, <code>Tcl_ListObjIndex</code> stores a NULL in <i>objPtrPtr</i> and returns <code>TCL_OK</code>. Otherwise it returns <code>TCL_OK</code> after storing the element&#8217;s object pointer. The reference count for the list element is not incremented; the caller must do that if it needs to retain a pointer to the element. </p>
<p> <code>Tcl_ListObjReplace</code> replaces zero or more elements of the list referenced by <i>listPtr</i> with the <i>objc</i> objects in the array referenced by <i>objv</i>. If <i>listPtr</i> does not point to a list object, <code>Tcl_ListObjReplace</code> will attempt to convert it to one; if the conversion fails, it returns <code>TCL_ERROR</code> and leaves an error message in the interpreter&#8217;s result object if <i>interp</i> is not NULL. Otherwise, it returns <code>TCL_OK</code> after replacing the objects. If <i>objv</i> is NULL, no new elements are added. If the argument <i>first</i> is zero or negative, it refers to the first element. If <i>first</i> is greater than or equal to the number of elements in the list, then no elements are deleted; the new elements are appended to the list. <i>count</i> gives the number of elements to replace. If <i>count</i> is zero or negative then no elements are deleted; the new elements are simply inserted before the one designated by <i>first</i>. <code>Tcl_ListObjReplace</code> invalidates <i>listPtr</i>&#8216;s old string representation. The reference counts of any elements inserted from <i>objv</i> are incremented since the resulting list now refers to them. Similarly, the reference counts for any replaced objects are decremented. </p>
<p> Because <code>Tcl_ListObjReplace</code> combines both element insertion and deletion, it can be used to implement a number of list operations. For example, the following code inserts the <i>objc</i> objects referenced by the array of object pointers <i>objv</i> just before the element <i>index</i> of the list referenced by <i>listPtr</i>: </p>
<dl COMPACT>
<dd>
<pre>result = Tcl_ListObjReplace(interp, listPtr, index, 0,
 objc, objv);</pre>
</dl>
<p> Similarly, the following code appends the <i>objc</i> objects referenced by the array <i>objv</i> to the end of the list <i>listPtr</i>: </p>
<dl COMPACT>
<dd>
<pre>result = Tcl_ListObjLength(interp, listPtr, &amp;length);
if (result == TCL_OK) {
 result = Tcl_ListObjReplace(interp, listPtr, length, 0,
 objc, objv);
}</pre>
</dl>
<p> The <i>count</i> list elements starting at <i>first</i> can be deleted by simply calling <code>Tcl_ListObjReplace</code> with a NULL <i>objvPtr</i>: </p>
<dl COMPACT>
<dd>
<pre>result = Tcl_ListObjReplace(interp, listPtr, first, count,
 0, NULL);</pre>
</dl>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_DecrRefCount, Tcl_IncrRefCount, Tcl_GetObjResult</p>
<h2>Keywords</h2>
<p>append, index, insert, internal representation, length, list, list object, list type, object, object type, replace, string representation</p>
