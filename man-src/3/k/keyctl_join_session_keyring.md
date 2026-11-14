---
title: "keyctl_join_session_keyring(3)"
name: "keyctl_join_session_keyring"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_join_session_keyring/"
description: "keyctl_join_session_keyring – Join a different session keyring"
---

<h2 class="name">NAME</h2>
<p> keyctl_join_session_keyring &#8211; Join a different session keyring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
key_serial_t keyctl_join_session_keyring(const char *name);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_join_session_keyring</code>() changes the session keyring to which a process is subscribed. </p>
<p> If <i>name</i> is <code>NULL</code> then a new anonymous keyring will be created, and the process will be subscribed to that. </p>
<p> If <i>name</i> points to a string, then if a keyring of that name is available, the process will attempt to subscribe to that keyring, giving an error if that is not permitted; otherwise a new keyring of that name is created and attached as the session keyring. </p>
<p> To attach to an extant named keyring, the keyring must have <code>search</code> permission available to the calling process.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_join_session_keyring</code>() returns the serial number of the key it found or created. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to create a key.</p>
<dt><code>EDQUOT</code></p>
<dd> The key quota for this user would be exceeded by creating this key or linking it to the keyring.</p>
<dt><code>EACCES</code></p>
<dd> The named keyring exists, but is not <code>searchable</code> by the calling process.</dl>
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
