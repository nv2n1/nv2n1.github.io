---
title: "iv_tls_user_ptr-2(3)"
name: "iv_tls_user_ptr-2"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_tls_user_ptr-2/"
description: "iv_tls_user_register, iv_tls_user_ptr – thread-local storage handling for ivykis modules"
---

<p>iv_tls_user_register, iv_tls_user_ptr &#8211; thread-local storage handling for ivykis modules</p>
<h2>Synopsis</h2>
<p><code>#include &lt;iv_tls.h&gt;</code> </p>
<pre>struct iv_tls_user {
 size_t sizeof_state;
 void (*init_thread)(void *st);
 void (*deinit_thread)(void *st);
};</pre>
<p><code>void iv_tls_user_register(struct iv_tls_user *</code><i>tu</i><code>);</code><br />
 <code>void *iv_tls_user_ptr(struct iv_tls_user *</code><i>tu</i><code>);</code> </p>
<h2>Description</h2>
<p>The <code>iv_tls</code> interface provides thread-local storage handling to <code>ivykis</code> modules. </p>
<p> An ivykis module can arrange for an amount of memory to be allocated for its use in each ivykis thread by calling <code>iv_tls_user_register.</code> This must be done before any calls to <code>iv_init</code> have been made in this process, and is typically done from a module initialization function marked as a constructor function. </p>
<p> The <code>-&gt;sizeof_state</code> member of the passed-in structure indicates how many bytes of memory the module wants allocated for its use in every ivykis thread. </p>
<p> When a thread calls <code>iv_init,</code> <code>-&gt;sizeof_state</code> bytes of memory will be allocated for use by this module in that thread, and initialised to zero. A pointer to this memory area can be obtained by calling <code>iv_tls_user_ptr</code> (which returns NULL in non-ivykis threads). </p>
<p> If the specified <code>-&gt;init_thread</code> function pointer is not NULL, it will be invoked at the end of <code>iv_init,</code> with its argument pointing to this thread&#8217;s memory area allocation for this module. </p>
<p> If <code>-&gt;deinit_thread</code> is not NULL, it will be invoked at the start of <code>iv_deinit,</code> or if the thread fails to call <code>iv_deinit</code> before terminating, at thread termination time. The argument passed into <code>-&gt;deinit_thread</code> is the same as for <code>-&gt;init_thread.</code> </p>
<p> It is permitted to call any ivykis API functions from the <code>-&gt;init_thread</code> and <code>-&gt;deinit_thread</code> callbacks. </p>
<p> There is no explicit serialization on calls to <code>-&gt;init_thread</code> and <code>-&gt;deinit_thread.</code> </p>
<p> Care must be taken when calling <code>iv_tls_user_ptr</code> from a signal handler, as there is a time window where it will return a non-NULL value before <code>-&gt;init_thread</code> or after <code>-&gt;deinit_thread</code> have been called. </p>
<p> Use of <code>iv_tls</code> for managing thread-local state is preferred over direct use of the <code>__thread</code> keyword, as not all platforms that ivykis runs on provide the <code>__thread</code> keyword. </p>
<p> Use of <code>iv_tls</code> for managing thread-local state is preferred over direct use of the <code>pthread_key_create</code> and <code>pthread_setspecific</code> APIs, as <code>iv_tls</code> provides a thread init hook as well as a destructor hook, and properly sequences <code>-&gt;init_thread</code> and <code>-&gt;deinit_thread</code> calls with core ivykis initialization and cleanup.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3)</p>
