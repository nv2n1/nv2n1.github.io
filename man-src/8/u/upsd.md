---
title: "upsd(8)"
name: "upsd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsd/"
description: "upsd – UPS information server"
---

<p>upsd &#8211; UPS information server</p>
<h2>Synopsis</h2>
<p><code>upsd</code> -h </p>
<p> <code>upsd</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p><code>upsd</code> is responsible for serving the data from the drivers to the clients. It connects to each driver and maintains a local cache of the current state. Queries from the clients are served from this cache, so delays are minimal. </p>
<p> It also conveys administrative messages from the clients back to the drivers, such as starting tests, or setting values. </p>
<p> Communication between <code>upsd</code> and clients is handled on a TCP port. Configuration details for this port are described in <code><a href="/docs/linux/man/8-upsd-conf/">upsd.conf</a></code>(8). </p>
<p> This program is essential, and must be running at all times to actually make any use out of the drivers and clients. </p>
<p> Controls in the configuration files allow you to limit access to the server, but you should also use a firewall for extra protection. Client processes such as <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) trust <code>upsd</code> for status information about the UPS hardware, so keep it secure.</p>
<h2>Options</h2>
<p><code>-c</code> <i>command</i></p>
<dl>
<dd>Send <i>command</i> to the background process as a signal. Valid commands are: </p>
<p> <code>reload</code></p>
<dl>
<dd>reread configuration files</dl>
<p> <code>stop</code></p>
<dl>
<dd>stop process and exit</dl>
</dl>
<p> <code>-D</code></p>
<dl>
<dd>Raise the debug level. Use this multiple times for additional details.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Display the help text.</dl>
<p> <code>-r</code> <i>directory</i></p>
<dl>
<dd>upsd will <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) to <i>directory</i> shortly after startup and before parsing any configuration files with this option set. You can use this to create a &quot;jail&quot; for greater security. </p>
<p> You must coordinate this with your drivers, as upsd must be able to find the state path within <i>directory</i>. See <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) and <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</dl>
<p> <code>-u</code> <i>user</i></p>
<dl>
<dd>Switch to user <i>user</i> after startup if started as root. This overrides whatever you may have compiled in with configure &#8211;with-user.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Display the version of the program.</dl>
<h2>Reloading</h2>
<p>upsd can reload its configuration files without shutting down the process if you send it a SIGHUP or start it again with -c reload. This only works if the background process is able to read those files. </p>
<p> If you think that upsd can&#8217;t reload, check your syslogs for error messages. If it&#8217;s complaining about not being able to read the files, then you need to adjust your system to make it possible. Either change the permissions on the files, or run upsd as another user that will be able to read them. </p>
<p> DO NOT make your upsd.conf or upsd.users world-readable, as those files hold important authentication information. In the wrong hands, it could be used by some evil person to spoof your master upsmon and command your systems to shut down.</p>
<h2>Diagnostics</h2>
<p>upsd expects the drivers to either update their status regularly or at least answer periodic queries, called pings. If a driver doesn&#8217;t answer, upsd will declare it &quot;stale&quot; and no more information will be provided to the clients. </p>
<p> If upsd complains about staleness when you start it, then either your driver or configuration files are probably broken. Be sure that the driver is actually running, and that the UPS definition in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) is correct. Also make sure that you start your driver(s) before starting upsd. </p>
<p> Data can also be marked stale if the driver can no longer communicate with the UPS. In this case, the driver should also provide diagnostic information in the syslog. If this happens, check the serial or USB cabling, or inspect the network path in the case of a SNMP UPS.</p>
<h2>Access Control</h2>
<p>If the server is build with tcp-wrappers support enabled, it will check if the NUT username is allowed to connect from the client address through the /etc/hosts.allow and /etc/hosts.deny files. Note that this will only be done for commands that require to be logged into the server. Further details are described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</p>
<h2>Files</h2>
<p>The general upsd configuration file is <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5). The administrative functions like SET and INSTCMD for users are defined and controlled in <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5). UPS definitions are found in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Environment Variables</h2>
<p><code>NUT_CONFPATH</code> is the path name of the directory that contains upsd.conf and other configuration files. If this variable is not set, <code>upsd</code> uses a built-in default, which is often /usr/local/ups/etc. </p>
<p> <code>NUT_STATEPATH</code> is the path name of the directory in which <code>upsd</code> keeps state information. If this variable is not set, <code>upsd</code> uses a built-in default, which is often /var/state/ups. The <code>STATEPATH</code> directive in <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5) overrides this variable.</p>
<h2>See Also</h2>
<h3>Clients:</h3>
<p><code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8), <code><a href="/docs/linux/man/8-upslog/">upslog</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8)</p>
<h3>CGI programs:</h3>
<p><code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Drivers:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/8-apcsmart/">apcsmart</a></code>(8), <code><a href="/docs/linux/man/8-belkin/">belkin</a></code>(8), <code><a href="/docs/linux/man/8-belkinunv/">belkinunv</a></code>(8), <code><a href="/docs/linux/man/8-bestuferrups/">bestuferrups</a></code>(8), <code><a href="/docs/linux/man/8-bestups/">bestups</a></code>(8), <code><a href="/docs/linux/man/8-cyberpower/">cyberpower</a></code>(8), <code><a href="/docs/linux/man/8-energizerups/">energizerups</a></code>(8), <code><a href="/docs/linux/man/8-etapro/">etapro</a></code>(8), <code><a href="/docs/linux/man/8-everups/">everups</a></code>(8), <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8), <code><a href="/docs/linux/man/8-isbmex/">isbmex</a></code>(8), <code><a href="/docs/linux/man/8-liebert/">liebert</a></code>(8), <code><a href="/docs/linux/man/8-masterguard/">masterguard</a></code>(8), <code><a href="/docs/linux/man/8-mge-shut/">mge-shut</a></code>(8), <code><a href="/docs/linux/man/8-mge-utalk/">mge-utalk</a></code>(8), <code><a href="/docs/linux/man/8-oneac/">oneac</a></code>(8), <code><a href="/docs/linux/man/8-powercom/">powercom</a></code>(8), <code><a href="/docs/linux/man/8-safenet/">safenet</a></code>(8), <code><a href="/docs/linux/man/8-snmp-ups/">snmp-ups</a></code>(8), <code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8), <code><a href="/docs/linux/man/8-tripplitesu/">tripplitesu</a></code>(8), <code><a href="/docs/linux/man/8-victronups/">victronups</a></code>(8),</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
