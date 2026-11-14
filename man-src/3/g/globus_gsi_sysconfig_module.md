---
title: "globus_gsi_sysconfig_module(3)"
name: "globus_gsi_sysconfig_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_module/"
description: "Activation –"
---

<p>Activation &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_SYSCONFIG_MODULE</code> </p>
<h2>Detailed Description</h2>
<p>Globus GSI System Configuration API uses standard Globus module activation and deactivation. Before any Globus GSI System Configuration API functions are called, the following function must be called: </p>
<pre>* globus_module_activate(GLOBUS_GSI_SYSCONFIG_MODULE)
* </pre>
<p>This function returns GLOBUS_SUCCESS if the Globus GSI System Configuration API was successfully initialized, and you are therefore allowed to subsequently call Globus GSI System Configuration API functions. Otherwise, an error code is returned, and Globus GSI Credential functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus GSI System Configuration API, the following function must be called: </p>
<pre>* globus_module_deactivate(GLOBUS_GSI_SYSCONFIG_MODULE)
* </pre>
<p>This function should be called once for each time Globus GSI System Configuration API was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_SYSCONFIG_MODULE</h3>
<p>Module descriptor</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_sysconfig from the source code.</p>
