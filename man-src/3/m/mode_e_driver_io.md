---
title: "mode_e_driver_io(3)"
name: "mode_e_driver_io"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mode_e_driver_io/"
description: "Reading/Writing –"
---

<p>Reading/Writing &#8211; </p>
<p> Mode E is unidirectional. Mode E is unidirectional. </p>
<p> Clients can only write and the server can only read. The <code>globus_xio_register_read()</code> enforce that the waitforbytes parameter should be one. When multiple transport streams are used between the client and the server, data might not be delivered in order. <code>globus_xio_data_descriptor_cntl()</code> can be used to get the offset of the data. </p>
<p> <code>globus_xio_register_write()</code> does not enforce any restriction on the waitforbytes parameter. </p>
<p> In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio from the source code.</p>
