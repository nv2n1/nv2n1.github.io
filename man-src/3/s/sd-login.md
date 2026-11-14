---
title: "sd-login(3)"
name: "sd-login"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd-login/"
description: "sd-login – APIs for tracking logins"
---

<p>sd-login &#8211; APIs for tracking logins</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-login.h&gt;





pkg-config --cflags --libs libsystemd</code></pre>
<h2>Description</h2>
<dd>sd-login.h provides APIs to introspect and monitor seat, login session and user status information on the local system. </p>
<p> See m[blue]<code>Multi-Seat on Linux</code>m[]<font SIZE="-2">[1]</font> for an introduction into multi-seat support on Linux, the background for this set of APIs. </p>
<p> Note that these APIs only allow purely passive access and monitoring of seats, sessions and users. To actively make changes to the seat configuration, terminate login sessions, or switch session on a seat you need to utilize the D-Bus API of systemd-logind, instead. </p>
<p> These functions synchronously access data in /proc, /sys/fs/cgroup and /run. All of these are virtual file systems, hence the runtime cost of the accesses is relatively cheap. </p>
<p> It is possible (and often a very good choice) to mix calls to the synchronous interface of sd-login.h with the asynchronous D-Bus interface of systemd-logind. However, if this is done you need to think a bit about possible races since the stream of events from D-Bus and from sd-login.h interfaces such as the login monitor are asynchronous and not ordered against each other. </p>
<p> If the functions return string arrays, these are generally <code>NULL</code> terminated and need to be freed by the caller with the libc <code><a href="/docs/linux/man/3-free/">free</a></code>(3) call after use, including the strings referenced therein. Similarly, individual strings returned need to be freed, as well. </p>
<p> As a special exception, instead of an empty string array <code>NULL</code> may be returned, which should be treated equivalent to an empty string array. </p>
<p> See <code><a href="/docs/linux/man/3-sd_pid_get_session/">sd_pid_get_session</a></code>(3), <code><a href="/docs/linux/man/3-sd_uid_get_state/">sd_uid_get_state</a></code>(3), <code><a href="/docs/linux/man/3-sd_session_is_active/">sd_session_is_active</a></code>(3), <code><a href="/docs/linux/man/3-sd_seat_get_active/">sd_seat_get_active</a></code>(3), <code><a href="/docs/linux/man/3-sd_get_seats/">sd_get_seats</a></code>(3), <code><a href="/docs/linux/man/3-sd_login_monitor_new/">sd_login_monitor_new</a></code>(3) for more information about the functions implemented.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_pid_get_session/">sd_pid_get_session</a></code>(3), <code><a href="/docs/linux/man/3-sd_uid_get_state/">sd_uid_get_state</a></code>(3), <code><a href="/docs/linux/man/3-sd_session_is_active/">sd_session_is_active</a></code>(3), <code><a href="/docs/linux/man/3-sd_seat_get_active/">sd_seat_get_active</a></code>(3), <code><a href="/docs/linux/man/3-sd_get_seats/">sd_get_seats</a></code>(3), <code><a href="/docs/linux/man/3-sd_login_monitor_new/">sd_login_monitor_new</a></code>(3), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/3-sd-readahead/">sd-readahead</a></code>(3), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Multi-Seat on Linux</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/multiseat">http://www.freedesktop.org/wiki/Software/systemd/multiseat</a></dl>
