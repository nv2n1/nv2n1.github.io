---
title: "umad_register2(3)"
name: "umad_register2"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_register2/"
description: "umad_register2 – register the specified management class and version for port"
---

<p>umad_register2 &#8211; register the specified management class and version for port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_register2(int port_fd, struct umad_reg_attr *attr, uint32_t *agent_id);</code></pre>
<h2>Description</h2>
<p><code>umad_register2()</code> registers for a MAD agent using the provided registration attributes <i>port_fd</i> the port on which to register the agent <i>attr</i> The registration attributes as defined by the structure passed. See below for details of this structure. <i>agent_id</i> returned on success. agent_id identifies the kernel MAD agent a MAD is received by or to be sent by. agent_id is returned in the umad header &quot;struct ib_user_mad&quot; on recv and specified in umad_send when sending. </p>
<h2>Registration Attribute Structure</h2>
<pre>struct umad_reg_attr {
uint8_t mgmt_class;
uint8_t mgmt_class_version;
uint32_t flags;
uint64_t method_mask[2];
uint32_t oui;
uint8_t rmpp_version;
};
<i>mgmt_class</i>
Management class to register for.
<i>mgmt_class_version</i>
Management class version to register for.
<i>flags</i>
Registration flags. If a flag specified is not supported by the kernel,
an error is returned, and the supported flags are returned in this field.
Current flags are:
UMAD_USER_RMPP -- flag to indicate the kernel should not process
RMPP packets. All RMPP packets will be treated like individual
MADs. The user is responsible for implementing the RMPP
protocol.
<i>method_mask</i>
A bit mask which indicates which unsolicited methods this agent should
receive. Setting this array to 0 will result in the agent only
receiving response MADs for which a request was sent.
<i>oui</i>
The oui (in host order) to use for vendor classes 0x30 - 0x4f.
Otherwise ignored.
<i>rmpp_version</i>
If the class supports RMPP and kernel RMPP is enabled (the default)
indicate which rmpp_version to use.</pre>
<h2>Return Value</h2>
<p><code>umad_register2()</code> returns 0 on success and +ERRNO on failure. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_unregister/">umad_unregister</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Ira Weiny &lt;ira.weiny [at] intel.com&gt;</p>
<dd></dl>
