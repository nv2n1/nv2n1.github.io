---
title: "sd_pid_notify_with_fds(3)"
name: "sd_pid_notify_with_fds"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_pid_notify_with_fds/"
description: "sd_notify, sd_notifyf, sd_pid_notify, sd_pid_notifyf, sd_pid_notify_with_fds – Notify service manager about start-up completion and other service status changes"
---

<p>sd_notify, sd_notifyf, sd_pid_notify, sd_pid_notifyf, sd_pid_notify_with_fds &#8211; Notify service manager about start-up completion and other service status changes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;

int sd_notify(int unset_environment, const char *state);

int sd_notifyf(int unset_environment, const char *format, ...);

int sd_pid_notify(pid_t pid, int unset_environment, const char *state);

int sd_pid_notifyf(pid_t pid, int unset_environment, const char *format, ...);

int sd_pid_notify_with_fds(pid_t pid, int unset_environment, const char *state, const int *fds, unsigned n_fds);</code></pre>
<h2>Description</h2>
<p><code>sd_notify()</code></p>
<dd>may be called by a service to notify the service manager about state changes. It can be used to send arbitrary information, encoded in an environment-block-like string. Most importantly it can be used for start-up completion notification. If the <i>unset_environment</i> parameter is non-zero, <code>sd_notify()</code> will unset the <i>$NOTIFY_SOCKET</i> environment variable before returning (regardless of whether the function call itself succeeded or not). Further calls to <code>sd_notify()</code> will then fail, but the variable is no longer inherited by child processes. The <i>state</i> parameter should contain a newline-separated list of variable assignments, similar in style to an environment block. A trailing newline is implied if none is specified. The string may contain any kind of variable assignments, but the following shall be considered well-known: READY=1</p>
<dl>
<dd>Tells the service manager that service startup is finished. This is only used by systemd if the service definition file has Type=notify set. Since there is little value in signaling non-readiness, the only value services should send is &quot;READY=1&quot; (i.e. &quot;READY=0&quot; is not defined).</dl>
<p> RELOADING=1</p>
<dl>
<dd>Tells the service manager that the service is reloading its configuration. This is useful to allow the service manager to track the service&#8217;s internal state, and present it to the user. Note that a service that sends this notification must also send a &quot;READY=1&quot; notification when it completed reloading its configuration.</dl>
<p> STOPPING=1</p>
<dl>
<dd>Tells the service manager that the service is beginning its shutdown. This is useful to allow the service manager to track the service&#8217;s internal state, and present it to the user.</dl>
<p> BUSERROR=&#8230;</p>
<p>If a service fails, the D-Bus error-style error code. Example:<br />
&quot;BUSERROR=org.freedesktop.DBus.Error.TimedOut&quot;<br />
MAINPID=&#8230;</p>
<p>The main process ID (PID) of the service, in case the service manager did not fork off the process itself. Example:<br />
&quot;MAINPID=4711&quot; ERRNO=&#8230;</p>
<dl>
<dd>If a service fails, the errno-style error code, formatted as string. Example: &quot;ERRNO=2&quot; for ENOENT.</dl>
<p> BUSERROR=&#8230;</p>
<p>If a service fails, the D-Bus error-style error code. Example:<br />
&quot;BUSERROR=org.freedesktop.DBus.Error.TimedOut&quot;<br />
MAINPID=&#8230;</p>
<p>The main process ID (PID) of the service, in case the service manager did not fork off the process itself. Example:<br />
&quot;MAINPID=4711&quot; WATCHDOG=1</p>
<dl>
<dd>Tells the service manager to update the watchdog timestamp. This is the keep-alive ping that services need to issue in regular intervals if <i>WatchdogSec=</i> is enabled for it. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for information how to enable this functionality and <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3) for the details of how the service can check if the the watchdog is enabled.</dl>
<p> FDSTORE=1</p>
<dl>
<dd>Stores additional file descriptors in the service manager. File descriptors sent this way will be maintained per-service by the service manager and be passed again using the usual file descriptor passing logic on the next invocation of the service (see <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3)). This is useful for implementing service restart schemes where services serialize their state to /run, push their file descriptors to the system manager, and are then restarted, retrieving their state again via socket passing and /run. Note that the service manager will accept messages for a service only if <i>FileDescriptorStoreMax=</i> is set to non-zero for it (defaults to zero). See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details. Multiple arrays of file descriptors may be sent in separate messages, in which case the arrays are combined. Note that the service manager removes duplicate file descriptors before passing them to the service. Use <code>sd_pid_notify_with_fds()</code> to send messages with &quot;FDSTORE=1&quot;, see below.</dl>
<p> It is recommended to prefix variable names that are not listed above with <i>X_</i> to avoid namespace clashes. Note that systemd will accept status data sent from a service only if the <i>NotifyAccess=</i> option is correctly set in the service definition file. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details. <code>sd_notifyf()</code> is similar to <code>sd_notify()</code> but takes a <code>printf()</code>-like format string plus arguments. <code>sd_pid_notify()</code> and <code>sd_pid_notifyf()</code> are similar to <code>sd_notify()</code> and <code>sd_notifyf()</code> but take a process ID (PID) to use as originating PID for the message as first argument. This is useful to send notification messages on behalf of other processes, provided the appropriate privileges are available. If the PID argument is specified as 0 the process ID of the calling process is used, in which case the calls are fully equivalent to <code>sd_notify()</code> and <code>sd_notifyf()</code>. <code>sd_pid_notify_with_fds()</code> is similar to <code>sd_pid_notify()</code> but takes an additional array of file descriptors. These file descriptors are sent along the notification message to the service manager. This is particularly useful for sending &quot;FDSTORE=1&quot; messages, as described above. The additional arguments are a pointer to the file descriptor array plus the number of file descriptors in the array. If the number of file descriptors is passed as 0, the call is fully equivalent to <code>sd_pid_notify()</code>, i.e. no file descriptors are passed. Note that sending file descriptors to the service manager on messages that do not expect them (i.e. without &quot;FDSTORE=1&quot;) they are immediately closed on reception.</p>
<h2>Return Value</h2>
<p>On failure, these calls return a negative errno-style error code. If <i>$NOTIFY_SOCKET</i> was not set and hence no status data could be sent, 0 is returned. If the status was sent, these functions return with a positive return value. In order to support both, init systems that implement this scheme and those which do not, it is generally recommended to ignore the return value of this call.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. </p>
<p> Internally, these functions send a single datagram with the state string as payload to the <code>AF_UNIX</code> socket referenced in the <i>$NOTIFY_SOCKET</i> environment variable. If the first character of <i>$NOTIFY_SOCKET</i> is &quot;@&quot;, the string is understood as Linux abstract namespace socket. The datagram is accompanied by the process credentials of the sending service, using SCM_CREDENTIALS.</p>
<h2>Environment</h2>
<p><i>$NOTIFY_SOCKET</i></p>
<dl>
<dd>Set by the service manager for supervised processes for status and start-up completion notification. This environment variable specifies the socket <code>sd_notify()</code> talks to. See above for details.</dl>
<h2>Examples</h2>
<p><code>Example 1. Start-up Notification</code> When a service finished starting up, it might issue the following call to notify the service manager: sd_pid_notify_with_fds(0, 0, &quot;FDSTORE=1&quot;, &amp;fd, 1); <code>Example 2. Extended Start-up Notification</code> A service could send the following after completing initialization: sd_notifyf(0, &quot;READY=1
&quot;<br />
&quot;STATUS=Processing requests&#8230;
&quot;<br />
&quot;MAINPID=%lu&quot;,<br />
(unsigned long) getpid()); <code>Example 3. Error Cause Notification</code> A service could send the following shortly before exiting, on failure: sd_notifyf(0, &quot;STATUS=Failed to start up: %s
&quot;<br />
&quot;ERRNO=%i&quot;,<br />
strerror(errno),<br />
errno); <code>Example 4. Store a File Descriptor in the Service Manager</code> To store an open file descriptor in the service manager, in order to continue operation after a service restart without losing state use &quot;FDSTORE=1&quot;: </p>
<pre><code>sd_pid_notify_with_fds(0, 0, &quot;FDSTORE=1&quot;, &amp;fd, 1);</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3) </p>
