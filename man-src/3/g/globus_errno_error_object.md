---
title: "globus_errno_error_object(3)"
name: "globus_errno_error_object"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_errno_error_object/"
description: "Error Construction –"
---

<h2 class="name">NAME</h2>
<p> Error Construction &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_ERROR_TYPE_ERRNO</code> </p>
<h3>Construct Error</h3>
<p> globus_object_t * <code>globus_error_construct_errno_error</code> (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const int system_errno) </p>
<h3>Initialize Error</h3>
<p> globus_object_t * <code>globus_error_initialize_errno_error</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const int system_errno) </p>
<h2>Detailed Description</h2>
<p> Create and initialize a Globus Errno Error object. </p>
<p> This section defines operations to create and initialize Globus Errno Error objects.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_ERROR_TYPE_ERRNO</h3>
<p> Error type definition</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_errno_error (<code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const intsystem_errno)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_ERRNO </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error, this parameter may be NULL.<br />
 <i>system_errno</i> The system errno.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h3>globus_object_t* globus_error_initialize_errno_error (globus_object_t *error, <code>globus_module_descriptor_t</code> *base_source, globus_object_t *base_cause, const intsystem_errno)</h3>
<p> Initialize a previously allocated error of type GLOBUS_ERROR_TYPE_ERRNO </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The previously allocated error object.<br />
 <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
 <i>system_errno</i> The system errno.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. You may have to call globus_error_put() on this object before passing it on.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
