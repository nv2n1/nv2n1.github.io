---
title: "libssh2_agent_disconnect(3)"
name: "libssh2_agent_disconnect"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_disconnect/"
description: "libssh2_agent_disconnect – close a connection to an ssh-agent"
---

<h2>NAME</h2>
<p> libssh2_agent_disconnect &#8211; close a connection to an ssh-agent</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_agent_disconnect(LIBSSH2_AGENT *agent);</p>
<h2>DESCRIPTION</h2>
<p> Close a connection to an ssh-agent. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if succeeded, or a negative value for error.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_connect/">libssh2_agent_connect</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_free/">libssh2_agent_free</a>(3)</code> </p>
<h2>Index</h2>
