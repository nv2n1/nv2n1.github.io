---
title: "globus_xio_mode_e_error_type_t(3)"
name: "globus_xio_mode_e_error_type_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_mode_e_error_type_t/"
description: "Error Types –"
---

<h3>Enumerations</h3>
<p> enum <code>globus_xio_mode_e_error_type_t</code> { <code>GLOBUS_XIO_MODE_E_HEADER_ERROR</code> } </p>
<h2>Detailed Description</h2>
<p> The errors reported by MODE_E driver include GLOBUS_XIO_ERROR_COMMAND, GLOBUS_XIO_ERROR_MEMORY, GLOBUS_XIO_ERROR_STATE, GLOBUS_XIO_ERROR_PARAMETER, GLOBUS_XIO_ERROR_EOF, GLOBUS_XIO_ERROR_CANCELED, <code>GLOBUS_XIO_MODE_E_HEADER_ERROR</code> </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
</dt><dd> globus_xio_driver_error_match() </dd>
<p> globus_error_errno_match()</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_mode_e_error_type_t</code></h3>
<p> MODE_E driver specific error types </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_MODE_E_HEADER_ERROR </i></dt>
<dd> Indicates that the mode_e header is erroneous</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
