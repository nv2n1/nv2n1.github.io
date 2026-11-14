---
title: "keyutils(7)"
name: "keyutils"
section: "7"
letter: "k"
url: "/docs/linux/man/7-keyutils/"
description: "keyutils – in-kernel key management utilities"
---

<p>keyutils &#8211; in-kernel key management utilities</p>
<h2>Description</h2>
<p>The <code>keyutils</code> package is a library and a set of utilities for accessing the kernel <code>keyrings</code> facility. A header file is supplied to provide the definitions and declarations required to access the library: </p>
<pre><code>#include &lt;keyutils.h&gt;</code></pre>
<p> To link with the library, the following:</p>
<dl>
<dd><code>-lkeyutils</code></dl>
<p> should be specified to the linker. Three system calls are provided:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2)</p>
<dd>Supply a new key to the kernel.</p>
<dt><code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2)</p>
<dd>Find an existing key for use, or, optionally, create one if one does not exist.</p>
<dt><code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2)</p>
<dd>Control a key in various ways. The library provides a variety of wrappers around this system call and those should be used rather than calling it directly.</dl>
<p> See the <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), and <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) manual pages for more information. The <code>keyctl</code>() wrappers are listed on the <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3) manual page.</p>
<h2>Utilities</h2>
<p>A program is provided to interact with the kernel facility by a number of subcommands, e.g.: </p>
<dl>
<dd><code>keyctl add user foo bar @s</code></dl>
<p> See the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) manual page for information on that. </p>
<p> The kernel has the ability to upcall to userspace to fabricate new keys. This can be triggered by <code>request_key</code>(), but userspace is better off using <code>add_key</code>() instead if it possibly can. </p>
<p> The upcalling mechanism is usually routed via the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program. What this does with any particular key is configurable in: </p>
<dl>
<dd><i>/etc/request-key.conf</i><br />
 <i>/etc/request-key.d/</i></dl>
<p> See the <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) and the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) manual pages for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) </p>
