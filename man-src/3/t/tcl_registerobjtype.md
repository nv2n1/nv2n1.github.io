---
title: "tcl_registerobjtype(3)"
name: "tcl_registerobjtype"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_registerobjtype/"
description: "Tcl_RegisterObjType, Tcl_GetObjType, Tcl_AppendAllObjTypes, Tcl_ConvertToType – manipulate Tcl object types"
---

<p>Tcl_RegisterObjType, Tcl_GetObjType, Tcl_AppendAllObjTypes, Tcl_ConvertToType &#8211; manipulate Tcl object types </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_RegisterObjType</code>(<i>typePtr</i>)
Tcl_ObjType *
<code>Tcl_GetObjType</code>(<i>typeName</i>)
int
<code>Tcl_AppendAllObjTypes</code>(<i>interp, objPtr</i>)
int
<code>Tcl_ConvertToType</code>(<i>interp, objPtr, typePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_ObjType <i>*typePtr</i> (in) Points to the structure containing information about the Tcl object type. This storage must live forever, typically by being statically allocated.</p>
<dd>const char <i>*typeName</i> (in) The name of a Tcl object type that <code>Tcl_GetObjType</code> should look up.</p>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) For <code>Tcl_AppendAllObjTypes</code>, this points to the object onto which it appends the name of each object type as a list element. For <code>Tcl_ConvertToType</code>, this points to an object that must have been the result of a previous call to <code>Tcl_NewObj</code>. </p>
</dl>
<h2>Description</h2>
<p>The procedures in this man page manage Tcl object types. They are used to register new object types, look up types, and force conversions from one type to another. </p>
<p> <code>Tcl_RegisterObjType</code> registers a new Tcl object type in the table of all object types that <code>Tcl_GetObjType</code> can look up by name. There are other object types supported by Tcl as well, which Tcl chooses not to register. Extensions can likewise choose to register the object types they create or not. The argument <i>typePtr</i> points to a Tcl_ObjType structure that describes the new type by giving its name and by supplying pointers to four procedures that implement the type. If the type table already contains a type with the same name as in <i>typePtr</i>, it is replaced with the new type. The Tcl_ObjType structure is described in the section <code>THE TCL_OBJTYPE STRUCTURE</code> below. </p>
<p> <code>Tcl_GetObjType</code> returns a pointer to the registered Tcl_ObjType with name <i>typeName</i>. It returns NULL if no type with that name is registered. </p>
<p> <code>Tcl_AppendAllObjTypes</code> appends the name of each registered object type as a list element onto the Tcl object referenced by <i>objPtr</i>. The return value is <code>TCL_OK</code> unless there was an error converting <i>objPtr</i> to a list object; in that case <code>TCL_ERROR</code> is returned. </p>
<p> <code>Tcl_ConvertToType</code> converts an object from one type to another if possible. It creates a new internal representation for <i>objPtr</i> appropriate for the target type <i>typePtr</i> and sets its <i>typePtr</i> member as determined by calling the <i>typePtr-&gt;setFromAnyProc</i> routine. Any internal representation for <i>objPtr</i>&#8216;s old type is freed. If an error occurs during conversion, it returns <code>TCL_ERROR</code> and leaves an error message in the result object for <i>interp</i> unless <i>interp</i> is NULL. Otherwise, it returns <code>TCL_OK</code>. Passing a NULL <i>interp</i> allows this procedure to be used as a test whether the conversion can be done (and in fact was done). </p>
<p> In many cases, the <i>typePtr-&gt;setFromAnyProc</i> routine will set <i>objPtr-&gt;typePtr</i> to the argument value <i>typePtr</i>, but that is no longer guaranteed. The <i>setFromAnyProc</i> is free to set the internal representation for <i>objPtr</i> to make use of another related Tcl_ObjType, if it sees fit.</p>
<h2>The Tcl_Objtype Structure</h2>
<p>Extension writers can define new object types by defining four procedures and initializing a Tcl_ObjType structure to describe the type. Extension writers may also pass a pointer to their Tcl_ObjType structure to <code>Tcl_RegisterObjType</code> if they wish to permit other extensions to look up their Tcl_ObjType by name with the <code>Tcl_GetObjType</code> routine. The <code>Tcl_ObjType</code> structure is defined as follows: </p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_ObjType {
 char *<i>name</i>;
 Tcl_FreeInternalRepProc *<i>freeIntRepProc</i>;
 Tcl_DupInternalRepProc *<i>dupIntRepProc</i>;
 Tcl_UpdateStringProc *<i>updateStringProc</i>;
 Tcl_SetFromAnyProc *<i>setFromAnyProc</i>;
} Tcl_ObjType;</pre>
</dl>
<h3>The Name Field</h3>
<p>The <i>name</i> member describes the name of the type, e.g. <code>int</code>. When a type is registered, this is the name used by callers of <code>Tcl_GetObjType</code> to lookup the type. For unregistered types, the <i>name</i> field is primarily of value for debugging. The remaining four members are pointers to procedures called by the generic Tcl object code:</p>
<h3>The Setfromanyproc Field</h3>
<p>The <i>setFromAnyProc</i> member contains the address of a function called to create a valid internal representation from an object&#8217;s string representation. </p>
<dl COMPACT>
<dd>
<pre>typedef int (Tcl_SetFromAnyProc) (Tcl_Interp *<i>interp</i>,
 Tcl_Obj *<i>objPtr</i>);</pre>
