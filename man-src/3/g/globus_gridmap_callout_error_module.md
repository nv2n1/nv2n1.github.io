---
title: "globus_gridmap_callout_error_module(3)"
name: "globus_gridmap_callout_error_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gridmap_callout_error_module/"
description: "Activation –"
---

<p>Activation &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GRIDMAP_CALLOUT_ERROR_MODULE</code> </p>
<h2>Detailed Description</h2>
<p>The Globus Gridmap Callout Error API uses standard Globus module activation and deactivation. Before any Globus Gridmap Callout Error API functions are called, the following function must be called: </p>
<pre>* globus_module_activate(GLOBUS_GRIDMAP_CALLOUT_ERROR_MODULE)
* </pre>
<p>This function returns GLOBUS_SUCCESS if the Globus Gridmap Callout Error API was successfully initialized, and you are therefore allowed to subsequently call Globus Gridmap Callout Error API functions. Otherwise, an error code is returned, and Globus GSI Credential functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus Gridmap Callout Error API, the following function must be called: </p>
<pre>* globus_module_deactivate(GLOBUS_GRIDMAP_CALLOUT_ERROR_MODULE)
* </pre>
<p>This function should be called once for each time Globus Gridmap Callout Error API was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GRIDMAP_CALLOUT_ERROR_MODULE</h3>
<p>Module descriptor</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gridmap_callout_error from the source code.</p>
