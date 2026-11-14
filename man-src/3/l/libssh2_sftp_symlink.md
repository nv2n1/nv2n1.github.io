---
title: "libssh2_sftp_symlink(3)"
name: "libssh2_sftp_symlink"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_sftp_symlink/"
description: "libssh2_sftp_symlink – convenience macro for libssh2_sftp_symlink_ex(3)"
---

<h2>NAME</h2>
<p> libssh2_sftp_symlink &#8211; convenience macro for <i><a href="/docs/linux/man/3-libssh2_sftp_symlink_ex/">libssh2_sftp_symlink_ex</a>(3)</i></p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
#define libssh2_sftp_symlink(sftp, orig, linkpath)                    \
    libssh2_sftp_symlink_ex((sftp), (orig), strlen(orig), (linkpath), \
                            strlen(linkpath), LIBSSH2_SFTP_SYMLINK)
</code></pre>
<h2>DESCRIPTION</h2>
<p> This is a macro defined in a public libssh2 header file that is using the underlying function <i><a href="/docs/linux/man/3-libssh2_sftp_symlink_ex/">libssh2_sftp_symlink_ex</a>(3)</i>.</p>
<h2>RETURN VALUE</h2>
<p> See <i><a href="/docs/linux/man/3-libssh2_sftp_symlink_ex/">libssh2_sftp_symlink_ex</a>(3)</i></p>
<h2>ERRORS</h2>
<p> See <i><a href="/docs/linux/man/3-libssh2_sftp_symlink_ex/">libssh2_sftp_symlink_ex</a>(3)</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_sftp_symlink_ex/">libssh2_sftp_symlink_ex</a>(3)</code> </p>
<h2>Index</h2>
