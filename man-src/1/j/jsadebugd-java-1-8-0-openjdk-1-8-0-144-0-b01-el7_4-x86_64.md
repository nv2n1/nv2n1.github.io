---
title: "jsadebugd-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64(1)"
name: "jsadebugd-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jsadebugd-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64/"
description: "jsadebugd – Attaches to a Java process or core file and acts as a debug server. This command is experimental and unsupported."
---

<p>jsadebugd &#8211; Attaches to a Java process or core file and acts as a debug server. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jsadebugd</code> <i>pid</i> [ <i>server-id</i> ]</pre>
<pre><code>jsadebugd</code> <i>executable</i> <i>core</i> [ <i>server-id</i> ]</pre>
<dl>
<dt><i>pid</i></p>
<dd>The process ID of the process to which the debug server attaches. The process must be a Java process. To get a list of Java processes running on a machine, use the <a href="/docs/linux/man/1-jps/">jps</a>(1) command. At most one instance of the debug server can be attached to a single process.</p>
<dt><i>executable</i></p>
<dd>The Java executable from which the core dump was produced.</p>
<dt><i>core</i></p>
<dd>The core file to which the debug server should attach.</p>
<dt><i>server-id</i></p>
<dd>An optional unique ID that is needed when multiple debug servers are started on the same machine. This ID must be used by remote clients to identify the particular debug server to which to attach. Within a single machine, this ID must be unique.</dl>
<h2>Description</h2>
<p>The <code>jsadebugd</code> command attaches to a Java process or core file and acts as a debug server. Remote clients such as <code>jstack</code>, <code>jmap</code>, and <code>jinfo</code> can attach to the server through Java Remote Method Invocation (RMI). Before you start the <code>jsadebugd</code> command, start the RMI registry with the <code>rmiregistry</code> command as follows where <i>$JAVA_HOME</i> is the JDK installation directory: </p>
<pre><code>rmiregistry -J-Xbootclasspath/p:$JAVA_HOME/lib/sajdi.jar</code></pre>
<p>If the RMI registry was not started, then the <code>jsadebugd</code> command starts an RMI registry in a standard (1099) port internally. The debug server can be stopped by sending a <code>SIGINT</code> to it. To send a SIGINT press <i>Ctrl+C</i>. </p>
<p> <i>Note:</i> This utility is unsupported and may or may not be available in future releases of the JDK. In Windows Systems where <code>dbgeng.dll</code> is not present, Debugging Tools For Windows must be installed to have these tools working. The <code>PATH</code> environment variable should contain the location of jvm.dll used by the target process or the location from which the crash dump file was produced. For example, <code>s</code><code>et PATH=%JDK_HOME%\jrein
