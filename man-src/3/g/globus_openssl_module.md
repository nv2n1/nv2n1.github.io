---
title: "globus_openssl_module(3)"
name: "globus_openssl_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_openssl_module/"
description: "Globus OpenSSL Module –"
---

<h2 class="name">NAME</h2>
<p> Globus OpenSSL Module &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<h2>Detailed Description</h2>
<p> The globus_openssl library is motivated by the desire to make OpenSSL thread safe. This is done by allocating a mutex pool and setting relevant callback functions in the module activation functions. </p>
<p> Any program that uses OpenSSL functions with Globus must include the <code>globus_openssl.h</code> header. </p>
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
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_openssl_module from the source code. </p>
<h2>Index</h2>
