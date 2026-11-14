---
title: "libssh2_channel_direct_tcpip_ex(3)"
name: "libssh2_channel_direct_tcpip_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_direct_tcpip_ex/"
description: "libssh2_channel_direct_tcpip_ex – Tunnel a TCP connection through an SSH session"
---

<h2>NAME</h2>
<p> libssh2_channel_direct_tcpip_ex &#8211; Tunnel a TCP connection through an SSH session</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> LIBSSH2_CHANNEL * libssh2_channel_direct_tcpip_ex(LIBSSH2_SESSION *session, const char *host, int port, const char *shost, int sport); </p>
<p> LIBSSH2_CHANNEL * libssh2_channel_direct_tcpip(LIBSSH2_SESSION *session, const char *host, int port); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>host</i> &#8211; Third party host to connect to using the SSH host as a proxy. </p>
<p> <i>port</i> &#8211; Port on third party host to connect to. </p>
<p> <i>shost</i> &#8211; Host to tell the SSH server the connection originated on. </p>
<p> <i>sport</i> &#8211; Port to tell the SSH server the connection originated from. </p>
<p> Tunnel a TCP/IP connection through the SSH transport via the remote host to a third party. Communication from the client to the SSH server remains encrypted, communication from the server to the 3rd party host travels in cleartext. </p>
<h2>RETURN VALUE</h2>
<p> Pointer to a newly allocated LIBSSH2_CHANNEL instance, or NULL on errors.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
