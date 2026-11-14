---
title: "selinux_status_getenforce(3)"
name: "selinux_status_getenforce"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_status_getenforce/"
description: "selinux_status_open, selinux_status_close, selinux_status_updated, selinux_status_getenforce, selinux_status_policyload and selinux_status_deny_unknown – reference the SELinux kernel status without..."
---

<p>selinux_status_open, selinux_status_close, selinux_status_updated, selinux_status_getenforce, selinux_status_policyload and selinux_status_deny_unknown &#8211; reference the SELinux kernel status without invocation of system calls</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/avc.h&gt;
int selinux_status_open(int fallback);
void selinux_status_close(void);
int selinux_status_updated(void);
int selinux_status_getenforce(void);
int selinux_status_policyload(void);
int selinux_status_deny_unknown(void);</code></pre>
<h2>Description</h2>
<p>Linux 2.6.37 or later provides a SELinux kernel status page; being mostly placed on <i>/sys/fs/selinux/status</i> entry. It enables userspace applications to mmap this page with read-only mode, then it informs some status without system call invocations. </p>
<p> In some cases that a userspace application tries to apply heavy frequent access control; such as row-level security in databases, it will face unignorable cost to communicate with kernel space to check invalidation of userspace avc. </p>
<p> These functions provides applications a way to know some kernel events without system-call invocation or worker thread for monitoring. </p>
<p> <code>selinux_status_open</code>() tries to <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <i>/sys/fs/selinux/status</i> and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) it in read-only mode. The file-descriptor and pointer to the page shall be stored internally; Don&#8217;t touch them directly. Set 1 on the <i>fallback</i> argument to handle a case of older kernels without kernel status page support. In this case, this function tries to open a netlink socket using <code><a href="/docs/linux/man/3-avc_netlink_open/">avc_netlink_open</a></code>(3) and overwrite corresponding callbacks ( setenforce and policyload). Thus, we need to pay attention to the interaction with these interfaces, when fallback mode is enabled. </p>
<p> <code>selinux_status_close</code>() unmap the kernel status page and close its file descriptor, or close the netlink socket if fallbacked. </p>
<p> <code>selinux_status_updated</code>() informs us whether something has been updated since the last call. It returns 0 if nothing was happened, however, 1 if something has been updated in this duration, or -1 on error. </p>
<p> <code>selinux_status_getenforce</code>() returns 0 if SELinux is running in permissive mode, 1 if enforcing mode, or -1 on error. Same as <code><a href="/docs/linux/man/3-security_getenforce/">security_getenforce</a></code>(3) except with or without system call invocation. </p>
<p> <code>selinux_status_policyload</code>() returns times of policy reloaded on the running system, or -1 on error. Note that it is not a reliable value on fallback-mode until it receive the first event message via netlink socket. Thus, don&#8217;t use this value to know actual times of policy reloaded. </p>
<p> <code>selinux_status_deny_unknown</code>() returns 0 if SELinux treats policy queries on undefined object classes or permissions as being allowed, 1 if such queries are denied, or -1 on error. </p>
<p> Also note that these interfaces are not thread-safe, so you have to protect them from concurrent calls using exclusive locks when multiple threads are performing.</p>
<h2>Return Value</h2>
<p><code>selinux_status_open</code>() returns 0 or 1 on success. 1 means we are ready to use these interfaces, but netlink socket was opened as fallback instead of the kernel status page. On error, -1 shall be returned. </p>
<p> Any other functions with a return value shall return its characteristic value as described above, or -1 on errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-avc_netlink_open/">avc_netlink_open</a></code>(3), <code><a href="/docs/linux/man/3-security_getenforce/">security_getenforce</a></code>(3), <code><a href="/docs/linux/man/3-security_deny_unknown/">security_deny_unknown</a></code>(3) </p>
