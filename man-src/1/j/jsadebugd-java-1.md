---
title: "jsadebugd-java-1(1)"
name: "jsadebugd-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jsadebugd-java-1/"
description: "jsadebugd – Serviceability Agent Debug Daemon"
---

<h2>Name</h2>
<p> jsadebugd &#8211; Serviceability Agent Debug Daemon </p>
<h2>SYNOPSIS</h2>
<pre><code>
jsadebugd pid[server - id] jsadebugd executable core[server - id]
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>pid</p>
<dd> process id of the process to which the debug server should attach. The process must be a Java process. To get a list of Java processes running on a machine, <a href="/docs/linux/man/1-jps/">jps</a>(1) may be used. At most one instance of the debug server may be attached to a single process.</p>
<dt>executable</p>
<dd> Java executable from which the core dump was produced</p>
<dt>core</p>
<dd> Core file to which the debug server should attach.</p>
<dt>server-id</p>
<dd> Optional unique id, needed if multiple debug servers are started on the same machine. This ID must be used by remote clients to identify the particular debug server to attach. Within a single machine, this ID must be unique.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jsadebugd</code> attaches to a Java process or core file and acts as a debug server. Remote clients such as <a href="/docs/linux/man/1-jstack/">jstack</a>(1), <a href="/docs/linux/man/1-jmap/">jmap</a>(1), and <a href="/docs/linux/man/1-jinfo/">jinfo</a>(1) can attach to the server using Java Remote Method Invocation (RMI). Before starting <i>jsadebugd</i>, <i>rmiregistry</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#rmi">http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#rmi</a> must be started with: </p>
<pre>
<tt>rmiregistry -J-Xbootclasspath/p:$JAVA_HOME/lib/sajdi.jar</tt>
</pre>
<p> where <i>$JAVA_HOME</i> is the JDK installation directory. If rmiregistry was not started, jsadebugd will start an rmiregistry in a standard (1099) port internally. Debug server may be stopped by sending SIGINT (pressing Ctrl-C) to it. </p>
<p> <code>NOTE</code> &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. In Windows Systems where dbgeng.dll is not present, &#8216;Debugging Tools For Windows&#8217; needs to be installed to have these tools working. Also, <i>PATH</i> environment variable should contain the location of <i>jvm.dll</i> used by the target process or the location from which the Crash Dump file was produced. </p>
<p> For example, <i>set PATH=&lt;jdk&gt;\jrein
