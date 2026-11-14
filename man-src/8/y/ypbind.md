---
title: "ypbind(8)"
name: "ypbind"
section: "8"
letter: "y"
url: "/docs/linux/man/8-ypbind/"
description: "ypbind – NIS binding process"
---

<p>ypbind &#8211; NIS binding process</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ypbind</code> [-broadcast | -ypset | -ypsetme] [-c] [-f&nbsp;<wbr><i>configfile</i>] [-no-ping] [-broken-server] [-local-only] [-i | -ping-interval&nbsp;<wbr><i>ping-interval</i>] [-r | -rebind-interval&nbsp;<wbr><i>rebind-interval</i>] [-d | -debug] [-v | -verbose] [-n | -foreground] [-p&nbsp;<wbr><i>port</i>] [-log&nbsp;<wbr><i>log-options</i>] [-no-dbus]</p>
<dt> <code>ypbind</code> &#8211;version</p>
<dt> <code>ypbind</code> &#8211;help</dl>
<h2>Description</h2>
<p><code>ypbind</code></p>
<dd>finds the server for NIS domains and maintains the NIS binding information. The client (normally the NIS routines in the standard C library) could get the information over RPC from <code>ypbind</code> or read the binding files. The binding files resides in the directory /var/yp/binding and are conventionally named <code>[domainname].[version]</code>. The supported versions are 1 and 2. There could be several such files since it is possible for an NIS client to be bound to more than one domain. After a binding has been established, <code>ypbind</code> will send YPPROC_DOMAIN requests to the current NIS server at 20 seconds intervals. If it doesn&#8217;t get an response or the NIS server reports that he doesn&#8217;t have this domain any longer, <code>ypbind</code> will search for a new NIS server. All 15 minutes <code>ypbind</code> will check to see if the current NIS server is the fastest. If it find a server which answers faster, it will switch to this server. You could tell <code>ypbind</code> to use network broadcasts to find a new server, what is insecure, or you could give it a list of known secure servers. In this case <code>ypbind</code> will send a ping to all servers and binds to first one which answers. Unless the option <code>-debug</code> is used, ypbind detaches itself from the controlling terminal and puts itself into background. <code>ypbind</code> uses <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for logging errors and warnings. At startup or when receiving signal SIGHUP, <code>ypbind</code> parses the file /etc/yp.conf and tries to use the entries for its initial binding. A broadcast entry in the configuration file will overwrite a ypserver/server entry and a ypserver/server entry broadcast. If all given server are down, <code>ypbind</code> will <code>not</code> switch to use broadcast. <code>ypbind</code> will try at first /etc/hosts and then <code>DNS</code> for resolving the hosts names from /etc/yp.conf. If <code>ypbind</code> couldn&#8217;t reconfigure the search order, it will use only <code>DNS</code>. If <code>DNS</code> isn&#8217;t available, you could only use IP-addresses in /etc/hosts. <code>ypbind</code> could only reconfigure the search order with glibc 2.x. If the <code>-broadcast</code> option is specified, <code>ypbind</code> will ignore the configuration file. If the file does not exist or if there are no valid entries, <code>ypbind</code> exit. This <code>ypbind</code> version listens for DBUS messages from NetworkManager. If no NetworkManager is running at startup, <code>ypbind</code> will behave as usual and assumes there is a working network connection. If NetworkManager is running on the system, ypbind will only search and provide NIS informations, if NetworkManager tells that a network connection is available. If NetworkManager establishes a connection, <code>ypbind</code> will reread all configuration files, registers at the local portmapper and try to search NIS servers. If NetworkManager drops a connection, <code>ypbind</code> will unregister from portmapper. In Fedora we use <code>systemd</code> for starting services. We need to finish starting process of <code>ypbind</code> service not before service is fully started, which means <code>ypbind</code> daemon is prepared to answer. There is a test script /usr/libexec/ypbind-post-waitbind used in <code>ypbind.service</code>, that waits for <code>ypbind</code> daemon to be fully connected to NIS server and waits by default up to 45s. Sometimes this is not enough, because network set up can take longer than 45s during boot, so starting <code>ypbind.service</code> fails. User can increase the <code>timeout</code> by setting an environment variable <code>NISTIMEOUT</code> in /etc/sysconfig/ypbind. For example NISTIMEOUT=180 means ypbind will wait up to 180 seconds for binding to a NIS server. Another option is to enable NetworkManager-wait-online.service and add an ordering rule into <code>ypbind.service</code>, ideally by creating /etc/systemd/system/ypbind.service with the following content: </p>
<pre><code>.include /lib/systemd/system/ypbind.service
[Service]
After=NetworkManager-wait-online.service</code></pre>
<h2>Options</h2>
<p><code>-broadcast</code></p>
<dl>
<dd>Send a broadcast to request the information needed to bind to a specific NIS server. With this option, /etc/yp.conf will be ignored.</dl>
<p> <code>-ypset</code></p>
<dl>
<dd>Allow <code>root</code> from any remote machine to change the binding for a domain via the <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8) command. By default, no one can change the binding. This option is really insecure. If you change a binding for a domain, all the current known servers for this domain will be forgotten. If the new server goes down, <code>ypbind</code> will use the old searchlist.</dl>
<p> <code>-ypsetme</code></p>
<dl>
<dd>The same as <code>-ypset</code>, but only <code>root</code> on the local machine is allowed to change the binding. Such requests are only allowed from <code>loopback</code>.</dl>
<p> <code>-c</code></p>
<dl>
<dd><code>ypbind</code> only checks if the config file has syntax errors and exits.</dl>
<p> <code>-d, -debug</code></p>
<dl>
<dd>starts <code>ypbind</code> in debug mode. <code>ypbind</code> will not put itself into background, and error messages and debug output are written to standard error.</dl>
<p> <code>-n, -foreground</code></p>
<dl>
<dd><code>ypbind</code> will not put itself into backgroun.</dl>
<p> <code>-v, -verbose</code></p>
<dl>
<dd>Causes <code>ypbind</code> to <a href="/docs/linux/man/2-syslog/">syslog</a>(2) any and all changes in the server its bound to.</dl>
<p> <code>-broken-server</code></p>
<dl>
<dd>Lets <code>ypbind</code> accept answers from servers running on an illegal port number. This should usually be avoided, but is required by some <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8) versions.</dl>
<p> <code>-no-ping</code></p>
<dl>
<dd><code>ypbind</code> will not check if the binding is alive. This option is for use with dialup connections to prevent <code>ypbind</code> from keeping the connection unnecessarily open or causing auto-dials.</dl>
<p> <code>-f</code> configfile</p>
<dl>
<dd><code>ypbind</code> will use <code>configfile</code> and not /etc/yp.conf</dl>
<p> <code>-local-only</code></p>
<dl>
<dd><code>ypbind</code> will only bind to the loopback device and is not reachable from a remote network.</dl>
<p> <code>-p port</code></p>
<dl>
<dd>Lets <code>ypbind</code> listen on a specified <code>port</code> number, rather than asking portmapper to assing a port for it.</dl>
<p> <code>-i, -ping-interval</code> ping-interval</p>
<dl>
<dd>The default value for <code>ypbind</code> to check, if a NIS server is still reachable, is 20 seconds. With this options another frequency in seconds can be specified.</dl>
<p> <code>-r, -rebind-interval</code> rebind-interval</p>
<dl>
<dd>The default value for <code>ypbind</code> to search for the fastest NIS server is 900 seconds (15 minutes). With this options another frequency in seconds can be specified.</dl>
<p> <code>-log</code> log-options</p>
<dl>
<dd>Allows to log special events. <code>log-options</code> is a logical sum of values for particular events &#8211; 1 for logging rpc calls, 2 for logging broken server calls, 4 for logging server changes.</dl>
<p> <code>-no-dbus</code></p>
<dl>
<dd>Disables DBUS support if compiled in.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Prints the version number</dl>
<h2>Files</h2>
<p>/etc/yp.conf</p>
<dl>
<dd>configuration file.</dl>
<p> /var/yp/binding/[domainname].[version]</p>
<dl>
<dd>binding file containing information about each NIS domain.</dl>
<p> /var/run/ypbind.pid</p>
<dl>
<dd>contains the process id of the currently running <code>ypbind</code> master process.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/1-domainname/">domainname</a></code>(1), <code><a href="/docs/linux/man/5-yp-conf/">yp.conf</a></code>(5), <code><a href="/docs/linux/man/8-ypdomainname/">ypdomainname</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypset/">ypset</a></code>(8)</p>
<h2>Author</h2>
<p><code>ypbind-mt</code> was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;.</p>
