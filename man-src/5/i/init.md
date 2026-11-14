---
title: "init(5)"
name: "init"
section: "5"
letter: "i"
url: "/docs/linux/man/5-init/"
description: "init – Upstart init daemon job configuration"
---

<p>init &#8211; Upstart init daemon job configuration</p>
<h2>Synopsis</h2>
<dl>
<dt><code>/etc/init/</code></p>
<dd>Default location of system job configuration files.</p>
<dt><code>$XDG_CONFIG_HOME/upstart/, $XDG_CONFIG_DIRS/upstart/</code></p>
<dd>Default locations of user session job configuration files.</p>
<dt><code>$HOME/.init/</code></p>
<dd>Deprecated location of user job configuration files (still honoured by User Session Mode).</dl>
<h2>Description</h2>
<p>On startup, the Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon reads its job configuration from files in the <i>/etc/init/</i> directory, and watches for future changes to these files using <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7). If Upstart was invoked as a user process with &#8211;user option, it will run in User Session mode. See <code>User Session Mode</code> for further details. To be considered by Upstart, files in this directory must have a recognized suffix and may also be present in sub-directories. There are two recognized suffixes:</p>
<dl>
<dt>&bull;</p>
<dd>Files ending in <i>.conf</i> are called configuration files, or simply &quot;conf files&quot; for short. These are the primary vehicle for specifying a job.</p>
<dt>&bull;</p>
<dd>Files ending in <i>.override</i> are called override files. If an override file is present, the stanzas it contains take precedence over those equivalently named stanzas in the corresponding configuration file contents for a particular job. The main use for override files is to modify how a job will run without having to modify its configuration file directly. See the section <code>Override File Handling</code> below for further details.</dl>
<p> A job can thus be defined by either:</p>
<dl>
<dt>&bull;</p>
<dd>A single configuration file.</p>
<dt>&bull;</p>
<dd>A single configuration file <code>and</code> a single override file.</dl>
<p> Unless explicitly stated otherwise, any reference to a jobs configuration can refer both to a configuration file or an override file. Each configuration file defines the template for a single <i>service</i> (long-running process or daemon) or <i>task</i> (short-lived process). Note that a configuration file is not itself a job: it is a description of an environment a job could be run in. A job is the runtime embodiment of a configuration file. The configuration file name as displayed by Upstart and associated tooling is taken from its relative path within the directory without the extension. For example a configuration file <i>/etc/init/rc-sysinit.conf</i> is named <i>rc-sysinit</i>, while a configuration file <i>/etc/init/net/apache.conf</i> is named <i>net/apache</i>. Since override files only modify the way a configuration file is interpreted, they are not named. Configuration files are plain text and should not be executable.</p>
<h3>Chroot Support</h3>
<p>Upstart is able to manage jobs within a <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2). To control jobs within the chroot environment, use the standard <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) facility. Note that it is not necessary to install D-Bus within the chroot (in fact it is not recommended). Note that this facility is distinct from the <code>chroot</code> stanza (see <code>Process environment</code> below).</p>
<h3>User Session Mode</h3>
<p>Upstart can manage complete User Sessions. In this mode it runs with a process id greater than 1 and will read job configuration files from the following list of directories in the order shown:</p>
<dl>
<dt>&bull;</p>
<dd><i>$XDG_CONFIG_HOME/upstart/</i></p>
<dt>&bull;</p>
<dd><i>$HOME/.init/</i></p>
<dt>&bull;</p>
<dd><i>$XDG_CONFIG_DIRS/upstart/</i></p>
<dt>&bull;</p>
<dd><i>/usr/share/upstart/sessions/</i></dl>
<p> Note that the first directory to contain a job is considered the owner of that job name: any subsequently searched directory that contains a job of the same name will be ignored. The same applies for override files: only the first override file found in the search order will be applied. Note that an override file can be in the same directory or earlier to that directory which contains the job file. Jobs in these locations are expected to launch the user&#8217;s session. Upstart will try to parent all spawned process with the aid of <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). If successful this will ensure that even double-forking daemons will be reparented to the User Session process, and not to the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon running with process id 1. When running in User Session mode, Upstart will kill all job processes on session logout or shutdown. All log output will be in <i>$XDG_CACHE_HOME/upstart</i> which defaults to <i>$HOME/.cache/upstart</i></p>
<h3>Configuration File Format</h3>
<p>Each line begins with a configuration stanza and continues until either the end of the line or a line containing a closing stanza. Line breaks within a stanza are permitted within single or double quotes, or if preceded by a blackslash. If a stanza is duplicated, the last occurence will be used. Unrecognized stanzas will generate parse errors, which will stop a job from running. Stanzas and their arguments are delimited by whitespace, which consists of one or more space or tab characters which are otherwise ignored unless placed within single or double quotes. Comments begin with a `#&#8217; and continue until the end of the line. Blank lines and lines consisting only of whitespace or comments are ignored.</p>
<h3>Process definition</h3>
<p>The primary use of jobs is to define services or tasks to be run by the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon. Each job may have one or more different processes run as part of its lifecycle, with the most common known as the main process. The main process is defined using either the <code>exec</code> or <code>script</code> stanzas, only one of which is permitted. These specify the executable or shell script that will be run when the job is considered to be running. Once this process terminates, the job stops. All processes are run with the full job environment available as environment variables in their process.</p>
<dl>
<dt><code>exec </code><i>COMMAND </i>[ <i>ARG </i>]&#8230;</p>
<dd>This stanza defines the process to be run as the name of an executable on the filesystem, and zero or more arguments to be passed to it. Any special characters, e.g. quotes or `$&#8217; specified will result in the entire command being passed to a shell for expansion. </p>
<pre>exec /usr/sbin/acpid -c $EVENTSDIR -s $SOCKET</pre>
<dt><code>script </code>&#8230; <code>end script</code></p>
<dd>This stanza defines the process to be run as a shell script that will be executed using <code><a href="/docs/linux/man/1-sh/">sh</a>(1).</code> The <i>-e</i> shell option is always used, so any command that fails will terminate the script. The <code>script</code> stanza appears on its own on a line, the script is everything up until the first <code>end script</code> stanza appearing on its own on a line. </p>
<pre>script
 dd bs=1 if=/proc/kmsg of=$KMSGSINK
 exec /sbin/klogd -P $KMSGSINK
