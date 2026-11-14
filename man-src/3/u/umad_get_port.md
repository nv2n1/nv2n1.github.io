---
title: "umad_get_port(3)"
name: "umad_get_port"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_port/"
description: "umad_get_port, umad_release_port – open and close an InfiniBand port"
---

<p>umad_get_port, umad_release_port &#8211; open and close an InfiniBand port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_port(char *ca_name, int portnum, umad_port_t *port);
int umad_release_port(umad_port_t *port);</code></pre>
<h2>Description</h2>
<p><code>umad_get_port()</code> fills the <i>port</i> structure with the IB port attributes specified by <i>ca_name</i> and <i>portnum</i> , or the default port if <i>ca_name</i> is NULL and <i>portnum</i> is zero. If only one of <i>ca_name</i> and <i>portnum</i> are specified, the other is used as a filter. For example, passing a NULL <i>ca_name</i> and 2 for the <i>portnum</i> means get a port from any of the local IB devices, as long as it is the second port. Note that the library may use some reference scheme to support port caching therefore <code>umad_release_port()</code> should be called before the <i>port</i> structure can be deallocated. The argument <i>port</i> is an <code>umad_port_t</code> struct, as specified in &lt;infiniband/umad.h&gt;. </p>
<pre>typedef struct umad_port {
char ca_name[UMAD_CA_NAME_LEN]; /* Name of the device */
int portnum; /* Physical port number */
uint base_lid; /* Base port LID */
uint lmc; /* LMC of LID */
uint sm_lid; /* SM LID */
uint sm_sl; /* SM service level */
uint state; /* Logical port state */
uint phys_state; /* Physical port state */
uint rate; /* Port link bit rate */
uint64_t capmask; /* Port capabilities */
uint64_t gid_prefix; /* Gid prefix of this port */
uint64_t port_guid; /* GUID of this port */
} umad_port_t;</pre>
<p><code>umad_release_port()</code> releases the resources that were allocated by the <code>umad_get_port()</code> function for the specified IB <i>port</i>.</p>
<h2>Return Value</h2>
<p><code>umad_get_port()</code> and <code>umad_release_port()</code> return 0 on success, and a negative value on error.</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
