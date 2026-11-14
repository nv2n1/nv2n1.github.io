---
title: "globus_error_v_construct_error(3)"
name: "globus_error_v_construct_error"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_v_construct_error/"
description: "Error Construction –"
---

<h2 class="name">NAME</h2>
<p> Error Construction &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_ERROR_TYPE_GLOBUS</code> </p>
<h3>Construct Error</h3>
<p> globus_object_t * <code>globus_error_construct_error</code> (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, int type, const char *source_file, const char *source_func, int source_line, const char *short_desc_format,&#8230;) </p>
<p> globus_object_t * <code>globus_error_v_construct_error</code> (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const int type, const char *source_file, const char *source_func, int source_line, const char *short_desc_format, va_list ap) </p>
<h3>Initialize Error</h3>
<p> globus_object_t * <code>globus_error_initialize_error</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, int type, const char *source_file, const char *source_func, int source_line, const char *short_desc_format, va_list ap) </p>
<h2>Detailed Description</h2>
<p> Create and initialize a Globus Generic Error object. </p>
<p> This section defines operations to create and initialize Globus Generic Error objects.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_ERROR_TYPE_GLOBUS</h3>
<p> Error type definition</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_error (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, inttype, const char *source_file, const char *source_func, intsource_line, const char *short_desc_format, &#8230;)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_GLOBUS </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
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
<h3>globus_object_t* globus_error_initialize_error (globus_object_t *error, <code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, inttype, const char *source_file, const char *source_func, intsource_line, const char *short_desc_format, va_listap)</h3>
<p> Initialize a previously allocated error of type GLOBUS_ERROR_TYPE_GLOBUS </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The previously allocated error object.<br />
 <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
 <i>type</i> The error type. We may reserve part of this namespace for common errors. Errors not in this space are assumed to be local to the originating module.<br />
 <i>source_file</i> Name of file. Use <code>FILE</code><br />
 <i>source_func</i> Name of function. Use _globus_func_name and declare your func with GlobusFuncName(&lt;name&gt;)<br />
 <i>source_line</i> Line number. Use <code>LINE</code><br />
 <i>short_desc_format</i> Short format string giving a succinct description of the error. To be passed on to the user.<br />
 <i>ap</i> Arguments for the format string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. You may have to call globus_error_put() on this object before passing it on.</dl>
<h3>globus_object_t* globus_error_v_construct_error (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const inttype, const char *source_file, const char *source_func, intsource_line, const char *short_desc_format, va_listap)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_GLOBUS </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
 <i>type</i> The error type. We may reserve part of this namespace for common errors. Errors not in this space are assumed to be local to the originating module.<br />
 <i>source_file</i> Name of file. Use <code>FILE</code><br />
 <i>source_func</i> Name of function. Use _globus_func_name and declare your func with GlobusFuncName(&lt;name&gt;)<br />
 <i>source_line</i> Line number. Use <code>LINE</code><br />
 <i>short_desc_format</i> Short format string giving a succinct description of the error. To be passed on to the user.<br />
 <i>ap</i> Arguments for the format string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
