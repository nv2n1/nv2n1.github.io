---
title: "umad_set_addr_net(3)"
name: "umad_set_addr_net"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_set_addr_net/"
description: "umad_set_addr_net – set MAD address fields within umad buffer using network ordering"
---

<p>umad_set_addr_net &#8211; set MAD address fields within umad buffer using network ordering</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_set_addr_net(void *umad, int dlid, int dqp, int sl, int qkey);</code></pre>
<h2>Description</h2>
<p><code>umad_set_addr_net()</code> sets the MAD address fields within the specified <i>umad</i> buffer using the provided network ordered fields. <i>dlid</i> is the destination LID. <i>dqp</i> is the destination QP (queue pair). <i>sl</i> is the SL (service level). <i>qkey</i> is the Q_Key (queue key).</p>
<h2>Return Value</h2>
<p><code>umad_set_addr_net()</code> returns 0 on success, and a negative value on errors. Currently, there are no errors indicated.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_set_addr/">umad_set_addr</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
