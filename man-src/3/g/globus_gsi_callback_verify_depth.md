---
title: "globus_gsi_callback_verify_depth(3)"
name: "globus_gsi_callback_verify_depth"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback_verify_depth/"
description: "globus_gsi_callback_constants.h –"
---

<p>globus_gsi_callback_constants.h &#8211; </p>
<p> Globus GSI Callback.</p>
<h2>Synopsis</h2>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_CALLBACK_VERIFY_DEPTH</code> 100 </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_callback_error_t</code> { <code>GLOBUS_GSI_CALLBACK_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_CALLBACK_ERROR_VERIFY_CRED</code> = 1, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_NOT_YET_VALID</code> = 2, <code>GLOBUS_GSI_CALLBACK_ERROR_CANT_GET_LOCAL_CA_CERT</code> = 3, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_HAS_EXPIRED</code> = 4, <code>GLOBUS_GSI_CALLBACK_ERROR_INVALID_PROXY</code> = 5, <code>GLOBUS_GSI_CALLBACK_ERROR_LIMITED_PROXY</code> = 6, <code>GLOBUS_GSI_CALLBACK_ERROR_INVALID_CRL</code> = 7, <code>GLOBUS_GSI_CALLBACK_ERROR_REVOKED_CERT</code> = 8, <code>GLOBUS_GSI_CALLBACK_ERROR_MIXING_DIFFERENT_PROXY_TYPES</code> = 9, <code>GLOBUS_GSI_CALLBACK_ERROR_WITH_SIGNING_POLICY</code> = 10, <code>GLOBUS_GSI_CALLBACK_ERROR_OLD_GAA</code> = 11, <code>GLOBUS_GSI_CALLBACK_ERROR_CALLBACK_DATA</code> = 12, <code>GLOBUS_GSI_CALLBACK_ERROR_ERRNO</code> = 13, <code>GLOBUS_GSI_CALLBACK_ERROR_CERT_CHAIN</code> = 14, <code>GLOBUS_GSI_CALLBACK_ERROR_WITH_CALLBACK_DATA_INDEX</code> = 15, <code>GLOBUS_GSI_CALLBACK_ERROR_PROXY_PATH_LENGTH_EXCEEDED</code> = 16, <code>GLOBUS_GSI_CALLBACK_ERROR_LAST</code> = 18 } </p>
<h2>Detailed Description</h2>
<p>Globus GSI Callback. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Meder, Sam Lang</dl>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GSI_CALLBACK_VERIFY_DEPTH 100</h3>
<p>Constant passed to SSL_CTX_set_verify_depth() and SSL_set_verify_depth() to increase allowed certificate depth to 100 rather than the OpenSSL default of 9. 100 is an arbitrarily chosen large value.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_callback from the source code.</p>
