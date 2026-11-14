---
title: "globus_gsi_proxy_ssl_api(3)"
name: "globus_gsi_proxy_ssl_api"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy_ssl_api/"
description: "Globus GSI Proxy SSL API –"
---

<h2 class="name">NAME</h2>
<p> Globus GSI Proxy SSL API &#8211; </p>
<h3>Modules</h3>
<p> <code>ProxyCertInfo</code> </p>
<p> <code>ProxyPolicy</code> </p>
<h2>Detailed Description</h2>
<p> The globus_gsi_proxy_ssl library provides the ability to create a PROXYCERTINFO extension for inclusion in an X.509 certificate. The current specification for the extension is described in RFC 3820. </p>
<p> The library conforms to the ASN.1 implementation in the OpenSSL library, and provides an interface to convert from a DER encoded PROXYCERTINFO to its internal structure and vice-versa.</p>
<h2>ProxyCertInfo</h2>
<p> The <code>proxycertinfo.h</code> file defines a method of maintaining information about proxy certificates. For more information, see the documentation in <code>ProxyCertInfo </code></p>
<h2>ProxyPolicy</h2>
<p> The proxypolicy set of data structures and functions provides an interface to generating a PROXYPOLICY structure which is maintained as a field in the PROXYCERTINFO structure, and ultimately gets written to a DER encoded string. </p>
<p> Further Information about proxy policies is available in the X.509 Proxy Certificate Profile document. For more information, see the documentation in <code>ProxyPolicy </code></p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_proxy_ssl from the source code. </p>
<h2>Index</h2>
