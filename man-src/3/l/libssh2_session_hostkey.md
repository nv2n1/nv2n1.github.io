---
title: "libssh2_session_hostkey(3)"
name: "libssh2_session_hostkey"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_hostkey/"
description: "libssh2_session_hostkey – get the remote key"
---

<h2>NAME</h2>
<p> libssh2_session_hostkey &#8211; get the remote key</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> const char *libssh2_session_hostkey(LIBSSH2_SESSION *session,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size_t&nbsp;<wbr>*len, int&nbsp;<wbr>*type);</p>
<h2>DESCRIPTION</h2>
<p> Returns a pointer to the current host key, the value <i>len</i> points to will get the length of the key. </p>
<p> The value <i>type</i> points to the type of hostkey which is one of: LIBSSH2_HOSTKEY_TYPE_RSA, LIBSSH2_HOSTKEY_TYPE_DSS, or LIBSSH2_HOSTKEY_TYPE_UNKNOWN. </p>
<h2>RETURN VALUE</h2>
<p> A pointer, or NULL if something went wrong.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> </p>
<h2>Index</h2>
