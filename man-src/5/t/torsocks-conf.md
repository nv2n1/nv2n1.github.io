---
title: "torsocks-conf(5)"
name: "torsocks-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-torsocks-conf/"
description: "torsocks.conf — Configuration file for"
---

<p>torsocks.conf &#8212; Configuration file for </p>
<p><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8) </p>
<h2>Summary</h2>
<p>By default, torsocks will assume that it should connect to the Tor SOCKS proxy running at 127.0.0.1 on port 9050. This is the default address and port for Tor&#8217;s socks server on most installations. If you are running a normal Tor installation and have no special requirements, then you should not need to create, edit or invoke a configuration file when using torsocks. </p>
<p> Your installation of torsocks includes a default configuration file that contains values sensible for use with most Tor installations. The installation location for your default configuration file is: </p>
<p> /etc/tor/torsocks.conf </p>
<p> In order to use a configuration file, you must set the environment variable TORSOCKS_CONF_FILE with the location of the file. </p>
<p> If TORSOCKS_CONF_FILE is not set, torsocks will attempt to read the configuration file at /etc/tor/torsocks.conf. If that file cannot be read, torsocks will use sensible defaults for most Tor installations, i.e. it will assume that you want to use a SOCKS proxy running at 127.0.0.1 (localhost) on port 9050.</p>
<h2>Configuration</h2>
<h3>Syntax</h3>
<p>The basic structure of all lines in the configuration file is: </p>
<dl>
<dd>&lt;directive&gt; &lt;parameters&gt;</dl>
<p> Empty lines are ignored and all input on a line after a &#8216;#&#8217; character is ignored.</p>
<h3>Directives</h3>
<p>The following directives are used in the torsocks configuration file: </p>
<dl>
<dt><i>TorAddress ip_addr</i></p>
<dd>The IP address of the Tor SOCKS server (e.g &quot;server = 10.1.4.253&quot;). Only one server may be specified. Currently, torsocks does NOT support hostname. (default: 127.0.0.1) </p>
<dt><i>TorPort port</i></p>
<dd>The port on which the Tor SOCKS server receives requests. (default: 9050) </p>
<dt><i>OnionAddrRange subnet/mask</i></p>
<dd>Tor hidden sites do not have real IP addresses. This specifies what range of IP addresses will be handed to the application as &quot;cookies&quot; for .onion names. Of course, you should pick a block of addresses which you aren&#8217;t going to ever need to actually connect to. This is similar to the MapAddress feature of the main tor daemon. (default: 127.42.42.0/24) </p>
<dt><i>SOCKS5Username username</i></p>
<dd>Username to use for SOCKS5 authentication method that makes the connections to Tor to use a different circuit from other existing streams. If set, the SOCKS5Password must be specified also. (Default: none). </p>
<dt><i>SOCKS5Password password</i></p>
<dd>Password to use for SOCKS5 authentication method that makes the connections to Tor to use a different circuit from other existing streams. If set, the SOCKS5Username must be specified also. (Default: none). </p>
<dt><i>AllowInbound 0|1</i></p>
<dd>Allow inbound connections meaning that listen() and accept()/accept4() will be allowed for non localhost address so the applicaton can handle incoming connection. Note that Unix socket are allowed. (Default: 0) </p>
<dt><i>AllowOutboundLocalhost 0|1</i></p>
<dd>Allow outbound connections to the loopback interface meaning that connect() will be allowed to connect to localhost addresses bypassing Tor. This option should not be used by most users. (Default: 0) </p>
<dt><i>IsolatePID 0|1</i></p>
<dd>Set Torsocks to use an automatically generated SOCKS5 username/password based on the process ID and current time, that makes the connections to Tor use a different circuit from other existing streams in Tor on a per-process basis. If set, the SOCKS5Username and SOCKS5Password options must not be set. (Default: 0) </p>
</dl>
<h2>Example</h2>
<pre><code>$ export TORSOCKS_CONF_FILE=$PWD/torsocks.conf
$ torsocks ssh account [at] sshserver.com
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-torsocks/">torsocks</a>(1),</code> <code><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8),</code> </p>
<h2>Author</h2>
<p>David Goulet &lt;dgoulet [at] ev0ke.net&gt;</p>
