---
title: "udp_driver_instance(3)"
name: "udp_driver_instance"
section: "3"
letter: "u"
url: "/docs/linux/man/3-udp_driver_instance/"
description: "Opening/Closing –"
---

<p>Opening/Closing &#8211; </p>
<p> An XIO handle with the udp driver can be created with <code>globus_xio_handle_create()</code>. An XIO handle with the udp driver can be created with <code>globus_xio_handle_create()</code>. </p>
<p> The handle can be created in two modes: open server or connected client. If the contact string does not have a host and port, the udp socket will accept messages from any sender. If a host and port is specified, the udp socket will be &#8216;connected&#8217; immediately to that host:port. This blocks packets from any sender other than the contact string. A handle that starts out as an open server can later be &#8216;connected&#8217; with <code>GLOBUS_XIO_UDP_CONNECT</code> (presumably after the first message is received from a sender and his contact info is available). </p>
<p> When the XIO handle is closed, the udp driver will destroy its internal resources and close the socket (unless this socket was set on the attr to <code>globus_xio_register_open()</code>).</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
