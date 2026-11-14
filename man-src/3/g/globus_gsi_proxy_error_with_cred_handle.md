---
title: "globus_gsi_proxy_error_with_cred_handle(3)"
name: "globus_gsi_proxy_error_with_cred_handle"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy_error_with_cred_handle/"
description: "Proxy Constants –"
---

<p>Proxy Constants &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_proxy_error_t</code> { <code>GLOBUS_GSI_PROXY_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE</code> = 1, <code>GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE_ATTRS</code> = 2, <code>GLOBUS_GSI_PROXY_ERROR_WITH_PROXYCERTINFO</code> = 3, <code>GLOBUS_GSI_PROXY_ERROR_WITH_PROXYPOLICY</code> = 4, <code>GLOBUS_GSI_PROXY_ERROR_WITH_PATHLENGTH</code> = 5, <code>GLOBUS_GSI_PROXY_ERROR_WITH_X509_REQ</code> = 6, <code>GLOBUS_GSI_PROXY_ERROR_WITH_X509</code> = 7, <code>GLOBUS_GSI_PROXY_ERROR_WITH_X509_EXTENSIONS</code> = 8, <code>GLOBUS_GSI_PROXY_ERROR_WITH_PRIVATE_KEY</code> = 9, <code>GLOBUS_GSI_PROXY_ERROR_WITH_BIO</code> = 10, <code>GLOBUS_GSI_PROXY_ERROR_WITH_CREDENTIAL</code> = 11, <code>GLOBUS_GSI_PROXY_ERROR_WITH_CRED_HANDLE</code> = 12, <code>GLOBUS_GSI_PROXY_ERROR_WITH_CRED_HANDLE_ATTRS</code> = 13, <code>GLOBUS_GSI_PROXY_ERROR_ERRNO</code> = 14, <code>GLOBUS_GSI_PROXY_ERROR_SETTING_HANDLE_TYPE</code> = 15, <code>GLOBUS_GSI_PROXY_INVALID_PARAMETER</code> = 16, <code>GLOBUS_GSI_PROXY_ERROR_SIGNING</code> = 17, <code>GLOBUS_GSI_PROXY_ERROR_LAST</code> = 18 } </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_proxy_error_t</code></h3>
<p>Proxy Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_PROXY_ERROR_SUCCESS </i></p>
<dd>Success &#8211; never used</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE </i></p>
<dd>Invalid proxy handle state</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_HANDLE_ATTRS </i></p>
<dd>Invalid proxy handle attributes state</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_PROXYCERTINFO </i></p>
<dd>Error with ASN.1 proxycertinfo structure</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_PROXYPOLICY </i></p>
<dd>Error with ASN.1 proxypolicy structure</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_PATHLENGTH </i></p>
<dd>Error with proxy path length</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_X509_REQ </i></p>
<dd>Error with the X.509 request structure</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_X509 </i></p>
<dd>Error with X.509 structure</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_X509_EXTENSIONS </i></p>
<dd>Error with X.509 extensions</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_PRIVATE_KEY </i></p>
<dd>Error with private key</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_BIO </i></p>
<dd>Error with OpenSSL&#8217;s BIO handle</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_CREDENTIAL </i></p>
<dd>Error with credential</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_CRED_HANDLE </i></p>
<dd>Error with credential handle</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_WITH_CRED_HANDLE_ATTRS </i></p>
<dd>Error with credential handle attributes</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_ERRNO </i></p>
<dd>System error</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_SETTING_HANDLE_TYPE </i></p>
<dd>Unable to set proxy type</p>
<dt><i>GLOBUS_GSI_PROXY_INVALID_PARAMETER </i></p>
<dd>Invalid function parameter</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_SIGNING </i></p>
<dd>A error occurred while signing the proxy certificate</p>
<dt><i>GLOBUS_GSI_PROXY_ERROR_LAST </i></p>
<dd>Last marker &#8211; never used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_proxy_core from the source code.</p>
