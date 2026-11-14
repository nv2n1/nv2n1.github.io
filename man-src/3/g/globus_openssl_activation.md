---
title: "globus_openssl_activation(3)"
name: "globus_openssl_activation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_openssl_activation/"
description: "Activation –"
---

<h2 class="name">NAME</h2>
<p> Activation &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_OPENSSL_MODULE</code> </p>
<h2>Detailed Description</h2>
<p> Globus OpenSSL uses standard Globus module activation and deactivation. Before any OpenSSL functions are called, the following function must be called: </p>
<pre>
globus_module_activate(GLOBUS_OPENSSL_MODULE)
</pre>
<p> This function returns GLOBUS_SUCCESS if OpenSSL was successfully initialized, and you are therefore allowed to subsequently call OpenSSL functions. Otherwise, an error code is returned, and OpenSSL functions should not subsequently be called. This function may be called multiple times. </p>
<p> To deactivate the OpenSSL module , the following function must be called: </p>
<pre>
globus_module_deactivate(GLOBUS_OPENSSL_MODULE)
</pre>
<p> This function should be called once for each time OpenSSL was activated.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_OPENSSL_MODULE</h3>
<p> Module descriptor</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_openssl_module from the source code. </p>
<h2>Index</h2>
