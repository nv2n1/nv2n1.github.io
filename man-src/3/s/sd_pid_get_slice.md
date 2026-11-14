---
title: "sd_pid_get_slice(3)"
name: "sd_pid_get_slice"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_pid_get_slice/"
description: "sd_pid_get_session, sd_pid_get_unit, sd_pid_get_user_unit, sd_pid_get_owner_uid, sd_pid_get_machine_name, sd_pid_get_slice, sd_peer_get_session, sd_peer_get_unit, sd_peer_get_user_unit, sd_peer_get..."
---

<p>sd_pid_get_session, sd_pid_get_unit, sd_pid_get_user_unit, sd_pid_get_owner_uid, sd_pid_get_machine_name, sd_pid_get_slice, sd_peer_get_session, sd_peer_get_unit, sd_peer_get_user_unit, sd_peer_get_owner_uid, sd_peer_get_machine_name, sd_peer_get_slice &#8211; Determine session, service, owner of a session, container/VM or slice of a specific PID or socket peer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;

int sd_pid_get_session(pid_t pid, char **session);

int sd_pid_get_unit(pid_t pid, char **unit);

int sd_pid_get_user_unit(pid_t pid, char **unit);

int sd_pid_get_owner_uid(pid_t pid, uid_t *uid);

int sd_pid_get_machine_name(pid_t pid, char **name);

int sd_pid_get_slice(pid_t pid, char **slice);

int sd_peer_get_session(int fd, char **session);

int sd_peer_get_unit(int fd, char **unit);

int sd_peer_get_user_unit(int fd, char **unit);

int sd_peer_get_owner_uid(int fd, uid_t *uid);

int sd_peer_get_machine_name(int fd, char **name);

int sd_peer_get_slice(int fd, char **slice);</code></pre>
<h2>Description</h2>
<p><code>sd_pid_get_session()</code></p>
<dd>may be used to determine the login session identifier of a process identified by the specified process identifier. The session identifier is a short string, suitable for usage in file system paths. Note that not all processes are part of a login session (e.g. system service processes, user processes that are shared between multiple sessions of the same user, or kernel threads). For processes not being part of a login session this function will fail. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_pid_get_unit()</code> may be used to determine the systemd system unit (i.e. system service) identifier of a process identified by the specified PID. The unit name is a short string, suitable for usage in file system paths. Note that not all processes are part of a system unit/service (e.g. user processes, or kernel threads). For processes not being part of a systemd system unit this function will fail. (More specifically: this call will not work for processes that are part of user units, use <code>sd_pid_get_user_unit()</code> for that.) The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_pid_get_user_unit()</code> may be used to determine the systemd user unit (i.e. user service) identifier of a process identified by the specified PID. This is similar to <code>sd_pid_get_unit()</code> but applies to user units instead of system units. </p>
<p> <code>sd_pid_get_owner_uid()</code> may be used to determine the Unix user identifier of the owner of the session of a process identified the specified PID. Note that this function will succeed for user processes which are shared between multiple login sessions of the same user, where <code>sd_pid_get_session()</code> will fail. For processes not being part of a login session and not being a shared process of a user this function will fail. </p>
<p> <code>sd_pid_get_machine_name()</code> may be used to determine the name of the VM or container is a member of. The machine name is a short string, suitable for usage in file system paths. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> <code>sd_pid_get_slice()</code> may be used to determine the slice unit the process is a member of. See <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5) for details about slices. The returned string needs to be freed with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use. </p>
<p> If the <i>pid</i> parameter of any of these functions is passed as 0, the operation is executed for the calling process. </p>
<p> The <code>sd_peer_get_session()</code>, <code>sd_peer_get_unit()</code>, <code>sd_peer_get_user_unit()</code>, <code>sd_peer_get_owner_uid()</code>, <code>sd_peer_get_machine_name()</code> and <code>sd_peer_get_slice()</code> calls operate similar to their PID counterparts, but operate on a connected AF_UNIX socket and retrieve information about the connected peer process.</p>
<h2>Return Value</h2>
<p>On success, these calls return 0 or a positive integer. On failure, these calls return a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_pid_get_session()</code>, <code>sd_pid_get_unit()</code>, <code>sd_pid_get_user_unit()</code>, <code>sd_pid_get_owner_uid()</code>, <code>sd_pid_get_machine_name()</code>, <code>sd_pid_get_slice()</code>, <code>sd_peer_get_session()</code>, <code>sd_peer_get_unit()</code>, <code>sd_peer_get_user_unit()</code>, <code>sd_peer_get_owner_uid()</code>, <code>sd_peer_get_machine_name()</code> and <code>sd_peer_get_slice()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. </p>
<p> Note that the login session identifier as returned by <code>sd_pid_get_session()</code> is completely unrelated to the process session identifier as returned by <code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_session_is_active/">sd_session_is_active</a></code>(3), <code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8) </p>
