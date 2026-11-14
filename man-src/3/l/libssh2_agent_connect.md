---
title: "libssh2_agent_connect(3)"
name: "libssh2_agent_connect"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_connect/"
description: "libssh2_agent_connect – connect to an ssh-agent"
---

<h2>NAME</h2>
<p> libssh2_agent_connect &#8211; connect to an ssh-agent</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_agent_connect(LIBSSH2_AGENT *agent);</p>
<h2>DESCRIPTION</h2>
<p> Connect to an ssh-agent running on the system. </p>
<p> Call <code><a href="/docs/linux/man/3-libssh2_agent_disconnect/">libssh2_agent_disconnect</a>(3)</code> to close the connection after you&#8217;re doing using it.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if succeeded, or a negative value for error.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_init/">libssh2_agent_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_disconnect/">libssh2_agent_disconnect</a>(3)</code> </p>
<h2>Index</h2>
