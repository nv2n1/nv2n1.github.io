---
title: "gsi_driver_errors(3)"
name: "gsi_driver_errors"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsi_driver_errors/"
description: "Error Types –"
---

<h2 class="name">NAME</h2>
<p> Error Types &#8211; </p>
<p> The GSI driver uses mostly GSSAPI calls, so it generally just wraps the underlying GSSAPI errors or uses generic xio errors.</p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_gsi_error_t</code> { <code>GLOBUS_XIO_GSI_ERROR_INVALID_PROTECTION_LEVEL</code>, <code>GLOBUS_XIO_GSI_ERROR_WRAP_GSSAPI</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_TARGET_NAME</code>, <code>GLOBUS_XIO_GSI_ERROR_EMPTY_HOST_NAME</code>, <code>GLOBUS_XIO_GSI_AUTHORIZATION_FAILED</code>, <code>GLOBUS_XIO_GSI_ERROR_TOKEN_TOO_BIG</code> } </p>
<h2>Detailed Description</h2>
<p> The GSI driver uses mostly GSSAPI calls, so it generally just wraps the underlying GSSAPI errors or uses generic xio errors. </p>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> globus_xio_driver_error_match() </p>
<p> globus_error_gssapi_match() </p>
<p> globus_error_match_openssl_error()</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_gsi_error_t</code></h3>
<p> GSI driver specific error types. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_ERROR_INVALID_PROTECTION_LEVEL </i></p>
<dd> Indicates that the established context does not meet the required protecetion level.</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_WRAP_GSSAPI </i></p>
<dd> Wraps a GSSAPI error.</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_EMPTY_TARGET_NAME </i></p>
<dd> Indicates that GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION is set but that the target name is empty.</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_EMPTY_HOST_NAME </i></p>
<dd> Indicates that GLOBUS_XIO_GSI_HOST_AUTHORIZATION is set but that no host name is available.</p>
<dt><i>GLOBUS_XIO_GSI_AUTHORIZATION_FAILED </i></p>
<dd> Indicates that the peer is not authorized.</p>
<dt><i>GLOBUS_XIO_GSI_ERROR_TOKEN_TOO_BIG </i></p>
<dd> Indicates the the token being read is too big. Usually happens when someone tries to establish a non secure session with a endpoint that expects security</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio gsi driver from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAG">Author</a></p>
<dd></dl>
