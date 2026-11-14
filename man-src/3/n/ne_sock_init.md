---
title: "ne_sock_init(3)"
name: "ne_sock_init"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_sock_init/"
description: "ne_sock_init, ne_sock_exit – perform library initialization"
---

<p>ne_sock_init, ne_sock_exit &#8211; perform library initialization</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_socket.h&gt;

int ne_sock_init(void);

void ne_sock_exit(void);</code></pre>
<h2>Description</h2>
<dd>In some platforms and configurations, neon may be using some socket or SSL libraries which require global initialization before use. To perform this initialization, the <code>ne_sock_init</code> function must be called before any other library functions are used. </p>
<p> Once all use of neon is complete, <code>ne_sock_exit</code> can be called to perform de-initialization of socket or SSL libraries, if necessary. Uses of <code>ne_sock_init</code> and <code>ne_sock_exit</code> are &quot;reference counted&quot;; if N calls to <code>ne_sock_init</code> are made, only the Nth call to <code>ne_sock_exit</code> will have effect. </p>
<p> <code>ne_sock_init</code> will set the disposition of the SIGPIPE signal to <i>ignored</i>. No change is made to the SIGPIPE disposition by <code>ne_sock_exit</code>. </p>
<p> Both the SSL libraries supported by neon &#8212; OpenSSL and GnuTLS &#8212; require callbacks to be registered to allow thread-safe use of SSL. These callbacks are stored as global variables and so their state persists for as long as the library in question is loaded into the process. If multiple users of the SSL library exist within the process, this can be problematic, particularly if one is dynamically loaded (and may subsequently be unloaded). </p>
<p> If neon is configured using the &#8211;enable-threadsafe-ssl flag, thread-safe SSL support will be enabled automatically, as covered in the following section. Otherwise, it is not safe to use neon with SSL in a multi-threaded process. The ne_has_support function can be used to determine whether neon is built to enable thread-safety support in the SSL library.</p>
<h3>Thread-safe SSL with OpenSSL</h3>
<p>neon follows two simple rules when dealing with the OpenSSL locking callbacks: </p>
<dl>
<dd>&bull; <code>ne_sock_init</code> will set thread-safety locking callbacks if and only if no locking callbacks are already registered.</dl>
<dl>
<dd>&bull; <code>ne_sock_exit</code> will unset the thread-safety locking callbacks if and only if the locking callbacks registered are those registered by <code>ne_sock_init</code>.</dl>
<p> Applications and libraries should be able to co-operate to ensure that SSL use is always thread-safe if similar rules are always followed.</p>
<h3>Thread-safe SSL with GnuTLS</h3>
<p>The cryptography library used by GnuTLS, libgcrypt, only supports an initialization operation to register thread-safety callbacks. <code>ne_sock_init</code> will register the thread-safe locking callbacks on first use; <code>ne_sock_exit</code> cannot unregister them. If multiple users of GnuTLS are present within the process, it is unsafe to dynamically unload neon from the process if neon is configured with thread-safe SSL support enabled (since the callbacks would be left pointing at unmapped memory once neon is unloaded).</p>
<h2>Return Value</h2>
<p><code>ne_sock_init</code> returns zero on success, or non-zero on error. If an error occurs, no further use of the neon library should be attempted.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-neon/">neon</a>(3), <a href="/docs/linux/man/3-ne_has_support/">ne_has_support</a>(3)</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
