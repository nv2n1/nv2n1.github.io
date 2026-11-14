---
title: "jconsole-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "jconsole-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jconsole-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "jconsole – Java Monitoring and Management Console"
---

<p>jconsole &#8211; Java Monitoring and Management Console </p>
<h2>Synopsis</h2>
<pre><code>jconsole</code> [ <i>options</i> ] [ connection ... ]</pre>
<h2>Parameters</h2>
<dl>
<dd>
<dl>
<dt>options</p>
<dd>Options, if used, should follow immediately after the command name.</p>
<dt>connection = pid | host:port | jmxUrl</p>
<dd>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>pid</i> Process ID of a local Java VM. The Java VM must be running with the same user ID as the user ID running jconsole. See <i>JMX Monitoring and Management</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/management/agent.html">http://docs.oracle.com/javase/7/docs/technotes/guides/management/agent.html</a> for details.</p>
<dt>o</p>
<dd><i>host</i>:<i>port</i> Name of the host system on which the Java VM is running and the port number specified by the system property <i>com.sun.management.jmxremote.port</i> when the Java VM was started. See <i>JMX Monitoring and Management</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/management/agent.html">http://docs.oracle.com/javase/7/docs/technotes/guides/management/agent.html</a> for details.</p>
<dt>o</p>
<dd><i>jmxUrl</i> Address of the JMX agent to be connected to as described in <i>JMXServiceURL</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/javax/management/remote/JMXServiceURL.html.">http://docs.oracle.com/javase/7/docs/api/javax/management/remote/JMXServiceURL.html.</a></dl>
</dl>
</dl>
</dl>
<h2>Description</h2>
<p>The <code>jconsole</code> command launches a graphical console tool that enables you to monitor and manage Java applications and virtual machines on a local or remote machine. </p>
<p> On Windows, <code>jconsole</code> does not associate with a console window. It will, however, display a dialog box with error information if the <code>jconsole</code> command fails for some reason. </p>
<h2>Options</h2>
<dl>
<dd>
<dl>
<dt>-interval=n</p>
<dd>Set the update interval to <i>n</i> seconds (default is 4 seconds).</p>
<dt>-notile</p>
<dd>Do not tile windows initially (for two or more connections).</p>
<dt>-pluginpath plugins</p>
<dd>Specify a list of directories or JAR files which are searched for JConsole plugins. The <i>plugins</i> path should contain a provider-configuration file named: </p>
<pre><code> META-INF/services/com.sun.tools.jconsole.JConsolePlugin</code></pre>
<p>containing one line for each plugin specifying the fully qualified class name of the class implementing the <i>com.sun.tools.jconsole.JConsolePlugin</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/jdk/api/jconsole/spec/com/sun/tools/jconsole/JConsolePlugin.html">http://docs.oracle.com/javase/7/docs/jdk/api/jconsole/spec/com/sun/tools/jconsole/JConsolePlugin.html</a> class.</p>
<dt>-version</p>
<dd>Output version information and exit.</p>
<dt>-help</p>
<dd>Output help message and exit.</p>
<dt>-J&lt;flag&gt;</p>
<dd>Pass &lt;flag&gt; to the Java virtual machine on which jconsole is run.</dl>
</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>Using JConsole</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/management/jconsole.html">http://docs.oracle.com/javase/7/docs/technotes/guides/management/jconsole.html</a></p>
<dt>o</p>
<dd><i>Monitoring and Management for Java Platform</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/management/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/management/index.html</a></dl>
</dl>
<p>&nbsp;<wbr></p>
