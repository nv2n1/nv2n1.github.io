---
title: "jinfo-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64(1)"
name: "jinfo-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jinfo-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64/"
description: "jinfo – Generates configuration information. This command is experimental and unsupported."
---

<p>jinfo &#8211; Generates configuration information. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jinfo</code> [ <i>option</i> ] <i>pid</i></pre>
<pre><code>jinfo</code> [ <i>option </i>] <i>executable core</i></pre>
<pre><code>jinfo</code> [ <i>option </i>] <i>[ servier-id ] remote-hostname-or-IP</i></pre>
<dl>
<dt><i>option</i></dt>
<dd>The command-line options. See Options.</dd>
<dt><i>pid</i></dt>
<dd>The process ID for which the configuration information is to be printed. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command.</dd>
<dt><i>executable</i></dt>
<dd>The Java executable from which the core dump was produced.</dd>
<dt><i>core</i></dt>
<dd>The core file for which the configuration information is to be printed.</dd>
<dt><i>remote-hostname-or-IP</i></dt>
<dd>The remote debug server <code>hostname</code> or <code>IP</code> address. See jsadebugd(1).</dd>
<dt><i>server-id</i></dt>
<dd>An optional unique ID to use when multiple debug servers are running on the same remote host.</dd></dl>
<h2>Description</h2>
<p>The <code>jinfo</code> command prints Java configuration information for a specified Java process or core file or a remote debug server. The configuration information includes Java system properties and Java Virtual Machine (JVM) command-line flags. If the specified process is running on a 64-bit JVM, then you might need to specify the <code>-J-d64</code> option, for example: <code>jinfo</code><code>-J-d64 -sysprops pid</code>. </p>
<p> This utility is unsupported and might not be available in future releases of the JDK. In Windows Systems where <code>dbgeng.dll</code> is not present, Debugging Tools For Windows must be installed to have these tools working. The <code>PATH</code> environment variable should contain the location of the jvm.dll that is used by the target process or the location from which the crash dump file was produced. For example, <code>set PATH=%JDK_HOME%\jrein
</p>
</code>
