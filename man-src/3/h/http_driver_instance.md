---
title: "http_driver_instance(3)"
name: "http_driver_instance"
section: "3"
letter: "h"
url: "/docs/linux/man/3-http_driver_instance/"
description: "Opening/Closing –"
---

<h2 class="name">NAME</h2>
<p> Opening/Closing &#8211; </p>
<p> An XIO handle with the http driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. An XIO handle with the http driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> If the handle is created with <code>globus_xio_server_register_accept()</code>, then an HTTP service handle will be created when <code>globus_xio_register_open()</code> is called. The XIO application must call one of the functions in the <code>globus_xio_read()</code> family to receive the HTTP request metadata. This metadata will be returned in the data descriptor associated with that first read: the application should use the GLOBUS_XIO_HTTP_GET_REQUEST descriptor cntl to extract this metadata. </p>
<p> If the handle is created with <code>globus_xio_handle_create()</code>, then an HTTP client handle will be created when <code>globus_xio_register_open()</code> is called. HTTP request headers, version and method may be chosen by setting attributes. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio from the source code. </p>
<h2>Index</h2>
