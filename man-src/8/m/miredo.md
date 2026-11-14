---
title: "miredo(8)"
name: "miredo"
section: "8"
letter: "m"
url: "/docs/linux/man/8-miredo/"
description: "miredo – Teredo IPv6 tunneling for Unix"
---

<p>miredo &#8211; Teredo IPv6 tunneling for Unix</p>
<h2>Synopsis</h2>
<p><code>miredo</code> [<code>-c config_file</code>] [<code>-f</code>] [<code>-u user</code>] [ <code>-t chrootdir</code>] [<code>server_name</code>] </p>
<h2>Descripton</h2>
<p><code>Miredo</code> is a daemon program providing a Teredo tunnel service compatible with the &quot;Teredo: Tunneling IPv6 over UDP through NATs&quot; Internet proposed standard (RFC 4380). It can provide either Teredo client or Teredo relay functionality. </p>
<p> This is mostly useful to provide IPv6 connectivity to users behind NAT, most of which do not support IPv6 at all. Many NATs do not even support <i>proto-41</i> forwarding, so it is not possible to set up a <i>6to4</i> or point-to-point <i>IPv6-over-IPv4</i> tunnel through them. </p>
<p> A Teredo relay is an IPv6 router which forwards IPv6 packets between the IPv6 Internet and Teredo clients by encapsulating these IPv6 packets over UDP/IPv4. </p>
<p> A Teredo client is an IPv6-enabled host which is located behind an IPv4-only Network Address Translator (a.k.a. NAT), and encapsulates its IPv6 traffic inside UDP over IPv4 packets. </p>
<p> A Teredo server is a special Teredo relay which is required for Teredo clients to setup their IPv6 connectivity through Teredo. A Teredo server must have to global static subsequent IPv4 addresses. It receives packets from Teredo clients and Teredo relays on UDP port 3544.</p>
<h2>Options</h2>
<dl>
<dt><code>-c config_file</code> or <code>&#8211;config config_file</code></p>
<dd>Specify an alternate configuration file for Miredo instead of the default, <i>/etc/miredo/miredo.conf</i>. </p>
<dt><code>-f</code> or <code>&#8211;foreground</code></p>
<dd>Do not detach from the console. Run the program in the foreground. </p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Display some help and exit. </p>
<dt><code>-t</code> or <code>&#8211;chrootdir</code></p>
<dd>Specify a directory to use as a root after initialization is completed. When used as a Teredo client, the hostname resolver library files must be present in the chroot. The directory can safely be left empty for a Teredo relay. </p>
<dt><code>-u username</code> or <code>&#8211;user username</code></p>
<dd>Override the user that the program will run as. By default, it runs as <code>nobody</code>. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd>Display program version and license and exit. </p>
<dt><code>server_name</code></p>
<dd>This optional command argument specifies a Teredo server to use. It will override any ServerAddress directive found in the configuration file. It is ignored if RelayType is not set to &quot;client&quot; (see miredo.conf). </p>
</dl>
<h2>Security</h2>
<p><code>Miredo</code> requires <i>root</i> privileges to create its IPv6 tunneling network interface, and to set it up properly. Once its initialization is complete, it will <i>setgid</i>, <i>chroot</i> into an empty directory and ultimately <i>setuid</i> (see option <i>-u</i>), so as to decrease the system&#8217;s exposure to potential security issues. However, if Miredo runs as a Teredo client, it needs root privileges when running, in order to change the tunneling network interface settings automatically. To prevent possible root compromise, Miredo implements <i>priveleges</i> <i>separation</i>. The process that handles data from the network is not privileged. </p>
<p> While that is not specific to nor dependant on Miredo, it should be noted that Teredo connectivity allows anyone behind a NAT to obtain global public IPv6 connectivity. It might break some corporate policy. If that is an issue, outgoing UDP packets with destination port 3544 should be blocked at the perimeter firewall.</p>
<h2>Signals</h2>
<p><code>SIGHUP</code> Force a reload of the daemon. </p>
<p> <code>SIGINT</code>, <code>SIGTERM</code> Shutdown the daemon. </p>
<p> <code>SIGUSR1</code>, <code>SIGUSR2</code> Do nothing, might be used in future versions.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/miredo/miredo.conf</i></p>
<dd>The default configuration file. </p>
<dt><i>/var/run/miredo.pid</i></p>
<dd>The process-id file. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-miredo-conf/">miredo.conf</a>(5), <a href="/docs/linux/man/8-miredo-server/">miredo-server</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7), <a href="/docs/linux/man/8-route/">route</a>(8), <a href="/docs/linux/man/8-ip/">ip</a>(8) </p>
<h2>Author</h2>
<p>R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a></p>
