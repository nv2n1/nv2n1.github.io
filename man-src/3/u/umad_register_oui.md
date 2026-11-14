---
title: "umad_register_oui(3)"
name: "umad_register_oui"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_register_oui/"
description: "umad_register_oui – register the specified class in vendor range 2 for port"
---

<p>umad_register_oui &#8211; register the specified class in vendor range 2 for port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_register_oui(int portid, int mgmt_class, uint8_t rmpp_version, uint8_t oui[3], uint32_t method_mask[4]);</code></pre>
<h2>Description</h2>
<p><code>umad_register_oui()</code> registers the specified class in vendor range 2, the specified <i>oui</i>, and whether RMPP is being used for the port specified by the <i>portid</i> handle. If <i>method_mask</i> array is provided, the caller is registered as a replier (server) for the methods having their corresponding bit on in the <i>method_mask</i>. If <i>method_mask</i> is NULL, the caller is registered as a MAD client, meaning that it can only receive replies on MADs that it sent (solicited MADs).</p>
<h2>Return Value</h2>
<p><code>umad_register()</code> returns non-negative agent id number on success, and a negative value on error as follows:<br />
&nbsp;<wbr>-EINVAL invalid port handle or class is not in the vendor class 2 range<br />
&nbsp;<wbr>-EPERM&nbsp;<wbr>&nbsp;<wbr>registration failed</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_register/">umad_register</a></code>(3), <code><a href="/docs/linux/man/3-umad_unregister/">umad_unregister</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
