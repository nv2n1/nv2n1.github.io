---
title: "upsd-conf(5)"
name: "upsd-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsd-conf/"
description: "upsd.conf – Configuration for Network UPS Tools upsd"
---

<p>upsd.conf &#8211; Configuration for Network UPS Tools upsd</p>
<h2>Description</h2>
<p>upsd uses this file to control access to the server and set some other miscellaneous configuration values. This file contains details on access controls, so keep it secure. Ideally, only the upsd process should be able to read it.</p>
<h2>Configuration Directives</h2>
<p>&quot;MAXAGE <i>seconds</i>&quot;</p>
<dl>
<dd>upsd usually allows a driver to stop responding for up to 15 seconds before declaring the data &quot;stale&quot;. If your driver takes a very long time to process updates but is otherwise operational, you can use MAXAGE to make upsd wait longer. </p>
<p> Most users should leave this at the default value.</dl>
<p> &quot;STATEPATH <i>path</i>&quot;</p>
<dl>
<dd>Tell upsd to look for the driver state sockets in <i>path</i> rather than the default that was compiled into the program.</dl>
<p> &quot;LISTEN <i>interface</i> <i>port</i>&quot;</p>
<dl>
<dd>Bind a listening port to the interface specified by its Internet address. This may be useful on hosts with multiple interfaces. You should not rely exclusively on this for security, as it can be subverted on many systems. </p>
<p> Listen on TCP port <i>port</i> instead of the default value which was compiled into the code. This overrides any value you may have set with <i>configure &#8211;with-port</i>. If you don&#8217;t change it with configure or this value, upsd will listen on port 3493 for this interface. </p>
<p> Multiple LISTEN addresses may be specified. The default is to bind to 127.0.0.1 if no LISTEN addresses are specified (and ::1 if IPv6 support is compiled in). </p>
<dl>
<dd>
<pre>LISTEN 127.0.0.1
LISTEN 192.168.50.1
LISTEN ::1
LISTEN 2001:0db8:1234:08d3:1319:8a2e:0370:7344</pre>
</dl>
<p> This parameter will only be read at startup. You&#8217;ll need to restart (rather than reload) upsd to apply any changes made here.</dl>
<p> &quot;MAXCONN <i>connections</i>&quot;</p>
<dl>
<dd>This defaults to maximum number allowed on your system. Each UPS, each LISTEN address and each client count as one connection. If the server runs out of connections, it will no longer accept new incoming client connections. Only set this if you know exactly what you&#8217;re doing.</dl>
<p> &quot;CERTFILE <i>certificate file</i>&quot;</p>
<dl>
<dd>When compiled with SSL support with OpenSSL backend, you can enter the certificate file here. The certificates must be in PEM format and must be sorted starting with the subject&#8217;s certificate (server certificate), followed by intermediate CA certificates (if applicable_ and the highest level (root) CA. It should end with the server key. See <i>docs/security.txt</i> or the Security chapter of NUT user manual for more information on the SSL support in NUT.</dl>
<p> &quot;CERTPATH <i>certificate database</i>&quot;</p>
<dl>
<dd>When compiled with SSL support with NSS backend, you can enter the certificate path here. Certificates are stored in a dedicated database (splitted in 3 files). Specify the path of the database directory.</dl>
<p> &quot;CERTIDENT <i>certificate name</i> <i>database password</i>&quot;</p>
<dl>
<dd>When compiled with SSL support with NSS backend, you can specify the certificate name to retrieve from database to authenticate itself and the password required to access certificate related private key.</dl>
<p> &quot;CERTREQUEST <i>certificate request level</i>&quot;</p>
<dl>
<dd>When compiled with SSL support with NSS backend and client certificate validation (disabled by default, see <i>docs/security.txt</i>), you can specify if upsd requests or requires client&#8217;s&#8217; certificates. Possible values are : </p>
<dl>
<dd>&bull; </p>
<p> <i>0</i> to not request to clients to provide any certificate</dl>
<dl>
<dd>&bull; </p>
<p> <i>1</i> to require to all clients a certificate</dl>
<dl>
<dd>&bull; </p>
<p> <i>2</i> to require to all clients a valid certificate</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
