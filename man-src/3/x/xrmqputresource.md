---
title: "xrmqputresource(3)"
name: "xrmqputresource"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrmqputresource/"
description: "XrmPutResource, XrmQPutResource, XrmPutStringResource, XrmQPutStringResource, XrmPutLineResource – store database resources"
---

<p>XrmPutResource, XrmQPutResource, XrmPutStringResource, XrmQPutStringResource, XrmPutLineResource &#8211; store database resources </p>
<h2>Syntax</h2>
<dl COMPACT>
<dt> #include &lt;X11/Xresource.h&gt;</dt>
<dd>void XrmPutResource(XrmDatabase *<i>database</i>, char *<i>specifier</i>, char *<i>type</i>, XrmValue *<i>value</i>);</dd>
<dd>void XrmQPutResource(XrmDatabase *<i>database</i>, XrmBindingList <i>bindings</i>, XrmQuarkList <i>quarks</i>, XrmRepresentation <i>type</i>, XrmValue *<i>value</i>);</dd>
<dd>void XrmPutStringResource(XrmDatabase *<i>database</i>, char *<i>specifier</i>, char *<i>value</i>);</dd>
<dd>void XrmQPutStringResource(XrmDatabase *<i>database</i>, XrmBindingList <i>bindings</i>, XrmQuarkList <i>quarks</i>, char *<i>value</i>);</dd>
<dd>void XrmPutLineResource(XrmDatabase *<i>database</i>, char *<i>line</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>bindings</i></dt>
<dd>Specifies a list of bindings.</dd>
<dt><i>database</i></dt>
<dd>Specifies the resource database.</dd>
<dt><i>line</i></dt>
<dd>Specifies the resource name and value pair as a single string.</dd>
<dt><i>quarks</i></dt>
<dd>Specifies the complete or partial name or the class list of the resource.</dd>
<dt><i>specifier</i></dt>
<dd>Specifies a complete or partial specification of the resource.</dd>
<dt><i>type</i></dt>
<dd>Specifies the type of the resource.</dd>
<dt><i>value</i></dt>
<dd>Specifies the value of the resource, which is specified as a string.</dd></dl>
<h2>Description</h2>
<p>If database contains NULL, <code>XrmPutResource</code> creates a new database and returns a pointer to it. <code>XrmPutResource</code> is a convenience function that calls <code>XrmStringToBindingQuarkList</code> followed by: </p>
<p> XrmQPutResource(database, bindings, quarks, XrmStringToQuark(type), value) </p>
<p> If the specifier and type are not in the Host Portable Character Encoding, the result is implementation-dependent. The value is stored in the database without modification. </p>
<p> If database contains NULL, <code>XrmQPutResource</code> creates a new database and returns a pointer to it. If a resource entry with the identical bindings and quarks already exists in the database, the previous type and value are replaced by the new specified type and value. The value is stored in the database without modification. </p>
<p> If database contains NULL, <code>XrmPutStringResource</code> creates a new database and returns a pointer to it. <code>XrmPutStringResource</code> adds a resource with the specified value to the specified database. <code>XrmPutStringResource</code> is a convenience function that first calls <code>XrmStringToBindingQuarkList</code> on the specifier and then calls <code>XrmQPutResource</code>, using a &#8220;String&#8221; representation type. If the specifier is not in the Host Portable Character Encoding, the result is implementation-dependent. The value is stored in the database without modification. </p>
<p> If database contains NULL, <code>XrmQPutStringResource</code> creates a new database and returns a pointer to it. <code>XrmQPutStringResource</code> is a convenience routine that constructs an <code>XrmValue</code> for the value string (by calling <code>strlen</code> to compute the size) and then calls <code>XrmQPutResource</code>, using a &#8220;String&#8221; representation type. The value is stored in the database without modification. </p>
<p> If database contains NULL, <code>XrmPutLineResource</code> creates a new database and returns a pointer to it. <code>XrmPutLineResource</code> adds a single resource entry to the specified database. The line should be in valid ResourceLine format (see section 15.1) terminated by a newline or null character; the database that results from using a string with incorrect syntax is implementation-dependent. The string is parsed in the locale of the database. If the <code>ResourceName</code> is not in the Host Portable Character Encoding, the result is implementation-dependent. Note that comment lines are not stored.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xrmgetresource/">XrmGetResource</a>(3), <a href="/docs/linux/man/3-xrminitialize/">XrmInitialize</a>(3), <a href="/docs/linux/man/3-xrmmergedatabases/">XrmMergeDatabases</a>(3), <a href="/docs/linux/man/3-xrmuniquequark/">XrmUniqueQuark</a>(3)<br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
