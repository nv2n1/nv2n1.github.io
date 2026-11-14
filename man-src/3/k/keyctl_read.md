---
title: "keyctl_read(3)"
name: "keyctl_read"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_read/"
description: "keyctl_read – Read a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_read &#8211; Read a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_read(key_serial_t key, char *buffer,
                 size_tbuflen);
long keyctl_read_alloc(key_serial_t key, void **_buffer);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_read</code>() reads the payload of a key if the key type supports it. </p>
<p> The caller must have <code>read</code> permission on a key to be able to read it. </p>
<p> <i>buffer</i> and <i>buflen</i> specify the buffer into which the payload data will be placed. If the buffer is too small, the full size of the payload will be returned, and no copy will take place. </p>
<p> <code>keyctl_read_alloc</code>() is similar to <code>keyctl_read</code>() except that it allocates a buffer big enough to hold the payload data and places the data in it. If successful, A pointer to the buffer is placed in <i>*_buffer</i>. The caller must free the buffer.</p>
<h2>READING KEYRINGS</h2>
<p> This call can be used to list the contents of a keyring. The data is presented to the user as an array of <code>key_serial_t</code> values, each of which corresponds to a key to which the keyring holds a link. </p>
<p> The size of the keyring will be sizeof(key_serial_t) multiplied by the number of keys. The size of key_serial_t is invariant across different word sizes, though the byte-ordering is as appropriate for the kernel.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_read</code>() returns the amount of data placed into the buffer. If the buffer was too small, then the size of buffer required will be returned, but no data will be transferred. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error. </p>
<p> On success <code>keyctl_read_alloc</code>() returns the amount of data in the buffer. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key specified has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key specified had been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>readable</code> by the calling process.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The key type does not support reading of the payload data.</dl>
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
