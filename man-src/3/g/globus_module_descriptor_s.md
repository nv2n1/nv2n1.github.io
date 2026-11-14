---
title: "globus_module_descriptor_s(3)"
name: "globus_module_descriptor_s"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_module_descriptor_s/"
description: "globus_module_descriptor_s –"
---

<h2 class="name">NAME</h2>
<p> globus_module_descriptor_s &#8211; </p>
<p> Module Descriptor.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_module.h&gt;</p>
<h3>Data Fields</h3>
<p> char * <code>module_name</code> </p>
<p> globus_module_activation_func_t <code>activation_func</code> </p>
<p> globus_module_deactivation_func_t <code>deactivation_func</code> </p>
<p> globus_module_atexit_func_t <code>atexit_func</code> </p>
<p> globus_module_get_pointer_func_t <code>get_pointer_func</code> </p>
<p> globus_version_t * <code>version</code> </p>
<p> <code>globus_error_print_friendly_t</code> <code>friendly_error_func</code> </p>
<h2>Detailed Description</h2>
<p> Module Descriptor. </p>
<p> Public data structure which contains function pointers to activate deactivate a module.</p>
<h2>Field Documentation</h2>
<h3>globus_module_activation_func_t globus_module_descriptor_s::activation_func</h3>
<p> Module activation function</p>
<h3>globus_module_atexit_func_t globus_module_descriptor_s::atexit_func</h3>
<p> Module atexit function</p>
<h3>globus_module_deactivation_func_t globus_module_descriptor_s::deactivation_func</h3>
<p> Module deactivation function</p>
<h3><code>globus_error_print_friendly_t</code> globus_module_descriptor_s::friendly_error_func</h3>
<p> Module error message function</p>
<h3>globus_module_get_pointer_func_t globus_module_descriptor_s::get_pointer_func</h3>
<p> Module get_pointer function</p>
<h3>char* globus_module_descriptor_s::module_name</h3>
<p> Module name string</p>
<h3>globus_version_t* globus_module_descriptor_s::version</h3>
<p> Module version </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
