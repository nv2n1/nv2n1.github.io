---
title: "keyctl_update(3)"
name: "keyctl_update"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_update/"
description: "keyctl_update – Update a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_update &#8211; Update a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_update(key_serial_t key, const void *payload,
                   size_t plen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_update</code>() updates the payload of a key if the key type permits it. </p>
<p> The caller must have <code>write</code> permission on a key to be able update it. </p>
<p> <i>payload</i> and <i>plen</i> specify the data for the new payload. <i>payload</i> may be NULL and <i>plen</i> may be zero if the key type permits that. The key type may reject the data if it&#8217;s in the wrong format or in some other way invalid.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_update</code>() returns <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key specified has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key specified had been revoked.</p>
<dt><code>EINVAL</code></p>
<dd> The payload data was invalid.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to store the new payload.</p>
<dt><code>EDQUOT</code></p>
<dd> The key quota for this user would be exceeded by increasing the size of the key to accommodate the new payload.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>writable</code> by the calling process.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The key type does not support the update operation on its keys.</dl>
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
