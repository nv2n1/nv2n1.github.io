---
title: "initctl(8)"
name: "initctl"
section: "8"
letter: "i"
url: "/docs/linux/man/8-initctl/"
description: "initctl – init daemon control tool"
---

<p>initctl &#8211; init daemon control tool</p>
<h2>Synopsis</h2>
<p><code>initctl</code> [<i>OPTION</i>]&#8230; <i>COMMAND</i> [<i>OPTION</i>]&#8230; <i>ARG</i>&#8230;</p>
<h2>Description</h2>
<p><code>initctl</code> allows a system administrator to communicate and interact with the Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon. </p>
<p> If D-Bus has been configured to allow non-privileged users to invoke all Upstart D-Bus methods, this command is also able to manage user jobs. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details. </p>
<p> When run as <code>initctl</code>, the first non-option argument is the <i>COMMAND</i>. Global options may be specified before or after the command. </p>
<p> You may also create symbolic or hard links to <code>initctl</code> named after commands. When invoked through these links the tool will behave only as that command, with global and command-specific options intermixed. The default installation supplies such links for the <code>start</code>, <code>stop</code>, <code>restart</code>, <code>reload</code> and <code>status</code> commands.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;user</code></p>
<dd>User mode. In this mode, initctl will talk to the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon using the D-Bus private socket defined in the <code>UPSTART_SESSION</code> environment variable. </p>
<p> Note that if the <code>UPSTART_SESSION</code> variable is defined, this option is implied.</p>
<dt><code>&#8211;session</code></p>
<dd>Connect to <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon using the existing D-Bus session bus (for testing purposes only).</p>
<dt><code>&#8211;system</code></p>
<dd>Communication with the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon is normally performed over a private socket connection. This has the advantage of speed and robustness, when issuing commands to start or stop services or even reboot the system you do not want to be affected by changes to the D-Bus system bus daemon. </p>
<p> The disadvantage to using the private socket however is security, <code><a href="/docs/linux/man/8-init/">init</a></code>(8) only permits the root user to communicate over this socket which means that read-only commands such as <code>status</code> and <code>list</code> cannot be made by other users. </p>
<p> The <code>&#8211;system</code> option instructs <code>initctl</code> to communicate via the D-Bus system bus rather than over the private socket. </p>
<p> This is only possible if the system bus daemon is running and if <code><a href="/docs/linux/man/8-init/">init</a></code>(8) is connected to it. The advantage is that the default security configuration allows non-root users to use read-only commands.</p>
<dt><code>&#8211;dest</code></p>
<dd>Specifies the well-known name of the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon when using <code>&#8211;system</code>. </p>
<p> There is normally no need to use this option since the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon uses the default <code>com.ubuntu.Upstart</code> name. However it may be useful for debugging.</p>
<dt><code>&#8211;no-wait</code></p>
<dd>Applies to the <code>start</code>, <code>stop</code>, <code>restart</code> and <code>emit</code> commands. </p>
<p> Normally <code>initctl</code> will wait for the command to finish before returning. </p>
<p> For the <code>start</code>, <code>stop</code> and <code>restart</code> commands, finishing means that the named job is running (or has finished for tasks) or has been fully stopped. </p>
<p> For the <code>emit</code> command, finishing means that all of the jobs affected by the event are running (or have finished for tasks) or have been fully stopped. </p>
<p> This option instead causes these commands to only wait for the goal change or event to be queued.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Reduces output of all commands to errors only.</dl>
<h2>Commands</h2>
<dl>
<dt><code>start</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Requests that a new instance of the named <i>JOB</i> be started by changing its goal to <code>start</code>. The status of the job is displayed on standard output when the command completes. </p>
<p> See <code>status</code> for a description of the output format. </p>
<p> The optional <i>KEY=VALUE</i> arguments specify environment variables to be passed to the starting job, and placed in its environment. They also serve to specify which instance of multi-instance jobs should be started. </p>
<p> Most jobs only permit a single instance; those that use the <code>instance</code> stanza in their configuration define a string expanded from environment variables to name the instance. As many unique instances may be started as unique names may be generated by the stanza. Thus the environment variables also serve to select which instance of <i>JOB</i> is to be acted upon. </p>
<p> If the job is already running, <code>start</code> will return an error. </p>
<p> When called from the <i>pre-stop</i> stanza of a job configuration, <code>start</code> may be called without argument to cancel the <code>stop.</code></p>
<dt><code>stop</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Requests that an instance of the named <i>JOB</i> be stopped by changing its goal to <code>stop</code>. The status of the job is displayed on standard output when the command completes. </p>
<p> See <code>status</code> for a description of the output format and <code>start</code> for a discussion on instances. </p>
<p> When called from the <i>pre-start</i> stanza of a job configuration, <code>stop</code> may be called without an argument to cancel the <code>start.</code> </p>
<p> By default <code>SIGTERM</code> is sent to the job process. If it does not respond within a reasonable period, it will be forcibly stopped by sending <code>SIGKILL.</code> </p>
<p> This behaviour can be changed using the <code>kill signal</code> and <code>kill timeout</code> stanzas. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</p>
<dt><code>restart</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Requests that an instance of the named <i>JOB</i> be restarted by first changing its goal to <code>stop</code>, and then changing its goal to <code>start</code>. The status of the job is displayed on standard output when the command completes. </p>
<p> This command is <i>similar</i> to running <code>stop</code> followed by <code>start</code> with one exception: the job instance being restarted will retain its original configuration. To have the new instance run with the latest job configuration, <code>stop</code> the job and then <code>start</code> it again instead. </p>
<p> See <code>status</code> for a description of the output format and <code>start</code> for a discussion on instances. </p>
<p> Note that this command can only be used when there is an instance of <i>JOB</i>, if there is none then it returns an error instead of starting a new one.</p>
<dt><code>reload</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Sends the <i>SIGHUP</i> signal to running process of the named <i>JOB</i> instance. </p>
<p> See <code>start</code> for a discussion on instances.</p>
<dt><code>status</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Requests the status an instance of the named <i>JOB</i>, outputting to standard output. </p>
<p> See <code>start</code> for a discussion on instances. </p>
<p> For a single-instance job a line like the following is output: </p>
<pre> job start/running, process 1234</pre>
<p>The job name is given first followed by the current goal and state of the selected instance. The goal is either <i>start</i> or <i>stop</i>, the status may be one of <i>waiting</i>, <i>starting</i>, <i>pre-start</i>, <i>spawned</i>, <i>post-start</i>, <i>running</i>, <i>pre-stop</i>, <i>stopping</i>, <i>killed</i> or <i>post-stop</i>. </p>
<p> Table 1 in the <code>Job States</code> section of <code><a href="/docs/linux/man/8-init/">init</a></code>(8) summarises job goal and state transitions. </p>
<p> If the job has an active process, the process id will follow on the same line. If the state is <i>pre-start</i> or <i>post-stop</i> this will be the process id of the equivalent process, otherwise it will be the process id of the main process. </p>
<pre> job start/pre-start, process 902</pre>
<p>The <i>post-start</i> and <i>pre-stop</i> states may have multiple processes attached, the extra processes will follow on consecutive lines indented by a tab: </p>
<pre> job start/post-start, process 1234
 post-start process 1357</pre>
