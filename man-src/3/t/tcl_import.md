---
title: "tcl_import(3)"
name: "tcl_import"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_import/"
description: "Tcl_AppendExportList, Tcl_CreateNamespace, Tcl_DeleteNamespace, Tcl_Export, Tcl_FindCommand, Tcl_FindNamespace, Tcl_ForgetImport, Tcl_GetCurrentNamespace, Tcl_GetGlobalNamespace, Tcl_GetNamespaceUn..."
---

<p>Tcl_AppendExportList, Tcl_CreateNamespace, Tcl_DeleteNamespace, Tcl_Export, Tcl_FindCommand, Tcl_FindNamespace, Tcl_ForgetImport, Tcl_GetCurrentNamespace, Tcl_GetGlobalNamespace, Tcl_GetNamespaceUnknownHandler, Tcl_Import, Tcl_SetNamespaceUnknownHandler &#8211; manipulate namespaces </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Namespace *
<code>Tcl_CreateNamespace</code>(<i>interp, name, clientData, deleteProc</i>)
<code>Tcl_DeleteNamespace</code>(<i>nsPtr</i>)
int
<code>Tcl_AppendExportList</code>(<i>interp, nsPtr, objPtr</i>)
int
<code>Tcl_Export</code>(<i>interp, nsPtr, pattern, resetListFirst</i>)
int
<code>Tcl_Import</code>(<i>interp, nsPtr, pattern, allowOverwrite</i>)
int
<code>Tcl_ForgetImport</code>(<i>interp, nsPtr, pattern</i>)
Tcl_Namespace *
<code>Tcl_GetCurrentNamespace</code>(<i>interp</i>)
Tcl_Namespace *
<code>Tcl_GetGlobalNamespace</code>(<i>interp</i>)
Tcl_Namespace *
<code>Tcl_FindNamespace</code>(<i>interp, name, contextNsPtr, flags</i>)
Tcl_Command
<code>Tcl_FindCommand</code>(<i>interp, name, contextNsPtr, flags</i>)
Tcl_Obj *
<code>Tcl_GetNamespaceUnknownHandler(</code><i>interp, nsPtr</i>)
int
<code>Tcl_SetNamespaceUnknownHandler(</code><i>interp, nsPtr, handlerPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in/out) The interpreter in which the namespace exists and where name lookups are performed. Also where error result messages are written.</p>
<dd>const char <i>*name</i> (in) The name of the namespace or command to be created or accessed.</p>
<dd>ClientData <i>clientData</i> (in) A context pointer by the creator of the namespace. Not interpreted by Tcl at all.</p>
<dd>Tcl_NamespaceDeleteProc <i>*deleteProc</i> (in) A pointer to function to call when the namespace is deleted, or NULL if no such callback is to be performed.</p>
<dd>Tcl_Namespace <i>*nsPtr</i> (in) The namespace to be manipulated, or NULL (for other than <code>Tcl_DeleteNamespace</code>) to manipulate the current namespace.</p>
<dd>Tcl_Obj <i>*objPtr</i> (out) A reference to an unshared object to which the function output will be written.</p>
<dd>const char <i>*pattern</i> (in) The glob-style pattern (see <code>Tcl_StringMatch</code>) that describes the commands to be imported or exported.</p>
<dd>int <i>resetListFirst</i> (in) Whether the list of export patterns should be reset before adding the current pattern to it.</p>
<dd>int <i>allowOverwrite</i> (in) Whether new commands created by this import action can overwrite existing commands.</p>
<dd>Tcl_Namespace <i>*contextNsPtr</i> (in) The location in the namespace hierarchy where the search for a namespace or command should be conducted relative to when the search term is not rooted at the global namespace. NULL indicates the current namespace.</p>
<dd>int <i>flags</i> (in) OR-ed combination of bits controlling how the search is to be performed. The following flags are supported: <code>TCL_GLOBAL_ONLY</code> (indicates that the search is always to be conducted relative to the global namespace), <code>TCL_NAMESPACE_ONLY</code> (just for <code>Tcl_FindCommand</code>; indicates that the search is always to be conducted relative to the context namespace), and <code>TCL_LEAVE_ERR_MSG</code> (indicates that an error message should be left in the interpreter if the search fails.)</p>
<dd>Tcl_Obj <i>*handlerPtr</i> (in) A script fragment to be installed as the unknown command handler for the namespace, or NULL to reset the handler to its default. </p>
</dl>
<h2>Description</h2>
<p>Namespaces are hierarchic naming contexts that can contain commands and variables. They also maintain a list of patterns that describes what commands are exported, and can import commands that have been exported by other namespaces. Namespaces can also be manipulated through the Tcl command <code>namespace</code>. </p>
<p> The <i>Tcl_Namespace</i> structure encapsulates a namespace, and is guaranteed to have the following fields in it: <i>name</i> (the local name of the namespace, with no namespace separator characters in it, with empty denoting the global namespace), <i>fullName</i> (the fully specified name of the namespace), <i>clientData</i>, <i>deleteProc</i> (the values specified in the call to <code>Tcl_CreateNamespace</code>), and <i>parentPtr</i> (a pointer to the containing namespace, or NULL for the global namespace.) </p>
<p> <code>Tcl_CreateNamespace</code> creates a new namespace. The <i>deleteProc</i> will have the following type signature:</p>
<dl COMPACT>
<dd>
<pre>typedef void (Tcl_NamespaceDeleteProc) (ClientData clientData);</pre>
</dl>
<p> <code>Tcl_DeleteNamespace</code> deletes a namespace. </p>
<p> <code>Tcl_AppendExportList</code> retrieves the export patterns for a namespace given namespace and appends them (as list items) to <i>objPtr</i>. </p>
<p> <code>Tcl_Export</code> sets and appends to the export patterns for a namespace. Patterns are appended unless the <i>resetListFirst</i> flag is true. </p>
<p> <code>Tcl_Import</code> imports commands matching a pattern into a namespace. Note that the pattern must include the name of the namespace to import from. This function returns an error if an attempt to import a command over an existing command is made, unless the <i>allowOverwrite</i> flag has been set. </p>
<p> <code>Tcl_ForgetImport</code> removes imports matching a pattern. </p>
<p> <code>Tcl_GetCurrentNamespace</code> returns the current namespace for an interpreter. </p>
<p> <code>Tcl_GetGlobalNamespace</code> returns the global namespace for an interpreter. </p>
<p> <code>Tcl_FindNamespace</code> searches for a namespace named <i>name</i> within the context of the namespace <i>contextNsPtr</i>. If the namespace cannot be found, NULL is returned. </p>
<p> <code>Tcl_FindCommand</code> searches for a command named <i>name</i> within the context of the namespace <i>contextNsPtr</i>. If the command cannot be found, NULL is returned. </p>
<p> <code>Tcl_GetNamespaceUnknownHandler</code> returns the unknown command handler for the namespace, or NULL if none is set. </p>
<p> <code>Tcl_SetNamespaceUnknownHandler</code> sets the unknown command handler for the namespace. If <i>handlerPtr</i> is NULL, then the handler is reset to its default. </p>
<h2>See Also</h2>
<p>Tcl_CreateCommand, Tcl_ListObjAppendElements, Tcl_SetVar </p>
<h2>Keywords</h2>
<p>namespace, command</p>