end script</pre>
<p> There are an additional four processes that may be run as part of the job&#8217;s lifecycle. These are specified as the process name, followed by an <code>exec</code> or <code>script</code> stanza.</p>
<dl>
<dt><code>pre-start exec</code>|<code>script</code>&#8230;</p>
<dd>This process will be run after the job&#8217;s <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7) event has finished, but before the main process is run. It is typically used to prepare the environment, such as making necessary directories, and it may also call the <code><a href="/docs/linux/man/8-stop/">stop</a></code>(8) command without arguments to cancel the start.</p>
<dt><code>post-start exec</code>|<code>script</code>&#8230;</p>
<dd>This process will be run before the job&#8217;s <code><a href="/docs/linux/man/7-started/">started</a></code>(7) event is emitted, but after the main process has been spawned. It is typically used to send necessary commands to the main process, or to delay the <code><a href="/docs/linux/man/7-started/">started</a></code>(7) event until the main process is ready to receive clients.</p>
<dt><code>pre-stop exec</code>|<code>script</code>&#8230;</p>
<dd>This process is run if the job is stopped by an event listed in its <code>stop on</code> stanza or by the <code><a href="/docs/linux/man/8-stop/">stop</a></code>(8) command. It will be run before the job&#8217;s <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) event is emitted and before the main process is killed. It is typically used to send any necessary shutdown commands to the main process, and it may also call the <code><a href="/docs/linux/man/8-start/">start</a></code>(8) command without arguments to cancel the stop.</p>
<dt><code>post-stop exec</code>|<code>script</code>&#8230;</p>
<dd>This process is run after the main process has been killed and before the job&#8217;s <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7) event is emitted. It is typically used to clean up the environment, such as removing temporary directories.  All of these processes, including the main process, are optional. Services without a main process will appear to be running until they are stopped: this is commonly used to define states such as runlevels. It is permissible to have no main process, but to have <code>pre-start</code> and <code>post-stop</code> processes for the state.</p>
<dl>
<dd>
<pre>pre-start exec ifup -a
post-stop exec ifdown -a</pre>
</dl>
<h3>Event definition</h3>
<p>Jobs can be manually started and stopped at any time by a system administrator using the <code><a href="/docs/linux/man/8-start/">start</a></code>(8) and <code><a href="/docs/linux/man/8-stop/">stop</a></code>(8) tools, however it is far more useful for jobs to be started and stopped automatically by the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon when necessary. This is done by specifying which events should cause your job to be started, and which cause your process to be stopped again. The set of possible events is limitless, however there are a number of standard events defined by the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon and <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) tools that you will want to use. When first started, the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon will emit the <code><a href="/docs/linux/man/7-startup/">startup</a></code>(7) event. This will activate jobs that implement System V compatibility and the <code><a href="/docs/linux/man/7-runlevel/">runlevel</a></code>(7) event. As jobs are started and stopped, the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon will emit the <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7), <code><a href="/docs/linux/man/7-started/">started</a></code>(7), <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) and <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7) events on their behalf.</p>
<dl>
<dt><code>start on </code><i>EVENT </i>[[<i>KEY=</i>]<i>VALUE</i>]&#8230; [<code>and</code>|<code>or</code>&#8230;]</p>
<dd>The <code>start on</code> stanza defines the set of events that will cause the job to be automatically started. Each <i>EVENT</i> is given by its name. Multiple events are permitted using the <code>and</code> &amp; <code>or</code> logical operators, and complex expressions may be performed with parentheses (within which line breaks are permitted). You may also match on the environment variables contained within the event by specifying the <i>KEY</i> and expected <i>VALUE</i>. If you know the order in which the variables are given to the event you may omit the <i>KEY</i>. <i>VALUE</i> may contain wildcard matches and globs as permitted by <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3) and may expand the value of any variable defined with the <code>env</code> stanza. Negation is permitted by using <i>!=</i> between the <i>KEY</i> and <i>VALUE</i>. If an event is emitted for which no jobs have registered interest (via either <code>start on</code> or <code>stop on</code>), the event is destroyed. If a job specifies a single event in its start condition and that event is emitted and matches any specifies event environment variables, the overall condition becomes true, the job is started and &#8212; assuming no other job has registered an interest in it &#8212; the event is destroyed. However, if an event is emitted which matches <i>part</i> of a jobs start condition, the job is said to be blocking the event (since the event is unable to change state until the job has started) and will both cause the event to persist and the job start condition to be marked as partially completed. Once all events in the start condition have been emitted, the overall job start condition becomes true and the job will be started. If no other jobs have registered interest in the events in the start condition, they will then be destroyed. Note that no job processes are started until the overall expression evaluates to true. Note that if a new job is created which specifies that it starts on one or more events <i>that have already been destroyed</i>, that job will not start automatically until those events are emitted again. Depending on the event, this may not happen until the next time the system is booted. Although complex expressions are supported, it should be possible to specify the start condition for the majority of jobs with very simple expressions (between one and four events as a very approximate guide). A large number or complex combination of events is often an indication that the condition should be refactored. Examples of <code>start on</code> conditions: </p>
<pre>start on started gdm or started kdm
start on stopped JOB=foo RESULT=failed PROCESS=pre-start
start on device-added SUBSYSTEM=tty DEVPATH=ttyS*
start on net-device-added INTERFACE!=lo
start on (A and B C=D and E F=G)</pre>
<dt><code>stop on </code><i>EVENT </i>[[<i>KEY=</i>]<i>VALUE</i>]&#8230; [<code>and</code>|<code>or</code>&#8230;]</p>
<dd>The <code>stop on</code> stanza defines the set of events that will cause the job to be automatically stopped. It has the same syntax as <code>start on</code>. <i>VALUE</i> may additionally expand the value of any variable that came from the job&#8217;s start environment (either the event or the command that started it). Examples of <code>stop on</code> conditions: </p>
<pre>stop on A
stop on starting B and stopped JOB=C
stop on stopping gdm or stopping kdm
stop on device-removed DEVPATH=$DEVPATH</pre>
<dt><code>manual</code></p>
<dd>This stanza will disregard any <i>previously seen</i> <code>start on</code> definition. By adding this stanza on any line below the <code>start on</code> definition, it provides the ability to stop a job from being automatically started. When specified, the only way to start such a job is via <code>start</code> (8).</dl>
<h3>Job environment</h3>
<p>Each job is run with an environment constructed from the following categories:</p>
<dl>
<dt>&bull;</p>
<dd>A minimal set of standard system variables added by Upstart. All jobs contain the <code>TERM</code> and <code>PATH</code> variables.</p>
<dt>&bull;</p>
<dd>Variables set using the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) job environment commands (such as <i>set-env</i>). These commands also allow unsetting of variables.</p>
<dt>&bull;</p>
<dd>A set of special variables added by Upstart that relate to the job itself. All jobs also contain the <code>UPSTART_JOB</code> and <code>UPSTART_INSTANCE</code> environment variables, containing the name of the job and instance. These are mostly used by the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) utility to default to acting on the job the commands are called from.</p>
<dt>&bull;</p>
<dd>Those variables introduced by the events or command that started the job. The special <code>UPSTART_EVENTS</code> environment variable contains the list of events that started the job, it will not be present if the job was started manually. The <code>pre-stop</code> and <code>post-stop</code> scripts are run with the environment of the events or commands that stopped the job. The <code>UPSTART_STOP_EVENTS</code> environment variable contains the list of events that stopped the job, it will not be present if the job was stopped manually.</p>
<dt>&bull;</p>
<dd>Variables set within the job itself using the <code>env</code> and <code>export</code> stanzas. These provide default values &#8211; if the command or event which causes the job to start specifies alternative values, those are given priority over the defaults.</p>
<dl>
<dd>
<dl>
<dt><code>env </code><i>KEY</i>[=<i>VALUE</i>]</p>
<dd>Defines a default environment variable, the value of which may be overridden by the event or command that starts the job. If &#8216;KEY=VALUE&#8217; is specified, the variable KEY is given the value VALUE. If only &#8216;KEY&#8217; is given, then the value is taken from the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon&#8217;s own environment.</p>
<dt><code>export </code><i>KEY</i></p>
<dd>Exports the value of an environment variable into the <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7), <code><a href="/docs/linux/man/7-started/">started</a></code>(7), <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) and <code><a href="/docs/linux/man/7-stopped/">stopped</a></code>(7) events for this job <code> and to all resultant events </code> (not just those relating to the current job).</dl>
</dl>
<p> The first two categories above comprise the <i>job environment table</i> which is applied to all jobs. Note that changing the job environment table will only affect newly-started jobs.</dl>
<h3>Services, tasks and respawning</h3>
<p>Jobs are <i>services</i> by default. This means that the act of starting the job is considered to be finished when the job is running, and that even exiting with a zero exit status means the service will be respawned.</p>
<dl>
<dt><code>task</code></p>
<dd>This stanza may be used to specify that the job is a <i>task</i> instead. This means that the act of starting the job is not considered to be finished until the job itself has been run and stopped again, but that exiting with a zero exit status means the task has completed successfully and will not be respawned.  The <code><a href="/docs/linux/man/8-start/">start</a></code>(8) command, and any <code><a href="/docs/linux/man/7-starting/">starting</a></code>(7) or <code><a href="/docs/linux/man/7-stopping/">stopping</a></code>(7) events will block only until a service is running or until a task has finished.</p>
<dl>
<dt><code>respawn</code></p>
<dd>A service or task with this stanza will be automatically started if it should stop abnormally. All reasons for a service stopping, except the <code><a href="/docs/linux/man/8-stop/">stop</a></code>(8) command itself, are considered abnormal. Tasks may exit with a zero exit status to prevent being respawned.</p>
<dt><code>respawn limit </code><i>COUNT INTERVAL</i></p>
<dd>Respawning is subject to a limit, if the job is respawned more than <i>COUNT</i> times in <i>INTERVAL</i> seconds, it will be considered to be having deeper problems and will be stopped. Default COUNT is 10. Default INTERVAL is 5 seconds. This only applies to automatic respawns and not the <code><a href="/docs/linux/man/8-restart/">restart</a></code>(8) command.</p>
<dt><code>normal exit </code><i>STATUS</i>|<i>SIGNAL</i>&#8230;</p>
<dd>Additional exit statuses or even signals may be added, if the job process terminates with any of these it will not be considered to have failed and will not be respawned. A signal can be specified either as a full name (for example &quot;<i>SIGTERM</i>&quot;) or a partial name (for example &quot;<i>TERM</i>&quot;). </p>
<pre>normal exit 0 1 TERM SIGHUP</pre>
</dl>
<h3>Instances</h3>
<p>By default, only one instance of any job is permitted to exist at one time. Attempting to start a job when it&#8217;s already starting or running results in an error. Note that a job is considered to be running if its pre-start process is running. Multiple instances may be permitted by defining the names of those instances. If an instance with the same name is not already starting or running, a new instance will be started instead of returning an error.</p>
<dl>
<dt><code>instance </code><i>NAME</i></p>
<dd>This stanza defines the names of instances, on its own its not particularly useful since it would just define the name of the single permitted instance, however <i>NAME</i> expands any variable defined in the job&#8217;s environment. These will often be variables that you need to pass to the process anyway, so are an excellent way to limit the instances. </p>
<pre>instance $CONFFILE
exec /sbin/httpd -c $CONFFILE</pre>
<pre>instance $TTY
exec /sbin/getty -8 38300 $TTY</pre>
<p>These jobs appear in the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) output with the instance name in parentheses, and have the <code>INSTANCE</code> environment variable set in their events.</dl>
<h3>Documentation</h3>
<p>Upstart provides several stanzas useful for documentation and external tools.</p>
<dl>
<dt><code>description </code><i>DESCRIPTION</i></p>
<dd>This stanza may contain a description of the job. </p>
<pre>description &quot;This does neat stuff&quot;</pre>
<dt><code>author </code><i>AUTHOR</i></p>
<dd>This stanza may contain the author of the job, often used as a contact for bug reports. </p>
<pre>author &quot;Scott James Remnant &lt;scott [at] netsplit.com&gt;&quot;</pre>
<dt><code>version </code><i>VERSION</i></p>
<dd>This stanza may contain version information about the job, such as revision control or package version number. It is not used or interpreted by <code><a href="/docs/linux/man/8-init/">init</a></code>(8) in any way. </p>
<pre>version &quot;$Id$&quot;</pre>
<dt><code>emits </code><i>EVENT</i>&#8230;</p>
<dd>All processes on the system are free to emit their own events by using the <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) tool, or by communicating directly with the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon. This stanza allows a job to document in its job configuration what events it emits itself, and may be useful for graphing possible transitions. The <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code>check-config</code> command attempts to use this stanza to resolve events. <i>EVENT</i> can be either a literal string or a string including shell wildcard meta-characters (asterisk (&#8216;*&#8217;), question mark (&#8216;?&#8217;), and square brackets (&#8216;[&#8216; and &#8216;]&#8217;)). Meta-characters are useful to allow <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code>check-config</code> to resolve a class of events, such as those emitted by <code><a href="/docs/linux/man/8-upstart-udev-bridge/">upstart-udev-bridge</a></code>(8).</p>
<dt><code>usage </code><i>USAGE</i></p>
<dd>This stanza may contain the text used by <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) <code>usage</code> command. This text may be also shown when commands <code><a href="/docs/linux/man/8-start/">start</a></code>(8), <code><a href="/docs/linux/man/8-stop/">stop</a></code>(8) or <code><a href="/docs/linux/man/8-status/">status</a></code>(8) fail. </p>
<pre>usage &quot;tty DEV=ttyX - where X is console id&quot;</pre>
</dl>
<h3>Process environment</h3>
<p>Many common adjustments to the process environment, such as resource limits, may be configured directly in the job rather than having to handle them yourself.</p>
<dl>
<dt><code>console none</code>|<code>log</code>|<code>output</code>|<code>owner</code></p>
<dd>
<dl>
<dd><code>none</code></p>
<dl>
<dd>If <code>none</code> is specified, the jobs standard input, standard output and standard error file descriptors are connected to <i>/dev/null</i>. Any output generated by a job will be discarded. This used to be the default prior to the introduction of <code>log</code> in Upstart 1.4.</dl>
</dl>
<dl>
<dd><code>log</code></p>
<dl>
<dd><code>If log</code> is specified, standard input is connected to <i>/dev/null</i>, and standard output and standard error are connected to a pseudo-tty which logs all job output. Output is logged to file <i>/var/log/upstart/&lt;job-log-file&gt;</i> or <i>$XDG_CACHE_HOME/upstart/&lt;job-log-file&gt;</i> for system and user session jobs respectively. If a job has specified <code>instance</code>, <i>&lt;job-log-file&gt;</i> will equate to <i>&lt;job&gt;-&lt;instance&gt;.log</i> where &#8216;&lt;instance&gt;&#8217; is replaced by the specific instance value and &#8216;&lt;job&gt;&#8217; is replaced with the job name (job configuration file name, without the extension). If <code>instance</code> is not specified, <i>&lt;job-log-file&gt;</i> will be <i>&lt;job&gt;.log</i> where &#8216;&lt;job&gt;&#8217; is replaced with the job name. Jobs started from within a chroot will have their output logged to such a path within the chroot. If log files already exist, they are appended to. All slash (&#8216;/&#8217;) characters in <i>&lt;job-log-file&gt;</i> are replaced with underscore (&#8216;_&#8217;) characters. For example, any output from the &#8216;wibble&#8217; instance of the &#8216;foo/bar&#8217; job would be encoded in file &#8216;foo_bar-wibble.log&#8217; in the log file directory. This gives the log file directory a flat structure. If the directory for system jobs does not exist, job output for each job will be cached until the job finishes. Thus, the boot process <code>must</code> ensure that the directory is available as soon as possible since any job that finishes before a writeable disk is available will not be able to take advantage of this facility. If it is not possible to write to any log file due to lack of disk space, the job will be considered to have specified a <code>console</code> value of <code>none</code> and all subsequent job output will be discarded. If the logger detects that the file it is about to write to was deleted, it will re-open the file first. Care should be taken if the log directory is a mount point since any job that starts before that mount is available and which produces output will then attempt to write logs to the mount point, not to the mounted directory. This may give the impression that log data has not been recorded. A strategy to handle this situation is to ensure the mount point directory is not writeable such that logs will only be written when the mount has succeeded (assuming the mount itself is writeable and has sufficient space). Note that since <code>log</code> utilizes pseudo-ttys, your kernel must support these. If it does not, the console value will be modified automatically to <code>none</code>. Further, note that it may be necessary to increase the number of available pty devices; see <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7) for details. Under Linux, full Unix 98 pty support requires that the <i>devpts</i> filesystem be mounted. If pty setup fails for any reason, an error message will be displayed and the job&#8217;s console value will be reset to <code>none</code>.</dl>
</dl>
<dl>
<dd><code>output</code></p>
<dl>
<dd>If <code>output</code> is specified, the standard input, standard output and standard error file descriptors are connected to <i>/dev/console</i>.</dl>
</dl>
<dl>
<dd><code>owner</code></p>
<dl>
<dd>The <code>owner</code> value is special: it not only connects the job to the system console but sets the job to be the owner of the system console, which means it will receive certain signals from the kernel when special key combinations such as Control-C are pressed.</dl>
</dl>
<dt><code>umask </code><i>UMASK</i></p>
<dd>A common configuration is to set the file mode creation mask for the process. <i>UMASK</i> should be an octal value for the mask, see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) for more details.</p>
<dt><code>nice </code><i>NICE</i></p>
<dd>Another common configuration is to adjust the process&#8217;s nice value, see <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1) for more details.</p>
<dt><code>oom score </code><i>ADJUSTMENT</i>|<code>never</code></p>
<dd>Normally the OOM killer regards all processes equally, this stanza advises the kernel to treat this job differently. <i>ADJUSTMENT</i> may be an integer value from <i>-999</i> (very unlikely to be killed by the OOM killer) up to <i>1000</i> (very likely to be killed by the OOM killer). It may also be the special value <code>never</code> to have the job ignored by the OOM killer entirely.</p>
<dt><code>chroot </code><i>DIR</i></p>
<dd>Runs the job&#8217;s processes in a <code><a href="/docs/linux/man/8-chroot/">chroot</a>(8)</code> environment underneath <i>DIR</i> Note that <i>DIR</i> must have all the necessary system libraries for the process to be run, often including <i>/bin/sh</i></p>
<dt><code>chdir </code><i>DIR</i></p>
<dd>Runs the job&#8217;s processes with a working directory of <i>DIR</i> instead of the root of the filesystem.</p>
<dt><code>limit </code><i>LIMIT SOFT</i>|<code>unlimited </code><i>HARD</i>|<code>unlimited</code></p>
<dd>Sets initial system resource limits for the job&#8217;s processes. <i>LIMIT</i> may be one of <i>core</i>, <i>cpu</i>, <i>data</i>, <i>fsize</i>, <i>memlock</i>, <i>msgqueue</i>, <i>nice</i>, <i>nofile</i>, <i>nproc</i>, <i>rss</i>, <i>rtprio</i>, <i>sigpending</i> or <i>stack</i>. Limits are specified as both a <i>SOFT</i> value and a <i>HARD</i> value, both of which are integers. The special value <code>unlimited</code> may be specified for either.</p>
<dt><code>setuid </code><i>USERNAME</i></p>
<dd>Changes to the user <i>USERNAME</i> before running any job process. The job process will run with the primary group of user <i>USERNAME</i> unless the <code>setgid</code> stanza is also specified in which case that group will be used instead. For system jobs <code><a href="/docs/linux/man/3-initgroups/">initgroups</a></code>(3) will be called to set up supplementary group access. Failure to determine and/or set user and group details will result in the overall job failing to start. If this stanza is unspecified, all job processes will run with user ID 0 (root) in the case of system jobs, and as the user in the case of user jobs. Note that system jobs using the <code>setuid</code> stanza are still system jobs, and can not be controlled by an unprivileged user, even if the <code>setuid</code> stanza specifies that user.</p>
<dt><code>setgid </code><i>GROUPNAME</i></p>
<dd>Changes to the group <i>GROUPNAME</i> before running any job process. For system jobs <code><a href="/docs/linux/man/3-initgroups/">initgroups</a></code>(3) will be called to set up supplementary group access. If this stanza is unspecified, the primary group of the user specified in the <code>setuid</code> block is used for all job processes. If both this and the <code>setuid</code> stanza are unspecified, all job processes will run with their group ID set to 0 (root) in the case of system jobs, and as the primary group of the user in the case of User Session jobs.</dl>
<h3>Override File Handling</h3>
<p>Override files allow a jobs environment to be changed without modifying the jobs configuration file. Rules governing override files:</p>
<dl>
<dt>&bull;</p>
<dd>If a job is embodied with only a configuration file, the contents of this file define the job.</p>
<dt>&bull;</p>
<dd>If an override files exists where there is no existing cofiguration file, the override file is ignored.</p>
<dt>&bull;</p>
<dd>If both a configuration file <code>and</code> an override file exist for a job and both files are syntactically correct:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>stanzas in the override file will take precedence over stanzas present in the corresponding configuration file.</p>
<dt>&bull;</p>
<dd>stanzas in the override file which are not present in the corresponding configuration file will be honoured when the job runs.</dl>
</dl>
<dt>&bull;</p>
<dd>If both a configuration file and an override file exist for a job and subsequently the override file is deleted, the configuration file is automatically reloaded with the effect that any changes introduced by the override file are undone and the configuration file alone now defines the job.</p>
<dt>&bull;</p>
<dd>If both a configuration file and an override file exist for a job and subsequently the configuration file is deleted, a new instance of the job can no longer be started (since without a corresponding configuration file an override file is ignored).</p>
<dt>&bull;</p>
<dd>If both a configuration file and an override file exist for a job and any of the contents of the override file are invalid, the override file is ignored and only the contents of the configuration file are considered.</dl>
<h3>AppArmor support</h3>
<p>Upstart provides several stanzas for loading and switching to different AppArmor profiles. If AppArmor isn&#8217;t enabled in the currently running kernel, the stanzas will be silently ignored.</p>
<dl>
<dt><code>apparmor load </code><i>PROFILE</i></p>
<dd>This stanza specifies an AppArmor profile to load into the Linux kernel at job start. The AppArmor profile will confine a main process automatically using path attachment, or manually by using the <code>apparmor switch</code> stanza. <i>PROFILE</i> must be an absolute path to a profile and a failure will occur if the file doesn&#8217;t exist. </p>
<pre>apparmor load /etc/apparmor.d/usr.sbin.cupsd</pre>
<dt><code>apparmor switch </code><i>NAME</i></p>
<dd>This stanza specifies the name of an AppArmor profile name to switch to before running the main process. <i>NAME</i> must be the name of a profile already loaded into the running Linux kernel, and will result in a failure if not available. </p>
<pre>apparmor switch /usr/sbin/cupsd</pre>
</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>kill signal </code><i>SIGNAL</i></p>
<dd>Specifies the stopping signal, <i>SIGTERM</i> by default, a job&#8217;s main process will receive when stopping the running job. The signal should be specified as a full name (for example &quot;<i>SIGTERM</i>&quot;) or a partial name (for example &quot;<i>TERM</i>&quot;). Note that it is possible to specify the signal as a number (for example &quot;<i>15</i>&quot;) although this should be avoided if at all possible since signal numbers may differ between systems. </p>
<pre>kill signal INT</pre>
<dt><code>reload signal </code><i>SIGNAL</i></p>
<dd>Specifies the reload signal, <i>SIGHUP</i> by default, a job&#8217;s main process will receive when reloading the running job. The signal should be specified as a full name (for example &quot;<i>SIGHUP</i>&quot;) or a partial name (for example &quot;<i>HUP</i>&quot;). Note that it is possible to specify the signal as a number (for example &quot;<i>1</i>&quot;) although this should be avoided if at all possible since signal numbers may differ between systems. </p>
<pre>reload signal USR1</pre>
<dt><code>kill timeout </code><i>INTERVAL</i></p>
<dd>Specifies the interval between sending the job&#8217;s main process the &quot;stopping&quot; (see above) and <i>SIGKILL</i> signals when stopping the running job. Default is 5 seconds.</p>
<dt><code>expect stop</code></p>
<dd>Specifies that the job&#8217;s main process will raise the <i>SIGSTOP</i> signal to indicate that it is ready. <code><a href="/docs/linux/man/8-init/">init</a></code>(8) will wait for this signal before running the job&#8217;s post-start script, or considering the job to be running. <code><a href="/docs/linux/man/8-init/">init</a></code>(8) will send the process the <i>SIGCONT</i> signal to allow it to continue.</p>
<dt><code>expect daemon</code></p>
<dd>Specifies that the job&#8217;s main process is a daemon, and will fork twice after being run. <code><a href="/docs/linux/man/8-init/">init</a></code>(8) will follow this daemonisation, and will wait for this to occur before running the job&#8217;s post-start script or considering the job to be running. Without this stanza <code><a href="/docs/linux/man/8-init/">init</a></code>(8) is unable to supervise daemon processes and will believe them to have stopped as soon as they daemonise on startup.</p>
<dt><code>expect fork</code></p>
<dd>Specifies that the job&#8217;s main process will fork once after being run. <code><a href="/docs/linux/man/8-init/">init</a></code>(8) will follow this fork, and will wait for this to occur before running the job&#8217;s post-start script or considering the job to be running. Without this stanza <code><a href="/docs/linux/man/8-init/">init</a></code>(8) is unable to supervise forking processes and will believe them to have stopped as soon as they fork on startup.</dl>
<h2>Restrictions</h2>
<p>The use of symbolic links in job configuration file directories is not supported since it can lead to unpredictable behaviour resulting from broken or inaccessible links (such as would be caused by a link crossing a filesystem boundary to a filesystem that has not yet been mounted).</p>
<h2>Bugs</h2>
<p>The <code>and</code> and <code>or</code> operators allowed with <code>start on</code> and <code>stop on</code> do not work intuitively: operands to the right of either operator are only evaluated once and state information is then discarded. This can lead to jobs with complex <code>start on</code> or stop on conditions not behaving as expected <i>when restarted</i>. For example, if a job encodes the following condition: </p>
<dl>
<dd>
<pre>start on A and (B or C)</pre>
</dl>
<p> When &#8216;A&#8217; and &#8216;B&#8217; become true, the condition is satisfied so the job will be run. However, if the job ends and subsequently &#8216;A&#8217; and &#8216;C&#8217; become true, the job will <i>not</i> be re-run even though the condtion is satisfied. Avoid using complex conditions with jobs which need to be restarted.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/init/*.conf</i></p>
<dd>System job configuration files.</p>
<dt><i>/etc/init/*.override</i></p>
<dd>System job override files.</p>
<dt><i>$HOME/.init/*.conf</i></p>
<dd>User job configuration files <code>(deprecated)</code>.</p>
<dt><i>$HOME/.init/*.override</i></p>
<dd>User job override files. <code>(deprecated)</code>.</p>
<dt><i>$XDG_CONFIG_HOME/upstart/*.conf</i></p>
<dd>User session job configuration files. See <code>User Session Mode</code> for other locations.</p>
<dt><i>$XDG_CONFIG_HOME/upstart/*.override</i></p>
<dd>User session job override files. See <code>User Session Mode</code> for other locations.</p>
<dt><i>/var/log/upstart/*.log</i></p>
<dd>Default location of system job output logs.</p>
<dt><i>$XDG_CACHE_HOME/upstart/*.log</i></p>
<dd>Default location of user session job output logs.</p>
<dt><i>$XDG_RUNTIME_DIR/upstart/sessions/*.session</i></p>
<dd>Location of session files created when running in User Session mode.</dl>
<h2>Author</h2>
<p>Manual page written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt; and James Hunt &lt;<code>james.hunt [at] canonical.com</code>&gt;<code>.</code></p>
<h2>Reporting Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/upstart/+bugs">https://launchpad.net/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-apparmor/">apparmor</a></code>(7), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/7-upstart-events/">upstart-events</a></code>(7). </p>
