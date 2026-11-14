---
title: "ordering_driver_errors(3)"
name: "ordering_driver_errors"
section: "3"
letter: "o"
url: "/docs/linux/man/3-ordering_driver_errors/"
description: "Error Types – The errors reported by ORDERING driver include GLOBUS_XIO_ERROR_COMMAND, GLOBUS_XIO_ERROR_MEMORY, GLOBUS_XIO_ERROR_STATE, GLOBUS_XIO_ERROR_CANCELED."
---

<p>Error Types &#8211; The errors reported by ORDERING driver include GLOBUS_XIO_ERROR_COMMAND, GLOBUS_XIO_ERROR_MEMORY, GLOBUS_XIO_ERROR_STATE, GLOBUS_XIO_ERROR_CANCELED.</p>
<h3>Enumerations</h3>
<pre><code>enum globus_xio_ordering_error_type_t { GLOBUS_XIO_ORDERING_ERROR_READ, GLOBUS_XIO_ORDERING_ERROR_CANCEL }</code></pre>
<h2>Detailed Description</h2>
<p>The errors reported by ORDERING driver include GLOBUS_XIO_ERROR_COMMAND, GLOBUS_XIO_ERROR_MEMORY, GLOBUS_XIO_ERROR_STATE, GLOBUS_XIO_ERROR_CANCELED. </p>
<p> <code>See also:</code></p>
<dl>
<dd>globus_xio_driver_error_match() </p>
<p> globus_error_errno_match()</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_ordering_error_type_t</code></h3>
<p>doxygen varargs filter stuff ORDERING driver specific error types </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_ORDERING_ERROR_READ </i></p>
<dd>Indicates that an error occured in reading data.</p>
<dt><i>GLOBUS_XIO_ORDERING_ERROR_CANCEL </i></p>
<dd>Indicates an error occured in canceling an operation.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
