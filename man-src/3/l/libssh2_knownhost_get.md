---
title: "libssh2_knownhost_get(3)"
name: "libssh2_knownhost_get"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_get/"
description: "libssh2_knownhost_get – get a known host off the collection of known hosts"
---

<h2>NAME</h2>
<p> libssh2_knownhost_get &#8211; get a known host off the collection of known hosts</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_get(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>**store,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>*prev):</p>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/3-libssh2_knownhost_get/">libssh2_knownhost_get</a>(3)</i> allows an application to iterate over all known hosts in the collection. </p>
<p> <i>store</i> should point to a pointer that gets filled in to point to the known host data. </p>
<p> <i>prev</i> is a pointer to a previous &#8216;struct libssh2_knownhost&#8217; as returned by a previous invoke of this function, or NULL to get the first entry in the internal collection.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 if everything is fine and information about a host was stored in the <i>store</i> struct. </p>
<p> Returns 1 if it reached the end of hosts. </p>
<p> Returns negative values for error</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_readfile/">libssh2_knownhost_readfile</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_writefile/">libssh2_knownhost_writefile</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> </p>
<h2>Index</h2>
