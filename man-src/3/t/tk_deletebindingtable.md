---
title: "tk_deletebindingtable(3)"
name: "tk_deletebindingtable"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_deletebindingtable/"
description: "Tk_CreateBindingTable, Tk_DeleteBindingTable, Tk_CreateBinding, Tk_DeleteBinding, Tk_GetBinding, Tk_GetAllBindings, Tk_DeleteAllBindings, Tk_BindEvent – invoke scripts in response to X events"
---

<p>Tk_CreateBindingTable, Tk_DeleteBindingTable, Tk_CreateBinding, Tk_DeleteBinding, Tk_GetBinding, Tk_GetAllBindings, Tk_DeleteAllBindings, Tk_BindEvent &#8211; invoke scripts in response to X events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_BindingTable
<code>Tk_CreateBindingTable(</code><i>interp</i><code>)</code>
<code>Tk_DeleteBindingTable(</code><i>bindingTable</i><code>)</code>
unsigned long
<code>Tk_CreateBinding(</code><i>interp, bindingTable, object, eventString, script, append</i><code>)</code>
int
<code>Tk_DeleteBinding(</code><i>interp, bindingTable, object, eventString</i><code>)</code>
const char *
<code>Tk_GetBinding(</code><i>interp, bindingTable, object, eventString</i><code>)</code>
<code>Tk_GetAllBindings(</code><i>interp, bindingTable, object</i><code>)</code>
<code>Tk_DeleteAllBindings(</code><i>bindingTable, object</i><code>)</code>
<code>Tk_BindEvent(</code><i>bindingTable, eventPtr, tkwin, numObjects, objectPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use when invoking bindings in binding table. Also used for returning results and errors from binding procedures.</p>
<dd>Tk_BindingTable <i>bindingTable</i> (in) Token for binding table; must have been returned by some previous call to <code>Tk_CreateBindingTable</code>.</p>
<dd>ClientData <i>object</i> (in) Identifies object with which binding is associated.</p>
<dd>const char <i>*eventString</i> (in) String describing event sequence.</p>
<dd>char <i>*script</i> (in) Tcl script to invoke when binding triggers.</p>
<dd>int <i>append</i> (in) Non-zero means append <i>script</i> to existing script for binding, if any; zero means replace existing script with new one.</p>
<dd>XEvent <i>*eventPtr</i> (in) X event to match against bindings in <i>bindingTable</i>.</p>
<dd>Tk_Window <i>tkwin</i> (in) Identifier for any window on the display where the event occurred. Used to find display-related information such as key maps.</p>
<dd>int <i>numObjects</i> (in) Number of object identifiers pointed to by <i>objectPtr</i>.</p>
<dd>ClientData <i>*objectPtr</i> (in) Points to an array of object identifiers: bindings will be considered for each of these objects in order from first to last. </p>
</dl>
<h2>Description</h2>
<p>These procedures provide a general-purpose mechanism for creating and invoking bindings. Bindings are organized in terms of <i>binding tables</i>. A binding table consists of a collection of bindings plus a history of recent events. Within a binding table, bindings are associated with <i>objects</i>. The meaning of an object is defined by clients of the binding package. For example, Tk keeps uses one binding table to hold all of the bindings created by the <code>bind</code> command. For this table, objects are pointers to strings such as window names, class names, or other binding tags such as <code>all</code>. Tk also keeps a separate binding table for each canvas widget, which manages bindings created by the canvas&#8217;s <code>bind</code> widget command; within this table, an object is either a pointer to the internal structure for a canvas item or a Tk_Uid identifying a tag. </p>
<p> The procedure <code>Tk_CreateBindingTable</code> creates a new binding table and associates <i>interp</i> with it (when bindings in the table are invoked, the scripts will be evaluated in <i>interp</i>). <code>Tk_CreateBindingTable</code> returns a token for the table, which must be used in calls to other procedures such as <code>Tk_CreateBinding</code> or <code>Tk_BindEvent</code>. </p>
<p> <code>Tk_DeleteBindingTable</code> frees all of the state associated with a binding table. Once it returns the caller should not use the <i>bindingTable</i> token again. </p>
<p> <code>Tk_CreateBinding</code> adds a new binding to an existing table. The <i>object</i> argument identifies the object with which the binding is to be associated, and it may be any one-word value. Typically it is a pointer to a string or data structure. The <i>eventString</i> argument identifies the event or sequence of events for the binding; see the documentation for the <code>bind</code> command for a description of its format. <i>script</i> is the Tcl script to be evaluated when the binding triggers. <i>append</i> indicates what to do if there already exists a binding for <i>object</i> and <i>eventString</i>: if <i>append</i> is zero then <i>script</i> replaces the old script; if <i>append</i> is non-zero then the new script is appended to the old one. <code>Tk_CreateBinding</code> returns an X event mask for all the events associated with the bindings. This information may be useful to invoke <code>XSelectInput</code> to select relevant events, or to disallow the use of certain events in bindings. If an error occurred while creating the binding (e.g., <i>eventString</i> refers to a non-existent event), then 0 is returned and an error message is left in <i>interp-&gt;result</i>. </p>
<p> <code>Tk_DeleteBinding</code> removes from <i>bindingTable</i> the binding given by <i>object</i> and <i>eventString</i>, if such a binding exists. <code>Tk_DeleteBinding</code> always returns <code>TCL_OK</code>. In some cases it may reset <i>interp-&gt;result</i> to the default empty value. </p>
<p> <code>Tk_GetBinding</code> returns a pointer to the script associated with <i>eventString</i> and <i>object</i> in <i>bindingTable</i>. If no such binding exists then NULL is returned and an error message is left in <i>interp-&gt;result</i>. </p>
<p> <code>Tk_GetAllBindings</code> returns in <i>interp-&gt;result</i> a list of all the event strings for which there are bindings in <i>bindingTable</i> associated with <i>object</i>. If there are no bindings for <i>object</i> then an empty string is returned in <i>interp-&gt;result</i>. </p>
<p> <code>Tk_DeleteAllBindings</code> deletes all of the bindings in <i>bindingTable</i> that are associated with <i>object</i>. </p>
<p> <code>Tk_BindEvent</code> is called to process an event. It makes a copy of the event in an internal history list associated with the binding table, then it checks for bindings that match the event. <code>Tk_BindEvent</code> processes each of the objects pointed to by <i>objectPtr</i> in turn. For each object, it finds all the bindings that match the current event history, selects the most specific binding using the priority mechanism described in the documentation for <code>bind</code>, and invokes the script for that binding. If there are no matching bindings for a particular object, then the object is skipped. <code>Tk_BindEvent</code> continues through all of the objects, handling exceptions such as errors, <code>break</code>, and <code>continue</code> as described in the documentation for <code>bind</code>. </p>
<h2>Keywords</h2>
<p>binding, event, object, script</p>
