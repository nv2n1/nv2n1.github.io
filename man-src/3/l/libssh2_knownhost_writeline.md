---
title: "libssh2_knownhost_writeline(3)"
name: "libssh2_knownhost_writeline"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_writeline/"
description: "libssh2_knownhost_writeline – convert a known host to a line for storage"
---

<h2>NAME</h2>
<p> libssh2_knownhost_writeline &#8211; convert a known host to a line for storage</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> libssh2_knownhost_writeline(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>*known,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>char&nbsp;<wbr>*buffer, size_t buflen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size_t&nbsp;<wbr>*outlen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int type);</p>
<h2>DESCRIPTION</h2>
<p> Converts a single known host to a single line of output for storage, using the &#8216;type&#8217; output format. </p>
<p> <i>known</i> identifies which particular known host </p>
<p> <i>buffer</i> points to an allocated buffer </p>
<p> <i>buflen</i> is the size of the <i>buffer</i>. See RETURN VALUE about the size. </p>
<p> <i>outlen</i> must be a pointer to a size_t variable that will get the output length of the stored data chunk. The number does not included the trailing zero! </p>
<p> <i>type</i> specifies what file type it is, and <i>LIBSSH2_KNOWNHOST_FILE_OPENSSH</i> is the only currently supported format.</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success. </p>
<p> If the provided buffer is deemed too small to fit the data libssh2 wants to store in it, LIBSSH2_ERROR_BUFFER_TOO_SMALL will be returned. The application is then advised to call the function again with a larger buffer. The <i>outlen</i> size will then hold the requested size.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_get/">libssh2_knownhost_get</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_readline/">libssh2_knownhost_readline</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_writefile/">libssh2_knownhost_writefile</a>(3)</code> </p>
<h2>Index</h2>
