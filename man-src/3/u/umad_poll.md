---
title: "umad_poll(3)"
name: "umad_poll"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_poll/"
description: "umad_poll – poll umad"
---

<p>umad_poll &#8211; poll umad</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_poll(int portid, int timeout_ms);</code></pre>
<h2>Description</h2>
<p><code>umad_poll()</code> waits up to <i>timeout_ms</i> milliseconds for a packet to be received from the port specified by <i>portid</i>. Once a packet is ready to be read, the function returns 0. After that the packet can be read using <code>umad_recv().</code> Otherwise, -ETIMEDOUT is returned. Note that successfully polling a port does not guarantee that the subsequent <code>umad_recv()</code> will be non blocking when several threads are using the same port. Instead, use a <i>timeout_ms</i> parameter of zero to <code>umad_recv()</code> to ensure a non-blocking read.</p>
<h2>Return Value</h2>
<p><code>umad_poll()</code> returns 0 on success, and a negative value on error as follows:<br />
&nbsp;<wbr>-EINVAL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>invalid port handle or agentid<br />
&nbsp;<wbr>-ETIMEDOUT poll operation timed out<br />
&nbsp;<wbr>-EIO&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>poll operation failed</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_recv/">umad_recv</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
