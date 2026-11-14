---
title: "globus_callout_handle_t(3)"
name: "globus_callout_handle_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout_handle_t/"
description: "Callout Handle Operations –"
---

<h2 class="name">NAME</h2>
<p> Callout Handle Operations &#8211; </p>
<p> Manage a Globus Callout Handle structure.</p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_i_callout_handle_s * <code>globus_callout_handle_t</code>&quot; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_callout_handle_init</code> (<code>globus_callout_handle_t</code> *handle) </p>
<p> globus_result_t <code>globus_callout_handle_destroy</code> (<code>globus_callout_handle_t</code> handle) </p>
<h2>Detailed Description</h2>
<p> Manage a Globus Callout Handle structure. </p>
<p> This section defines operations for initializing and destroying Globus Callout Handle structure.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_i_callout_handle_s* <code>globus_callout_handle_t</code></h3>
<p> Callout handle type definition</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_callout_handle_destroy (<code>globus_callout_handle_t</code>handle)</h3>
<p> Destroy a Globus Callout Handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle that is to be destroyed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_callout_handle_init (<code>globus_callout_handle_t</code> *handle)</h3>
<p> Initialize a Globus Callout Handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> Pointer to the handle that is to be initialized</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns GLOBUS_SUCCESS or a globus_result_t referring to an error object of one of the following types</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_CALLOUT_ERROR_WITH_HASHTABLE</i> Hashtable initialization failed</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_callout from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
