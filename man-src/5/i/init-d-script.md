---
title: "init-d-script(5)"
name: "init-d-script"
section: "5"
letter: "i"
url: "/docs/linux/man/5-init-d-script/"
description: "init-d-script – interpreter for short and simple init.d scripts"
---

<p>Debian</p>
<h2>Name</h2>
<p><code>init-d-script</code> &#8211; interpreter for short and simple init.d scripts</p>
<h2>Description</h2>
<p>Generic init.d script framework to reduce the redundant code in /etc/init.d/ The goal is to create an init.d script that is Debian and LSB compliant. When the Debian policy conflicts with the LSB, the Debian policy takes precedence. </p>
<p> This is a simple example on how init-d-script can be used to start and stop a daemon with PID file support: </p>
<blockquote>
<pre>#!/bin/sh /lib/init/init-d-script
### BEGIN INIT INFO
# Provides: atd
# Required-Start: $syslog $time $remote_fs
# Required-Stop: $syslog $time $remote_fs
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: run at jobs
# Description: Debian init script to start the daemon
# running at jobs.
### END INIT INFO
DAEMON=/usr/sbin/atd</pre>
</blockquote>
<p> The following variables affect behaviour of an init script:</p>
<dl>
<dt><code>DAEMON</code></p>
<dd>Path to daemon being started. If the init script is not supposed to start any kind of daemon, it should be set to &#8220;<code>none</code> &#8221; and the functions Fn do_start_override , Fn do_stop_override and Fn do_status_override should be defined instead.</p>
<dt><code>DAEMON_ARGS</code></p>
<dd>Additional arguments, passed to daemon during start.</p>
<dt><code>DESC</code></p>
<dd>Full name or short description of the daemon, printed on screen. If unset, this variable defaults to the &#8220;<code>NAME</code> &#8221; value.</p>
<dt><code>NAME</code></p>
<dd>Additional environment variables are sourced from /etc/default/${NAME} If unset, this variable defaults to the basename of the &#8220;<code>DAEMON</code> &#8221; value.</p>
<dt><code>COMMAND_NAME</code></p>
<dd>If this variable is set, it is used as argument to the &#8211;<code>-name</code> option of start-stop-daemon8. It may be useful if the value of the &#8220;<code>NAME</code> &#8221; variable is longer than the command name length supported by the running kernel. If the value is verbatim &#8220;<code>none</code> &#8221; the command name will not be used to match the processes. If unset, this variable defaults to the &#8220;<code>NAME</code> &#8221; value.</p>
<dt><code>PIDFILE</code></p>
<dd>Path to file where the process identifier of the started daemon will be stored during start. If the value is verbatim &#8220;<code>none</code> &#8221; the process identifier will not be stored in any file. If this variable is not set, it gets a sensible default value, so it is rarely necessary to set this variable explicitly.</p>
<dt><code>RELOAD_SIGNAL</code></p>
<dd>Signal number or name (without the SIG prefix) that will be sent to the process on <code>reload</code> If the daemon performs reload action upon receiving a <code>SIGHUP</code> signal, this variable should be set to &#8220;<code>1</code> &#8221; or &#8220;<code>HUP</code> &#8221;</dl>
<p> The variables <code>RELOAD_ARGS</code> <code>START_ARGS</code> and <code>STOP_ARGS</code> are additional arguments, passed to start-stop-daemon8 during reload, start and stop actions, to override the default options. </p>
<p> Additionally, it is possible to change the behaviour of the resulting shell script by overriding some of the internal functions. To do so, define function with an <code>_override</code> suffix. So, for example, to override the Fn do_status function, one should define a Fn do_status_override function. The <i>exception</i> to this rule is the Fn do_reload function, whose override should be defined as-is, <i>without</i> the above-mentioned suffix. </p>
<p> Here is a control flow chart that explains what functions are called and when: </p>
<blockquote>
<pre>/etc/init.d/script start
 do_start
 do_start_prepare # no-op
 do_start_cmd # start-stop-daemon is called here
 do_start_cleanup # no-op
/etc/init.d/script stop
 do_stop
 do_stop_prepare # no-op
 do_stop_cmd # start-stop-daemon is called here
 do_stop_cleanup # no-op
/etc/init.d/script status
 do_status
/etc/init.d/script reload
 do_reload
 do_usage
 exit 3
/etc/init.d/script force-reload
 do_force_reload
 do_reload # if overridden
 do_restart
 do_restart_prepare
 do_stop_cmd
 do_start_cmd
 do_restart_cleanup
/etc/init.d/script restart
 do_force_restart
/etc/init.d/script try-restart
 if do_status; then
 do_restart
 do_restart_prepare
 do_stop_cmd # start-stop-daemon is called here
 do_start_cmd # start-stop-daemon is called here
 do_restart_cleanup
/etc/init.d/script &lt;arg&gt;
 do_unknown &lt;arg&gt;
 exit 3
/etc/init.d/script
 do_usage</pre>
</blockquote>
<p> As can be seen, by default, the script does not support the <code>reload</code> action; it should be implemented by the script writer by defining a Fn do_reload function. </p>
<p> If Fn do_reload is not defined but Fn do_reload_cmd is, the latter will be called on <code>reload</code> after Fn do_reload_prepare and before Fn do_reload_cleanup .</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-inittab/">inittab</a>(8), <a href="/docs/linux/man/8-service/">service</a>(8), update-rc.d8.</p>
<h2>Authors</h2>
<p>An -nosplit An Petter Reinholdtsen Aq pere [at] debian.org</p>
