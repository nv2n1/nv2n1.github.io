---
title: "keyctl_set_timeout(3)"
name: "keyctl_set_timeout"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_set_timeout/"
description: "keyctl_set_timeout – Set the expiration timer on a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_set_timeout &#8211; Set the expiration timer on a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_set_timeout(key_serial_t key, unsigned timeout);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_set_timeout</code>() sets the expiration timer on a key to <i>timeout</i> seconds into the future. Setting <i>timeout</i> to <code>zero</code> cancels the expiration, assuming the key hasn&#8217;t already expired. </p>
<p> When the key expires, further attempts to access it will be met with error <code>EKEYEXPIRED</code>. </p>
<p> The caller must have <code>setattr</code> permission on a key to be able change its permissions mask.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_set_timeout</code>() returns <code>0 .</code> On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The specified key does not exist.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The specified key has already expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The specified key has been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The named key exists, but does not grant <code>setattr</code> permission to the calling process.</dl>
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
