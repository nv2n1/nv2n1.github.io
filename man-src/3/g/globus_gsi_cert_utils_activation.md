---
title: "globus_gsi_cert_utils_activation(3)"
name: "globus_gsi_cert_utils_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cert_utils_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GSI_CERT_UTILS_MODULE</code> </p>
<h2>Detailed Description</h2>
<p> Globus GSI Cert Utils uses standard Globus module activation and deactivation. Before any Globus GSI Cert Utils functions are called, the following function must be called: </p>
<pre>
globus_module_activate(GLOBUS_GSI_CERT_UTILS_MODULE)
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus GSI Credential was successfully initialized, and you are therefore allowed to subsequently call Globus GSI Cert Utils functions. Otherwise, an error code is returned, and Globus GSI Cert Utils functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus GSI Cert Utils, the following function must be called: </p>
<pre>
globus_module_deactivate(GLOBUS_GSI_CERT_UTILS_MODULE)
</pre>
<p> This function should be called once for each time Globus GSI Cert Utils was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_CERT_UTILS_MODULE</h3>
<p> Module descriptor</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_cert_utils from the source code. </p>
<h2>Index</h2>
