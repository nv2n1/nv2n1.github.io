---
title: "globus_error_get_long_desc(3)"
name: "globus_error_get_long_desc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_get_long_desc/"
description: "Error Data Accessors and Modifiers –"
---

<h2 class="name">NAME</h2>
<p> Error Data Accessors and Modifiers &#8211; </p>
<h3>Get Source</h3>
<p> <code>globus_module_descriptor_t</code> * <code>globus_error_get_source</code> (globus_object_t *error) </p>
<h3>Set Source</h3>
<p> void <code>globus_error_set_source</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *source_module) </p>
<h3>Get Cause</h3>
<p> globus_object_t * <code>globus_error_get_cause</code> (globus_object_t *error) </p>
<h3>Set Cause</h3>
<p> void <code>globus_error_set_cause</code> (globus_object_t *error, globus_object_t *causal_error) </p>
<h3>Get Type</h3>
<p> int <code>globus_error_get_type</code> (globus_object_t *error) </p>
<h3>Set Type</h3>
<p> void <code>globus_error_set_type</code> (globus_object_t *error, const int type) </p>
<h3>Get Short Description</h3>
<p> char * <code>globus_error_get_short_desc</code> (globus_object_t *error) </p>
<h3>Set Short Description</h3>
<p> void <code>globus_error_set_short_desc</code> (globus_object_t *error, const char *short_desc_format,&#8230;) </p>
<h3>Get Long Description</h3>
<p> char * <code>globus_error_get_long_desc</code> (globus_object_t *error) </p>
<h3>Set Long Description</h3>
<p> void <code>globus_error_set_long_desc</code> (globus_object_t *error, const char *long_desc_format,&#8230;) </p>
<h2>Detailed Description</h2>
<p> Get and set data in a Globus Generic Error object. </p>
<p> This section defines operations for accessing and modifying data in a Globus Generic Error object.</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_get_cause (globus_object_t *error)</h3>
<p> Retrieve the underlying error from a error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the causative error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The underlying error object if it exists, NULL if it doesn&#8217;t.</dl>
<h3>char* globus_error_get_long_desc (globus_object_t *error)</h3>
<p> Retrieve the long error description from a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the description</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The long error description of the object</dl>
<h3>char* globus_error_get_short_desc (globus_object_t *error)</h3>
<p> Retrieve the short error description from a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the description</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The short error description of the object</dl>
<h3><code>globus_module_descriptor_t</code>* globus_error_get_source (globus_object_t *error)</h3>
<p> Retrieve the originating module descriptor from a error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the module descriptor</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The originating module descriptor.</dl>
<h3>int globus_error_get_type (globus_object_t *error)</h3>
<p> Retrieve the error type from a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error from which to retrieve the error type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The error type of the object</dl>
<h3>void globus_error_set_cause (globus_object_t *error, globus_object_t *causal_error)</h3>
<p> Set the causative error in a error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the causative error.<br />
 <i>causal_error</i> The causative error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h3>void globus_error_set_long_desc (globus_object_t *error, const char *long_desc_format, &#8230;)</h3>
<p> Set the long error description in a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the description<br />
 <i>long_desc_format</i> Longer format string giving a more detailed explanation of the error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h3>void globus_error_set_short_desc (globus_object_t *error, const char *short_desc_format, &#8230;)</h3>
<p> Set the short error description in a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the description<br />
 <i>short_desc_format</i> Short format string giving a succinct description of the error. To be passed on to the user.<br />
 <i>&#8230;</i> Arguments for the format string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h3>void globus_error_set_source (globus_object_t *error, <code>globus_module_descriptor_t</code> *source_module)</h3>
<p> Set the originating module descriptor in a error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the causative error<br />
 <i>source_module</i> The originating module descriptor</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h3>void globus_error_set_type (globus_object_t *error, const inttype)</h3>
<p> Set the error type in a generic globus error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to set the error type<br />
 <i>type</i> The error type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAY">Author</a></p>
<dd></dl>
