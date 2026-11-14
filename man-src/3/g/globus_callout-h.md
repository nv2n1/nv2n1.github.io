---
title: "globus_callout-h(3)"
name: "globus_callout-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout-h/"
description: "globus_callout.h – Globus Callout Infrastructure."
---

<p>globus_callout.h &#8211; Globus Callout Infrastructure.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_callout_constants.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_CALLOUT_MODULE</code> </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_i_callout_handle_s * <code>globus_callout_handle_t</code>&quot; </p>
<p> typedef globus_result_t(* <code>globus_callout_function_t</code> )(va_list ap) </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_callout_handle_init</code> (<code>globus_callout_handle_t</code> *handle) </p>
<p> globus_result_t <code>globus_callout_handle_destroy</code> (<code>globus_callout_handle_t</code> handle) </p>
<p> globus_result_t <code>globus_callout_read_config</code> (<code>globus_callout_handle_t</code> handle, char *filename) </p>
<p> globus_result_t <code>globus_callout_register</code> (<code>globus_callout_handle_t</code> handle, char *type, char *library, char *symbol) </p>
<p> globus_result_t <code>globus_callout_call_type</code> (<code>globus_callout_handle_t</code> handle, char *type,&#8230;) </p>
<h3>Variables</h3>
<p>globus_module_descriptor_t <code>globus_i_callout_module</code> </p>
<h2>Detailed Description</h2>
<p>Globus Callout Infrastructure. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Meder</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_callout from the source code.</p>
