---
title: "keyctl_get_keyring_id(3)"
name: "keyctl_get_keyring_id"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_get_keyring_id/"
description: "keyctl_get_keyring_ID – Get the ID of a special keyring"
---

<p>keyctl_get_keyring_ID &#8211; Get the ID of a special keyring </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;keyutils.h&gt;</code>
<code>key_serial_t keyctl_get_keyring_ID(key_serial_t </code><i>key</i><code>,</code>
<code> int </code><i>create</i><code>);</code></pre>
<h2>Description</h2>
<p><code>keyctl_get_keyring_ID</code>() maps a special <i>key</i> or keyring ID to the serial number of the key actually representing that feature. The serial number will be returned if that key exists. </p>
<p> If the key or keyring does not yet exist, then if <i>create</i> is non-zero, the key or keyring will be created if it is appropriate to do so. </p>
<p> The following special key IDs may be specified as <i>key</i>:</p>
<dl COMPACT>
<dt><code>KEY_SPEC_THREAD_KEYRING</code></p>
<dd>This specifies the caller&#8217;s thread-specific keyring.</p>
<dt><code>KEY_SPEC_PROCESS_KEYRING</code></p>
<dd>This specifies the caller&#8217;s process-specific keyring.</p>
<dt><code>KEY_SPEC_SESSION_KEYRING</code></p>
<dd>This specifies the caller&#8217;s session-specific keyring.</p>
<dt><code>KEY_SPEC_USER_KEYRING</code></p>
<dd>This specifies the caller&#8217;s UID-specific keyring.</p>
<dt><code>KEY_SPEC_USER_SESSION_KEYRING</code></p>
<dd>This specifies the caller&#8217;s UID-session keyring.</p>
<dt><code>KEY_SPEC_REQKEY_AUTH_KEY</code></p>
<dd>This specifies the authorisation key created by <code>request_key</code>() and passed to the process it spawns to generate a key.</dl>
<p> If a valid keyring ID is passed in, then this will simply be returned if the key exists; an error will be issued if it doesn&#8217;t exist.</p>
<h2>Return Value</h2>
<p>On success <code>keyctl_get_keyring_ID</code>() returns the serial number of the key it found. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>ENOKEY</code></p>
<dd>No matching key was found.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory to create a key.</p>
<dt><code>EDQUOT</code></p>
<dd>The key quota for this user would be exceeded by creating this key or linking it to the keyring.</dl>
<h2>Linking</h2>
<p>This is a library function that can be found in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)</p>
