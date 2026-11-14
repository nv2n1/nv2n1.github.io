---
title: "libssh2_knownhost_writefile(3)"
name: "libssh2_knownhost_writefile"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_writefile/"
description: "libssh2_knownhost_writefile – write a collection of known hosts to a file"
---

<h2>NAME</h2>
<p> libssh2_knownhost_writefile &#8211; write a collection of known hosts to a file</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_writefile(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*filename, int type);</p>
<h2>DESCRIPTION</h2>
<p> Writes all the known hosts to the specified file using the specified file format. </p>
<p> <i>filename</i> specifies what filename to create </p>
<p> <i>type</i> specifies what file type it is, and <i>LIBSSH2_KNOWNHOST_FILE_OPENSSH</i> is the only currently supported format.</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_readfile/">libssh2_knownhost_readfile</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> </p>
<h2>Index</h2>
