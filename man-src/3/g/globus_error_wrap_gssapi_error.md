---
title: "globus_error_wrap_gssapi_error(3)"
name: "globus_error_wrap_gssapi_error"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_wrap_gssapi_error/"
description: "Error Handling Helpers –"
---

<h2 class="name">NAME</h2>
<p> Error Handling Helpers &#8211; </p>
<h3>Functions</h3>
<p> globus_bool_t <code>globus_error_gssapi_match</code> (globus_object_t *error, globus_module_descriptor_t *module, const OM_uint32 major_status)<br />
 <i>Error Match. </i><br />
 globus_object_t * <code>globus_error_wrap_gssapi_error</code> (globus_module_descriptor_t *base_source, OM_uint32 major_status, OM_uint32 minor_status, int type, const char *source_file, const char *source_func, int source_line, const char *short_desc_format,&#8230;)<br />
 <i>Wrap GSSAPI Error. </i></p>
<h2>Detailed Description</h2>
<p> Helper functions for dealing with Globus GSSAPI Error objects. </p>
<p> This section defines utility functions for dealing with Globus GSSAPI Error objects.</p>
<h2>Function Documentation</h2>
<h3>globus_bool_t globus_error_gssapi_match (globus_object_t *error, globus_module_descriptor_t *module, const OM_uint32major_status)</h3>
<p> Error Match. Check whether the error originated from a specific module and match a specific major status. </p>
<p> This function checks whether the error or any of it&#8217;s causative errors originated from a specific module and contains a specific major status. If the module descriptor is left unspecified this function will check for any error of the specified major_status and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to perform the check<br />
 <i>module</i> The module descriptor to check for<br />
 <i>major_status</i> The major status to check for</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_TRUE</i> The error matched the module and major status<br />
 <i>GLOBUS_FALSE</i> The error failed to match the module and major status</dl>
<h3>globus_object_t* globus_error_wrap_gssapi_error (globus_module_descriptor_t *base_source, OM_uint32major_status, OM_uint32minor_status, inttype, const char *source_file, const char *source_func, intsource_line, const char *short_desc_format, &#8230;)</h3>
<p> Wrap GSSAPI Error. Allocate and initialize an error of type GLOBUS_ERROR_TYPE_GLOBUS which contains a causal error of type GLOBUS_ERROR_TYPE_GSSAPI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>major_status</i> The major status to use when generating the causal error.<br />
 <i>minor_status</i> The minor status to use when generating the causal error.<br />
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
<p> Generated automatically by Doxygen for globus_gssapi_error from the source code. </p>
<h2>Index</h2>
