---
title: "systemd-notify(1)"
name: "systemd-notify"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-notify/"
description: "systemd-notify – Notify service manager about start-up completion and other daemon status changes"
---

<h2 class="name">NAME</h2>
<p> systemd-notify &#8211; Notify service manager about start-up completion and other daemon status changes </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-notify </code><code>[OPTIONS&#8230;]</code><code>[VARIABLE=VALUE&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-notify</code></p>
<dd>may be called by daemon scripts to notify the init system about status changes. It can be used to send arbitrary information, encoded in an environment-block-like list of strings. Most importantly, it can be used for start-up completion notification. </p>
<p> This is mostly just a wrapper around <code>sd_notify()</code> and makes this functionality available to shell scripts. For details see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3). </p>
<p> The command line may carry a list of environment variables to send as part of the status update. </p>
<p> Note that systemd will refuse reception of status updates from this command unless <i>NotifyAccess=</i> is set for the service unit this command is called from. </p>
<p> Note that <code>sd_notify()</code> notifications may be attributed to units correctly only if either the sending process is still around at the time PID 1 processes the message, or if the sending process is explicitly runtime-tracked by the service manager. The latter is the case if the service manager originally forked off the process, i.e. on all processes that match <i>NotifyAccess=</i><code>main</code> or <i>NotifyAccess=</i><code>exec</code>. Conversely, if an auxiliary process of the unit sends an <code>sd_notify()</code> message and immediately exits, the service manager might not be able to properly attribute the message to the unit, and thus will ignore it, even if <i>NotifyAccess=</i><code>all </code> is set for it. When <code>&#8211;no-block</code> is used, all synchronization for reception of notifications is disabled, and hence the aforementioned race may occur if the invoking process is not the service manager or spawned by the service manager. </p>
<p> Hence, <code>systemd-notify</code> will first attempt to invoke <code>sd_notify()</code> pretending to have the PID of the invoking process. This will only succeed when invoked with sufficient privileges. On failure, it will then fall back to invoking it under its own PID. This behaviour is useful in order that when the tool is invoked from a shell script the shell process &#8212; and not the <code>systemd-notify</code> process &#8212; appears as sender of the message, which in turn is helpful if the shell process is the main process of a service, due to the limitations of <i>NotifyAccess=</i><code>all</code>. Use the <code>&#8211;pid=</code> switch to tweak this behaviour.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;ready</code></p>
<dl>
<dt>
<dd> Inform the init system about service start-up completion. This is equivalent to <code>systemd-notify READY=1</code>. For details about the semantics of this option see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3).</dl>
<p> <code>&#8211;pid=</code></p>
<dl>
<dt>
<dd> Inform the service manager about the main PID of the daemon. Takes a PID as argument. If the argument is specified as &quot;auto&quot; or omitted, the PID of the process that invoked <code>systemd-notify</code> is used, except if that&#8217;s the service manager. If the argument is specified as &quot;self&quot;, the PID of the <code>systemd-notify</code> command itself is used, and if &quot;parent&quot; is specified the calling process&#8217; PID is used &#8212; even if it is the service manager. This is equivalent to <code>systemd-notify MAINPID=$PID</code>. For details about the semantics of this option see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3).</dl>
<p> <code>&#8211;uid=</code><i>USER</i></p>
<dl>
<dt>
<dd> Set the user ID to send the notification from. Takes a UNIX user name or numeric UID. When specified the notification message will be sent with the specified UID as sender, in place of the user the command was invoked as. This option requires sufficient privileges in order to be able manipulate the user identity of the process.</dl>
<p> <code>&#8211;status=</code></p>
<dl>
<dt>
<dd> Send a free-form status string for the daemon to the init systemd. This option takes the status string as argument. This is equivalent to <code>systemd-notify STATUS=&#8230;</code>. For details about the semantics of this option see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3).</dl>
<p> <code>&#8211;booted</code></p>
<dl>
<dt>
<dd> Returns 0 if the system was booted up with systemd, non-zero otherwise. If this option is passed, no message is sent. This option is hence unrelated to the other options. For details about the semantics of this option, see <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3). An alternate way to check for this state is to call <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) with the <code>is-system-running</code> command. It will return &quot;offline&quot; if the system was not booted with systemd.</dl>
<p> <code>&#8211;no-block</code></p>
<dl>
<dt>
<dd> Do not synchronously wait for the requested operation to finish. Use of this option is only recommended when <code>systemd-notify</code> is spawned by the service manager, or when the invoking process is directly spawned by the service manager and has enough privileges to allow <code>systemd-notify</code> to send the notification on its behalf. Sending notifications with this option set is prone to race conditions in all other cases.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>EXAMPLE</h2>
<p> <code>Example 1. Start-up Notification and Status Updates</code> </p>
<p> A simple shell daemon that sends start-up notifications after having set up its communication channel. During runtime it sends further status updates to the init system: </p>
<dl>
<dt>
<dd>
<pre><code>
#!/ bin / bash
mkfifo / tmp / waldo systemd - notify-- ready-- status = "Waiting for data..." while:;
do
read a &lt; / tmp / waldo systemd - notify-- status = "Processing $a"
#Do something with $a...
                                                   systemd -
                                                   notify-- status = "Waiting for data..." done
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3) </p>
<h2>Index</h2>
