---
title: "libssh2_userauth_publickey(3)"
name: "libssh2_userauth_publickey"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_publickey/"
description: "libssh2_userauth_publickey – authenticate using a callback function"
---

<h2>NAME</h2>
<p> libssh2_userauth_publickey &#8211; authenticate using a callback function</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
int libssh2_userauth_publickey(LIBSSH2_SESSION *session,
                               const char *user,
                               const unsigned char *pubkeydata,
                               size_t pubkeydata_len,
                               sign_callback,
                               void **abstract);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Authenticate with the <i>sign_callback</i> callback that matches the prototype below</p>
<h2>CALLBACK</h2>
<pre><code>
int name(LIBSSH2_SESSION *session, unsigned char **sig, size_t *sig_len,
         const unsigned char *data, size_t data_len, void **abstract);
</code></pre>
<p> This function gets called&#8230;</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_userauth_publickey_fromfile_ex/">libssh2_userauth_publickey_fromfile_ex</a>(3)</code> </p>
<h2>Index</h2>
