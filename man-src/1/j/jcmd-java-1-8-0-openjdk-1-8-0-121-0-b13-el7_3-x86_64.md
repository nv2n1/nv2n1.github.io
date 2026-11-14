---
title: "jcmd-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64(1)"
name: "jcmd-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jcmd-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64/"
description: "jcmd – Sends diagnostic command requests to a running Java Virtual Machine (JVM)."
---

<p>jcmd &#8211; Sends diagnostic command requests to a running Java Virtual Machine (JVM). </p>
<h2>Synopsis</h2>
<dl>
<dd>
<pre><code>jcmd</code> [<code>-l</code>|<code>-h</code>|<code>-help</code>]</pre>
</dl>
<dl>
<dd>
<pre><code>jcmd</code> <i>pid</i>|<i>main-class</i> <code>PerfCounter.print</code></pre>
</dl>
<dl>
<dd>
<pre><code>jcmd</code> <i>pid</i>|<i>main-class</i> <code>-f</code> <i>filename</i></pre>
</dl>
<dl>
<dd>
<pre><code>jcmd</code> <i>pid</i>|<i>main-class</i> <i>command</i>[ <i>arguments</i>]</pre>
</dl>
<h2>Description</h2>
<p>The <code>jcmd</code> utility is used to send diagnostic command requests to the JVM. It must be used on the same machine on which the JVM is running, and have the same effective user and group identifiers that were used to launch the JVM. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> To invoke diagnostic commands from a remote machine or with different identifiers, you can use the <code>com.sun.management.DiagnosticCommandMBean</code> interface. For more information about the <code>DiagnosticCommandMBean</code> interface, see the API documentation at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/jre/api/management/extension/com/sun/management/DiagnosticCommandMBean.html">http://docs.oracle.com/javase/8/docs/jre/api/management/extension/com/sun/management/DiagnosticCommandMBean.html</a>
</td>
</tr>
</table>
</dl>
<p> If you run <code>jcmd</code> without arguments or with the <code>-l</code> option, it prints the list of running Java process identifiers with the main class and command-line arguments that were used to launch the process. Running <code>jcmd</code> with the <code>-h</code> or <code>-help</code> option prints the tool&#8217;s help message. </p>
<p> If you specify the processes identifier (<i>pid</i>) or the main class (<i>main-class</i>) as the first argument, <code>jcmd</code> sends the diagnostic command request to the Java process with the specified identifier or to all Java processes with the specified name of the main class. You can also send the diagnostic command request to all available Java processes by specifying <code>0</code> as the process identifier. Use one of the following as the diagnostic command request: </p>
<p> Perfcounter.print</p>
<dl>
<dd>Prints the performance counters available for the specified Java process. The list of performance counters might vary with the Java process.</dl>
<p> -f <i>filename</i></p>
<dl>
<dd>The name of the file from which to read diagnostic commands and send them to the specified Java process. Used only with the <code>-f</code> option. Each command in the file must be written on a single line. Lines starting with a number sign (<code>#</code>) are ignored. Processing of the file ends when all lines have been read or when a line containing the <code>stop</code> keyword is read.</dl>
<p> <i>command</i> [<i>arguments</i>]</p>
<dl>
<dd>The command to be sent to the specified Java process. The list of available diagnostic commands for a given process can be obtained by sending the <code>help</code> command to this process. Each diagnostic command has its own set of arguments. To see the description, syntax, and a list of available arguments for a command, use the name of the command as the argument for the <code>help</code> command. </p>
<p> <code>Note:</code> If any arguments contain spaces, you must surround them with single or double quotation marks (<code>&#8216;</code> or <code>&quot;</code>). In addition, you must escape single or double quotation marks with a backslash (<code>\</code>) to prevent the operating system shell from processing quotation marks. Alternatively, you can surround these arguments with single quotation marks and then with double quotation marks (or with double quotation marks and then with single quotation marks).</dl>
<h2>Options</h2>
<p>Options are mutually exclusive. </p>
<p> -f <i>filename</i></p>
<dl>
<dd>Reads commands from the specified file. This option can be used only if you specify the process identifier or the main class as the first argument. Each command in the file must be written on a single line. Lines starting with a number sign (<code>#</code>) are ignored. Processing of the file ends when all lines have been read or when a line containing the <code>stop</code> keyword is read.</dl>
<p> -h<br />
 -help</p>
<dl>
<dd>Prints a help message.</dl>
<p> -l</p>
<dl>
<dd>Prints the list of running Java processes identifiers with the main class and command-line arguments.</dl>
<h2>See Also</h2>
<dl>
<dd>&bull; <a href="/docs/linux/man/1-jps/">jps</a>(1)</dl>
