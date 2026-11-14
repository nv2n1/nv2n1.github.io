---
title: "globus_error_mutliple_add_chain(3)"
name: "globus_error_mutliple_add_chain"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_error_mutliple_add_chain/"
description: "globus_error_generic.h –"
---

<h2 class="name">NAME</h2>
<p> globus_error_generic.h &#8211; </p>
<p> Globus Error API.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_object.h&#8217;<br />
 #include &#8216;globus_module.h&#8217;<br />
 #include &lt;stdarg.h&gt; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_ERROR_TYPE_GLOBUS</code> </p>
<h3>Typedefs</h3>
<p> typedef char *(* <code>globus_error_print_friendly_t</code> )(globus_object_t *error, const globus_object_type_t *type) </p>
<h3>Functions</h3>
<p> <code>globus_module_descriptor_t</code> * <code>globus_error_get_source</code> (globus_object_t *error) </p>
<p> void <code>globus_error_set_source</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *source_module) </p>
<p> globus_object_t * <code>globus_error_get_cause</code> (globus_object_t *error) </p>
<p> void <code>globus_error_set_cause</code> (globus_object_t *error, globus_object_t *causal_error) </p>
<p> int <code>globus_error_get_type</code> (globus_object_t *error) </p>
<p> void <code>globus_error_set_type</code> (globus_object_t *error, const int type) </p>
<p> char * <code>globus_error_get_short_desc</code> (globus_object_t *error) </p>
<p> void <code>globus_error_set_short_desc</code> (globus_object_t *error, const char *short_desc_format,&#8230;) </p>
<p> char * <code>globus_error_get_long_desc</code> (globus_object_t *error) </p>
<p> void <code>globus_error_set_long_desc</code> (globus_object_t *error, const char *long_desc_format,&#8230;) </p>
<p> <code>globus_bool_t</code> <code>globus_error_match</code> (globus_object_t *error, <code>globus_module_descriptor_t</code> *module, int type) </p>
<p> char * <code>globus_error_print_chain</code> (globus_object_t *error) </p>
<p> char * <code>globus_error_print_friendly</code> (globus_object_t *error) </p>
<p> globus_object_t * <code>globus_error_construct_multiple</code> (<code>globus_module_descriptor_t</code> *base_source, int type, const char *fmt,&#8230;) </p>
<p> void <code>globus_error_mutliple_add_chain</code> (globus_object_t *multiple_error, globus_object_t *chain, const char *fmt,&#8230;) </p>
<p> globus_object_t * <code>globus_error_multiple_remove_chain</code> (globus_object_t *multiple_error) </p>
<h2>Detailed Description</h2>
<p> Globus Error API. </p>
<h2>Typedef Documentation</h2>
<h3>typedef char*(* globus_error_print_friendly_t)(globus_object_t *error, const globus_object_type_t *type)</h3>
<p> If registered with a module&#8217;s descriptor, this handler will be called on behalf of <code>globus_error_print_friendly()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error</i> The error chain that originated from this module. The top error object in the chain will be one created by this module and have a type of &#8216;type&#8217;; The remaining objects are the same as the cause chain used at creation time. The user can use globus_error_get_type(error) to get the error code (for GLOBUS_ERROR_TYPE_GLOBUS objects)<br />
 <i>type</i> The error object type for the top object in the error chain (e.g. GLOBUS_ERROR_TYPE_GLOBUS, GLOBUS_ERROR_TYPE_ERRNO)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The function should return a newly allocated string with a friendly error message explaining the error in more detail. This string should be considered the only message a user will see. If the module has nothing nice to say, it should return NULL so the next module in the error chain can be tried.</dl>
<p> If you think a friendly error from causes beneath you should be included, you may use globus_error_print_friendly(globus_error_get_cause(error)) within this handler to append to your message.</p>
<h2>Function Documentation</h2>
<h3>globus_object_t* globus_error_construct_multiple (<code>globus_module_descriptor_t</code> *base_source, inttype, const char *fmt, &#8230;)</h3>
<p> Multiple error type stuff Construct a container object for multiple error chains. Useful when an application tries many things (and each fails) before finally giving up; </p>
<p> Use <code>globus_error_mutliple_add_chain()</code> to add error objects/chains to this object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>base_source</i> Pointer to the originating module.<br />
 <i>type</i> The error type. We may reserve part of this namespace for common errors. Errors not in this space are assumed to be local to the originating module. <code>globus_error_match()</code> will match against this type, but not of the contained chains.<br />
 <i>fmt</i> a printf style format string describing the multiple errors</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The resulting error object. It is the user&#8217;s responsibility to eventually free this object using globus_object_free(). A globus_result_t may be obtained by calling globus_error_put() on this object.</dl>
<h3>globus_object_t* globus_error_multiple_remove_chain (globus_object_t *multiple_error)</h3>
<p> Remove an error chain from a multiple error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>multiple_error</i> The error from which to remove a chain. Must have been created with <code>globus_error_construct_multiple()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The removed error chain, or NULL if none found.</dl>
<h3>void globus_error_mutliple_add_chain (globus_object_t *multiple_error, globus_object_t *chain, const char *fmt, &#8230;)</h3>
<p> Add an error chain to a multiple error object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>multiple_error</i> The error to add the chain to. Must have been created with <code>globus_error_construct_multiple()</code><br />
 <i>chain</i> The chain to add to this error. This error object assumes control over &#8216;chain&#8221;s memory after this call.<br />
 <i>fmt</i> a printf style format string describing this chain</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
