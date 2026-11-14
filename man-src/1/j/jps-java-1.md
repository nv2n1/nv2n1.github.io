---
title: "jps-java-1(1)"
name: "jps-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jps-java-1/"
description: "jps – Java Virtual Machine Process Status Tool"
---

<h2>Name</h2>
<p> jps &#8211; Java Virtual Machine Process Status Tool </p>
<h2>SYNOPSIS</h2>
<pre><code>
jps[options][hostid]
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>options</p>
<dd> Command-line options.</p>
<dt>hostid</p>
<dd> The host identifier of the host for which the process report should be generated. The <i>hostid</i> may include optional components that indicate the communications protocol, port number, and other implementation specific data.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>jps</code> tool lists the instrumented HotSpot Java Virtual Machines (JVMs) on the target system. The tool is limited to reporting information on JVMs for which it has the access permissions. </p>
<p> If <code>jps</code> is run without specifying a <i>hostid</i>, it will look for instrumented JVMs on the local host. If started with a <i>hostid</i>, it will look for JVMs on the indicated host, using the specified protocol and port. A <code>jstatd</code> process is assumed to be running on the target host. </p>
<p> The <code>jps</code> command will report the local VM identifier, or <i>lvmid</i>, for each instrumented JVM found on the target system. The <code>lvmid</code> is typically, but not necessarily, the operating system&#8217;s process identifier for the JVM process. With no options, <code>jps</code> will list each Java application&#8217;s <i>lvmid</i> followed by the short form of the application&#8217;s class name or jar file name. The short form of the class name or JAR file name omits the class&#8217;s package information or the JAR files path information. </p>
<p> The <code>jps</code> command uses the <code>java</code> launcher to find the class name and arguments passed to the <i>main</i> method. If the target JVM is started with a custom launcher, the class name (or JAR file name) and the arguments to the <i>main</i> method will not be available. In this case, the <code>jps</code> command will output the string <i>Unknown</i> for the class name or JAR file name and for the arguments to the main method. </p>
<p> The list of JVMs produced by the <code>jps</code> command may be limited by the permissions granted to the principal running the command. The command will only list the JVMs for which the principle has access rights as determined by operating system specific access control mechanisms. </p>
<p> <code>NOTE:</code> This utility is unsupported and may not be available in future versions of the JDK. It is not currently available on Windows 98 and Windows ME platforms. </p>
<h2>OPTIONS</h2>
<p> The <code>jps</code> command supports a number of options that modify the output of the command. These options are subject to change or removal in the future. </p>
<dl>
<dt>
<dd>
<dl>
<dt>-q</p>
<dd> Suppress the output of the class name, JAR file name, and arguments passed to the <i>main</i> method, producing only a list of local VM identifiers.</p>
<dt>-m</p>
<dd> Output the arguments passed to the main method. The output may be null for embedded JVMs.</p>
<dt>-l</p>
<dd> Output the full package name for the application&#8217;s main class or the full path name to the application&#8217;s JAR file.</p>
<dt>-v</p>
<dd> Output the arguments passed to the JVM.</p>
<dt>-V</p>
<dd> Output the arguments passed to the JVM through the flags file (the .hotspotrc file or the file specified by the -XX:Flags=&lt;<i>filename</i>&gt; argument).</p>
<dt>-Joption</p>
<dd> Pass <i>option</i> to the <code>java</code> launcher called by <code>jps</code>. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. It is a common convention for <code>-J</code> to pass options to the underlying VM executing applications written in Java.</dl>
</dl>
<h3>HOST IDENTIFIER</h3>
<p> The host identifier, or <i>hostid</i> is a string that indicates the target system. The syntax of the <i>hostid</i> string largely corresponds to the syntax of a URI: </p>
<p>[protocol:][[//]hostname][:port][/servername]</p>
<dl>
<dt>
<dd>
<dl>
<dt>protocol</p>
<dd> The communications protocol. If the <i>protocol</i> is omitted and a <i>hostname</i> is not specified, the default protocol is a platform specific, optimized, local protocol. If the <i>protocol</i> is omitted and a <i>hostname</i> is specified, then the default protocol is <code>rmi</code>.</p>
<dt>hostname</p>
<dd> A hostname or IP address indicating the target host. If <i>hostname</i> is omitted, then the target host is the local host.</p>
<dt>port</p>
<dd> The default port for communicating with the remote server. If the <i>hostname</i> is omitted or the <i>protocol</i> specifies an optimized, local protocol, then <i>port</i> is ignored. Otherwise, treatment of the <i>port</i> parameter is implementation specific. For the default <code>rmi</code> protocol the <i>port</i> indicates the port number for the rmiregistry on the remote host. If <i>port</i> is omitted, and <i>protocol</i> indicates <code>rmi</code>, then the default rmiregistry port (1099) is used.</p>
<dt>servername</p>
<dd> The treatment of this parameter depends on the implementation. For the optimized, local protocol, this field is ignored. For the <code>rmi</code> protocol, this parameter is a string representing the name of the RMI remote object on the remote host. See the <code>-n</code> option for the <a href="/docs/linux/man/1-jstatd/">jstatd</a>(1) command.</dl>
</dl>
<h2>OUTPUT FORMAT</h2>
<p> The output of the <code>jps</code> command follows the following pattern: </p>
<pre><code>
lvmid [[classname | JARfilename | "Unknown"] [arg * ] [jvmarg * ]]
</code></pre>
<p> Where all output tokens are separated by white space. An <i>arg</i> that includes embedded white space will introduce ambiguity when attempting to map arguments to their actual positional parameters. </p>
<p> <code>NOTE</code>: You are advised not to write scripts to parse <code>jps</code> output since the format may change in future releases. If you choose to write scripts that parse <code>jps</code> output, expect to modify them for future releases of this tool. </p>
<h2>EXAMPLES</h2>
<p> This section provides examples of the <code>jps</code> command. </p>
<p> Listing the instrumented JVMs on the local host: </p>
<pre>
<code>jps</code>
<br>
18027 Java2Demo.JAR
<br>
18032 jps
<br>
18005 jstat
<br>
</pre>
<p> Listing the instrumented JVMs on a remote host: </p>
<p> This example assumes that the <code>jstat</code> server and either the its internal RMI registry or a separate external <code>rmiregistry</code> process are running on the remote host on the default port (port 1099). It also assumes that the local host has appropriate permissions to access the remote host. This example also includes the <i>-l</i> option to output the long form of the class names or JAR file names. </p>
<pre>
<code>jps -l remote.domain</code>
<br>
3002 /opt/jdk1.7.0/demo/jfc/Java2D/Java2Demo.JAR
<br>
2857 sun.tools.jstatd.jstatd
<br>
</pre>
<p> Listing the instrumented JVMs on a remote host with a non-default port for the RMI registry </p>
<p> This example assumes that the <code>jstatd</code> server, with an internal RMI registry bound to port 2002, is running on the remote host. This example also uses the <i>-m</i> option to include the arguments passed to the <i>main</i> method of each of the listed Java applications. </p>
<pre>
<code>jps -m remote.domain:2002</code>
<br>
3002 /opt/jdk1.7.0/demo/jfc/Java2D/Java2Demo.JAR
<br>
3102 sun.tools.jstatd.jstatd -p 2002
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1) &#8211; the Java Application Launcher</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jstat/">jstat</a>(1) &#8211; the Java virtual machine Statistics Monitoring Tool</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jstatd/">jstatd</a>(1) &#8211; the jstat daemon</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-rmiregistry/">rmiregistry</a>(1) &#8211; the Java Remote Object Registry</dl>
</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
