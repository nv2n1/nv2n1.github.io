---
title: "jconsole-java-1-6-0-openjdk(1)"
name: "jconsole-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jconsole-java-1-6-0-openjdk/"
description: "jconsole – Java Monitoring and Management Console"
---

<p>jconsole &#8211; Java Monitoring and Management Console</p>
<h2>Synopsis</h2>
<pre><code>jconsole</code> [ <i>options</i> ] [ connection ... ]</pre>
<h2>Parameters</h2>
<dl>
<dd>
<dl>
<dt>options</p>
<dd>Options, if used, should follow immediately after the command name. </p>
<dt>connection = pid | host:port | jmxUrl</p>
<dd>
<dl>
<dd><i>pid</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> Process ID of a local Java VM. The Java VM must be running with the same user ID as the user ID running jconsole. See JMX Monitoring and Management for details.<br />
 <i>host</i>:<i>port</i>&nbsp;<wbr>&nbsp;<wbr> Name of the host system on which the Java VM is running and the port number specified by the system property <i>com.sun.management.jmxremote.port</i> when the Java VM was started. See JMX Monitoring and Management for details.<br />
 <i>jmxUrl</i>&nbsp;<wbr>&nbsp;<wbr> Address of the JMX agent to be connected to as described in JMXServiceURL.</dl>
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
<dt>-notile&nbsp;<wbr></p>
<dd>Do not tile windows initially (for two or more connections).</p>
<dt>-pluginpath&nbsp;<wbr> plugins</p>
<dd>Specify a list of directories or JAR files which are searched for JConsole plugins. The <i>plugins</i> path should contain a provider-configuration file named: </p>
<pre><code> META-INF/services/com.sun.tools.jconsole.JConsolePlugin</code></pre>
</dl>
<p> containing one line for each plugin specifying the fully qualified class name of the class implementing the com.sun.tools.jconsole.JConsolePlugin class.</p>
<dl>
<dt>-version&nbsp;<wbr></p>
<dd>Output version information and exit.</p>
<dt>-help&nbsp;<wbr></p>
<dd>Output help message and exit.</p>
<dt>-J&lt;flag&gt;&nbsp;<wbr></p>
<dd>Pass &lt;flag&gt; to the Java virtual machine on which jconsole is run.</dl>
</dl>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>Using JConsole</p>
<dt>o</p>
<dd>Monitoring and Management for Java Platform</dl>
</dl>
<p>&nbsp;<wbr></p>
