---
title: "cimserver(8)"
name: "cimserver"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cimserver/"
description: "cimserver – start or stop the CIM Server; display the version number or running status of the CIM Server"
---

<p>cimserver &#8211; start or stop the CIM Server; display the version number or running status of the CIM Server</p>
<h2>Synopsis</h2>
<p><code>cimserver</code> [<i>configProperty</i>=<i>value</i>]<i>&nbsp;<wbr>&#8230;</i> </p>
<p> <code>cimserver -s</code> [ <code>shutdownTimeout</code> = value ] </p>
<p> <code>cimserver -v</code> </p>
<p> <code>cimserver -h</code> </p>
<p> <code>cimserver &#8211;help</code> </p>
<p> <code>cimserver &#8211;version</code> </p>
<p> <code>cimserver &#8211;status</code></p>
<h3>Remarks</h3>
<p>This command can only be executed by a privileged user.</p>
<h2>Description</h2>
<p>The <code>cimserver </code> command provides a command line interface to stop and start the CIM Server, as well as to display the version number or running status of the CIM Server. </p>
<p> After installation, the CIM Server must be started using the <code>cimserver </code> command. If the system is rebooted, the CIM Server will automatically restart, with the exception of the case where the CIM Server was shutdown prior to the reboot. Generally, once the CIM Server is started, it is expected to be always running and ready to serve CIM requests. However, if the CIM Server must be stopped and restarted, the <code>cimserver </code> command can be used to shutdown the CIM Server gracefully and restart it at a later time.</p>
<h3>Starting the CIM Server</h3>
<p>Issuing the <code>cimserver </code> command without any options starts the CIM Server process. </p>
<p> When starting the CIM Server using the <code>cimserver </code> command, the &lt;<i>configProperty</i>=<i>value</i>&gt; syntax can be used to set the configuration properties to be used by the CIM Server. It is important to know that the values specified in the <code>cimserver</code> command apply only to the current CIM Server process that gets started. The default values for the configuration properties do not change. For a list of the CIM Server configuration properties, see the man page for the <code>cimconfig</code> command.</p>
<h3>Shutting down the CIM Server</h3>
<p>Issuing the <code>cimserver </code> command with the <code>-s</code> option stops the CIM Server. Optionally, a timeout value can be specified by setting the <code>shutdownTimeout</code> configuration property. </p>
<p> Under normal operation, CIM Server should be able to be shutdown fairly quickly without problem. There are, however, situations that may prevent CIM Server from shutting down within a reasonable amount of time. For example, a provider that is not responding to requests, or a provider that is servicing a long-running CIM request. To handle such situations and to ensure that the CIM Server can be shutdown without having the user wait a long period of time (or indefinitely), a shutdown timeout value is used. </p>
<p> The shutdown timeout value is the maximum amount of time (in seconds) the user is willing to wait for the CIM Server to complete all the outstanding CIM operation requests before shutting down the CIM Server. If the specified shutdown timeout period expires, the CIM Server will be shutdown even if there are CIM operations in progress. The shutdown timeout value is a CIM Server configuration property (<code>shutdownTimeout )</code> that can be changed using the command. The default shutdown timeout value is 10 seconds. </p>
<p> A timeout value (in seconds) can be specified in the <code>cimserver</code> command to shutdown the CIM Server using the =<i>value</i>&gt; syntax. This overrides the default shutdown timeout value. The minimum timeout value is 2 seconds. </p>
<p> While CIM Server is shutting down, a client connection request will result in a connection error (the same as if the CIM Server were not running). For clients who have already established a connection to the CIM Server, new CIM requests will be rejected with a CIM error indicating that the CIM Server is shutting down. </p>
<p> When a client receives a response containing a CIM error indicating that the CIM Server is shutting down, it should close the connection and reconnect to CIM Server at a later time.</p>
<h3>Options</h3>
<p>The <code>cimserver</code> command recognizes the following options:</p>
<dl>
<dd>
</dd><dl>
<dt><code>-v, &#8211;version</code></dt>
<dd>Display the version number or running status of the CIM Server.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display the command usage.</dd>
<dt><code>&#8211;status</code></dt>
<dd>Display the running status of the CIM Server.</dd>
<dt><code>-s</code></dt>
<dd>Stop the CIM Server.</dd>
<dd>Specify the timeout value for shutting down the CIM Server. This can only be used in conjunction with the <code>-s </code> option. The minimum timeout value is 2 seconds. If this is not specified, the default configurable timeout value will be used.</dd>
<dt><i>configProperty=value</i></dt>
<dd>Set the value for the specified configuration property to be used in starting the CIM Server.</dd></dl>
</dl>
<h2>Exit Status</h2>
<p>The <code>cimserver </code> command returns one of the following values:</p>
<dl>
<dd>
</dd><dl>
<dt><code>0</code></dt>
<dd>Success</dd>
<dt><code>1 </code></dt>
<dd>Error</dd></dl>
</dl>
<p> The <code>cimserver &#8211;status </code> command returns one of the following values:</p>
<dl>
<dd>
</dd><dl>
<dt><code>0</code></dt>
<dd>The CIM Server is running</dd>
<dt><code>1 </code></dt>
<dd>Error</dd>
<dt><code>2 </code></dt>
<dd>The CIM Server is not running</dd></dl>
</dl>
<p> When an error occurs, an error message is written to stderr and an error value of 1 is returned.</p>
<h2>Diagnostics</h2>
<p><code>unable to connect to CIM Server. CIM Server may not be running.</code></p>
<dl>
<dd>The <code>cimserver</code> command was issued to stop the CIM Server when CIM Server was not running. An exit status value of 1 is returned.</dd></dl>
<p> <code>Error: Bind failed: Failed to bind socket. </code></p>
<dl>
<dd>The <code>cimserver</code> command was issued to start the CIM Server and the CIM Server was already running. An exit status value of 1 is returned.</dd></dl>
<h2>Examples</h2>
<p>Stop the CIM Server with the default timeout value of 10 seconds.</p>
<dl>
<dd><code>cimserver -s</code></dd></dl>
<p> Stop the CIM Server with a timeout value of 5 seconds.</p>
<dl>
<dd><code>cimserver -s shutdownTimeout=5</code></dd></dl>
<p> Start the CIM Server.</p>
<dl>
<dd><code>cimserver</code></dd></dl>
<p> Start the CIM Server with the configuration property <code>enableNamespaceAuthorization</code> set to true.</p>
<dl>
<dd><code>cimserver enableNamespaceAuthorization=true</code></dd></dl>
<p> Display the version number of the CIM Server. This version number is used to identify the release version of the CIM Server in the OpenPegasus release.</p>
<dl>
<dd><code>cimserver -v</code></dd></dl>
<p> Display the command usage.</p>
<dl>
<dd><code>cimserver -h</code></dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-cimconfig/">cimconfig</a>(8). </p>
