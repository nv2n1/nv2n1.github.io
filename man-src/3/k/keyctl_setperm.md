---
title: "keyctl_setperm(3)"
name: "keyctl_setperm"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_setperm/"
description: "keyctl_setperm – Change the permissions mask on a key"
---

<h2 class="name">NAME</h2>
<p> keyctl_setperm &#8211; Change the permissions mask on a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_setperm(key_serial_t key, key_perm_t perm);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_setperm</code>() changes the permissions mask on a key. </p>
<p> A process that does not have the <code>SysAdmin</code> capability may not change the permissions mask on a key that doesn&#8217;t have the same UID as the caller. </p>
<p> The caller must have <code>setattr</code> permission on a key to be able change its permissions mask. </p>
<p> The permissions mask is a bitwise-OR of the following flags:</p>
<dl>
<dt><code>KEY_xxx_VIEW</code></p>
<dd> Grant permission to view the attributes of a key.</p>
<dt><code>KEY_xxx_READ</code></p>
<dd> Grant permission to read the payload of a key or to list a keyring.</p>
<dt><code>KEY_xxx_WRITE</code></p>
<dd> Grant permission to modify the payload of a key or to add or remove links to/from a keyring.</p>
<dt><code>KEY_xxx_SEARCH</code></p>
<dd> Grant permission to find a key or to search a keyring.</p>
<dt><code>KEY_xxx_LINK</code></p>
<dd> Grant permission to make links to a key.</p>
<dt><code>KEY_xxx_SETATTR</code></p>
<dd> Grant permission to change the ownership and permissions attributes of a key.</p>
<dt><code>KEY_xxx_ALL</code></p>
<dd> Grant all the above.</dl>
<p> The &#8216;<code>xxx</code>&#8216; in the above should be replaced by one of:</p>
<dl>
<dt><code>POS</code></p>
<dd> Grant the permission to a process that possesses the key (has it attached searchably to one of the process&#8217;s keyrings).</p>
<dt><code>USR</code></p>
<dd> Grant the permission to a process with the same UID as the key.</p>
<dt><code>GRP</code></p>
<dd> Grant the permission to a process with the same GID as the key, or with a match for the key&#8217;s GID amongst that process&#8217;s Groups list.</p>
<dt><code>OTH</code></p>
<dd> Grant the permission to any other process.</dl>
<p> Examples include: <code>KEY_POS_VIEW</code>, <code>KEY_USR_READ</code>, <code>KEY_GRP_SEARCH</code> and <code>KEY_OTH_ALL</code>. </p>
<p> User, group and other grants are exclusive: if a process qualifies in the &#8216;user&#8217; category, it will not qualify in the &#8216;groups&#8217; category; and if a process qualifies in either &#8216;user&#8217; or &#8216;groups&#8217; then it will not qualify in the &#8216;other&#8217; category. </p>
<p> Possessor grants are cumulative with the grants from the &#8216;user&#8217;, &#8216;groups&#8217; and &#8216;other&#8217; categories.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_setperm</code>() returns <code>0 .</code> On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The specified key does not exist.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The specified key has expired.</p>
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