<p>If there is no main process, they may follow on the same line but will be prefixed to indicate that it is not the main process id being given: </p>
<pre> job start/post-start, (post-start) process 1357</pre>
<p>Jobs that permit multiple instances have names for each instance, the output is otherwise identical to the above except that the instance name follows the job name in parentheses: </p>
<pre> job (tty1) start/post-start, process 1234
 post-start process 1357</pre>
<dt><code>list</code></p>
<dd>Requests a list of the known jobs and instances, outputs the status of each to standard output. </p>
<p> Note that this command includes in the enumeration as-yet-to-run jobs (in other words configuration files for which no job instances have yet been created) in the output with status &quot;stop/waiting&quot;. In effect such entries denote configuration files which represent potential future jobs. </p>
<p> See <code>status</code> for a description of the output format and <code>start</code> for a discussion on instances. </p>
<p> No particular order is used for the output, and there is no difference in the output (other than the instance name appearing in parentheses) between single-instance and multiple-instance jobs.</p>
<dt><code>emit</code></p>
<dd><i>EVENT</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Requests that the named <i>EVENT</i> be emitted, potentially causing jobs to be started and stopped depending on their use of the <code>start on</code> and <code>stop on</code> stanzas in their configuration. </p>
<p> The optional <i>KEY=VALUE</i> arguments specify environment variables to be included with the event and thus exported into the environment of any jobs started and stopped by the event. </p>
<p> The environment may also serve to specify which instance of multi-instance jobs should be started or stopped. See <code>start</code> for a discussion on instances. </p>
<p> There is no limitation on the event names that may be emitted with this command, you are free to invent new events and use them in your job configurations. </p>
<p> The most well-known event used by the default Upstart configuration is the <code><a href="/docs/linux/man/7-runlevel/">runlevel</a></code>(7) event. This is normally emitted by the <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) and <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) tools.</p>
<dt><code>reload-configuration</code></p>
<dd>Requests that the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon reloads its configuration. </p>
<p> This command is generally not necessary since <code><a href="/docs/linux/man/8-init/">init</a></code>(8) watches its configuration directories with <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) and automatically reloads in cases of changes. </p>
<p> No jobs will be started by this command.</p>
<dt><code>version</code></p>
<dd>Requests and outputs the version of the running init daemon.</p>
<dt><code>log-priority</code></p>
<dd>[<i>PRIORITY</i>] </p>
<p> When called with a <i>PRIORITY</i> argument, it requests that the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon log all messages with that priority or greater. This may be used to both increase and decrease the volume of logged messages. </p>
<p> <i>PRIORITY</i> may be one of <i>debug</i>, <i>info</i>, <i>message</i>, <i>warn</i>, <i>error</i> or <i>fatal</i>. </p>
<p> When called without argument, it requests the current minimum message priority that the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon will log and outputs to standard output.</p>
<dt><code>show-config</code></p>
<dd>[<i>OPTIONS</i>] [<i>CONF</i>] </p>
<p> Display emits, start on and stop on job configuration details (in that order) for specified job configuration, <i>CONF</i>. If <i>CONF</i> is not specified, list information for all valid job configurations. </p>
<p> Note that a job configuration is the name of a job configuration file, without the extension. Note too that this information is static: it does not refer to any running job. </p>
<p> For each event emitted, a separate line is displayed beginning with two space characters followed by, &#8217;emits <i>event</i>&#8216; where &#8216;<i>event</i>&#8216; denotes a single emitted event. </p>
<p> The <code>start on</code> and <code>stop on</code> conditions are listed on separate lines beginning with two space characters and followed by &#8216;start on&#8217; and &#8216;stop on&#8217; respectively and ending with the appropriate condition. </p>
<p> If a job configuration has no emits, start on, or stop on conditions, the name of the job configuration will be displayed with no further details. </p>
<p> Note that the <code>start on</code> and <code>stop on</code> conditions will be fully bracketed, regardless of whether they appear like this in the job configuration file. This is useful to see how the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon perceives the condition. </p>
<p> Example output: </p>
<pre>foo
 emits boing
 emits blip
 start on (starting A and (B or C var=2)) 
 stop on (bar HELLO=world testing=123 or stopping wibble)</pre>
