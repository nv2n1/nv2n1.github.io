---
title: "libssh2_knownhost_del(3)"
name: "libssh2_knownhost_del"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_del/"
description: "libssh2_knownhost_del – delete a known host entry"
---

<h2>NAME</h2>
<p> libssh2_knownhost_del &#8211; delete a known host entry</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_del(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>*entry);</p>
<h2>DESCRIPTION</h2>
<p> Delete a known host entry from the collection of known hosts. </p>
<p> <i>entry</i> is a pointer to a struct that you can extract with <i><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</i> or <i><a href="/docs/linux/man/3-libssh2_knownhost_get/">libssh2_knownhost_get</a>(3)</i>.</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_init/">libssh2_knownhost_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> </p>
<h2>Index</h2>
