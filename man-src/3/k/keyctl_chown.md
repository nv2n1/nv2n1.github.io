---
title: "keyctl_chown(3)"
name: "keyctl_chown"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_chown/"
description: "keyctl_chown – Change the ownership of a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_chown &#8211; Change the ownership of a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_chown(key_serial_t key, uid_t uid, gid_t gid);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_chown</code>() changes the user and group ownership details of a key. </p>
<p> A setting of <code>-1</code> on either <i>uid</i> or <i>gid</i> will cause that setting to be ignored. </p>
<p> A process that does not have the <code>SysAdmin</code> capability may not change a key&#8217;s UID or set the key&#8217;s GID to a value that does not match the process&#8217;s GID or one of its group list. </p>
<p> The caller must have <code>setattr</code> permission on a key to be able change its ownership.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_chown</code>() returns <code>0 .</code> On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The specified key does not exist.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The specified key has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The specified key has been revoked.</p>
<dt><code>EDQUOT</code></p>
<dd> Changing the UID to the one specified would run that UID out of quota.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but does not grant <code>setattr</code> permission to the calling process.</dl>
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
