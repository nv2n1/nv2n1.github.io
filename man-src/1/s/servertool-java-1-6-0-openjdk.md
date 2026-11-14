---
title: "servertool-java-1-6-0-openjdk(1)"
name: "servertool-java-1-6-0-openjdk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-servertool-java-1-6-0-openjdk/"
description: "servertool – The Java(TM) IDL Server Tool"
---

<p>servertool &#8211; The Java(TM) IDL Server Tool </p>
<p> <code>servertool</code> provides a command-line interface for application programmers to register, unregister, startup, and shutdown a persistent server. </p>
<h2>Synopsis</h2>
<pre><code>servertool -ORBInitialPort </code><tt>nameserverport</tt><code>options</code><code> [ </code><code>commands</code><code> ]</code></pre>
<p>If you did not enter a command when starting <i>servertool</i>, the command-line tool displays with a <i>servertool &gt;</i> prompt. Enter commands at the <i>servertool &gt;</i> prompt. </p>
<p> If you enter a command when starting <i>servertool</i>, the Java IDL Server Tool starts, runs the command, and exits. </p>
<p> The <i>-ORBInitialPort</i> <i>nameserverport</i> option is <code>required</code>. The value for <i>nameserverport</i> must specify the port on which <i>orbd</i> is running and listening for incoming requests. When using Solaris software, you must become root to start a process on a port under 1024. For this reason, we recommend that you use a port number greater than or equal to 1024 for the <i>nameserverport</i>. </p>
<h2>Description</h2>
<p>The <i>servertool</i> provides the command-line interface for the application programmers to register, unregister, startup, and shutdown a persistent server. Other commands are provided to obtain various statistical information about the server. </p>
<h2>Options</h2>
<dl COMPACT>
<dt>-ORBInitialHost nameserverhost</p>
<dd>Specifies the host machine on which the name server is running and listening for incoming requests. The <i>nameserverhost</i> defaults to <i>localhost</i> if this option is not specified. If <i>orbd</i> and <i>servertool</i> are running on different machines, you must specify the name or IP address of the host on which <i>orbd</i> is running.</p>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <i>java a pplication launcher</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html.">http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html.</a> For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. It is a common convention for <code>-J</code> to pass options to the underlying virtual machine.</dl>
<h2>Commands</h2>
<dl COMPACT>
<dt>register -server&nbsp;<wbr>&lt;server class name&gt;</p>
<dd>&nbsp;<wbr>-classpath&nbsp;<wbr>&lt;classpath to server&gt; [&nbsp;<wbr>-applicationName&nbsp;<wbr>&lt;application name&gt; -args&nbsp;<wbr>&lt;args to server&gt; -vmargs&nbsp;<wbr>&lt;flags to be passed to Java VM&gt; &nbsp;<wbr>] Register a new persistent server with the Object Request Broker Daemon (ORBD). If the server is not already registered, it is registered and activated. This command causes an install method to be invoked in the main class of the server identified by the <i>-server</i> option. The install method must be <i>public static void install(org.omg.CORBA.ORB)</i>. The install method is optional and enables the developer to provide their own server installation behavior (for example, creating database schema).</p>
<dt>unregister</p>
<dd>-serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>| -applicationName&nbsp;<wbr>&lt;application name&gt; Unregister a server from the ORBD by using either its server id or its application name. This command causes an uninstall method to be invoked in the main class of the server identified by the <i>-server</i> option. The uninstall method must be <i>public static void uninstall(org.omg.CORBA.ORB)</i>. The uninstall method is optional and enables the developer to provide their own server uninstall behavior (for example, undoing the behavior of the install method).</p>
<dt>getserverid</p>
<dd>-applicationName&nbsp;<wbr>&lt;application name&gt; Return the server id that corresponds with an application.</p>
<dt>list</p>
<dd>List information about all persistent servers registered with the ORBD.</p>
<dt>listappnames</p>
<dd>List the application names for all servers currently registered with the ORBD.</p>
<dt>listactive</p>
<dd>List information about all persistent servers that have been launched by the ORBD and are currently running.</p>
<dt>locate -serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>|</p>
<dd>-applicationName&nbsp;<wbr>&lt;application name&gt; [-endpointType&nbsp;<wbr>&lt;endpointType&gt;&nbsp;<wbr>] Locate the endpoints (ports) of a specific type for all ORBs created by a registered server. If a server is not already running, it is activated. If an endpoint type is not specified, then the plain/non-protected endpoint associated with each ORB in a server is returned.</p>
<dt>locateperorb</p>
<dd>-serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>| -applicationName&nbsp;<wbr>&lt;application name&gt; [-orbid&nbsp;<wbr>&lt;ORB name&gt;&nbsp;<wbr>] Locate all the endpoints (ports) registered by a specific ORB of registered server. If a server is not already running, then it is activated. If an <i>orbid</i> is not specified, the default value of &quot;&quot; is assigned to the <i>orbid</i>. If any ORBs are created with an <i>orbid</i> of empty string, all ports registered by it are returned.</p>
<dt>orblist -serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>|</p>
<dd>-applicationName&nbsp;<wbr>&lt;application name&gt; Lists the ORBId of the ORBs defined on a server. An ORBId is the string name for the ORB created by the server. If the server is not already running, it is activated.</p>
<dt>shutdown -serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>|</p>
<dd>-applicationName&nbsp;<wbr>&lt;application name&gt; Shutdown an active server that is registered with ORBD. During execution of this command, the <i>shutdown()</i> method defined in the class specified by either the <i>-serverid</i> or <i>-applicationName</i> parameter is also invoked to shutdown the server process appropriately.</p>
<dt>startup -serverid&nbsp;<wbr>&lt;server id&nbsp;<wbr>&gt;&nbsp;<wbr>|</p>
<dd>-applicationName&nbsp;<wbr>&lt;application name&gt; Startup or activate a server that is registered with ORBD. If the server is not running, this command launches the server. If the server is already running, an error message is returned to the user.</p>
<dt>help</p>
<dd>List all the commands available to the server through the server tool.</p>
<dt>quit</p>
<dd>Exit the server tool.</dl>
<h2>See Also</h2>
<p>orbd </p>
<p>&nbsp;<wbr></p>
