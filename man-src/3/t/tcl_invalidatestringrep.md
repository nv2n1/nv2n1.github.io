---
title: "tcl_invalidatestringrep(3)"
name: "tcl_invalidatestringrep"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_invalidatestringrep/"
description: "Tcl_NewObj, Tcl_DuplicateObj, Tcl_IncrRefCount, Tcl_DecrRefCount, Tcl_IsShared, Tcl_InvalidateStringRep – manipulate Tcl objects"
---

<p>Tcl_NewObj, Tcl_DuplicateObj, Tcl_IncrRefCount, Tcl_DecrRefCount, Tcl_IsShared, Tcl_InvalidateStringRep &#8211; manipulate Tcl objects </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewObj</code>()
Tcl_Obj *
<code>Tcl_DuplicateObj</code>(<i>objPtr</i>)
<code>Tcl_IncrRefCount</code>(<i>objPtr</i>)
<code>Tcl_DecrRefCount</code>(<i>objPtr</i>)
int
<code>Tcl_IsShared</code>(<i>objPtr</i>)
<code>Tcl_InvalidateStringRep</code>(<i>objPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Obj <i>*objPtr</i> (in) Points to an object; must have been the result of a previous call to <code>Tcl_NewObj</code>. </p>
</dl>
<h2>Introduction</h2>
<p>This man page presents an overview of Tcl objects and how they are used. It also describes generic procedures for managing Tcl objects. These procedures are used to create and copy objects, and increment and decrement the count of references (pointers) to objects. The procedures are used in conjunction with ones that operate on specific types of objects such as <code>Tcl_GetIntFromObj</code> and <code>Tcl_ListObjAppendElement</code>. The individual procedures are described along with the data structures they manipulate. </p>
<p> Tcl&#8217;s <i>dual-ported</i> objects provide a general-purpose mechanism for storing and exchanging Tcl values. They largely replace the use of strings in Tcl. For example, they are used to store variable values, command arguments, command results, and scripts. Tcl objects behave like strings but also hold an internal representation that can be manipulated more efficiently. For example, a Tcl list is now represented as an object that holds the list&#8217;s string representation as well as an array of pointers to the objects for each list element. Dual-ported objects avoid most runtime type conversions. They also improve the speed of many operations since an appropriate representation is immediately available. The compiler itself uses Tcl objects to cache the instruction bytecodes resulting from compiling scripts. </p>
<p> The two representations are a cache of each other and are computed lazily. That is, each representation is only computed when necessary, it is computed from the other representation, and, once computed, it is saved. In addition, a change in one representation invalidates the other one. As an example, a Tcl program doing integer calculations can operate directly on a variable&#8217;s internal machine integer representation without having to constantly convert between integers and strings. Only when it needs a string representing the variable&#8217;s value, say to print it, will the program regenerate the string representation from the integer. Although objects contain an internal representation, their semantics are defined in terms of strings: an up-to-date string can always be obtained, and any change to the object will be reflected in that string when the object&#8217;s string representation is fetched. Because of this representation invalidation and regeneration, it is dangerous for extension writers to access <code>Tcl_Obj</code> fields directly. It is better to access Tcl_Obj information using procedures like <code>Tcl_GetStringFromObj</code> and <code>Tcl_GetString</code>. </p>
<p> Objects are allocated on the heap and are referenced using a pointer to their <code>Tcl_Obj</code> structure. Objects are shared as much as possible. This significantly reduces storage requirements because some objects such as long lists are very large. Also, most Tcl values are only read and never modified. This is especially true for procedure arguments, which can be shared between the caller and the called procedure. Assignment and argument binding is done by simply assigning a pointer to the value. Reference counting is used to determine when it is safe to reclaim an object&#8217;s storage. </p>
<p> Tcl objects are typed. An object&#8217;s internal representation is controlled by its type. Several types are predefined in the Tcl core including integer, double, list, and bytecode. Extension writers can extend the set of types by defining their own <code>Tcl_ObjType</code> structs.</p>
<h2>The Tcl_Obj Structure</h2>
<p>Each Tcl object is represented by a <code>Tcl_Obj</code> structure which is defined as follows.</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_Obj {
 int <i>refCount</i>;
 char *<i>bytes</i>;
 int <i>length</i>;
 Tcl_ObjType *<i>typePtr</i>;
 union {
 long <i>longValue</i>;
 double <i>doubleValue</i>;
 void *<i>otherValuePtr</i>;
 Tcl_WideInt <i>wideValue</i>;
 struct {
 void *<i>ptr1</i>;
 void *<i>ptr2</i>;
 } <i>twoPtrValue</i>;
 struct {
 void *<i>ptr</i>;
 unsigned long <i>value</i>;
 } <i>ptrAndLongRep</i>;
 } <i>internalRep</i>;
} Tcl_Obj;</pre>
</dl>
<p> The <i>bytes</i> and the <i>length</i> members together hold an object&#8217;s UTF-8 string representation, which is a <i>counted string</i> not containing null bytes (UTF-8 null characters should be encoded as a two byte sequence: 192, 128.) <i>bytes</i> points to the first byte of the string representation. The <i>length</i> member gives the number of bytes. The byte array must always have a null byte after the last data byte, at offset <i>length</i>; this allows string representations to be treated as conventional null-terminated C strings. C programs use <code>Tcl_GetStringFromObj</code> and <code>Tcl_GetString</code> to get an object&#8217;s string representation. If <i>bytes</i> is NULL, the string representation is invalid. </p>
<p> An object&#8217;s type manages its internal representation. The member <i>typePtr</i> points to the Tcl_ObjType structure that describes the type. If <i>typePtr</i> is NULL, the internal representation is invalid. </p>
<p> The <i>internalRep</i> union member holds an object&#8217;s internal representation. This is either a (long) integer, a double-precision floating-point number, a pointer to a value containing additional information needed by the object&#8217;s type to represent the object, a Tcl_WideInt integer, two arbitrary pointers, or a pair made up of an unsigned long integer and a pointer. </p>
<p> The <i>refCount</i> member is used to tell when it is safe to free an object&#8217;s storage. It holds the count of active references to the object. Maintaining the correct reference count is a key responsibility of extension writers. Reference counting is discussed below in the section <code>STORAGE MANAGEMENT OF OBJECTS</code>. </p>
<p> Although extension writers can directly access the members of a Tcl_Obj structure, it is much better to use the appropriate procedures and macros. For example, extension writers should never read or update <i>refCount</i> directly; they should use macros such as <code>Tcl_IncrRefCount</code> and <code>Tcl_IsShared</code> instead. </p>
<p> A key property of Tcl objects is that they hold two representations. An object typically starts out containing only a string representation: it is untyped and has a NULL <i>typePtr</i>. An object containing an empty string or a copy of a specified string is created using <code>Tcl_NewObj</code> or <code>Tcl_NewStringObj</code> respectively. An object&#8217;s string value is gotten with <code>Tcl_GetStringFromObj</code> or <code>Tcl_GetString</code> and changed with <code>Tcl_SetStringObj</code>. If the object is later passed to a procedure like <code>Tcl_GetIntFromObj</code> that requires a specific internal representation, the procedure will create one and set the object&#8217;s <i>typePtr</i>. The internal representation is computed from the string representation. An object&#8217;s two representations are duals of each other: changes made to one are reflected in the other. For example, <code>Tcl_ListObjReplace</code> will modify an object&#8217;s internal representation and the next call to <code>Tcl_GetStringFromObj</code> or <code>Tcl_GetString</code> will reflect that change. </p>
<p> Representations are recomputed lazily for efficiency. A change to one representation made by a procedure such as <code>Tcl_ListObjReplace</code> is not reflected immediately in the other representation. Instead, the other representation is marked invalid so that it is only regenerated if it is needed later. Most C programmers never have to be concerned with how this is done and simply use procedures such as <code>Tcl_GetBooleanFromObj</code> or <code>Tcl_ListObjIndex</code>. Programmers that implement their own object types must check for invalid representations and mark representations invalid when necessary. The procedure <code>Tcl_InvalidateStringRep</code> is used to mark an object&#8217;s string representation invalid and to free any storage associated with the old string representation. </p>
<p> Objects usually remain one type over their life, but occasionally an object must be converted from one type to another. For example, a C program might build up a string in an object with repeated calls to <code>Tcl_AppendToObj</code>, and then call <code>Tcl_ListObjIndex</code> to extract a list element from the object. The same object holding the same string value can have several different internal representations at different times. Extension writers can also force an object to be converted from one type to another using the <code>Tcl_ConvertToType</code> procedure. Only programmers that create new object types need to be concerned about how this is done. A procedure defined as part of the object type&#8217;s implementation creates a new internal representation for an object and changes its <i>typePtr</i>. See the man page for <code>Tcl_RegisterObjType</code> to see how to create a new object type.</p>
<h2>Example Of The Lifetime Of An Object</h2>
<p>As an example of the lifetime of an object, consider the following sequence of commands:</p>
<dl COMPACT>
<dd>
<pre><code>set x 123</code></pre>
</dl>
<p> This assigns to <i>x</i> an untyped object whose <i>bytes</i> member points to <code>123</code> and <i>length</i> member contains 3. The object&#8217;s <i>typePtr</i> member is NULL.</p>
<dl COMPACT>
<dd>
<pre><code>puts &quot;x is $x&quot;</code></pre>
</dl>
<p> <i>x</i>&#8216;s string representation is valid (since <i>bytes</i> is non-NULL) and is fetched for the command.</p>
<dl COMPACT>
<dd>
<pre><code>incr x</code></pre>
</dl>
<p> The <code>incr</code> command first gets an integer from <i>x</i>&#8216;s object by calling <code>Tcl_GetIntFromObj</code>. This procedure checks whether the object is already an integer object. Since it is not, it converts the object by setting the object&#8217;s <i>internalRep.longValue</i> member to the integer <code>123</code> and setting the object&#8217;s <i>typePtr</i> to point to the integer Tcl_ObjType structure. Both representations are now valid. <code>incr</code> increments the object&#8217;s integer internal representation then invalidates its string representation (by calling <code>Tcl_InvalidateStringRep</code>) since the string representation no longer corresponds to the internal representation.</p>
<dl COMPACT>
<dd>
<pre><code>puts &quot;x is now $x&quot;</code></pre>
</dl>
<p> The string representation of <i>x</i>&#8216;s object is needed and is recomputed. The string representation is now <code>124</code> and both representations are again valid.</p>
<h2>Storage Management Of Objects</h2>
<p>Tcl objects are allocated on the heap and are shared as much as possible to reduce storage requirements. Reference counting is used to determine when an object is no longer needed and can safely be freed. An object just created by <code>Tcl_NewObj</code> or <code>Tcl_NewStringObj</code> has <i>refCount</i> 0. The macro <code>Tcl_IncrRefCount</code> increments the reference count when a new reference to the object is created. The macro <code>Tcl_DecrRefCount</code> decrements the count when a reference is no longer needed and, if the object&#8217;s reference count drops to zero, frees its storage. An object shared by different code or data structures has <i>refCount</i> greater than 1. Incrementing an object&#8217;s reference count ensures that it will not be freed too early or have its value change accidentally. </p>
<p> As an example, the bytecode interpreter shares argument objects between calling and called Tcl procedures to avoid having to copy objects. It assigns the call&#8217;s argument objects to the procedure&#8217;s formal parameter variables. In doing so, it calls <code>Tcl_IncrRefCount</code> to increment the reference count of each argument since there is now a new reference to it from the formal parameter. When the called procedure returns, the interpreter calls <code>Tcl_DecrRefCount</code> to decrement each argument&#8217;s reference count. When an object&#8217;s reference count drops less than or equal to zero, <code>Tcl_DecrRefCount</code> reclaims its storage. Most command procedures do not have to be concerned about reference counting since they use an object&#8217;s value immediately and do not retain a pointer to the object after they return. However, if they do retain a pointer to an object in a data structure, they must be careful to increment its reference count since the retained pointer is a new reference. </p>
<p> Command procedures that directly modify objects such as those for <code>lappend</code> and <code>linsert</code> must be careful to copy a shared object before changing it. They must first check whether the object is shared by calling <code>Tcl_IsShared</code>. If the object is shared they must copy the object by using <code>Tcl_DuplicateObj</code>; this returns a new duplicate of the original object that has <i>refCount</i> 0. If the object is not shared, the command procedure &#8220;owns&#8221; the object and can safely modify it directly. For example, the following code appears in the command procedure that implements <code>linsert</code>. This procedure modifies the list object passed to it in <i>objv[1]</i> by inserting <i>objc-3</i> new elements before <i>index</i>. </p>
<dl COMPACT>
<dd>
<pre>listPtr = objv[1];
if (Tcl_IsShared(listPtr)) {
 listPtr = Tcl_DuplicateObj(listPtr);
}
result = Tcl_ListObjReplace(interp, listPtr, index, 0,
 (objc-3), &amp;(objv[3]));</pre>
</dl>
<p> As another example, <code>incr</code>&#8216;s command procedure must check whether the variable&#8217;s object is shared before incrementing the integer in its internal representation. If it is shared, it needs to duplicate the object in order to avoid accidentally changing values in other data structures.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_converttotype/">Tcl_ConvertToType</a>(3), <a href="/docs/linux/man/3-tcl_getintfromobj/">Tcl_GetIntFromObj</a>(3), <a href="/docs/linux/man/3-tcl_listobjappendelement/">Tcl_ListObjAppendElement</a>(3), <a href="/docs/linux/man/3-tcl_listobjindex/">Tcl_ListObjIndex</a>(3), <a href="/docs/linux/man/3-tcl_listobjreplace/">Tcl_ListObjReplace</a>(3), <a href="/docs/linux/man/3-tcl_registerobjtype/">Tcl_RegisterObjType</a>(3)</p>
<h2>Keywords</h2>
<p>internal representation, object, object creation, object type, reference counting, string representation, type conversion</p>
