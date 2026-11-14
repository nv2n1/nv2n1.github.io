---
title: "globus_openssl_error_handle_get_filename(3)"
name: "globus_openssl_error_handle_get_filename"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_openssl_error_handle_get_filename/"
description: "Globus OpenSSL Error Object –"
---

<h2 class="name">NAME</h2>
<p> Globus OpenSSL Error Object &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_ERROR_TYPE_OPENSSL</code> </p>
<h3>Functions</h3>
<p> unsigned long <code>globus_openssl_error_handle_get_error_code</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_data</code> (globus_openssl_error_handle_t handle) </p>
<p> int <code>globus_openssl_error_handle_get_data_flags</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_filename</code> (globus_openssl_error_handle_t handle) </p>
<p> int <code>globus_openssl_error_handle_get_linenumber</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_library</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_function</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_reason</code> (globus_openssl_error_handle_t handle) </p>
<p> globus_object_t * <code>globus_error_construct_openssl_error</code> (globus_module_descriptor_t *base_source, globus_object_t *base_cause) </p>
<p> globus_object_t * <code>globus_error_initialize_openssl_error</code> (globus_object_t *error, globus_module_descriptor_t *base_source, globus_object_t *base_cause, globus_openssl_error_handle_t openssl_error_handle) </p>
<h2>Detailed Description</h2>
<p> The globus_openssl_error_handle_t is an opaque structure pointer which contains information about the OpenSSL call which generated an error. The functions in the <code>Globus OpenSSL Error Object </code> section of the API are used to create, manipulate, and destroy Globus OpenSSL Error object data.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_ERROR_TYPE_OPENSSL</h3>
<p> Error type definition</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_openssl_error (globus_module_descriptor_t *base_source, globus_object_t *base_cause)</h3>
<p> Allocate and initialize an error of type GLOBUS_ERROR_TYPE_OPENSSL This function, combined with <code>globus_error_initialize_openssl_error()</code> will recursively generate globus error objects (of type globus_object_t) from the errors on OpenSSL&#8217;s static error stack. The errors will be chained in a causal fashion to provide a path to the root cause of the actual error. </p>
<p> NOTE: the static stack OpenSSL implements for its errors currently only supports at most 16 errors, so if more are added, the errors that were added first will be wiped out. If 16 errors are counted in the chain of OpenSSL errors, its possible that some errors (including the original error) are missing. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating globus module.<br />
 <i>base_cause</i> The error object causing the error. This parameter should be NULL in nearly all cases, as the root cause of an error will most likely be in the OpenSSL code itself. The actual cause of the error is determined from the static stack of OpenSSL errors.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h3>globus_object_t* globus_error_initialize_openssl_error (globus_object_t *error, globus_module_descriptor_t *base_source, globus_object_t *base_cause, globus_openssl_error_handle_topenssl_error_handle)</h3>
<p> Initialize a previously allocated error of type GLOBUS_ERROR_TYPE_OPENSSL </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The previously allocated error object.<br />
 <i>base_source</i> Pointer to the originating module.<br />
 <i>base_cause</i> The error object causing the error. If this is the original error this parameter may be NULL.<br />
 <i>openssl_error_handle</i> The OpenSSL error handle associated with this error, this parameter should already be initialized to contain the OpenSSL error code associated with the error.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. You may have to call globus_error_put() on this object before passing it on.</dl>
<h3>const char* globus_openssl_error_handle_get_data (globus_openssl_error_handle_thandle)</h3>
<p> Get the OpenSSL error data which contains additional data about the error from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The error data</dl>
<h3>int globus_openssl_error_handle_get_data_flags (globus_openssl_error_handle_thandle)</h3>
<p> Get the OpenSSL error data flags from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The error data flags</dl>
<h3>unsigned long globus_openssl_error_handle_get_error_code (globus_openssl_error_handle_thandle)</h3>
<p> Get the OpenSSL error code which represents the OpenSSL error from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The error code</dl>
<h3>const char* globus_openssl_error_handle_get_filename (globus_openssl_error_handle_thandle)</h3>
<p> Get the filename where the OpenSSL error occurred from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The filename</dl>
<h3>const char* globus_openssl_error_handle_get_function (globus_openssl_error_handle_thandle)</h3>
<p> Get the function name where the OpenSSL error occurred from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The function name</dl>
<h3>const char* globus_openssl_error_handle_get_library (globus_openssl_error_handle_thandle)</h3>
<p> Get the library name where the OpenSSL error occurred in from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The library name</dl>
<h3>int globus_openssl_error_handle_get_linenumber (globus_openssl_error_handle_thandle)</h3>
<p> Get the line number on which the OpenSSL error occurred from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The line number</dl>
<h3>const char* globus_openssl_error_handle_get_reason (globus_openssl_error_handle_thandle)</h3>
<p> Get the reason string which caused the OpenSSL error from the OpenSSL error handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The OpenSSL error handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The reason string</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_openssl_error from the source code. </p>
<h2>Index</h2>
