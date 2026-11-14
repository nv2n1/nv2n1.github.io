---
title: "libssh2_session_callback_set(3)"
name: "libssh2_session_callback_set"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_session_callback_set/"
description: "libssh2_session_callback_set – set a callback function"
---

<h2>NAME</h2>
<p> libssh2_session_callback_set &#8211; set a callback function</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
void *libssh2_session_callback_set(LIBSSH2_SESSION *session,
                                   int cbtype, void *callback);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Sets a custom callback handler for a previously initialized session object. Callbacks are triggered by the receipt of special packets at the Transport layer. To disable a callback, set it to NULL. </p>
<p> <i>session</i> &#8211; Session instance as returned by <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<p> <i>cbtype</i> &#8211; Callback type. One of the types listed in Callback Types. </p>
<p> <i>callback</i> &#8211; Pointer to custom callback function. The prototype for this function must match the associated callback declaration macro.</p>
<h2>CALLBACK TYPES</h2>
<dl>
<dt>LIBSSH2_CALLBACK_IGNORE</p>
<dd> Called when a SSH_MSG_IGNORE message is received</p>
<dt>LIBSSH2_CALLBACK_DEBUG</p>
<dd> Called when a SSH_MSG_DEBUG message is received</p>
<dt>LIBSSH2_CALLBACK_DISCONNECT</p>
<dd> Called when a SSH_MSG_DISCONNECT message is received</p>
<dt>LIBSSH2_CALLBACK_MACERROR</p>
<dd> Called when a mismatched MAC has been detected in the transport layer. If the function returns 0, the packet will be accepted nonetheless.</p>
<dt>LIBSSH2_CALLBACK_X11</p>
<dd> Called when an X11 connection has been accepted</p>
<dt>LIBSSH2_CALLBACK_SEND</p>
<dd> Called when libssh2 wants to send some data on the connection. Can be set to a custom function to handle I/O your own way.</p>
<dt>LIBSSH2_CALLBACK_RECV</p>
<dd> Called when libssh2 wants to receive some data from the connection. Can be set to a custom function to handle I/O your own way.</dl>
<h2>RETURN VALUE</h2>
<p> Pointer to previous callback handler. Returns NULL if no prior callback handler was set or the callback type was unknown.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
