---
title: "systemd-cat(1)"
name: "systemd-cat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-cat/"
description: "systemd-cat – Connect a pipeline or program’s output with the journal"
---

<h2 class="name">NAME</h2>
<p> systemd-cat &#8211; Connect a pipeline or program&#8217;s output with the journal </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-cat </code><code>[OPTIONS&#8230;]</code><code>[COMMAND]</code><code>[ARGUMENTS&#8230;]</code></p>
<dt> <code>systemd-cat </code><code>[OPTIONS&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-cat</code></p>
<dd>may be used to connect the standard input and output of a process to the journal, or as a filter tool in a shell pipeline to pass the output the previous pipeline element generates to the journal. </p>
<p> If no parameter is passed, <code>systemd-cat</code> will write everything it reads from standard input (stdin) to the journal. </p>
<p> If parameters are passed, they are executed as command line with standard output (stdout) and standard error output (stderr) connected to the journal, so that all it writes is stored in the journal.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>-t</code>, <code>&#8211;identifier=</code></p>
<dl>
<dt>
<dd> Specify a short string that is used to identify the logging tool. If not specified, no identification string is written to the journal.</dl>
<p> <code>-p</code>, <code>&#8211;priority=</code></p>
<dl>
<dt>
<dd> Specify the default priority level for the logged messages. Pass one of &quot;emerg&quot;, &quot;alert&quot;, &quot;crit&quot;, &quot;err&quot;, &quot;warning&quot;, &quot;notice&quot;, &quot;info&quot;, &quot;debug&quot;, or a value between 0 and 7 (corresponding to the same named levels). These priority values are the same as defined by <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). Defaults to &quot;info&quot;. Note that this simply controls the default, individual lines may be logged with different levels if they are prefixed accordingly. For details, see <code>&#8211;level-prefix=</code> below.</dl>
<p> <code>&#8211;stderr-priority=</code></p>
<dl>
<dt>
<dd> Specifies the default priority level for messages from the process&#8217;s standard error output (stderr). Usage of this option is the same as the <code>&#8211;priority=</code> option, above, and both can be used at once. When both are used, <code>&#8211;priority=</code> will specify the default priority for standard output (stdout). </p>
<p> If <code>&#8211;stderr-priority=</code> is not specified, messages from stderr will still be logged, with the same default priority level as stdout. </p>
<p> Also, note that when stdout and stderr use the same default priority, the messages will be strictly ordered, because one channel is used for both. When the default priority differs, two channels are used, and so stdout messages will not be strictly ordered with respect to stderr messages &#8211; though they will tend to be approximately ordered.</dl>
<p> <code>&#8211;level-prefix=</code></p>
<dl>
<dt>
<dd> Controls whether lines read are parsed for syslog priority level prefixes. If enabled (the default), a line prefixed with a priority prefix such as &quot;&lt;5&gt;&quot; is logged at priority 5 (&quot;notice&quot;), and similar for the other priority levels. Takes a boolean argument.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Invoke a program</code> </p>
<p> This calls /bin/ls with standard output and error connected to the journal: </p>
<dl>
<dt>
<dd>
<pre>
# systemd-cat ls
</pre>
</dl>
<p> <code>Example 2. Usage in a shell pipeline</code> </p>
<p> This builds a shell pipeline also invoking /bin/ls and writes the output it generates to the journal: </p>
<dl>
<dt>
<dd>
<pre>
# ls | systemd-cat
</pre>
</dl>
<p> Even though the two examples have very similar effects the first is preferable since only one process is running at a time, and both stdout and stderr are captured while in the second example, only stdout is captured.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) </p>
<h2>Index</h2>
