---
title: "libssh2_knownhost_readfile(3)"
name: "libssh2_knownhost_readfile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_readfile/"
description: "libssh2_knownhost_readfile – parse a file of known hosts"
---

<h2>NAME</h2>
<p> libssh2_knownhost_readfile &#8211; parse a file of known hosts</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_readfile(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*filename, int type);</p>
<h2>DESCRIPTION</h2>
<p> Reads a collection of known hosts from a specified file and adds them to the collection of known hosts. </p>
<p> <i>filename</i> specifies which file to read </p>
<p> <i>type</i> specifies what file type it is, and <i>LIBSSH2_KNOWNHOST_FILE_OPENSSH</i> is the only currently supported format. This file is normally found named ~/.ssh/known_hosts</p>
<h2>RETURN VALUE</h2>
<p> Returns a negative value, a regular libssh2 error code for errors, or a positive number as number of parsed known hosts in the file.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_init/">libssh2_knownhost_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> </p>
<h2>Index</h2>
