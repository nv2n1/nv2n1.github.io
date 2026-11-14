---
title: "krenew(1)"
name: "krenew"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krenew/"
description: "krenew – Renew a Kerberos ticket"
---

<h2 class="name">NAME</h2>
<p> krenew &#8211; Renew a Kerberos ticket </p>
<h2>SYNOPSIS</h2>
<p> <code>krenew</code> [<code>-bhiLstvx</code>] [<code>-c</code> <i>child pid file</i>] [<code>-H</code> <i>minutes</i>]<br />
&nbsp;<wbr>[<code>-K</code>&nbsp;<wbr><i>minutes</i>]&nbsp;<wbr>[<code>-k</code>&nbsp;<wbr><i>ticket cache</i>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>pid file</i>]<br />
&nbsp;<wbr>[<i>command</i>&nbsp;<wbr>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>krenew</code> renews an existing renewable ticket. When run without any arguments, it just attempts to renew the existing ticket-granting ticket in the current ticket cache, equivalent to <tt>&quot;kinit -R&quot;</tt>, but it can optionally run a program like <code>aklog</code> to refresh <font SIZE="-1">AFS</font> tokens, can run as a daemon and wake up periodically to renew the ticket cache, or can run a specified command and keep renewing the ticket cache until the command finishes (or renewal is no longer possible). If a command is specified, <code>krenew</code> by default wakes up every 60 minutes (1 hour) to check the ticket cache. </p>
<p> If a command is given, <code>krenew</code> makes a copy of the ticket cache and creates a private ticket cache just for that command, thus isolating it from later destruction of the original ticket cache. This allows krenew to maintain authentication for a command even if, for example, the user running the command logs out and OpenSSH destroys their original ticket cache. </p>
<p> If a command is given, it will not be run using the shell, so if you want to use shell metacharacters in the command with their special meaning, give <tt>&quot;sh -c </tt>command<tt>&quot;</tt> as the command to run and quote <i>command</i>. If the command contains command-line options (like <tt>&quot;-c&quot;</tt>), put <tt>&quot;--&quot;</tt> on the command line before the beginning of the command to tell <code>krenew</code> to not parse those options as its own. </p>
<p> If <code>krenew</code> is built with <i>setpag()</i> support and <font SIZE="-1">AFS</font> tokens are requested with the <code>-t</code> option, it will put the command in a separate <font SIZE="-1">PAG</font> before obtaining <font SIZE="-1">AFS</font> tokens so that they don&#8217;t interfere with other processes on the system. </p>
<p> When running a command, <code>krenew</code> propagates <font SIZE="-1">HUP</font>, <font SIZE="-1">TERM</font>, <font SIZE="-1">INT</font>, and <font SIZE="-1">QUIT</font> signals to the child process and does not exit when those signals are received. (If the propagated signal causes the child process to exit, <code>krenew</code> will then exit.) This allows <code>krenew</code> to react properly when run under a command supervision system such as <i><a href="/docs/linux/man/8-runit/">runit</a></i>(8) or <i><a href="/docs/linux/man/8-svscan/">svscan</a></i>(8) that uses signals to control supervised commands, and to run interactive commands that should receive Ctrl-C. </p>
<p> If a running <code>krenew</code> receives an <font SIZE="-1">ALRM</font> signal, it immediately refreshes the ticket cache regardless of whether it is in danger of expiring.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> After starting, detach from the controlling terminal and run in the background. This option only makes sense in combination with <code>-K</code> or a command that <code>krenew</code> will be running. <code>krenew</code> will not background itself until after it does the initial ticket renewal, so that any initial errors will be reported, but it will then redirect output to <i>/dev/null</i> and no subsequent errors will be reported. </p>
<p> If this flag is given, <code>krenew</code> will also change directories to <tt>&quot;/&quot;</tt>. All paths (such as to a command to run or a <font SIZE="-1">PID</font> file) should therefore be given as absolute, not relative, paths. </p>
<p> If used in conjunction with a command to run, that command will also run in the background and will also have its input and output redirected to <i>/dev/null</i>. It will have to report any errors via some other mechanism for the errors to be seen. </p>
<p> Use of this flag on Mac <font SIZE="-1">OS</font> X without specifying a file-based ticket cache by either using <code>-k</code> or setting <font SIZE="-1">KRB5CCNAME</font> will probably not do what you want. Ticket caches on Mac <font SIZE="-1">OS</font> X are, by default, per-session and with <code>-b</code> <code>krenew</code> will detach itself from your existing ticket cache. Instead, to renew the default ticket cache on Mac <font SIZE="-1">OS</font> X, try something like: </p>
<pre>
    (krenew -K 60 &amp;)
</pre>
<p> to run <code>krenew</code> in the background but within the current session. </p>
<p> When using this option, consider also using <code>-L</code> to report <code>krenew</code> errors to syslog.</p>
<dt><code>-c</code> <i>child pid file</i></p>
<dd> Save the process <font SIZE="-1">ID</font> (<font SIZE="-1">PID</font>) of the child process into <i>child pid file</i>. <i>child pid file</i> is created if it doesn&#8217;t exist and overwritten if it does exist. This option is only allowed when a command was given on the command line and is most useful in conjunction with <code>-b</code> to allow management of the running child process. </p>
<p> Note that, when used with <code>-b</code>, the <font SIZE="-1">PID</font> file is written out after <code>krenew</code> is backgrounded and changes its working directory to <i>/</i>, so relative paths for the <font SIZE="-1">PID</font> file will be relative to <i>/</i> (probably not what you want).</p>
<dt><code>-H</code> <i>minutes</i></p>
<dd> Only renew the ticket if it has a remaining lifetime of less than <i>minutes</i> minutes. If either the ticket already has a sufficiently long remaining lifetime or renewal was successful, run the command (if one was specified) or exit immediately with status 0 (if none was). Otherwise, try to renew the ticket so that it will have a remaining lifetime of at least <i>minutes</i>, exit with an error if unsuccessful, and then run the command, if any. Cannot be used with <code>-K</code>.</p>
<dt><code>-h</code></p>
<dd> Display a usage message and exit.</p>
<dt><code>-i</code></p>
<dd> Ignore errors in renewing the ticket and keep running. Normally, <code>krenew</code> exits as soon as the ticket cache either disappears or the tickets run out of renewable lifetime. If this flag is given, it will complain about the failure to standard error (unless <code>-b</code> was given) but continue running, waking up to try again after the next check interval (see <code>-K</code>). This is useful if some other process may recreate an expired ticket cache and <code>krenew</code> should stay around and act on that recreated ticket cache once it&#8217;s present. </p>
<p> Setup errors opening the Kerberos ticket cache or running the command will still cause <code>krenew</code> to exit, even if this flag is given. Only Kerberos errors and errors after <code>krenew</code> is running and any command has been started will be ignored. </p>
<p> This flag is only useful in daemon mode or when a command was given.</p>
<dt><code>-K</code> <i>minutes</i></p>
<dd> Run in daemon mode to keep a ticket alive indefinitely. The program reawakens after <i>minutes</i> minutes, checks if the ticket will expire before or less than two minutes before the next scheduled check, and renews the ticket if needed. If this option is not given but a command was given on the command line, the default interval is 60 minutes (1 hour). </p>
<p> If an error occurs in refreshing the ticket cache that doesn&#8217;t cause <code>krenew</code> to exit, the wake-up interval will be shortened to one minute and the operation retried at that interval for as long as the error persists.</p>
<dt><code>-k</code> <i>ticket cache</i></p>
<dd> Use <i>ticket cache</i> as the ticket cache rather than the contents of the environment variable <font SIZE="-1">KRB5CCNAME</font> or the library default. <i>ticket cache</i> may be any ticket cache identifier recognized by the underlying Kerberos libraries. This generally supports a path to a file, with or without a leading <tt>&quot;FILE:&quot;</tt> string, but may also support other ticket cache types.</p>
<dt><code>-L</code></p>
<dd> Report messages to syslog as well as to standard output or standard error. All messages will be logged with facility <font SIZE="-1">LOG_DAEMON</font>. Regular messages that are displayed on standard output are logged with level <font SIZE="-1">LOG_NOTICE</font>. Errors that don&#8217;t cause <code>krenew</code> to terminate when run with <code>-i</code> are logged with level <font SIZE="-1">LOG_WARNING</font>. Fatal errors are logged with level <font SIZE="-1">LOG_ERR</font>. </p>
<p> This is useful when debugging problems in combination with <code>-b</code>.</p>
<dt><code>-p</code> <i>pid file</i></p>
<dd> Save the process <font SIZE="-1">ID</font> (<font SIZE="-1">PID</font>) of the running <code>krenew</code> process into <i>pid file</i>. <i>pid file</i> is created if it doesn&#8217;t exist and overwritten if it does exist. This option is most useful in conjunction with <code>-b</code> to allow management of the running <code>krenew</code> daemon. </p>
<p> Note that, when used with <code>-b</code> the <font SIZE="-1">PID</font> file is written out after <code>krenew</code> is backgrounded and changes its working directory to <i>/</i>, so relative paths for the <font SIZE="-1">PID</font> file will be relative to <i>/</i> (probably not what you want).</p>
<dt><code>-s</code></p>
<dd> Normally, when <code>krenew</code> exits abnormally while running a command (if, for example, the ticket&#8217;s renewable lifetime has expired), it leaves the command running. If <code>-s</code> is given, it will send a <font SIZE="-1">SIGHUP</font> signal to the command before exiting. This can be useful if it&#8217;s pointless for the command to keep running without Kerberos tickets.</p>
<dt><code>-t</code></p>
<dd> Run an external program after getting a ticket. The default use of this is to run <code>aklog</code> to get a token. If the environment variable <font SIZE="-1">KINIT_PROG</font> is set, it overrides the compiled-in default. </p>
<p> If <code>krenew</code> has been built with <font SIZE="-1">AFS</font> <i>setpag()</i> support and a command was given on the command line, <code>krenew</code> will create a new <font SIZE="-1">PAG</font> before obtaining <font SIZE="-1">AFS</font> tokens. Otherwise, it will obtain tokens in the current <font SIZE="-1">PAG</font>.</p>
<dt><code>-v</code></p>
<dd> Be verbose. This will print out a bit of additional information about what is being attempted and what the results are.</p>
<dt><code>-x</code></p>
<dd> Exit immediately on any error. Normally, when running a command or when run with the <code>-K</code> option, <code>krenew</code> keeps running even if it fails to renew the ticket cache as long as the ticket cache still exists and appears to be renewable. It tries again at the next check interval. With this option, <code>krenew</code> will instead exit.</dl>
<h2>RETURN VALUES</h2>
<p> The program normally exits with status 0 if it successfully renews a ticket. If <code>krenew</code> runs aklog or some other program <code>krenew</code> returns the exit status of that program.</p>
<h2>EXAMPLES</h2>
<p> Renew the current ticket-granting ticket. </p>
<pre>
    krenew
</pre>
<p> Wake up every ten minutes and check to see if the ticket cache needs renewing. If it does, re-run <code>aklog</code> as well. </p>
<pre>
    krenew -K 10 -t
</pre>
<p> Run the program <i>/usr/local/bin/compute-job</i> in the background, checking every hour to see if the ticket needs to be renewed (the default). Put the <font SIZE="-1">PID</font> of the <code>krenew</code> job in <i>/var/run/compute.pid</i>. Obtain a new <font SIZE="-1">AFS</font> token each time the ticket has to be renewed. </p>
<pre>
    krenew -b -t -p /var/run/compute.pid /usr/local/bin/compute-job
</pre>
<p> If you wanted to pass options to <i>/usr/local/bin/compute-job</i>, putting a <tt>&quot;--&quot;</tt> argument before it would be necessary to keep <code>krenew</code> from interpreting those options as its own. </p>
<p> If you want to redirect output to a file that requires authentication to write to, you will need to do that redirection in a sub-shell. In other words, the following command: </p>
<pre>
    krenew -t compute-job &gt; /afs/local/data/output
</pre>
<p> won&#8217;t work if /afs/local/data/output requires an <font SIZE="-1">AFS</font> token to write to. The job, while running, will have an <font SIZE="-1">AFS</font> token, but the output redirection is done in the parent shell and doesn&#8217;t benefit from <code>krenew</code>. The above should instead be written as: </p>
<pre>
    krenew -t -- sh -c 'compute-job &gt; /afs/local/data/output'
</pre>
<p> With this command, the shell doing the redirection will also be run under <code>krenew</code> and have the benefit of the <font SIZE="-1">AFS</font> token it obtains.</p>
<h2>ENVIRONMENT</h2>
<p> If the environment variable <font SIZE="-1">AKLOG</font> is set, its value will be used as the program to run with <code>-t</code> rather than the default complied into <code>krenew</code>. If <font SIZE="-1">AKLOG</font> is not set and <font SIZE="-1">KINIT_PROG</font> is set, its value will be used instead. <font SIZE="-1">KINIT_PROG</font> is honored for backward compatibility but its use is not recommended due to its confusing name. </p>
<p> If no ticket file (with <code>-k</code>) or command is specified on the command line, <code>krenew</code> will use the environment variable <font SIZE="-1">KRB5CCNAME</font> to determine the location of the the ticket granting ticket. If the <code>-k</code> option is used, <font SIZE="-1">KRB5CCNAME</font> will be set to point to the ticket file before running the <code>aklog</code> program or any command given on the command line.</p>
<h2>FILES</h2>
<p> The default ticket cache is determined by the underlying Kerberos libraries. The default path for aklog is determined at build time, and will normally be whichever of <code>aklog</code> or <code>afslog</code> is found in the user&#8217;s path.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-k5start/">k5start</a></i>(1), <i><a href="/docs/linux/man/1-kinit/">kinit</a></i>(1) </p>
<p> The kstart web page at &lt;<a rel="nofollow" href="http://www.eyrie.org/~eagle/software/kstart/">http://www.eyrie.org/~eagle/software/kstart/</a>&gt; will have the current version of <code>krenew</code>.</p>
<h2>AUTHORS</h2>
<p> <code>krenew</code> was written by Russ Allbery &lt;rra [at] stanford.edu&gt;. It was based heavily on <code>k5start</code> by Booker C. Bense, which in turn was based on the k4start code written by Robert Morgan. </p>
<h2>Index</h2>
