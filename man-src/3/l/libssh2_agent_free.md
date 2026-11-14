---
title: "libssh2_agent_free(3)"
name: "libssh2_agent_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_free/"
description: "libssh2_agent_free – free an ssh-agent handle"
---

<h2>NAME</h2>
<p> libssh2_agent_free &#8211; free an ssh-agent handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_agent_free(LIBSSH2_AGENT *agent);</p>
<h2>DESCRIPTION</h2>
<p> Free an ssh-agent handle. This function also frees the internal collection of public keys.</p>
<h2>RETURN VALUE</h2>
<p> None.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_init/">libssh2_agent_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_disconnect/">libssh2_agent_disconnect</a>(3)</code> </p>
<h2>Index</h2>
