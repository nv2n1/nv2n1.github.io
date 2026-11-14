---
title: "jstatd-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "jstatd-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstatd-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "jstatd – Virtual Machine jstat Daemon"
---

<p>jstatd &#8211; Virtual Machine jstat Daemon </p>
<h2>Synopsis</h2>
<pre><code>jstatd [ </code><tt>options</tt><code> ]</code>
<br></pre>
<h2>Parameters</h2>
<dl>
<dd>
<dl>
<dt>options</p>
<dd>Command-line options. The options may be in any order. If there are redundant or contradictory options, the last option specified will take precedence.</dl>
</dl>
<h2>Description</h2>
<p>The <code>jstatd</code> tool is an RMI server application that monitors for the creation and termination of instrumented HotSpot Java virtual machines (JVMs) and provides a interface to allow remote monitoring tools to attach to JVMs running on the local host. </p>
<p> The <code>jstatd</code> server requires the presence of an RMI registry on the local host. The <code>jstatd</code> server will attempt to attach to the RMI registry on the default port, or on the port indicated by the <i>-p port</i> option. If an RMI registry is not found, one will be created within the <code>jstatd</code> application bound to the port indicated by the <i>-p port</i> option or to the default RMI registry port if <i>-p port</i> is omitted. Creation of an internal RMI registry can be inhibited by specifying the <i>-nr</i> option. </p>
<p> <code>NOTE:</code> This utility is unsupported and may or may not be available in future versions of the JDK. It is not currently available on the Windows 98 and Windows ME platforms. </p>
<h2>Options</h2>
<p>The <code>jstatd</code> command supports the following options: </p>
<dl>
<dd>
<dl>
<dt>-nr</p>
<dd>Do not attempt to create an internal RMI registry within the <i>jstatd</i> process when an existing RMI registry is not found.</p>
<dt>-p&nbsp;<wbr> port</p>
<dd>Port number where the RMI registry is expected to be found, or, if not found, created if <i>-nr</i> is not specified.</p>
<dt>-n&nbsp;<wbr> rminame</p>
<dd>Name to which the remote RMI object is bound in the RMI registry. The default name is <i>JStatRemoteHost</i>. If multiple <code>jstatd</code> servers are started on the same host, the name of the exported RMI object for each server can be made unique by specifying this option. However, doing so will require that the unique server name be included in the monitoring client&#8217;s <i>hostid</i> and <i>vmid</i> strings.</p>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the <code>java</code> launcher called by <code>javac</code>. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. It is a common convention for <code>-J</code> to pass options to the underlying VM executing applications written in Java.</dl>
</dl>
<h2>Security</h2>
<p>The <code>jstatd</code> server can only monitor JVMs for which it has the appropriate native access permissions. Therefor the <code>jstatd</code> process must be running with the same user credentials as the target JVMs. Some user credentials, such as the <i>root</i> user in UNIX(TM) based systems, have permission to access the instrumentation exported by any JVM on the system. A <code>jstatd</code> process running with such credentials can monitor any JVM on the system, but introduces additional security concerns. </p>
<p> The <code>jstatd</code> server does not provide any authentication of remote clients. Therefore, running a <code>jstatd</code> server process exposes the instrumentation export by all JVMs for which the <code>jstatd</code> process has access permissions to any user on the network. This exposure may be undesireable in your environment and local security policies should be considered before starting the <code>jstatd</code> process, particularly in production environments or on unsecure networks. </p>
<p> The <code>jstatd</code> server installs an instance of RMISecurityPolicy if no other security manager has been installed and therefore requires a security policy file to be specified. The policy file must conform to the default policy implementation&#8217;s <i>Policy File Syntax</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/security/PolicyFiles.html.">http://docs.oracle.com/javase/7/docs/technotes/guides/security/PolicyFiles.html.</a> </p>
<p> The following policy file will allow the <code>jstatd</code> server to run without any security exceptions. This policy is less liberal then granting all permissions to all codebases, but is more liberal than a policy that grants the minimal permissions to run the <code>jstatd</code> server. </p>
<pre><code>grant codebase &quot;file:${java.home}/../lib/tools.jar&quot; {</code>
<br>
<code>
 permission java.security.AllPermission;</code>
<br>
<code>
};</code>
<br></pre>
<p>To use this policy, copy the text into a file called <i>jstatd.all.policy</i> and run the <code>jstatd</code> server as follows: </p>
<pre><code>jstatd -J-Djava.security.policy=jstatd.all.policy</code>
<br></pre>
<p>For sites with more restrictive security practices, it is possible to use a custom policy file to limit access to specific trusted hosts or networks, though such techniques are subject to IP addreess spoofing attacks. If your security concerns cannot be addressed with a customized policy file, then the safest action is to not run the <code>jstatd</code> server and use the <code>jstat</code> and <code>jps</code> tools locally. </p>
<h2>Remote Interface</h2>
<p>The interface exported by the <code>jstatd</code> process is proprietary and is guaranteed to change. Users and developers are discouraged from writing to this interface. </p>
<h2>Examples</h2>
<p>Here are some examples of starting <code>jstatd</code>. Note that the <code>jstatd</code> scripts automatically start the server in the background. </p>
<h3>Using Internal RMI Registry</h3>
<p>This example demonstrates starting <code>jstatd</code> with an internal RMI registry. This example assumes that no other server is bound to the default RMI Registry port (port 1099). </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy</code></pre>
<h3>Using External RMI Registry</h3>
<p>This example demonstrates starting <code>jstatd</code> with a external RMI registry. </p>
<pre><code>rmiregistry&amp;
jstatd -J-Djava.security.policy=all.policy</code></pre>
<p>This example demonstrates starting <code>jstatd</code> with an external RMI registry server on port 2020. </p>
<pre><code>rmiregistry 2020&amp;
jstatd -J-Djava.security.policy=all.policy -p 2020</code></pre>
<p>This example demonstrates starting <code>jstatd</code> with an external RMI registry on port 2020, bound to name AlternateJstatdServerName. </p>
<pre><code>rmiregistry 2020&amp;
jstatd -J-Djava.security.policy=all.policy -p 2020 -n AlternateJstatdServerName</code></pre>
<h3>Inhibiting creation of an in-process RMI registry</h3>
<p>This example demonstrates starting <code>jstatd</code> such that it will not create a RMI registry if one is not found. This example assumes an RMI registry is already running. If it is not, an appropriate error message is emitted. </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy -nr</code></pre>
<h3>Enabling RMI logging capabilities.</h3>
<p>This example demonstrates starting <code>jstatd</code> with RMI logging capabilities enabled. This technique is useful as a troubleshooting aid or for monitoring server activities. </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy -J-Djava.rmi.server.logCalls=true</code></pre>
<h2>See Also</h2>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><a href="/docs/linux/man/1-java/">java</a>(1) &#8211; the Java Application Launcher</p>
<dt>o</p>
<dd><a href="/docs/linux/man/1-jps/">jps</a>(1) &#8211; the Java Process Status Application</p>
<dt>o</p>
<dd><a href="/docs/linux/man/1-jstat/">jstat</a>(1) &#8211; the Java Virtual Machine Statistics Monitoring Tool</p>
<dt>o</p>
<dd><i>rmiregistry</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#rmi">http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#rmi</a> &#8211; the Java Remote Object Registry</dl>
</dl>
<p>&nbsp;<wbr></p>
