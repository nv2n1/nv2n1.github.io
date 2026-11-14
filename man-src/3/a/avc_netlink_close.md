---
title: "avc_netlink_close(3)"
name: "avc_netlink_close"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_netlink_close/"
description: "avc_netlink_open, avc_netlink_close, avc_netlink_acquire_fd, avc_netlink_release_fd, avc_netlink_check_nb, avc_netlink_loop – SELinux netlink processing"
---

<h2 class="name">NAME</h2>
<p> avc_netlink_open, avc_netlink_close, avc_netlink_acquire_fd, avc_netlink_release_fd, avc_netlink_check_nb, avc_netlink_loop &#8211; SELinux netlink processing </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_netlink_open(int </code><i>blocking</i><code>);</code> </p>
<p> <code>void avc_netlink_close(void);</code> </p>
<p> <code>int avc_netlink_acquire_fd(void);</code> </p>
<p> <code>void avc_netlink_release_fd(void);</code> </p>
<p> <code>void avc_netlink_loop(void);</code> </p>
<p> <code>int avc_netlink_check_nb(void);</code></p>
<h2>DESCRIPTION</h2>
<p> These functions enable applications to handle notification of SELinux events via netlink. The userspace AVC normally checks for netlink messages on each call to <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3). Applications may wish to override this behavior and check for notification separately, for example in a <code><a href="/docs/linux/man/2-select/">select</a></code>(2) loop. These functions also permit netlink monitoring without requiring a call to <code><a href="/docs/linux/man/3-avc_open/">avc_open</a></code>(3). </p>
<p> <code>avc_netlink_open</code>() opens a netlink socket to receive SELinux notifications. The socket descriptor is stored internally; use <code><a href="/docs/linux/man/3-avc_netlink_acquire_fd/">avc_netlink_acquire_fd</a></code>(3) to take ownership of it in application code. The <i>blocking</i> argument controls whether the O_NONBLOCK flag is set on the socket descriptor. <code><a href="/docs/linux/man/3-avc_open/">avc_open</a></code>(3) calls this function internally, specifying non-blocking behavior. </p>
<p> <code>avc_netlink_close</code>() closes the netlink socket. This function is called automatically by <code><a href="/docs/linux/man/3-avc_destroy/">avc_destroy</a></code>(3). </p>
<p> <code>avc_netlink_acquire_fd</code>() returns the netlink socket descriptor number and informs the userspace AVC not to check the socket descriptor automatically on calls to <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3). </p>
<p> <code>avc_netlink_release_fd</code>() returns control of the netlink socket to the userspace AVC, re-enabling automatic processing of notifications. </p>
<p> <code>avc_netlink_check_nb</code>() checks the netlink socket for pending messages and processes them. Callbacks for policyload and enforcing changes will be called; see <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3). This function does not block. </p>
<p> <code>avc_netlink_loop</code>() enters a loop blocking on the netlink socket and processing messages as they are received. This function will not return unless an error occurs on the socket, in which case the socket is closed.</p>
<h2>RETURN VALUE</h2>
<p> <code>avc_netlink_acquire_fd</code>() returns a non-negative file descriptor number on success. Other functions with a return value return zero on success. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_open/">avc_open</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