</dl>
<p> If an internal representation cannot be created from the string, it returns <code>TCL_ERROR</code> and puts a message describing the error in the result object for <i>interp</i> unless <i>interp</i> is NULL. If <i>setFromAnyProc</i> is successful, it stores the new internal representation, sets <i>objPtr</i>&#8216;s <i>typePtr</i> member to point to the <code>Tcl_ObjType</code> struct corresponding to the new internal representation, and returns <code>TCL_OK</code>. Before setting the new internal representation, the <i>setFromAnyProc</i> must free any internal representation of <i>objPtr</i>&#8216;s old type; it does this by calling the old type&#8217;s <i>freeIntRepProc</i> if it is not NULL. </p>
<p> As an example, the <i>setFromAnyProc</i> for the built-in Tcl list type gets an up-to-date string representation for <i>objPtr</i> by calling <code>Tcl_GetStringFromObj</code>. It parses the string to verify it is in a valid list format and to obtain each element value in the list, and, if this succeeds, stores the list elements in <i>objPtr</i>&#8216;s internal representation and sets <i>objPtr</i>&#8216;s <i>typePtr</i> member to point to the list type&#8217;s Tcl_ObjType structure. </p>
<p> Do not release <i>objPtr</i>&#8216;s old internal representation unless you replace it with a new one or reset the <i>typePtr</i> member to NULL. </p>
<p> The <i>setFromAnyProc</i> member may be set to NULL, if the routines making use of the internal representation have no need to derive that internal representation from an arbitrary string value. However, in this case, passing a pointer to the type to Tcl_ConvertToType() will lead to a panic, so to avoid this possibility, the type should <i>not</i> be registered.</p>
<h3>The Updatestringproc Field</h3>
<p>The <i>updateStringProc</i> member contains the address of a function called to create a valid string representation from an object&#8217;s internal representation. </p>
<dl COMPACT>
<dd>
<pre>typedef void (Tcl_UpdateStringProc) (Tcl_Obj *<i>objPtr</i>);</pre>
</dl>
<p> <i>objPtr</i>&#8216;s <i>bytes</i> member is always NULL when it is called. It must always set <i>bytes</i> non-NULL before returning. We require the string representation&#8217;s byte array to have a null after the last byte, at offset <i>length</i>, and to have no null bytes before that; this allows string representations to be treated as conventional null character-terminated C strings. These restrictions are easily met by using Tcl&#8217;s internal UTF encoding for the string representation, same as one would do for other Tcl routines accepting string values as arguments. Storage for the byte array must be allocated in the heap by <code>Tcl_Alloc</code> or <code>ckalloc</code>. Note that <i>updateStringProc</i>s must allocate enough storage for the string&#8217;s bytes and the terminating null byte. </p>
<p> The <i>updateStringProc</i> for Tcl&#8217;s built-in double type, for example, calls Tcl_PrintDouble to write to a buffer of size TCL_DOUBLE_SPACE, then allocates and copies the string representation to just enough space to hold it. A pointer to the allocated space is stored in the <i>bytes</i> member. </p>
<p> The <i>updateStringProc</i> member may be set to NULL, if the routines making use of the internal representation are written so that the string representation is never invalidated. Failure to meet this obligation will lead to panics or crashes when <code>Tcl_GetStringFromObj</code> or other similar routines ask for the string representation.</p>
<h3>The Dupintrepproc Field</h3>
<p>The <i>dupIntRepProc</i> member contains the address of a function called to copy an internal representation from one object to another. </p>
<dl COMPACT>
<dd>
<pre>typedef void (Tcl_DupInternalRepProc) (Tcl_Obj *<i>srcPtr</i>,
 Tcl_Obj *<i>dupPtr</i>);</pre>
</dl>
<p> <i>dupPtr</i>&#8216;s internal representation is made a copy of <i>srcPtr</i>&#8216;s internal representation. Before the call, <i>srcPtr</i>&#8216;s internal representation is valid and <i>dupPtr</i>&#8216;s is not. <i>srcPtr</i>&#8216;s object type determines what copying its internal representation means. </p>
<p> For example, the <i>dupIntRepProc</i> for the Tcl integer type simply copies an integer. The built-in list type&#8217;s <i>dupIntRepProc</i> uses a far more sophisticated scheme to continue sharing storage as much as it reasonably can.</p>
<h3>The Freeintrepproc Field</h3>
<p>The <i>freeIntRepProc</i> member contains the address of a function that is called when an object is freed. </p>
<dl COMPACT>
<dd>
<pre>typedef void (Tcl_FreeInternalRepProc) (Tcl_Obj *<i>objPtr</i>);</pre>
</dl>
<p> The <i>freeIntRepProc</i> function can deallocate the storage for the object&#8217;s internal representation and do other type-specific processing necessary when an object is freed. </p>
<p> For example, the list type&#8217;s <i>freeIntRepProc</i> respects the storage sharing scheme established by the <i>dupIntRepProc</i> so that it only frees storage when the last object sharing it is being freed. </p>
<p> The <i>freeIntRepProc</i> member can be set to NULL to indicate that the internal representation does not require freeing. The <i>freeIntRepProc</i> implementation must not access the <i>bytes</i> member of the object, since Tcl makes its own internal uses of that field during object deletion. The defined tasks for the <i>freeIntRepProc</i> have no need to consult the <i>bytes</i> member.</p>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_DecrRefCount, Tcl_IncrRefCount</p>
<h2>Keywords</h2>
<p>internal representation, object, object type, string representation, type conversion</p>
