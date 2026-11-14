---
title: "servertool-java-1(1)"
name: "servertool-java-1"
section: "1"
letter: "s"
url: "/docs/linux/man/1-servertool-java-1/"
description: "servertool – Provides an easy-to-use interface for developers to register, unregister, start up, and shut down a persistent server."
---

<h2>NAME</h2>
<p> servertool &#8211; Provides an easy-to-use interface for developers to register, unregister, start up, and shut down a persistent server.</p>
<h2>SYNOPSIS</h2>
<pre><code>
servertool - ORBInitialPort nameserverport[options][commands]
</code></pre>
<dl>
<dt><i>options</i></p>
<dd> The command-line options. See Options.</p>
<dt>commands</p>
<dd> The command-line commands. See Commands.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>servertool</code> command provides the command-line interface for developers to register, unregister, start up, and shut down a persistent server. Command-line commands let you obtain various statistical information about the server. See Commands.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-ORBInitialHost <i>nameserverhost</i></p>
<dd>
 This options is required. It specifies the host machine on which the name server runs and listens for incoming requests. The <code>nameserverhost</code> value must specify the port on which the <code>orb</code> is running and listening for requests. The value defaults to <code>localhost</code> when this option is not specified. If <code>orbd</code> and <code>servertool</code> are running on different machines, then you must specify the name or IP address of the host on which <code>orbd</code> is running. </p>
<p> <i>Note:</i> On Oracle Solaris, you must become a root user to start a process on a port below 1024. Oracle recommends that you use a port number above or equal to 1024 for the <code>nameserverport</code> value.</p>
<dt>-J<i>option</i></p>
<dd>
 Passes <code>option</code> to the Java Virtual Machine, where <code>option</code> is one of the options described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>COMMANDS</h2>
<p> You can start the <code>servertool</code> command with or without a command-line command.</p>
<dl>
<dt>&bull;</p>
<dd> If you did not specify a command when you started <code>servertool</code>, then the command-line tool displays the <code>servertool</code> prompt where you can enter commands: <code>servertool &gt;</code>.</p>
<dt>&bull;</p>
<dd> If you specify a command when you start <code>servertool</code>, then the Java IDL Server Tool starts, executes the command, and exits.</p>
<dt>
<dd> register -server <i>server-class-name</i> -classpath <i>classpath-to-server</i> [ -applicationName <i>application-name</i> -args <i>args-to-server</i> -vmargs <i>flags-for-JVM</i> ] Registers a new persistent server with the Object Request Broker Daemon (ORBD). If the server is not already registered, then it is registered and activated. This command causes an installation method to be called in the <code>main</code> class of the server identified by the <code>-server</code> option. The installation method must be <code>public static void install(org.omg.CORBA.ORB)</code>. The install method is optional and lets developers provide their own server installation behavior, such as creating a database schema.</p>
<dt>
<dd> unregister -serverid <i>server-id</i> | -applicationName <i>application-name</i> Unregisters a server from the ORBD with either its server ID or its application name. This command causes an uninstallation method to be called in the <code>main</code> class of the server identified by the <code>-server</code> option. The <code>uninstall</code> method must be <code>public static void uninstall(org.omg.CORBA.ORB)</code>. The <code>uninstall</code> method is optional and lets developers provide their own server uninstallation behavior, such as undoing the behavior of the <code>install</code> method.</p>
<dt>getserverid -applicationName <i>application-name</i></p>
<dd> Returns the server ID that corresponds to the <code>application-name</code> value.</p>
<dt>list</p>
<dd> Lists information about all persistent servers registered with the ORBD.</p>
<dt>listappnames</p>
<dd> Lists the application names for all servers currently registered with the ORBD.</p>
<dt>listactive</p>
<dd> Lists information about all persistent servers that were started by the ORBD and are currently running.</p>
<dt>
<dd> locate -serverid <i>server-id</i> | -applicationName <i>application-name</i> [ -endpointType <i>endpointType</i> ] Locates the endpoints (ports) of a specific type for all ORBs created by a registered server. If a server is not already running, then it is activated. If an <code>endpointType</code> value is not specified, then the plain/non-protected endpoint associated with each ORB in a server is returned.</p>
<dt>
<dd> locateperorb -serverid <i>server-id</i> | -applicationName <i>application-name</i> [ -orbid <i>ORB-name</i> ] Locates all the endpoints (ports) registered by a specific Object Request Broker (ORB) of registered server. If a server is not already running, then it is activated. If an <code>orbid</code> is not specified, then the default value of <code>&quot;&quot;</code> is assigned to the <code>orbid</code>. If any ORBs are created with an <code>orbid</code> of empty string, then all ports registered by it are returned.</p>
<dt>orblist -serverid <i>server-id</i> | -applicationName <i>application-name</i></p>
<dd> Lists the <code>ORBId</code> of the ORBs defined on a server. An <code>ORBId</code> is the string name for the ORB created by the server. If the server is not already running, then it is activated.</p>
<dt>shutdown -serverid <i>server-id</i> | -applicationName application-name</p>
<dd> Shut down an active server that is registered with ORBD. During execution of this command, the <code>shutdown</code> method defined in the class specified by either the <code>-serverid</code> or <code>-applicationName</code> parameter is also called to shut down the server process.</p>
<dt>startup -serverid <i>server-id</i> | -applicationName application-name</p>
<dd> Starts up or activate a server that is registered with ORBD. If the server is not running, then this command starts the server. If the server is already running, then an error message is displayed.</p>
<dt>help</p>
<dd> Lists all the commands available to the server through the <code>servertool</code> command.</p>
<dt>quit</p>
<dd> Exits the <code>servertool</code> command.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-orbd/">orbd</a>(1) </p>
</dl>
<h2>Index</h2>
