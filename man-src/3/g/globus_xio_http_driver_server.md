---
title: "globus_xio_http_driver_server(3)"
name: "globus_xio_http_driver_server"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_http_driver_server/"
description: "Server – The globus_xio_server_create() causes a new transport-specific listener socket to be created to handle new HTTP connections. globus_xio_server_register_accept() will accept a new connectio..."
---

<h2 class="name">NAME</h2>
<p> Server &#8211; The <code>globus_xio_server_create()</code> causes a new transport-specific listener socket to be created to handle new HTTP connections. <code>globus_xio_server_register_accept()</code> will accept a new connection for processing. <code>globus_xio_server_register_close()</code> cleans up the internal resources associated with the http server and calls close on the listener. </p>
<p> Multiple HTTP requests may be read in sequence from an HTTP server. After each request is processed and the response is sent (either by writing the entire entity body as specified by the Content-Length header or by using the GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY handle cntl), the next read will contain the metadata related to the next operation. Only one request will be in process at once&#8211;the previous request must have sent or received and EOF (whichever is applicable to the request type). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
