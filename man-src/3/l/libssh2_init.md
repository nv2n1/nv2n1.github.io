---
title: "libssh2_init(3)"
name: "libssh2_init"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_init/"
description: "libssh2_init – global library initialization"
---

<h2>NAME</h2>
<p> libssh2_init &#8211; global library initialization</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> #define LIBSSH2_INIT_NO_CRYPTO 0x0001 </p>
<p> int libssh2_init(int flags);</p>
<h2>DESCRIPTION</h2>
<p> Initialize the libssh2 functions. This typically initialize the crypto library. It uses a global state, and is not thread safe &#8212; you must make sure this function is not called concurrently.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if succeeded, or a negative value for error.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.5</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_exit/">libssh2_exit</a>(3)</code> </p>
<h2>Index</h2>
