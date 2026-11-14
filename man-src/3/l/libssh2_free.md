---
title: "libssh2_free(3)"
name: "libssh2_free"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_free/"
description: "libssh2_free – deallocate libssh2 memory"
---

<h2>NAME</h2>
<p> libssh2_free &#8211; deallocate libssh2 memory</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> void libssh2_free(LIBSSH2_SESSION *session, void *ptr);</p>
<h2>DESCRIPTION</h2>
<p> Deallocate memory allocated by earlier call to libssh2 functions. It uses the memory allocation callbacks provided by the application, if any. Otherwise, this will just call free(). </p>
<p> This function is mostly useful under Windows when libssh2 is linked to one run-time library and the application to another.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.8</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_session_init_ex/">libssh2_session_init_ex</a>(3)</code> </p>
<h2>Index</h2>
