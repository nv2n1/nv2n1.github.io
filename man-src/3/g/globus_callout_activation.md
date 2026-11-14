---
title: "globus_callout_activation(3)"
name: "globus_callout_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_callout_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<p> Callback API Activation.</p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_CALLOUT_MODULE</code> </p>
<h3>Variables</h3>
<p> globus_module_descriptor_t <code>globus_i_callout_module</code> </p>
<h2>Detailed Description</h2>
<p> Callback API Activation. </p>
<p> Globus Callout API uses standard Globus module activation and deactivation. Before any Globus Callout API functions are called, the following function must be called: </p>
<pre>
*      globus_module_activate(GLOBUS_CALLOUT_MODULE)
* 
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus Callout API was successfully initialized, and you are therefore allowed to subsequently call Globus Callout API functions. Otherwise, an error code is returned, and Globus GSI Credential functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus Callout API, the following function must be called: </p>
<pre>
*    globus_module_deactivate(GLOBUS_CALLOUT_MODULE)
* 
</pre>
<p> This function should be called once for each time Globus Callout API was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_CALLOUT_MODULE</h3>
<p> Module descriptor</p>
<h2>Variable Documentation</h2>
<h3>globus_module_descriptor_t globus_i_callout_module</h3>
<p> <code>Initial value:</code> </p>
<pre>
=
{
    &quot;globus_callout_module&quot;,
    globus_l_callout_activate,
    globus_l_callout_deactivate,
    GLOBUS_NULL,
    GLOBUS_NULL,
    &amp;local_version
}
</pre>
<p> Module descriptor static initializer.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_callout from the source code. </p>
<h2>Index</h2>
