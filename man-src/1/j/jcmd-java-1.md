---

title: "jcmd-java-1(1)"
name: "jcmd-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jcmd-java-1/"
description: "jcmd – Sends diagnostic command requests to a running Java Virtual Machine"
---

<p> jcmd &#8211; Sends diagnostic command requests to a running Java Virtual Machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
jcmd[options] jcmd[pid | main - class] PerfCounter.print
        jcmd[pid | main - class] command[arguments] jcmd[pid | main - class] -
    f file
</code></pre>
<dl>
<dl>
<dt>options</dt>
<dd> The command-line options. See Options.</dd>
<dt>pid</dt>
<dd> Identifies the process that receives the diagnostic command requests. The process must be a Java process. To get a list of Java processes running on a machine, use <a href="/docs/linux/man/1-jps/">jps</a>(1) or <a href="/docs/linux/man/1-jcmd/">jcmd</a>(1).</dd>
<dt>main-class</dt>
<dd> The main class of the process that receives the diagnostic command requests. When matching processes, any process whose main class name contains the specified string as a substring is matched. If several running Java processes share the same main class, then the diagnostic command request is sent to all these processes. To get a list of Java processes running on a machine, use <a href="/docs/linux/man/1-jps/">jps</a>(1) or <a href="/docs/linux/man/1-jcmd/">jcmd</a>(1).</dd>
<dt>command [arguments]</dt>
<dd> The main class of the process that receives the diagnostic command requests. When matching processes, any process whose main class name contains the specified string as a substring is matched. If several running Java processes share the same main class, then the diagnostic command request is sent to all these processes. To get a list of Java processes running on a machine, use <a href="/docs/linux/man/1-jps/">jps</a>(1) or <a href="/docs/linux/man/1-jcmd/">jcmd</a>(1).</dd>
<dt>Perfcounter.print</dt>
<dd> Print the performance counters available on the targeted Java processes. The list of performance counters might vary with the Java process.</dd>
<dt>-f file</dt>
<dd> Read commands from <i>file</i> and call them on the targeted Java processes. In <i>file</i>, each command must be written on a single line. Lines starting with # are ignored. Processing of <i>file</i> ends when all lines have been called or when a line containing the <code>stop</code> keyword is read.</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jcmd</code> is a utility to send diagnostic command requests to a Java Virtual Machine supporting this feature. </p>
<p> Used without arguments or with the <code>-l</code> option, <code>jcmd</code> prints the list of running Java processes with their process ID, their main class and their command-line arguments. </p>
<p> When a process ID is specified on the command line, <code>jcmd</code> sends the diagnostic command request to the process with this ID. </p>
<p> When a main class is specified on the command line, <code>jcmd</code> sends the diagnostic command request to all Java processes for which the command-line argument is a substring of the Java process&#8217; main class. </p>
<p> With the <code>PerfCounter.print</code> argument, <code>jcmd</code> prints the performance counters available on the targeted Java processes. </p>
<p> With the <code>-f</code> option, <code>jcmd</code> sends to the targeted Java processes the diagnostic commands stored in the specified <code>file</code>. </p>
<h2>OPTIONS</h2>
<p> Options are mutually exclusive. Options, when used, must immediately follow the command name. </p>
<dl>
<dl>
<dt>-l</dt>
<dd> Prints the list of running Java processes with their process IDs, their main classes, and their command-line arguments.</dd>
<dt>-h</dt>
<dd> Prints a help message.</dd>
<dt>-help</dt>
<dd> Prints a help message.</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dl>
<dt>o</dt>
<dd> jps</dd></dl>
</dl>
<p>&nbsp;<wbr> </p>
