---
title: "keyctl_set_reqkey_keyring(3)"
name: "keyctl_set_reqkey_keyring"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_set_reqkey_keyring/"
description: "keyctl_set_reqkey_keyring – Set the implicit destination keyring"
---

<h2 class="name">NAME</h2>
<p> keyctl_set_reqkey_keyring &#8211; Set the implicit destination keyring </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_set_reqkey_keyring(int reqkey_defl);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_set_reqkey_keyring</code>() sets the default destination for implicit key requests for the current thread and returns the old setting. </p>
<p> After this operation has been issued, keys acquired by implicit key requests, such as might be performed by open() on an AFS or NFS filesystem, will be linked by default to the specified keyring by this function. </p>
<p> The valid values of <i>reqkey_defl</i> are:</p>
<dl>
<dt><code>KEY_REQKEY_DEFL_NO_CHANGE</code></p>
<dd> This makes no change to the current setting.</p>
<dt><code>KEY_REQKEY_DEFL_THREAD_KEYRING</code></p>
<dd> This makes the thread-specific keyring the default destination.</p>
<dt><code>KEY_REQKEY_DEFL_PROCESS_KEYRING</code></p>
<dd> This makes the process-specific keyring the default destination.</p>
<dt><code>KEY_REQKEY_DEFL_SESSION_KEYRING</code></p>
<dd> This makes the session keyring the default destination.</p>
<dt><code>KEY_REQKEY_DEFL_USER_KEYRING</code></p>
<dd> This makes the UID-specific keyring the default destination.</p>
<dt><code>KEY_REQKEY_DEFL_USER_SESSION_KEYRING</code></p>
<dd> This makes the UID-specific session keyring the default destination.</p>
<dt><code>KEY_REQKEY_DEFL_DEFAULT</code></p>
<dd> This selects the default behaviour which is to use the thread-specific keyring if there is one, otherwise the process-specific keyring if there is one, otherwise the session keyring if there is one, otherwise the UID-specific session keyring.</dl>
<p> This setting is inherited across <code>fork</code>() and <code>exec</code>(). </p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_set_reqkey_keyring</code>() returns <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The value of <i>reqkey_defl</i> is invalid.</dl>
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
