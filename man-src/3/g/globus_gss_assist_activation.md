---
title: "globus_gss_assist_activation(3)"
name: "globus_gss_assist_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<p> Module Activation.</p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GSI_GSS_ASSIST_MODULE</code> </p>
<h2>Detailed Description</h2>
<p> Module Activation. </p>
<p> Globus GSI GSS Assist uses standard Globus module activation and deactivation. Before any Globus GSS Assist functions are called, the following function must be called: </p>
<pre>
globus_module_activate(GLOBUS_GSI_GSS_ASSIST_MODULE);
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus GSI GSS Assist was successfully initialized, and you are therefore allowed to call GSS Assist functions. Otherwise, an error code is returned, and GSS Assist functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus GSS Assist, the following function must be called: </p>
<pre>
globus_module_deactivate(GLOBUS_GSI_GSS_ASSIST_MODULE)
</pre>
<p> This function should be called once for each time Globus GSI GSS Assist was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_GSS_ASSIST_MODULE</h3>
<p> Module descriptor</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
