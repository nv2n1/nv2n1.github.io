---
title: "keyctl_describe(3)"
name: "keyctl_describe"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_describe/"
description: "keyctl_describe – Describe a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_describe &#8211; Describe a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_describe(key_serial_t key, char *buffer,
                     size_tbuflen);
long keyctl_describe_alloc(key_serial_t key, char **_buffer);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_describe</code>() describes the attributes of a key as a NUL-terminated string. </p>
<p> The caller must have <code>view</code> permission on a key to be able to get a description of it. </p>
<p> <i>buffer</i> and <i>buflen</i> specify the buffer into which the key description will be placed. If the buffer is too small, the full size of the description will be returned, and no copy will take place. </p>
<p> <code>keyctl_describe_alloc</code>() is similar to <code>keyctl_describe</code>() except that it allocates a buffer big enough to hold the description and places the description in it. If successful, A pointer to the buffer is placed in <i>*_buffer</i>. The caller must free the buffer. </p>
<p> The description will be a string of format:</p>
<dl>
<dt>
<dd> <code>&#8220;%s;%d;%d;%08x;%s&#8221;</code></dl>
<p> where the arguments are: key type name, key UID, key GID, key permissions mask and key description. </p>
<p> <code>NOTE!</code> The key description will not contain any semicolons, so that should be separated out by working backwards from the end of the string. This permits extra information to be inserted before it by later versions of the kernel simply by inserting more semicolon-terminated substrings.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_describe</code>() returns the amount of data placed into the buffer. If the buffer was too small, then the size of buffer required will be returned, but no data will be transferred. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error. </p>
<p> On success <code>keyctl_describe_alloc</code>() returns the amount of data in the buffer, less the NUL terminator. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
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
