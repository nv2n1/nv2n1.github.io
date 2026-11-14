---
title: "avc_cleanup(3)"
name: "avc_cleanup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_cleanup/"
description: "avc_open, avc_destroy, avc_reset, avc_cleanup – userspace SELinux AVC setup and teardown"
---

<h2 class="name">NAME</h2>
<p> avc_open, avc_destroy, avc_reset, avc_cleanup &#8211; userspace SELinux AVC setup and teardown </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_open(struct selinux_opt *</code><i>options</i><code>, unsigned </code><i>nopt</i><code>);</code> </p>
<p> <code>void avc_destroy(void);</code> </p>
<p> <code>int avc_reset(void);</code> </p>
<p> <code>void avc_cleanup(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>avc_open</code>() initializes the userspace AVC and must be called before any other AVC operation can be performed. </p>
<p> <code>avc_destroy</code>() destroys the userspace AVC, freeing all internal memory structures. After this call has been made, <code>avc_open</code>() must be called again before any AVC operations can be performed. </p>
<p> <code>avc_reset</code>() flushes the userspace AVC, causing it to forget any cached access decisions. The userspace AVC normally calls this function automatically when needed, see <code>NETLINK NOTIFICATION</code> below. </p>
<p> <code>avc_cleanup</code>() attempts to free unused memory within the userspace AVC, but does not flush any cached access decisions. Under normal operation, calling this function should not be necessary.</p>
<h2>OPTIONS</h2>
<p> The userspace AVC obeys callbacks set via <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), in particular the logging and audit callbacks. </p>
<p> The options which may be passed to <code>avc_open</code>() include the following:</p>
<dl>
<dt><code>AVC_OPT_SETENFORCE</code></p>
<dd> This option forces the userspace AVC into enforcing mode if the option value is non-NULL; permissive mode otherwise. The system enforcing mode will be ignored.</dl>
<h2>NETLINK NOTIFICATION</h2>
<p> Beginning with version 2.6.4, the Linux kernel supports SELinux status change notification via netlink. Two message types are currently implemented, indicating changes to the enforcing mode and to the loaded policy in the kernel, respectively. The userspace AVC listens for these messages and takes the appropriate action, modifying the behavior of <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3) to reflect the current enforcing mode and flushing the cache on receipt of a policy load notification. Audit messages are produced when netlink notifications are processed.</p>
<h2>RETURN VALUE</h2>
<p> Functions with a return value return zero on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3), <code><a href="/docs/linux/man/3-avc_context_to_sid/">avc_context_to_sid</a></code>(3), <code><a href="/docs/linux/man/3-avc_cache_stats/">avc_cache_stats</a></code>(3), <code><a href="/docs/linux/man/3-avc_add_callback/">avc_add_callback</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/3-security_compute_av/">security_compute_av</a></code>(3) </p>
<h2>Index</h2>
