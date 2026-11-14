---
title: "jsadebugd-java-1-6-0-openjdk(1)"
name: "jsadebugd-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jsadebugd-java-1-6-0-openjdk/"
description: "jsadebugd – Serviceability Agent Debug Daemon"
---

<p>jsadebugd &#8211; Serviceability Agent Debug Daemon</p>
<h2>Synopsis</h2>
<pre><code>jsadebugd</code> pid [ server-id ]
<code>jsadebugd</code> executable core [ server-id ]</pre>
<h2>Parameters</h2>
<dl>
<dt>pid</p>
<dd>process id of the process to which the debug server should attach. The process must be a Java process. To get a list of Java processes running on a machine, jps may be used. At most one instance of the debug server may be attached to a single process.</dl>
<dl>
<dt>executable</p>
<dd></dl>
<dl>
<dt>Java executable from which the core dump was produced</p>
<dd></dl>
<dl>
<dt>core</p>
<dd>Core file to which the debug server should attach.</dl>
<dl>
<dt>server-id</p>
<dd>Optional unique id, needed if multiple debug servers are started on the same machine. This ID must be used by remote clients to identify the particular debug server to attach. Within a single machine, this ID must be unique.</dl>
<h2>Description</h2>
<p><code>jsadebugd</code> attaches to a Java process or core file and acts as a debug server. Remote clients such as jstack, jmap, and jinfo can attach to the server using Java Remote Method Invocation (RMI). Before starting <i>jsadebugd</i>, rmiregistry must be started with: </p>
<dl>
<dd>
<pre><tt>rmiregistry -J-Xbootclasspath/p:$JAVA_HOME/lib/sajdi.jar</tt></pre>
</dl>
<p> where <i>$JAVA_HOME</i> is the JDK installation directory. If rmiregistry was not started, jsadebugd will start an rmiregistry in a standard (1099) port internally. Debug server may be stopped by sending SIGINT (pressing Ctrl-C) to it. </p>
<p> <code>NOTE &#8211; This utility is unsupported and may or may not be available in future versions of the JDK. jsadebugd is not currently available on Windows platforms.</code> </p>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>jinfo</p>
<dt>*</p>
<dd>jmap</p>
<dt>*</p>
<dd>jps</p>
<dt>*</p>
<dd>jstack</p>
<dt>*</p>
<dd>rmiregistry</dl>
</dl>
<p>&nbsp;<wbr></p>
