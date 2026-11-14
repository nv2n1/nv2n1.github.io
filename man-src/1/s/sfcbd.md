---
title: "sfcbd(1)"
name: "sfcbd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbd/"
description: "sfcbd – Small-Footprint CIM Broker (sfcb)"
---

<h2 class="name">NAME</h2>
<p> sfcbd &#8211; Small-Footprint CIM Broker (sfcb) </p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbd</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> sfcb is a lightweight CIM daemon (aka CIMOM) that responds to CIM client requests for system management data and/or performs system management tasks. sfcb supports most of the standard CIM XML over http/https protocol. It is highly modular, allowing functionality to be easily added, removed or customized for different management applications. sfcb is specifically targetted for small embedded system that do not have the available CPU, memory or disk resources to support a full-blown enterprise-level CIMOM. That said, sfcb runs very well on a regular Linux/Unix system and supports most of the functions required by CIM clients to manage such the system. Supported CIM operations include:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>GetClass</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>EnumerateClasses</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>EnumerateClassNames</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>GetInstance</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>DeleteInstance</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>CreateInstance</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ModifyInstance</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>EnumerateInstances</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>EnumerateInstanceNames</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>InvokeMethod (MethodCall)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ExecQuery</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Associators</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>AssociatorNames</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>References</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>ReferenceNames</td>
<td>
</td>
</tr>
</table>
</dl>
<p> CIM process and lifecycle indications (aka &#8216;events&#8217;) are also supported.</p>
<h2>OPTIONS</h2>
<p> Supported command line options are:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;config-file</code>=<i>FILE</i></p>
<dd> Specify an alternative configuration file. Default=<i>/etc/sfcb/sfcb.cfg</i></p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Run sfcbd (and child processes) in the background.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-k</code>, <code>&#8211;color-trace</code></p>
<dd> -k, &#8211;color-trace Color the trace output of each process</p>
<dt><code>-s</code>, <code>&#8211;collect-stats</code></p>
<dd> Turn on runtime statistics collecting. If enabled then various sfcbd runtime statistics will be written to <i>./sfcbStat</i>. Default is no statistics are collected.</p>
<dt><code>-t</code>, <code>&#8211;trace-components</code>=<i>NUM</i></p>
<dd> Activate component-level tracing messages, where <i>NUM</i> is an OR-ed bitmask integer defining which component to trace. Specifying &quot;-t ?&quot; will list all the components and their associated integer bitmask.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Prints version information and exits.</dl>
<h2>CONFIGURATION FILE</h2>
<p> sfcbd reads the configuration file <i>/etc/sfcb/sfcb.cfg</i> (or the file specified with the -c option) at start up. The configuration file contains <i>option : value</i> pairs, one per line. For a complete list of options, see the default configuration file included with the sfcb package.</p>
<dl>
<dt><code>httpPort</code></p>
<dd> Local port that sfcbd should listen to receive HTTP (i.e. insecure) requests from CIM clients. Default=<i>5988</i></p>
<dt><code>enableHttp</code></p>
<dd> Whether sfcb should accept HTTP client connections. Default=<i>true</i>.</p>
<dt><code>httpProcs</code></p>
<dd> Maximum number of simultaneous HTTP client connections before blocking new incoming HTTP requests. Default=<i>8</i></p>
<dt><code>httpsPort</code></p>
<dd> Local port that sfcbd should listen to receive HTTPS (i.e. secure) requests from CIM clients. Default=<i>5989</i></p>
<dt><code>enableHttps</code></p>
<dd> Whether sfcb should accept HTTPS client connections. Default=<i>false</i>.</p>
<dt><code>httpsProcs</code></p>
<dd> Maximum number of simultaneous HTTPS client connections before blocking new incoming HTTPS requests. Default=<i>8</i></p>
<dt><code>enableInterOp</code></p>
<dd> Whether sfcb should provide the interop namespace for indication support. Default=<i>true</i></p>
<dt><code>provProcs</code></p>
<dd> Maximum number of simultaneous provider processes. After this point if a new incoming request requires loading a new provider, then one of the existing providers will first be automatically unloaded. Default=<i>32</i></p>
<dt><code>doBasicAuth</code></p>
<dd> Perform basic authentication on the client userid (obtained from the HTTP/HTTPS header) before allowing the request. Default=<i>false</i> (i.e. no client authentication performed).</p>
<dt><code>basicAuthLib</code></p>
<dd> Name of the local library to call to authenticate the client userid. Default=<i>sfcBasicAuthentication</i></p>
<dt><code>useChunking</code></p>
<dd> Tell sfcbd to use HTTP/HTTPS &#8216;chunking&#8217; to return large volumes of response data to the client in &#8216;chunks&#8217;, rather than buffering the data and sending it back all at once. Default=<i>true</i></p>
<dt><code>keepaliveTimeout</code></p>
<dd> Specify the maximum time in seconds an sfcb HTTP process will wait between two requests on one connection before terminating. Setting it to 0 will disable HTTP keep-alive. Default=<i>0</i></p>
<dt><code>keepaliveMaxRequest</code></p>
<dd> Specify the maximum number of consecutive request on one connection. Setting it to 0 will effectively disable HTTP keep-alive. Default=<i>10</i></p>
<dt><code>registrationDir</code></p>
<dd> Specify the registration directory, which contains the provider registration data, the staging area and the static repository. Default=<i>/var/lib/sfcb/registration</i></p>
<dt><code>providerDirs</code></p>
<dd> A space separated list of directories where sfcb is looking for provider libraries. Default=<i>/usr/lib&nbsp;<wbr>/usr/lib/cmpi /usr/lib64&nbsp;<wbr>/usr/lib64/cmpi</i></p>
<dt><code>providerSampleInterval</code></p>
<dd> The interval in seconds at which the provider manager is checking for idle providers. Default: <i>30</i></p>
<dt><code>providerTimeoutInterval</code></p>
<dd> The interval in seconds before an idle provider gets unloaded by the provider manager. Default: <i>60</i></p>
<dt><code>providerAutoGroup</code></p>
<dd> If set to true, all providers residing in the same shared library will be executed in the same process unless another group has been specified in the provider registration file. Default: <i>true</i></p>
<dt><code>sslCertificateFilePath</code></p>
<dd> Specify the name of the file containing the server&#8217;s certificate. The file must be in PEM format. This file is only required if enableHttps is set to <i>true</i>. Default=<i> /etc/sfcb/server.pem</i></p>
<dt><code>sslKeyFilePath</code></p>
<dd> Specify the name of the file containing the private key for the server&#8217;s certificate. The file must be in PEM format and may not be passphrase-protected. This file is only required if enableHttps is set to <i>true</i>. Default=<i>/etc/sfcb/file.pem</i></p>
<dt><code>sslClientTrustStore</code></p>
<dd> Specify the name of the file or directory containing either the CA certificate issuing client certificates or self-signed certificates of the clients. This setting is only required if sslClientCertificate is set to <i>accept</i> or <i>require</i>. </p>
<p> If a file, it must be in PEM format. </p>
<p> If a directory, it must be in &quot;hash format&quot;: each file in the directory should be named <i>hash.0</i>, where <i>hash</i> is the output of <i>openssl x509 -hash</i>. See the <i>-CApath</i> option in <i><a href="/docs/linux/man/1-verify/">verify</a>(1)</i> from the <i>openssl</i> package for more information about the hash format. </p>
<p> Default=<i>/etc/sfcb/client.pem</i></p>
<dt><code>sslClientCertificate</code></p>
<dd> Specify the way sfcb handles client certificate based authentication. If set to <i>ignore</i> it will not request a certificate from the client. If set to <i>accept</i> it will request a certificate from the client but not fail if the client doesn&#8217;t present one. If set to <i>require</i> it will refuse the client connection if the client doesn&#8217;t present a certificate. Default=<i>ignore</i></p>
<dt><code>certificateAuthLib</code></p>
<dd> Name of the local library to call for client-certificate based user authentication. Called only if sslClientCertificate is not set to <i>ignore</i>. Default=<i>sfcCertificateAuthentication</i></p>
<dt><code>traceLevel</code></p>
<dd> Specify the trace level for sfcb. Can be overriden by setting environment variable SFCB_TRACE_LEVEL. Default:<i>0</i>.</p>
<dt><code>traceMask</code></p>
<dd> Specify the trace mask for sfcb. Can be overriden by the command line option &#8211;trace-components. Default: <i>0</i>.</p>
<dt><code>traceFile</code></p>
<dd> Specify the trace file for sfcb. Can be overriden by setting environment variable SFCB_TRACE_FILE. Default: <i>stderr</i>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SFCB_PAUSE_PROVIDER</code></p>
<dd> Specifies the name of the provider to pause after first being loaded to facilitate attaching a runtime debugger to the provider&#8217;s process for debugging purposes.</p>
<dt><code>SFCB_PAUSE_CODEC</code></p>
<dd> Specifies the name of the sfcb codec (currently only &quot;http&quot;) to pause after first being started to facilitate attaching a runtime debugger to the process.</p>
<dt><code>SFCB_TRACE</code></p>
<dd> Specifies the level of trace/debug messages for sfcb. Valid values are 0 (no trace messages), or 1 (key trace messages only) to 4 (all messages). A default value of 1 will be assumed, if this variable is not set.<br />
 [Note: SFCB_TRACE level is used in conjunction with sfcb&#8217;s component-level tracing to control the level of detail of trace messages to display within each component]</p>
<dt><code>SFCB_TRACE_FILE</code></p>
<dd> By default sfcb trace messages are written to STDERR. Setting this envorinment variable causes the trace messages to be written to a file instead.</p>
<dt><code>SFCB_TRAP</code></p>
<dd> If set this environment variable enables trap interrupts on x86 platforms to be generated by sfcb in special situations.<br />
 [Note: not currently ever used]</p>
<dt><code>SBLIM_TRACE</code></p>
<dd> Specifies the level of trace/debug messages for SBLIM providers. Valid values are 0 (no trace messages), or 1 (key trace messages only) to 4 (all messages).<br />
 [Note: this only applies to SBLIM providers written with explicit trace messages in their source code.]</p>
<dt><code>SBLIM_TRACE_FILE</code></p>
<dd> By default SBLIM provider trace messages are written to STDERR. Setting this envorinment variable causes the trace messages to be written to a file instead.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/sfcb/sfcb.cfg</i></p>
<dd> Default sfcb configuration file.</p>
<dt><i>/etc/sfcb/server.pem</i></p>
<dd> SSL server certificate for sfcb.</p>
<dt><i>/etc/sfcb/file.pem</i></p>
<dd> SSL private key file for sfcb.</p>
<dt><i>/etc/sfcb/client.pem</i></p>
<dd> SSL client certificate / trust store for sfcb.</dl>
<h2>LIBRARIES</h2>
<dl>
<dt><i>/usr/lib/libsfc* /usr/lib64/libsfc*</i></p>
<dd> Binaries for sfcb runtime libraries.</p>
<dt><i>/usr/lib/cmpi/* /usr/lib64/cmpi/*</i></p>
<dd> Binaries for providers.</dl>
<h2>AUTHOR</h2>
<p> Adrian Schuur &lt;schuur [at] de.ibm.com&gt;</p>
<h2>CONRIBUTORS</h2>
<table>
<tr VALIGN=top>
<td>Dr. Gareth S. Bestor &lt;bestor [at] us.ibm.com&gt;,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Viktor Mihajlovski &lt;MIHAJLOV [at] de.ibm.com&gt;,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Chris Buccella &lt;buccella [at] linux.vnet.ibm.com&gt;</td>
<td>
</td>
</tr>
</table>
<h2>BUGS</h2>
<p> The SBLIM project maintains a mailing list to which you should direct all questions regarding sfcb, sfcc, wbemcli, or any of the SBLIM providers. To subscribe to this mailing list visit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://lists.sourceforge.net/lists/listinfo/sblim-devel">http://lists.sourceforge.net/lists/listinfo/sblim-devel</a></dl>
<p> The SBLIM Project Bug tracking page can be found at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=128809">http://sourceforge.net/tracker/?group_id=128809</a>&amp;atid=712784</dl>
<h2>COPYRIGHT</h2>
<p> (C) Copyright IBM Corp. 2004, 2005, 2009</p>
<h2>AVAILABILITY</h2>
<p> The Small-Footprint CIM Broker (sfcb) is a part of the SBLIM project. The most recent version is available on the web at</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://sblim.sourceforge.net/">http://sblim.sourceforge.net/</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sfcbmof/">sfcbmof</a></code>(1), <code><a href="/docs/linux/man/1-sfcbstage/">sfcbstage</a></code>(1), <code><a href="/docs/linux/man/1-sfcbunstage/">sfcbunstage</a></code>(1), <code><a href="/docs/linux/man/1-sfcbrebos/">sfcbrebos</a></code>(1), <code><a href="/docs/linux/man/1-gensslcert-sh/">genSslCert.sh</a></code>(1), <code><a href="/docs/linux/man/1-getschema-sh/">getSchema.sh</a></code>(1), <code><a href="/docs/linux/man/1-wbemcli/">wbemcli</a></code>(1) </p>
<h2>Index</h2>
