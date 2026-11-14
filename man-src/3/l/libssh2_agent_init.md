---
title: "libssh2_agent_init(3)"
name: "libssh2_agent_init"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_init/"
description: "libssh2_agent_init – init an ssh-agent handle"
---

<h2>NAME</h2>
<p> libssh2_agent_init &#8211; init an ssh-agent handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_AGENT *libssh2_agent_init(LIBSSH2_SESSION *session);</p>
<h2>DESCRIPTION</h2>
<p> Init an ssh-agent handle. Returns the handle to an internal representation of an ssh-agent connection. After the successful initialization, an application can call <code><a href="/docs/linux/man/3-libssh2_agent_connect/">libssh2_agent_connect</a>(3)</code> to connect to a running ssh-agent. </p>
<p> Call <code><a href="/docs/linux/man/3-libssh2_agent_free/">libssh2_agent_free</a>(3)</code> to free the handle again after you&#8217;re doing using it.</p>
<h2>RETURN VALUE</h2>
<p> Returns a handle pointer or NULL if something went wrong. The returned handle is used as input to all other ssh-agent related functions libssh2 provides.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_connect/">libssh2_agent_connect</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_free/">libssh2_agent_free</a>(3)</code> </p>
<h2>Index</h2>
