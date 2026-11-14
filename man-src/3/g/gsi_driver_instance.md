---
title: "gsi_driver_instance(3)"
name: "gsi_driver_instance"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsi_driver_instance/"
description: "Opening/Closing –"
---

<h2 class="name">NAME</h2>
<p> Opening/Closing &#8211; </p>
<p> An XIO handle with the gsi driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. An XIO handle with the gsi driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> If the handle is created with <code>globus_xio_server_register_accept()</code>, the <code>globus_xio_register_open()</code> call will proceed to accept a GSSAPI security context. Upon successful completion of the open, ie after the open callback has been called, the application may proceed to read or write data associated with the GSI session. </p>
<p> If the handle is created with <code>globus_xio_handle_create()</code>, then the XIO handle will implement the client-side (init) of the GSSAPI call sequence and establish a security context with the accepting side indicated by the contact_string passed to <code>globus_xio_register_open()</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio gsi driver from the source code. </p>
<h2>Index</h2>
