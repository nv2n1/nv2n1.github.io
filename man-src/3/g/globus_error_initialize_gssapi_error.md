---
title: "globus_error_initialize_gssapi_error(3)"
name: "globus_error_initialize_gssapi_error"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_initialize_gssapi_error/"
description: "Error Construction –"
---

<h2 class="name">NAME</h2>
<p> Error Construction &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_ERROR_TYPE_GSSAPI</code> </p>
<h3>Functions</h3>
<p> globus_object_t * <code>globus_error_construct_gssapi_error</code> (globus_module_descriptor_t *base_source, globus_object_t *base_cause, const OM_uint32 major_status, const OM_uint32 minor_status)<br />
 <i>Construct Error. </i><br />
 globus_object_t * <code>globus_error_initialize_gssapi_error</code> (globus_object_t *error, globus_module_descriptor_t *base_source, globus_object_t *base_cause, const OM_uint32 major_status, const OM_uint32 minor_status)<br />
 <i>Initialize Error. </i></p>
<h2>Detailed Description</h2>
<p> Create and initialize a Globus GSSAPI Error object. </p>
<p> This section defines operations to create and initialize Globus GSSAPI Error objects.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_ERROR_TYPE_GSSAPI</h3>
<p> Error type definition</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_gssapi_error (globus_module_descriptor_t *base_source, globus_object_t *base_cause, const OM_uint32major_status, const OM_uint32minor_status)</h3>
<p> Construct Error. Allocate and initialize an error of type GLOBUS_ERROR_TYPE_GSSAPI </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error, this parameter may be NULL.<br />
 <i>major_status</i> The GSSAPI major status<br />
 <i>minor_status</i> The GSSAPI minor status</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h3>globus_object_t* globus_error_initialize_gssapi_error (globus_object_t *error, globus_module_descriptor_t *base_source, globus_object_t *base_cause, const OM_uint32major_status, const OM_uint32minor_status)</h3>
<p> Initialize Error. Initialize a previously allocated error of type GLOBUS_ERROR_TYPE_GSSAPI </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The previously allocated error object.<br />
 <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
 <i>major_status</i> The GSSAPI major status<br />
 <i>minor_status</i> The GSSAPI minor status</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. You may have to call globus_error_put() on this object before passing it on.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_error from the source code. </p>
<h2>Index</h2>
