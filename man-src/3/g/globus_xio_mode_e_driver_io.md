---
title: "globus_xio_mode_e_driver_io(3)"
name: "globus_xio_mode_e_driver_io"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_mode_e_driver_io/"
description: "Reading/Writing – Mode E is unidirectional. Clients can only write and the server can only read. The globus_xio_register_read() enforce that the waitforbytes parameter should be one. When multiple ..."
---

<h2 class="name">NAME</h2>
<p> Reading/Writing &#8211; Mode E is unidirectional. Clients can only write and the server can only read. The <code>globus_xio_register_read()</code> enforce that the waitforbytes parameter should be one. When multiple transport streams are used between the client and the server, data might not be delivered in order. <code>globus_xio_data_descriptor_cntl()</code> can be used to get the offset of the data. </p>
<p> <code>globus_xio_register_write()</code> does not enforce any restriction on the waitforbytes parameter. </p>
<p> In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
