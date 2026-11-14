---
title: "systemd-kill(5)"
name: "systemd-kill"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-kill/"
description: "systemd.kill – Process killing procedure configuration"
---

<p>systemd.kill &#8211; Process killing procedure configuration</p>
<h2>Synopsis</h2>
<p><i>service</i>.service, <i>socket</i>.socket, <i>mount</i>.mount, <i>swap</i>.swap, <i>scope</i>.scope</p>
<h2>Description</h2>
<p>Unit configuration files for services, sockets, mount points, swap devices and scopes share a subset of configuration options which define the killing procedure of processes belonging to the unit. </p>
<p> This man page lists the configuration options shared by these five unit types. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options shared by all unit configuration files, and <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5) for more information on the configuration file options specific to each unit type. </p>
<p> The kill procedure configuration options are configured in the [Service], [Socket], [Mount] or [Swap] section, depending on the unit type.</p>
<h2>Options</h2>
<p><i>KillMode=</i></p>
<dl>
<dd>Specifies how processes of this unit shall be killed. One of <code>control-group</code>, <code>mixed</code>, <code>process</code>, <code>none</code>. </p>
<p> If set to <code>control-group</code>, all remaining processes in the control group of this unit will be killed on unit stop (for services: after the stop command is executed, as configured with <i>ExecStop=</i>). If set to <code>mixed</code>, the <code>SIGTERM</code> signal (see below) is sent to the main process while the subsequent <code>SIGKILL</code> signal (see below) is sent to all remaining processes of the unit&#8217;s control group. If set to <code>process</code>, only the main process itself is killed (not recommended!). If set to <code>none</code>, no process is killed (strongly recommended against!). In this case, only the stop command will be executed on unit stop, but no process will be killed otherwise. Processes remaining alive after stop are left in their control group and the control group continues to exist after stop unless empty. </p>
<p> Note that it is not recommended to set <i>KillMode=</i> to <code>process</code> or even <code>none</code>, as this allows processes to escape the service manager&#8217;s lifecycle and resource management, and to remain running even while their service is considered stopped and is assumed to not consume any resources. </p>
<p> Processes will first be terminated via <code>SIGTERM</code> (unless the signal to send is changed via <i>KillSignal=</i> or <i>RestartKillSignal=</i>). Optionally, this is immediately followed by a <code>SIGHUP</code> (if enabled with <i>SendSIGHUP=</i>). If processes still remain after the main process of a unit has exited or the delay configured via the <i>TimeoutStopSec=</i> has passed, the termination request is repeated with the <code>SIGKILL</code> signal or the signal specified via <i>FinalKillSignal=</i> (unless this is disabled via the <i>SendSIGKILL=</i> option). See <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) for more information. </p>
<p> Defaults to <code>control-group</code>.</dl>
<p> <i>KillSignal=</i></p>
<dl>
<dd>Specifies which signal to use when stopping a service. This controls the signal that is sent as first step of shutting down a unit (see above), and is usually followed by <code>SIGKILL</code> (see above and below). For a list of valid signals, see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). Defaults to <code>SIGTERM</code>. </p>
<p> Note that, right after sending the signal specified in this setting, systemd will always send <code>SIGCONT</code>, to ensure that even suspended tasks can be terminated cleanly.</dl>
<p> <i>RestartKillSignal=</i></p>
<dl>
<dd>Specifies which signal to use when restarting a service. The same as <i>KillSignal=</i> described above, with the exception that this setting is used in a restart job. Not set by default, and the value of <i>KillSignal=</i> is used.</dl>
<p> <i>SendSIGHUP=</i></p>
<dl>
<dd>Specifies whether to send <code>SIGHUP</code> to remaining processes immediately after sending the signal configured with <i>KillSignal=</i>. This is useful to indicate to shells and shell-like programs that their connection has been severed. Takes a boolean value. Defaults to &quot;no&quot;.</dl>
<p> <i>SendSIGKILL=</i></p>
<dl>
<dd>Specifies whether to send <code>SIGKILL</code> (or the signal specified by <i>FinalKillSignal=</i>) to remaining processes after a timeout, if the normal shutdown procedure left processes of the service around. When disabled, a <i>KillMode=</i> of <code>control-group</code> or <code>mixed</code> service will not restart if processes from prior services exist within the control group. Takes a boolean value. Defaults to &quot;yes&quot;.</dl>
<p> <i>FinalKillSignal=</i></p>
<dl>
<dd>Specifies which signal to send to remaining processes after a timeout if <i>SendSIGKILL=</i> is enabled. The signal configured here should be one that is not typically caught and processed by services (<code>SIGTERM</code> is not suitable). Developers can find it useful to use this to generate a coredump to troubleshoot why a service did not terminate upon receiving the initial <code>SIGTERM</code> signal. This can be achieved by configuring <i>LimitCORE=</i> and setting <i>FinalKillSignal=</i> to either <code>SIGQUIT</code> or <code>SIGABRT</code>. Defaults to <code>SIGKILL</code>.</dl>
<p> <i>WatchdogSignal=</i></p>
<dl>
<dd>Specifies which signal to use to terminate the service when the watchdog timeout expires (enabled through <i>WatchdogSec=</i>). Defaults to <code>SIGABRT</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) </p>
