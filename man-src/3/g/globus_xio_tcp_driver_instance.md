---
title: "globus_xio_tcp_driver_instance(3)"
name: "globus_xio_tcp_driver_instance"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_driver_instance/"
description: "Opening/Closing – An XIO handle with the tcp driver can be created with either globus_xio_handle_create() or globus_xio_server_register_accept()."
---

<h2 class="name">NAME</h2>
<p> Opening/Closing &#8211; An XIO handle with the tcp driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> If the handle is created with <code>globus_xio_server_register_accept()</code>, the <code>globus_xio_register_open()</code> call does nothing more than initialize the internal handle with the accepted socket. </p>
<p> If the handle is created with <code>globus_xio_handle_create()</code>, and there is no handle set on the attr passed to the <code>globus_xio_register_open()</code> call, it performs the equivalent of an asynchronous connect() call. In this case, the contact string must contain a host name and service/port. Both the hostname and port number can be numeric or symbolic (eg: some.webserver.com:80 or 214.123.12.1:http). If the hostname is symbolic and it resolves to multiple ip addresses, each one will be attempted in succession, until the connect is successful or there are no more addresses. </p>
<p> When the XIO handle is closed, the tcp driver will destroy its internal resources and close the socket (unless this socket was set on an attr). Any write data pending in system buffers will be sent unless the linger option has been set. Any remaining data in recv buffers will be discarded and (on some systems) a connection reset sent to the peer. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
