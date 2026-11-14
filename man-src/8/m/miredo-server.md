---
title: "miredo-server(8)"
name: "miredo-server"
section: "8"
letter: "m"
url: "/docs/linux/man/8-miredo-server/"
description: "miredo-server – Teredo server for Unix"
---

<p>miredo-server &#8211; Teredo server for Unix</p>
<h2>Synopsis</h2>
<p><code>miredo-server</code> [<code>-c config_file</code>] [<code>-f</code>] [<code>-u user</code>] [<code>server_name</code>] </p>
<h2>Descripton</h2>
<p><code>Miredo-server</code> is an Unix daemon program which implements a Teredo server as specified by the &quot;Teredo: Tunneling IPv6 over UDP through NATs&quot; Internet proposed standard (RFC 4380). </p>
<p> A Teredo server is required for Teredo clients to setup their IPv6 connectivity through Teredo. A Teredo server must have two global static subsequent IPv4 addresses. It receives packets from Teredo clients and Teredo relays on UDP port 3544.</p>
<h2>Options</h2>
<dl>
<dt><code>-c config_file</code> or <code>&#8211;config config_file</code></p>
<dd>Specify an alternate configuration file for Miredo instead of the default, <i>/etc/miredo/miredo-server.conf</i>. </p>
<dt><code>-f</code> or <code>&#8211;foreground</code></p>
<dd>Do not detach from the console. Run the program in the foreground. </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-u username</code> or <code>&#8211;user username</code></p>
<dd>Override the user that the program will run as. By default, it runs as <code>nobody</code>. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and license and exit. </p>
</dl>
<h2>Security</h2>
<p><code>miredo-server</code> requires <i>root</i> privileges to create open a raw IPv6 socket that is used to emit ICMPv6 Echo Request packets. Once its initialization is complete, it will <i>setgid</i>, <i>chroot</i> into an empty directory and ultimately <i>setuid</i> (see option <i>-u</i>), so as to decrease the system&#8217;s exposure to potential security issues.</p>
<h2>Signals</h2>
<p><code>SIGHUP</code> Force a reload of the daemon. </p>
<p> <code>SIGINT</code>, <code>SIGTERM</code> Shutdown the daemon. </p>
<p> <code>SIGUSR1</code>, <code>SIGUSR2</code> Do nothing, might be used in future versions.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/miredo/miredo-server.conf</i></p>
<dd>The default configuration file. </p>
<dt><i>/var/run/miredo-server.pid</i></p>
<dd>The process-id file. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-miredo-server-conf/">miredo-server.conf</a>(5), <a href="/docs/linux/man/8-miredo/">miredo</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a></p>
