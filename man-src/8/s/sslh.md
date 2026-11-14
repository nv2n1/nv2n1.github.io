---
title: "sslh(8)"
name: "sslh"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sslh/"
---

<pre> sslh - protocol demultiplexer</pre>
<h2>Synopsis</h2>
<p>sslh [<code>-F</code> <i>config file</i>] [ <code>-t</code> <i>num</i> ] [<code>&#8211;transparent</code>] [<code>-p</code> <i>listening address</i> [<code>-p</code> <i>listening address</i> &#8230;] [<code>&#8211;ssl</code> <i>target address for </i><font SIZE="-1"><i>SSL</i></font><i></i>] [<code>&#8211;ssh</code> <i>target address for </i><font SIZE="-1"><i>SSH</i></font><i></i>] [<code>&#8211;openvpn</code> <i>target address for OpenVPN</i>] [<code>&#8211;http</code> <i>target address for </i><font SIZE="-1"><i>HTTP</i></font><i></i>] [<code>&#8211;anyprot</code> <i>default target address</i>] [<code>&#8211;on-timeout</code> <i>protocol name</i>] [<code>-u</code> <i>username</i>] [<code>-P</code> <i>pidfile</i>] [-v] [-i] [-V] [-f] [-n]</p>
<h2>Description</h2>
<p><code>sslh</code> accepts connections on specified ports, and forwards them further based on tests performed on the first data packet sent by the remote client. </p>
<p> Probes for <font SIZE="-1">HTTP, SSL, SSH,</font> OpenVPN, tinc, <font SIZE="-1">XMPP</font> are implemented, and any other protocol that can be tested using a regular expression, can be recognised. A typical use case is to allow serving several services on port 443 (e.g. to connect to ssh from inside a corporate firewall, which almost never block port 443) while still serving <font SIZE="-1">HTTPS</font> on that port. </p>
<p> Hence <code>sslh</code> acts as a protocol demultiplexer, or a switchboard. Its name comes from its original function to serve <font SIZE="-1">SSH</font> and <font SIZE="-1">HTTPS</font> on the same port.</p>
<h3>Libwrap support</h3>
<p>One drawback of <code>sslh</code> is that the servers do not see the original <font SIZE="-1">IP</font> address of the client anymore, as the connection is forwarded through <code>sslh</code>. </p>
<p> For this reason, <code>sslh</code> can be compiled with <code>libwrap</code> to check accesses defined in <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>. Libwrap services can be defined using the configuration file.</p>
<h3>Configuration file</h3>
<p>A configuration file can be supplied to <code>sslh</code>. Command line arguments override file settings. <code>sslh</code> uses <code>libconfig</code> to parse the configuration file, so the general file format is indicated in &lt;<a rel="nofollow" href="http://www.hyperrealm.com/libconfig/libconfig_manual.html">http://www.hyperrealm.com/libconfig/libconfig_manual.html</a>&gt;. Please refer to the example configuration file provided with <code>sslh</code> for the specific format (Options have the same names as on the command line, except for the list of listen ports and the list of protocols). </p>
<p> The configuration file makes it possible to specify protocols using regular expressions: a list of regular expressions is given as the <i>regex_patterns</i> parameter, and if the first packet received from the client matches any of these expressions, <code>sslh</code> connects to that protocol.</p>
<h3>Probing protocols</h3>
<p>When receiving an incoming connection, <code>sslh</code> will read the first bytes sent be the connecting client. It will then probe for the protocol in the order specified on the command line (or the configuration file). Therefore <code>&#8211;anyprot</code> should alway be used last, as it always succeeds and further protocols will never be tried. </p>
<p> If no data is sent by the client, <code>sslh</code> will eventually time out and connect to the protocol specified with <code>&#8211;on-timeout</code>, or <i>ssh</i> if none is specified.</p>
<h3>Logging</h3>
<p>As a security/authorization program, <code>sslh</code> logs to the <font SIZE="-1">LOG_AUTH</font> facility, with priority <font SIZE="-1">LOG_INFO</font> for normal connections and <font SIZE="-1">LOG_ERR</font> for failures.</p>
<h2>Options</h2>
<dl>
<dt><code>-F</code> <i>filename</i>, <code>&#8211;config</code> <i>filename</i></p>
<dd>Uses <i>filename</i> has configuration file. If other command-line options are specified, they will override the configuration file&#8217;s settings.</p>
<dt><code>-t</code> <i>num</i>, <code>&#8211;timeout</code> <i>num</i></p>
<dd>Timeout before forwarding the connection to the timeout protocol (which should usually be <font SIZE="-1">SSH</font>). Default is 2s.</p>
<dt><code>&#8211;on-timeout</code> <i>protocol name</i></p>
<dd>Name of the protocol to connect to after the timeout period is over. Default is &#8216;ssh&#8217;.</p>
<dt><code>&#8211;transparent</code></p>
<dd>Makes <code>sslh</code> behave as a transparent proxy, i.e. the receiving service sees the original client&#8217;s <font SIZE="-1">IP</font> address. This works on Linux only and involves <code>iptables</code> settings. Refer to the <font SIZE="-1">README</font> for more information.</p>
<dt><code>-p</code> <i>listening address</i>, <code>&#8211;listen</code> <i>listening address</i></p>
<dd>Interface and port on which to listen, e.g. <i>foobar:443</i>, where <i>foobar</i> is the name of an interface (typically the <font SIZE="-1">IP</font> address on which the Internet connection ends up). </p>
<p> This can be specified several times to bind <code>sslh</code> to several addresses.</p>
<dt><code>&#8211;ssl</code> <i>target address</i></p>
<dd>
<dt><code>&#8211;tls</code> <i>target address</i></p>
<dd>Interface and port on which to forward <font SIZE="-1">SSL</font> connection, typically <i>localhost:443</i>. </p>
<p> Note that you can set <code>sslh</code> to listen on <i>ext_ip:443</i> and <code>httpd</code> to listen on <i>localhost:443</i>: this allows clients inside your network to just connect directly to <code>httpd</code>. </p>
<p> Also, <code>sslh</code> probes for SSLv3 (or TLSv1) handshake and will reject connections from clients requesting SSLv2. This is compliant to <font SIZE="-1">RFC6176</font> which prohibits the usage of SSLv2. If you wish to accept SSLv2, use <code>&#8211;default</code> instead.</p>
<dt><code>&#8211;ssh</code> <i>target address</i></p>
<dd>Interface and port on which to forward <font SIZE="-1">SSH</font> connections, typically <i>localhost:22</i>.</p>
<dt><code>&#8211;openvpn</code> <i>target address</i></p>
<dd>Interface and port on which to forward OpenVPN connections, typically <i>localhost:1194</i>.</p>
<dt><code>&#8211;xmpp</code> <i>target address</i></p>
<dd>Interface and port on which to forward <font SIZE="-1">XMPP</font> connections, typically <i>localhost:5222</i>.</p>
<dt><code>&#8211;http</code> <i>target address</i></p>
<dd>Interface and port on which to forward <font SIZE="-1">HTTP</font> connections, typically <i>localhost:80</i>.</p>
<dt><code>&#8211;tinc</code> <i>target address</i></p>
<dd>Interface and port on which to forward tinc connections, typically <i>localhost:655</i>. </p>
<p> This is experimental. If you use this feature, please report the results (even if it works!)</p>
<dt><code>&#8211;anyprot</code> <i>target address</i></p>
<dd>Interface and port on which to forward if no other protocol has been found. Because <code>sslh</code> tries protocols in the order specified on the command line, this should be specified last. If no default is specified, <code>sslh</code> will forward unknown protocols to the first protocol specified.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase verboseness.</p>
<dt><code>-n</code>, <code>&#8211;numeric</code></p>
<dd>Do not attempt to resolve hostnames: logs will contain <font SIZE="-1">IP</font> addresses. This is mostly useful if the system&#8217;s <font SIZE="-1">DNS</font> is slow and running the <i>sslh-select</i> variant, as <font SIZE="-1">DNS</font> requests will hang all connections.</p>
<dt><code>-V</code></p>
<dd>Prints <code>sslh</code> version.</p>
<dt><code>-u</code> <i>username</i>, <code>&#8211;user</code> <i>username</i></p>
<dd>Requires to run under the specified username.</p>
<dt><code>-P</code> <i>pidfile</i>, <code>&#8211;pidfile</code> <i>pidfile</i></p>
<dd>Specifies a file in which to write the <font SIZE="-1">PID</font> of the main server.</p>
<dt><code>-i</code>, <code>&#8211;inetd</code></p>
<dd>Runs as an <i>inetd</i> server. Options <code>-P</code> (<font SIZE="-1">PID</font> file), <code>-p</code> (listen address), <code>-u</code> (user) are ignored.</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>Runs in foreground. The server will not fork and will remain connected to the terminal. Messages normally sent to <code>syslog</code> will also be sent to <i>stderr</i>.</p>
<dt><code>&#8211;background</code></p>
<dd>Runs in background. This overrides <code>foreground</code> if set in the configuration file (or on the command line, but there is no point setting both on the command line unless you have a personality disorder).</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/systemd/system/sslh.service</i></p>
<dd>Systemd unit to control the daemon.</p>
<dt><i>/etc/sysconfig/sslh</i></p>
<dd>Server configuration. These are environment variables loaded by the start-up script and passed to <code>sslh</code> as command-line arguments. Refer to the <font SIZE="-1">OPTIONS</font> section for a detailed explanation of the variables used by <code>sslh</code>.</dl>
<h2>See Also</h2>
<p>Last version available from &lt;<a rel="nofollow" href="http://www.rutschle.net/tech/sslh">http://www.rutschle.net/tech/sslh</a>&gt;, and can be tracked from &lt;<a rel="nofollow" href="http://freecode.com/projects/sslh">http://freecode.com/projects/sslh</a>&gt;.</p>
<h2>Author</h2>
<p>Written by Yves Rutschle</p>
