---
title: "avc_add_callback(3)"
name: "avc_add_callback"
section: "3"
letter: "a"
url: "/docs/linux/man/3-avc_add_callback/"
description: "avc_add_callback – additional event notification for SELinux userspace object managers"
---

<h2 class="name">NAME</h2>
<p> avc_add_callback &#8211; additional event notification for SELinux userspace object managers </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code><br />
 <code>#include &lt;selinux/avc.h&gt;</code> </p>
<p> <code>int avc_add_callback(int (*</code><i>callback</i><code>)(uint32_t </code><i>event</i><code>,</code> <code>security_id_t </code><i>ssid</i><code>,</code><br />
 <code>security_id_t </code><i>tsid</i><code>,</code><br />
 <code>security_class_t </code><i>tclass</i><code>,</code><br />
 <code>access_vector_t </code><i>perms</i><code>,</code><br />
 <code>access_vector_t *</code><i>out_retained</i><code>),</code> <code>uint32_t </code><i>events</i><code>, security_id_t </code><i>ssid</i><code>,</code><br />
 <code>security_id_t </code><i>tsid</i><code>, security_class_t </code><i>tclass</i><code>,</code><br />
 <code>access_vector_t </code><i>perms</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>avc_add_callback</code>() is used to register callback functions on security events. The purpose of this functionality is to allow userspace object managers to take additional action when a policy change, usually a policy reload, causes permissions to be granted or revoked. </p>
<p> <i>events</i> is the bitwise-<i>or</i> of security events on which to register the callback; see <code>SECURITY EVENTS</code> below. </p>
<p> <i>ssid</i>, <i>tsid</i>, <i>tclass</i>, and <i>perms</i> specify the source and target SID&#8217;s, target class, and specific permissions that the callback wishes to monitor. The special symbol <code>SECSID_WILD</code> may be passed as the <i>source</i> or <i>target</i> and will cause any SID to match. </p>
<p> <i>callback</i> is the callback function provided by the userspace object manager. The <i>event</i> argument indicates the security event which occurred; the remaining arguments are interpreted according to the event as described below. The return value of the callback should be zero on success, -1 on error with <i>errno</i> set appropriately (but see <code>RETURN VALUE</code> below).</p>
<h2>SECURITY EVENTS</h2>
<p> In all cases below, <i>ssid</i> and/or <i>tsid</i> may be set to <code>SECSID_WILD</code>, indicating that the change applies to all source and/or target SID&#8217;s. Unless otherwise indicated, the <i>out_retained</i> parameter is unused.</p>
<dl>
<dt><code>AVC_CALLBACK_GRANT</code></p>
<dd> Previously denied permissions are now granted for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>. <i>perms</i> indicates the permissions to grant.</p>
<dt><code>AVC_CALLBACK_TRY_REVOKE</code></p>
<dd> Previously granted permissions are now conditionally revoked for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>. <i>perms</i> indicates the permissions to revoke. The callback should set <i>out_retained</i> to the subset of <i>perms</i> which are retained as migrated permissions. Note that <i>out_retained</i> is ignored if the callback returns -1.</p>
<dt><code>AVC_CALLBACK_REVOKE</code></p>
<dd> Previously granted permissions are now unconditionally revoked for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>. <i>perms</i> indicates the permissions to revoke.</p>
<dt><code>AVC_CALLBACK_RESET</code></p>
<dd> Indicates that the cache was flushed. The SID, class, and permission arguments are unused and are set to NULL.</p>
<dt><code>AVC_CALLBACK_AUDITALLOW_ENABLE</code></p>
<dd> The permissions given by <i>perms</i> should now be audited when granted for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>.</p>
<dt><code>AVC_CALLBACK_AUDITALLOW_DISABLE</code></p>
<dd> The permissions given by <i>perms</i> should no longer be audited when granted for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>.</p>
<dt><code>AVC_CALLBACK_AUDITDENY_ENABLE</code></p>
<dd> The permissions given by <i>perms</i> should now be audited when denied for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>.</p>
<dt><code>AVC_CALLBACK_AUDITDENY_DISABLE</code></p>
<dd> The permissions given by <i>perms</i> should no longer be audited when denied for <i>ssid</i>, <i>tsid</i> with respect to <i>tclass</i>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>avc_add_callback</code>() returns zero. On error, -1 is returned and <i>errno</i> is set appropriately. </p>
<p> A return value of -1 from a callback is interpreted as a failed policy operation. If such a return value is encountered, all remaining callbacks registered on the event are called. In threaded mode, the netlink handler thread may then terminate and cause the userspace AVC to return <code>EINVAL</code> on all further permission checks until <code><a href="/docs/linux/man/3-avc_destroy/">avc_destroy</a></code>(3) is called. In non-threaded mode, the permission check on which the error occurred will return -1 and the value of <i>errno</i> encountered to the caller. In both cases, a log message is produced and the kernel may be notified of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> An attempt to allocate memory failed.</dl>
<h2>NOTES</h2>
<p> If the userspace AVC is running in threaded mode, callbacks registered via <code>avc_add_callback</code>() may be executed in the context of the netlink handler thread. This will likely introduce synchronization issues requiring the use of locks. See <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3). </p>
<p> Support for dynamic revocation and retained permissions is mostly unimplemented in the SELinux kernel module. The only security event that currently gets exercised is <code>AVC_CALLBACK_RESET</code>.</p>
<h2>AUTHOR</h2>
<p> Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-avc_init/">avc_init</a></code>(3), <code><a href="/docs/linux/man/3-avc_has_perm/">avc_has_perm</a></code>(3), <code><a href="/docs/linux/man/3-avc_context_to_sid/">avc_context_to_sid</a></code>(3), <code><a href="/docs/linux/man/3-avc_cache_stats/">avc_cache_stats</a></code>(3), <code><a href="/docs/linux/man/3-security_compute_av/">security_compute_av</a></code>(3) <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
<h2>Index</h2>
