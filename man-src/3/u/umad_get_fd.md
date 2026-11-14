---
title: "umad_get_fd(3)"
name: "umad_get_fd"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_get_fd/"
description: "umad_get_fd – get the umad fd for the requested port"
---

<p>umad_get_fd &#8211; get the umad fd for the requested port</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_get_fd(int portid);</code></pre>
<h2>Description</h2>
<p><code>umad_get_fd()</code> returns the umad fd for the port specified by <i>portid</i>.</p>
<h2>Return Value</h2>
<p><code>umad_get_fd()</code> returns the fd for the <i>portid</i> requested or -EINVAL if <i>portid</i> is invalid.</p>
<h2>Author</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd></dl>
