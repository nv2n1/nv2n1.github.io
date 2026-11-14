---
title: "sd_watchdog_enabled(3)"
name: "sd_watchdog_enabled"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_watchdog_enabled/"
description: "sd_watchdog_enabled – Check whether the service manager expects watchdog keep-alive notifications from a service"
---

<p>sd_watchdog_enabled &#8211; Check whether the service manager expects watchdog keep-alive notifications from a service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;

int sd_watchdog_enabled(int unset_environment, uint64_t *usec);</code></pre>
<h2>Description</h2>
<p><code>sd_watchdog_enabled()</code></p>
<dd>may be called by a service to detect whether the service manager expects regular keep-alive watchdog notification events from it, and the timeout after which the manager will act on the service if it did not get such a notification. </p>
<p> If the <i>$WATCHDOG_USEC</i> environment variable is set, and the <i>$WATCHDOG_PID</i> variable is unset or set to the PID of the current process, the service manager expects notifications from this process. The manager will usually terminate a service when it does not get a notification message within the specified time after startup and after each previous message. It is recommended that a daemon sends a keep-alive notification message to the service manager every half of the time returned here. Notification messages may be sent with <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) with a message string of &quot;WATCHDOG=1&quot;. </p>
<p> If the <i>unset_environment</i> parameter is non-zero, <code>sd_watchdog_enabled()</code> will unset the <i>$WATCHDOG_USEC</i> and <i>$WATCHDOG_PID</i> environment variables before returning (regardless of whether the function call itself succeeded or not). Those variables are no longer inherited by child processes. Further calls to <code>sd_watchdog_enabled()</code> will also return with zero. </p>
<p> If the <i>usec</i> parameter is non-NULL, <code>sd_watchdog_enabled()</code> will write the timeout in &micro;s for the watchdog logic to it. </p>
<p> To enable service supervision with the watchdog logic, use <i>WatchdogSec=</i> in service files. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details.</p>
<h2>Return Value</h2>
<p>On failure, this call returns a negative errno-style error code. If the service manager expects watchdog keep-alive notification messages to be sent, &gt; 0 is returned, otherwise 0 is returned. Only if the return value is &gt; 0, the <i>usec</i> parameter is valid after the call.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. </p>
<p> Internally, this functions parses the <i>$WATCHDOG_PID</i> and <i>$WATCHDOG_USEC</i> environment variable. The call will ignore these variables if <i>$WATCHDOG_PID</i> does not contain the PID of the current process, under the assumption that in that case, the variables were set for a different process further up the process tree.</p>
<h2>Environment</h2>
<p><i>$WATCHDOG_PID</i></p>
<dl>
<dd>Set by the system manager for supervised process for which watchdog support is enabled, and contains the PID of that process. See above for details.</dl>
<p> <i>$WATCHDOG_USEC</i></p>
<dl>
<dd>Set by the system manager for supervised process for which watchdog support is enabled, and contains the watchdog timeout in &micro;s See above for details.</dl>
<h2>History</h2>
<p>The watchdog functionality and the <i>$WATCHDOG_USEC</i> variable were added in systemd-41. </p>
<p> <code>sd_watchdog_enabled()</code> function was added in systemd-209. Since that version the <i>$WATCHDOG_PID</i> variable is also set.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) </p>
