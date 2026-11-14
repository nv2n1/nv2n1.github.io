---
title: "umad_register(3)"
name: "umad_register"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_register/"
description: "umad_register – register the specified management class and version for port"
---

<p>umad_register &#8211; register the specified management class and version for port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_register(int portid, int mgmt_class, int mgmt_version, uint8_t rmpp_version, long method_mask[16 / sizeof(long)]);</code></pre>
<h2>Description</h2>
<p><code>umad_register()</code> registers the specified management class, management version, and whether RMPP is being used for the port specified by the <i>portid</i> parameter. If <i>method_mask</i> array is provided, the caller is registered as a replier (server) for the methods having their corresponding bit on in the <i>method_mask</i>. If <i>method_mask</i> is NULL, the caller is registered as a MAD client, meaning that it can only receive replies on MADs that it sent (solicited MADs).</p>
<h2>Return Value</h2>
<p><code>umad_register()</code> returns non-negative agent id number on success, and a negative value on error as follows:<br />
&nbsp;<wbr>-EINVAL invalid port handle<br />
&nbsp;<wbr>-EPERM&nbsp;<wbr>&nbsp;<wbr>registration failed</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_register_oui/">umad_register_oui</a>(3),</code> <code><a href="/docs/linux/man/3-umad_unregister/">umad_unregister</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
