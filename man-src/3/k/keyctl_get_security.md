---
title: "keyctl_get_security(3)"
name: "keyctl_get_security"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_get_security/"
description: "keyctl_get_security – Retrieve a key’s security context"
---

<h2 class="name">NAME</h2>
<p> keyctl_get_security &#8211; Retrieve a key&#8217;s security context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_get_security(key_serial_t key, char *buffer,
                         size_t buflen);
long keyctl_get_security_alloc(key_serial_t key, char **_buffer);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_get_security</code>() retrieves the security context of a key as a NUL-terminated string. This will be rendered in a form appropriate to the LSM in force &#8211; for instance, with SELinux, it may look like</p>
<dl>
<dt>
<dd> <code>unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023</code></dl>
<p> The caller must have <code>view</code> permission on a key to be able to get its security context. </p>
<p> <i>buffer</i> and <i>buflen</i> specify the buffer into which the string will be placed. If the buffer is too small, the full size of the string will be returned, and no copy will take place. </p>
<p> <code>keyctl_get_security_alloc</code>() is similar to <code>keyctl_get_security</code>() except that it allocates a buffer big enough to hold the string and copies the string into it. If successful, A pointer to the buffer is placed in <i>*_buffer</i>. The caller must free the buffer.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_get_security</code>() returns the amount of data placed into the buffer. If the buffer was too small, then the size of buffer required will be returned, but no data will be transferred. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error. </p>
<p> On success <code>keyctl_get_security_alloc</code>() returns the amount of data in the buffer, less the NUL terminator. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key specified has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key specified had been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>viewable</code> by the calling process.</dl>
<h2>LINKING</h2>
<p> This is a library function that can be found in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<h2>Index</h2>
