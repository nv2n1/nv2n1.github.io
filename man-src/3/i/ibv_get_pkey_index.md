---
title: "ibv_get_pkey_index(3)"
name: "ibv_get_pkey_index"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_get_pkey_index/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_get_pkey_index - obtain the index in the P_Key table of a P_Key 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_get_pkey_index(struct ibv_context *context,
                       uint8_t port_num,
                       __be16 pkey);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Every InfiniBand HCA maintains a P_Key table for each of its ports that is indexed by an integer and with a P_Key in each element. Certain InfiniBand data structures that work with P_Keys expect a P_Key index, e.g. struct ibv_qp_attr and struct ib_mad_addr. Hence the function ibv_get_pkey_index() that accepts a P_Key in network byte order and that returns an index in the P_Key table as result.

<h2>RETURN VALUE</h2>

 

 ibv_get_pkey_index() returns the P_Key index on success, and -1 on error.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a>(3), <a HREF="/docs/linux/man/3-ibv_query_gid/">ibv_query_gid</a>(3), <a HREF="/docs/linux/man/3-ibv_query_pkey/">ibv_query_pkey</a>(3), <a HREF="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a>(3)

<h2>AUTHOR</h2>

 

 Bart Van Assche &lt;bvanassche [at] acm.org&gt; 

<h2>Index</h2>


