---
title: "tcp_driver_envs(3)"
name: "tcp_driver_envs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcp_driver_envs/"
---

Env Variables - The tcp driver uses the following environment variables
<dl><dt>*
<dd>GLOBUS_HOSTNAME Used when setting the hostname in the contact string
<dt>*
<dd>GLOBUS_TCP_PORT_RANGE Used to restrict anonymous listener ports ex: GLOBUS_TCP_PORT_RANGE=4000,4100
<dt>*
<dd>GLOBUS_TCP_PORT_RANGE_STATE_FILE Used in conjunction with GLOBUS_TCP_PORT_RANGE to maintain last used port among many applications making use of the same port range.</dl>
 
&nbsp;<wbr> The tcp driver uses the following environment variables
<dl><dt>*
<dd>GLOBUS_HOSTNAME Used when setting the hostname in the contact string
<dt>*
<dd>GLOBUS_TCP_PORT_RANGE Used to restrict anonymous listener ports ex: GLOBUS_TCP_PORT_RANGE=4000,4100
<dt>*
<dd>GLOBUS_TCP_PORT_RANGE_STATE_FILE Used in conjunction with GLOBUS_TCP_PORT_RANGE to maintain last used port among many applications making use of the same port range.</dl>
 That last port + 1 will be used as a starting point within the specified tcp port range instead of always starting at the beginning. This is really only necessary when a machine is behind a stateful firewall which is holding a port in a different state than the application's machine. See bugzilla.globus.org, bug 1851 for more info. ex: GLOBUS_TCP_PORT_RANGE_STATE_FILE=/tmp/port_state (file will be created if it does not exist)
<dl><dt>*
<dd>GLOBUS_TCP_SOURCE_RANGE Used to restrict local ports used in a connection
<dt>*
<dd>GLOBUS_XIO_TCP_DEBUG Available if using a debug build. See globus_debug.h for format. The TCP driver defines the levels TRACE for all function call tracing and INFO for write buffer sizes
<dt>*
<dd>GLOBUS_XIO_SYSTEM_DEBUG Available if using a debug build. See globus_debug.h for format. The TCP driver uses globus_xio_system (along with the File and UDP drivers) which defines the following levels: TRACE for all function call tracing, DATA for data read and written counts, INFO for some special events, and RAW which dumps the raw buffers actually read or written. This can contain binary data, so be careful when you enable it.</dl>
 

<h2>Author</h2>

Generated automatically by Doxygen for globus xio from the source code.
