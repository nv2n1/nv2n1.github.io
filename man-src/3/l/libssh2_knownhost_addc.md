---
title: "libssh2_knownhost_addc(3)"
name: "libssh2_knownhost_addc"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libssh2_knownhost_addc/"
description: "libssh2_knownhost_add – add a known host"
---

<h2>NAME</h2>
<p> libssh2_knownhost_add &#8211; add a known host</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libssh2.h&gt; </p>
<p> int libssh2_knownhost_addc(LIBSSH2_KNOWNHOSTS *hosts,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>char&nbsp;<wbr>*host, char&nbsp;<wbr>*salt,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>char&nbsp;<wbr>*key, size_t keylen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>const char&nbsp;<wbr>*comment, size_t commentlen,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int typemask,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct libssh2_knownhost&nbsp;<wbr>**store);</p>
<h2>DESCRIPTION</h2>
<p> Adds a known host to the collection of known hosts identified by the &#8216;hosts&#8217; handle. </p>
<p> <i>host</i> is a pointer the host name in plain text or hashed. If hashed, it must be provided base64 encoded. The host name can be the IP numerical address of the host or the full name. </p>
<p> If you want to add a key for a specific port number for the given host, you must provide the host name like &#8216;[host]:port&#8217; with the actual characters &#8216;[&#8216; and &#8216;]&#8217; enclosing the host name and a colon separating the host part from the port number. For example: &quot;[host.example.com]:222&quot;. </p>
<p> <i>salt</i> is a pointer to the salt used for the host hashing, if the host is provided hashed. If the host is provided in plain text, salt has no meaning. The salt has to be provided base64 encoded with a trailing zero byte. </p>
<p> <i>key</i> is a pointer to the key for the given host. </p>
<p> <i>keylen</i> is the total size in bytes of the key pointed to by the <i>key</i> argument </p>
<p> <i>comment</i> is a pointer to a comment for the key. </p>
<p> <i>commentlen</i> is the total size in bytes of the comment pointed to by the <i>comment</i> argument </p>
<p> <i>typemask</i> is a bitmask that specifies format and info about the data passed to this function. Specificly, it details what format the host name is, what format the key is and what key type it is. </p>
<p> The host name is given as one of the following types: LIBSSH2_KNOWNHOST_TYPE_PLAIN, LIBSSH2_KNOWNHOST_TYPE_SHA1 or LIBSSH2_KNOWNHOST_TYPE_CUSTOM. </p>
<p> The key is encoded using one of the following encodings: LIBSSH2_KNOWNHOST_KEYENC_RAW or LIBSSH2_KNOWNHOST_KEYENC_BASE64. </p>
<p> The key is using one of these algorithms: LIBSSH2_KNOWNHOST_KEY_RSA1, LIBSSH2_KNOWNHOST_KEY_SSHRSA or LIBSSH2_KNOWNHOST_KEY_SSHDSS. </p>
<p> <i>store</i> should point to a pointer that gets filled in to point to the known host data after the addition. NULL can be passed if you don&#8217;t care about this pointer.</p>
<h2>RETURN VALUE</h2>
<p> Returns a regular libssh2 error code, where negative values are error codes and 0 indicates success.</p>
<h2>AVAILABILITY</h2>
<p> Added in libssh2 1.2.5</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libssh2_knownhost_init/">libssh2_knownhost_init</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_free/">libssh2_knownhost_free</a>(3)</code> <code><a href="/docs/linux/man/3-libssh2_knownhost_check/">libssh2_knownhost_check</a>(3)</code> </p>
<h2>Index</h2>
