---
title: "sd_login_monitor_get_events(3)"
name: "sd_login_monitor_get_events"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_login_monitor_get_events/"
description: "sd_login_monitor_new, sd_login_monitor_unref, sd_login_monitor_flush, sd_login_monitor_get_fd, sd_login_monitor_get_events, sd_login_monitor_get_timeout, sd_login_monitor – Monitor login sessions, ..."
---

<p>sd_login_monitor_new, sd_login_monitor_unref, sd_login_monitor_flush, sd_login_monitor_get_fd, sd_login_monitor_get_events, sd_login_monitor_get_timeout, sd_login_monitor &#8211; Monitor login sessions, seats, users and virtual machines/containers </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-login.h&gt;
</pre>
<dl COMPACT>
<dt> <code>int sd_login_monitor_new(const char&nbsp;<wbr>*</code><i>category</i><code>, sd_login_monitor&nbsp;<wbr>**</code><i>ret</i><code>);</code></p>
<dt> <code>sd_login_monitor *sd_login_monitor_unref(sd_login_monitor&nbsp;<wbr>*</code><i>m</i><code>);</code></p>
<dt> <code>int sd_login_monitor_flush(sd_login_monitor&nbsp;<wbr>*</code><i>m</i><code>);</code></p>
<dt> <code>int sd_login_monitor_get_fd(sd_login_monitor&nbsp;<wbr>*</code><i>m</i><code>);</code></p>
<dt> <code>int sd_login_monitor_get_events(sd_login_monitor&nbsp;<wbr>*</code><i>m</i><code>);</code></p>
<dt> <code>int sd_login_monitor_get_timeout(sd_login_monitor&nbsp;<wbr>*</code><i>m</i><code>, uint64_t&nbsp;<wbr>*</code><i>timeout_usec</i><code>);</code></dl>
<h2>Description</h2>
<p> <code>sd_login_monitor_new()</code></p>
<dd>may be used to monitor login sessions, users, seats, and virtual machines/containers. Via a monitor object a file descriptor can be integrated into an application defined event loop which is woken up each time a user logs in, logs out or a seat is added or removed, or a session, user, seat or virtual machine/container changes state otherwise. The first parameter takes a string which can be &quot;seat&quot; (to get only notifications about seats being added, removed or changed), &quot;session&quot; (to get only notifications about sessions being created or removed or changed), &quot;uid&quot; (to get only notifications when a user changes state in respect to logins) or &quot;machine&quot; (to get only notifications when a virtual machine or container is started or stopped). If notifications shall be generated in all these conditions, <code>NULL</code> may be passed. Note that in the future additional categories may be defined. The second parameter returns a monitor object and needs to be freed with the <code>sd_login_monitor_unref()</code> call after use. </p>
<p> <code>sd_login_monitor_unref()</code> may be used to destroy a monitor object. Note that this will invalidate any file descriptor returned by <code>sd_login_monitor_get_fd()</code>. </p>
<p> <code>sd_login_monitor_flush()</code> may be used to reset the wakeup state of the monitor object. Whenever an event causes the monitor to wake up the event loop via the file descriptor this function needs to be called to reset the wake-up state. If this call is not invoked, the file descriptor will immediately wake up the event loop again. </p>
<p> <code>sd_login_monitor_get_fd()</code> may be used to retrieve the file descriptor of the monitor object that may be integrated in an application defined event loop, based around <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) or a similar interface. The application should include the returned file descriptor as wake-up source for the events mask returned by <code>sd_login_monitor_get_events()</code>. It should pass a timeout value as returned by <code>sd_login_monitor_get_timeout()</code>. Whenever a wake-up is triggered the file descriptor needs to be reset via <code>sd_login_monitor_flush()</code>. An application needs to reread the login state with a function like <code><a href="/docs/linux/man/3-sd_get_seats/">sd_get_seats</a></code>(3) or similar to determine what changed. </p>
<p> <code>sd_login_monitor_get_events()</code> will return the <code>poll()</code> mask to wait for. This function will return a combination of <code>POLLIN</code>, <code>POLLOUT</code> and similar to fill into the &quot;.events&quot; field of <i>struct pollfd</i>. </p>
<p> <code>sd_login_monitor_get_timeout()</code> will return a timeout value for usage in <code>poll()</code>. This returns a value in microseconds since the epoch of <code>CLOCK_MONOTONIC</code> for timing out <code>poll()</code> in <i>timeout_usec</i>. See <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) for details about <code>CLOCK_MONOTONIC</code>. If there is no timeout to wait for this will fill in <code>(uint64_t) -1</code> instead. Note that <code>poll()</code> takes a relative timeout in milliseconds rather than an absolute timeout in microseconds. To convert the absolute &#8216;us&#8217; timeout into relative &#8216;ms&#8217;, use code like the following: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
uint64_t t;
int msec;
sd_login_monitor_get_timeout(m, &amp;t);
if (t == (uint64_t) -1)
  msec = -1;
else {
  struct timespec ts;
  uint64_t n;
  clock_getttime(CLOCK_MONOTONIC, &amp;ts);
  n = (uint64_t) ts.tv_sec * 1000000 + ts.tv_nsec / 1000;
  msec = t &gt; n ? (int) ((t - n + 999) / 1000) : 0;
}
</pre>
</dl>
<p> The code above does not do any error checking for brevity&#8217;s sake. The calculated <i>msec</i> integer can be passed directly as <code>poll()</code>&#8216;s timeout parameter.</p>
<h2>Return Value</h2>
<p> On success, <code>sd_login_monitor_new()</code>, <code>sd_login_monitor_flush()</code> and <code>sd_login_monitor_get_timeout()</code> return 0 or a positive integer. On success, <code>sd_login_monitor_get_fd()</code> returns a Unix file descriptor. On success, <code>sd_login_monitor_get_events()</code> returns a combination of <code>POLLIN</code>, <code>POLLOUT</code> and suchlike. On failure, these calls return a negative errno-style error code. </p>
<p> <code>sd_login_monitor_unref()</code> always returns <code>NULL</code>.</p>
<h2>Notes</h2>
<p> The <code>sd_login_monitor_new()</code>, <code>sd_login_monitor_unref()</code>, <code>sd_login_monitor_flush()</code>, <code>sd_login_monitor_get_fd()</code>, <code>sd_login_monitor_get_events()</code> and <code>sd_login_monitor_get_timeout()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-login/">sd-login</a></code>(3), <code><a href="/docs/linux/man/3-sd_get_seats/">sd_get_seats</a></code>(3), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)</p>
