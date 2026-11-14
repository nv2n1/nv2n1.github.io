---
title: "umad_close_port(3)"
name: "umad_close_port"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_close_port/"
description: "umad_close_port – close InfiniBand device port for umad access"
---

<p>umad_close_port &#8211; close InfiniBand device port for umad access</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_close_port(int portid);</code></pre>
<h2>Description</h2>
<p><code>umad_close_port()</code> closes the port specified by the handle <i>portid</i>.</p>
<h2>Return Value</h2>
<p><code>umad_close_port()</code> returns 0 on success, and a negative value on error. -EINVAL is returned if the <i>portid</i> is not a handle to a valid (open) port.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-umad_open_port/">umad_open_port</a></code>(3)</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
