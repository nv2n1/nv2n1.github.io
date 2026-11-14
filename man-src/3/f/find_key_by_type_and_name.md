---
title: "find_key_by_type_and_name(3)"
name: "find_key_by_type_and_name"
section: "3"
letter: "f"
url: "/docs/linux/man/3-find_key_by_type_and_name/"
description: "find_key_by_type_and_name – Find a key by type and name"
---

<h2 class="name">NAME</h2>
<p> find_key_by_type_and_name &#8211; Find a key by type and name </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
key_serial_t find_key_by_type_and_name(const char *type,
                                       const char *description, key_serial_t destringid);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>find_key_by_type_and_name</code>() searches for a key with the given <i>type</i> and exact <i>description</i>, firstly in the thread, process and session keyrings to which a process is subscribed and secondly in /proc/keys. </p>
<p> If a key is found, and <i>destringid</i> is not 0 and specifies a keyring, then the found key will be linked into it.</p>
<h2>RETURN VALUE</h2>
<p> The function returns the ID of the key if a key was found or -1 otherwise.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> No key was found or the keyring specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The key or keyring have expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key or keyring have been revoked.</p>
<dt><code>EACCES</code></p>
<dd> The key is not accessible or keyring exists, but is not <code>writable</code> by the calling process.</dl>
<h2>LINKING</h2>
<p> When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/3-request_key/">request_key</a></code>(3) </p>
<h2>Index</h2>
