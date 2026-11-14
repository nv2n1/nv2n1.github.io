---
title: "keyctl_invalidate(3)"
name: "keyctl_invalidate"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_invalidate/"
description: "keyctl_invalidate – Invalidate a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_invalidate &#8211; Invalidate a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_invalidate(key_serial_t key);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_invalidate</code>() invalidates a <i>key</i>. The key is scheduled for immediate removal from all the keyrings that point to it, after which it will be deleted. The key will be ignored by all searches once this function is called even if it is not yet fully dealt with. </p>
<p> The caller must have <code>search</code> permission on a key to be able to invalidate it.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_invalidate</code>() returns <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key specified has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key specified had been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>searchable</code> by the calling process.</dl>
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
