---
title: "globus_xio_tcp_driver_server(3)"
name: "globus_xio_tcp_driver_server"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_driver_server/"
description: "Server – globus_xio_server_create() causes a tcp listener socket to be created and listened upon. globus_xio_server_register_accept() performs an asynchronous accept(). globus_xio_server_register_c..."
---

<h2 class="name">NAME</h2>
<p> Server &#8211; <code>globus_xio_server_create()</code> causes a tcp listener socket to be created and listened upon. <code>globus_xio_server_register_accept()</code> performs an asynchronous accept(). <code>globus_xio_server_register_close()</code> cleans up the internal resources associated with the tcp server and calls close() on the listener socket (unless the socket was set on the server via the attr) </p>
<p> All accepted handles inherit all tcp specific attributes set in the attr to <code>globus_xio_server_create()</code>, but can be overridden with the attr to <code>globus_xio_register_open()</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
