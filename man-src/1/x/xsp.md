---
title: "xsp(1)"
name: "xsp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsp/"
description: "XSP – Mono ASP.NET Web Server (xsp and xsp2)"
---

<h2>NAME</h2>
<p> XSP &#8211; Mono ASP.NET Web Server (xsp and xsp2)</p>
<h2>SYNOPSIS</h2>
<p> <code>xsp</code> [options] </p>
<p> or </p>
<p> <code>mod-mono-server</code> [options] </p>
<p> or </p>
<p> <code>fastcgi-mono-server</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> XSP, mod-mono-server and fastcgi-mono-server are hosts for ASP.NET-based applications. </p>
<p> If run as `xsp&#8217;, the process provides a minimalistic web server which hosts the ASP.NET runtime and can be used to test and debug web applications that use the System.Web facilities in Mono. This server is most convenient for testing and running small sites, does not offer everything a production web server offers. </p>
<p> `mod-mono-server&#8217; and &#8216;fastcgi-mono-server&#8217; are both ASP.NET runtimes hosts that can communicate with another web server (at the time of this writing, Apache 1.3-2.2 were supported through mod_mono and several other web servers through FastCGI). This mechanism is better used for high-traffic servers or production systems, since it can integrate with the main HTTP server and leverage all of the optimizations and extensions of an existing server, while providing the ASP.NET runtime. You can choose the communication channel used between mod_mono and mod-mono-server. If you provide a &#8211;filename option, a unix socket is used, otherwise you can give &#8211;port to use a TCP socket.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;address addr</i></p>
<dd> Sets the IP address to listen on. By default it&#8217;s 0.0.0.0 for xsp and 127.0.0.1 for mod-mono-server. AppSettings key name: MonoServerAddress</p>
<dt><i>&#8211;port PORT</i></p>
<dd> Changes the default port where the XSP server will listen to requests. By default XSP listens on port 8080 and mod-mono-server has no default. AppSettings key name: MonoServerPort</p>
<dt><i>&#8211;backlog N</i></p>
<dd> The backlog of connections to set on the listener socket. By default the value is set to 500.</p>
<dt><i>&#8211;minThreads N</i></p>
<dd> The minimum number of threads the threadpool allocates. Increase this value to better handle the sudden arrival of connections. The default value is determined by the mono runtime.</p>
<dt><i>&#8211;filename file (mod-mono-server and fastcgi-mono-server)</i></p>
<dd> The unix socket file name to listen on. Default value: /tmp/mod_mono_server (fastcgi-mono-server: /tmp/fastcgi-mono-server) AppSettings key name: UnixSocketFileName (fastcgi-mono-server: MonoUnixSocket)</p>
<dt><i>&#8211;root PATH</i></p>
<dd> The root directory for XSP. The default is the directory where XSP is executed. The current directory will be changed to this one before creating any application. AppSettings key name: MonoServerRootDir</p>
<dt><i>&#8211;appconfigfile FILENAME</i></p>
<dd> Adds application definitions from the XML configuration file. See sample configuration file that comes with the server (sample.webapp) and <code>WEBAPP FILE FORMAT</code> below. AppSettings key name: MonoApplicationsConfigFile</p>
<dt><i>&#8211;appconfigdir DIR</i></p>
<dd> Adds application definitions from all XML files found in the specified directory DIR. Files must have &#8216;.webapp&#8217; extension. AppSettings key name: MonoApplicationsConfigDir</p>
<dt><i>&#8211;applications APPS</i></p>
<dd> A comma separated list of virtual directory and real directory for all the applications we want to manage with this server. The virtual and real dirs. are separated by a colon. The default value is &#8216;/:.&#8217;.</p>
<dt>Some examples:</p>
<dd>
<dt><code>&#8216;/:.&#8217;</code></p>
<dd> The virtual / is mapped to the current directory.</p>
<dt><code>&#8216;/blog:../myblog&#8217;</code></p>
<dd> The virtual /blog is mapped to ../myblog</p>
<dt><code>&#8216;/:.,/blog:../myblog&#8217;</code></p>
<dd> Two applications like the above ones are handled.</p>
<dt><code>myhost.someprovider.net:/blog:../myblog</code></p>
<dd> The virtual /blog at myhost.someprovider.net is mapped to ../myblog.</p>
<dt><i>&#8211;master</i></p>
<dd>
<dt>This instance will be used to by mod_mono to create ASP.NET</p>
<dd> applications on demand. If this option is provided, there is no need to provide a list of applications to start. This applies only to mod-mono-server.exe. <i>&#8211;nonstop</i> By default xsp/mod-mono-server will stop processing requests when the return key is pressed. Use this to avoid this behavior.</p>
<dt><i>&#8211;no-hidden</i></p>
<dd> Do not protect hidden files/directories from being accessed by clients. Hidden files/directories are those with Hidden attribute on Windows and whose name starts with a dot on Unix. Any file/directory below a hidden directory is inacessible. This option turns the default behavior of protecting such locations off. If your application does not contain any hidden files/directories, you might want to use this option as the checking process has a per-request cost. AppSettings key name: MonoServerCheckHiddenFiles (a boolean accepting &#8216;true&#8217; or &#8216;false&#8217;)</p>
<dt><i>&#8211;https</i></p>
<dd> Enables HTTPS support on the server, you must supply an X.509 certificate and a private key with either the &#8211;cert/&#8211;pkfile options or with the &#8211;p12file (which combines both the certificate and the private key into a single file).</p>
<dt>To use you must first create an X.509 certificate for your server, for</p>
<dd> example: </p>
<pre>
        $ makecert -r -eku 1.3.6.1.5.5.7.3.1 -n &quot;CN=server&quot; -p12 server.p12 s3kr3t
        Mono MakeCert - version 1.1.9.0
        X.509 Certificate Builder
        Copyright 2002, 2003 Motus Technologies. Copyright 2004-2005 Novell. BSD licensed.
        
        Success
</pre>
<dt>Then you must pass the following flags to xsp:</p>
<dd>
<pre>
        $ xsp --https --p12file server.p12 --pkpwd s3kr3t
</pre>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;https-client-accept</i></p>
<dd> Like &#8211;https this enables HTTPS support on the server. However this option also send an &quot;invitation&quot; to clients to provide client-certificates to authenticate themselves. Client are free to provide, or not, a client certificate. Web application can detect if a client certificate is used and react accordingly. Most web browser will not send a client certificate unless they have been explicitly requested to do so.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;https-client-require</i></p>
<dd> Like &#8211;https this enables HTTPS support on the server. However this option also <code>requires </code> clients to use client-certificates to authenticate themselves. Client who do not provide client certificates will receive an error. Note that client may send an empty certificate structure so web application should check the certificate content.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;p12file FILENAME</i></p>
<dd> Used to specify the PKCS#12 file to use. This file includes both the X.509 certificate and the private key required to encrypt the HTTP traffic.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;cert FILENAME</i></p>
<dd> Used to specify the server X.509 certificate file. This is normally used with the &#8211;pkfile.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;pkfile FILENAME</i></p>
<dd> Used to specify the path to the private keyfile. The PVK format isn&#8217;t very secure and you should use the PKCS#12 format (&#8211;p12file option) to store new private keys.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;pkpwd PASSWORD</i></p>
<dd> If your private key is password protected, PASSWORD is the password used to decote the private key. This option works for both PVK and PKCS#12 formats.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;protocol PROTOCOL</i></p>
<dd> Specifies which protocols are available for encrypting the communications. The possible values are Default, Tls and Ssl3. <code>Ssl2 isn&#8217;t supported.</code> The default value is &quot;Default&quot; which auto-detect the client protocol and adjust the server protocol accordingly.</p>
<dt>
<dd>This option is only valid for XSP. For mod_mono you should configure Apache for SSL/TLS.</p>
<dt><i>&#8211;terminate (mod-mono-server only)</i></p>
<dd> Gracefully terminates a running mod-mono-server instance. All other options but &#8211;filename or &#8211;address and &#8211;port are ignored if this option is provided.</p>
<dt><i>&#8211;version</i></p>
<dd> Displays version information and exits.</p>
<dt><i>&#8211;help</i></p>
<dd> Shows the list of options and exits.</p>
<dt><i>&#8211;verbose</i></p>
<dd> Prints extra messages. Useful for debugging.</p>
<dt><i>&#8211;pidfile FILE</i></p>
<dd> Writes the xsp PID to the specified file.</dl>
<h2>MONO RUNTIME OPTIONS</h2>
<p> xsp and xsp2 are scripts that call mono. If you want to pass options to mono (for example, options to get line numbers in stack traces), you can use the MONO_OPTIONS environment variable when invoking xsp or xsp2. </p>
<p> For example: </p>
<pre>
        $ MONO_OPTIONS=--debug xsp2
</pre>
<h2>DEFAULT INDEX FILES</h2>
<p> You can choose which files are considered as index using <i>xsp.exe.config</i> configuration file like this: </p>
<pre>
    &lt;appSettings&gt;
    &lt;add key=&quot;MonoServerDefaultIndexFiles&quot;
         value=&quot;index.aspx&quot; /&gt;
    &lt;/appSettings&gt;
</pre>
<p> By default, it has index.aspx, Default.aspx, default.aspx, index.html and index.htm. The order matters. </p>
<h2>WEBAPP FILE FORMAT</h2>
<p> The format of the .webapp files used for &#8211;appconfigfile and &#8211;appconfigdir is: </p>
<pre><code>
&lt;apps&gt;
&lt;web-application&gt;
        &lt;name&gt;{appname}&lt;/name&gt;
        &lt;vhost&gt;{virtual host for application}&lt;/vhost&gt;
        &lt;vport&gt;{port for the application}&lt;/vport&gt;
        &lt;vpath&gt;{virtual directory in apache}&lt;/vpath&gt;
        &lt;path&gt;{physical path to aspx files}&lt;/path&gt;
        &lt;!-- &lt;enabled&gt; is true by default --&gt;
        &lt;enabled&gt;{true|false}&lt;/enabled&gt;
&lt;/web-application&gt;
&lt;/apps&gt;
</code></pre>
<p> You can include any number of &lt;web-application&gt; nodes, one per ASP.NET application to run. </p>
<p> There&#8217;s a <i>sample.webapp</i> file in the XSP samples directory. </p>
<h2>AUTHORS</h2>
<p> The Mono XSP server was written by Gonzalo Paniagua Javier (gonzalo [at] ximian.com). Fastcgi-mono-server was written by Brian Nickel &lt;<a rel="nofollow" href="http://kerrick.wordpress.com">http://kerrick.wordpress.com</a>&gt;.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>MONO_ASPNET_NODELETE</i></p>
<dd> If set to any value, temporary source files generated by ASP.NET support classes will not be removed. They will be kept in the user&#8217;s temporary directory.</dl>
<h2>FILES</h2>
<dl>
<dt><code>Web.config, web.config</code></p>
<dd> ASP.NET applications are configured through these files, the configuration is done on a per-directory basis. For more information on this subject see the <a rel="nofollow" href="http://www.mono-project.com/Config_system.web">http://www.mono-project.com/Config_system.web</a> page.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a></code>(1),<code><a href="/docs/linux/man/1-dbsessmgr/">dbsessmgr</a></code>(1),<code><a href="/docs/linux/man/1-asp-state/">asp-state</a></code>(1),<code><a href="/docs/linux/man/8-mod_mono/">mod_mono</a></code>(8),<code><a href="/docs/linux/man/1-makecert/">makecert</a>(1)</code> </p>
<p> For more information on creating certificates, see: <a rel="nofollow" href="http://pages.infinit.net/ctech/20050701-1048.html">http://pages.infinit.net/ctech/20050701-1048.html</a> </p>
<p> System.Web, System.Web.Hosting namespaces. </p>
<p> <a rel="nofollow" href="http://www.asp.net">http://www.asp.net</a> is Microsoft&#8217;s official site for ASP.NET</p>
<h2>MORE INFORMATION</h2>
<p> The Mono project (<a rel="nofollow" href="http://www.go-mono.com)">http://www.go-mono.com)</a> is a collaborative effort led by Novell (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a> to implement an open source version of the .NET Framework.</p>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://www.mono-project.com/Mailing_Lists">http://www.mono-project.com/Mailing_Lists</a> </p>
<h2>Index</h2>
