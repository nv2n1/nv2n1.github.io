---
title: "globus_errno_error_utility(3)"
name: "globus_errno_error_utility"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_errno_error_utility/"
description: "Error Handling Helpers –"
---

<h2 class="name">NAME</h2>
<p> Error Handling Helpers &#8211; </p>
<h3>Error Match</h3>
<p> <code>globus_bool_t</code> <code>globus_error_errno_match</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *module, int system_errno) </p>
<h3>Wrap Errno Error</h3>
<p> globus_object_t * <code>globus_error_wrap_errno_error</code> (<code>globus_module_descriptor_t</code> *base_source, int system_errno, int type, const char *source_file, const char *source_func, int source_line, const char *short_desc_format,&#8230;) </p>
<h2>Detailed Description</h2>
<p> Helper functions for dealing with Globus Errno Error objects. </p>
<p> This section defines utility functions for dealing with Globus Errno Error objects.</p>
<h2>Function Documentation</h2>
<h3><code>globus_bool_t</code> globus_error_errno_match (globus_object_t *error, <code>globus_module_descriptor_t</code> *module, intsystem_errno)</h3>
<p> Check whether the error originated from a specific module and matches a specific errno. </p>
<p> This function checks whether the error or any of it&#8217;s causative errors originated from a specific module and contains a specific errno. If the module descriptor is left unspecified this function will check for any error of the specified errno and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to perform the check<br />
 <i>module</i> The module descriptor to check for<br />
 <i>system_errno</i> The errno to check for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_TRUE &#8211; the error matched the module and errno GLOBUS_FALSE &#8211; the error failed to match the module and errno</dl>
<h3>globus_object_t* globus_error_wrap_errno_error (<code>globus_module_descriptor_t</code> *base_source, intsystem_errno, inttype, const char *source_file, const char *source_func, intsource_line, const char *short_desc_format, &#8230;)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_GLOBUS which contains a causal error of type GLOBUS_ERROR_TYPE_ERRNO. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>system_errno</i> The errno to use when generating the causal error.<br />
 <i>type</i> The error type. We may reserve part of this namespace for common errors. Errors not in this space are assumed to be local to the originating module.<br />
 <i>source_file</i> Name of file. Use <code>FILE</code><br />
 <i>source_func</i> Name of function. Use _globus_func_name and declare your func with GlobusFuncName(&lt;name&gt;)<br />
 <i>source_line</i> Line number. Use <code>LINE</code><br />
 <i>short_desc_format</i> Short format string giving a succinct description of the error. To be passed on to the user.<br />
 <i>&#8230;</i> Arguments for the format string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
