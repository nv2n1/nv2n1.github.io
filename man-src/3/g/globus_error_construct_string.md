---
title: "globus_error_construct_string(3)"
name: "globus_error_construct_string"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_construct_string/"
description: "globus_error_string.h –"
---

<h2 class="name">NAME</h2>
<p> globus_error_string.h &#8211; </p>
<p> Error Object Containing a String.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_error.h&#8217; </p>
<h3>Functions</h3>
<p> globus_object_t * <code>globus_error_construct_string</code> (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const char *fmt,&#8230;) </p>
<h2>Detailed Description</h2>
<p> Error Object Containing a String. </p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_string (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const char *fmt, &#8230;)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_STRING </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i><br />
 <i>base_cause</i><br />
 <i>fmt</i><br />
 <i>&#8230;</i></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
