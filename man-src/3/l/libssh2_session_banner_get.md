---
title: "libssh2_session_banner_get(3)"
name: "libssh2_session_banner_get"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_banner_get/"
description: "libssh2_session_banner_get – get the remote banner"
---

<h2>NAME</h2>
<p> libssh2_session_banner_get &#8211; get the remote banner</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> const char *libssh2_session_banner_get(oLIBSSH2_SESSION *session);</p>
<h2>DESCRIPTION</h2>
<p> Once the session has been setup and <i><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3)</i> has completed successfully, this function can be used to get the server id from the banner each server presents.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a string or NULL if something failed. The data pointed to will be allocated and associated to the session handle and will be freed by libssh2 when <i><a href="/docs/linux/man/3-libssh2_session_free/">libssh2_session_free</a>(3)</i> is used.</p>
<h2>AVAILABILITY</h2>
<p> Added in 1.4.0</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_banner_set/">libssh2_session_banner_set</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_session_handshake/">libssh2_session_handshake</a>(3),</code> <code><a href="/docs/linux/man/3-libssh2_session_free/">libssh2_session_free</a>(3)</code> </p>
<h2>Index</h2>
