---
title: "tcl_classgetmetadata(3)"
name: "tcl_classgetmetadata"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_classgetmetadata/"
description: "Tcl_ClassGetMetadata, Tcl_ClassSetMetadata, Tcl_CopyObjectInstance, Tcl_GetClassAsObject, Tcl_GetObjectAsClass, Tcl_GetObjectCommand, Tcl_GetObjectFromObj, Tcl_GetObjectName, Tcl_GetObjectNamespace..."
---

<p>Tcl_ClassGetMetadata, Tcl_ClassSetMetadata, Tcl_CopyObjectInstance, Tcl_GetClassAsObject, Tcl_GetObjectAsClass, Tcl_GetObjectCommand, Tcl_GetObjectFromObj, Tcl_GetObjectName, Tcl_GetObjectNamespace, Tcl_NewObjectInstance, Tcl_ObjectDeleted, Tcl_ObjectGetMetadata, Tcl_ObjectGetMethodNameMapper, Tcl_ObjectSetMetadata, Tcl_ObjectSetMethodNameMapper &#8211; manipulate objects and classes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tclOO.h&gt;</code>
Tcl_Object
<code>Tcl_GetObjectFromObj</code>(<i>interp, objPtr</i>)
Tcl_Object
<code>Tcl_GetClassAsObject</code>(<i>class</i>)
Tcl_Class
<code>Tcl_GetObjectAsClass</code>(<i>object</i>)
Tcl_Obj *
<code>Tcl_GetObjectName</code>(<i>interp, object</i>)
Tcl_Command
<code>Tcl_GetObjectCommand</code>(<i>object</i>)
Tcl_Namespace *
<code>Tcl_GetObjectNamespace</code>(<i>object</i>)
Tcl_Object
<code>Tcl_NewObjectInstance</code>(<i>interp, class, name, nsName, objc, objv, skip</i>)
Tcl_Object
<code>Tcl_CopyObjectInstance</code>(<i>interp, object, name, nsName</i>)
int
<code>Tcl_ObjectDeleted</code>(<i>object</i>)
ClientData
<code>Tcl_ObjectGetMetadata</code>(<i>object, metaTypePtr</i>)
<code>Tcl_ObjectSetMetadata</code>(<i>object, metaTypePtr, metadata</i>)
ClientData
<code>Tcl_ClassGetMetadata</code>(<i>class, metaTypePtr</i>)
<code>Tcl_ClassSetMetadata</code>(<i>class, metaTypePtr, metadata</i>)
Tcl_ObjectMapMethodNameProc
<code>Tcl_ObjectGetMethodNameMapper</code>(<i>object</i>)
<code>Tcl_ObjectSetMethodNameMapper</code>(<i>object</i>, <i>methodNameMapper</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in/out) Interpreter providing the context for looking up or creating an object, and into whose result error messages will be written on failure.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) The name of the object to look up.</p>
<dd>Tcl_Object <i>object</i> (in) Reference to the object to operate upon.</p>
<dd>Tcl_Class <i>class</i> (in) Reference to the class to operate upon.</p>
<dd>const char <i>*name</i> (in) The name of the object to create, or NULL if a new unused name is to be automatically selected.</p>
<dd>const char <i>*nsName</i> (in) The name of the namespace to create for the object&#8217;s private use, or NULL if a new unused name is to be automatically selected.</p>
<dd>int <i>objc</i> (in) The number of elements in the <i>objv</i> array.</p>
<dd>Tcl_Obj *const <i>*objv</i> (in) The arguments to the command to create the instance of the class.</p>
<dd>int <i>skip</i> (in) The number of arguments at the start of the argument array, <i>objv</i>, that are not arguments to any constructors.</p>
<dd>Tcl_ObjectMetadataType <i>*metaTypePtr</i> (in) The type of <i>metadata</i> being set with <code>Tcl_ClassSetMetadata</code> or retrieved with <code>Tcl_ClassGetMetadata</code>.</p>
<dd>ClientData <i>metadata</i> (in) An item of metadata to attach to the class, or NULL to remove the metadata associated with a particular <i>metaTypePtr</i>.</p>
<dd>Tcl_ObjectMapMethodNameProc <i>methodNameMapper</i> (in) A pointer to a function to call to adjust the mapping of objects and method names to implementations, or NULL when no such mapping is required.
</dl>
<h2>Description</h2>
<p>Objects are typed entities that have a set of operations (&quot;methods&quot;) associated with them. Classes are objects that can manufacture objects. Each class can be viewed as an object itself; the object view can be retrieved using <code>Tcl_GetClassAsObject</code> which always returns the object when applied to a non-destroyed class, and an object can be viewed as a class with the aid of the <code>Tcl_GetObjectAsClass</code> (which either returns the class, or NULL if the object is not a class). An object may be looked up using the <code>Tcl_GetObjectFromObj</code> function, which either returns an object or NULL (with an error message in the interpreter result) if the object cannot be found. The correct way to look up a class by name is to look up the object with that name, and then to use <code>Tcl_GetObjectAsClass</code>. </p>
<p> Every object has its own command and namespace associated with it. The command may be retrieved using the <code>Tcl_GetObjectCommand</code> function, the name of the object (and hence the name of the command) with <code>Tcl_GetObjectName</code>, and the namespace may be retrieved using the <code>Tcl_GetObjectNamespace</code> function. Note that the Tcl_Obj reference returned by <code>Tcl_GetObjectName</code> is a shared reference. </p>
<p> Instances of classes are created using <code>Tcl_NewObjectInstance</code>, which creates an object from any class (and which is internally called by both the <code>create</code> and <code>new</code> methods of the <code>oo::class</code> class). It takes parameters that optionally give the name of the object and namespace to create, and which describe the arguments to pass to the class&#8217;s constructor (if any). The result of the function will be either a reference to the newly created object, or NULL if the creation failed (when an error message will be left in the interpreter result). In addition, objects may be copied by using <code>Tcl_CopyObjectInstance</code> which creates a copy of an object without running any constructors.</p>
<h2>Object And Class Metadata</h2>
<p>Every object and every class may have arbitrary amounts of metadata attached to it, which the object or class attaches no meaning to beyond what is described in a Tcl_ObjectMetadataType structure instance. Metadata to be attached is described by the type of the metadata (given in the <i>metaTypePtr</i> argument) and an arbitrary pointer (the <i>metadata</i> argument) that are given to <code>Tcl_ObjectSetMetadata</code> and <code>Tcl_ClassSetMetadata</code>, and a particular piece of metadata can be retrieved given its type using <code>Tcl_ObjectGetMetadata</code> and <code>Tcl_ClassGetMetadata</code>. If the <i>metadata</i> parameter to either <code>Tcl_ObjectSetMetadata</code> or <code>Tcl_ClassSetMetadata</code> is NULL, the metadata is removed if it was attached, and the results of <code>Tcl_ObjectGetMetadata</code> and <code>Tcl_ClassGetMetadata</code> are NULL if the given type of metadata was not attached. It is not an error to request or remove a piece of metadata that was not attached.</p>
<h3>Tcl_Objectmetadatatype Structure</h3>
<p>The contents of the Tcl_ObjectMetadataType structure are as follows: </p>
<dl COMPACT>
<dd>
<pre>typedef const struct {
 int <i>version</i>;
 const char *<i>name</i>;
 Tcl_ObjectMetadataDeleteProc *<i>deleteProc</i>;
 Tcl_CloneProc *<i>cloneProc</i>;
} <code>Tcl_ObjectMetadataType</code>;</pre>
</dl>
<p> The <i>version</i> field allows for future expansion of the structure, and should always be declared equal to TCL_OO_METADATA_VERSION_CURRENT. The <i>name</i> field provides a human-readable name for the type, and is reserved for debugging. </p>
<p> The <i>deleteProc</i> field gives a function of type Tcl_ObjectMetadataDeleteProc that is used to delete a particular piece of metadata, and is called when the attached metadata is replaced or removed; the field must not be NULL. </p>
<p> The <i>cloneProc</i> field gives a function that is used to copy a piece of metadata (used when a copy of an object is created using <code>Tcl_CopyObjectInstance</code>); if NULL, the metadata will be just directly copied.</p>
<h3>Tcl_Objectmetadatadeleteproc Function Signature</h3>
<p>Functions matching this signature are used to delete metadata associated with a class or object. </p>
<dl COMPACT>
<dd>
<pre>typedef void <code>Tcl_ObjectMetadataDeleteProc</code>(
 ClientData <i>metadata</i>);</pre>
