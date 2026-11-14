---
title: "systemd-run(1)"
name: "systemd-run"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-run/"
description: "systemd-run – Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units"
---

<h2 class="name">NAME</h2>
<p> systemd-run &#8211; Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-run</code> [OPTIONS&#8230;] <i>COMMAND</i>&nbsp;[ARGS&#8230;]</p>
<dt> <code>systemd-run</code> [OPTIONS&#8230;] [PATH OPTIONS&#8230;] {<i>COMMAND</i>} [ARGS&#8230;]</p>
<dt> <code>systemd-run</code> [OPTIONS&#8230;] [SOCKET OPTIONS&#8230;] {<i>COMMAND</i>} [ARGS&#8230;]</p>
<dt> <code>systemd-run</code> [OPTIONS&#8230;] [TIMER OPTIONS&#8230;] {<i>COMMAND</i>} [ARGS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-run</code></p>
<dd>may be used to create and start a transient .service or .scope unit and run the specified <i>COMMAND</i> in it. It may also be used to create and start a transient .path, .socket, or .timer unit, that activates a .service unit when elapsing. </p>
<p> If a command is run as transient service unit, it will be started and managed by the service manager like any other service, and thus shows up in the output of <code>systemctl list-units</code> like any other unit. It will run in a clean and detached execution environment, with the service manager as its parent process. In this mode, <code>systemd-run</code> will start the service asynchronously in the background and return after the command has begun execution (unless <code>&#8211;no-block</code> or <code>&#8211;wait</code> are specified, see below). </p>
<p> If a command is run as transient scope unit, it will be executed by <code>systemd-run</code> itself as parent process and will thus inherit the execution environment of the caller. However, the processes of the command are managed by the service manager similar to normal services, and will show up in the output of <code>systemctl list-units</code>. Execution in this case is synchronous, and will return only when the command finishes. This mode is enabled via the <code>&#8211;scope</code> switch (see below). </p>
<p> If a command is run with path, socket, or timer options such as <code>&#8211;on-calendar=</code> (see below), a transient path, socket, or timer unit is created alongside the service unit for the specified command. Only the transient path, socket, or timer unit is started immediately, the transient service unit will be triggered by the path, socket, or timer unit. If the <code>&#8211;unit=</code> option is specified, the <i>COMMAND</i> may be omitted. In this case, <code>systemd-run</code> creates only a .path, .socket, or .timer unit that triggers the specified unit. </p>
<p> By default, services created with <code>systemd-run</code> default to the <code>simple</code> type, see the description of <i>Type=</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details. Note that when this type is used the service manager (and thus the <code>systemd-run</code> command) considers service start-up successful as soon as the <code>fork()</code> for the main service process succeeded, i.e. before the <code>execve()</code> is invoked, and thus even if the specified command cannot be started. Consider using the <code>exec</code> service type (i.e. <code>&#8211;property=Type=exec</code>) to ensure that <code>systemd-run</code> returns successfully only if the specified command line has been successfully started.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;scope</code></p>
<dl>
<dt>
<dd> Create a transient .scope unit instead of the default transient .service unit (see above).</dl>
<p> <code>&#8211;unit=</code>, <code>-u</code></p>
<dl>
<dt>
<dd> Use this unit name instead of an automatically generated one.</dl>
<p> <code>&#8211;property=</code>, <code>-p</code></p>
<dl>
<dt>
<dd> Sets a property on the scope or service unit that is created. This option takes an assignment in the same format as <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>set-property</code> command.</dl>
<p> <code>&#8211;description=</code></p>
<dl>
<dt>
<dd> Provide a description for the service, scope, path, socket, or timer unit. If not specified, the command itself will be used as a description. See <i>Description=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</dl>
<p> <code>&#8211;slice=</code></p>
<dl>
<dt>
<dd> Make the new .service or .scope unit part of the specified slice, instead of system.slice (when running in <code>&#8211;system</code> mode) or the root slice (when running in <code>&#8211;user</code> mode).</dl>
<p> <code>&#8211;slice-inherit</code></p>
<dl>
<dt>
<dd> Make the new .service or .scope unit part of the inherited slice. This option can be combined with <code>&#8211;slice=</code>. </p>
<p> An inherited slice is located within <code>systemd-run</code> slice. Example: if <code>systemd-run</code> slice is foo.slice, and the <code>&#8211;slice=</code> argument is bar, the unit will be placed under the foo-bar.slice.</dl>
<p> <code>-r</code>, <code>&#8211;remain-after-exit</code></p>
<dl>
<dt>
<dd> After the service process has terminated, keep the service around until it is explicitly stopped. This is useful to collect runtime information about the service after it finished running. Also see <i>RemainAfterExit=</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5).</dl>
<p> <code>&#8211;send-sighup</code></p>
<dl>
<dt>
<dd> When terminating the scope or service unit, send a SIGHUP immediately after SIGTERM. This is useful to indicate to shells and shell-like processes that the connection has been severed. Also see <i>SendSIGHUP=</i> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5).</dl>
<p> <code>&#8211;service-type=</code></p>
<dl>
<dt>
<dd> Sets the service type. Also see <i>Type=</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5). This option has no effect in conjunction with <code>&#8211;scope</code>. Defaults to <code>simple</code>.</dl>
<p> <code>&#8211;uid=</code>, <code>&#8211;gid=</code></p>
<dl>
<dt>
<dd> Runs the service process under the specified UNIX user and group. Also see <i>User=</i> and <i>Group=</i> in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <code>&#8211;nice=</code></p>
<dl>
<dt>
<dd> Runs the service process with the specified nice level. Also see <i>Nice=</i> in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <code>&#8211;working-directory=</code></p>
<dl>
<dt>
<dd> Runs the service process with the specified working directory. Also see <i>WorkingDirectory=</i> in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <code>&#8211;same-dir</code>, <code>-d</code></p>
<dl>
<dt>
<dd> Similar to <code>&#8211;working-directory=</code> but uses the current working directory of the caller for the service to execute.</dl>
<p> <code>-E </code><i>NAME</i><code>=</code><i>VALUE</i>, <code>&#8211;setenv=</code><i>NAME</i><code>=</code><i>VALUE</i></p>
<dl>
<dt>
<dd> Runs the service process with the specified environment variable set. Also see <i>Environment=</i> in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5).</dl>
<p> <code>&#8211;pty</code>, <code>-t</code></p>
<dl>
<dt>
<dd> When invoking the command, the transient service connects its standard input, output and error to the terminal <code>systemd-run</code> is invoked on, via a pseudo TTY device. This allows running programs that expect interactive user input/output as services, such as interactive command shells. </p>
<p> Note that <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1)&#8217;s <code>shell</code> command is usually a better alternative for requesting a new, interactive login session on the local host or a local container. </p>
<p> See below for details on how this switch combines with <code>&#8211;pipe</code>.</dl>
<p> <code>&#8211;pipe</code>, <code>-P</code></p>
<dl>
<dt>
<dd> If specified, standard input, output, and error of the transient service are inherited from the <code>systemd-run</code> command itself. This allows <code>systemd-run</code> to be used within shell pipelines. Note that this mode is not suitable for interactive command shells and similar, as the service process will not become a TTY controller when invoked on a terminal. Use <code>&#8211;pty</code> instead in that case. </p>
<p> When both <code>&#8211;pipe</code> and <code>&#8211;pty</code> are used in combination the more appropriate option is automatically determined and used. Specifically, when invoked with standard input, output and error connected to a TTY <code>&#8211;pty</code> is used, and otherwise <code>&#8211;pipe</code>. </p>
<p> When this option is used the original file descriptors <code>systemd-run</code> receives are passed to the service processes as-is. If the service runs with different privileges than <code>systemd-run</code>, this means the service might not be able to re-open the passed file descriptors, due to normal file descriptor access restrictions. If the invoked process is a shell script that uses the <code>echo &quot;hello&quot; &gt; /dev/stderr</code> construct for writing messages to stderr, this might cause problems, as this only works if stderr can be re-opened. To mitigate this use the construct <code>echo &quot;hello&quot; &gt;&amp;2</code> instead, which is mostly equivalent and avoids this pitfall.</dl>
<p> <code>&#8211;shell</code>, <code>-S</code></p>
<dl>
<dt>
<dd> A shortcut for &quot;&#8211;pty &#8211;same-dir &#8211;wait &#8211;collect &#8211;service-type=exec $SHELL&quot;, i.e. requests an interactive shell in the current working directory, running in service context, accessible with a single switch.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dt>
<dd> Suppresses additional informational output while running. This is particularly useful in combination with <code>&#8211;pty</code> when it will suppress the initial message explaining how to terminate the TTY connection.</dl>
<p> <code>&#8211;on-active=</code>, <code>&#8211;on-boot=</code>, <code>&#8211;on-startup=</code>, <code>&#8211;on-unit-active=</code>, <code>&#8211;on-unit-inactive=</code></p>
<dl>
<dt>
<dd> Defines a monotonic timer relative to different starting points for starting the specified command. See <i>OnActiveSec=</i>, <i>OnBootSec=</i>, <i>OnStartupSec=</i>, <i>OnUnitActiveSec=</i> and <i>OnUnitInactiveSec=</i> in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5) for details. These options are shortcuts for <code>&#8211;timer-property=</code> with the relevant properties. These options may not be combined with <code>&#8211;scope</code> or <code>&#8211;pty</code>.</dl>
<p> <code>&#8211;on-calendar=</code></p>
<dl>
<dt>
<dd> Defines a calendar timer for starting the specified command. See <i>OnCalendar=</i> in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5). This option is a shortcut for <code>&#8211;timer-property=OnCalendar=</code>. This option may not be combined with <code>&#8211;scope</code> or <code>&#8211;pty</code>.</dl>
<p> <code>&#8211;on-clock-change</code>, <code>&#8211;on-timezone-change</code></p>
<dl>
<dt>
<dd> Defines a trigger based on system clock jumps or timezone changes for starting the specified command. See <i>OnClockChange=</i> and <i>OnTimezoneChange=</i> in <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5). These options are shortcuts for <code>&#8211;timer-property=OnClockChange=yes</code> and <code>&#8211;timer-property=OnTimezoneChange=yes</code>. These options may not be combined with <code>&#8211;scope</code> or <code>&#8211;pty</code>.</dl>
<p> <code>&#8211;path-property=</code>, <code>&#8211;socket-property=</code>, <code>&#8211;timer-property=</code></p>
<dl>
<dt>
<dd> Sets a property on the path, socket, or timer unit that is created. This option is similar to <code>&#8211;property=</code> but applies to the transient path, socket, or timer unit rather than the transient service unit created. This option takes an assignment in the same format as <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1)&#8217;s <code>set-property</code> command. These options may not be combined with <code>&#8211;scope</code> or <code>&#8211;pty</code>.</dl>
<p> <code>&#8211;no-block</code></p>
<dl>
<dt>
<dd> Do not synchronously wait for the unit start operation to finish. If this option is not specified, the start request for the transient unit will be verified, enqueued and <code>systemd-run</code> will wait until the unit&#8217;s start-up is completed. By passing this argument, it is only verified and enqueued. This option may not be combined with <code>&#8211;wait</code>.</dl>
<p> <code>&#8211;wait</code></p>
<dl>
<dt>
<dd> Synchronously wait for the transient service to terminate. If this option is specified, the start request for the transient unit is verified, enqueued, and waited for. Subsequently the invoked unit is monitored, and it is waited until it is deactivated again (most likely because the specified command completed). On exit, terse information about the unit&#8217;s runtime is shown, including total runtime (as well as CPU usage, if <code>&#8211;property=CPUAccounting=1</code> was set) and the exit code and status of the main process. This output may be suppressed with <code>&#8211;quiet</code>. This option may not be combined with <code>&#8211;no-block</code>, <code>&#8211;scope</code> or the various path, socket, or timer options.</dl>
<p> <code>-G</code>, <code>&#8211;collect</code></p>
<dl>
<dt>
<dd> Unload the transient unit after it completed, even if it failed. Normally, without this option, all units that ran and failed are kept in memory until the user explicitly resets their failure state with <code>systemctl reset-failed</code> or an equivalent command. On the other hand, units that ran successfully are unloaded immediately. If this option is turned on the &quot;garbage collection&quot; of units is more aggressive, and unloads units regardless if they exited successfully or failed. This option is a shortcut for <code>&#8211;property=CollectMode=inactive-or-failed</code>, see the explanation for <i>CollectMode=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for further information.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the calling user, rather than the service manager of the system.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Talk to the service manager of the system. This is the implied default.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> All command line arguments after the first non-option argument become part of the command line of the launched process. If a command is run as service unit, the first argument needs to be an absolute program path.</p>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned. If <code>systemd-run</code> failed to start the service, a non-zero return value will be returned. If <code>systemd-run</code> waits for the service to terminate, the return value will be propagated from the service. 0 will be returned on success, including all the cases where systemd considers a service to have exited cleanly, see the discussion of <i>SuccessExitStatus=</i> in <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5).</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Logging environment variables provided by systemd to services</code> </p>
<dl>
<dt>
<dd>
<pre><code>
#systemd - run env
Running as unit : run - 19945.service
#journalctl - u run - 19945.service
                            Sep 08 07 : 37 : 21 bupkis systemd[1] : Starting /
                                                                    usr / bin / env... Sep 08 07 : 37 : 21 bupkis systemd[1] : Started / usr / bin / env.Sep 08 07 : 37 : 21 bupkis env[19948] : PATH = / usr / local / sbin : / usr / local / bin : / usr / sbin : / usr / bin Sep 08 07 : 37 : 21 bupkis env[19948] : LANG = en_US.UTF - 8 Sep 08 07 : 37 : 21 bupkis env[19948] : BOOT_IMAGE = / vmlinuz - 3.11.0 - 0.rc5.git6.2.fc20.x86_64
