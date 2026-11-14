---
title: "xrmenumeratedatabase(3)"
name: "xrmenumeratedatabase"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmenumeratedatabase/"
description: "XrmEnumerateDatabase – enumerate resource database entries"
---

<p>XrmEnumerateDatabase &#8211; enumerate resource database entries </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt; </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XrmEnumAllLevels</code> </td>
<td>
<dd>0
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>XrmEnumOneLevel</code> </td>
<td> 1
</td>
</tr>
</table>
<dd>Bool XrmEnumerateDatabase(XrmDatabase <i>database</i>, XrmNameList <i>name_prefix</i>, XrmClassList <i>class_prefix</i>, int <i>mode</i>, Bool (*<i>proc</i>)(), XPointer <i>arg</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>database</i></p>
<dd>Specifies the resource database.</p>
<dt><i>name_prefix</i></p>
<dd>Specifies the resource name prefix.</p>
<dt><i>class_prefix</i></p>
<dd>Specifies the resource class prefix.</p>
<dt><i>mode</i></p>
<dd>Specifies the number of levels to enumerate.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called for each matching entry.</p>
<dt><i>arg</i></p>
<dd>Specifies the user-supplied argument that will be passed to the procedure.</dl>
<h2>Description</h2>
<p>The <code>XrmEnumerateDatabase</code> function calls the specified procedure for each resource in the database that would match some completion of the given name/class resource prefix. The order in which resources are found is implementation-dependent. If mode is <code>XrmEnumOneLevel</code>, a resource must match the given name/class prefix with just a single name and class appended. If mode is <code>XrmEnumAllLevels</code>, the resource must match the given name/class prefix with one or more names and classes appended. If the procedure returns <code>True</code>, the enumeration terminates and the function returns <code>True</code>. If the procedure always returns <code>False</code>, all matching resources are enumerated and the function returns <code>False</code>. </p>
<p> The procedure is called with the following arguments: </p>
<p> (*<i>proc</i>)(<i>database</i>, <i>bindings</i>, <i>quarks</i>, <i>type</i>, <i>value</i>, <i>arg</i>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmDatabase&nbsp;*<i>database</i>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmBindingList&nbsp;<i>bindings</i>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmQuarkList&nbsp;<i>quarks</i>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmRepresentation&nbsp;*<i>type</i>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XrmValue&nbsp;*<i>value</i>;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XPointer&nbsp;<i>arg</i>; </p>
<p> The bindings and quarks lists are terminated by <code>NULLQUARK</code>. Note that pointers to the database and type are passed, but these values should not be modified. </p>
<p> The procedure must not modify the database. If Xlib has been initialized for threads, the procedure is called with the database locked and the result of a call by the procedure to any Xlib function using the same database is not defined.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmputresource/">XrmPutResource</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
