---
title: "tcl_methodistype(3)"
name: "tcl_methodistype"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_methodistype/"
description: "Tcl_ClassSetConstructor, Tcl_ClassSetDestructor, Tcl_MethodDeclarerClass, Tcl_MethodDeclarerObject, Tcl_MethodIsPublic, Tcl_MethodIsType, Tcl_MethodName, Tcl_NewInstanceMethod, Tcl_NewMethod, Tcl_O..."
---

<p>Tcl_ClassSetConstructor, Tcl_ClassSetDestructor, Tcl_MethodDeclarerClass, Tcl_MethodDeclarerObject, Tcl_MethodIsPublic, Tcl_MethodIsType, Tcl_MethodName, Tcl_NewInstanceMethod, Tcl_NewMethod, Tcl_ObjectContextInvokeNext, Tcl_ObjectContextIsFiltering, Tcl_ObjectContextMethod, Tcl_ObjectContextObject, Tcl_ObjectContextSkippedArgs &#8211; manipulate methods and method-call contexts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tclOO.h&gt;</code>
Tcl_Method
<code>Tcl_NewMethod</code>(<i>interp, class, nameObj, isPublic,
 methodTypePtr, clientData</i>)
Tcl_Method
<code>Tcl_NewInstanceMethod</code>(<i>interp, object, nameObj, isPublic,
 methodTypePtr, clientData</i>)
<code>Tcl_ClassSetConstructor</code>(<i>interp, class, method</i>)
<code>Tcl_ClassSetDestructor</code>(<i>interp, class, method</i>)
Tcl_Class
<code>Tcl_MethodDeclarerClass</code>(<i>method</i>)
Tcl_Object
<code>Tcl_MethodDeclarerObject</code>(<i>method</i>)
Tcl_Obj *
<code>Tcl_MethodName</code>(<i>method</i>)
int
<code>Tcl_MethodIsPublic</code>(<i>method</i>)
int
<code>Tcl_MethodIsType</code>(<i>method, methodTypePtr, clientDataPtr</i>)
int
<code>Tcl_ObjectContextInvokeNext</code>(<i>interp, context, objc, objv, skip</i>)
int
<code>Tcl_ObjectContextIsFiltering</code>(<i>context</i>)
Tcl_Method
<code>Tcl_ObjectContextMethod</code>(<i>context</i>)
Tcl_Object
<code>Tcl_ObjectContextObject</code>(<i>context</i>)
int
<code>Tcl_ObjectContextSkippedArgs</code>(<i>context</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in/out) The interpreter holding the object or class to create or update a method in.</p>
<dd>Tcl_Object <i>object</i> (in) The object to create the method in.</p>
<dd>Tcl_Class <i>class</i> (in) The class to create the method in.</p>
<dd>Tcl_Obj <i>*nameObj</i> (in) The name of the method to create. Should not be NULL unless creating constructors or destructors.</p>
<dd>int <i>isPublic</i> (in) A boolean flag saying whether the method is to be exported.</p>
<dd>Tcl_MethodType <i>*methodTypePtr</i> (in) A description of the type of the method to create, or the type of method to compare against.</p>
<dd>ClientData <i>clientData</i> (in) A piece of data that is passed to the implementation of the method without interpretation.</p>
<dd>ClientData <i>*clientDataPtr</i> (out) A pointer to a variable in which to write the <i>clientData</i> value supplied when the method was created. If NULL, the <i>clientData</i> value will not be retrieved.</p>
<dd>Tcl_Method <i>method</i> (in) A reference to a method to query.</p>
<dd>Tcl_ObjectContext <i>context</i> (in) A reference to a method-call context. Note that client code <i>must not</i> retain a reference to a context.</p>
<dd>int <i>objc</i> (in) The number of arguments to pass to the method implementation.</p>
<dd>Tcl_Obj *const <i>*objv</i> (in) An array of arguments to pass to the method implementation.</p>
<dd>int <i>skip</i> (in) The number of arguments passed to the method implementation that do not represent &quot;real&quot; arguments.
</dl>
<h2>Description</h2>
<p>A method is an operation carried out on an object that is associated with the object. Every method must be attached to either an object or a class; methods attached to a class are associated with all instances (direct and indirect) of that class. </p>
<p> Given a method, the entity that declared it can be found using <code>Tcl_MethodDeclarerClass</code> which returns the class that the method is attached to (or NULL if the method is not attached to any class) and <code>Tcl_MethodDeclarerObject</code> which returns the object that the method is attached to (or NULL if the method is not attached to an object). The name of the method can be retrieved with <code>Tcl_MethodName</code> and whether the method is exported is retrieved with <code>Tcl_MethodIsPublic</code>. The type of the method can also be introspected upon to a limited degree; the function <code>Tcl_MethodIsType</code> returns whether a method is of a particular type, assigning the per-method <i>clientData</i> to the variable pointed to by <i>clientDataPtr</i> if (that is non-NULL) if the type is matched.</p>
<h3>Method Creation</h3>
<p>Methods are created by <code>Tcl_NewMethod</code> and <code>Tcl_NewInstanceMethod</code>, which create a method attached to a class or an object respectively. In both cases, the <i>nameObj</i> argument gives the name of the method to create, the <i>isPublic</i> argument states whether the method should be exported initially, the <i>methodTypePtr</i> argument describes the implementation of the method (see the <code>METHOD TYPES</code> section below) and the <i>clientData</i> argument gives some implementation-specific data that is passed on to the implementation of the method when it is called. </p>
<p> When the <i>nameObj</i> argument to <code>Tcl_NewMethod</code> is NULL, an unnamed method is created, which is used for constructors and destructors. Constructors should be installed into their class using the <code>Tcl_ClassSetConstructor</code> function, and destructors (which must not require any arguments) should be installed into their class using the <code>Tcl_ClassSetDestructor</code> function. Unnamed methods should not be used for any other purpose, and named methods should not be used as either constructors or destructors. Also note that a NULL <i>methodTypePtr</i> is used to provide internal signaling, and should not be used in client code.</p>
<h3>Method Call Contexts</h3>
<p>When a method is called, a method-call context reference is passed in as one of the arguments to the implementation function. This context can be inspected to provide information about the caller, but should not be retained beyond the moment when the method call terminates. </p>
<p> The method that is being called can be retrieved from the context by using <code>Tcl_ObjectContextMethod</code>, and the object that caused the method to be invoked can be retrieved with <code>Tcl_ObjectContextObject</code>. The number of arguments that are to be skipped (e.g. the object name and method name in a normal method call) is read with <code>Tcl_ObjectContextSkippedArgs</code>, and the context can also report whether it is working as a filter for another method through <code>Tcl_ObjectContextIsFiltering</code>. </p>
<p> During the execution of a method, the method implementation may choose to invoke the stages of the method call chain that come after the current method implementation. This (the core of the <code>next</code> command) is done using <code>Tcl_ObjectContextInvokeNext</code>. Note that this function does not manipulate the call-frame stack, unlike the <code>next</code> command; if the method implementation has pushed one or more extra frames on the stack as part of its implementation, it is also responsible for temporarily popping those frames from the stack while the <code>Tcl_ObjectContextInvokeNext</code> function is executing. Note also that the method-call context is <i>never</i> deleted during the execution of this function.</p>
<h2>Method Types</h2>
<p>The types of methods are described by a pointer to a Tcl_MethodType structure, which is defined as: </p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 int <i>version</i>;
 const char *<i>name</i>;
 Tcl_MethodCallProc *<i>callProc</i>;
 Tcl_MethodDeleteProc *<i>deleteProc</i>;
 Tcl_CloneProc *<i>cloneProc</i>;
} <code>Tcl_MethodType</code>;</pre>
</dl>
<p> The <i>version</i> field allows for future expansion of the structure, and should always be declared equal to TCL_OO_METHOD_VERSION_CURRENT. The <i>name</i> field provides a human-readable name for the type, and is the value that is exposed via the <code>info class methodtype</code> and <code>info object methodtype</code> Tcl commands. </p>
<p> The <i>callProc</i> field gives a function that is called when the method is invoked; it must never be NULL. </p>
<p> The <i>deleteProc</i> field gives a function that is used to delete a particular method, and is called when the method is replaced or removed; if the field is NULL, it is assumed that the method&#8217;s <i>clientData</i> needs no special action to delete. </p>
<p> The <i>cloneProc</i> field is either a function that is used to copy a method&#8217;s <i>clientData</i> (as part of <code>Tcl_CopyObjectInstance</code>) or NULL to indicate that the <i>clientData</i> can just be copied directly.</p>
<h3>Tcl_Methodcallproc Function Signature</h3>
<p>Functions matching this signature are called when the method is invoked. </p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_MethodCallProc</code>(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 Tcl_ObjectContext <i>objectContext</i>,
 int <i>objc</i>,
 Tcl_Obj *const *<i>objv</i>);</pre>
