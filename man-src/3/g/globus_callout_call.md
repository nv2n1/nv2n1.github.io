---
title: "globus_callout_call(3)"
name: "globus_callout_call"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout_call/"
description: "Callout Invocation –"
---

<h2 class="name">NAME</h2>
<p> Callout Invocation &#8211; </p>
<p> Invoke callouts.</p>
<h3>Typedefs</h3>
<p> typedef globus_result_t(* <code>globus_callout_function_t</code> )(va_list ap) </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_callout_call_type</code> (<code>globus_callout_handle_t</code> handle, char *type,&#8230;) </p>
<h2>Detailed Description</h2>
<p> Invoke callouts. </p>
<p> This section defines a operation for invoking callouts by their abstract type.</p>
<h2>Typedef Documentation</h2>
<h3>typedef globus_result_t(* globus_callout_function_t)(va_list ap)</h3>
<p> Callout function type definition</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_callout_call_type (<code>globus_callout_handle_t</code>handle, char *type, &#8230;)</h3>
<p> Call a callout of specified abstract type </p>
<p> This function looks up the callouts corresponding to the given type and invokes them with the passed arguments. If a invoked callout returns an error it will be chained to a error of the type GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR and no more callouts will be called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> A configured callout handle<br />
 <i>type</i> The abstract type of the callout that is to be invoked</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS or a globus_result_t referring to an error object of one of the following types</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_CALLOUT_ERROR_TYPE_NOT_REGISTERED</i> Callout type not registered<br />
 <i>GLOBUS_CALLOUT_ERROR_CALLOUT_ERROR</i> Callout function error<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_DL</i> Error with dlopen or dlsym<br />
 <i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</i> Error caching dlopen handle<br />
 <i>GLOBUS_CALLOUT_ERROR_OUT_OF_MEMORY</i> Out of memory</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_callout from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
