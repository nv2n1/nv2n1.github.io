---
title: "skill(1)"
name: "skill"
section: "1"
letter: "s"
url: "/docs/linux/man/1-skill/"
description: "skill, snice – send a signal or report process status"
---

<h2 class="name">NAME</h2>
<p> skill, snice &#8211; send a signal or report process status </p>
<h2>SYNOPSIS</h2>
<p> <code>skill</code> [<i>signal</i>] [<i>options</i>] <i>expression</i><br />
 <code>snice</code> [<i>new priority</i>] [<i>options</i>] <i>expression</i></p>
<h2>DESCRIPTION</h2>
<p> These tools are obsolete and unportable. The command syntax is poorly defined. Consider using the killall, pkill, and pgrep commands instead. </p>
<p> The default signal for skill is TERM. Use -l or -L to list available signals. Particularly useful signals include HUP, INT, KILL, STOP, CONT, and 0. Alternate signals may be specified in three ways: -9 -SIGKILL -KILL. </p>
<p> The default priority for snice is +4. Priority numbers range from +20 (slowest) to -20 (fastest). Negative priority numbers are restricted to administrative users.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>,<code>&nbsp;&#8211;fast</code></p>
<dd> Fast mode. This option has not been implemented.</p>
<dt><code>-i</code>,<code>&nbsp;&#8211;interactive</code></p>
<dd> Interactive use. You will be asked to approve each action.</p>
<dt><code>-l</code>,<code>&nbsp;&#8211;list</code></p>
<dd> List all signal names.</p>
<dt><code>-L</code>,<code>&nbsp;&#8211;table</code></p>
<dd> List all signal names in a nice table.</p>
<dt><code>-n</code>,<code>&nbsp;&#8211;no-action</code></p>
<dd> No action; perform a simulation of events that would occur but do not actually change the system.</p>
<dt><code>-v</code>,<code>&nbsp;&#8211;verbose</code></p>
<dd> Verbose; explain what is being done.</p>
<dt><code>-w</code>,<code>&nbsp;&#8211;warnings</code></p>
<dd> Enable warnings. This option has not been implemented.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information.</dl>
<h2>PROCESS SELECTION OPTIONS</h2>
<p> Selection criteria can be: terminal, user, pid, command. The options below may be used to ensure correct interpretation.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;tty</code> <i>tty</i></p>
<dd> The next expression is a terminal (tty or pty).</p>
<dt><code>-u</code>, <code>&#8211;user</code> <i>user</i></p>
<dd> The next expression is a username.</p>
<dt><code>-p</code>, <code>&#8211;pid</code> <i>pid</i></p>
<dd> The next expression is a process ID number.</p>
<dt><code>-c</code>, <code>&#8211;command</code> <i>command</i></p>
<dd> The next expression is a command name.</p>
<dt><code>&#8211;ns </code><i>pid</i></p>
<dd> Match the processes that belong to the same namespace as pid.</p>
<dt><code>&#8211;nslist </code><i>ns/</i>,,<i>&#8230;/</i></p>
<dd> list which namespaces will be considered for the &#8211;ns option. Available namespaces: ipc, mnt, net, pid, user, uts.</dl>
<h2>SIGNALS</h2>
<p> The behavior of signals is explained in <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) manual page.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>snice -c seti -c crack +7</code></p>
<dd> Slow down seti and crack commands.</p>
<dt><code>skill -KILL -t /dev/pts/*</code></p>
<dd> Kill users on PTY devices.</p>
<dt><code>skill -STOP -u viro -u lm -u davem</code></p>
<dd> Stop three users.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>STANDARDS</h2>
<p> No standards apply.</p>
<h2>AUTHOR</h2>
<p> Albert Cahalan wrote skill and snice in 1999 as a replacement for a non-free version.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
