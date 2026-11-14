---
title: "gsi_driver_server(3)"
name: "gsi_driver_server"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsi_driver_server/"
description: "Server –"
---

<h2 class="name">NAME</h2>
<p> Server &#8211; </p>
<p> <code>globus_xio_server_create()</code> causes a new transport-specific listener socket to be created to handle new GSI connections. <code>globus_xio_server_create()</code> causes a new transport-specific listener socket to be created to handle new GSI connections. </p>
<p> <code>globus_xio_server_register_accept()</code> will accept a new connection for processing. <code>globus_xio_server_register_close()</code> cleans up the internal resources associated with the http server and calls close on the listener. </p>
<p> All accepted handles inherit all gsi specific attributes set in the attr to <code>globus_xio_server_create()</code>, but can be overridden with the attr to <code>globus_xio_register_open()</code>. Furthermore, accepted handles will use the GSSAPI accept security context call unless explicitly overriden during the <code>globus_xio_register_open()</code> call (<code>GLOBUS_XIO_GSI_FORCE_SERVER_MODE</code>). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio gsi driver from the source code. </p>
<h2>Index</h2>
