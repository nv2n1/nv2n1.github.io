---
title: "globus_error_openssl-h(3)"
name: "globus_error_openssl-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_openssl-h/"
description: "globus_error_openssl.h – Globus Generic Error."
---

<p>globus_error_openssl.h &#8211; Globus Generic Error.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_error_generic.h&#8217;<br />
 #include &#8216;openssl/err.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_OPENSSL_ERROR_MODULE</code> </p>
<p> #define <code>GLOBUS_ERROR_TYPE_OPENSSL</code> </p>
<h3>Functions</h3>
<p>unsigned long <code>globus_openssl_error_handle_get_error_code</code> (globus_openssl_error_handle_t error_code) </p>
<p> const char * <code>globus_openssl_error_handle_get_filename</code> (globus_openssl_error_handle_t handle) </p>
<p> int <code>globus_openssl_error_handle_get_linenumber</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_library</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_function</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_reason</code> (globus_openssl_error_handle_t handle) </p>
<p> const char * <code>globus_openssl_error_handle_get_data</code> (globus_openssl_error_handle_t handle) </p>
<p> int <code>globus_openssl_error_handle_get_data_flags</code> (globus_openssl_error_handle_t handle) </p>
<p> globus_object_t * <code>globus_error_construct_openssl_error</code> (globus_module_descriptor_t *base_source, globus_object_t *base_cause) </p>
<p> globus_object_t * <code>globus_error_initialize_openssl_error</code> (globus_object_t *error, globus_module_descriptor_t *base_source, globus_object_t *base_cause, globus_openssl_error_handle_t openssl_error_handle) </p>
<p> globus_object_t * <code>globus_error_wrap_openssl_error</code> (globus_module_descriptor_t *base_source, int error_type, const char *source_file, const char *source_func, int source_line, const char *format,&#8230;) </p>
<p> globus_bool_t <code>globus_error_match_openssl_error</code> (globus_object_t *error, unsigned long library, unsigned long function, unsigned long reason) </p>
<p> const char * <code>globus_error_openssl_error_get_filename</code> (globus_object_t *error) </p>
<p> int <code>globus_error_openssl_error_get_linenumber</code> (globus_object_t *error) </p>
<p> const char * <code>globus_error_openssl_error_get_library</code> (globus_object_t *error) </p>
<p> const char * <code>globus_error_openssl_error_get_function</code> (globus_object_t *error) </p>
<p> const char * <code>globus_error_openssl_error_get_reason</code> (globus_object_t *error) </p>
<p> const char * <code>globus_error_openssl_error_get_data</code> (globus_object_t *error) </p>
<p> int <code>globus_error_openssl_error_get_data_flags</code> (globus_object_t *error) </p>
<h2>Detailed Description</h2>
<p>Globus Generic Error. </p>
<h2>Function Documentation</h2>
<h3>const char* globus_error_openssl_error_get_data (globus_object_t *error)</h3>
<p>Get the OpenSSL Error Data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The error data for the OpenSSL error</dl>
<h3>int globus_error_openssl_error_get_data_flags (globus_object_t *error)</h3>
<p>Get the OpenSSL Error Data Flags </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The error data flags for the OpenSSL error</dl>
<h3>const char* globus_error_openssl_error_get_filename (globus_object_t *error)</h3>
<p>Get the OpenSSL filename where the error occurred </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The filename where the OpenSSL error occurred</dl>
<h3>const char* globus_error_openssl_error_get_function (globus_object_t *error)</h3>
<p>Get the OpenSSL filename where the error occurred </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The function name where the OpenSSL error occurred</dl>
<h3>const char* globus_error_openssl_error_get_library (globus_object_t *error)</h3>
<p>Get the OpenSSL library the error occurred in </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The library name where the OpenSSL error occurred</dl>
<h3>int globus_error_openssl_error_get_linenumber (globus_object_t *error)</h3>
<p>Get the OpenSSL line number where the error occurred </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The line number where the OpenSSL error occurred</dl>
<h3>const char* globus_error_openssl_error_get_reason (globus_object_t *error)</h3>
<p>Get the OpenSSL reason for the error </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The globus object that represents the error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The reason for the OpenSSL error</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_openssl_error from the source code.</p>
