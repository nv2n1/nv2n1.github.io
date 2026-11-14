---
title: "orbd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64(1)"
name: "orbd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orbd-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64/"
description: "orbd – Enables clients to locate and call persistent objects on servers in the CORBA environment."
---

<p>orbd &#8211; Enables clients to locate and call persistent objects on servers in the CORBA environment.</p>
<h2>Synopsis</h2>
<pre><code>orbd</code> [ <i>options</i> ]</pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>Command-line options. See Options.</dl>
<h2>Description</h2>
<p>The <code>orbd</code> command enables clients to transparently locate and call persistent objects on servers in the CORBA environment. The Server Manager included with the orbd tool is used to enable clients to transparently locate and call persistent objects on servers in the CORBA environment. The persistent servers, while publishing the persistent object references in the naming service, include the port number of the ORBD in the object reference instead of the port number of the server. The inclusion of an ORBD port number in the object reference for persistent object references has the following advantages:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The object reference in the naming service remains independent of the server life cycle. For example, the object reference could be published by the server in the Naming Service when it is first installed, and then, independent of how many times the server is started or shut down, the ORBD returns the correct object reference to the calling client.</p>
<dt>&bull;</p>
<dd>The client needs to look up the object reference in the naming service only once, and can keep reusing this reference independent of the changes introduced due to server life cycle.</dl>
<p> To access the ORBD Server Manager, the server must be started using <code>servertool</code>, which is a command-line interface for application programmers to register, unregister, start up, and shut down a persistent server. For more information on the Server Manager, see Server Manager. </p>
<p> When <code>orbd</code> starts, it also starts a naming service. For more information about the naming service. See Start and Stop the Naming Service.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-ORBInitialPort <i>nameserverport</i></p>
<dd>Required. Specifies the port on which the name server should be started. After it is started, <code>orbd</code> listens for incoming requests on this port. On Oracle Solaris software, you must become the root user to start a process on a port below 1024. For this reason, Oracle recommends that you use a port number above or equal to 1024.</dl>
<h3>Nonrequired Options</h3>
<dl COMPACT>
<dt>-port <i>port</i></p>
<dd>Specifies the activation port where ORBD should be started, and where ORBD will be accepting requests for persistent objects. The default value for this port is 1049. This port number is added to the port field of the persistent Interoperable Object References (IOR).</p>
<dt>-defaultdb <i>directory</i></p>
<dd>Specifies the base where the ORBD persistent storage directory, <code>orb.db</code>, is created. If this option is not specified, then the default value is <code>./orb.db</code>.</p>
<dt>-serverPollingTime <i>milliseconds</i></p>
<dd>Specifies how often ORBD checks for the health of persistent servers registered through <code>servertool</code>. The default value is 1000 ms. The value specified for <code>milliseconds</code> must be a valid positive integer.</p>
<dt>-serverStartupDelay milliseconds</p>
<dd>Specifies how long ORBD waits before sending a location forward exception after a persistent server that is registered through <code>servertool</code> is restarted. The default value is 1000 ms. The value specified for <code>milliseconds</code> must be a valid positive integer.</p>
<dt>-J<i>option</i></p>
<dd>Passes <code>option</code> to the Java Virtual Machine, where <code>option</code> is one of the options described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h3>Start And Stop The Naming Service</h3>
<p>A naming service is a CORBA service that allows CORBA objects to be named by means of binding a name to an object reference. The name binding can be stored in the naming service, and a client can supply the name to obtain the desired object reference. </p>
<p> Before running a client or a server, you will start ORBD. ORBD includes a persistent naming service and a transient naming service, both of which are an implementation of the COS Naming Service. </p>
<p> The Persistent Naming Service provides persistence for naming contexts. This means that this information is persistent across service shutdowns and startups, and is recoverable in the event of a service failure. If ORBD is restarted, then the Persistent Naming Service restores the naming context graph, so that the binding of all clients&#8217; and servers&#8217; names remains intact (persistent). </p>
<p> For backward compatibility, <code>tnameserv</code>, a Transient Naming Service that shipped with earlier releases of the JDK, is also included in this release of Java SE. A transient naming service retains naming contexts as long as it is running. If there is a service interruption, then the naming context graph is lost. </p>
<p> The <code>-ORBInitialPort</code> argument is a required command-line argument for <code>orbd</code>, and is used to set the port number on which the naming service runs. The following instructions assume you can use port 1050 for the Java IDL Object Request Broker Daemon. When using Oracle Solaris software, you must become a root user to start a process on a port lower than 1024. For this reason, it is recommended that you use a port number above or equal to 1024. You can substitute a different port when necessary. </p>
<p> To start <code>orbd</code> from a UNIX command shell, enter: </p>
<pre><code>orbd -ORBInitialPort 1050&amp;</code></pre>
<p>From an MS-DOS system prompt (Windows), enter: </p>
<pre><code>start orbd -ORBInitialPort 1050</code></pre>
<p>Now that ORBD is running, you can run your server and client applications. When running the client and server applications, they must be made aware of the port number (and machine name, when applicable) where the Naming Service is running. One way to do this is to add the following code to your application: </p>
<pre><code>Properties props = new Properties();</code></pre>
<pre><code>props.put(&quot;org.omg.CORBA.ORBInitialPort&quot;, &quot;1050&quot;);</code></pre>
<pre><code>props.put(&quot;org.omg.CORBA.ORBInitialHost&quot;, &quot;MyHost&quot;);</code></pre>
<pre><code>ORB orb = ORB.init(args, props);</code></pre>
<p>In this example, the naming service is running on port 1050 on host <code>MyHost</code>. Another way is to specify the port number and/or machine name when running the server or client application from the command line. For example, you would start your <code>HelloApplication</code> with the following command line: </p>
<pre><code>java HelloApplication -ORBInitialPort 1050 -ORBInitialHost MyHost</code></pre>
<p>To stop the naming service, use the relevant operating system command, such as <code>pkill</code><code>orbd</code> on Oracle Solaris, or <i>Ctrl+C</i> in the DOS window in which <code>orbd</code> is running. Note that names registered with the naming service can disappear when the service is terminated because of a transient naming service. The Java IDL naming service will run until it is explicitly stopped. </p>
<p> For more information about the naming service included with ORBD, see Naming Service at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html</a></p>
<h2>Server Manager</h2>
<p>To access the ORBD Server Manager and run a persistent server, the server must be started with <code>servertool</code>, which is a command-line interface for application programmers to register, unregister, start up, and shut down a persistent server. When a server is started using <code>servertool</code>, it must be started on the same host and port on which <code>orbd</code> is executing. If the server is run on a different port, then the information stored in the database for local contexts will be invalid and the service will not work properly. </p>
<p> See Java IDL: The &quot;Hello World&quot; Example at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample.html</a> </p>
<p> In this example, you run the <code>idlj</code> compiler and <code>javac</code> compiler as shown in the tutorial. To run the ORBD Server Manager, follow these steps for running the application: </p>
<p> Start <code>orbd</code>. </p>
<p> UNIX command shell, enter: <code>orbd -ORBInitialPort 1050</code>. </p>
<p> MS-DOS system prompt (Windows), enter: <code>s</code><code>tart orbd -ORBInitialPort 105</code><code>0</code>. </p>
<p> Port 1050 is the port on which you want the name server to run. The <code>-ORBInitialPort</code> option is a required command-line argument. When using Oracle Solaris software, you must become a root user to start a process on a port below 1024. For this reason, it is recommended that you use a port number above or equal to 1024. </p>
<p> Start the <code>servertool</code>: <code>servertool -ORBInitialPort 1050</code>. </p>
<p> Make sure the name server (<code>orbd</code>) port is the same as in the previous step, for example, <code>-ORBInitialPort 1050.</code> The <code>servertool</code> must be started on the same port as the name server. </p>
<p> In the <code>servertool</code> command line interface, start the <code>Hello</code> server from the <code>servertool</code> prompt: </p>
<pre><code>servertool &gt; register -server HelloServer -classpath . -applicationName</code></pre>
<pre><code> HelloServerApName</code></pre>
<p>The <code>servertool</code> registers the server, assigns it the name <code>HelloServerApName</code>, and displays its server ID with a listing of all registered servers.Run the client application from another terminal window or prompt: </p>
<pre><code>java HelloClient -ORBInitialPort 1050 -ORBInitialHost localhost</code></pre>
<p>For this example, you can omit <code>-ORBInitialHost localhost</code> because the name server is running on the same host as the <code>Hello</code> client. If the name server is running on a different host, then use the &#8211;<code>ORBInitialHost nameserverhost</code> option to specify the host on which the IDL name server is running.Specify the name server (<code>orbd</code>) port as done in the previous step, for example, <code>-ORBInitialPort 1050</code>. When you finish experimenting with the ORBD Server Manager, be sure to shut down or terminate the name server (<code>orbd</code>) and <code>servertool</code>. To shut down <code>orbd</code> from am MS-DOS prompt, select the window that is running the server and enter <i>Ctrl+C</i> to shut it down. </p>
<p> To shut down <code>orbd</code> from an Oracle Solaris shell, find the process, and terminate with the <code>kill</code> command. The server continues to wait for invocations until it is explicitly stopped. To shut down the <code>servertool</code>, type <i>quit</i> and press the <i>Enter</i> key.</p>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-servertool/">servertool</a>(1)</p>
<dt>&bull;</p>
<dd>Naming Service at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html</a> </p>
</dl>
