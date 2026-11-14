---
title: "libssh2_channel_setenv_ex(3)"
name: "libssh2_channel_setenv_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_channel_setenv_ex/"
description: "libssh2_channel_setenv_ex – set an environment variable on the channel"
---

<h2>NAME</h2>
<p> libssh2_channel_setenv_ex &#8211; set an environment variable on the channel</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_channel_setenv_ex(LIBSSH2_CHANNEL *channel, char *varname, unsigned int varname_len, const char *value, unsigned int value_len); </p>
<p> int libssh2_channel_setenv(LIBSSH2_CHANNEL *channel, char *varname, const char *value); </p>
<h2>DESCRIPTION</h2>
<p> <i>channel</i> &#8211; Previously opened channel instance such as returned by <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<p> <i>varname</i> &#8211; Name of environment variable to set on the remote channel instance. </p>
<p> <i>varname_len</i> &#8211; Length of passed varname parameter. </p>
<p> <i>value</i> &#8211; Value to set varname to. </p>
<p> <i>value_len</i> &#8211; Length of value parameter. </p>
<p> Set an environment variable in the remote channel&#8217;s process space. Note that this does not make sense for all channel types and may be ignored by the server despite returning success.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se. </p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <i>LIBSSH2_ERROR_CHANNEL_REQUEST_DENIED</i> &#8211;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_channel_open_ex/">libssh2_channel_open_ex</a>(3)</code> </p>
<h2>Index</h2>
