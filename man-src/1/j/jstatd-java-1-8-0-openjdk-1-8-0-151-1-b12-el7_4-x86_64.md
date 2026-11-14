---
title: "jstatd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64(1)"
name: "jstatd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jstatd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64/"
description: "jstatd – Monitors Java Virtual Machines (JVMs) and enables remote monitoring tools to attach to JVMs. This command is experimental and unsupported."
---

<p>jstatd &#8211; Monitors Java Virtual Machines (JVMs) and enables remote monitoring tools to attach to JVMs. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jstatd</code> [ <i>options</i> ]</pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</dl>
<h2>Description</h2>
<p>The <code>jstatd</code> command is an RMI server application that monitors for the creation and termination of instrumented Java HotSpot VMs and provides an interface to enable remote monitoring tools to attach to JVMs that are running on the local host. </p>
<p> The <code>jstatd</code> server requires an RMI registry on the local host. The <code>jstatd</code> server attempts to attach to the RMI registry on the default port, or on the port you specify with the <code>-p</code><code>port</code> option. If an RMI registry is not found, then one is created within the <code>jstatd</code> application that is bound to the port that is indicated by the <code>-p</code><code>port</code> option or to the default RMI registry port when the <code>-p</code><code>port</code> option is omitted. You can stop the creation of an internal RMI registry by specifying the <code>-nr</code> option.</p>
<h2>Options</h2>
<dl>
<dt>-nr</p>
<dd>Does not attempt to create an internal RMI registry within the <code>jstatd</code> process when an existing RMI registry is not found.</p>
<dt>-p <i>port</i></p>
<dd>The port number where the RMI registry is expected to be found, or when not found, created if the <code>-nr</code> option is not specified.</p>
<dt>-n <i>rminame</i></p>
<dd>Name to which the remote RMI object is bound in the RMI registry. The default name is <code>JStatRemoteHost</code>. If multiple <code>jstatd</code> servers are started on the same host, then the name of the exported RMI object for each server can be made unique by specifying this option. However, doing so requires that the unique server name be included in the monitoring client&#8217;s <code>hostid</code> and <code>vmid</code> strings.</p>
<dt>-J<i>option</i></p>
<dd>Passes <code>option</code> to the JVM, where option is one of the <code>options</code> described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>Security</h2>
<p>The <code>jstatd</code> server can only monitor JVMs for which it has the appropriate native access permissions. Therefore, the <code>jstatd</code> process must be running with the same user credentials as the target JVMs. Some user credentials, such as the root user in UNIX-based systems, have permission to access the instrumentation exported by any JVM on the system. A <code>jstatd</code> process running with such credentials can monitor any JVM on the system, but introduces additional security concerns. </p>
<p> The <code>jstatd</code> server does not provide any authentication of remote clients. Therefore, running a <code>jstatd</code> server process exposes the instrumentation export by all JVMs for which the <code>jstatd</code> process has access permissions to any user on the network. This exposure might be undesirable in your environment, and therefore, local security policies should be considered before you start the <code>jstatd</code> process, particularly in production environments or on networks that are not secure. </p>
<p> The <code>jstatd</code> server installs an instance of <code>RMISecurityPolicy</code> when no other security manager is installed, and therefore, requires a security policy file to be specified. The policy file must conform to Default Policy Implementation and Policy File Syntax at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html">http://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html</a> </p>
<p> The following policy file allows the <code>jstatd</code> server to run without any security exceptions. This policy is less liberal than granting all permissions to all code bases, but is more liberal than a policy that grants the minimal permissions to run the <code>jstatd</code> server. </p>
<pre><code>grant codebase &quot;file:${java.home}/../lib/tools.jar&quot; { </code></pre>
<pre><code> permission java.security.AllPermission;</code></pre>
<pre><code>};</code></pre>
<p>To use this policy setting, copy the text into a file called <code>jstatd.all.policy</code> and run the <code>jstatd</code> server as follows: </p>
<pre><code>jstatd -J-Djava.security.policy=jstatd.all.policy</code></pre>
<p>For sites with more restrictive security practices, it is possible to use a custom policy file to limit access to specific trusted hosts or networks, though such techniques are subject to IP address spoofing attacks. If your security concerns cannot be addressed with a customized policy file, then the safest action is to not run the <code>jstatd</code> server and use the <code>jstat</code> and <code>jps</code> tools locally.</p>
<h2>Remote Interface</h2>
<p>The interface exported by the <code>jstatd</code> process is proprietary and guaranteed to change. Users and developers are discouraged from writing to this interface.</p>
<h2>Examples</h2>
<p>The following are examples of the <code>jstatd</code> command. The <code>jstatd</code> scripts automatically start the server in the background</p>
<h3>Internal Rmi Registry</h3>
<p>This example shows hos to start a <code>jstatd</code> session with an internal RMI registry. This example assumes that no other server is bound to the default RMI registry port (port 1099). </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy</code></pre>
<h3>External Rmi Registry</h3>
<p>This example starts a <code>jstatd</code> session with a external RMI registry. </p>
<pre><code>rmiregistry&amp;</code></pre>
<pre><code>jstatd -J-Djava.security.policy=all.policy</code></pre>
<p>This example starts a <code>jstatd</code> session with an external RMI registry server on port 2020. </p>
<pre><code>jrmiregistry 2020&amp;</code></pre>
<pre><code>jstatd -J-Djava.security.policy=all.policy -p 2020</code></pre>
<p>This example starts a <code>jstatd</code> session with an external RMI registry on port 2020 that is bound to <code>AlternateJstatdServerName</code>. </p>
<pre><code>rmiregistry 2020&amp;</code></pre>
<pre><code>jstatd -J-Djava.security.policy=all.policy -p 2020</code></pre>
<pre><code> -n AlternateJstatdServerName</code></pre>
<h3>Stop The Creation Of An In-Process Rmi Registry</h3>
<p>This example starts a <code>jstatd</code> session that does not create an RMI registry when one is not found. This example assumes an RMI registry is already running. If an RMI registry is not running, then an error message is displayed. </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy -nr</code></pre>
<h3>Enable Rmi Logging</h3>
<p>This example starts a <code>jstatd</code> session with RMI logging capabilities enabled. This technique is useful as a troubleshooting aid or for monitoring server activities. </p>
<pre><code>jstatd -J-Djava.security.policy=all.policy</code></pre>
<pre><code> -J-Djava.rmi.server.logCalls=true</code></pre>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jps/">jps</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-jstat/">jstat</a>(1)</p>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-rmiregistry/">rmiregistry</a>(1) </p>
</dl>
