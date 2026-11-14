---
title: "globus_gass_transfer_module(3)"
name: "globus_gass_transfer_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_module/"
description: "Activation –"
---

<p>Activation &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GASS_TRANSFER_MODULE</code> </p>
<h2>Detailed Description</h2>
<p> The Globus GASS Transfer library uses the standard module activation and deactivation API to initialize its state. Before any GASS functions are called, the module must be activated </p>
<pre>
*    globus_module_activate(GLOBUS_GASS_TRANSFER_MODULE);
* 
</pre>
<p> This function returns GLOBUS_SUCCESS if the GASS library was successfully initialized. This may be called multiple times. </p>
<p> To deactivate the GASS transfer library, the following must be called </p>
<pre>
*    globus_module_deactivate(GLOBUS_GASS_TRANSFER_MODULE);
* 
</pre>
<p>&nbsp;<wbr></p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GASS_TRANSFER_MODULE</h3>
<p> Module descriptor</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code.</p>