<p><code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-e</code>, <code>&#8211;enumerate</code></p>
<dd>If specified, rather than listing the precise <code>start on</code> and <code>stop on</code> conditions, outputs the emits lines along with one line for each event or job the <i>CONF</i> in question <i>may</i> be started or stopped by if it were to become a job. If the start on condition specifies a non-job event, this will be listed verbatim, whereas for a job event, the name of the <i>job</i> as opposed to the event the job emits will be listed. </p>
<p> The type of entity, its triggering event (if appropriate) and its full environment is displayed in brackets following its name for clarity. </p>
<p> This option is useful for tools which generate graphs of relationships between jobs and events. It is also instructive since it shows how the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon has parsed the job configuration file. </p>
<p> Example output (an analog of the default output format above): </p>
<pre>foo
 emits boing
 emits blip
 start on starting (job: A, env:)
 start on B (job:, env:)
 start on C (job:, env: var=2)
 stop on bar (job:, env: HELLO=world testing=123)
 stop on stopping (job: wibble, event: stopping, env:)</pre>
</dl>
</dl>
<dt><code>check-config</code></p>
<dd>[<i>OPTIONS</i>] [<i>CONF</i>] </p>
<p> Considers all job configurations looking for jobs that cannot be started or stopped, given the currently available job configurations. This is achieved by considering the start on, stop on and emits stanzas for each job configuration and identifying unreachable scenarios. </p>
<p> This option is useful for determining the impact of adding or removing job configuration files. </p>
<p> Note that to use this command, it is necessary to ensure that all job configuration files advertise the events they emit correctly. </p>
<p> If errors are identified, the name of the job configuration will be displayed. Subsequent lines will show the failed conditions for the job configuration, one per line. Condition lines begin with two spaces and are followed with either &quot;start on: &quot; or &quot;stop on: &quot;, the word &quot;unknown&quot;, the type of entity that is not known and finally its name. </p>
<p> Note that only job configurations that are logically in error (those with unsatisfiable conditions) will be displayed. Note too that job configurations that are syntactically invalid may trigger an error if they would cause a condition to be in error. </p>
<p> Assuming job configuration file <i>/etc/init/foo.conf</i> contains the following: </p>
<pre> start on starting grape
 stop on peach</pre>
