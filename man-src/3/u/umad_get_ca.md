---
title: "umad_get_ca(3)"
name: "umad_get_ca"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_ca/"
description: "umad_get_ca, umad_release_ca – get and release InfiniBand device port attributes"
---

<p>umad_get_ca, umad_release_ca &#8211; get and release InfiniBand device port attributes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_ca(char *ca_name, umad_ca_t *ca);
int umad_release_ca(umad_ca_t *ca);</code></pre>
<h2>Description</h2>
<p><code>umad_get_ca()</code> gets the attributes of the InfiniBand device <i>ca_name</i>. It fills the <i>ca</i> structure with the device attributes specified by the <i>ca_name</i> or with the default device attributes if <i>ca_name</i> is NULL. <code>umad_release_ca()</code> should be called before the <i>ca</i> structure is deallocated. The argument <i>ca</i> is an <i>umad_ca_t</i> struct, as specified in &lt;infiniband/umad.h&gt;. </p>
<pre>typedef struct umad_ca {
char ca_name[UMAD_CA_NAME_LEN]; /* Name of the device */
uint node_type; /* Type of the device */
int numports; /* Number of physical ports */
char fw_ver[20]; /* FW version */
char ca_type[40]; /* CA type (e.g. MT23108, etc.) */
char hw_ver[20]; /* Hardware version */
uint64_t node_guid; /* Node GUID */
uint64_t system_guid; /* System image GUID */
umad_port_t *ports[UMAD_CA_MAX_PORTS]; /* Array of device port properties */
} umad_ca_t;</pre>
<p><code>umad_release_ca()</code> releases the resources that were allocated in the function <code>umad_get_ca()</code>.</p>
<h2>Return Value</h2>
<p><code>umad_get_ca()</code> and <code>umad_release_ca()</code> return 0 on success, and a negative value on error.</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
