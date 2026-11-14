---
title: "env(1)"
name: "env"
section: "1"
letter: "e"
url: "/docs/linux/man/1-env/"
description: "env – run a program in a modified environment"
---

<h2 class="name">NAME</h2>
<p> env &#8211; run a program in a modified environment </p>
<h2>SYNOPSIS</h2>
<p> <code>env</code> [<i>,OPTION/</i>]&#8230; [<i>,-/</i>] [<i>,NAME=VALUE/</i>]&#8230; [<i>,COMMAND /</i>[<i>,ARG/</i>]&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Set each NAME to VALUE in the environment and run COMMAND. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;ignore-environment</code></p>
<dd> start with an empty environment</p>
<dt><code>-0</code>, <code>&#8211;null</code></p>
<dd> end each output line with NUL, not newline</p>
<dt><code>-u</code>, <code>&#8211;unset</code>=<i>,NAME/</i></p>
<dd> remove variable from the environment</p>
<dt><code>-C</code>, <code>&#8211;chdir</code>=<i>,DIR/</i></p>
<dd> change working directory to DIR</p>
<dt><code>-S</code>, <code>&#8211;split-string</code>=<i>,S/</i></p>
<dd> process and split S into separate arguments; used to pass multiple arguments on shebang lines</p>
<dt><code>&#8211;block-signal</code>[=<i>,SIG/</i>]</p>
<dd> block delivery of SIG signal(s) to COMMAND</p>
<dt><code>&#8211;default-signal</code>[=<i>,SIG/</i>]</p>
<dd> reset handling of SIG signal(s) to the default</p>
<dt><code>&#8211;ignore-signal</code>[=<i>,SIG/</i>]</p>
<dd> set handling of SIG signals(s) to do nothing</p>
<dt><code>&#8211;list-signal-handling</code></p>
<dd> list non default signal handling to stderr</p>
<dt><code>-v</code>, <code>&#8211;debug</code></p>
<dd> print verbose information for each processing step</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> A mere &#8211; implies <code>-i</code>. If no COMMAND, print the resulting environment. </p>
<p> SIG may be a signal name like &#8216;PIPE&#8217;, or a signal number like &#8217;13&#8217;. Without SIG, all known signals are included. Multiple signals can be comma-separated.</p>
<h2>OPTIONS</h2>
<h3>-S/&#8211;split-string usage in scripts</h3>
<p> The <code>-S</code> option allows specifying multiple parameters in a script. Running a script named <code>1.pl</code> containing the following first line: </p>
<dl>
<dt>
<dd>
<pre>
#!/usr/bin/env -S perl -w -T
...
</pre>
</dl>
<p> Will execute <code>perl -w -T 1.pl.</code> </p>
<p> Without the <code>&#8216;-S&#8217;</code> parameter the script will likely fail with: </p>
<dl>
<dt>
<dd>
<pre>
/usr/bin/env: 'perl -w -T': No such file or directory
</pre>
</dl>
<p> See the full documentation for more details. </p>
<h3>&#8211;default-signal[=SIG] usage</h3>
<p> This option allows setting a signal handler to its default action, which is not possible using the traditional shell trap command. The following example ensures that seq will be terminated by SIGPIPE no matter how this signal is being handled in the process invoking the command. </p>
<dl>
<dt>
<dd>
<pre>
sh -c 'env --default-signal=PIPE seq inf | head -n1'
</pre>
</dl>
<h2>NOTES</h2>
<p> POSIX&#8217;s <a href="/docs/linux/man/2-exec/">exec</a>(2) pages says:</p>
<dl>
<dt>
<dd> &quot;many existing applications wrongly assume that they start with certain signals set to the default action and/or unblocked&#8230;. Therefore, it is best not to block or ignore signals across execs without explicit reason to do so, and especially not to block signals across execs of arbitrary (not closely cooperating) programs.&quot;</dl>
<h2>AUTHOR</h2>
<p> Written by Richard Mlynarik, David MacKenzie, and Assaf Gordon.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-sigaction/">sigaction</a>(2), <a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a>(2), <a href="/docs/linux/man/7-signal/">signal</a>(7) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/env">https://www.gnu.org/software/coreutils/env</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) env invocation&#8217; </p>
<h2>Index</h2>
