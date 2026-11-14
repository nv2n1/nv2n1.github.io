---
title: "libssh2_userauth_keyboard_interactive(3)"
name: "libssh2_userauth_keyboard_interactive"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_userauth_keyboard_interactive/"
description: "libssh2_userauth_keyboard_interactive – convenience macro for libssh2_userauth_keyboard_interactive_ex(3) calls"
---

<h2>NAME</h2>
<p> libssh2_userauth_keyboard_interactive &#8211; convenience macro for <i><a href="/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/">libssh2_userauth_keyboard_interactive_ex</a>(3)</i> calls</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<pre><code>
int libssh2_userauth_keyboard_interactive(LIBSSH2_SESSION *session,
                                          const char *username,
                                          LIBSSH2_USERAUTH_KBDINT_RESPONSE_FUNC((*response_callback)));
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a macro defined in a public libssh2 header file that is using the underlying function <i><a href="/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/">libssh2_userauth_keyboard_interactive_ex</a>(3)</i>.</p>
<h2>RETURN VALUE</h2>
<p> See <i><a href="/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/">libssh2_userauth_keyboard_interactive_ex</a>(3)</i></p>
<h2>ERRORS</h2>
<p> See <i><a href="/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/">libssh2_userauth_keyboard_interactive_ex</a>(3)</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_userauth_keyboard_interactive_ex/">libssh2_userauth_keyboard_interactive_ex</a>(3)</code> </p>
<h2>Index</h2>
