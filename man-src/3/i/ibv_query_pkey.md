---
title: "ibv_query_pkey(3)"
name: "ibv_query_pkey"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_pkey/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_query_pkey - query an InfiniBand port's P_Key table 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_query_pkey(struct ibv_context *context,
                   uint8_t port_num,
                   int index,
                   uint16_t *pkey);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_query_pkey() returns the P_Key value (in network byte order) in entry index of port port_num for device context context through the pointer pkey.

<h2>RETURN VALUE</h2>

 

 ibv_query_pkey() returns 0 on success, and -1 on error.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_gid/">ibv_query_gid</a>(3), <a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


