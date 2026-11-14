---
title: "libssh2_agent_userauth(3)"
name: "libssh2_agent_userauth"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_agent_userauth/"
description: "libssh2_agent_userauth – authenticate a session with a public key, with the help of ssh-agent"
---

<h2>NAME</h2>
<p> libssh2_agent_userauth &#8211; authenticate a session with a public key, with the help of ssh-agent</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_agent_userauth(LIBSSH2_AGENT *agent,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*username,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_agent_publickey&nbsp;<wbr>*identity);</p>
<h2>DESCRIPTION</h2>
<p> <i>agent</i> &#8211; ssh-agent handle as returned by <code><a href="/docs/linux/man/3-libssh2_agent_init/">libssh2_agent_init</a>(3)</code> </p>
<p> <i>username</i> &#8211; Remote user name to authenticate as. </p>
<p> <i>identity</i> &#8211; Public key to authenticate with, as returned by <code><a href="/docs/linux/man/3-libssh2_agent_get_identity/">libssh2_agent_get_identity</a>(3)</code> </p>
<p> Attempt public key authentication with the help of ssh-agent.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if succeeded, or a negative value for error.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_agent_init/">libssh2_agent_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_agent_get_identity/">libssh2_agent_get_identity</a>(3)</code> </p>
<h2>Index</h2>
