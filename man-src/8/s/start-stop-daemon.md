---
title: "start-stop-daemon(8)"
name: "start-stop-daemon"
section: "8"
letter: "s"
url: "/docs/linux/man/8-start-stop-daemon/"
description: "start-stop-daemon – start and stop system daemon programs"
---

<p>start-stop-daemon &#8211; start and stop system daemon programs</p>
<h2>Synopsis</h2>
<p><code>start-stop-daemon</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>Description</h2>
<p><code>start-stop-daemon</code> is used to control the creation and termination of system-level processes. Using one of the matching options, <code>start-stop-daemon</code> can be configured to find existing instances of a running process. </p>
<p> <code>Note:</code> Unless <code>&#8211;pid</code> or <code>&#8211;pidfile</code> are specified, <code>start-stop-daemon</code> behaves similar to <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1). <code>start-stop-daemon</code> will scan the process table looking for any processes which match the process name, parent pid, uid, and/or gid (if specified). Any matching process will prevent <code>&#8211;start</code> from starting the daemon. All matching processes will be sent the <font SIZE="-1">TERM</font> signal (or the one specified via <code>&#8211;signal</code> or <code>&#8211;retry</code>) if <code>&#8211;stop</code> is specified. For daemons which have long-lived children which need to live through a <code>&#8211;stop</code>, you must specify a pidfile.</p>
<h2>Commands</h2>
<dl>
<dt><code>-S</code>, <code>&#8211;start</code> [<code>&#8212;</code>] <i>arguments</i></p>
<dd>Check for the existence of a specified process. If such a process exists, <code>start-stop-daemon</code> does nothing, and exits with error status 1 (0 if <code>&#8211;oknodo</code> is specified). If such a process does not exist, it starts an instance, using either the executable specified by <code>&#8211;exec</code> or, if specified, by <code>&#8211;startas</code>. Any arguments given after <code>&#8212;</code> on the command line are passed unmodified to the program being started.</p>
<dt><code>-K</code>, <code>&#8211;stop</code></p>
<dd>Checks for the existence of a specified process. If such a process exists, <code>start-stop-daemon</code> sends it the signal specified by <code>&#8211;signal</code>, and exits with error status 0. If such a process does not exist, <code>start-stop-daemon</code> exits with error status 1 (0 if <code>&#8211;oknodo</code> is specified). If <code>&#8211;retry</code> is specified, then <code>start-stop-daemon</code> will check that the process(es) have terminated.</p>
<dt><code>-T</code>, <code>&#8211;status</code></p>
<dd>Check for the existence of a specified process, and returns an exit status code, according to the <font SIZE="-1">LSB</font> Init Script Actions (since version 1.16.1).</p>
<dt><code>-H</code>, <code>&#8211;help</code></p>
<dd>Show usage information and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the program version and exit.</dl>
<h2>Options</h2>
<h3>Matching options</h3>
<dl>
<dt><code>&#8211;pid</code> <i>pid</i></p>
<dd>Check for a process with the specified <i>pid</i> (since version 1.17.6). The <i>pid</i> must be a number greater than 0.</p>
<dt><code>&#8211;ppid</code> <i>ppid</i></p>
<dd>Check for a process with the specified parent pid <i>ppid</i> (since version 1.17.7). The <i>ppid</i> must be a number greater than 0.</p>
<dt><code>-p</code>, <code>&#8211;pidfile</code> <i>pidfile</i></p>
<dd>Check whether a process has created the file <i>pidfile</i>. </p>
<p> <code>Note:</code> Using this matching option alone might cause unintended processes to be acted on, if the old process terminated without being able to remove the <i>pidfile</i>. </p>
<p> <code>Warning:</code> Using this match option with a world-writable pidfile or using it alone with a daemon that writes the pidfile as an unprivileged (non-root) user will be refused with an error (since version 1.19.3) as this is a security risk, because either any user can write to it, or if the daemon gets compromised, the contents of the pidfile cannot be trusted, and then a privileged runner (such as an init script executed as root) would end up acting on any system process. Using <i>/dev/null</i> is exempt from these checks.</p>
<dt><code>-x</code>, <code>&#8211;exec</code> <i>executable</i></p>
<dd>Check for processes that are instances of this <i>executable</i>. The <i>executable</i> argument should be an absolute pathname. </p>
<p> <code>Note:</code> This might not work as intended with interpreted scripts, as the executable will point to the interpreter. Take into account processes running from inside a chroot will also be matched, so other match restrictions might be needed.</p>
<dt><code>-n</code>, <code>&#8211;name</code> <i>process-name</i></p>
<dd>Check for processes with the name <i>process-name</i>. The <i>process-name</i> is usually the process filename, but it could have been changed by the process itself. </p>
<p> <code>Note:</code> On most systems this information is retrieved from the process comm name from the kernel, which tends to have a relatively short length limit (assuming more than 15 characters is non-portable).</p>
<dt><code>-u</code>, <code>&#8211;user</code> <i>username</i>|<i>uid</i></p>
<dd>Check for processes owned by the user specified by <i>username</i> or <i>uid</i>. </p>
<p> <code>Note:</code> Using this matching option alone will cause all processes matching the user to be acted on.</dl>
<h3>Generic options</h3>
<dl>
<dt><code>-g</code>, <code>&#8211;group</code> <i>group</i>|<i>gid</i></p>
<dd>Change to <i>group</i> or <i>gid</i> when starting the process.</p>
<dt><code>-s</code>, <code>&#8211;signal</code> <i>signal</i></p>
<dd>With <code>&#8211;stop</code>, specifies the signal to send to processes being stopped (default <font SIZE="-1">TERM</font>).</p>
<dt><code>-R</code>, <code>&#8211;retry</code> <i>timeout</i>|<i>schedule</i></p>
<dd>With <code>&#8211;stop</code>, specifies that <code>start-stop-daemon</code> is to check whether the process(es) do finish. It will check repeatedly whether any matching processes are running, until none are. If the processes do not exit it will then take further action as determined by the schedule. </p>
<p> If <i>timeout</i> is specified instead of <i>schedule</i>, then the schedule <i>signal</i><code>/</code><i>timeout</i><code>/KILL/</code><i>timeout</i> is used, where <i>signal</i> is the signal specified with <code>&#8211;signal</code>. </p>
<p> <i>schedule</i> is a list of at least two items separated by slashes (<code>/</code>); each item may be <code>&#8211;</code><i>signal-number</i> or [<code>&#8211;</code>]<i>signal-name</i>, which means to send that signal, or <i>timeout</i>, which means to wait that many seconds for processes to exit, or <code>forever</code>, which means to repeat the rest of the schedule forever if necessary. </p>
<p> If the end of the schedule is reached and <code>forever</code> is not specified, then <code>start-stop-daemon</code> exits with error status 2. If a schedule is specified, then any signal specified with <code>&#8211;signal</code> is ignored.</p>
<dt><code>-a</code>, <code>&#8211;startas</code> <i>pathname</i></p>
<dd>With <code>&#8211;start</code>, start the process specified by <i>pathname</i>. If not specified, defaults to the argument given to <code>&#8211;exec</code>.</p>
<dt><code>-t</code>, <code>&#8211;test</code></p>
<dd>Print actions that would be taken and set appropriate return value, but take no action.</p>
<dt><code>-o</code>, <code>&#8211;oknodo</code></p>
<dd>Return exit status 0 instead of 1 if no actions are (would be) taken.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Do not print informational messages; only display error messages.</p>
<dt><code>-c</code>, <code>&#8211;chuid</code> <i>username</i>|<i>uid</i>[<code>:</code><i>group</i>|<i>gid</i>]</p>
<dd>Change to this username/uid before starting the process. You can also specify a group by appending a <code>:</code>, then the group or gid in the same way as you would for the <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1) command (<i>user</i><code>:</code><i>group</i>). If a user is specified without a group, the primary <font SIZE="-1">GID</font> for that user is used. When using this option you must realize that the primary and supplemental groups are set as well, even if the <code>&#8211;group</code> option is not specified. The <code>&#8211;group</code> option is only for groups that the user isn&#8217;t normally a member of (like adding per process group membership for generic users like <code>nobody</code>).</p>
<dt><code>-r</code>, <code>&#8211;chroot</code> <i>root</i></p>
<dd>Change directory and chroot to <i>root</i> before starting the process. Please note that the pidfile is also written after the chroot.</p>
<dt><code>-d</code>, <code>&#8211;chdir</code> <i>path</i></p>
<dd>Change directory to <i>path</i> before starting the process. This is done after the chroot if the <code>-r</code>|<code>&#8211;chroot</code> option is set. When not specified, <code>start-stop-daemon</code> will change directory to the root directory before starting the process.</p>
<dt><code>-b</code>, <code>&#8211;background</code></p>
<dd>Typically used with programs that don&#8217;t detach on their own. This option will force <code>start-stop-daemon</code> to fork before starting the process, and force it into the background. </p>
<p> <code>Warning: start-stop-daemon</code> cannot check the exit status if the process fails to execute for <code>any</code> reason. This is a last resort, and is only meant for programs that either make no sense forking on their own, or where it&#8217;s not feasible to add the code for them to do this themselves.</p>
<dt><code>&#8211;notify-await</code></p>
<dd>Wait for the background process to send a readiness notification before considering the service started (since version 1.19.3). This implements parts of the systemd readiness protocol, as specified in the <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3) man page. The following variables are supported:</p>
<dl>
<dd>
<dl>
<dt><code>READY=1</code></p>
<dd>The program is ready to give service, so we can exit safely.</p>
<dt><code>EXTEND_TIMEOUT_USEC=</code><i>number</i></p>
<dd>The program requests to extend the timeout by <i>number</i> microseconds. This will reset the current timeout to the specified value.</p>
<dt><code>ERRNO=</code><i>number</i></p>
<dd>The program is exiting with an error. Do the same and print the user-friendly string for the <code>errno</code> value.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;notify-timeout</code> <i>timeout</i></p>
<dd>Set a timeout for the <code>&#8211;notify-await</code> option (since version 1.19.3). When the timeout is reached, <code>start-stop-daemon</code> will exit with an error code, and no readiness notification will be awaited. The default is <code>60</code> seconds.</p>
<dt><code>-C</code>, <code>&#8211;no-close</code></p>
<dd>Do not close any file descriptor when forcing the daemon into the background (since version 1.16.5). Used for debugging purposes to see the process output, or to redirect file descriptors to log the process output. Only relevant when using <code>&#8211;background</code>.</p>
<dt><code>-O</code>, <code>&#8211;output</code> <i>pathname</i></p>
<dd>Redirect <code>stdout</code> and <code>stderr</code> to <i>pathname</i> when forcing the daemon into the background (since version 1.20.6). Only relevant when using <code>&#8211;background</code>.</p>
<dt><code>-N</code>, <code>&#8211;nicelevel</code> <i>int</i></p>
<dd>This alters the priority of the process before starting it.</p>
<dt><code>-P</code>, <code>&#8211;procsched</code> <i>policy</i><code>:</code><i>priority</i></p>
<dd>This alters the process scheduler policy and priority of the process before starting it (since version 1.15.0). The priority can be optionally specified by appending a <code>:</code> followed by the value. The default <i>priority</i> is 0. The currently supported policy values are <code>other</code>, <code>fifo</code> and <code>rr</code>.</p>
<dt><code>-I</code>, <code>&#8211;iosched</code> <i>class</i><code>:</code><i>priority</i></p>
<dd>This alters the <font SIZE="-1">IO</font> scheduler class and priority of the process before starting it (since version 1.15.0). The priority can be optionally specified by appending a <code>:</code> followed by the value. The default <i>priority</i> is 4, unless <i>class</i> is <code>idle</code>, then <i>priority</i> will always be 7. The currently supported values for <i>class</i> are <code>idle</code>, <code>best-effort</code> and <code>real-time</code>.</p>
<dt><code>-k</code>, <code>&#8211;umask</code> <i>mask</i></p>
<dd>This sets the umask of the process before starting it (since version 1.13.22).</p>
<dt><code>-m</code>, <code>&#8211;make-pidfile</code></p>
<dd>Used when starting a program that does not create its own pid file. This option will make <code>start-stop-daemon</code> create the file referenced with <code>&#8211;pidfile</code> and place the pid into it just before executing the process. Note, the file will only be removed when stopping the program if <code>&#8211;remove-pidfile</code> is used. </p>
<p> <code>Note:</code> This feature may not work in all cases. Most notably when the program being executed forks from its main process. Because of this, it is usually only useful when combined with the <code>&#8211;background</code> option.</p>
<dt><code>&#8211;remove-pidfile</code></p>
<dd>Used when stopping a program that does not remove its own pid file (since version 1.17.19). This option will make <code>start-stop-daemon</code> remove the file referenced with <code>&#8211;pidfile</code> after terminating the process.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Print verbose informational messages.</dl>
<h2>Exit Status</h2>
<dl>
<dt><code>0</code></p>
<dd>The requested action was performed. If <code>&#8211;oknodo</code> was specified, it&#8217;s also possible that nothing had to be done. This can happen when <code>&#8211;start</code> was specified and a matching process was already running, or when <code>&#8211;stop</code> was specified and there were no matching processes.</p>
<dt><code>1</code></p>
<dd>If <code>&#8211;oknodo</code> was not specified and nothing was done.</p>
<dt><code>2</code></p>
<dd>If <code>&#8211;stop</code> and <code>&#8211;retry</code> were specified, but the end of the schedule was reached and the processes were still running.</p>
<dt><code>3</code></p>
<dd>Any other error.</dl>
<p> When using the <code>&#8211;status</code> command, the following status codes are returned:</p>
<dl>
<dt><code>0</code></p>
<dd>Program is running.</p>
<dt><code>1</code></p>
<dd>Program is not running and the pid file exists.</p>
<dt><code>3</code></p>
<dd>Program is not running.</p>
<dt><code>4</code></p>
<dd>Unable to determine program status.</dl>
<h2>Example</h2>
<p>Start the <code>food</code> daemon, unless one is already running (a process named food, running as user food, with pid in food.pid): </p>
<pre> start-stop-daemon --start --oknodo --user food --name food \
 --pidfile /run/food.pid --startas /usr/sbin/food \
 --chuid food -- --daemon</pre>
<p>Send <font SIZE="-1"><code>SIGTERM</code></font> to <code>food</code> and wait up to 5 seconds for it to stop: </p>
<pre> start-stop-daemon --stop --oknodo --user food --name food \
 --pidfile /run/food.pid --retry 5</pre>
<p>Demonstration of a custom schedule for stopping <code>food</code>: </p>
<pre> start-stop-daemon --stop --oknodo --user food --name food \
 --pidfile /run/food.pid --retry=TERM/30/KILL/5</pre>
