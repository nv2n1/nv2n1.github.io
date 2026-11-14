---
title: "umad_get_mad_addr(3)"
name: "umad_get_mad_addr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_mad_addr/"
description: "umad_get_mad_addr – get the address of the ib_mad_addr from a umad buffer"
---

<p>umad_get_mad_addr &#8211; get the address of the ib_mad_addr from a umad buffer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

ib_mad_addr_t *umad_get_mad_addr(void *umad);</code></pre>
<h2>Description</h2>
<p><code>umad_get_mad_addr()</code> returns a pointer to the ib_mad_addr struct within the specified <i>umad</i> buffer.</p>
<h2>Return Value</h2>
<p>The return value is a pointer to an <i>ib_mad_addr_t</i> struct, as specified in &lt;infiniband/umad.h&gt;. </p>
<pre>typedef struct ib_mad_addr {
uint32_t qpn;
uint32_t qkey;
uint16_t lid;
uint8_t sl;
uint8_t path_bits;
uint8_t grh_present;
uint8_t gid_index;
uint8_t hop_limit;
uint8_t traffic_class;
uint8_t gid[16];
uint32_t flow_label;
} ib_mad_addr_t;</pre>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
