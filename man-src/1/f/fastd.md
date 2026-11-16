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
<dt><code>&#8211;help</code>, <code>-h</code></dt>
<dd> Shows a help text.</dd>
<dt><code>&#8211;version</code>, <code>-v</code></dt>
<dd> Shows the fastd version.</dd>
<dt><code>&#8211;daemon</code>, <code>-d</code></dt>
<dd> Runs fastd in the background.</dd>
<dt><code>&#8211;pid-file</code> &lt;filename&gt;</dt>
<dd> Writes fastd&#8217;s PID to the specified file.</dd>
<dt><code>&#8211;status-socket</code> &lt;socket&gt;</dt>
<dd> Configure a socket to get fastd&#8217;s status.</dd>
<dt><code>&#8211;config</code>, <code>-c</code> &lt;filename&gt;</dt>
<dd> Loads a config file. &#8211; can be specified to read a config file from stdin. More than one config file can be loaded.</dd>
<dt><code>&#8211;config-peer</code> &lt;filename&gt;</dt>
<dd> Loads a config file for a single peer. The filename will be used as the peer name.</dd>
<dt><code>&#8211;config-peer-dir</code> &lt;dir&gt;</dt>
<dd> Loads all files from a directory as peer configs. On <code>SIGHUP</code> fastd will reload peer directories.</dd>
<dt><code>&#8211;user</code> &lt;user&gt;</dt>
<dd> Sets the user to run fastd as.</dd>
<dt><code>&#8211;group</code> &lt;group&gt;</dt>
<dd> Sets the group to run fastd as.</dd>
<dt><code>&#8211;log-level</code> error|warn|info|verbose|debug|debug2</dt>
<dd> Sets the stderr log level; default is <i>info</i> if no alternative log destination is configured.</dd>
<dt><code>&#8211;syslog-level</code> error|warn|info|verbose|debug|debug2</dt>
<dd> Sets the log level for syslog output; default is not to use syslog.</dd>
<dt><code>&#8211;syslog-ident</code> &lt;ident&gt;</dt>
<dd> Sets the syslog identification; default is <i>fastd</i>.</dd>
<dt><code>&#8211;hide-ip-addresses</code></dt>
<dd> Hides IP addresses in log output.</dd>
<dt><code>&#8211;hide-mac-addresses</code></dt>
<dd> Hides MAC addresses in log output.</dd>
<dt><code>&#8211;mode</code>, <code>-m</code> tap|multitap|tun</dt>
<dd> Sets the mode of the interface; default is TAP mode.</dd>
<dt><code>&#8211;interface</code>, <code>-i</code> &lt;name&gt;</dt>
<dd> Sets the name of the TUN/TAP interface to use. If not specified, default names specified by the system will be used.</dd>
<dt><code>&#8211;mtu</code>, <code>-M</code> &lt;mtu&gt;</dt>
<dd> Sets the MTU; must be at least 576.</dd>
<dt><code>&#8211;bind</code>, <code>-b</code> &lt;address&gt;[:&lt;port&gt;]</dt>
<dd> Sets the bind address. Address can be an IPv4 address or an IPv6 address, or the keyword any. IPv6 addresses must be put in square brackets. </dd>
<p> By default fastd will to bind to a random port for both IPv4 and IPv6. It is currently not possible to specify an IPv6 link-local address on the command line.</p>
<dt><code>&#8211;protocol</code>, <code>-p</code> &lt;protocol&gt;</dt>
<dd> Sets the handshake protocol. Currently the only protocol available is <i>ec25519-fhmqvc</i>, which provides a secure authentication of peers based on public/secret keys.</dd>
<dt><code>&#8211;method</code> &lt;method&gt;</dt>
<dd> Sets the encryption method.</dd>
<dt><code>&#8211;forward</code></dt>
<dd> Enables forwarding of packets between peers; read the full documentation before use!</dd>
<dt><code>&#8211;on-pre-up</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute before interface creation.</dd>
<dt><code>&#8211;on-up</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute after interface creation.</dd>
<dt><code>&#8211;on-down</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute before interface destruction.</dd>
<dt><code>&#8211;on-post-down</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute after interface destruction.</dd>
<dt><code>&#8211;on-connect</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute when a handshake is sent to establish a new connection.</dd>
<dt><code>&#8211;on-establish</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute when a new connection is established.</dd>
<dt><code>&#8211;on-disestablish</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute when a connection is lost.</dd>
<dt><code>&#8211;on-verify</code> &lt;command&gt;</dt>
<dd> Sets a shell command to execute to check a connection attempt by an unknown peer.</dd>
<dt><code>&#8211;verify-config</code></dt>
<dd> Checks the configuration and exits.</dd>
<dt><code>&#8211;generate-key</code></dt>
<dd> Generates a new keypair.</dd>
<dt><code>&#8211;show-key</code></dt>
<dd> Shows the public key corresponding to the configured secret.</dd>
<dt><code>&#8211;machine-readable</code></dt>
<dd> Suppresses output of explaining text in the <code>&#8211;show-key</code> and <code>&#8211;generate-key</code> commands.</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>fastd</code> is maintained in the Wiki at <i><a rel="nofollow" href="https://projects.universe-factory.net/projects/fastd/wiki/Fastd">https://projects.universe-factory.net/projects/fastd/wiki/Fastd</a></i>. </p>
<p> See the user manual at <i><a rel="nofollow" href="https://projects.universe-factory.net/projects/fastd/wiki/User_manual">https://projects.universe-factory.net/projects/fastd/wiki/User_manual</a></i> in particular. </p>
<h2>Index</h2>
