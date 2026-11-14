---
title: "init(8)"
name: "init"
section: "8"
letter: "i"
url: "/docs/linux/man/8-init/"
description: "init – Upstart process management daemon"
---

<p>init &#8211; Upstart process management daemon</p>
<h2>Synopsis</h2>
<p><code>init</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p><code>init</code> is the parent of all processes on the system, it is executed by the kernel and is responsible for starting all other processes; it is the parent of all processes whose natural parents have died and it is responsible for reaping those when they die. </p>
<p> Processes managed by <code>init</code> are known as jobs and are defined by files in the <i>/etc/init</i> directory. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for more details on configuring Upstart.</p>
<h3>Events</h3>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8) is an event-based init daemon. This means that jobs will be automatically started and stopped by changes that occur to the system state, including as a result of jobs starting and stopping. </p>
<p> This is different to dependency-based init daemons which start a specified set of goal jobs, and resolve the order in which they should be started and other jobs required by iterating their dependencies. </p>
<p> For more information on starting and stopping jobs, as well as emitting events that will automatically start and stop jobs, see the manual page for the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) tool. </p>
<p> The primary event is the <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7) event, emitted when the daemon has finished loading its configuration. Other useful events are the <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7), <code><a href="/docs/linux/man/7-started/">started</a></code>(7), <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) and <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7) events emitted as jobs change state.</p>
<h3>Job States</h3>
<p><code>Table 1: Job Goals and State Transitions.</code> </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center COLSPAN=2>Goal
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>Current State </td>
<td ALIGN=center>start </td>
<td ALIGN=center> stop
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>waiting </td>
<td> starting </td>
<td> n/a
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>starting </td>
<td> pre-start </td>
<td> stopping
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>pre-start </td>
<td> spawned </td>
<td> stopping
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>spawned </td>
<td> post-start </td>
<td> stopping
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>post-start </td>
<td> running </td>
<td> stopping
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>running </td>
<td> stopping </td>
<td> pre-stop / stopping (*)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>pre-stop </td>
<td> running </td>
<td> stopping
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>stopping </td>
<td> killed </td>
<td> killed
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>killed </td>
<td> post-stop </td>
<td> post-stop
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>post-stop </td>
<td> starting </td>
<td> waiting
</td>
</tr>
</table>
</table>
<p> Key:<br />
&nbsp;<wbr>&nbsp;<wbr>(*)&nbsp;<wbr>If there is a&nbsp;<wbr><code>script</code>&nbsp;<wbr>or&nbsp;<wbr><code>exec</code>&nbsp;<wbr>section and this process is running,<br />
&nbsp;<wbr>&nbsp;<wbr>state will be&nbsp;<wbr>&#8216;pre-stop&#8217;, else it will be&nbsp;<wbr>&#8216;stopping&#8217;.</p>
<h3>Job Lifecycle</h3>
<dl>
<dt>Starting a Job</p>
<dd>
<dt>step]</p>
<dd>Initially the job is &quot;at rest&quot; with a goal of &#8216;stop&#8217; and a state of &#8216;waiting&#8217; (shown as &#8216;stop/waiting&#8217; by the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code>list</code> and <code>status</code> commands).</p>
<dt>step]</p>
<dd>The goal is changed from &#8216;stop&#8217; to &#8216;start&#8217; indicating the job is attempting to start.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;waiting&#8217; to &#8216;starting&#8217;.</p>
<dt>step]</p>
<dd>The <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7) event is emitted denoting the job is &quot;about to start&quot;.</p>
<dt>step]</p>
<dd>Any jobs whose &#8216;start on&#8217; (or &#8216;stop on&#8217;) condition would be satisfied by this job starting are started (or stopped respectively).</p>
<dt>step]</p>
<dd>The <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7) event completes.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;starting&#8217; to &#8216;pre-start&#8217;.</p>
<dt>step]</p>
<dd>If the <code>pre-start</code> stanza exists, the pre-start process is spawned.</p>
<dt>step]</p>
<dd>If the pre-start process fails, the goal is changed from &#8216;start&#8217; to &#8216;stop&#8217;, and the <code><a href="/docs/linux/man/7-stopping/">stopping</a>(7)</code> and <code><a href="/docs/linux/man/7-stopped/">stopped</a>(7)</code> events are emitted with appropriate variables set denoting the error.</p>
<dt>step]</p>
<dd>Assuming the pre-start did not fail or did not call &quot;stop&quot;, the main process is spawned.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;pre-start&#8217; to &#8216;spawned&#8217;.</p>
<dt>step]</p>
<dd>Upstart then ascertains the <i>final</i> PID for the job which may be a descendent of the immediate child process if <code>expect fork</code> or <code>expect daemon</code> has been specified.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;spawned&#8217; to &#8216;post-start&#8217;.</p>
<dt>step]</p>
<dd>If the <code>post-start</code> stanza exists, the post-start process is spawned.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;post-start&#8217; to &#8216;running&#8217;.</p>
<dt>step]</p>
<dd>The <code><a href="/docs/linux/man/7-started/">started</a></code>(7) event is emitted. </p>
<p> For services, when this event completes the main process will now be fully running. If the job refers to a task, it will now have completed (successfully or otherwise).</p>
<dt>step]</p>
<dd>Any jobs whose &#8216;start on&#8217; (or &#8216;stop on&#8217;) condition would be satisfied by this job being started are started (or stopped respectively).</p>
<dt>Stopping a Job</p>
<dd>
<dt>step]</p>
<dd>Assuming the job is fully running, it will have a goal of &#8216;start&#8217; and a state of &#8216;running&#8217; (shown as &#8216;start/running&#8217; by the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code>list</code> and <code>status</code> commands).</p>
<dt>step]</p>
<dd>The goal is changed from &#8216;start&#8217; to &#8216;stop&#8217; indicating the job is attempting to stop.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;running&#8217; to &#8216;pre-stop&#8217;.</p>
<dt>step]</p>
<dd>If the <code>pre-stop</code> stanza exists, the pre-stop process is spawned.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;pre-stop&#8217; to &#8216;stopping&#8217;.</p>
<dt>step]</p>
<dd>The <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) event is emitted.</p>
<dt>step]</p>
<dd>Any jobs whose &#8216;start on&#8217; (or &#8216;stop on&#8217;) condition would be satisfied by this job stopping are started (or stopped respectively).</p>
<dt>step]</p>
<dd>The main process is stopped:</p>
<dl>
<dd>
<dl>
<dt>step2]</p>
<dd>The signal specified by the <code>kill signal</code> stanza is sent to the process group of the main process (such that all processes belonging to the jobs main process are killed). By default this signal is <code>SIGTERM</code>. </p>
<p> See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) and <code><a href="/docs/linux/man/5-init/">init</a></code>(5).</p>
<dt>step2]</p>
<dd>Upstart waits for up to &quot;kill timeout&quot; seconds (default 5 seconds) for the process to end.</p>
<dt>step2]</p>
<dd>If the process is still running after the timeout, a <code>SIGKILL</code> signal is sent to the process which cannot be ignored and will forcibly stop the processes in the process group.</dl>
</dl>
<dt>step]</p>
<dd>The state is changed from &#8216;killed&#8217; to &#8216;post-stop&#8217;.</p>
<dt>step]</p>
<dd>If the <code>post-stop</code> stanza exists, the post-stop process is spawned.</p>
<dt>step]</p>
<dd>The state is changed from &#8216;post-stop&#8217; to &#8216;waiting&#8217;.</p>
<dt>step]</p>
<dd>The <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7) event is emitted. </p>
<p> When this event completes, the job is fully stopped.</p>
<dt>step]</p>
<dd>Any jobs whose &#8216;start on&#8217; (or &#8216;stop on&#8217;) condition would be satisfied by this job being stopped are started (or stopped respectively).</dl>
<h3>System V compatibility</h3>
<p>The Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon does not keep track of runlevels itself, instead they are implemented entirely by its userspace tools. The event emitted to signify a change of runlevel is the <code><a href="/docs/linux/man/7-runlevel/">runlevel</a></code>(7) event. For more information see its manual page.</p>
<h2>Options</h2>
<p>Options are passed to <code><a href="/docs/linux/man/8-init/">init</a></code>(8) by placing them on the kernel command-line.</p>
<dl>
<dt><code>&#8211;chroot-sessions</code></p>
<dd>Enable chroot session support. See <code>Chroot Support</code> in <code><a href="/docs/linux/man/5-init/">init</a></code>(5).</p>
<dt><code>&#8211;confdir </code><i>directory</i></p>
<dd>Read job configuration files from a directory other than the default (<i>/etc/init</i> for process ID 1). </p>
<p> When running as process ID 1, the last directory specified will be used. </p>
<p> In user session mode, multiple directories will be honoured and job configuration files loaded from the directories in the order specified.</p>
<dt><code>&#8211;default-console </code><i>value</i></p>
<dd>Default value for jobs that do not specify a &#8216;<code>console</code>&#8216; stanza. This could be used for example to set the default to &#8216;<code>none</code>&#8216; but still honour jobs that specify explicitly &#8216;<code>console log</code>&#8216;. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for all possible values of <code>console</code>.</p>
<dt><code>&#8211;no-dbus</code></p>
<dd>Do not connect to a D-Bus bus.</p>
<dt><code>&#8211;no-inherit-env</code></p>
<dd>Stop jobs from inheriting the initial environment. Only meaningful when running in user mode.</p>
<dt><code>&#8211;logdir </code><i>directory</i></p>
<dd>Write job output log files to a directory other than <i>/var/log/upstart</i> (system mode) or <i>$XDG_CACHE_HOME/upstart</i> (user session mode).</p>
<dt><code>&#8211;no-log</code></p>
<dd>Disable logging of job output. Note that jobs specifying &#8216;<code>console log</code>&#8216; will be treated as if they had specified &#8216;<code>console none</code>&#8216;. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</p>
<dt><code>&#8211;no-sessions</code></p>
<dd>Disable chroot sessions (default).</p>
<dt><code>&#8211;no-startup-event</code></p>
<dd>Suppress emission of the initial startup event. This option should only be used for testing since it will stop the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon from starting <code>any</code> jobs automatically.</p>
<dt><code>&#8211;session</code></p>
<dd>Connect to the D-Bus session bus. This should only be used for testing.</p>
<dt><code>&#8211;startup-event </code><i>event</i></p>
<dd>Specify a different initial startup event from the standard <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7)<code>.</code></p>
<dt><code>&#8211;user</code></p>
<dd>Starts in user mode, as used for user sessions. Upstart will be run as an unprivileged user, reading configuration files from configuration locations as per roughly XDG Base Directory Specification. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Reduces output messages to errors only.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Outputs verbose messages about job state changes and event emissions to the system console or log, useful for debugging boot.</p>
<dt><code>&#8211;version</code></p>
<dd>Outputs version information and exits.</dl>
<h2>Notes</h2>
<p><code>init</code> is not normally executed by a user process, and expects to have a process id of 1. If this is not the case, it will actually execute <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) and pass all arguments to that. See that manual page for further details. However, if the <code>&#8211;user</code> option is specified, it will run as a <code>Session Init</code> and read alternative configuration files and manage the individual user session in a similar fashion. </p>
<p> Sending a Session Init a <i>SIGTERM</i> signal is taken as a request to shutdown due to an impending system shutdown. In this scenario, the Session Init will emit the <code>session-end</code> event and request all running jobs stop. It will attempt to honour jobs <code>kill timeout</code> values (see <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details). Note however that system policy will prevail: if jobs request timeout values longer than the system policy allows for complete system shutdown, it will not be possible to honour them before the Session Init is killed by the system.</p>
<h2>Environment Variables</h2>
<p>When run as a user process, the following variables may be used to find job configuration files: </p>
<dl>
<dt>&bull;</p>
<dd><i>$XDG_CONFIG_HOME</i></p>
<dt>&bull;</p>
<dd><i>$XDG_CONFIG_DIRS</i></dl>
<p> See <code>User Session Mode</code> in <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</p>
<h2>Files</h2>
<p><i>/etc/init.conf</i> </p>
<p> <i>/etc/init/</i> </p>
<p> <i>$HOME/.init/</i> </p>
<p> <i>$XDG_CONFIG_DIRS/upstart/</i> </p>
<p> <i>$XDG_CONFIG_HOME/upstart/</i></p>
<h2>Author</h2>
<p>Written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt;</p>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-all-swaps/">all-swaps</a></code>(7), <code><a href="/docs/linux/man/7-control-alt-delete/">control-alt-delete</a></code>(7), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/7-dbus-event/">dbus-event</a></code>(7), <code><a href="/docs/linux/man/7-dconf-event/">dconf-event</a></code>(7), <code><a href="/docs/linux/man/7-file-event/">file-event</a></code>(7), <code><a href="/docs/linux/man/7-filesystem/">filesystem</a></code>(7), <code><a href="/docs/linux/man/5-init/">init</a></code>(5), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8), <code><a href="/docs/linux/man/7-keyboard-request/">keyboard-request</a></code>(7), <code><a href="/docs/linux/man/7-local-filesystems/">local-filesystems</a></code>(7), <code><a href="/docs/linux/man/8-mountall/">mountall</a></code>(8), <code><a href="/docs/linux/man/7-mounted/">mounted</a></code>(7), <code><a href="/docs/linux/man/7-mounting/">mounting</a></code>(7), <code><a href="/docs/linux/man/7-power-status-changed/">power-status-changed</a></code>(7), <code><a href="/docs/linux/man/7-remote-filesystems/">remote-filesystems</a></code>(7), <code><a href="/docs/linux/man/7-runlevel/">runlevel</a></code>(7), <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8), <code><a href="/docs/linux/man/7-socket-event/">socket-event</a></code>(7), <code><a href="/docs/linux/man/7-started/">started</a></code>(7), <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7), <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7), <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7), <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7), <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8), <code><a href="/docs/linux/man/8-upstart-dbus-bridge/">upstart-dbus-bridge</a></code>(8), <code><a href="/docs/linux/man/8-upstart-dconf-bridge/">upstart-dconf-bridge</a></code>(8), <code><a href="/docs/linux/man/8-upstart-event-bridge/">upstart-event-bridge</a></code>(8), <code><a href="/docs/linux/man/7-upstart-events/">upstart-events</a></code>(7), <code><a href="/docs/linux/man/8-upstart-file-bridge/">upstart-file-bridge</a></code>(8), <code><a href="/docs/linux/man/8-upstart-local-bridge/">upstart-local-bridge</a></code>(8), <code><a href="/docs/linux/man/8-upstart-socket-bridge/">upstart-socket-bridge</a></code>(8), <code><a href="/docs/linux/man/8-upstart-udev-bridge/">upstart-udev-bridge</a></code>(8), <code><a href="/docs/linux/man/7-virtual-filesystems/">virtual-filesystems</a></code>(7). </p>
