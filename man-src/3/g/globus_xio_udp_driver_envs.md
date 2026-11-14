---
title: "globus_xio_udp_driver_envs(3)"
name: "globus_xio_udp_driver_envs"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_udp_driver_envs/"
---

<h2 class="name">NAME</h2>
 

 Env Variables - The udp driver uses the following environment variables
<dl>
<dt>&bull;
<dd> GLOBUS_HOSTNAME Used when setting the hostname in the contact string
<dt>&bull;
<dd> GLOBUS_UDP_PORT_RANGE Used to restrict the port the udp socket binds to
<dt>&bull;
<dd> GLOBUS_XIO_SYSTEM_DEBUG Available if using a debug build. See globus_debug.h for format. The UDP driver uses globus_xio_system (along with the File and TCP drivers) which defines the following levels: TRACE for all function call tracing, DATA for data read and written counts, INFO for some special events, and RAW which dumps the raw buffers actually read or written. This can contain binary data, so be careful when you enable it.</dl>
 

<h2>Author</h2>

 

 Generated automatically by Doxygen for globus_xio from the source code. 

<h2>Index</h2>


