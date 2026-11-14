---
title: "libipmidetect(3)"
name: "libipmidetect"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libipmidetect/"
description: "libipmidetect – a library of functions to determine if a node is detected or undetected"
---

<h2>NAME</h2>
<p> libipmidetect &#8211; a library of functions to determine if a node is detected or undetected</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ipmidetect.h&gt;</code> </p>
<p> <code>ipmidetect_t ipmidetect_handle_create(void);</code> </p>
<p> <code>int ipmidetect_handle_destroy(ipmidetect_t handle);</code> </p>
<p> <code>int ipmidetect_load_data(ipmidetect_t handle, const char *hostname, int port, int timeout_len);</code> </p>
<p> <code>int ipmidetect_errnum(ipmidetect_t handle);</code> </p>
<p> <code>char *ipmidetect_strerror(int errnum);</code> </p>
<p> <code>char *ipmidetect_errormsg(int errnum);</code> </p>
<p> <code>void ipmidetect_perror(ipmidetect_t handle, const char *msg);</code> </p>
<p> <code>int ipmidetect_get_detected_nodes_string(ipmidetect_t handle, char *buf, int buflen);</code> </p>
<p> <code>int ipmidetect_get_undetected_nodes_string(ipmidetect_t handle, char *buf, int buflen);</code> </p>
<p> <code>int ipmidetect_is_node_detected(ipmidetect_t handle, const char *node);</code> </p>
<p> <code>int ipmidetect_is_node_undetected(ipmidetect_t handle, const char *node);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>Libipmidetect</code> implements a high level API for determing which nodes in a cluster do or do-not support IPMI. This library is primarily useful for detecting whe nodes are removed from a cluster for servicing, so that IPMI applications can avoid unnecessary timeouts. The library interacts with the <code><a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8)</code> daemon.</p>
<h2>FILES</h2>
<p> /usr/include/ipmidetect.h</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2007 The Regents of the University of California. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ipmidetect/">ipmidetect</a>(8), <a href="/docs/linux/man/8-ipmidetectd/">ipmidetectd</a>(8) </p>
<p> <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
<h2>Index</h2>
