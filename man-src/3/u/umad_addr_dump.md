---
title: "umad_addr_dump(3)"
name: "umad_addr_dump"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_addr_dump/"
description: "umad_addr_dump – dump addr structure to stderr"
---

<p>umad_addr_dump &#8211; dump addr structure to stderr</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

void umad_addr_dump(ib_mad_addr_t *addr);</code></pre>
<h2>Description</h2>
<p><code>umad_addr_dump()</code> dumps the given <i>addr</i> to stderr. The argument <i>addr</i> is an <i>ib_mad_addr_t</i> struct, as specified in &lt;infiniband/umad.h&gt;. </p>
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
<h2>Return Value</h2>
<p><code>umad_addr_dump()</code> returns no value.</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
