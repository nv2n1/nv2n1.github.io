---
title: "jmap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "jmap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jmap-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "jmap – Prints shared object memory maps or heap memory details for a process, core file, or remote debug server. This command is experimental and unsupported."
---

<p>jmap &#8211; Prints shared object memory maps or heap memory details for a process, core file, or remote debug server. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jmap</code> [ <i>options</i> ] <i>pid</i></pre>
<pre><code>jmap</code> [ <i>options</i> ] <i>executable</i> <i>core</i></pre>
<pre><code>jmap</code> [ <i>options</i> ] [ <i>pid</i> ] <i>server-id</i>@ ] <i>remote-hostname-or-IP</i></pre>
<dl>
<dt><i>options</i></dt>
<dd>The command-line options. See Options.</dd>
<dt><i>pid</i></dt>
<dd>The process ID for which the memory map is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command.</dd>
<dt><i>executable</i></dt>
<dd>The Java executable from which the core dump was produced.</dd>
<dt><i>core</i></dt>
<dd>The core file for which the memory map is to be printed.</dd>
<dt><i>remote-hostname-or-IP</i></dt>
<dd>The remote debug server <code>hostname</code> or <code>IP</code> address. See jsadebugd(1).</dd>
<dt><i>server-id</i></dt>
<dd>An optional unique ID to use when multiple debug servers are running on the same remote host.</dd></dl>
<h2>Description</h2>
<p>The <code>jmap</code> command prints shared object memory maps or heap memory details of a specified process, core file, or remote debug server. If the specified process is running on a 64-bit Java Virtual Machine (JVM), then you might need to specify the <code>-J-d64</code> option, for example: <code>jmap</code><code>-J-d64 -heap pid</code>. </p>
<p> <i>Note:</i> This utility is unsupported and might not be available in future releases of the JDK. On Windows Systems where the <code>dbgeng.dll</code> file is not present, Debugging Tools For Windows must be installed to make these tools work. The <code>PATH</code> environment variable should contain the location of the <code>jvm.dll</code> file that is used by the target process or the location from which the crash dump file was produced, for example: <code>set PATH=%JDK_HOME%\jrein
</p>
</code>
