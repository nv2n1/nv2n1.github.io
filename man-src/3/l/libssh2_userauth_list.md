---
title: "libssh2_userauth_list(3)"
name: "libssh2_userauth_list"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_list/"
description: "libssh2_userauth_list – list supported authentication methods"
---

<h2>NAME</h2>
<p> libssh2_userauth_list &#8211; list supported authentication methods</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
char *
libssh2_userauth_list(LIBSSH2_SESSION *session, const char *username,
                      unsigned int username_len);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>username</i> &#8211; Username which will be used while authenticating. Note that most server implementations do not permit attempting authentication with different usernames between requests. Therefore this must be the same username you will use on later userauth calls. </p>
<p> <i>username_len</i> &#8211; Length of username parameter. </p>
<p> Send a <code>SSH_USERAUTH_NONE</code> request to the remote host. Unless the remote host is configured to accept none as a viable authentication scheme (unlikely), it will return <code>SSH_USERAUTH_FAILURE</code> along with a listing of what authentication schemes it does support. In the unlikely event that none authentication succeeds, this method with return NULL. This case may be distinguished from a failing case by examining <i><a href="/docs/linux/man/3-libssh2_userauth_authenticated/">libssh2_userauth_authenticated</a>(3)</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success a comma delimited list of supported authentication schemes. This list is internally managed by libssh2. On failure ruturns NULL.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_EAGAIN</i> &#8211; Marked for non-blocking I/O but the call</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
