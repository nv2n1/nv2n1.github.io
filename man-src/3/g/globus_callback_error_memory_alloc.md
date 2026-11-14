---
title: "globus_callback_error_memory_alloc(3)"
name: "globus_callback_error_memory_alloc"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callback_error_memory_alloc/"
description: "Globus Callback –"
---

<p>Globus Callback &#8211; </p>
<p> Globus Callback Function Interface.</p>
<h3>Modules</h3>
<p><code>Globus Callback API</code> </p>
<p> <code>Globus Callback Spaces</code> </p>
<p> <code>Globus Callback Signal Handling</code> </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_CALLBACK_MODULE</code><br />
 <i>Module descriptor. </i><br />
 #define <code>GLOBUS_POLL_MODULE</code><br />
 <i>Module descriptor. </i></p>
<h3>Typedefs</h3>
<p>typedef int <code>globus_callback_handle_t</code><br />
 <i>Periodic callback handle. </i><br />
 typedef int <code>globus_callback_space_t</code><br />
 <i>Callback space handle. </i><br />
 typedef struct<br />
 globus_l_callback_space_attr_s * <code>globus_callback_space_attr_t</code>&quot;<br />
 <i>Callback space attribute. </i></p>
<h3>Enumerations</h3>
<p>enum <code>globus_callback_error_type_t</code> { <code>GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE</code> = 1024, <code>GLOBUS_CALLBACK_ERROR_INVALID_SPACE</code>, <code>GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC</code>, <code>GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT</code>, <code>GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED</code>, <code>GLOBUS_CALLBACK_ERROR_NO_ACTIVE_CALLBACK</code> }<br />
 <i>Error types. </i></p>
<h2>Detailed Description</h2>
<p>Globus Callback Function Interface. </p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_CALLBACK_MODULE</h3>
<p>Module descriptor. Module descriptor for for globus_callback module. Must be activated before any of the following api is called. </p>
<p> Note: You would not normally activate this module directly. Activating the GLOBUS_COMMON_MODULE will in turn activate this also.</p>
<h3>#define GLOBUS_POLL_MODULE</h3>
<p>Module descriptor. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd></dl>
<p> Backward compatible name</p>
<h2>Typedef Documentation</h2>
<h3>typedef int <code>globus_callback_handle_t</code></h3>
<p>Periodic callback handle. This handle can be copied or compared, and represented as NULL with GLOBUS_NULL_HANDLE</p>
<h3>typedef struct globus_l_callback_space_attr_s* <code>globus_callback_space_attr_t</code></h3>
<p>Callback space attribute. This handle can be copied and represented as NULL with GLOBUS_NULL</p>
<h3>typedef int <code>globus_callback_space_t</code></h3>
<p>Callback space handle. This handle can be copied or compared and represented as NULL with GLOBUS_NULL_HANDLE</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_callback_error_type_t</code></h3>
<p>Error types. Possible error types returned by the api in this module. You can use the error API to check results against these types. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Error Handling Helpers</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_CALLBACK_ERROR_INVALID_CALLBACK_HANDLE </i></p>
<dd>The callback handle is not valid or it has already been destroyed</p>
<dt><i>GLOBUS_CALLBACK_ERROR_INVALID_SPACE </i></p>
<dd>The space handle is not valid or it has already been destroyed</p>
<dt><i>GLOBUS_CALLBACK_ERROR_MEMORY_ALLOC </i></p>
<dd>Could not allocate memory for an internal structure</p>
<dt><i>GLOBUS_CALLBACK_ERROR_INVALID_ARGUMENT </i></p>
<dd>One of the arguments is NULL or out of range</p>
<dt><i>GLOBUS_CALLBACK_ERROR_ALREADY_CANCELED </i></p>
<dd>Attempt to unregister callback again</p>
<dt><i>GLOBUS_CALLBACK_ERROR_NO_ACTIVE_CALLBACK </i></p>
<dd>Attempt to retrieve info about a callback not in callers&#8217;s stack</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
