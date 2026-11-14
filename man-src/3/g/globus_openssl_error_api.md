---
title: "globus_openssl_error_api(3)"
name: "globus_openssl_error_api"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_openssl_error_api/"
description: "Globus OpenSSL Error API –"
---

<h2 class="name">NAME</h2>
<p> Globus OpenSSL Error API &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Globus OpenSSL Error Object</code> </p>
<p> <code>Error Object Helper Functions</code> </p>
<h2>Detailed Description</h2>
<p> The globus_gsi_openssl_error functions provide a wrapper to error types defined by OpenSSL. The types and prototypes for the globus_gsi_openssl_error library are defined in the <code>globus_error_openssl.h</code> header. Applications which use these functions must link with the libglobus_openssl_error library. The library is distributed with a pkg-config module called globus-gsi-openssl-error to automatically find header and library paths.</p>
<h2>Library Initialization</h2>
<p> Globus GSI OpenSSL Error uses standard Globus module activation and deactivation. Before any Globus GSI OpenSSL Error functions are called, the following function must be called: </p>
<pre>
globus_module_activate(GLOBUS_GSI_OPENSSL_ERROR_MODULE)
</pre>
<p> This function returns GLOBUS_SUCCESS if Globus GSI OpenSSL Error was successfully initialized, and you are therefore allowed to subsequently call Globus GSI OpenSSL Error functions. Otherwise, an error code is returned, and Globus GSI OpenSSL Error functions should not be subsequently called. This function may be called multiple times. </p>
<p> To deactivate Globus GSI OpenSSL Error, the following function must be called: </p>
<pre>
globus_module_deactivate(GLOBUS_GSI_OPENSSL_ERROR_MODULE)
</pre>
<p> This function should be called once for each time Globus GSI OpenSSL Error was activated.</p>
<h2>Error Object Data Definition</h2>
<p> The globus_openssl_error_handle_t is an opaque structure pointer which contains information about the OpenSSL call which generated an error. The functions in the <code>Globus OpenSSL Error Object </code> section of the API are used to create, manipulate, and destroy Globus OpenSSL Error object data.</p>
<h2>Error Object Manipulators</h2>
<p> The functions in the <code>Error Object Helper Functions </code> section deal with Globus error objects constructed with OpenSSL error data. These functions manipulate the generic globus_object_t representation of an OpenSSL error.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_openssl_error from the source code. </p>
<h2>Index</h2>
