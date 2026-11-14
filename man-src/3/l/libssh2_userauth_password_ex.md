---
title: "libssh2_userauth_password_ex(3)"
name: "libssh2_userauth_password_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_password_ex/"
description: "libssh2_userauth_password_ex – authenticate a session with username and password"
---

<h2>NAME</h2>
<p> libssh2_userauth_password_ex &#8211; authenticate a session with username and password</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
int libssh2_userauth_password_ex(LIBSSH2_SESSION *session,
                                 const char *username,
                                 unsigned int username_len,
                                 const char *password,
                                 unsigned int password_len,
                                 LIBSSH2_PASSWD_CHANGEREQ_FUNC((*passwd_change_cb)));
#define libssh2_userauth_password(session, username, password) \
    libssh2_userauth_password_ex((session), (username),        \
                                 strlen(username),             \
                                 (password), strlen(password), NULL)
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>username</i> &#8211; Name of user to attempt plain password authentication for. </p>
<p> <i>username_len</i> &#8211; Length of username parameter. </p>
<p> <i>password</i> &#8211; Password to use for authenticating username. </p>
<p> <i>password_len</i> &#8211; Length of password parameter. </p>
<p> <i>passwd_change_cb</i> &#8211; If the host accepts authentication but requests that the password be changed, this callback will be issued. If no callback is defined, but server required password change, authentication will fail. </p>
<p> Attempt basic password authentication. Note that many SSH servers which appear to support ordinary password authentication actually have it disabled and use Keyboard Interactive authentication (routed via PAM or another authentication backed) instead. </p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> Some of the errors this function may return include: </p>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_PASSWORD_EXPIRED</i> &#8211; </p>
<p> <tt>IBSSH2_ERROR_AUTHENTICATION_FAILED</tt> &#8211; failed, invalid username/password or public/private key.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
