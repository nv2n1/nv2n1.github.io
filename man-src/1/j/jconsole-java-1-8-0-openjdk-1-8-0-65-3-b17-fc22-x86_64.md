---
title: "jconsole-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64(1)"
name: "jconsole-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jconsole-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64/"
description: "jconsole – Starts a graphical console that lets you monitor and manage Java applications."
---

<p>jconsole &#8211; Starts a graphical console that lets you monitor and manage Java applications.</p>
<h2>Synopsis</h2>
<pre><code>jconsole</code> [ <i>options</i> ] [ connection ... ]</pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt>connection = <i>pid</i> | <i>host</i>:<i>port</i> | <i>jmxURL</i></p>
<dd>The <code>pid</code> value is the process ID of a local Java Virtual Machine (JVM). The JVM must be running with the same user ID as the user ID running the <code>jconsole</code> command.The <code>host:port</code> values are the name of the host system on which the JVM is running, and the port number specified by the system property <code>com.sun.management.jmxremote.port</code> when the JVM was started.The <code>jmxUrl</code> value is the address of the JMX agent to be connected to as described in JMXServiceURL. </p>
<p> For more information about the <code>connection</code> parameter, see Monitoring and Management Using JMX Technology at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html">http://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html</a> </p>
<p> See also the <code>JMXServiceURL</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html">http://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html</a></dl>
<h2>Description</h2>
<p>The <code>jconsole</code> command starts a graphical console tool that lets you monitor and manage Java applications and virtual machines on a local or remote machine. </p>
<p> On Windows, the <code>jconsole</code> command does not associate with a console window. It does, however, display a dialog box with error information when the <code>jconsole</code> command fails.</p>
<h2>Options</h2>
<dl>
<dt>-interval<i>=n</i></p>
<dd>Sets the update interval to <i>n</i> seconds (default is 4 seconds).</p>
<dt>-notile</p>
<dd>Does not tile windows initially (for two or more connections).</p>
<dt>-pluginpath <i>plugins</i></p>
<dd>Specifies a list of directories or JAR files to be searched for <code>JConsole</code> plug-ins. The <i>plugins</i> path should contain a provider-configuration file named <code>META-INF/services/com.sun.tools.jconsole.JConsolePlugin</code> that contains one line for each plug-in. The line specifies the fully qualified class name of the class implementing the <code>com.sun.tools.jconsole.JConsolePlugin</code> class.</p>
<dt>-version</p>
<dd>Displays release information and exits.</p>
<dt>-help</p>
<dd>Displays a help message.</p>
<dt>-J<i>flag</i></p>
<dd>Passes <code>flag</code> to the JVM on which the <code>jconsole</code> command is run.</dl>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>Using JConsole at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/management/jconsole.html">http://docs.oracle.com/javase/8/docs/technotes/guides/management/jconsole.html</a></p>
<dt>&bull;</p>
<dd>Monitoring and Management Using JMX Technology at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html">http://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html</a></p>
<dt>&bull;</p>
<dd>The <code>JMXServiceURL</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html">http://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html</a> </p>
</dl>
