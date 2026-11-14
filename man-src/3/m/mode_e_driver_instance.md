---
title: "mode_e_driver_instance(3)"
name: "mode_e_driver_instance"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mode_e_driver_instance/"
description: "Opening/Closing –"
---

<p>Opening/Closing &#8211; </p>
<p> An XIO handle with the mode_e driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. An XIO handle with the mode_e driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> If the handle is created with <code>globus_xio_handle_create()</code>, the contact string passed to ref <code>globus_xio_register_open()</code> call must contain a host name and service/port. The number of streams required can be specified on the attr using <code>GLOBUS_XIO_MODE_E_SET_NUM_STREAMS</code> (default is one stream). The stack of drivers to be used on the streams can be specified on the attr using <code>GLOBUS_XIO_MODE_E_SET_STACK</code> (default is a stack containing TCP driver). </p>
<p> When the XIO handle is closed, the mode_e driver will destroy its internal resources and close the stream(s). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
