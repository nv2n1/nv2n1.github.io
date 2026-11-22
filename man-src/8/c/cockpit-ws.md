---
title: "cockpit-ws(8)"
name: "cockpit-ws"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cockpit-ws/"
description: "cockpit-ws – Cockpit web service"
---

<p>cockpit-ws &#8211; Cockpit web service</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>cockpit-ws</code> [<code>&#8211;help</code>] [<code>&#8211;port</code>&nbsp;<wbr><i>PORT</i>] [<code>&#8211;no-tls</code>] [<code>&#8211;local-ssh</code>] [<code>&#8211;address</code>&nbsp;<wbr><i>ADDRESS</i>]</dt></dl>
<h2>Description</h2>
<dd>The <code>cockpit-ws</code> program is the web service component used for communication between the browser application and various configuration tools and services like <code>cockpit-bridge</code>(8). </dd>
<p> Users or administrators should never need to start this program as it automatically started by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) on bootup.</p>
<h2>Transport Security</h2>
<p>To specify the TLS certificate the web service should use, simply drop a file with the extension .cert in the /etc/cockpit/ws-certs.d directory. If there are multiple files in this directory, then the highest priority one is chosen after sorting. </p>
<p> The .cert file should contain at least two OpenSSL style PEM blocks. First one or more BEGIN CERTIFICATE blocks for the server certificate and intermediate certificate authorities and a last one containing a BEGIN PRIVATE KEY or similar. The key may not be encrypted. </p>
<p> If there is no TLS certificate, a self-signed certificate is automatically generated using <code>openssl</code> and stored in the 0-self-signed.cert file. To check which certificate <code>cockpit-ws</code> will use run the following command. </p>
<dl>
<dd>
<pre>$ sudo remotectl certificate</pre>
</dd></dl>
<h2>Timeout</h2>
<p>When started via <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) then <code>cockpit-ws</code> will exit after 90 seconds if nobody logs in, or after the last user is disconnected.</p>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dd></dl>
<p> <code>&#8211;local-ssh</code></p>
<dl>
<dd>Normally <code>cockpit-ws</code> uses <code>cockpit-session</code> and PAM to authenticate the user and start a user session. With this option enabled, it will instead authenticate via SSH at 127.0.0.1 port 22.</dd></dl>
<p> <code>&#8211;port</code> <i>PORT</i></p>
<dl>
<dd>Serve HTTP requests <i>PORT</i> instead of port 9090. Usually Cockpit is started on demand by <code>systemd</code> socket activation, and this option has no effect. Update the ListenStream directive cockpit.socket file in the usual <code>systemd</code> manner.</dd></dl>
<p> <code>&#8211;address</code> <i>ADDRESS</i></p>
<dl>
<dd>Bind to address <i>ADDRESS</i> instead of binding to all available addresses. Usually Cockpit is started on demand by <code>systemd</code> socket activation, and this option has no effect. In that case, update the ListenStream directive in the cockpit.socket file in the usual <code>systemd</code> manner.</dd></dl>
<p> <code>&#8211;no-tls</code></p>
<dl>
<dd>Don&#8217;t use TLS.</dd></dl>
<h2>Environment</h2>
<p>The <code>cockpit-ws</code> process will use the XDG_CONFIG_DIRS environment variable from the m[blue]<code>XDG basedir spec</code>m[][1] to find its <code><a href="/docs/linux/man/5-cockpit-conf/">cockpit.conf</a></code>(5) configuration file. </p>
<p> In addition the XDG_DATA_DIRS environment variable from the m[blue]<code>XDG basedir spec</code>m[][1] can be used to override the location to serve static files from. These are the files that are served to a non-logged in user.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[][2].</p>
<h2>Author</h2>
<p>Cockpit has been written by many m[blue]<code>contributors</code>m[][3].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cockpit-conf/">cockpit.conf</a></code>(5) , <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>XDG basedir spec</dd>
<dl>
<dd><a rel="nofollow" href="https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html">https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html</a></dd></dl>
<dt> 2.</dt>
<dd>upstream bug tracker</dd>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dd></dl>
<dt> 3.</dt>
<dd>contributors</dd>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dd></dl>
</dl>