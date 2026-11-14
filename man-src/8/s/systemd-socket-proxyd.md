---
title: "systemd-socket-proxyd(8)"
name: "systemd-socket-proxyd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-socket-proxyd/"
description: "systemd-socket-proxyd – Bidirectionally proxy local sockets to another (possibly remote) socket"
---

<p>systemd-socket-proxyd &#8211; Bidirectionally proxy local sockets to another (possibly remote) socket</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-socket-proxyd</code> [<i>OPTIONS</i>&#8230;] <i>HOST</i>:<i>PORT</i></p>
<dt> <code>systemd-socket-proxyd</code> [<i>OPTIONS</i>&#8230;] <i>UNIX-DOMAIN-SOCKET-PATH</i></dl>
<h2>Description</h2>
<p><code>systemd-socket-proxyd</code></p>
<dd>is a generic socket-activated network socket forwarder proxy daemon for IPv4, IPv6 and UNIX stream sockets. It may be used to bi-directionally forward traffic from a local listening socket to a local or remote destination socket. </p>
<p> One use of this tool is to provide socket activation support for services that do not natively support socket activation. On behalf of the service to activate, the proxy inherits the socket from systemd, accepts each client connection, opens a connection to a configured server for each client, and then bidirectionally forwards data between the two. </p>
<p> This utility&#8217;s behavior is similar to <code><a href="/docs/linux/man/1-socat/">socat</a></code>(1). The main differences for <code>systemd-socket-proxyd</code> are support for socket activation with &quot;Accept=no&quot; and an event-driven design that scales better with the number of connections.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<p> <code>&#8211;connections-max=</code>, <code>-c</code></p>
<dl>
<dd>Sets the maximum number of simultaneous connections, defaults to 256. If the limit of concurrent connections is reached further connections will be refused.</dl>
<p> <code>&#8211;exit-idle-time=</code></p>
<dl>
<dd>Sets the time before exiting when there are no connections, defaults to <code>infinity</code>. Takes a unit-less value in seconds, or a time span value such as &quot;5min 20s&quot;.</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>Examples</h2>
<h3>Simple Example</h3>
<p>Use two services with a dependency and no namespace isolation. </p>
<p> <code>Example 1. proxy-to-nginx.socket</code> </p>
<dl>
<dd>
<pre>[Socket]
ListenStream=80
[Install]
WantedBy=sockets.target</pre>
</dl>
<p> <code>Example 2. proxy-to-nginx.service</code> </p>
<dl>
<dd>
<pre>[Unit]
Requires=nginx.service
After=nginx.service
Requires=proxy-to-nginx.socket
After=proxy-to-nginx.socket
[Service]
ExecStart=/lib/systemd/systemd-socket-proxyd /run/nginx/socket
PrivateTmp=yes
PrivateNetwork=yes</pre>
</dl>
<p> <code>Example 3. nginx.conf</code> </p>
<dl>
<dd>
<pre>[...]
server {
 listen unix:/run/nginx/socket;
 [...]</pre>
</dl>
<p> <code>Example 4. Enabling the proxy</code> </p>
<dl>
<dd>
<pre># systemctl enable --now proxy-to-nginx.socket
$ curl <a rel="nofollow" href="http://localhost:80/">http://localhost:80/</a></pre>
</dl>
<p> If nginx.service has <i>StopWhenUnneeded=</i> set, then passing <code>&#8211;exit-idle-time=</code> to <code>systemd-socket-proxyd</code> allows both services to stop during idle periods.</p>
<h3>Namespace Example</h3>
<p>Similar as above, but runs the socket proxy and the main service in the same private namespace, assuming that nginx.service has <i>PrivateTmp=</i> and <i>PrivateNetwork=</i> set, too. </p>
<p> <code>Example 5. proxy-to-nginx.socket</code> </p>
<dl>
<dd>
<pre>[Socket]
ListenStream=80
[Install]
WantedBy=sockets.target</pre>
</dl>
<p> <code>Example 6. proxy-to-nginx.service</code> </p>
<dl>
<dd>
<pre>[Unit]
Requires=nginx.service
After=nginx.service
Requires=proxy-to-nginx.socket
After=proxy-to-nginx.socket
JoinsNamespaceOf=nginx.service
[Service]
ExecStart=/lib/systemd/systemd-socket-proxyd 127.0.0.1:8080
PrivateTmp=yes
PrivateNetwork=yes</pre>
</dl>
<p> <code>Example 7. nginx.conf</code> </p>
<dl>
<dd>
<pre>[...]
server {
 listen 8080;
 [...]</pre>
</dl>
<p> <code>Example 8. Enabling the proxy</code> </p>
<dl>
<dd>
<pre># systemctl enable --now proxy-to-nginx.socket
$ curl <a rel="nofollow" href="http://localhost:80/">http://localhost:80/</a></pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/1-socat/">socat</a></code>(1), <code><a href="/docs/linux/man/1-nginx/">nginx</a></code>(1), <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1) </p>
