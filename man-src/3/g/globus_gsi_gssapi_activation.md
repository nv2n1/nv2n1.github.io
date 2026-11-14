---
title: "globus_gsi_gssapi_activation(3)"
name: "globus_gsi_gssapi_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gssapi_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<p> Module Activation.</p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GSI_GSSAPI_MODULE</code> </p>
<h2>Detailed Description</h2>
<p> Module Activation. </p>
<p> Globus GSI GSSAPI uses standard Globus module activation and deactivation. Before any Globus GSI GSSAPI functions are called, the following function should be called: </p>
<pre>
globus_module_activate(GLOBUS_GSI_GSSAPI_MODULE)
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus GSI GSSAPI was successfully initialized, and you are therefore allowed to subsequently call Globus GSI GSSAPI functions. Otherwise, an error code is returned, and Globus GSI GSSAPI functions should not subsequently be called. This function may be called multiple times. </p>
<p> To deactivate Globus GSI GSSAPI, the following function should be called: </p>
<pre>
globus_module_deactivate(GLOBUS_GSI_GSSAPI_MODULE)
</pre>
<p> This function should be called once for each time Globus GSI GSSAPI was activated. </p>
<p> Note that it is not mandatory to call the above functions.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_GSSAPI_MODULE</h3>
<p> Module descriptor</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
