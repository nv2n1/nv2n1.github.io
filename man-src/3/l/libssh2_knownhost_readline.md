---
title: "libssh2_knownhost_readline(3)"
name: "libssh2_knownhost_readline"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_readline/"
description: "libssh2_knownhost_readline – read a known host line"
---

<h2>NAME</h2>
<p> libssh2_knownhost_readline &#8211; read a known host line</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_readline(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*line, size_t len, int type):</p>
<h2>DESCRIPTION</h2>
<p> Tell libssh2 to read a buffer as it if is a line from a known hosts file. </p>
<p> <i>line</i> points to the start of the line </p>
<p> <i>len</i> is the length of the line in bytes </p>
<p> <i>type</i> specifies what file type it is, and <i>LIBSSH2_KNOWNHOST_FILE_OPENSSH</i> is the only currently supported format. This file is normally found named ~/.ssh/known_hosts</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_get/">libssh2_knownhost_get</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_writeline/">libssh2_knownhost_writeline</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_readfile/">libssh2_knownhost_readfile</a>(3)</code> </p>
<h2>Index</h2>