</code></pre>
</dl>
<p> <code>Example 2. Limiting resources available to a command</code> </p>
<dl>
<dt>
<dd>
<pre>
# systemd-run -p BlockIOWeight=10 updatedb
</pre>
</dl>
<p> This command invokes the <code><a href="/docs/linux/man/8-updatedb/">updatedb</a></code>(8) tool, but lowers the block I/O weight for it to 10. See <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5) for more information on the <i>BlockIOWeight=</i> property. </p>
<p> <code>Example 3. Running commands at a specified time</code> </p>
<p> The following command will touch a file after 30 seconds. </p>
<dl>
<dt>
<dd>
#date; systemd &#8211; run&#8211; on &#8211; active = 30 &#8211;timer &#8211; property = AccuracySec = 100ms / bin / touch / tmp / foo<br />
Mon Dec 8 20 : 44 : 24 KST 2014 Running as unit : run &#8211; 71.timer Will run service as unit : run &#8211; 71.service<br />
#journalctl &#8211; b &#8211; u run &#8211; 71.timer<br />
                                                                                            &#8211;Journal begins at Fri 2014 &#8211;<br />
                                                                                            12 &#8211; 05 19 : 09 : 21 KST,<br />
    ends at Mon 2014 &#8211; 12 &#8211; 08 20 : 44 : 54 KST.&#8211;Dec 08 20 : 44 : 38 container systemd[1] : Starting / bin / touch / tmp / foo.Dec 08 20 : 44 : 38 container systemd[1] : Started / bin / touch / tmp / foo.<br />
