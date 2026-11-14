---
title: "pgrep(1)"
name: "pgrep"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgrep/"
description: "pgrep, pkill, pidwait – look up, signal, or wait for processes based on name and other attributes"
---

<h2 class="name">NAME</h2>
<p> pgrep, pkill, pidwait &#8211; look up, signal, or wait for processes based on name and other attributes </p>
<h2>SYNOPSIS</h2>
<p> <code>pgrep</code> [options] pattern<br />
 <code>pkill</code> [options] pattern<br />
 <code>pidwait</code> [options] pattern</p>
<h2>DESCRIPTION</h2>
<p> <code>pgrep</code> looks through the currently running processes and lists the process IDs which match the selection criteria to stdout. All the criteria have to match. For example,</p>
<dl>
<dt>
<dd> $ pgrep -u root sshd</dl>
<p> will only list the processes called <code>sshd</code> AND owned by <code>root</code>. On the other hand,</p>
<dl>
<dt>
<dd> $ pgrep -u root,daemon</dl>
<p> will list the processes owned by <code>root</code> OR <code>daemon</code>. </p>
<p> <code>pkill</code> will send the specified signal (by default <code>SIGTERM</code>) to each process instead of listing them on stdout. </p>
<p> <code>pidwait</code> will wait for each process instead of listing them on stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code><i>signal</i></p>
<dd> <code>&#8211;signal</code> <i>signal</i> Defines the signal to send to each matched process. Either the numeric or the symbolic signal name can be used. (<code>pkill</code> only.)</p>
<dt><code>-c</code>, <code>&#8211;count</code></p>
<dd> Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will return non-zero value. Note that for pkill and pidwait, the count is the number of matching processes, not the processes that were successfully signaled or waited for.</p>
<dt><code>-d</code>, <code>&#8211;delimiter</code> <i>delimiter</i></p>
<dd> Sets the string used to delimit each process ID in the output (by default a newline). (<code>pgrep</code> only.)</p>
<dt><code>-e</code>, <code>&#8211;echo</code></p>
<dd> Display name and PID of the process being killed. (<code>pkill</code> only.)</p>
<dt><code>-f</code>, <code>&#8211;full</code></p>
<dd> The <i>pattern</i> is normally only matched against the process name. When <code>-f</code> is set, the full command line is used.</p>
<dt><code>-g</code>, <code>&#8211;pgroup</code> <i>pgrp</i>,&#8230;</p>
<dd> Only match processes in the process group IDs listed. Process group 0 is translated into <code>pgrep</code>&#8216;s, <code>pkill</code>&#8216;s, or <code>pidwait</code>&#8216;s own process group.</p>
<dt><code>-G</code>, <code>&#8211;group</code> <i>gid</i>,&#8230;</p>
<dd> Only match processes whose real group ID is listed. Either the numerical or symbolical value may be used.</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> Match processes case-insensitively.</p>
<dt><code>-l</code>, <code>&#8211;list-name</code></p>
<dd> List the process name as well as the process ID. (<code>pgrep</code> only.)</p>
<dt><code>-a</code>, <code>&#8211;list-full</code></p>
<dd> List the full command line as well as the process ID. (<code>pgrep</code> only.)</p>
<dt><code>-n</code>, <code>&#8211;newest</code></p>
<dd> Select only the newest (most recently started) of the matching processes.</p>
<dt><code>-o</code>, <code>&#8211;oldest</code></p>
<dd> Select only the oldest (least recently started) of the matching processes.</p>
<dt><code>-O</code>, <code>&#8211;older</code> <i>secs</i></p>
<dd> Select processes older than secs.</p>
<dt><code>-P</code>, <code>&#8211;parent</code> <i>ppid</i>,&#8230;</p>
<dd> Only match processes whose parent process ID is listed.</p>
<dt><code>-s</code>, <code>&#8211;session</code> <i>sid</i>,&#8230;</p>
<dd> Only match processes whose process session ID is listed. Session ID 0 is translated into <code>pgrep</code>&#8216;s, <code>pkill</code>&#8216;s, or <code>pidwait</code>&#8216;s own session ID.</p>
<dt><code>-t</code>, <code>&#8211;terminal</code> <i>term</i>,&#8230;</p>
<dd> Only match processes whose controlling terminal is listed. The terminal name should be specified without the &quot;/dev/&quot; prefix.</p>
<dt><code>-u</code>, <code>&#8211;euid</code> <i>euid</i>,&#8230;</p>
<dd> Only match processes whose effective user ID is listed. Either the numerical or symbolical value may be used.</p>
<dt><code>-U</code>, <code>&#8211;uid</code> <i>uid</i>,&#8230;</p>
<dd> Only match processes whose real user ID is listed. Either the numerical or symbolical value may be used.</p>
<dt><code>-v</code>, <code>&#8211;inverse</code></p>
<dd> Negates the matching. This option is usually used in <code>pgrep</code>&#8216;s or <code>pidwait</code>&#8216;s context. In <code>pkill</code>&#8216;s context the short option is disabled to avoid accidental usage of the option.</p>
<dt><code>-w</code>, <code>&#8211;lightweight</code></p>
<dd> Shows all thread ids instead of pids in <code>pgrep</code>&#8216;s or <code>pidwait</code>&#8216;s context. In <code>pkill</code>&#8216;s context this option is disabled.</p>
<dt><code>-x</code>, <code>&#8211;exact</code></p>
<dd> Only match processes whose names (or command lines if <code>-f</code> is specified) <code>exactly</code> match the <i>pattern</i>.</p>
<dt><code>-F</code>, <code>&#8211;pidfile</code> <i>file</i></p>
<dd> Read <i>PID</i>s from <i>file</i>. This option is more useful for <code>pkill</code>or<code>pidwait</code> than <code>pgrep</code>.</p>
<dt><code>-L</code>, <code>&#8211;logpidfile</code></p>
<dd> Fail if pidfile (see <code>-F</code>) not locked.</p>
<dt><code>-r</code>, <code>&#8211;runstates</code> <i>D,R,S,Z,</i>&#8230;</p>
<dd> Match only processes which match the process state.</p>
<dt><code>&#8211;ns </code><i>pid</i></p>
<dd> Match processes that belong to the same namespaces. Required to run as root to match processes from other users. See <code>&#8211;nslist</code> for how to limit which namespaces to match.</p>
<dt><code>&#8211;nslist </code><i>name</i>,&#8230;</p>
<dd> Match only the provided namespaces. Available namespaces: ipc, mnt, net, pid, user,uts.</p>
<dt><code>-q</code>, <code>&#8211;queue </code><i>value</i></p>
<dd> Use <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a>(3)</code> rather than <code><a href="/docs/linux/man/2-kill/">kill</a>(2)</code> and the value argument is used to specify an integer to be sent with the signal. If the receiving process has installed a handler for this signal using the SA_SIGINFO flag to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a>(2)</code> , then it can obtain this data via the si_value field of the siginfo_t structure.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help and exit.</dl>
<h2>OPERANDS</h2>
<dl>
<dt><i>pattern</i></p>
<dd> Specifies an Extended Regular Expression for matching against the process names or command lines.</dl>
<h2>EXAMPLES</h2>
<p> Example 1: Find the process ID of the <code>named</code> daemon:</p>
<dl>
<dt>
<dd> $ pgrep -u root named</dl>
<p> Example 2: Make <code>syslog</code> reread its configuration file:</p>
<dl>
<dt>
<dd> $ pkill -HUP syslogd</dl>
<p> Example 3: Give detailed information on all <code>xterm</code> processes:</p>
<dl>
<dt>
<dd> $ ps -fp $(pgrep -d, -x xterm)</dl>
<p> Example 4: Make all <code>chrome</code> processes run nicer:</p>
<dl>
<dt>
<dd> $ renice +4 $(pgrep chrome)</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</p>
<dd> One or more processes matched the criteria. For pkill and pidwait, one or more processes must also have been successfully signalled or waited for.</p>
<dt>1</p>
<dd> No processes matched or none of them could be signalled.</p>
<dt>2</p>
<dd> Syntax error in the command line.</p>
<dt>3</p>
<dd> Fatal error: out of memory etc.</dl>
<h2>NOTES</h2>
<p> The process name used for matching is limited to the 15 characters present in the output of /proc/<i>pid</i>/stat. Use the <code>-f</code> option to match against the complete command line, /proc/<i>pid</i>/cmdline. </p>
<p> The running <code>pgrep</code>, <code>pkill</code>, or <code>pidwait</code> process will never report itself as a match.</p>
<h2>BUGS</h2>
<p> The options <code>-n</code> and <code>-o</code> and <code>-v</code> can not be combined. Let me know if you need to do this. </p>
<p> Defunct processes are reported. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/1-skill/">skill</a></code>(1), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)</p>
<h2>AUTHOR</h2>
<p> Kjetil Torgrim Homme</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
