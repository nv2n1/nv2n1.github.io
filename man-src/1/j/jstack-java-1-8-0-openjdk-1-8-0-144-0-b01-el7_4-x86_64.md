---
title: "jstack-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64(1)"
name: "jstack-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstack-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64/"
description: "jstack – Prints Java thread stack traces for a Java process, core file, or remote debug server. This command is experimental and unsupported."
---

<p>jstack &#8211; Prints Java thread stack traces for a Java process, core file, or remote debug server. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jstack</code> [ <i>options</i> ] <i>pid</i> </pre>
<pre><code>jstack</code> [ <i>options</i> ] <i>executable</i> <i>core</i></pre>
<pre><code>jstack</code> [ <i>options</i> ] [ <i>server-id</i>@ ] <i>remote-hostname-or-IP</i></pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>pid</i></p>
<dd>The process ID for which the stack trace is printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command.</p>
<dt><i>executable</i></p>
<dd>The Java executable from which the core dump was produced.</p>
<dt><i>core</i></p>
<dd>The core file for which the stack trace is to be printed.</p>
<dt><i>remote-hostname-or-IP</i></p>
<dd>The remote debug server <code>hostname</code> or <code>IP</code> address. See <a href="/docs/linux/man/1-jsadebugd/">jsadebugd</a>(1).</p>
<dt><i>server-id</i></p>
<dd>An optional unique ID to use when multiple debug servers are running on the same remote host.</dl>
<h2>Description</h2>
<p>The <code>jstack</code> command prints Java stack traces of Java threads for a specified Java process, core file, or remote debug server. For each Java frame, the full class name, method name, byte code index (BCI), and line number, when available, are printed. With the <code>-m</code> option, the <code>jstack</code> command prints both Java and native frames of all threads with the program counter (PC). For each native frame, the closest native symbol to PC, when available, is printed. C++ mangled names are not demangled. To demangle C++ names, the output of this command can be piped to <code>c++filt</code>. When the specified process is running on a 64-bit Java Virtual Machine, you might need to specify the <code>-J-d64</code> option, for example: <code>jstack -J-d64 -m pid</code>. </p>
<p> <i>Note:</i> This utility is unsupported and might not be available in future release of the JDK. In Windows Systems where the dbgeng.dll file is not present, Debugging Tools For Windows must be installed so these tools work. The <code>PATH</code> environment variable needs to contain the location of the jvm.dll that is used by the target process, or the location from which the crash dump file was produced. For example: </p>
<pre><code>set PATH=&lt;jdk&gt;\jrein
