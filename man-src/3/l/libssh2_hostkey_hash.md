---
title: "libssh2_hostkey_hash(3)"
name: "libssh2_hostkey_hash"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_hostkey_hash/"
description: "libssh2_hostkey_hash – return a hash of the remote host’s key"
---

<h2>NAME</h2>
<p> libssh2_hostkey_hash &#8211; return a hash of the remote host&#8217;s key</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> const char * libssh2_hostkey_hash(LIBSSH2_SESSION *session, int hash_type); </p>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>hash_type</i> &#8211; One of: <code>LIBSSH2_HOSTKEY_HASH_MD5</code> or <code>LIBSSH2_HOSTKEY_HASH_SHA1</code>. </p>
<p> Returns the computed digest of the remote system&#8217;s hostkey. The length of the returned string is hash_type specific (e.g. 16 bytes for MD5, 20 bytes for SHA1).</p>
<h2>RETURN VALUE</h2>
<p> Computed hostkey hash value, or NULL if the information is not available (either the session has not yet been started up, or the requested hash algorithm was not available). The hash consists of raw binary bytes, not hex digits, so it is not directly printable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
