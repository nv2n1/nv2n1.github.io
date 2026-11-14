---
title: "globus_openssl_error_utility(3)"
name: "globus_openssl_error_utility"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_openssl_error_utility/"
description: "Error Object Helper Functions –"
---

<h2 class="name">NAME</h2>
<p> Error Object Helper Functions &#8211; </p>
<h3>Functions</h3>
<p> globus_bool_t <code>globus_error_match_openssl_error</code> (globus_object_t *error, unsigned long library, unsigned long function, unsigned long reason) </p>
<p> globus_object_t * <code>globus_error_wrap_openssl_error</code> (globus_module_descriptor_t *base_source, int error_type, const char *source_file, const char *source_func, int source_line, const char *format,&#8230;) </p>
<h2>Detailed Description</h2>
<p> The functions in the <code>Error Object Helper Functions </code> section deal with Globus error objects constructed with OpenSSL error data. These functions manipulate the generic globus_object_t representation of an OpenSSL error.</p>
<h2>Function Documentation</h2>
<h3>globus_bool_t globus_error_match_openssl_error (globus_object_t *error, unsigned longlibrary, unsigned longfunction, unsigned longreason)</h3>
<p> Check whether the error originated from a specific library, from a specific function and is of a specific type. </p>
<p> This function checks whether the error or any of it&#8217;s causative errors originated from a specific library, specific function and is of a specific type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to perform the check<br />
 <i>library</i> The library to check for<br />
 <i>function</i> The function to check for<br />
 <i>reason</i> The type to check for</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_TRUE</i> Error matched<br />
 <i>GLOBUS_FALSE</i> Error failed to match</dl>
<h3>globus_object_t* globus_error_wrap_openssl_error (globus_module_descriptor_t *base_source, interror_type, const char *source_file, const char *source_func, intsource_line, const char *format, &#8230;)</h3>
<p> Wrap the OpenSSL error and create a wrapped globus error object from the error. </p>
<p> This function gets all the OpenSSL errors from the error list, and chains them using the globus error string object. The resulting globus error object is a wrapper to the OpenSSL error at the end of the chain. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> The module that the error was generated from<br />
 <i>error_type</i> The type of error encapsulating the OpenSSL error<br />
 <i>source_file</i> Name of file. Use <code>FILE</code><br />
 <i>source_func</i> Name of function. Use _globus_func_name and declare your func with GlobusFuncName(&lt;name&gt;)<br />
 <i>source_line</i> Line number. Use <code>LINE</code><br />
 <i>format</i> format string for the description of the error entry point where the OpenSSL error occurred, should be followed by parameters to fill the format string (like in printf).</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The globus error object. A globus_result_t object can be created using the globus_error_put function</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_error_put()</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_openssl_error from the source code. </p>
<h2>Index</h2>