<p>The check-config command might display: </p>
<pre> foo
 start on: unknown job grape
 stop on: unknown event peach</pre>
<p>If any errors are detected, the exit code will be 1 (one). If all checks pass, the exit code will be 0 (zero). </p>
<p> Note that for complex start on and stop on conditions, this command may give what appears to be misleading output when an error condition is found since all expressions in the failing condition that are in error will generate error output. For example, if job configuration <i>/etc/init/bar.conf</i> contains the following: </p>
<pre> start on (A and (started B or (starting C or D)))</pre>
<p>And only event A can be satisfied, the output will be: </p>
<pre> bar
 start on: unknown job B
 start on: unknown job C
 start on: unknown event D</pre>
<p><code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-i</code> <i>[EVENTS]</i>, <code>&#8211;ignore-events</code> <i>[EVENTS]</i></p>
<dd>If specified, the argument should be a list of comma-separated events to ignore when checking the job configuration files. </p>
<p> This option may be useful to ignore errors if a particular job configuration file does not advertise it emits an event. </p>
<p> Note that internal events (such as <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7) and <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7)) are automatically ignored.</p>
<dt><code>-w</code>, <code>&#8211;warn</code></p>
<dd>If specified, treat <i>any</i> unknown jobs and events as errors.</dl>
</dl>
<dt><code>notify-disk-writeable</code></p>
<dd>Notify the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon that the disk is now writeable. This currently causes the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon to flush its internal cache of &#8216;early job&#8217; output data. An early job is any job which <i>finishes</i> before the log disk becomes writeable. If job logging is not disabled, this command should be called once the log disk becomes writeable to ensure that output from all early jobs is flushed. If the data is written successfully to disk, the internal cache is deleted.</p>
<dt><code>notify-dbus-address</code></p>
<dd>Notify the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon of the D-Bus address it should use to connect to. </p>
<p> This command is only permitted when running in <code>User Session Mode.</code> See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</p>
<dt><code>list-env</code></p>
<dd>[<i>OPTIONS</i>] </p>
<p> Display a lexicographically sorted list of all variables and their values in a job environment table. </p>
<p> When run from within a job, this command will automatically query the job-specific environment table; otherwise the global environment table that is applied to all jobs when they first start is queried. </p>
<p> Note that the global job environment table comprises those variables already set in the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemons environment at startup, the minimal set of standard system variables added by the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon, and any variables set using <code>set-env</code>. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd>Operate on the global job environment table. This option is implied when not run from within a job.</dl>
</dl>
<dt><code>get-env</code></p>
<dd>[<i>OPTIONS</i>] <i>VARIABLE</i> </p>
<p> Display the value of the specified variable in a job environment table. </p>
<p> When run from within a job, this command will automatically query the job-specific environment table; otherwise the global environment table that is applied to all jobs when they first start is queried. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd>Operate on the global job environment table. This option is implied when not run from within a job.</dl>
</dl>
<dt><code>set-env</code></p>
<dd>[<i>OPTIONS</i>] <i>VARIABLE[=VALUE]</i> </p>
<p> Adds or updates a variable in a job environment table. Variables set in this way will apply to all the subsequently-starting processes for a job. </p>
<p> This command is only permitted when running in <code>User Session Mode.</code> See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-r</code>, <code>&#8211;retain</code></p>
<dd>If the specified variable is already set, do not modify it.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd>Operate on the global job environment table and all existing running job environment tables. This option is implied when not run from within a job. </p>
<p> This is an advanced option whose use is discouraged since it can change the environment of a job as it moves between different process stages (for example between <code>pre-start</code> and the main process). See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</dl>
</dl>
<dt><code>unset-env</code></p>
<dd>[<i>OPTIONS</i>] <i>VARIABLE</i> </p>
<p> Remove the specified variable from a job environment table. If the variable does not already exist in the table, no change will be made. </p>
<p> This command is only permitted when running in <code>User Session Mode.</code> See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-r</code>, <code>&#8211;retain</code></p>
<dd>If the specified variable is already set, do not modify it.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd>Operate on the global job environment table and all existing running jobenvironment tables. This option is implied when not run from within a job. </p>
<p> This is an advanced option whose use is discouraged since it can change the environment of a job as it moves between different process stages (for example between <code>pre-start</code> and the main process). See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details.</dl>
</dl>
<dt><code>reset-env</code></p>
<dd>[<i>OPTIONS</i>] </p>
<p> Discards all changes make to a job environment table, setting it back to its default set of variables and values. </p>
<p> This command is only permitted when running in <code>User Session Mode.</code> See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details. </p>
<p> Note that the effect of the Session Init process that manages the User Session Mode restarting is equivalent to this command having been called. </p>
<p> <code>OPTIONS</code></p>
<dl>
<dd>
<dl>
<dt><code>-r</code>, <code>&#8211;retain</code></p>
<dd>If the specified variable is already set, do not modify it.</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>-g</code>, <code>&#8211;global</code></p>
<dd>Operate on the global job environment table. This option is implied when not run from within a job. </p>
<p> Note that unlike <code>set-env</code> and <code>unset-env</code>, this option does not modify running job environment tables.</dl>
</dl>
<dt><code>list-sessions</code></p>
<dd>List the pid of the Session Init process followed by the value of <code>UPSTART_SESSION</code> in use for that session separted by a space character. Session files relating to non-longer running Session Init processes are considered &#8216;stale&#8217; and are not listed (although when run using <code>&#8211;verbose</code>, the full path of the stale session file is displayed).</p>
<dt><code>usage</code></p>
<dd><i>JOB</i> [<i>KEY=VALUE</i>]&#8230; </p>
<p> Show usage information for the named <i>JOB</i>. If the job specified does not define the <code>usage</code> stanza, a blank usage will be displayed. </p>
<p> Example output for a job that specifies the <code>usage</code> stanza is shown below. See <code><a href="/docs/linux/man/5-init/">init</a></code>(5) for further details of the <code>usage</code> stanza: </p>
<pre> Usage: tty DEV=ttyX - where X is console id</pre>
</dl>
<h2>Author</h2>
<p>Written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt; and James Hunt &lt;<code>james.hunt [at] canonical.com</code>&gt;<code>.</code></p>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) <code><a href="/docs/linux/man/8-shutdown/">shutdown</a></code>(8) </p>
