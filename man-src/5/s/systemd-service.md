---
title: "systemd-service(5)"
name: "systemd-service"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-service/"
description: "systemd.service – Service unit configuration"
---

<p>systemd.service &#8211; Service unit configuration</p>
<h2>Synopsis</h2>
<p><i>service</i>.service</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.service&quot; encodes information about a process controlled and supervised by systemd. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The service specific configuration options are configured in the [Service] section. </p>
<p> Additional options are listed in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), which define the execution environment the commands are executed in, and in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), which define the way the processes of the service are terminated, and in <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), which configure resource control settings for the processes of the service. </p>
<p> If a service is requested under a certain name but no unit configuration file is found, systemd looks for a SysV init script by the same name (with the .service suffix removed) and dynamically creates a service unit from that script. This is useful for compatibility with SysV. Note that this compatibility is quite comprehensive but not 100%. For details about the incompatibilities, see the m[blue]<code>Incompatibilities with SysV</code>m[]<font SIZE="-2">[1]</font> document. </p>
<p> The <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1) command allows creating .service and .scope units dynamically and transiently from the command line.</p>
<h2>Service Templates</h2>
<p>It is possible for <code>systemd</code> services to take a single argument via the &quot;<i>service</i>@<i>argument</i>.service&quot; syntax. Such services are called &quot;instantiated&quot; services, while the unit definition without the <i>argument</i> parameter is called a &quot;template&quot;. An example could be a dhcpcd [at] .service service template which takes a network interface as a parameter to form an instantiated service. Within the service file, this parameter or &quot;instance name&quot; can be accessed with %-specifiers. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; Services with <i>Type=dbus</i> set automatically acquire dependencies of type <i>Requires=</i> and <i>After=</i> on dbus.socket.</dl>
<dl>
<dd>&bull; Socket activated services are automatically ordered after their activating .socket units via an automatic <i>After=</i> dependency. Services also pull in all .socket units listed in <i>Sockets=</i> via automatic <i>Wants=</i> and <i>After=</i> dependencies.</dl>
<p> Additional implicit dependencies may be added as result of execution and resource control parameters as documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</p>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Service units will have dependencies of type <i>Requires=</i> and <i>After=</i> on sysinit.target, a dependency of type <i>After=</i> on basic.target as well as dependencies of type <i>Conflicts=</i> and <i>Before=</i> on shutdown.target. These ensure that normal service units pull in basic system initialization, and are terminated cleanly prior to system shutdown. Only services involved with early boot or late system shutdown should disable this option.</dl>
<dl>
<dd>&bull; Instanced service units (i.e. service units with an &quot;@&quot; in their name) are assigned by default a per-template slice unit (see <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5)), named after the template unit, containing all instances of the specific template. This slice is normally stopped at shutdown, together with all template instances. If that is not desired, set <i>DefaultDependencies=no</i> in the template unit, and either define your own per-template slice unit file that also sets <i>DefaultDependencies=no</i>, or set <i>Slice=system.slice</i> (or another suitable slice) in the template unit. Also see <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5).</dl>
<h2>Options</h2>
<p>Service files must include a [Service] section, which carries information about the service and the process it supervises. A number of options that may be used in this section are shared with other unit types. These options are documented in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5). The options specific to the [Service] section of service units are the following: </p>
<p> <i>Type=</i></p>
<dl>
<dd>Configures the process start-up type for this service unit. One of <code>simple</code>, <code>exec</code>, <code>forking</code>, <code>oneshot</code>, <code>dbus</code>, <code>notify</code> or <code>idle</code>: </p>
<dl>
<dd>&bull; If set to <code>simple</code> (the default if <i>ExecStart=</i> is specified but neither <i>Type=</i> nor <i>BusName=</i> are), the service manager will consider the unit started immediately after the main service process has been forked off. It is expected that the process configured with <i>ExecStart=</i> is the main process of the service. In this mode, if the process offers functionality to other processes on the system, its communication channels should be installed before the service is started up (e.g. sockets set up by systemd, via socket activation), as the service manager will immediately proceed starting follow-up units, right after creating the main service process, and before executing the service&#8217;s binary. Note that this means <code>systemctl start</code> command lines for <code>simple</code> services will report success even if the service&#8217;s binary cannot be invoked successfully (for example because the selected <i>User=</i> doesn&#8217;t exist, or the service binary is missing).</dl>
<dl>
<dd>&bull; The <code>exec</code> type is similar to <code>simple</code>, but the service manager will consider the unit started immediately after the main service binary has been executed. The service manager will delay starting of follow-up units until that point. (Or in other words: <code>simple</code> proceeds with further jobs right after <code>fork()</code> returns, while <code>exec</code> will not proceed before both <code>fork()</code> and <code>execve()</code> in the service process succeeded.) Note that this means <code>systemctl start</code> command lines for <code>exec</code> services will report failure when the service&#8217;s binary cannot be invoked successfully (for example because the selected <i>User=</i> doesn&#8217;t exist, or the service binary is missing).</dl>
<dl>
<dd>&bull; If set to <code>forking</code>, it is expected that the process configured with <i>ExecStart=</i> will call <code>fork()</code> as part of its start-up. The parent process is expected to exit when start-up is complete and all communication channels are set up. The child continues to run as the main service process, and the service manager will consider the unit started when the parent process exits. This is the behavior of traditional UNIX services. If this setting is used, it is recommended to also use the <i>PIDFile=</i> option, so that systemd can reliably identify the main process of the service. systemd will proceed with starting follow-up units as soon as the parent process exits.</dl>
<dl>
<dd>&bull; Behavior of <code>oneshot</code> is similar to <code>simple</code>; however, the service manager will consider the unit up after the main process exits. It will then start follow-up units. <i>RemainAfterExit=</i> is particularly useful for this type of service. <i>Type=</i><code>oneshot</code> is the implied default if neither <i>Type=</i> nor <i>ExecStart=</i> are specified. Note that if this option is used without <i>RemainAfterExit=</i> the service will never enter &quot;active&quot; unit state, but directly transition from &quot;activating&quot; to &quot;deactivating&quot; or &quot;dead&quot; since no process is configured that shall run continuously. In particular this means that after a service of this type ran (and which has <i>RemainAfterExit=</i> not set) it will not show up as started afterwards, but as dead.</dl>
<dl>
<dd>&bull; Behavior of <code>dbus</code> is similar to <code>simple</code>; however, it is expected that the service acquires a name on the D-Bus bus, as configured by <i>BusName=</i>. systemd will proceed with starting follow-up units after the D-Bus bus name has been acquired. Service units with this option configured implicitly gain dependencies on the dbus.socket unit. This type is the default if <i>BusName=</i> is specified. A service unit of this type is considered to be in the activating state until the specified bus name is acquired. It is considered activated while the bus name is taken. Once the bus name is released the service is considered being no longer functional which has the effect that the service manager attempts to terminate any remaining processes belonging to the service. Services that drop their bus name as part of their shutdown logic thus should be prepared to receive a <code>SIGTERM</code> (or whichever signal is configured in <i>KillSignal=</i>) as result.</dl>
<dl>
<dd>&bull; Behavior of <code>notify</code> is similar to <code>exec</code>; however, it is expected that the service sends a notification message via <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) or an equivalent call when it has finished starting up. systemd will proceed with starting follow-up units after this notification message has been sent. If this option is used, <i>NotifyAccess=</i> (see below) should be set to open access to the notification socket provided by systemd. If <i>NotifyAccess=</i> is missing or set to <code>none</code>, it will be forcibly set to <code>main</code>.</dl>
<dl>
<dd>&bull; Behavior of <code>idle</code> is very similar to <code>simple</code>; however, actual execution of the service program is delayed until all active jobs are dispatched. This may be used to avoid interleaving of output of shell services with the status output on the console. Note that this type is useful only to improve console output, it is not useful as a general unit ordering tool, and the effect of this service type is subject to a 5s timeout, after which the service program is invoked anyway.</dl>
<p> It is generally recommended to use <i>Type=</i><code>simple</code> for long-running services whenever possible, as it is the simplest and fastest option. However, as this service type won&#8217;t propagate service start-up failures and doesn&#8217;t allow ordering of other units against completion of initialization of the service (which for example is useful if clients need to connect to the service through some form of IPC, and the IPC channel is only established by the service itself &#8212; in contrast to doing this ahead of time through socket or bus activation or similar), it might not be sufficient for many cases. If so, <code>notify</code> or <code>dbus</code> (the latter only in case the service provides a D-Bus interface) are the preferred options as they allow service program code to precisely schedule when to consider the service started up successfully and when to proceed with follow-up units. The <code>notify</code> service type requires explicit support in the service codebase (as <code>sd_notify()</code> or an equivalent API needs to be invoked by the service at the appropriate time) &#8212; if it&#8217;s not supported, then <code>forking</code> is an alternative: it supports the traditional UNIX service start-up protocol. Finally, <code>exec</code> might be an option for cases where it is enough to ensure the service binary is invoked, and where the service binary itself executes no or little initialization on its own (and its initialization is unlikely to fail). Note that using any type other than <code>simple</code> possibly delays the boot process, as the service manager needs to wait for service initialization to complete. It is hence recommended not to needlessly use any types other than <code>simple</code>. (Also note it is generally not recommended to use <code>idle</code> or <code>oneshot</code> for long-running services.)</dl>
<p> <i>RemainAfterExit=</i></p>
<dl>
<dd>Takes a boolean value that specifies whether the service shall be considered active even when all its processes exited. Defaults to <code>no</code>.</dl>
<p> <i>GuessMainPID=</i></p>
<dl>
<dd>Takes a boolean value that specifies whether systemd should try to guess the main PID of a service if it cannot be determined reliably. This option is ignored unless <code>Type=forking</code> is set and <code>PIDFile=</code> is unset because for the other types or with an explicitly configured PID file, the main PID is always known. The guessing algorithm might come to incorrect conclusions if a daemon consists of more than one process. If the main PID cannot be determined, failure detection and automatic restarting of a service will not work reliably. Defaults to <code>yes</code>.</dl>
<p> <i>PIDFile=</i></p>
<dl>
<dd>Takes a path referring to the PID file of the service. Usage of this option is recommended for services where <i>Type=</i> is set to <code>forking</code>. The path specified typically points to a file below /run/. If a relative path is specified it is hence prefixed with /run/. The service manager will read the PID of the main process of the service from this file after start-up of the service. The service manager will not write to the file configured here, although it will remove the file after the service has shut down if it still exists. The PID file does not need to be owned by a privileged user, but if it is owned by an unprivileged user additional safety restrictions are enforced: the file may not be a symlink to a file owned by a different user (neither directly nor indirectly), and the PID file must refer to a process already belonging to the service. </p>
<p> Note that PID files should be avoided in modern projects. Use <code>Type=notify</code> or <code>Type=simple</code> where possible, which does not require use of PID files to determine the main process of a service and avoids needless forking.</dl>
<p> <i>BusName=</i></p>
<dl>
<dd>Takes a D-Bus destination name that this service shall use. This option is mandatory for services where <i>Type=</i> is set to <code>dbus</code>. It is recommended to always set this property if known to make it easy to map the service name to the D-Bus destination. In particular, <code>systemctl service-log-level/service-log-target</code> verbs make use of this.</dl>
<p> <i>ExecStart=</i></p>
<dl>
<dd>Commands with their arguments that are executed when this service is started. The value is split into zero or more command lines according to the rules described below (see section &quot;Command Lines&quot; below). </p>
<p> Unless <i>Type=</i> is <code>oneshot</code>, exactly one command must be given. When <i>Type=oneshot</i> is used, zero or more commands may be specified. Commands may be specified by providing multiple command lines in the same directive, or alternatively, this directive may be specified more than once with the same effect. If the empty string is assigned to this option, the list of commands to start is reset, prior assignments of this option will have no effect. If no <i>ExecStart=</i> is specified, then the service must have <i>RemainAfterExit=yes</i> and at least one <i>ExecStop=</i> line set. (Services lacking both <i>ExecStart=</i> and <i>ExecStop=</i> are not valid.) </p>
<p> For each of the specified commands, the first argument must be either an absolute path to an executable or a simple file name without any slashes. Optionally, this filename may be prefixed with a number of special characters: </p>
<p> <code>Table 1. Special executable prefixes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Prefix </code></td>
<td><code> Effect </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;@&quot; </td>
<td> If the executable path is prefixed with &quot;@&quot;, the second specified token will be passed as &quot;argv[0]&quot; to the executed process (instead of the actual filename), followed by the further arguments specified.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;-&quot; </td>
<td> If the executable path is prefixed with &quot;-&quot;, an exit code of the command normally considered a failure (i.e. non-zero exit status or abnormal exit due to signal) is recorded, but has no further effect and is considered equivalent to success.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;:&quot; </td>
<td> If the executable path is prefixed with &quot;:&quot;, environment variable substitution (as described by the &quot;Command Lines&quot; section below) is not applied.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;+&quot; </td>
<td> If the executable path is prefixed with &quot;+&quot; then the process is executed with full privileges. In this mode privilege restrictions configured with <i>User=</i>, <i>Group=</i>, <i>CapabilityBoundingSet=</i> or the various file system namespacing options (such as <i>PrivateDevices=</i>, <i>PrivateTmp=</i>) are not applied to the invoked command line (but still affect any other <i>ExecStart=</i>, <i>ExecStop=</i>, &#8230; lines).
</td>
</tr>
<tr VALIGN=top>
<td> &quot;!&quot; </td>
<td> Similar to the &quot;+&quot; character discussed above this permits invoking command lines with elevated privileges. However, unlike &quot;+&quot; the &quot;!&quot; character exclusively alters the effect of <i>User=</i>, <i>Group=</i> and <i>SupplementaryGroups=</i>, i.e. only the stanzas that affect user and group credentials. Note that this setting may be combined with <i>DynamicUser=</i>, in which case a dynamic user/group pair is allocated before the command is invoked, but credential changing is left to the executed process itself.
</td>
</tr>
<tr VALIGN=top>
<td> &quot;!!&quot; </td>
<td> This prefix is very similar to &quot;!&quot;, however it only has an effect on systems lacking support for ambient process capabilities, i.e. without support for <i>AmbientCapabilities=</i>. It&#8217;s intended to be used for unit files that take benefit of ambient capabilities to run processes with minimal privileges wherever possible while remaining compatible with systems that lack ambient capabilities support. Note that when &quot;!!&quot; is used, and a system lacking ambient capability support is detected any configured <i>SystemCallFilter=</i> and <i>CapabilityBoundingSet=</i> stanzas are implicitly modified, in order to permit spawned processes to drop credentials and capabilities themselves, even if this is configured to not be allowed. Moreover, if this prefix is used and a system lacking ambient capability support is detected <i>AmbientCapabilities=</i> will be skipped and not be applied. On systems supporting ambient capabilities, &quot;!!&quot; has no effect and is redundant.
</td>
</tr>
</table>
<p> &quot;@&quot;, &quot;-&quot;, &quot;:&quot;, and one of &quot;+&quot;/&quot;!&quot;/&quot;!!&quot; may be used together and they can appear in any order. However, only one of &quot;+&quot;, &quot;!&quot;, &quot;!!&quot; may be used at a time. Note that these prefixes are also supported for the other command line settings, i.e. <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecReload=</i>, <i>ExecStop=</i> and <i>ExecStopPost=</i>. </p>
<p> If more than one command is specified, the commands are invoked sequentially in the order they appear in the unit file. If one of the commands fails (and is not prefixed with &quot;-&quot;), other lines are not executed, and the unit is considered failed. </p>
<p> Unless <i>Type=forking</i> is set, the process started via this command line will be considered the main process of the daemon.</dl>
<p> <i>ExecStartPre=</i>, <i>ExecStartPost=</i></p>
<dl>
<dd>Additional commands that are executed before or after the command in <i>ExecStart=</i>, respectively. Syntax is the same as for <i>ExecStart=</i>, except that multiple command lines are allowed and the commands are executed one after the other, serially. </p>
<p> If any of those commands (not prefixed with &quot;-&quot;) fail, the rest are not executed and the unit is considered failed. </p>
<p> <i>ExecStart=</i> commands are only run after all <i>ExecStartPre=</i> commands that were not prefixed with a &quot;-&quot; exit successfully. </p>
<p> <i>ExecStartPost=</i> commands are only run after the commands specified in <i>ExecStart=</i> have been invoked successfully, as determined by <i>Type=</i> (i.e. the process has been started for <i>Type=simple</i> or <i>Type=idle</i>, the last <i>ExecStart=</i> process exited successfully for <i>Type=oneshot</i>, the initial process exited successfully for <i>Type=forking</i>, &quot;READY=1&quot; is sent for <i>Type=notify</i>, or the <i>BusName=</i> has been taken for <i>Type=dbus</i>). </p>
<p> Note that <i>ExecStartPre=</i> may not be used to start long-running processes. All processes forked off by processes invoked via <i>ExecStartPre=</i> will be killed before the next service process is run. </p>
<p> Note that if any of the commands specified in <i>ExecStartPre=</i>, <i>ExecStart=</i>, or <i>ExecStartPost=</i> fail (and are not prefixed with &quot;-&quot;, see above) or time out before the service is fully up, execution continues with commands specified in <i>ExecStopPost=</i>, the commands in <i>ExecStop=</i> are skipped. </p>
<p> Note that the execution of <i>ExecStartPost=</i> is taken into account for the purpose of <i>Before=</i>/<i>After=</i> ordering constraints.</dl>
<p> <i>ExecCondition=</i></p>
<dl>
<dd>Optional commands that are executed before the command(s) in <i>ExecStartPre=</i>. Syntax is the same as for <i>ExecStart=</i>, except that multiple command lines are allowed and the commands are executed one after the other, serially. </p>
<p> The behavior is like an <i>ExecStartPre=</i> and condition check hybrid: when an <i>ExecCondition=</i> command exits with exit code 1 through 254 (inclusive), the remaining commands are skipped and the unit is <i>not</i> marked as failed. However, if an <i>ExecCondition=</i> command exits with 255 or abnormally (e.g. timeout, killed by a signal, etc.), the unit will be considered failed (and remaining commands will be skipped). Exit code of 0 or those matching <i>SuccessExitStatus=</i> will continue execution to the next command(s). </p>
<p> The same recommendations about not running long-running processes in <i>ExecStartPre=</i> also applies to <i>ExecCondition=</i>. <i>ExecCondition=</i> will also run the commands in <i>ExecStopPost=</i>, as part of stopping the service, in the case of any non-zero or abnormal exits, like the ones described above.</dl>
<p> <i>ExecReload=</i></p>
<dl>
<dd>Commands to execute to trigger a configuration reload in the service. This argument takes multiple command lines, following the same scheme as described for <i>ExecStart=</i> above. Use of this setting is optional. Specifier and environment variable substitution is supported here following the same scheme as for <i>ExecStart=</i>. </p>
<p> One additional, special environment variable is set: if known, <i>$MAINPID</i> is set to the main process of the daemon, and may be used for command lines like the following: </p>
<dl>
<dd>
<pre>ExecReload=kill -HUP $MAINPID</pre>
</dl>
<p> Note however that reloading a daemon by sending a signal (as with the example line above) is usually not a good choice, because this is an asynchronous operation and hence not suitable to order reloads of multiple services against each other. It is strongly recommended to set <i>ExecReload=</i> to a command that not only triggers a configuration reload of the daemon, but also synchronously waits for it to complete. For example, <code><a href="/docs/linux/man/1-dbus-broker/">dbus-broker</a></code>(1) uses the following: </p>
<dl>
<dd>
<pre>ExecReload=busctl call org.freedesktop.DBus \
 /org/freedesktop/DBus org.freedesktop.DBus \
 ReloadConfig</pre>
</dl>
</dl>
<p> <i>ExecStop=</i></p>
<dl>
<dd>Commands to execute to stop the service started via <i>ExecStart=</i>. This argument takes multiple command lines, following the same scheme as described for <i>ExecStart=</i> above. Use of this setting is optional. After the commands configured in this option are run, it is implied that the service is stopped, and any processes remaining for it are terminated according to the <i>KillMode=</i> setting (see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5)). If this option is not specified, the process is terminated by sending the signal specified in <i>KillSignal=</i> or <i>RestartKillSignal=</i> when service stop is requested. Specifier and environment variable substitution is supported (including <i>$MAINPID</i>, see above). </p>
<p> Note that it is usually not sufficient to specify a command for this setting that only asks the service to terminate (for example, by sending some form of termination signal to it), but does not wait for it to do so. Since the remaining processes of the services are killed according to <i>KillMode=</i> and <i>KillSignal=</i> or <i>RestartKillSignal=</i> as described above immediately after the command exited, this may not result in a clean stop. The specified command should hence be a synchronous operation, not an asynchronous one. </p>
<p> Note that the commands specified in <i>ExecStop=</i> are only executed when the service started successfully first. They are not invoked if the service was never started at all, or in case its start-up failed, for example because any of the commands specified in <i>ExecStart=</i>, <i>ExecStartPre=</i> or <i>ExecStartPost=</i> failed (and weren&#8217;t prefixed with &quot;-&quot;, see above) or timed out. Use <i>ExecStopPost=</i> to invoke commands when a service failed to start up correctly and is shut down again. Also note that the stop operation is always performed if the service started successfully, even if the processes in the service terminated on their own or were killed. The stop commands must be prepared to deal with that case. <i>$MAINPID</i> will be unset if systemd knows that the main process exited by the time the stop commands are called. </p>
<p> Service restart requests are implemented as stop operations followed by start operations. This means that <i>ExecStop=</i> and <i>ExecStopPost=</i> are executed during a service restart operation. </p>
<p> It is recommended to use this setting for commands that communicate with the service requesting clean termination. For post-mortem clean-up steps use <i>ExecStopPost=</i> instead.</dl>
<p> <i>ExecStopPost=</i></p>
<dl>
<dd>Additional commands that are executed after the service is stopped. This includes cases where the commands configured in <i>ExecStop=</i> were used, where the service does not have any <i>ExecStop=</i> defined, or where the service exited unexpectedly. This argument takes multiple command lines, following the same scheme as described for <i>ExecStart=</i>. Use of these settings is optional. Specifier and environment variable substitution is supported. Note that &#8211; unlike <i>ExecStop=</i> &#8211; commands specified with this setting are invoked when a service failed to start up correctly and is shut down again. </p>
<p> It is recommended to use this setting for clean-up operations that shall be executed even when the service failed to start up correctly. Commands configured with this setting need to be able to operate even if the service failed starting up half-way and left incompletely initialized data around. As the service&#8217;s processes have been terminated already when the commands specified with this setting are executed they should not attempt to communicate with them. </p>
<p> Note that all commands that are configured with this setting are invoked with the result code of the service, as well as the main process&#8217; exit code and status, set in the <i>$SERVICE_RESULT</i>, <i>$EXIT_CODE</i> and <i>$EXIT_STATUS</i> environment variables, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details. </p>
<p> Note that the execution of <i>ExecStopPost=</i> is taken into account for the purpose of <i>Before=</i>/<i>After=</i> ordering constraints.</dl>
<p> <i>RestartSec=</i></p>
<dl>
<dd>Configures the time to sleep before restarting a service (as configured with <i>Restart=</i>). Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Defaults to 100ms.</dl>
<p> <i>TimeoutStartSec=</i></p>
<dl>
<dd>Configures the time to wait for start-up. If a daemon service does not signal start-up completion within the configured time, the service will be considered failed and will be shut down again. The precise action depends on the <i>TimeoutStartFailureMode=</i> option. Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass &quot;infinity&quot; to disable the timeout logic. Defaults to <i>DefaultTimeoutStartSec=</i> from the manager configuration file, except when <i>Type=oneshot</i> is used, in which case the timeout is disabled by default (see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)). </p>
<p> If a service of <i>Type=notify</i> sends &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot;, this may cause the start time to be extended beyond <i>TimeoutStartSec=</i>. The first receipt of this message must occur before <i>TimeoutStartSec=</i> is exceeded, and once the start time has extended beyond <i>TimeoutStartSec=</i>, the service manager will allow the service to continue to start, provided the service repeats &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot; within the interval specified until the service startup status is finished by &quot;READY=1&quot;. (see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3)).</dl>
<p> <i>TimeoutStopSec=</i></p>
<dl>
<dd>This option serves two purposes. First, it configures the time to wait for each <i>ExecStop=</i> command. If any of them times out, subsequent <i>ExecStop=</i> commands are skipped and the service will be terminated by <code>SIGTERM</code>. If no <i>ExecStop=</i> commands are specified, the service gets the <code>SIGTERM</code> immediately. This default behavior can be changed by the <i>TimeoutStopFailureMode=</i> option. Second, it configures the time to wait for the service itself to stop. If it doesn&#8217;t terminate in the specified time, it will be forcibly terminated by <code>SIGKILL</code> (see <i>KillMode=</i> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5)). Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass &quot;infinity&quot; to disable the timeout logic. Defaults to <i>DefaultTimeoutStopSec=</i> from the manager configuration file (see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)). </p>
<p> If a service of <i>Type=notify</i> sends &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot;, this may cause the stop time to be extended beyond <i>TimeoutStopSec=</i>. The first receipt of this message must occur before <i>TimeoutStopSec=</i> is exceeded, and once the stop time has extended beyond <i>TimeoutStopSec=</i>, the service manager will allow the service to continue to stop, provided the service repeats &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot; within the interval specified, or terminates itself (see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3)).</dl>
<p> <i>TimeoutAbortSec=</i></p>
<dl>
<dd>This option configures the time to wait for the service to terminate when it was aborted due to a watchdog timeout (see <i>WatchdogSec=</i>). If the service has a short <i>TimeoutStopSec=</i> this option can be used to give the system more time to write a core dump of the service. Upon expiration the service will be forcibly terminated by <code>SIGKILL</code> (see <i>KillMode=</i> in <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5)). The core file will be truncated in this case. Use <i>TimeoutAbortSec=</i> to set a sensible timeout for the core dumping per service that is large enough to write all expected data while also being short enough to handle the service failure in due time. </p>
<p> Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;. Pass an empty value to skip the dedicated watchdog abort timeout handling and fall back <i>TimeoutStopSec=</i>. Pass &quot;infinity&quot; to disable the timeout logic. Defaults to <i>DefaultTimeoutAbortSec=</i> from the manager configuration file (see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)). </p>
<p> If a service of <i>Type=notify</i> handles <code>SIGABRT</code> itself (instead of relying on the kernel to write a core dump) it can send &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot; to extended the abort time beyond <i>TimeoutAbortSec=</i>. The first receipt of this message must occur before <i>TimeoutAbortSec=</i> is exceeded, and once the abort time has extended beyond <i>TimeoutAbortSec=</i>, the service manager will allow the service to continue to abort, provided the service repeats &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot; within the interval specified, or terminates itself (see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3)).</dl>
<p> <i>TimeoutSec=</i></p>
<dl>
<dd>A shorthand for configuring both <i>TimeoutStartSec=</i> and <i>TimeoutStopSec=</i> to the specified value.</dl>
<p> <i>TimeoutStartFailureMode=</i>, <i>TimeoutStopFailureMode=</i></p>
<dl>
<dd>These options configure the action that is taken in case a daemon service does not signal start-up within its configured <i>TimeoutStartSec=</i>, respectively if it does not stop within <i>TimeoutStopSec=</i>. Takes one of <code>terminate</code>, <code>abort</code> and <code>kill</code>. Both options default to <code>terminate</code>. </p>
<p> If <code>terminate</code> is set the service will be gracefully terminated by sending the signal specified in <i>KillSignal=</i> (defaults to <code>SIGTERM</code>, see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5)). If the service does not terminate the <i>FinalKillSignal=</i> is sent after <i>TimeoutStopSec=</i>. If <code>abort</code> is set, <i>WatchdogSignal=</i> is sent instead and <i>TimeoutAbortSec=</i> applies before sending <i>FinalKillSignal=</i>. This setting may be used to analyze services that fail to start-up or shut-down intermittently. By using <code>kill</code> the service is immediately terminated by sending <i>FinalKillSignal=</i> without any further timeout. This setting can be used to expedite the shutdown of failing services.</dl>
<p> <i>RuntimeMaxSec=</i></p>
<dl>
<dd>Configures a maximum time for the service to run. If this is used and the service has been active for longer than the specified time it is terminated and put into a failure state. Note that this setting does not have any effect on <i>Type=oneshot</i> services, as they terminate immediately after activation completed. Pass &quot;infinity&quot; (the default) to configure no runtime limit. </p>
<p> If a service of <i>Type=notify</i> sends &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot;, this may cause the runtime to be extended beyond <i>RuntimeMaxSec=</i>. The first receipt of this message must occur before <i>RuntimeMaxSec=</i> is exceeded, and once the runtime has extended beyond <i>RuntimeMaxSec=</i>, the service manager will allow the service to continue to run, provided the service repeats &quot;EXTEND_TIMEOUT_USEC=&#8230;&quot; within the interval specified until the service shutdown is achieved by &quot;STOPPING=1&quot; (or termination). (see <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3)).</dl>
<p> <i>WatchdogSec=</i></p>
<dl>
<dd>Configures the watchdog timeout for a service. The watchdog is activated when the start-up is completed. The service must call <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) regularly with &quot;WATCHDOG=1&quot; (i.e. the &quot;keep-alive ping&quot;). If the time between two such calls is larger than the configured time, then the service is placed in a failed state and it will be terminated with <code>SIGABRT</code> (or the signal specified by <i>WatchdogSignal=</i>). By setting <i>Restart=</i> to <code>on-failure</code>, <code>on-watchdog</code>, <code>on-abnormal</code> or <code>always</code>, the service will be automatically restarted. The time configured here will be passed to the executed service process in the <i>WATCHDOG_USEC=</i> environment variable. This allows daemons to automatically enable the keep-alive pinging logic if watchdog support is enabled for the service. If this option is used, <i>NotifyAccess=</i> (see below) should be set to open access to the notification socket provided by systemd. If <i>NotifyAccess=</i> is not set, it will be implicitly set to <code>main</code>. Defaults to 0, which disables this feature. The service can check whether the service manager expects watchdog keep-alive notifications. See <code><a href="/docs/linux/man/3-sd_watchdog_enabled/">sd_watchdog_enabled</a></code>(3) for details. <code><a href="/docs/linux/man/3-sd_event_set_watchdog/">sd_event_set_watchdog</a></code>(3) may be used to enable automatic watchdog notification support.</dl>
<p> <i>Restart=</i></p>
<dl>
<dd>Configures whether the service shall be restarted when the service process exits, is killed, or a timeout is reached. The service process may be the main service process, but it may also be one of the processes specified with <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecStop=</i>, <i>ExecStopPost=</i>, or <i>ExecReload=</i>. When the death of the process is a result of systemd operation (e.g. service stop or restart), the service will not be restarted. Timeouts include missing the watchdog &quot;keep-alive ping&quot; deadline and a service start, reload, and stop operation timeouts. </p>
<p> Takes one of <code>no</code>, <code>on-success</code>, <code>on-failure</code>, <code>on-abnormal</code>, <code>on-watchdog</code>, <code>on-abort</code>, or <code>always</code>. If set to <code>no</code> (the default), the service will not be restarted. If set to <code>on-success</code>, it will be restarted only when the service process exits cleanly. In this context, a clean exit means any of the following: </p>
<dl>
<dd>&bull; exit code of 0;</dl>
<dl>
<dd>&bull; for types other than <i>Type=oneshot</i>, one of the signals <code>SIGHUP</code>, <code>SIGINT</code>, <code>SIGTERM</code>, or <code>SIGPIPE</code>;</dl>
<dl>
<dd>&bull; exit statuses and signals specified in <i>SuccessExitStatus=</i>.</dl>
<p> If set to <code>on-failure</code>, the service will be restarted when the process exits with a non-zero exit code, is terminated by a signal (including on core dump, but excluding the aforementioned four signals), when an operation (such as service reload) times out, and when the configured watchdog timeout is triggered. If set to <code>on-abnormal</code>, the service will be restarted when the process is terminated by a signal (including on core dump, excluding the aforementioned four signals), when an operation times out, or when the watchdog timeout is triggered. If set to <code>on-abort</code>, the service will be restarted only if the service process exits due to an uncaught signal not specified as a clean exit status. If set to <code>on-watchdog</code>, the service will be restarted only if the watchdog timeout for the service expires. If set to <code>always</code>, the service will be restarted regardless of whether it exited cleanly or not, got terminated abnormally by a signal, or hit a timeout. </p>
<p> <code>Table 2. Exit causes and the effect of the </code><i>Restart=</i> settings </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Restart settings/Exit causes </code></td>
<td><code> <code>no</code> </code></td>
<td><code> <code>always</code> </code></td>
<td><code> <code>on-success</code> </code></td>
<td><code> <code>on-failure</code> </code></td>
<td><code> <code>on-abnormal</code> </code></td>
<td><code> <code>on-abort</code> </code></td>
<td><code> <code>on-watchdog</code> </code>
</td>
</tr>
<tr VALIGN=top>
<td> Clean exit code or signal </td>
<td> &nbsp; </td>
<td> X </td>
<td> X </td>
<td> &nbsp; </td>
<td> &nbsp; </td>
<td> &nbsp; </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td> Unclean exit code </td>
<td> &nbsp; </td>
<td> X </td>
<td> &nbsp; </td>
<td> X </td>
<td> &nbsp; </td>
<td> &nbsp; </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td> Unclean signal </td>
<td> &nbsp; </td>
<td> X </td>
<td> &nbsp; </td>
<td> X </td>
<td> X </td>
<td> X </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td> Timeout </td>
<td> &nbsp; </td>
<td> X </td>
<td> &nbsp; </td>
<td> X </td>
<td> X </td>
<td> &nbsp; </td>
<td> &nbsp;
</td>
</tr>
<tr VALIGN=top>
<td> Watchdog </td>
<td> &nbsp; </td>
<td> X </td>
<td> &nbsp; </td>
<td> X </td>
<td> X </td>
<td> &nbsp; </td>
<td> X
</td>
</tr>
</table>
<p> As exceptions to the setting above, the service will not be restarted if the exit code or signal is specified in <i>RestartPreventExitStatus=</i> (see below) or the service is stopped with <code>systemctl stop</code> or an equivalent operation. Also, the services will always be restarted if the exit code or signal is specified in <i>RestartForceExitStatus=</i> (see below). </p>
<p> Note that service restart is subject to unit start rate limiting configured with <i>StartLimitIntervalSec=</i> and <i>StartLimitBurst=</i>, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. A restarted service enters the failed state only after the start limits are reached. </p>
<p> Setting this to <code>on-failure</code> is the recommended choice for long-running services, in order to increase reliability by attempting automatic recovery from errors. For services that shall be able to terminate on their own choice (and avoid immediate restarting), <code>on-abnormal</code> is an alternative choice.</dl>
<p> <i>SuccessExitStatus=</i></p>
<dl>
<dd>Takes a list of exit status definitions that, when returned by the main service process, will be considered successful termination, in addition to the normal successful exit status 0 and, except for <i>Type=oneshot</i>, the signals <code>SIGHUP</code>, <code>SIGINT</code>, <code>SIGTERM</code>, and <code>SIGPIPE</code>. Exit status definitions can be numeric termination statuses, termination status names, or termination signal names, separated by spaces. See the Process Exit Codes section in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for a list of termination status names (for this setting only the part without the &quot;EXIT_&quot; or &quot;EX_&quot; prefix should be used). See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for a list of signal names. </p>
<p> Note that this setting does not change the mapping between numeric exit statuses and their names, i.e. regardless how this setting is used 0 will still be mapped to &quot;SUCCESS&quot; (and thus typically shown as &quot;0/SUCCESS&quot; in tool outputs) and 1 to &quot;FAILURE&quot; (and thus typically shown as &quot;1/FAILURE&quot;), and so on. It only controls what happens as effect of these exit statuses, and how it propagates to the state of the service as a whole. </p>
<p> This option may appear more than once, in which case the list of successful exit statuses is merged. If the empty string is assigned to this option, the list is reset, all prior assignments of this option will have no effect. </p>
<p> <code>Example 1. A service with the </code><i>SuccessExitStatus=</i> setting </p>
<dl>
<dd>
<pre>SuccessExitStatus=TEMPFAIL 250 SIGKILL</pre>
</dl>
<p> Exit status 75 (<code>TEMPFAIL</code>), 250, and the termination signal <code>SIGKILL</code> are considered clean service terminations. </p>
<p> Note: <code>systemd-analyze exit-status</code> may be used to list exit statuses and translate between numerical status values and names.</dl>
<p> <i>RestartPreventExitStatus=</i></p>
<dl>
<dd>Takes a list of exit status definitions that, when returned by the main service process, will prevent automatic service restarts, regardless of the restart setting configured with <i>Restart=</i>. Exit status definitions can either be numeric exit codes or termination signal names, and are separated by spaces. Defaults to the empty list, so that, by default, no exit status is excluded from the configured restart logic. For example: </p>
<dl>
<dd>
<pre>RestartPreventExitStatus=1 6 SIGABRT</pre>
</dl>
<p> ensures that exit codes 1 and 6 and the termination signal <code>SIGABRT</code> will not result in automatic service restarting. This option may appear more than once, in which case the list of restart-preventing statuses is merged. If the empty string is assigned to this option, the list is reset and all prior assignments of this option will have no effect. </p>
<p> Note that this setting has no effect on processes configured via <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecStop=</i>, <i>ExecStopPost=</i> or <i>ExecReload=</i>, but only on the main service process, i.e. either the one invoked by <i>ExecStart=</i> or (depending on <i>Type=</i>, <i>PIDFile=</i>, &#8230;) the otherwise configured main process.</dl>
<p> <i>RestartForceExitStatus=</i></p>
<dl>
<dd>Takes a list of exit status definitions that, when returned by the main service process, will force automatic service restarts, regardless of the restart setting configured with <i>Restart=</i>. The argument format is similar to <i>RestartPreventExitStatus=</i>.</dl>
<p> <i>RootDirectoryStartOnly=</i></p>
<dl>
<dd>Takes a boolean argument. If true, the root directory, as configured with the <i>RootDirectory=</i> option (see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for more information), is only applied to the process started with <i>ExecStart=</i>, and not to the various other <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecReload=</i>, <i>ExecStop=</i>, and <i>ExecStopPost=</i> commands. If false, the setting is applied to all configured commands the same way. Defaults to false.</dl>
<p> <i>NonBlocking=</i></p>
<dl>
<dd>Set the <code>O_NONBLOCK</code> flag for all file descriptors passed via socket-based activation. If true, all file descriptors &gt;= 3 (i.e. all except stdin, stdout, stderr), excluding those passed in via the file descriptor storage logic (see <i>FileDescriptorStoreMax=</i> for details), will have the <code>O_NONBLOCK</code> flag set and hence are in non-blocking mode. This option is only useful in conjunction with a socket unit, as described in <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) and has no effect on file descriptors which were previously saved in the file-descriptor store for example. Defaults to false.</dl>
<p> <i>NotifyAccess=</i></p>
<dl>
<dd>Controls access to the service status notification socket, as accessible via the <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) call. Takes one of <code>none</code> (the default), <code>main</code>, <code>exec</code> or <code>all</code>. If <code>none</code>, no daemon status updates are accepted from the service processes, all status update messages are ignored. If <code>main</code>, only service updates sent from the main process of the service are accepted. If <code>exec</code>, only service updates sent from any of the main or control processes originating from one of the <i>Exec*=</i> commands are accepted. If <code>all</code>, all services updates from all members of the service&#8217;s control group are accepted. This option should be set to open access to the notification socket when using <i>Type=notify</i> or <i>WatchdogSec=</i> (see above). If those options are used but <i>NotifyAccess=</i> is not configured, it will be implicitly set to <code>main</code>. </p>
<p> Note that <code>sd_notify()</code> notifications may be attributed to units correctly only if either the sending process is still around at the time PID 1 processes the message, or if the sending process is explicitly runtime-tracked by the service manager. The latter is the case if the service manager originally forked off the process, i.e. on all processes that match <code>main</code> or <code>exec</code>. Conversely, if an auxiliary process of the unit sends an <code>sd_notify()</code> message and immediately exits, the service manager might not be able to properly attribute the message to the unit, and thus will ignore it, even if <i>NotifyAccess=</i><code>all</code> is set for it. </p>
<p> Hence, to eliminate all race conditions involving lookup of the client&#8217;s unit and attribution of notifications to units correctly, <code>sd_notify_barrier()</code> may be used. This call acts as a synchronization point and ensures all notifications sent before this call have been picked up by the service manager when it returns successfully. Use of <code>sd_notify_barrier()</code> is needed for clients which are not invoked by the service manager, otherwise this synchronization mechanism is unnecessary for attribution of notifications to the unit.</dl>
<p> <i>Sockets=</i></p>
<dl>
<dd>Specifies the name of the socket units this service shall inherit socket file descriptors from when the service is started. Normally, it should not be necessary to use this setting, as all socket file descriptors whose unit shares the same name as the service (subject to the different unit name suffix of course) are passed to the spawned process. </p>
<p> Note that the same socket file descriptors may be passed to multiple processes simultaneously. Also note that a different service may be activated on incoming socket traffic than the one which is ultimately configured to inherit the socket file descriptors. Or, in other words: the <i>Service=</i> setting of .socket units does not have to match the inverse of the <i>Sockets=</i> setting of the .service it refers to. </p>
<p> This option may appear more than once, in which case the list of socket units is merged. Note that once set, clearing the list of sockets again (for example, by assigning the empty string to this option) is not supported.</dl>
<p> <i>FileDescriptorStoreMax=</i></p>
<dl>
<dd>Configure how many file descriptors may be stored in the service manager for the service using <code><a href="/docs/linux/man/3-sd_pid_notify_with_fds/">sd_pid_notify_with_fds</a></code>(3)&#8217;s &quot;FDSTORE=1&quot; messages. This is useful for implementing services that can restart after an explicit request or a crash without losing state. Any open sockets and other file descriptors which should not be closed during the restart may be stored this way. Application state can either be serialized to a file in /run/, or better, stored in a <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2) memory file descriptor. Defaults to 0, i.e. no file descriptors may be stored in the service manager. All file descriptors passed to the service manager from a specific service are passed back to the service&#8217;s main process on the next service restart (see <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3) for details about the precise protocol used and the order in which the file descriptors are passed). Any file descriptors passed to the service manager are automatically closed when <code>POLLHUP</code> or <code>POLLERR</code> is seen on them, or when the service is fully stopped and no job is queued or being executed for it. If this option is used, <i>NotifyAccess=</i> (see above) should be set to open access to the notification socket provided by systemd. If <i>NotifyAccess=</i> is not set, it will be implicitly set to <code>main</code>.</dl>
<p> <i>USBFunctionDescriptors=</i></p>
<dl>
<dd>Configure the location of a file containing m[blue]<code>USB FunctionFS</code>m[]<font SIZE="-2">[2]</font> descriptors, for implementation of USB gadget functions. This is used only in conjunction with a socket unit with <i>ListenUSBFunction=</i> configured. The contents of this file are written to the ep0 file after it is opened.</dl>
<p> <i>USBFunctionStrings=</i></p>
<dl>
<dd>Configure the location of a file containing USB FunctionFS strings. Behavior is similar to <i>USBFunctionDescriptors=</i> above.</dl>
<p> <i>OOMPolicy=</i></p>
<dl>
<dd>Configure the Out-Of-Memory (OOM) killer policy. On Linux, when memory becomes scarce the kernel might decide to kill a running process in order to free up memory and reduce memory pressure. This setting takes one of <code>continue</code>, <code>stop</code> or <code>kill</code>. If set to <code>continue</code> and a process of the service is killed by the kernel&#8217;s OOM killer this is logged but the service continues running. If set to <code>stop</code> the event is logged but the service is terminated cleanly by the service manager. If set to <code>kill</code> and one of the service&#8217;s processes is killed by the OOM killer the kernel is instructed to kill all remaining processes of the service, too. Defaults to the setting <i>DefaultOOMPolicy=</i> in <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5) is set to, except for services where <i>Delegate=</i> is turned on, where it defaults to <code>continue</code>. </p>
<p> Use the <i>OOMScoreAdjust=</i> setting to configure whether processes of the unit shall be considered preferred or less preferred candidates for process termination by the Linux OOM killer logic. See <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details.</dl>
<p> Check <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for more settings.</p>
<h2>Command Lines</h2>
<p>This section describes command line parsing and variable and specifier substitutions for <i>ExecStart=</i>, <i>ExecStartPre=</i>, <i>ExecStartPost=</i>, <i>ExecReload=</i>, <i>ExecStop=</i>, and <i>ExecStopPost=</i> options. </p>
<p> Multiple command lines may be concatenated in a single directive by separating them with semicolons (these semicolons must be passed as separate words). Lone semicolons may be escaped as &quot;\;&quot;. </p>
<p> Each command line is unquoted using the rules described in &quot;Quoting&quot; section in <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7). The first item becomes the command to execute, and the subsequent items the arguments. </p>
<p> This syntax is inspired by shell syntax, but only the meta-characters and expansions described in the following paragraphs are understood, and the expansion of variables is different. Specifically, redirection using &quot;&lt;&quot;, &quot;&lt;&lt;&quot;, &quot;&gt;&quot;, and &quot;&gt;&gt;&quot;, pipes using &quot;|&quot;, running programs in the background using &quot;&amp;&quot;, and <i>other elements of shell syntax are not supported</i>. </p>
<p> The command to execute may contain spaces, but control characters are not allowed. </p>
<p> The command line accepts &quot;%&quot; specifiers as described in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> Basic environment variable substitution is supported. Use &quot;${FOO}&quot; as part of a word, or as a word of its own, on the command line, in which case it will be erased and replaced by the exact value of the environment variable (if any) including all whitespace it contains, always resulting in exactly a single argument. Use &quot;$FOO&quot; as a separate word on the command line, in which case it will be replaced by the value of the environment variable split at whitespace, resulting in zero or more arguments. For this type of expansion, quotes are respected when splitting into words, and afterwards removed. </p>
<p> If the command is not a full (absolute) path, it will be resolved to a full path using a fixed search path determined at compilation time. Searched directories include /usr/local/bin/, /usr/bin/, /bin/ on systems using split /usr/bin/ and /bin/ directories, and their sbin/ counterparts on systems using split bin/ and sbin/. It is thus safe to use just the executable name in case of executables located in any of the &quot;standard&quot; directories, and an absolute path must be used in other cases. Using an absolute path is recommended to avoid ambiguity. Hint: this search path may be queried using <code>systemd-path search-binaries-default</code>. </p>
<p> Example: </p>
<dl>
<dd>
<pre>Environment=&quot;ONE=one&quot; 'TWO=two two'
ExecStart=echo $ONE $TWO ${TWO}</pre>
</dl>
<p> This will execute <code>/bin/echo</code> with four arguments: &quot;one&quot;, &quot;two&quot;, &quot;two&quot;, and &quot;two two&quot;. </p>
<p> Example: </p>
<dl>
<dd>
<pre>Environment=ONE='one' &quot;TWO='two two'&nbsp;too&quot; THREE=
ExecStart=/bin/echo ${ONE} ${TWO} ${THREE}
ExecStart=/bin/echo $ONE $TWO $THREE</pre>
</dl>
<p> This results in /bin/echo being called twice, the first time with arguments &quot;&#8217;one&#8217;&quot;, &quot;&#8217;two two&#8217;&nbsp;too&quot;, &quot;&quot;, and the second time with arguments &quot;one&quot;, &quot;two two&quot;, &quot;too&quot;. </p>
<p> To pass a literal dollar sign, use &quot;$$&quot;. Variables whose value is not known at expansion time are treated as empty strings. Note that the first argument (i.e. the program to execute) may not be a variable. </p>
<p> Variables to be used in this fashion may be defined through <i>Environment=</i> and <i>EnvironmentFile=</i>. In addition, variables listed in the section &quot;Environment variables in spawned processes&quot; in <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), which are considered &quot;static configuration&quot;, may be used (this includes e.g. <i>$USER</i>, but not <i>$TERM</i>). </p>
<p> Note that shell command lines are not directly supported. If shell command lines are to be used, they need to be passed explicitly to a shell implementation of some kind. Example: </p>
<dl>
<dd>
<pre>ExecStart=sh -c 'dmesg | tac'</pre>
</dl>
<p> Example: </p>
<dl>
<dd>
<pre>ExecStart=echo one ; echo &quot;two two&quot;</pre>
</dl>
<p> This will execute <code>echo</code> two times, each time with one argument: &quot;one&quot; and &quot;two two&quot;, respectively. Because two commands are specified, <i>Type=oneshot</i> must be used. </p>
<p> Example: </p>
<dl>
<dd>
<pre>ExecStart=echo / &gt;/dev/null &amp; \; \
ls</pre>
</dl>
<p> This will execute <code>echo</code> with five arguments: &quot;/&quot;, &quot;&gt;/dev/null&quot;, &quot;&amp;&quot;, &quot;;&quot;, and &quot;ls&quot;.</p>
<h2>Examples</h2>
<p><code>Example 2. Simple service</code> </p>
<p> The following unit file creates a service that will execute /usr/sbin/foo-daemon. Since no <i>Type=</i> is specified, the default <i>Type=</i><code>simple</code> will be assumed. systemd will assume the unit to be started immediately after the program has begun executing. </p>
<dl>
<dd>
<pre>[Unit]
Description=Foo
[Service]
ExecStart=/usr/sbin/foo-daemon
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Note that systemd assumes here that the process started by systemd will continue running until the service terminates. If the program daemonizes itself (i.e. forks), please use <i>Type=</i><code>forking</code> instead. </p>
<p> Since no <i>ExecStop=</i> was specified, systemd will send SIGTERM to all processes started from this service, and after a timeout also SIGKILL. This behavior can be modified, see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for details. </p>
<p> Note that this unit type does not include any type of notification when a service has completed initialization. For this, you should use other unit types, such as <i>Type=</i><code>notify</code> if the service understands systemd&#8217;s notification protocol, <i>Type=</i><code>forking</code> if the service can background itself or <i>Type=</i><code>dbus</code> if the unit acquires a DBus name once initialization is complete. See below. </p>
<p> <code>Example 3. Oneshot service</code> </p>
<p> Sometimes, units should just execute an action without keeping active processes, such as a filesystem check or a cleanup action on boot. For this, <i>Type=</i><code>oneshot</code> exists. Units of this type will wait until the process specified terminates and then fall back to being inactive. The following unit will perform a cleanup action: </p>
<dl>
<dd>
<pre>[Unit]
Description=Cleanup old Foo data
[Service]
Type=oneshot
ExecStart=/usr/sbin/foo-cleanup
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Note that systemd will consider the unit to be in the state &quot;starting&quot; until the program has terminated, so ordered dependencies will wait for the program to finish before starting themselves. The unit will revert to the &quot;inactive&quot; state after the execution is done, never reaching the &quot;active&quot; state. That means another request to start the unit will perform the action again. </p>
<p> <i>Type=</i><code>oneshot</code> are the only service units that may have more than one <i>ExecStart=</i> specified. For units with multiple commands (<i>Type=oneshot</i>), all commands will be run again. </p>
<p> For <i>Type=oneshot</i>, <i>Restart=</i><code>always</code> and <i>Restart=</i><code>on-success</code> are <i>not</i> allowed. </p>
<p> <code>Example 4. Stoppable oneshot service</code> </p>
<p> Similarly to the oneshot services, there are sometimes units that need to execute a program to set up something and then execute another to shut it down, but no process remains active while they are considered &quot;started&quot;. Network configuration can sometimes fall into this category. Another use case is if a oneshot service shall not be executed each time when they are pulled in as a dependency, but only the first time. </p>
<p> For this, systemd knows the setting <i>RemainAfterExit=</i><code>yes</code>, which causes systemd to consider the unit to be active if the start action exited successfully. This directive can be used with all types, but is most useful with <i>Type=</i><code>oneshot</code> and <i>Type=</i><code>simple</code>. With <i>Type=</i><code>oneshot</code>, systemd waits until the start action has completed before it considers the unit to be active, so dependencies start only after the start action has succeeded. With <i>Type=</i><code>simple</code>, dependencies will start immediately after the start action has been dispatched. The following unit provides an example for a simple static firewall. </p>
<dl>
<dd>
<pre>[Unit]
Description=Simple firewall
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/local/sbin/simple-firewall-start
ExecStop=/usr/local/sbin/simple-firewall-stop
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Since the unit is considered to be running after the start action has exited, invoking <code>systemctl start</code> on that unit again will cause no action to be taken. </p>
<p> <code>Example 5. Traditional forking services</code> </p>
<p> Many traditional daemons/services background (i.e. fork, daemonize) themselves when starting. Set <i>Type=</i><code>forking</code> in the service&#8217;s unit file to support this mode of operation. systemd will consider the service to be in the process of initialization while the original program is still running. Once it exits successfully and at least a process remains (and <i>RemainAfterExit=</i><code>no</code>), the service is considered started. </p>
<p> Often, a traditional daemon only consists of one process. Therefore, if only one process is left after the original process terminates, systemd will consider that process the main process of the service. In that case, the <i>$MAINPID</i> variable will be available in <i>ExecReload=</i>, <i>ExecStop=</i>, etc. </p>
<p> In case more than one process remains, systemd will be unable to determine the main process, so it will not assume there is one. In that case, <i>$MAINPID</i> will not expand to anything. However, if the process decides to write a traditional PID file, systemd will be able to read the main PID from there. Please set <i>PIDFile=</i> accordingly. Note that the daemon should write that file before finishing with its initialization. Otherwise, systemd might try to read the file before it exists. </p>
<p> The following example shows a simple daemon that forks and just starts one process in the background: </p>
<dl>
<dd>
<pre>[Unit]
Description=Some simple daemon
[Service]
Type=forking
ExecStart=/usr/sbin/my-simple-daemon -d
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Please see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for details on how you can influence the way systemd terminates the service. </p>
<p> <code>Example 6. DBus services</code> </p>
<p> For services that acquire a name on the DBus system bus, use <i>Type=</i><code>dbus</code> and set <i>BusName=</i> accordingly. The service should not fork (daemonize). systemd will consider the service to be initialized once the name has been acquired on the system bus. The following example shows a typical DBus service: </p>
<dl>
<dd>
<pre>[Unit]
Description=Simple DBus service
[Service]
Type=dbus
BusName=org.example.simple-dbus-service
ExecStart=/usr/sbin/simple-dbus-service
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> For <i>bus-activatable</i> services, do not include a [Install] section in the systemd service file, but use the <i>SystemdService=</i> option in the corresponding DBus service file, for example (/usr/share/dbus-1/system-services/org.example.simple-dbus-service.service): </p>
<dl>
<dd>
<pre>[D-BUS Service]
Name=org.example.simple-dbus-service
Exec=/usr/sbin/simple-dbus-service
User=root
SystemdService=simple-dbus-service.service</pre>
</dl>
<p> Please see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for details on how you can influence the way systemd terminates the service. </p>
<p> <code>Example 7. Services that notify systemd about their initialization</code> </p>
<p> <i>Type=</i><code>simple</code> services are really easy to write, but have the major disadvantage of systemd not being able to tell when initialization of the given service is complete. For this reason, systemd supports a simple notification protocol that allows daemons to make systemd aware that they are done initializing. Use <i>Type=</i><code>notify</code> for this. A typical service file for such a daemon would look like this: </p>
<dl>
<dd>
<pre>[Unit]
Description=Simple notifying service
[Service]
Type=notify
ExecStart=/usr/sbin/simple-notifying-service
[Install]
WantedBy=multi-user.target</pre>
</dl>
<p> Note that the daemon has to support systemd&#8217;s notification protocol, else systemd will think the service has not started yet and kill it after a timeout. For an example of how to update daemons to support this protocol transparently, take a look at <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3). systemd will consider the unit to be in the &#8216;starting&#8217; state until a readiness notification has arrived. </p>
<p> Please see <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5) for details on how you can influence the way systemd terminates the service.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/5-systemd-resource-control/">systemd.resource-control</a></code>(5), <code><a href="/docs/linux/man/5-systemd-kill/">systemd.kill</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Incompatibilities with SysV</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/Incompatibilities">https://www.freedesktop.org/wiki/Software/systemd/Incompatibilities</a></dl>
<dt> 2.</p>
<dd>USB FunctionFS</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/usb/functionfs.txt">https://www.kernel.org/doc/Documentation/usb/functionfs.txt</a></dl>
