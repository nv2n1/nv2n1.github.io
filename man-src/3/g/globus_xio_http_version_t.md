---
title: "globus_xio_http_version_t(3)"
name: "globus_xio_http_version_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_http_version_t/"
description: "Globus XIO HTTP Driver –"
---

<h2 class="name">NAME</h2>
<p> Globus XIO HTTP Driver &#8211; </p>
<h3>Modules</h3>
<p> <code>Opening/Closing</code> </p>
<p> <code>Reading/Writing</code> </p>
<p> <code>Server</code> </p>
<p> <code>Attributes and Cntls</code> </p>
<p> <code>Error Types</code> </p>
<h3>Data Structures</h3>
<p> struct <code>globus_xio_http_header_t</code><br />
 <i>HTTP Header. </i></p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_http_version_t</code> { , <code>GLOBUS_XIO_HTTP_VERSION_1_0</code>, <code>GLOBUS_XIO_HTTP_VERSION_1_1</code> } </p>
<h2>Detailed Description</h2>
<p> This driver implements the HTTP/1.0 and HTTP/1.1 protocols within the Globus XIO framework. It may be used with the tcp driver for the standard HTTP protocol stack, or may be combined with the gsi driver for a HTTPS implementation. </p>
<p> This implementation supports user-defined HTTP headers, persistent connections, and chunked transfer encoding.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_http_version_t</code></h3>
<p> Valid HTTP versions, used with the <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code> attribute and the <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code> handle control </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_XIO_HTTP_VERSION_1_0 </i></p>
<dd> HTTP/1.0</p>
<dt><i>GLOBUS_XIO_HTTP_VERSION_1_1 </i></p>
<dd> HTTP/1.1</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
