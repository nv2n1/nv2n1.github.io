---
title: "libssh2_knownhost_add(3)"
name: "libssh2_knownhost_add"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_add/"
description: "libssh2_knownhost_add – add a known host"
---

<h2>NAME</h2>
<p> libssh2_knownhost_add &#8211; add a known host</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libssh2.h&gt;
int libssh2_knownhost_add(LIBSSH2_KNOWNHOSTS *hosts,
                          char *host, char *salt,
                          char *key, size_t keylen,
                          int typemask,
                          struct libssh2_knownhost **store);
</code></pre>
<h2>DESCRIPTION</h2>
<p> We discourage use of this function as of libssh2 1.2.5. Instead we strongly urge users to use <i><a href="/docs/linux/man/3-libssh2_knownhost_addc/">libssh2_knownhost_addc</a>(3)</i> instead, which as a more complete API. <i><a href="/docs/linux/man/3-libssh2_knownhost_add/">libssh2_knownhost_add</a>(3)</i> is subject for removal in a future release. </p>
<p> Adds a known host to the collection of known hosts identified by the &#8216;hosts&#8217; handle. </p>
<p> <i>host</i> is a pointer the host name in plain text or hashed. If hashed, it must be provided base64 encoded. The host name can be the IP numerical address of the host or the full name. </p>
<p> <i>saltP is a pointer to the salt used for the host hashing, if the host is provided hashed. If the host is provided in plain text, salt has no meaning. The salt has to be provided base64 encoded with a trailing zero byte. </p>
<p> key</i> is a pointer to the key for the given host. </p>
<p> <i>keylen</i> is the total size in bytes of the key pointed to by the <i>key</i> argument </p>
<p> <i>typemask</i> is a bitmask that specifies format and info about the data passed to this function. Specificly, it details what format the host name is, what format the key is and what key type it is. </p>
<p> The host name is given as one of the following types: LIBSSH2_KNOWNHOST_TYPE_PLAIN, LIBSSH2_KNOWNHOST_TYPE_SHA1 or LIBSSH2_KNOWNHOST_TYPE_CUSTOM. </p>
<p> The key is encoded using one of the following encodings: LIBSSH2_KNOWNHOST_KEYENC_RAW or LIBSSH2_KNOWNHOST_KEYENC_BASE64. </p>
<p> The key is using one of these algorithms: LIBSSH2_KNOWNHOST_KEY_RSA1, LIBSSH2_KNOWNHOST_KEY_SSHRSA or LIBSSH2_KNOWNHOST_KEY_SSHDSS. </p>
<p> <i>store</i> should point to a pointer that gets filled in to point to the known host data after the addition. NULL can be passed if you don&#8217;t care about this pointer.</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2, deprecated since libssh2 1.2.5. Use <i><a href="/docs/linux/man/3-libssh2_knownhost_addc/">libssh2_knownhost_addc</a>(3)</i> instead!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_init/">libssh2_knownhost_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_addc/">libssh2_knownhost_addc</a>(3)</code> </p>
<h2>Index</h2>
