---
title: "fastd(1)"
name: "fastd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fastd/"
description: "fastd – Fast and Secure Tunnelling Daemon"
---

<h2>NAME</h2>
<p> fastd &#8211; Fast and Secure Tunnelling Daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>fastd</code> <i>OPTION</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> fastd is a very small VPN daemon which tunnels IP packets and Ethernet frames over UDP. It supports various modern encryption and authentication schemes and can be used in many different network topologies (1:1, 1:n, meshed).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Shows a help text.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Shows the fastd version.</p>
<dt><code>&#8211;daemon</code>, <code>-d</code></p>
<dd> Runs fastd in the background.</p>
<dt><code>&#8211;pid-file</code> &lt;filename&gt;</p>
<dd> Writes fastd&#8217;s PID to the specified file.</p>
<dt><code>&#8211;status-socket</code> &lt;socket&gt;</p>
<dd> Configure a socket to get fastd&#8217;s status.</p>
<dt><code>&#8211;config</code>, <code>-c</code> &lt;filename&gt;</p>
<dd> Loads a config file. &#8211; can be specified to read a config file from stdin. More than one config file can be loaded.</p>
<dt><code>&#8211;config-peer</code> &lt;filename&gt;</p>
<dd> Loads a config file for a single peer. The filename will be used as the peer name.</p>
<dt><code>&#8211;config-peer-dir</code> &lt;dir&gt;</p>
<dd> Loads all files from a directory as peer configs. On <code>SIGHUP</code> fastd will reload peer directories.</p>
<dt><code>&#8211;user</code> &lt;user&gt;</p>
<dd> Sets the user to run fastd as.</p>
<dt><code>&#8211;group</code> &lt;group&gt;</p>
<dd> Sets the group to run fastd as.</p>
<dt><code>&#8211;log-level</code> error|warn|info|verbose|debug|debug2</p>
<dd> Sets the stderr log level; default is <i>info</i> if no alternative log destination is configured.</p>
<dt><code>&#8211;syslog-level</code> error|warn|info|verbose|debug|debug2</p>
<dd> Sets the log level for syslog output; default is not to use syslog.</p>
<dt><code>&#8211;syslog-ident</code> &lt;ident&gt;</p>
<dd> Sets the syslog identification; default is <i>fastd</i>.</p>
<dt><code>&#8211;hide-ip-addresses</code></p>
<dd> Hides IP addresses in log output.</p>
<dt><code>&#8211;hide-mac-addresses</code></p>
<dd> Hides MAC addresses in log output.</p>
<dt><code>&#8211;mode</code>, <code>-m</code> tap|multitap|tun</p>
<dd> Sets the mode of the interface; default is TAP mode.</p>
<dt><code>&#8211;interface</code>, <code>-i</code> &lt;name&gt;</p>
<dd> Sets the name of the TUN/TAP interface to use. If not specified, default names specified by the system will be used.</p>
<dt><code>&#8211;mtu</code>, <code>-M</code> &lt;mtu&gt;</p>
<dd> Sets the MTU; must be at least 576.</p>
<dt><code>&#8211;bind</code>, <code>-b</code> &lt;address&gt;[:&lt;port&gt;]</p>
<dd> Sets the bind address. Address can be an IPv4 address or an IPv6 address, or the keyword any. IPv6 addresses must be put in square brackets. </p>
<p> By default fastd will to bind to a random port for both IPv4 and IPv6. It is currently not possible to specify an IPv6 link-local address on the command line.</p>
<dt><code>&#8211;protocol</code>, <code>-p</code> &lt;protocol&gt;</p>
<dd> Sets the handshake protocol. Currently the only protocol available is <i>ec25519-fhmqvc</i>, which provides a secure authentication of peers based on public/secret keys.</p>
<dt><code>&#8211;method</code> &lt;method&gt;</p>
<dd> Sets the encryption method.</p>
<dt><code>&#8211;forward</code></p>
<dd> Enables forwarding of packets between peers; read the full documentation before use!</p>
<dt><code>&#8211;on-pre-up</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute before interface creation.</p>
<dt><code>&#8211;on-up</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute after interface creation.</p>
<dt><code>&#8211;on-down</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute before interface destruction.</p>
<dt><code>&#8211;on-post-down</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute after interface destruction.</p>
<dt><code>&#8211;on-connect</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute when a handshake is sent to establish a new connection.</p>
<dt><code>&#8211;on-establish</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute when a new connection is established.</p>
<dt><code>&#8211;on-disestablish</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute when a connection is lost.</p>
<dt><code>&#8211;on-verify</code> &lt;command&gt;</p>
<dd> Sets a shell command to execute to check a connection attempt by an unknown peer.</p>
<dt><code>&#8211;verify-config</code></p>
<dd> Checks the configuration and exits.</p>
<dt><code>&#8211;generate-key</code></p>
<dd> Generates a new keypair.</p>
<dt><code>&#8211;show-key</code></p>
<dd> Shows the public key corresponding to the configured secret.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> Suppresses output of explaining text in the <code>&#8211;show-key</code> and <code>&#8211;generate-key</code> commands.</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>fastd</code> is maintained in the Wiki at <i><a rel="nofollow" href="https://projects.universe-factory.net/projects/fastd/wiki/Fastd">https://projects.universe-factory.net/projects/fastd/wiki/Fastd</a></i>. </p>
<p> See the user manual at <i><a rel="nofollow" href="https://projects.universe-factory.net/projects/fastd/wiki/User_manual">https://projects.universe-factory.net/projects/fastd/wiki/User_manual</a></i> in particular. </p>
<h2>Index</h2>