#journalctl &#8211; b &#8211; u run &#8211; 71.service<br />
                                                                                                                                                                                                         &#8211;Journal begins at Fri 2014 &#8211;<br />
        12 &#8211; 05 19 : 09 : 21 KST,<br />
    ends at Mon 2014 &#8211; 12 &#8211; 08 20 : 44 : 54 KST.&#8211;Dec 08 20 : 44 : 48 container systemd[1] : Starting / bin / touch / tmp / foo&#8230; Dec 08 20 : 44 : 48 container systemd[1] : Started / bin / touch / tmp / foo.
</dl>
<p> <code>Example 4. Allowing access to the tty</code> </p>
<p> The following command invokes /bin/bash as a service passing its standard input, output and error to the calling TTY. </p>
<dl>
<dt>
<dd>
<pre>
# systemd-run -t --send-sighup /bin/bash
</pre>
</dl>
<p> <code>Example 5. Start screen as a user service</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-run --scope --user screen
Running scope as unit run-r14b0047ab6df45bfb45e7786cc839e76.scope.
$ screen -ls
There is a screen on:
        492..laptop     (Detached)
1 Socket in /var/run/screen/S-fatima.
</pre>
</dl>
<p> This starts the <code>screen</code> process as a child of the <code>systemd &#8211;user</code> process that was started by user [at] .service, in a scope unit. A <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5) unit is used instead of a <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) unit, because <code>screen</code> will exit when detaching from the terminal, and a service unit would be terminated. Running <code>screen</code> as a user unit has the advantage that it is not part of the session scope. If <i>KillUserProcesses=yes</i> is configured in <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5), the default, the session scope will be terminated when the user logs out of that session. </p>
<p> The user [at] .service is started automatically when the user first logs in, and stays around as long as at least one login session is open. After the user logs out of the last session, user [at] .service and all services underneath it are terminated. This behavior is the default, when &quot;lingering&quot; is not enabled for that user. Enabling lingering means that user [at] .service is started automatically during boot, even if the user is not logged in, and that the service is not terminated when the user logs out. </p>
<p> Enabling lingering allows the user to run processes without being logged in, for example to allow <code>screen</code> to persist after the user logs out, even if the session scope is terminated. In the default configuration, users can enable lingering for themselves: </p>
<dl>
<dt>
<dd>
<pre>
$ loginctl enable-linger
</pre>
</dl>
<p> <code>Example 6. Return value</code> </p>
<dl>
<dt>
<dd>
<pre><code>
$ systemd - run-- user-- wait true $ systemd - run-- user-- wait - p SuccessExitStatus = 11 bash - c 'exit 11' $ systemd - run-- user-- wait - p SuccessExitStatus = SIGUSR1 bash - c 'kill -SIGUSR1 $$$$'
</code></pre>
</dl>
<p> Those three invocations will succeed, i.e. terminate with an exit code of 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/1-systemd-mount/">systemd-mount</a></code>(1), <code><a href="/docs/linux/man/1-machinectl/">machinectl</a></code>(1) </p>
<h2>Index</h2>
