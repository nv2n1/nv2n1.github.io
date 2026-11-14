---
title: "keyctl_get_persistent(3)"
name: "keyctl_get_persistent"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_get_persistent/"
description: "keyctl_get_persistent – Get the persistent keyring for a user"
---

<h2 class="name">NAME</h2>
<p> keyctl_get_persistent &#8211; Get the persistent keyring for a user </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_get_persistent(uid_t uid, key_serial_t keyring);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_get_persistent</code>() gets the persistent keyring for the specified user ID. Unlike the session and user keyrings, this keyring will persist once all login sessions have been deleted and can thus be used to carry authentication tokens for processes that run without user interaction, such as programs started by cron. </p>
<p> The persistent keyring will be created by the kernel if it does not yet exist. Each time this function is called, the persistent keyring will have its expiration timeout reset to the value in:</p>
<dl>
<dt>
<dd> /proc/sys/kernel/keys/persistent_keyring_expiry</dl>
<p> (by default three days). Should the timeout be reached, the persistent keyring will be removed and everything it pins can then be garbage collected. </p>
<p> If <i>uid</i> is <code>-1</code> then the calling process&#8217;s real user ID will be used. If <i>uid</i> is not <code>-1</code> then error <i>EPERM</i> will be given if the user ID requested does not match either the caller&#8217;s real or effective user IDs or if the calling process does not have <code>SetUid</code> capability. </p>
<p> If successful, a link to the persistent keyring will be added into <i>keyring</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_get_persistent</code>() returns the serial number of the persistent keyring. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> Not permitted to access the persistent keyring for the requested <i>uid</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to create the persistent keyring or to extend <i>keyring</i>.</p>
<dt><code>ENOKEY</code></p>
<dd> <i>keyring</i> does not exist.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> <i>keyring</i> has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> <i>keyring</i> has been revoked.</p>
<dt><code>EDQUOT</code></p>
<dd> The user does not have sufficient quota to extend <i>keyring</i>.</p>
<dt><code>EACCES</code></p>
<dd> <i>keyring</i> exists, but does not grant <code>write</code> permission to the calling process. </p>
</dl>
<h2>LINKING</h2>
<p> This is a library function that can be found in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7),<br />
 <code><a href="/docs/linux/man/7-keyutils/">keyutils</a></code>(7),<br />
 <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7) </p>
<h2>Index</h2>
