---
title: "libssh2_agent_list_identities(3)"
name: "libssh2_agent_list_identities"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_list_identities/"
description: "libssh2_agent_list_identities – request an ssh-agent to list of public keys."
---

<h2>NAME</h2>
<p> libssh2_agent_list_identities &#8211; request an ssh-agent to list of public keys.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_agent_list_identities(LIBSSH2_AGENT *agent);</p>
<h2>DESCRIPTION</h2>
<p> Request an ssh-agent to list of public keys, and stores them in the internal collection of the handle. Call <i><a href="/docs/linux/man/3-libssh2_agent_get_identity/">libssh2_agent_get_identity</a>(3)</i> to get a public key off the collection. </p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if succeeded, or a negative value for error.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_connect/">libssh2_agent_connect</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_get_identity/">libssh2_agent_get_identity</a>(3)</code> </p>
<h2>Index</h2>
