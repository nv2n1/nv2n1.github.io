---
title: "rmid-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "rmid-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmid-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "rmid – Starts the activation system daemon that enables objects to be registered and activated in a Java Virtual Machine (JVM)."
---

<p>rmid &#8211; Starts the activation system daemon that enables objects to be registered and activated in a Java Virtual Machine (JVM).</p>
<h2>Synopsis</h2>
<pre><code>rmid</code> [<i>options</i>]</pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</dl>
<h2>Description</h2>
<p>The <code>rmid</code> command starts the activation system daemon. The activation system daemon must be started before activatable objects can be either registered with the activation system or activated in a JVM. For details on how to write programs that use activatable objects, the <i>Using Activation</i> tutorial at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/rmi/activation/overview.html">http://docs.oracle.com/javase/8/docs/technotes/guides/rmi/activation/overview.html</a> </p>
<p> Start the daemon by executing the <code>rmid</code> command and specifying a security policy file, as follows: </p>
<pre><code>rmid -J-Djava.security.policy=rmid.policy</code></pre>
<p>When you run Oracle&#8217;s implementation of the <code>rmid</code> command, by default you must specify a security policy file so that the <code>rmid</code> command can verify whether or not the information in each <code>ActivationGroupDesc</code> is allowed to be used to start a JVM for an activation group. Specifically, the command and options specified by the <code>CommandEnvironment</code> and any properties passed to an <code>ActivationGroupDesc</code> constructor must now be explicitly allowed in the security policy file for the <code>rmid</code> command. The value of the <code>sun.rmi.activation.execPolicy</code> property dictates the policy that the <code>rmid</code> command uses to determine whether or not the information in an <code>ActivationGroupDesc</code> can be used to start a JVM for an activation group. For more information see the description of the -J-Dsun.rmi.activation.execPolicy=policy option. </p>
<p> Executing the <code>rmid</code> command starts the Activator and an internal registry on the default port1098 and binds an <code>ActivationSystem</code> to the name <code>java.rmi.activation.ActivationSystem</code> in this internal registry. </p>
<p> To specify an alternate port for the registry, you must specify the <code>-port</code> option when you execute the <code>rmid</code> command. For example, the following command starts the activation system daemon and a registry on the registry&#8217;s default port, 1099. </p>
<pre><code>rmid -J-Djava.security.policy=rmid.policy -port 1099</code></pre>
<h2>Start Rmid On Demand</h2>
<p>An alternative to starting <code>rmid</code> from the command line is to configure <code>inetd</code> (Oracle Solaris) or <code>xinetd</code> (Linux) to start <code>rmid</code> on demand. </p>
<p> When RMID starts, it attempts to obtain an inherited channel (inherited from <code>inetd</code>/<code>xinetd</code>) by calling the <code>System.inheritedChannel</code> method. If the inherited channel is null or not an instance of <code>java.nio.channels.ServerSocketChannel</code>, then RMID assumes that it was not started by <code>inetd</code>/<code>xinetd</code>, and it starts as previously described. </p>
<p> If the inherited channel is a <code>ServerSocketChannel</code> instance, then RMID uses the <code>java.net.ServerSocket</code> obtained from the <code>ServerSocketChannel</code> as the server socket that accepts requests for the remote objects it exports: The registry in which the <code>java.rmi.activation.ActivationSystem</code> is bound and the <code>java.rmi.activation.Activator</code> remote object. In this mode, RMID behaves the same as when it is started from the command line, except in the following cases:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Output printed to <code>System.err</code> is redirected to a file. This file is located in the directory specified by the <code>java.io.tmpdir</code> system property (typically <code>/var/tmp</code> or <code>/tmp</code>) with the prefix <code>rmid-err</code> and the suffix <code>tmp</code>.</p>
<dt>&bull;</p>
<dd>The <code>-port</code> option is not allowed. If this option is specified, then RMID exits with an error message.</p>
<dt>&bull;</p>
<dd>The <code>-log</code> option is required. If this option is not specified, then RMID exits with an error message</dl>
<p> See the man pages for <code>inetd</code> (Oracle Solaris) or <code>xinetd</code> (Linux) for details on how to configure services to be started on demand.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-C<i>option</i></p>
<dd>Specifies an option that is passed as a command-line argument to each child process (activation group) of the <code>rmid</code> command when that process is created. For example, you could pass a property to each virtual machine spawned by the activation system daemon: </p>
<pre><code>rmid -C-Dsome.property=value</code></pre>
<p>This ability to pass command-line arguments to child processes can be useful for debugging. For example, the following command enables server-call logging in all child JVMs. </p>
<pre><code>rmid -C-Djava.rmi.server.logCalls=true</code></pre>
<dt>-J<i>option</i></p>
<dd>Specifies an option that is passed to the Java interpreter running RMID. For example, to specify that the <code>rmid</code> command use a policy file named <code>rmid.policy</code>, the <code>-J</code> option can be used to define the <code>java.security.policy</code> property on the <code>rmid</code> command line, for example: </p>
<pre><code>rmid -J-Djava.security.policy-rmid.policy</code></pre>
<dt>-J-Dsun.rmi.activation.execPolicy=<i>policy</i></p>
<dd>Specifies the policy that RMID employs to check commands and command-line options used to start the JVM in which an activation group runs. Please note that this option exists only in Oracle&#8217;s implementation of the Java RMI activation daemon. If this property is not specified on the command line, then the result is the same as though <code>-J-Dsun.rmi.activation.execPolicy=default</code> were specified. The possible values of <code>policy</code> can be <code>default</code>, <code>policyClassName</code>, or <code>none</code>.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>default </p>
<p> The <code>default</code> or unspecified value <code>execPolicy</code> allows the <code>rmid</code> command to execute commands with specific command-line options only when the <code>rmid</code> command was granted permission to execute those commands and options in the security policy file that the <code>rmid</code> command uses. Only the default activation group implementation can be used with the default execution policy. </p>
<p> The <code>rmid</code> command starts a JVM for an activation group with the information in the group&#8217;s registered activation group descriptor, an <code>ActivationGroupDesc</code>. The group descriptor specifies an optional <code>ActivationGroupDesc.CommandEnvironment</code> that includes the command to execute to start the activation group and any command-line options to be added to the command line. By default, the <code>rmid</code> command uses the <code>java</code> command found in <code>java.home</code>. The group descriptor also contains properties overrides that are added to the command line as options defined as: <code>-D&lt;property&gt;=&lt;value&gt;</code>.The <code>com.sun.rmi.rmid.ExecPermission</code> permission grants the <code>rmid</code> command permission to execute a command that is specified in the group descriptor&#8217;s <code>CommandEnvironment</code> to start an activation group. The <code>com.sun.rmi.rmid.ExecOptionPermission</code> permission enables the <code>rmid</code> command to use command-line options, specified as properties overrides in the group descriptor or as options in the <code>CommandEnvironment</code> when starting the activation group.When granting the <code>rmid</code> command permission to execute various commands and options, the permissions <code>ExecPermission</code> and <code>ExecOptionPermission</code> must be granted to all code sources. </p>
<p> <i>ExecPermission</i> </p>
<p> The <code>ExecPermission</code> class represents permission for the <code>rmid</code> command to execute a specific command to start an activation group. </p>
<p> <i>Syntax</i>: The name of an <code>ExecPermission</code> is the path name of a command to grant the <code>rmid</code> command permission to execute. A path name that ends in a slash (/) and an asterisk (*) indicates that all of the files contained in that directory where slash is the file-separator character, <code>File.separatorChar</code>. A path name that ends in a slash (/) and a minus sign (-) indicates all files and subdirectories contained in that directory (recursively). A path name that consists of the special token <code>&lt;&lt;ALL FILES&gt;&gt;</code> matches any file. </p>
<p> A path name that consists of an asterisk (*) indicates all the files in the current directory. A path name that consists of a minus sign (-) indicates all the files in the current directory and (recursively) all files and subdirectories contained in the current directory. </p>
<p> <i>ExecOptionPermission</i> </p>
<p> The <code>ExecOptionPermission</code> class represents permission for the <code>rmid</code> command to use a specific command-line option when starting an activation group. The name of an <code>ExecOptionPermission</code> is the value of a command-line option. </p>
<p> <i>Syntax</i>: Options support a limited wild card scheme. An asterisk signifies a wild card match, and it can appear as the option name itself (matches any option), or an asterisk (*) can appear at the end of the option name only when the asterisk (*) follows a dot (.) or an equals sign (=). </p>
<p> For example: <code>*</code> or <code>-Dmydir.*</code> or <code>-Da.b.c=*</code> is valid, but <code>*mydir</code> or <code>-Da*b</code> or <code>ab*</code> is not. </p>
<p> <i>Policy file for rmid</i> </p>
<p> When you grant the <code>rmid</code> command permission to execute various commands and options, the permissions <code>ExecPermission</code> and <code>ExecOptionPermission</code> must be granted to all code sources (universally). It is safe to grant these permissions universally because only the <code>rmid</code> command checks these permissions. </p>
<p> An example policy file that grants various execute permissions to the <code>rmid</code> command is: </p>
<pre><code>grant {</code></pre>
<pre><code> permission com.sun.rmi.rmid.ExecPermission</code></pre>
<pre><code> &quot;/files/apps/java/jdk1.7.0/solaris/bin/java&quot;;</code></pre>
<pre><code> permission com.sun.rmi.rmid.ExecPermission</code></pre>
<pre><code> &quot;/files/apps/rmidcmds/*&quot;;</code></pre>
<pre><code> permission com.sun.rmi.rmid.ExecOptionPermission</code></pre>
<pre><code> &quot;-Djava.security.policy=/files/policies/group.policy&quot;;</code></pre>
<pre><code> permission com.sun.rmi.rmid.ExecOptionPermission</code></pre>
<pre><code> &quot;-Djava.security.debug=*&quot;;</code></pre>
<pre><code> permission com.sun.rmi.rmid.ExecOptionPermission</code></pre>
<pre><code> &quot;-Dsun.rmi.*&quot;;</code></pre>
<pre><code>};</code></pre>
<p>The first permission granted allows the <code>rmid</code> tcommand o execute the 1.7.0 release of the <code>java</code> command, specified by its explicit path name. By default, the version of the <code>java</code> command found in <code>java.home</code> is used (the same one that the <code>rmid</code> command uses), and does not need to be specified in the policy file. The second permission allows the <code>rmid</code> command to execute any command in the directory <code>/files/apps/rmidcmds</code>. </p>
<p> The third permission granted, an <code>ExecOptionPermission</code>, allows the <code>rmid</code> command to start an activation group that defines the security policy file to be <code>/files/policies/group.policy</code>. The next permission allows the <code>java.security.debug property</code> to be used by an activation group. The last permission allows any property in the <code>sun.rmi property</code> name hierarchy to be used by activation groups. </p>
<p> To start the <code>rmid</code> command with a policy file, the <code>java.security.policy</code> property needs to be specified on the <code>rmid</code> command line, for example: </p>
<p> <code>rmid -J-Djava.security.policy=rmid.policy</code>.</p>
<dt>&bull;</p>
<dd>&lt;policyClassName&gt; </p>
<p> If the default behavior is not flexible enough, then an administrator can provide, when starting the <code>rmid</code> command, the name of a class whose <code>checkExecCommand</code> method is executed to check commands to be executed by the <code>rmid</code> command. </p>
<p> The <code>policyClassName</code> specifies a public class with a public, no-argument constructor and an implementation of the following <code>checkExecCommand</code> method: </p>
<pre><code> public void checkExecCommand(ActivationGroupDesc desc, String[] command)</code></pre>
<pre><code> throws SecurityException;</code></pre>
<p>Before starting an activation group, the <code>rmid</code> command calls the policy&#8217;s <code>checkExecCommand</code> method and passes to it the activation group descriptor and an array that contains the complete command to start the activation group. If the <code>checkExecCommand</code> throws a <code>SecurityException</code>, then the <code>rmid</code> command does not start the activation group and an <code>ActivationException</code> is thrown to the caller attempting to activate the object.</p>
<dt>&bull;</p>
<dd>none </p>
<p> If the <code>sun.rmi.activation.execPolicy</code> property value is <code>none</code>, then the <code>rmid</code> command does not perform any validation of commands to start activation groups.</dl>
</dl>
<dt>-log <i>dir</i></p>
<dd>Specifies the name of the directory the activation system daemon uses to write its database and associated information. The log directory defaults to creating a log, in the directory in which the <code>rmid</code> command was executed.</p>
<dt>-port <i>port</i></p>
<dd>Specifies the port the registry uses. The activation system daemon binds the <code>ActivationSystem</code>, with the name <code>java.rmi.activation.ActivationSystem</code>, in this registry. The <code>ActivationSystem</code> on the local machine can be obtained using the following <code>Naming.lookup</code> method call: </p>
<pre><code>import java.rmi.*; </code></pre>
<pre><code> import java.rmi.activation.*;</code></pre>
<pre><code> ActivationSystem system; system = (ActivationSystem)</code></pre>
<pre><code> Naming.lookup(&quot;//:port/java.rmi.activation.ActivationSystem&quot;);</code></pre>
<dt>-stop</p>
<dd>Stops the current invocation of the <code>rmid</code> command for a port specified by the <code>-port</code> option. If no port is specified, then this option stops the <code>rmid</code> invocation running on port 1098.</dl>
<h2>Environment Variables</h2>
<dl COMPACT>
<dt>CLASSPATH</p>
<dd>Used to provide the system a path to user-defined classes. Directories are separated by colons, for example: <code>.:/usr/local/java/classes</code>.</dl>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd>Setting the Class Path </p>
</dl>
