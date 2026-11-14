---
title: "ibacm(7)"
name: "ibacm"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ibacm/"
---

ibacm - InfiniBand communication management assistant

<h2>Synopsis</h2>

<pre><code>#include &lt;infiniband/acm.h&gt;</code></pre>

<h2>Description</h2>

Used to resolve remote endpoint information before establishing communications over InfiniBand.

<h2>Notes</h2>

Th IB ACM provides scalable address and route resolution services over InfiniBand. It resolves system network names and IP addresses to InfiniBand path record data using efficient mechanisms, including caching of data. 

 The IB ACM provides information needed to establish a connection, but does not implement the communication management protocol. It provides services similar to rdma_getaddrinfo, rdma_resolve_addr, and rdma_resolve_route using IB multicast. The IB ACM does not require IPoIB or use standard naming services, such as DNS, and limits network communication, especially with the IB SA. The ib_acme utility assists in verifying what options of the ibacm service may be usable for the current fabric topology. 

 Client interactions with the ibacm service are done over sockets through a standard TCP connection. The librdmacm abstracts this interaction.

<h2>Return Codes</h2>

<dl><dt>== 0
<dd>success
<dt>!= 0
<dd>error</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-ib_acme/">ib_acme</a>(1), <a HREF="/docs/linux/man/1-ibacm/">ibacm</a>(1) 