</dl>
<p> The <i>clientData</i> argument to a Tcl_MethodCallProc is the value that was given when the method was created, the <i>interp</i> is a place in which to execute scripts and access variables as well as being where to put the result of the method, and the <i>objc</i> and <i>objv</i> fields give the parameter objects to the method. The calling context of the method can be discovered through the <i>objectContext</i> argument, and the return value from a Tcl_MethodCallProc is any Tcl return code (e.g. TCL_OK, TCL_ERROR).</p>
<h3>Tcl_Methoddeleteproc Function Signature</h3>
<p>Functions matching this signature are used when a method is deleted, whether through a new method being created or because the object or class is deleted. </p>
<dl COMPACT>
<dd>
<pre>typedef void <code>Tcl_MethodDeleteProc</code>(
 ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> argument to a Tcl_MethodDeleteProc will be the same as the value passed to the <i>clientData</i> argument to <code>Tcl_NewMethod</code> or <code>Tcl_NewInstanceMethod</code> when the method was created.</p>
<h3>Tcl_Cloneproc Function Signature</h3>
<p>Functions matching this signature are used to copy a method when the object or class is copied using <code>Tcl_CopyObjectInstance</code> (or <code>oo::copy</code>). </p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_CloneProc</code>(
 Tcl_Interp *<i>interp</i>,
 ClientData <i>oldClientData</i>,
 ClientData *<i>newClientDataPtr</i>);</pre>
</dl>
<p> The <i>interp</i> argument gives a place to write an error message when the attempt to clone the object is to fail, in which case the clone procedure must also return TCL_ERROR; it should return TCL_OK otherwise. The <i>oldClientData</i> field to a Tcl_CloneProc gives the value from the method being copied from, and the <i>newClientDataPtr</i> field will point to a variable in which to write the value for the method being copied to.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-class/">Class</a>(3), <a href="/docs/linux/man/n-oo--class/">oo::class</a>(n), <a href="/docs/linux/man/n-oo--define/">oo::define</a>(n), <a href="/docs/linux/man/n-oo--object/">oo::object</a>(n)</p>
<h2>Keywords</h2>
<p>constructor, method, object</p>
