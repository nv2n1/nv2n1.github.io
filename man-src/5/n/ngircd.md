---
title: "ngircd(5)"
name: "ngircd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ngircd/"
description: "ngircd.conf – configuration file of ngIRCd"
---

<p>ngircd.conf &#8211; configuration file of ngIRCd</p>
<h2>Synopsis</h2>
<p><code>/etc/ngircd.conf</code></p>
<h2>Description</h2>
<p><code>ngircd.conf</code> is the configuration file of the <code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) Internet Relay Chat (IRC) daemon which you should adept to your local preferences and needs.</p>
<h2>File Format</h2>
<p>The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. </p>
<p> Sections contain parameters of the form </p>
<dl>
<dd><i>name</i> = <i>value</i></dl>
<p> Empty lines and any line beginning with a semicolon (&#8216;;&#8217;) or a hash (&#8216;#&#8217;) character are treated as a comment and will be ignored. Leading and trailing whitespaces are trimmed before any processing takes place. </p>
<p> The file format is line-based &#8211; that means, each non-empty newline-terminated line represents either a comment, a section name, or a parameter. </p>
<p> Section and parameter names are not case sensitive.</p>
<h2>Section Overview</h2>
<p>The file can contain blocks of four types: [Global], [Operator], [Server], and [Channel]. </p>
<p> The main configuration of the server is stored in the <i>[Global]</i> section, like the server name, administrative information and the ports on which the server should be listening. IRC operators of this server are defined in <i>[Operator]</i> blocks. <i>[Server]</i> is the section where server links are configured. And <i>[Channel]</i> blocks are used to configure pre-defined (&quot;persistent&quot;) IRC channels. </p>
<p> There can be more than one [Operator], [Server] and [Channel] sections per configuration file, but only one [Global] section.</p>
<h2>[Global]</h2>
<p>The <i>[Global]</i> section is used to define the server main configuration, like the server name and the ports on which the server should be listening.</p>
<dl>
<dt><code>Name</code></p>
<dd>Server name in the IRC network, must contain at least one dot (&quot;.&quot;).</p>
<dt><code>Info</code></p>
<dd>Info text of the server. This will be shown by WHOIS and LINKS requests for example.</p>
<dt><code>AdminInfo1</code>, <code>AdminInfo2</code>, <code>AdminEMail</code></p>
<dd>Information about the server and the administrator, used by the ADMIN command.</p>
<dt><code>Ports</code></p>
<dd>Ports on which the server should listen. There may be more than one port, separated with &#8216;,&#8217;. Default: 6667.</p>
<dt><code>Listen</code></p>
<dd>A comma seperated list of IP address on which the server should listen. If unset, the defaults value is &quot;0.0.0.0&quot;, or, if ngircd was compiled with IPv6 support, &quot;::,0.0.0.0&quot;, so the server listens on all configured IP addresses and interfaces by default.</p>
<dt><code>MotdFile</code></p>
<dd>Text file with the &quot;message of the day&quot; (MOTD). This message will be shown to all users connecting to the server.</p>
<dt><code>MotdPhrase</code></p>
<dd>A simple Phrase (&lt;256 chars) if you don&#8217;t want to use a MOTD file. If it is set no MotdFile will be read at all which can be handy if the daemon should run inside a chroot directory.</p>
<dt><code>ServerUID</code></p>
<dd>User ID under which the server should run; you can use the name of the user or the numerical ID.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges! In addition, the configuration and MOTD files must be readable by this user, otherwise RESTART and REHASH won&#8217;t work!</dl>
<dl>
<dt><code>ServerGID</code></p>
<dd>Group ID under which the ngIRCd should run; you can use the name of the group or the numerical ID.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges!</dl>
<dl>
<dt><code>ChrootDir</code></p>
<dd>A directory to chroot in when everything is initialized. It doesn&#8217;t need to be populated if ngIRCd is compiled as a static binary. By default ngIRCd won&#8217;t use the chroot() feature.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges!</dl>
<dl>
<dt><code>PidFile</code></p>
<dd>This tells ngIRCd to write its current process ID to a file. Note that the pidfile is written AFTER chroot and switching the user ID, i. e. the directory the pidfile resides in must be writeable by the ngIRCd user and exist in the chroot directory (if configured, see above).</p>
<dt><code>PingTimeout</code></p>
<dd>After &lt;PingTimeout&gt; seconds of inactivity the server will send a PING to the peer to test whether it is alive or not. Default: 120.</p>
<dt><code>PongTimeout</code></p>
<dd>If a client fails to answer a PING with a PONG within &lt;PongTimeout&gt; seconds, it will be disconnected by the server. Default: 20.</p>
<dt><code>ConnectRetry</code></p>
<dd>The server tries every &lt;ConnectRetry&gt; seconds to establish a link to not yet (or no longer) connected servers. Default: 60.</p>
<dt><code>OperCanUseMode</code></p>
<dd>Should IRC Operators be allowed to use the MODE command even if they are not(!) channel-operators? Default: no.</p>
<dt><code>OperServerMode</code></p>
<dd>If OperCanUseMode is enabled, this may lead the compatibility problems with Servers that run the ircd-irc2 Software. This Option &quot;masks&quot; mode requests by non-chanops as if they were coming from the server. Default: no.</p>
<dt><code>PredefChannelsOnly</code></p>
<dd>If enabled, no new channels can be created. Useful if you do not want to have channels other than those defined in the config file. Default: No.</p>
<dt><code>NoDNS</code></p>
<dd>If enabled, ngircd will not make DNS lookups when clients connect. If you configure ngircd to connect to other servers, ngircd may still perform a DNS lookup if required. Default: No.</p>
<dt><code>ConnectIPv4</code></p>
<dd>Set this to no if you do not want ngircd to connect to other irc servers using ipv4. This allows use of ngircd in ipv6-only setups. Default: Yes.</p>
<dt><code>ConnectIPv6</code></p>
<dd>Set this to no if you do not want ngircd to connect to other irc servers using ipv6. Default: Yes.</p>
<dt><code>MaxConnections</code></p>
<dd>Maximum number of simultaneous connection the server is allowed to accept (0: unlimited). Default: 0.</p>
<dt><code>MaxConnectionsIP</code></p>
<dd>Maximum number of simultaneous connections from a single IP address that the server will accept (0: unlimited). This configuration options lowers the risk of denial of service attacks (DoS). Default: 5.</p>
<dt><code>MaxJoins</code></p>
<dd>Maximum number of channels a user can be member of (0: no limit). Default: 10.</p>
<dt><code>MaxNickLength</code></p>
<dd>Maximum length of an user nick name (Default: 9, as in RFC 2812). Please note that all servers in an IRC network MUST use the same maximum nick name length!</dl>
<h2>[Operator]</h2>
<p><i>[Operator]</i> sections are used to define IRC Operators. There may be more than one <i>[Operator]</i> block, one for each local operator.</p>
<dl>
<dt><code>Name</code></p>
<dd>ID of the operator (may be different of the nick name).</p>
<dt><code>Password</code></p>
<dd>Password of the IRC operator.</p>
<dt><code>Mask</code></p>
<dd>Mask that is to be checked before an /OPER for this account is accepted. Example: nick!ident@*.example.com</dl>
<h2>[Server]</h2>
<p>Other servers are configured in <i>[Server]</i> sections. If you configure a port for the connection, then this ngIRCd tries to connect to to the other server on the given port (active); if not, it waits for the other server to connect (passive). </p>
<p> ngIRCd supports &quot;server groups&quot;: You can assign an &quot;ID&quot; to every server with which you want this ngIRCd to link, and the daemon ensures that at any given time only one direct link exists to servers with the same ID. So if a server of a group won&#8217;t answer, ngIRCd tries to connect to the next server in the given group (=&quot;with the same ID&quot;), but never tries to connect to more than one server of this group simultaneously. </p>
<p> There may be more than one <i>[Server]</i> block.</p>
<dl>
<dt><code>Name</code></p>
<dd>IRC name of the remote server.</p>
<dt><code>Host</code></p>
<dd>Internet host name (or IP address) of the peer.</p>
<dt><code>Bind</code></p>
<dd>IP address to use as source IP for the outgoing connection. Default ist to let the operating system decide.</p>
<dt><code>Port</code></p>
<dd>Port of the remote server to which ngIRCd should connect (active). If no port is assigned to a configured server, the daemon only waits for incoming connections (passive).</p>
<dt><code>MyPassword</code></p>
<dd>Own password for this connection. This password has to be configured as &quot;PeerPassword&quot; on the other server. Must not have &#8216;:&#8217; as first character.</p>
<dt><code>PeerPassword</code></p>
<dd>Foreign password for this connection. This password has to be configured as &quot;MyPassword&quot; on the other server.</p>
<dt><code>Group</code></p>
<dd>Group of this server (optional).</p>
<dt><code>Passive</code></p>
<dd>Disable automatic connection even if port value is specified. Default: false. You can use the IRC Operator command CONNECT later on to create the link.</dl>
<h2>[Channel]</h2>
<p>Pre-defined channels can be configured in <i>[Channel]</i> sections. Such channels are created by the server when starting up and even persist when there are no more members left. </p>
<p> Persistent channels are marked with the mode &#8216;P&#8217;, which can be set and unset by IRC operators like other modes on the fly. </p>
<p> There may be more than one <i>[Channel]</i> block.</p>
<dl>
<dt><code>Name</code></p>
<dd>Name of the channel, including channel prefix (&quot;#&quot;).</p>
<dt><code>Topic</code></p>
<dd>Topic for this channel.</p>
<dt><code>Modes</code></p>
<dd>Initial channel modes.</p>
<dt><code>Key</code></p>
<dd>Sets initial channel key (only relevant if mode k is set).</p>
<dt><code>MaxUsers</code></p>
<dd>Set maximum user limit for this channel (only relevant if mode l is set).</dl>
<h2>Hints</h2>
<p>It&#8217;s wise to use &quot;ngircd &#8211;configtest&quot; to validate the configuration file after changing it. See <code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) for details.</p>
<h2>Author</h2>
<p>Alexander Barton, alex [at] barton.de<br />
 Homepage: <a rel="nofollow" href="http://ngircd.barton.de/">http://ngircd.barton.de/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) </p>
