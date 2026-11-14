---
title: "ibv_query_gid(3)"
name: "ibv_query_gid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_gid/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_query_gid - query an InfiniBand port's GID table 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_query_gid(struct ibv_context *context,
                  uint8_t port_num,
                  int index,
                  union ibv_gid *gid);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_query_gid() returns the GID value in entry index of port port_num for device context context through the pointer gid.

<h2>RETURN VALUE</h2>

 

 ibv_query_gid() returns 0 on success, and -1 on error.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_pkey/">ibv_query_pkey</a>(3), <a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


