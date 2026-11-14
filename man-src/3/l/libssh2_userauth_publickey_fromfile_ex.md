---
title: "libssh2_userauth_publickey_fromfile_ex(3)"
name: "libssh2_userauth_publickey_fromfile_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_publickey_fromfile_ex/"
description: "libssh2_userauth_publickey_fromfile – authenticate a session with a public key, read from a file"
---

<h2>NAME</h2>
<p> libssh2_userauth_publickey_fromfile &#8211; authenticate a session with a public key, read from a file</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
int libssh2_userauth_publickey_fromfile_ex(LIBSSH2_SESSION *session,
                                           const char *username,
                                           const char *publickey,
                                           const char *privatekey,
                                           const char *passphrase);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>username</i> &#8211; Pointer to user name to authenticate as. </p>
<p> <i>username_len</i> &#8211; Length of <i>username</i>. </p>
<p> <i>publickey</i> &#8211; Path name of the public key file. (e.g. /etc/ssh/hostkey.pub). If libssh2 is built against OpenSSL, this option can be set to NULL. </p>
<p> <i>privatekey</i> &#8211; Path name of the private key file. (e.g. /etc/ssh/hostkey) </p>
<p> <i>passphrase</i> &#8211; Passphrase to use when decoding <i>privatekey</i>. </p>
<p> Attempt public key authentication using a PEM encoded private key file stored on disk </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_TIMEOUT</i> &#8211; </p>
<p> <i>LIBSSH2_ERROR_PUBLICKEY_UNVERIFIED</i> &#8211; The username/public key combination was invalid. </p>
<p> <i>LIBSSH2_ERROR_AUTHENTICATION_FAILED</i> &#8211; Authentication using the supplied public key was not accepted. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
