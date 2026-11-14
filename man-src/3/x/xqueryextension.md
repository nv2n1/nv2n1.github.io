---
title: "xqueryextension(3)"
name: "xqueryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xqueryextension/"
---

XQueryExtension, XListExtensions, XFreeExtensionList - list available extensions 

<h2>Syntax</h2><dl COMPACT><dd>Bool XQueryExtension(<i>display, name</i>, <i>major_opcode_return</i>, <i>first_event_return</i>, <i>first_error_return</i>)
<dd>char **XListExtensions(<i>display</i>, <i>nextensions_return</i>)
<dd>XFreeExtensionList(<i>list</i>)</dl><h2>Arguments</h2><dl COMPACT><dt><i>display</i>
<dd>Specifies the connection to the X server.
<dt><i>name</i>
<dd>Specifies the extension name.
<dt><i>major_opcode_return</i>
<dd>Returns the major opcode.
<dt><i>first_event_return</i>
<dd>Returns the first event code, if any.
<dt><i>first_error_return</i>
<dd>Returns the first error code, if any.
<dt><i>nextensions_return</i>
<dd>Returns the number of extensions listed.
<dt><i>list</i>
<dd>Specifies the list of extension names.</dl><h2>Description</h2>The <i>XQueryExtension</i> function determines if the named extension is present. If the extension is not present, <i>XQueryExtension</i> returns <i>False</i>; otherwise, it returns <i>True</i>. If the extension is present, <i>XQueryExtension</i> returns the major opcode for the extension to major_opcode_return; otherwise, it returns zero. Any minor opcode and the request formats are specific to the extension. If the extension involves additional event types, <i>XQueryExtension</i> returns the base event type code to first_event_return; otherwise, it returns zero. The format of the events is specific to the extension. If the extension involves additional error codes, <i>XQueryExtension</i> returns the base error code to first_error_return; otherwise, it returns zero. The format of additional data in the errors is specific to the extension. If the extension name is not in the Host Portable Character Encoding the result is implementation-dependent. Uppercase and lowercase matter; the strings ``thing'', ``Thing'', and ``thinG'' are all considered different names. 

 The <i>XListExtensions</i> function returns a list of all extensions supported by the server. If the data returned by the server is in the Latin Portable Character Encoding, then the returned strings are in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. 

 The <i>XFreeExtensionList</i> function frees the memory allocated by <i>XListExtensions</i>.
