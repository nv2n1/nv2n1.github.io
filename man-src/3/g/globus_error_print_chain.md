---
title: "globus_error_print_chain(3)"
name: "globus_error_print_chain"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_print_chain/"
description: "Error Handling Helpers –"
---

<h2 class="name">NAME</h2>
<p> Error Handling Helpers &#8211; </p>
<h3>Error Match</h3>
<p> <code>globus_bool_t</code> <code>globus_error_match</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *module, int type) </p>
<h3>Print Error Chain</h3>
<p> char * <code>globus_error_print_chain</code> (globus_object_t *error) </p>
<h3>Print User Friendly Error Message</h3>
<p> char * <code>globus_error_print_friendly</code> (globus_object_t *error) </p>
<h2>Detailed Description</h2>
<p> Helper functions for dealing with Globus Generic Error objects. </p>
<p> This section defines utility functions for dealing with Globus Generic Error objects.</p>
<h2>Function Documentation</h2>
<h3><code>globus_bool_t</code> globus_error_match (globus_object_t *error, <code>globus_module_descriptor_t</code> *module, inttype)</h3>
<p> Check whether the error originated from a specific module and is of a specific type. </p>
<p> This function checks whether the error or any of it&#8217;s causative errors originated from a specific module and is of a specific type. If the module descriptor is left unspecified this function will check for any error of the specified type and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error object for which to perform the check<br />
 <i>module</i> The module descriptor to check for<br />
 <i>type</i> The type to check for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_TRUE &#8211; the error matched the module and type GLOBUS_FALSE &#8211; the error failed to match the module and type</dl>
<h3>char* globus_error_print_chain (globus_object_t *error)</h3>
<p> Return a string containing all printable errors found in a error object and it&#8217;s causative error chain. </p>
<p> If the GLOBUS_ERROR_VERBOSE env is set, file, line and function info will also be printed (where available). Otherwise, only the module name will be printed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing all printable errors. This string needs to be freed by the user of this function.</dl>
<h3>char* globus_error_print_friendly (globus_object_t *error)</h3>
<p> Return a string containing error messages from the top 1 and bottom 3 objects, and, if found, show a friendly error message. The error chain will be searched from top to bottom until a friendly handler is found and a friendly message is created. </p>
<p> If the GLOBUS_ERROR_VERBOSE env is set, then the result from <code>globus_error_print_chain()</code> will be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error to print</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing a friendly error message. This string needs to be freed by the user of this function.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