</dl>
<p> The <i>metadata</i> argument gives the address of the metadata to be deleted.</p>
<h3>Tcl_Cloneproc Function Signature</h3>
<p>Functions matching this signature are used to create copies of metadata associated with a class or object. </p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_CloneProc</code>(
 Tcl_Interp *<i>interp</i>,
 ClientData <i>srcMetadata</i>,
 ClientData *<i>dstMetadataPtr</i>);</pre>
</dl>
<p> The <i>interp</i> argument gives a place to write an error message when the attempt to clone the object is to fail, in which case the clone procedure must also return TCL_ERROR; it should return TCL_OK otherwise. The <i>srcMetadata</i> argument gives the address of the metadata to be cloned, and the cloned metadata should be written into the variable pointed to by <i>dstMetadataPtr</i>; a NULL should be written if the metadata is to not be cloned but the overall object copy operation is still to succeed.</p>
<h2>Object Method Name Mapping</h2>
<p>It is possible to control, on a per-object basis, what methods are invoked when a particular method is invoked. Normally this is done by looking up the method name in the object and then in the class hierarchy, but fine control of exactly what the value used to perform the look up is afforded through the ability to set a method name mapper callback via <code>Tcl_ObjectSetMethodNameMapper</code> (and its introspection counterpart, <code>Tcl_ObjectGetMethodNameMapper</code>, which returns the current mapper). The current mapper (if any) is invoked immediately before looking up what chain of method implementations is to be used.</p>
<h3>Tcl_Objectmapmethodnameproc Function Signature</h3>
<p>The <i>Tcl_ObjectMapMethodNameProc</i> callback is defined as follows: </p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_ObjectMapMethodNameProc</code>(
 Tcl_Interp *<i>interp</i>,
 Tcl_Object <i>object</i>,
 Tcl_Class *<i>startClsPtr</i>,
 Tcl_Obj *<i>methodNameObj</i>);</pre>
</dl>
<p> If the result is TCL_OK, the remapping is assumed to have been done. If the result is TCL_ERROR, an error message will have been left in <i>interp</i> and the method call will fail. If the result is TCL_BREAK, the standard method name lookup rules will be used; the behavior of other result codes is currently undefined. The <i>object</i> parameter says which object is being processed. The <i>startClsPtr</i> parameter points to a variable that contains the first class to provide a definition in the method chain to process, or NULL if the whole chain is to be processed (the argument itself is never NULL); this variable may be updated by the callback. The <i>methodNameObj</i> parameter gives an unshared object containing the name of the method being invoked, as provided by the user; this object may be updated by the callback.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-method/">Method</a>(3), <a href="/docs/linux/man/n-oo--class/">oo::class</a>(n), <a href="/docs/linux/man/n-oo--copy/">oo::copy</a>(n), <a href="/docs/linux/man/n-oo--define/">oo::define</a>(n), <a href="/docs/linux/man/n-oo--object/">oo::object</a>(n)</p>
<h2>Keywords</h2>
<p>class, constructor, object</p>
