---
title: "mrmregisternamesinhierarchy(3)"
name: "mrmregisternamesinhierarchy"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mrmregisternamesinhierarchy/"
description: "MrmRegisterNamesInHierarchy — Registers the values associated with the names referenced in UIL within a single hierarchy (for example, UIL callback function names or UIL identifier names)"
---

<p><code>MrmRegisterNamesInHierarchy</code> &#8212; Registers the values associated with the names referenced in UIL within a single hierarchy (for example, UIL callback function names or UIL identifier names)</p>
<h2>Synopsis</h2>
<pre>#include &lt;Mrm/MrmPublic.h&gt;
<code>Cardinal MrmRegisterNamesInHierarchy</code>(
<code>MrmHierarchy hierarchy_id</code>,
<code>MrmRegisterArglist register_list</code>,
<code>MrmCount register_count</code>);</pre>
<h2>Description</h2>
<p>The <code>MrmRegisterNamesInHierarchy</code> function registers a vector of names and associated values for access in MRM. The values can be callback functions, pointers to user-defined data, or any other values. The information provided is used to resolve symbolic references occurring in UID files to their run-time values. For callbacks, this information provides the procedure address required by the Motif Toolkit. For names used as identifiers in UIL, this information provides any run-time mapping the application needs. </p>
<p> This function is similar to <code>MrmRegisterNames</code>, except that the scope of the names registered by <code>MrmRegisterNamesInHierarchy</code> is limited to the hierarchy specified by <i>hierarchy_id</i>, whereas the names registered by <code>MrmRegisterNames</code> have global scope. When MRM looks up a name, it first tries to find the name among those registered for the given hierarchy. If that lookup fails, it tries to find the name among those registered globally.</p>
<dl COMPACT>
<dt><i>hierarchy_id</i></p>
<dd>Specifies the hierarchy with which the names are to be associated.</p>
<dt><i>register_list</i></p>
<dd>Specifies a list of name/value pairs for the names to be registered. Each name is a case-sensitive, NULL-terminated ASCII string. Each value is a 32-bit quantity, interpreted as a procedure address if the name is a callback function, and uninterpreted otherwise.</p>
<dt><i>register_count</i></p>
<dd>Specifies the number of entries in <i>register_list</i>.</dl>
<p> The names in the list are case-sensitive. The list can be either ordered or unordered. </p>
<p> Callback functions registered through <code>MrmRegisterNamesInHierarchy</code> can be either regular or creation callbacks. Regular callbacks have declarations determined by Motif Toolkit and user requirements. Creation callbacks have the same format as any other callback: </p>
<pre><code>void CallBackProc</code>(
<code>Widget *widget_id</code>,
<code>Opaque tag</code>,
<code>XmAnyCallbackStruct *callback_data</code>);</pre>
<dl COMPACT>
<dt><i>widget_id</i></p>
<dd>Specifies the widget ID associated with the widget performing the callback (as in any callback function).</p>
<dt><i>tag</i></p>
<dd>Specifies the tag value (as in any callback function).</p>
<dt><i>callback_data</i></p>
<dd>Specifies a widget-specific data structure. This data structure has a minimum of two members: event and reason. The reason member is always set to <code>MrmCR_CREATE</code>.</dl>
<p> Note that the widget name and parent are available from the widget record accessible through <i>widget_id</i>.</p>
<h2>Return</h2>
<p>This function returns one of the following status return constants:</p>
<dl COMPACT>
<dt><code>MrmSUCCESS</code></p>
<dd>The function executed successfully.</p>
<dt><code>MrmFAILURE</code></p>
<dd>The function failed. </p>
</dl>
