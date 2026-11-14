---
title: "keyctl_link(3)"
name: "keyctl_link"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_link/"
description: "keyctl_link – Link a key to a keyring keyctl_unlink – Unlink a key from a keyring"
---

<h2 class="name">NAME</h2>
<p> keyctl_link &#8211; Link a key to a keyring keyctl_unlink &#8211; Unlink a key from a keyring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_link(key_serial_t key, key_serial_t keyring);
long keyctl_unlink(key_serial_t key, key_serial_t keyring);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_link</code>() creates a link from <i>keyring</i> to <i>key</i>, displacing any link to another key of the same type and description in that keyring if one exists. </p>
<p> <code>keyctl_unlink</code>() removes the link from <i>keyring</i> to <i>key</i> if it exists. </p>
<p> The caller must have <code>write</code> permission on a keyring to be able create or remove links in it. </p>
<p> The caller must have <code>link</code> permission on a key to be able to create a link to it.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_link</code>() and <code>keyctl_unlink</code>() return <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key or the keyring specified are invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key or the keyring specified have expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key or the keyring specified have been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The keyring exists, but is not <code>writable</code> by the calling process.</dl>
<p> For <code>keyctl_link</code>() only:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to expand the keyring</p>
<dt><code>EDQUOT</code></p>
<dd> Expanding the keyring would exceed the keyring owner&#8217;s quota.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>linkable</code> by the calling process.</dl>
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
