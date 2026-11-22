---

title: "skill(1)"
name: "skill"
section: "1"
letter: "s"
url: "/docs/linux/man/1-skill/"
description: "skill, snice – send a signal or report process status"
---

<p> skill, snice &#8211; send a signal or report process status </p>
<h2>SYNOPSIS</h2>
<p> <code>skill</code> [<i>signal</i>] [<i>options</i>] <i>expression</i><br/>
 <code>snice</code> [<i>new priority</i>] [<i>options</i>] <i>expression</i></p>
<h2>DESCRIPTION</h2>
<p> These tools are obsolete and unportable. The command syntax is poorly defined. Consider using the killall, pkill, and pgrep commands instead. </p>
<p> The default signal for skill is TERM. Use -l or -L to list available signals. Particularly useful signals include HUP, INT, KILL, STOP, CONT, and 0. Alternate signals may be specified in three ways: -9 -SIGKILL -KILL. </p>
<p> The default priority for snice is +4. Priority numbers range from +20 (slowest) to -20 (fastest). Negative priority numbers are restricted to administrative users.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>,<code>&nbsp;&#8211;fast</code></dt>
<dd> Fast mode. This option has not been implemented.</dd>
<dt><code>-i</code>,<code>&nbsp;&#8211;interactive</code></dt>
<dd> Interactive use. You will be asked to approve each action.</dd>
<dt><code>-l</code>,<code>&nbsp;&#8211;list</code></dt>
<dd> List all signal names.</dd>
<dt><code>-L</code>,<code>&nbsp;&#8211;table</code></dt>
<dd> List all signal names in a nice table.</dd>
<dt><code>-n</code>,<code>&nbsp;&#8211;no-action</code></dt>
<dd> No action; perform a simulation of events that would occur but do not actually change the system.</dd>
<dt><code>-v</code>,<code>&nbsp;&#8211;verbose</code></dt>
<dd> Verbose; explain what is being done.</dd>
<dt><code>-w</code>,<code>&nbsp;&#8211;warnings</code></dt>
<dd> Enable warnings. This option has not been implemented.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display help text and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Display version information.</dd></dl>
<h2>PROCESS SELECTION OPTIONS</h2>
<p> Selection criteria can be: terminal, user, pid, command. The options below may be used to ensure correct interpretation.</p>
<dl>
<dt><code>-t</code>, <code>&#8211;tty</code> <i>tty</i></dt>
<dd> The next expression is a terminal (tty or pty).</dd>
<dt><code>-u</code>, <code>&#8211;user</code> <i>user</i></dt>
<dd> The next expression is a username.</dd>
<dt><code>-p</code>, <code>&#8211;pid</code> <i>pid</i></dt>
<dd> The next expression is a process ID number.</dd>
<dt><code>-c</code>, <code>&#8211;command</code> <i>command</i></dt>
<dd> The next expression is a command name.</dd>
<dt><code>&#8211;ns </code><i>pid</i></dt>
<dd> Match the processes that belong to the same namespace as pid.</dd>
<dt><code>&#8211;nslist </code><i>ns/</i>,,<i>&#8230;/</i></dt>
<dd> list which namespaces will be considered for the &#8211;ns option. Available namespaces: ipc, mnt, net, pid, user, uts.</dd></dl>
<h2>SIGNALS</h2>
<p> The behavior of signals is explained in <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) manual page.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>snice -c seti -c crack +7</code></dt>
<dd> Slow down seti and crack commands.</dd>
<dt><code>skill -KILL -t /dev/pts/*</code></dt>
<dd> Kill users on PTY devices.</dd>
<dt><code>skill -STOP -u viro -u lm -u davem</code></dt>
<dd> Stop three users.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>STANDARDS</h2>
<p> No standards apply.</p>
<h2>AUTHOR</h2>
<p> Albert Cahalan wrote skill and snice in 1999 as a replacement for a non-free version.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
