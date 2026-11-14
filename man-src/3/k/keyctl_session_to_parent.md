---
title: "keyctl_session_to_parent(3)"
name: "keyctl_session_to_parent"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_session_to_parent/"
description: "keyctl_session_to_parent – Set the parent process’s session keyring"
---

<h2 class="name">NAME</h2>
<p> keyctl_session_to_parent &#8211; Set the parent process&#8217;s session keyring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_session_to_parent();
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_session_to_parent</code>() changes the session keyring to which the calling process&#8217;s parent subscribes to be the that of the calling process. </p>
<p> The keyring must have <code>link</code> permission available to the calling process, the parent process must have the same UIDs/GIDs as the calling process, and the LSM must not reject the replacement. Furthermore, this may not be used to affect init or a kernel thread. </p>
<p> Note that the replacement will not take immediate effect upon the parent process, but will rather be deferred to the next time it returns to userspace from kernel space.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_session_to_parent</code>() returns 0. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to create a key.</p>
<dt><code>EPERM</code></p>
<dd> The credentials of the parent don&#8217;t match those of the caller.</p>
<dt><code>EACCES</code></p>
<dd> The named keyring exists, but is not <code>linkable</code> by the calling process.</dl>
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
