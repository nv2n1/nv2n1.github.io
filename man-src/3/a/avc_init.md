---
title: "avc_init(3)"
name: "avc_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_init/"
description: "avc_init – legacy userspace SELinux AVC setup"
---

<h2 class="name">NAME</h2>
<p> avc_init &#8211; legacy userspace SELinux AVC setup </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_init(const char *</code><i>msgprefix</i><code>,</code> <code>const struct avc_memory_callback *</code><i>mem_callbacks</i><code>,</code><br />
 <code>const struct avc_log_callback *</code><i>log_callbacks</i><code>,</code><br />
 <code>const struct avc_thread_callback *</code><i>thread_callbacks</i><code>,</code><br />
 <code>const struct avc_lock_callback *</code><i>lock_callbacks</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>avc_init</code>() is deprecated; please use <code><a href="/docs/linux/man/3-avc_open/">avc_open</a></code>(3) in conjunction with <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3) in all new code. </p>
<p> <code>avc_init</code>() initializes the userspace AVC and must be called before any other AVC operation can be performed. A non-NULL <i>msgprefix</i> will be prepended to all audit messages produced by the userspace AVC. The default is `uavc&#8217;. The remaining arguments, if non-NULL, specify callbacks to be used by the userspace AVC.</p>
<h2>CALLBACKS</h2>
<p> The userspace AVC can be directed how to perform memory allocation, logging, thread creation, and locking via callback functions passed to <code>avc_init</code>(). The purpose of this functionality is to allow the userspace AVC to be smoothly integrated into existing userspace object managers. </p>
<p> Use an <code>avc_memory_callback</code> structure to specify alternate functions for dynamic memory allocation. </p>
<dl>
<dt>
<dd>
<pre><code>
struct avc_memory_callback {
    void *(*func_malloc)(size_t size);
    void (*func_free)(void *ptr);
};
</code></pre>
</dl>
<p> The two fields of the structure should be pointers to functions which behave as <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and <code><a href="/docs/linux/man/3-free/">free</a></code>(3), which are used by default. </p>
<p> Use an <code>avc_log_callback</code> structure to specify alternate functions for logging. </p>
<dl>
<dt>
<dd>
struct avc_log_callback {<br />
    void (*func_log)(const char *fmt, &#8230;);<br />
    void (*func_audit)(void *auditdata,<br />
                       security_class_t class,<br />
                       char *msgbuf, size_t msgbufsize);<br />
};
</dl>
<p> The <code>func_log</code> callback should accept a <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) style format and arguments and log them as desired. The default behavior prints the message on the standard error. The <code>func_audit</code> callback should interpret the <i>auditdata</i> parameter for the given <i>class</i>, printing a human-readable interpretation to <i>msgbuf</i> using no more than <i>msgbufsize</i> characters. The default behavior is to ignore <i>auditdata</i>. </p>
<p> Use an <code>avc_thread_callback</code> structure to specify functions for starting and manipulating threads. </p>
<dl>
<dt>
<dd>
struct avc_thread_callback {<br />
    void *(*func_create_thread)(void (*run)(void));<br />
    void (*func_stop_thread)(void *thread);<br />
};
</dl>
<p> The <code>func_create_thread</code> callback should create a new thread and return a pointer which references it. The thread should execute the <i>run</i> argument, which does not return under normal conditions. The <code>func_stop_thread</code> callback should cancel the running thread referenced by <i>thread</i>. By default, threading is not used; see <code>NETLINK NOTIFICATION</code> below. </p>
<p> Use an <code>avc_lock_callback</code> structure to specify functions to create, obtain, and release locks for use by threads. </p>
<dl>
<dt>
<dd>
<pre><code>
struct avc_lock_callback {
    void *(*func_alloc_lock)(void);
    void (*func_get_lock)(void *lock);
    void (*func_release_lock)(void *lock);
    void (*func_free_lock)(void *lock);
};
</code></pre>
</dl>
<p> The <code>func_alloc_lock</code> callback should create a new lock, returning a pointer which references it. The <code>func_get_lock</code> callback should obtain <i>lock</i>, blocking if necessary. The <code>func_release_lock</code> callback should release <i>lock</i>. The <code>func_free_lock</code> callback should destroy <i>lock</i>, freeing any resources associated with it. The default behavior is not to perform any locking. Note that undefined behavior may result if threading is used without appropriate locking.</p>
<h2>NETLINK NOTIFICATION</h2>
<p> Beginning with version 2.6.4, the Linux kernel supports SELinux status change notification via netlink. Two message types are currently implemented, indicating changes to the enforcing mode and to the loaded policy in the kernel, respectively. The userspace AVC listens for these messages and takes the appropriate action, modifying the behavior of <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3) to reflect the current enforcing mode and flushing the cache on receipt of a policy load notification. Audit messages are produced when netlink notifications are processed. </p>
<p> In the default single-threaded mode, the userspace AVC checks for new netlink messages at the start of each permission query. If threading and locking callbacks are passed to <code>avc_init</code>() however, a dedicated thread will be started to listen on the netlink socket. This may increase performance and will ensure that log messages are generated immediately rather than at the time of the next permission query.</p>
<h2>RETURN VALUE</h2>
<p> Functions with a return value return zero on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>NOTES</h2>
<p> The <i>msgprefix</i> argument to <code>avc_init</code>() currently has a length limit of 15 characters and will be truncated if necessary. </p>
<p> If a provided <code>func_malloc</code> callback does not set <i>errno</i> appropriately on error, userspace AVC calls may exhibit the same behavior. </p>
<p> If a netlink thread has been created and an error occurs on the socket (such as an access error), the thread may terminate and cause the userspace AVC to return <code>EINVAL</code> on all further permission checks until <code>avc_destroy </code> is called.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_open/">avc_open</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
