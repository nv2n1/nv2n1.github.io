---
title: "globus_xio_tcp_error_type_t(3)"
name: "globus_xio_tcp_error_type_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_error_type_t/"
description: "Error Types –"
---

<h2 class="name">NAME</h2>
<p> Error Types &#8211; </p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_tcp_error_type_t</code> { <code>GLOBUS_XIO_TCP_ERROR_NO_ADDRS</code> } </p>
<h2>Detailed Description</h2>
<p> The TCP driver is very close to the system code, so most errors reported by it are converted from the system errno. A few of the exceptions are GLOBUS_XIO_ERROR_EOF, GLOBUS_XIO_ERROR_COMMAND, GLOBUS_XIO_ERROR_CONTACT_STRING, GLOBUS_XIO_ERROR_CANCELED, and <code>GLOBUS_XIO_TCP_ERROR_NO_ADDRS</code> </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> globus_xio_driver_error_match() </p>
<p> globus_error_errno_match()</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_tcp_error_type_t</code></h3>
<p> TCP driver specific error types </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_TCP_ERROR_NO_ADDRS </i></p>
<dd> Indicates that no IPv4/6 compatible sockets could be resolved for the specified hostname</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAG">Author</a></p>
<dd></dl>
