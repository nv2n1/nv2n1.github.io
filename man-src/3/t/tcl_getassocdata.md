---
title: "tcl_getassocdata(3)"
name: "tcl_getassocdata"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getassocdata/"
description: "Tcl_GetAssocData, Tcl_SetAssocData, Tcl_DeleteAssocData – manage associations of string keys and user specified data with Tcl interpreters"
---

<p>Tcl_GetAssocData, Tcl_SetAssocData, Tcl_DeleteAssocData &#8211; manage associations of string keys and user specified data with Tcl interpreters </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
ClientData
<code>Tcl_GetAssocData</code>(<i>interp, key, delProcPtr</i>)
<code>Tcl_SetAssocData</code>(<i>interp, key, delProc, clientData</i>)
<code>Tcl_DeleteAssocData</code>(<i>interp, key</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to execute the specified command.</p>
<dd>const char <i>*key</i> (in) Key for association with which to store data or from which to delete or retrieve data. Typically the module prefix for a package.</p>
<dd>Tcl_InterpDeleteProc <i>*delProc</i> (in) Procedure to call when <i>interp</i> is deleted.</p>
<dd>Tcl_InterpDeleteProc <i>**delProcPtr</i> (in) Pointer to location in which to store address of current deletion procedure for association. Ignored if NULL.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value associated with the given key in this interpreter. This data is owned by the caller. </p>
</dl>
<h2>Description</h2>
<p>These procedures allow extensions to associate their own data with a Tcl interpreter. An association consists of a string key, typically the name of the extension, and a one-word value, which is typically a pointer to a data structure holding data specific to the extension. Tcl makes no interpretation of either the key or the value for an association. </p>
<p> Storage management is facilitated by storing with each association a procedure to call when the interpreter is deleted. This procedure can dispose of the storage occupied by the client&#8217;s data in any way it sees fit. </p>
<p> <code>Tcl_SetAssocData</code> creates an association between a string key and a user specified datum in the given interpreter. If there is already an association with the given <i>key</i>, <code>Tcl_SetAssocData</code> overwrites it with the new information. It is up to callers to organize their use of names to avoid conflicts, for example, by using package names as the keys. If the <i>deleteProc</i> argument is non-NULL it specifies the address of a procedure to invoke if the interpreter is deleted before the association is deleted. <i>DeleteProc</i> should have arguments and result that match the type <code>Tcl_InterpDeleteProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_InterpDeleteProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> When <i>deleteProc</i> is invoked the <i>clientData</i> and <i>interp</i> arguments will be the same as the corresponding arguments passed to <code>Tcl_SetAssocData</code>. The deletion procedure will <i>not</i> be invoked if the association is deleted before the interpreter is deleted. </p>
<p> <code>Tcl_GetAssocData</code> returns the datum stored in the association with the specified key in the given interpreter, and if the <i>delProcPtr</i> field is non-<code>NULL</code>, the address indicated by it gets the address of the delete procedure stored with this association. If no association with the specified key exists in the given interpreter <code>Tcl_GetAssocData</code> returns <code>NULL</code>. </p>
<p> <code>Tcl_DeleteAssocData</code> deletes an association with a specified key in the given interpreter. Then it calls the deletion procedure.</p>
<h2>Keywords</h2>
<p>association, data, deletion procedure, interpreter, key</p>
