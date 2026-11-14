---
title: "globus_gsi_callback_error_errno(3)"
name: "globus_gsi_callback_error_errno"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback_error_errno/"
description: "GSI Callback Constants –"
---

<p>GSI Callback Constants &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_callback_error_t</code> { <code>GLOBUS_GSI_CALLBACK_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_CALLBACK_ERROR_VERIFY_CRED</code> = 1, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_NOT_YET_VALID</code> = 2, <code>GLOBUS_GSI_CALLBACK_ERROR_CANT_GET_LOCAL_CA_CERT</code> = 3, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_HAS_EXPIRED</code> = 4, <code>GLOBUS_GSI_CALLBACK_ERROR_INVALID_PROXY</code> = 5, <code>GLOBUS_GSI_CALLBACK_ERROR_LIMITED_PROXY</code> = 6, <code>GLOBUS_GSI_CALLBACK_ERROR_INVALID_CRL</code> = 7, <code>GLOBUS_GSI_CALLBACK_ERROR_REVOKED_CERT</code> = 8, <code>GLOBUS_GSI_CALLBACK_ERROR_MIXING_DIFFERENT_PROXY_TYPES</code> = 9, <code>GLOBUS_GSI_CALLBACK_ERROR_WITH_SIGNING_POLICY</code> = 10, <code>GLOBUS_GSI_CALLBACK_ERROR_OLD_GAA</code> = 11, <code>GLOBUS_GSI_CALLBACK_ERROR_CALLBACK_DATA</code> = 12, <code>GLOBUS_GSI_CALLBACK_ERROR_ERRNO</code> = 13, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_CHAIN</code> = 14, <code>GLOBUS_GSI_CALLBACK_ERROR_WITH_CALLBACK_DATA_INDEX</code> = 15, <code>GLOBUS_GSI_CALLBACK_ERROR_PROXY_PATH_LENGTH_EXCEEDED</code> = 16, <code>GLOBUS_GSI_CALLBACK_ERROR_LAST</code> = 18 } </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_callback_error_t</code></h3>
<p>GSI Callback Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_SUCCESS </i></p>
<dd>Success &#8211; never used</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_VERIFY_CRED </i></p>
<dd>Error verifying credential</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_CERT_NOT_YET_VALID </i></p>
<dd>The certificate is not yet valid</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_CANT_GET_LOCAL_CA_CERT </i></p>
<dd>Unable to discover a local trusted CA for a given certificate</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_CERT_HAS_EXPIRED </i></p>
<dd>The certificate has expired</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_INVALID_PROXY </i></p>
<dd>The proxy format is invalid</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_LIMITED_PROXY </i></p>
<dd>Limited proxies are not accepted</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_INVALID_CRL </i></p>
<dd>Invalid CRL</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_REVOKED_CERT </i></p>
<dd>The certificate has been revoked</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_MIXING_DIFFERENT_PROXY_TYPES </i></p>
<dd>The cert chain contains both legacy on RFC compliant proxies</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_WITH_SIGNING_POLICY </i></p>
<dd>Could not verify certificate chain against the signing policy for the issuing CA</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_OLD_GAA </i></p>
<dd>OldGAA error</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_CALLBACK_DATA </i></p>
<dd>Error with the callback data structure</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_ERRNO </i></p>
<dd>System error</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_CERT_CHAIN </i></p>
<dd>Error setting or getting the cert chain from callback data</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_WITH_CALLBACK_DATA_INDEX </i></p>
<dd>Error getting callback data index</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_PROXY_PATH_LENGTH_EXCEEDED </i></p>
<dd>Exceeded the path length specified in the proxy cert info extension</p>
<dt><i>GLOBUS_GSI_CALLBACK_ERROR_LAST </i></p>
<dd>Last marker &#8211; never used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_callback from the source code.</p>
