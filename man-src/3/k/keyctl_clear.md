---
title: "keyctl_clear(3)"
name: "keyctl_clear"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_clear/"
description: "keyctl_clear – Clear a keyring"
---

<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_clear(key_serial_t keyring);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_clear</code>() clears the contents of a <i>keyring</i>. </p>
<p> The caller must have <code>write</code> permission on a keyring to be able clear it.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_clear</code>() returns <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></dt>
<dd> The keyring specified is invalid.</dd>
<dt><code>EKEYEXPIRED</code></dt>
<dd> The keyring specified has expired.</dd>
<dt><code>EKEYREVOKED</code></dt>
<dd> The keyring specified had been revoked.</dd>
<dt><code>EACCES</code></dt>
<dd> The keyring exists, but is not <code>writable</code> by the calling process.</dd></dl>
<h2>LINKING</h2>
<p> This is a library function that can be found in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
