---
title: "umad_set_grh(3)"
name: "umad_set_grh"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_set_grh/"
description: "umad_set_grh – set GRH fields within umad buffer using host ordering"
---

<p>umad_set_grh &#8211; set GRH fields within umad buffer using host ordering</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_set_grh(void *umad, void *mad_addr);</code></pre>
<h2>Description</h2>
<p><code>umad_set_grh()</code> sets the GRH fields (grh_present, gid, hop_limit, traffic_class, flow_label) within the specified <i>umad</i> buffer based on the <i>mad_addr</i> supplied. The provided <i>mad_addr</i> fields are expected to be in host order. If the <i>mad_addr</i> pointer supplied is NULL, no GRH is set. The argument <i>mad_addr</i> is a pointer to an <i>ib_mad_addr_t</i> struct, as specified in <i>&lt;infiniband/umad.h&gt;.</i> The argument <i>umad</i> is a pointer to an <i>ib_user_mad_t</i> struct, as specified in <i>&lt;infiniband/umad.h&gt;.</i> </p>
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
} ib_mad_addr_t;
typedef struct ib_user_mad {
uint32_t agent_id;
uint32_t status;
uint32_t timeout_ms;
uint32_t retries;
uint32_t length;
ib_mad_addr_t addr;
uint8_t data[0];
} ib_user_mad_t;</pre>
<h2>Return Value</h2>
<p><code>umad_set_grh()</code> returns 0 on success, and a negative value on errors. Currently, there are no errors indicated.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_set_grh_net/">umad_set_grh_net</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
