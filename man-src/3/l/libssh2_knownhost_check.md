---
title: "libssh2_knownhost_check(3)"
name: "libssh2_knownhost_check"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_check/"
description: "libssh2_knownhost_check – check a host+key against the list of known hosts"
---

<h2>NAME</h2>
<p> libssh2_knownhost_check &#8211; check a host+key against the list of known hosts</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_check(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*host,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*key, size_t keylen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int typemask,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>**knownhost);</p>
<h2>DESCRIPTION</h2>
<p> Checks a host and its associated key against the collection of known hosts, and returns info back about the (partially) matched entry. </p>
<p> <i>host</i> is a pointer the host name in plain text. The host name can be the IP numerical address of the host or the full name. </p>
<p> <i>key</i> is a pointer to the key for the given host. </p>
<p> <i>keylen</i> is the total size in bytes of the key pointed to by the <i>key</i> argument </p>
<p> <i>typemask</i> is a bitmask that specifies format and info about the data passed to this function. Specificly, it details what format the host name is, what format the key is and what key type it is. </p>
<p> The host name is given as one of the following types: LIBSSH2_KNOWNHOST_TYPE_PLAIN or LIBSSH2_KNOWNHOST_TYPE_CUSTOM. </p>
<p> The key is encoded using one of the following encodings: LIBSSH2_KNOWNHOST_KEYENC_RAW or LIBSSH2_KNOWNHOST_KEYENC_BASE64. </p>
<p> <i>knownhost</i> if set to non-NULL, it must be a pointer to a &#8216;struct libssh2_knownhost&#8217; pointer that gets filled in to point to info about a known host that matches or partially matches.</p>
<h2>RETURN VALUE</h2>
<p> <i><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</i> returns info about how well the provided host + key pair matched one of the entries in the list of known hosts. </p>
<p> LIBSSH2_KNOWNHOST_CHECK_FAILURE &#8211; something prevented the check to be made </p>
<p> LIBSSH2_KNOWNHOST_CHECK_NOTFOUND &#8211; no host match was found </p>
<p> LIBSSH2_KNOWNHOST_CHECK_MATCH &#8211; hosts and keys match. </p>
<p> LIBSSH2_KNOWNHOST_CHECK_MISMATCH &#8211; host was found, but the keys didn&#8217;t match!</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2</p>
<h2>EXAMPLE</h2>
<p> See the ssh2_exec.c example as provided in the tarball.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_init/">libssh2_knownhost_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</code> </p>
<h2>Index</h2>
