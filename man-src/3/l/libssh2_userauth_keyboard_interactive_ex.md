---
title: "libssh2_userauth_keyboard_interactive_ex(3)"
name: "libssh2_userauth_keyboard_interactive_ex"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/"
description: "libssh2_userauth_keyboard_interactive_ex – authenticate a session using keyboard-interactive authentication"
---

<h2>NAME</h2>
<p> libssh2_userauth_keyboard_interactive_ex &#8211; authenticate a session using keyboard-interactive authentication</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
int libssh2_userauth_keyboard_interactive_ex(LIBSSH2_SESSION *session,
                                             const char *username,
                                             unsigned int username_len,
                                             LIBSSH2_USERAUTH_KBDINT_RESPONSE_FUNC(*response_callback));
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>session</i> &#8211; Session instance as returned by <i><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</i>. </p>
<p> <i>username</i> &#8211; Name of user to attempt keyboard-interactive authentication for. </p>
<p> <i>username_len</i> &#8211; Length of username parameter. </p>
<p> <i>response_callback</i> &#8211; As authentication proceeds, the host issues several (1 or more) challenges and requires responses. This callback will be called at this moment. The callback is responsible to obtain responses for the challenges, fill the provided data structure and then return control. Responses will be sent to the host. String values will be <a href="/docs/linux/man/3-free/">free</a>(3)ed by the library. The callback prototype must match this: </p>
<pre><code>
void response(const char *name,
              int name_len, const char *instruction,
              int instruction_len,
              int num_prompts,
              const LIBSSH2_USERAUTH_KBDINT_PROMPT *prompts,
              LIBSSH2_USERAUTH_KBDINT_RESPONSE *responses,
              void **abstract);
</code></pre>
<p> Attempts keyboard-interactive (challenge/response) authentication. </p>
<p> Note that many SSH servers will always issue a single &quot;password&quot; challenge, requesting actual password as response, but it is not required by the protocol, and various authentication schemes, such as smartcard authentication may use keyboard-interactive authentication type too.</p>
<h2>RETURN VALUE</h2>
<p> Return 0 on success or negative on failure. It returns LIBSSH2_ERROR_EAGAIN when it would otherwise block. While LIBSSH2_ERROR_EAGAIN is a negative number, it isn&#8217;t really a failure per se.</p>
<h2>ERRORS</h2>
<p> <i>LIBSSH2_ERROR_ALLOC</i> &#8211; An internal memory allocation call failed. </p>
<p> <i>LIBSSH2_ERROR_SOCKET_SEND</i> &#8211; Unable to send data on socket. </p>
<p> <tt>IBSSH2_ERROR_AUTHENTICATION_FAILED</tt> &#8211; failed, invalid username/password or public/private key.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
