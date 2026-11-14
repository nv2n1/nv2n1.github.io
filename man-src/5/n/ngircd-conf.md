---
title: "ngircd-conf(5)"
name: "ngircd-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ngircd-conf/"
description: "ngircd.conf – configuration file of ngIRCd"
---

<p>ngircd.conf &#8211; configuration file of ngIRCd</p>
<h2>Synopsis</h2>
<p><code>/etc/ngircd.conf</code></p>
<h2>Description</h2>
<p><code>ngircd.conf</code> is the configuration file of the <code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) Internet Relay Chat (IRC) daemon, which must be customized to the local preferences and needs. </p>
<p> Most variables can be modified while the ngIRCd daemon is already running: It will reload its configuration file when a HUP signal or REHASH command is received.</p>
<h2>File Format</h2>
<p>The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. </p>
<p> Sections contain parameters of the form </p>
<dl>
<dd><i>name</i> = <i>value</i></dl>
<p> Empty lines and any line beginning with a semicolon (&#8216;;&#8217;) or a hash (&#8216;#&#8217;) character are treated as a comment and will be ignored. Leading and trailing whitespaces are trimmed before any processing takes place. </p>
<p> The file format is line-based &#8211; that means, each non-empty newline-terminated line represents either a comment, a section name, or a parameter. </p>
<p> Section and parameter names are not case sensitive. </p>
<p> There are three types of variables: <i>booleans,</i> <i>text strings,</i> and <i>numbers.</i> Boolean values are <i>true</i> if they are &quot;yes&quot;, &quot;true&quot;, or any non-null integer. Text strings are used 1:1 without leading and following spaces; there is no way to quote strings. And for numbers all decimal integer values are valid. </p>
<p> In addition, some string or numerical variables accept lists of values, separated by commas (&quot;,&quot;).</p>
<h2>Section Overview</h2>
<p>The file can contain blocks of seven types: [Global], [Limits], [Options], [SSL], [Operator], [Server], and [Channel]. </p>
<p> The main configuration of the server is stored in the <i>[Global]</i> section, like the server name, administrative information and the ports on which the server should be listening. The variables in this section have to be adjusted to the local requirements most of the time, whereas all the variables in the other sections can be left on their defaults very often. </p>
<p> Options in the <i>[Limits]</i> block are used to tweak different limits and timeouts of the daemon, like the maximum number of clients allowed to connect to this server. Variables in the <i>[Options]</i> section can be used to enable or disable specific features of ngIRCd, like support for IDENT, PAM, IPv6, and protocol and cloaking features. The <i>[SSL]</i> block contains all SSL-related configuration variables. These three sections are all optional. </p>
<p> IRC operators of this server are defined in <i>[Operator]</i> blocks. Links to remote servers are configured in <i>[Server]</i> sections. And <i>[Channel]</i> blocks are used to configure pre-defined (&quot;persistent&quot;) IRC channels. </p>
<p> There can be more than one [Operator], [Server] and [Channel] section per configuration file, one for each operator, server, and channel. [Global], [Limits], [Options], and [SSL] sections can occure multiple times, too, but each variable overwrites itself, only the last assignment is relevant.</p>
<h2>[Global]</h2>
<p>The <i>[Global]</i> section is used to define the main configuration of the server, like the server name and the ports on which the server should be listening. These settings depend on your personal preferences, so you should make sure that they correspond to your installation and setup!</p>
<dl>
<dt><code>Name</code> (string; required)</p>
<dd>Server name in the IRC network. This is an individual name of the IRC server, it is not related to the DNS host name. It must be unique in the IRC network and must contain at least one dot (&quot;.&quot;) character.</p>
<dt><code>AdminInfo1</code>, <code>AdminInfo2</code>, <code>AdminEMail</code> (string)</p>
<dd>Information about the server and the administrator, used by the ADMIN command. This information is not required by the server but by RFC!</p>
<dt><code>HelpFile</code> (string)</p>
<dd>Text file which contains the ngIRCd help text. This file is required to display help texts when using the &quot;HELP &lt;cmd&gt;&quot; command. Please note: Changes made to this file take effect when ngircd starts up or is instructed to re-read its configuration file.</p>
<dt><code>Info</code> (string)</p>
<dd>Info text of the server. This will be shown by WHOIS and LINKS requests for example.</p>
<dt><code>Listen</code> (list of strings)</p>
<dd>A comma separated list of IP address on which the server should listen. If unset, the defaults value is &quot;0.0.0.0&quot; or, if ngIRCd was compiled with IPv6 support, &quot;::,0.0.0.0&quot;. So the server listens on all configured IP addresses and interfaces by default.</p>
<dt><code>MotdFile</code> (string)</p>
<dd>Text file with the &quot;message of the day&quot; (MOTD). This message will be shown to all users connecting to the server. Please note: Changes made to this file take effect when ngircd starts up or is instructed to re-read its configuration file.</p>
<dt><code>MotdPhrase</code> (string)</p>
<dd>A simple Phrase (&lt;256 chars) if you don&#8217;t want to use a MOTD file.</p>
<dt><code>Network</code> (string)</p>
<dd>The name of the IRC network to which this server belongs. This name is optional, should only contain ASCII characters, and can&#8217;t contain spaces. It is only used to inform clients. The default is empty, so no network name is announced to clients.</p>
<dt><code>Password</code> (string)</p>
<dd>Global password for all users needed to connect to the server. The default is empty, so no password is required. Please note: This feature is not available if ngIRCd is using PAM!</p>
<dt><code>PidFile</code> (string)</p>
<dd>This tells ngIRCd to write its current process ID to a file. Note that the &quot;PID file&quot; is written AFTER chroot and switching the user ID, therefore the directory the file resides in must be writable by the ngIRCd user and exist in the chroot directory (if configured, see above).</p>
<dt><code>Ports</code> (list of numbers)</p>
<dd>Port number(s) on which the server should listen for unencrypted connections. There may be more than one port, separated with commas (&quot;,&quot;). Default: 6667.</p>
<dt><code>ServerGID</code> (string or number)</p>
<dd>Group ID under which the ngIRCd daemon should run; you can use the name of the group or the numerical ID.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges!</dl>
<dl>
<dt><code>ServerUID</code> (string or number)</p>
<dd>User ID under which the ngIRCd daemon should run; you can use the name of the user or the numerical ID.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges! In addition, the configuration and MOTD files must be readable by this user, otherwise RESTART and REHASH won&#8217;t work!</dl>
<h2>[Limits]</h2>
<p>This section is used to define some limits and timeouts for this ngIRCd instance. Default values should be safe, but it is wise to double-check :-)</p>
<dl>
<dt><code>ConnectRetry</code> (number)</p>
<dd>The server tries every &lt;ConnectRetry&gt; seconds to establish a link to not yet (or no longer) connected servers. Default: 60.</p>
<dt><code>IdleTimeout</code> (number)</p>
<dd>Number of seconds after which the whole daemon should shutdown when no connections are left active after handling at least one client (0: never). This can be useful for testing or when ngIRCd is started using &quot;socket activation&quot; with <a href="/docs/linux/man/8-systemd/">systemd</a>(8), for example. Default: 0.</p>
<dt><code>MaxConnections</code> (number)</p>
<dd>Maximum number of simultaneous in- and outbound connections the server is allowed to accept (0: unlimited). Default: 0.</p>
<dt><code>MaxConnectionsIP</code> (number)</p>
<dd>Maximum number of simultaneous connections from a single IP address that the server will accept (0: unlimited). This configuration options lowers the risk of denial of service attacks (DoS). Default: 5.</p>
<dt><code>MaxJoins</code> (number)</p>
<dd>Maximum number of channels a user can be member of (0: no limit). Default: 10.</p>
<dt><code>MaxNickLength</code> (number)</p>
<dd>Maximum length of an user nickname (Default: 9, as in RFC 2812). Please note that all servers in an IRC network MUST use the same maximum nickname length!</p>
<dt><code>MaxListSize</code> (number)</p>
<dd>Maximum number of channels returned in response to a LIST command. Default: 100.</p>
<dt><code>PingTimeout</code> (number)</p>
<dd>After &lt;PingTimeout&gt; seconds of inactivity the server will send a PING to the peer to test whether it is alive or not. Default: 120.</p>
<dt><code>PongTimeout</code> (number)</p>
<dd>If a client fails to answer a PING with a PONG within &lt;PongTimeout&gt; seconds, it will be disconnected by the server. Default: 20.</dl>
<h2>[Options]</h2>
<p>Optional features and configuration options to further tweak the behavior of ngIRCd are configured in this section. If you want to get started quickly, you most probably don&#8217;t have to make changes here &#8212; they are all optional.</p>
<dl>
<dt><code>AllowedChannelTypes</code> (string)</p>
<dd>List of allowed channel types (channel prefixes) for newly created channels on the local server. By default, all supported channel types are allowed. Set this variable to the empty string to disallow creation of new channels by local clients at all. Default: #&amp;+</p>
<dt><code>AllowRemoteOper</code> (boolean)</p>
<dd>If this option is active, IRC operators connected to remote servers are allowed to control this local server using administrative commands, for example like CONNECT, DIE, SQUIT etc. Default: no.</p>
<dt><code>ChrootDir</code> (string)</p>
<dd>A directory to chroot in when everything is initialized. It doesn&#8217;t need to be populated if ngIRCd is compiled as a static binary. By default ngIRCd won&#8217;t use the chroot() feature.</dl>
<dl>
<dd><code>Attention:</code><br />
 For this to work the server must have been started with root privileges!</dl>
<dl>
<dt><code>CloakHost</code> (string)</p>
<dd>Set this hostname for every client instead of the real one. Default: empty, don&#8217;t change. Use %x to add the hashed value of the original hostname.</p>
<dt><code>CloakHostModeX</code> (string)</p>
<dd>Use this hostname for hostname cloaking on clients that have the user mode &quot;+x&quot; set, instead of the name of the server. Default: empty, use the name of the server. Use %x to add the hashed value of the original hostname</p>
<dt><code>CloakHostSalt</code> (string)</p>
<dd>The Salt for cloaked hostname hashing. When undefined a random hash is generated after each server start.</p>
<dt><code>CloakUserToNick</code> (boolean)</p>
<dd>Set every clients&#8217; user name and real name to their nickname and hide the one supplied by the IRC client. Default: no.</p>
<dt><code>ConnectIPv4</code> (boolean)</p>
<dd>Set this to no if you do not want ngIRCd to connect to other IRC servers using the IPv4 protocol. This allows the usage of ngIRCd in IPv6-only setups. Default: yes.</p>
<dt><code>ConnectIPv6</code> (boolean)</p>
<dd>Set this to no if you do not want ngIRCd to connect to other IRC servers using the IPv6 protocol. Default: yes.</p>
<dt><code>DefaultUserModes</code> (string)</p>
<dd>Default user mode(s) to set on new local clients. Please note that only modes can be set that the client could set using regular MODE commands, you can&#8217;t set &quot;a&quot; (away) for example! Default: none.</p>
<dt><code>DNS</code> (boolean)</p>
<dd>If set to false, ngIRCd will not make any DNS lookups when clients connect. If you configure the daemon to connect to other servers, ngIRCd may still perform a DNS lookup if required. Default: yes.</p>
<dt><code>Ident</code> (boolean)</p>
<dd>If ngIRCd is compiled with IDENT support this can be used to disable IDENT lookups at run time. Users identified using IDENT are registered without the &quot;~&quot; character prepended to their user name. Default: yes.</p>
<dt><code>IncludeDir</code> (string)</p>
<dd>Directory containing configuration snippets (*.conf), that should be read in after parsing the current configuration file. Default: none.</p>
<dt><code>MorePrivacy</code> (boolean)</p>
<dd>This will cause ngIRCd to censor user idle time, logon time as well as the PART/QUIT messages (that are sometimes used to inform everyone about which client software is being used). WHOWAS requests are also silently ignored, and NAMES output doesn&#8217;t list any clients for non-members. This option is most useful when ngIRCd is being used together with anonymizing software such as TOR or I2P and one does not wish to make it too easy to collect statistics on the users. Default: no.</p>
<dt><code>NoticeBeforeRegistration</code> (boolean)</p>
<dd>Normally ngIRCd doesn&#8217;t send any messages to a client until it is registered. Enable this option to let the daemon send &quot;NOTICE *&quot; messages to clients while connecting. Default: no.</p>
<dt><code>OperCanUseMode</code> (boolean)</p>
<dd>Should IRC Operators be allowed to use the MODE command even if they are not(!) channel-operators? Default: no.</p>
<dt><code>OperChanPAutoOp</code> (boolean)</p>
<dd>Should IRC Operators get AutoOp (+o) in persistent (+P) channels? Default: yes.</p>
<dt><code>OperServerMode</code> (boolean)</p>
<dd>If <code>OperCanUseMode</code> is enabled, this may lead the compatibility problems with Servers that run the ircd-irc2 Software. This Option &quot;masks&quot; mode requests by non-chanops as if they were coming from the server. Default: no; only enable it if you have ircd-irc2 servers in your IRC network.</p>
<dt><code>PAM</code> (boolean)</p>
<dd>If ngIRCd is compiled with PAM support this can be used to disable all calls to the PAM library at runtime; all users connecting without password are allowed to connect, all passwords given will fail. Users identified using PAM are registered without the &quot;~&quot; character prepended to their user name. Default: yes.</p>
<dt><code>PAMIsOptional</code> (boolean)</p>
<dd>When PAM is enabled, all clients are required to be authenticated using PAM; connecting to the server without successful PAM authentication isn&#8217;t possible. If this option is set, clients not sending a password are still allowed to connect: they won&#8217;t become &quot;identified&quot; and keep the &quot;~&quot; character prepended to their supplied user name. Please note: To make some use of this behavior, it most probably isn&#8217;t useful to enable &quot;Ident&quot;, &quot;PAM&quot; and &quot;PAMIsOptional&quot; at the same time, because you wouldn&#8217;t be able to distinguish between Ident&#8217;ified and PAM-authenticated users: both don&#8217;t have a &quot;~&quot; character prepended to their respective user names! Default: no.</p>
<dt><code>RequireAuthPing</code> (boolean)</p>
<dd>Let ngIRCd send an &quot;authentication PING&quot; when a new client connects, and register this client only after receiving the corresponding &quot;PONG&quot; reply. Default: no.</p>
<dt><code>ScrubCTCP</code> (boolean)</p>
<dd>If set to true, ngIRCd will silently drop all CTCP requests sent to it from both clients and servers. It will also not forward CTCP requests to any other servers. CTCP requests can be used to query user clients about which software they are using and which versions said software is. CTCP can also be used to reveal clients IP numbers. ACTION CTCP requests are not blocked, this means that /me commands will not be dropped, but please note that blocking CTCP will disable file sharing between users! Default: no.</p>
<dt><code>SyslogFacility</code> (string)</p>
<dd>Syslog &quot;facility&quot; to which ngIRCd should send log messages. Possible values are system dependent, but most probably &quot;auth&quot;, &quot;daemon&quot;, &quot;user&quot; and &quot;local1&quot; through &quot;local7&quot; are possible values; see <a href="/docs/linux/man/3-syslog/">syslog</a>(3). Default is &quot;local5&quot; for historical reasons, you probably want to change this to &quot;daemon&quot;, for example.</p>
<dt><code>WebircPassword</code> (string)</p>
<dd>Password required for using the WEBIRC command used by some Web-to-IRC gateways. If not set or empty, the WEBIRC command can&#8217;t be used. Default: not set.</dl>
<h2>[Ssl]</h2>
<p>All SSL-related configuration variables are located in the <i>[SSL]</i> section. Please note that this whole section is only recognized by ngIRCd when it is compiled with support for SSL using OpenSSL or GnuTLS!</p>
<dl>
<dt><code>CertFile</code> (string)</p>
<dd>SSL Certificate file of the private server key.</p>
<dt><code>CipherList</code> (string)</p>
<dd>Select cipher suites allowed for SSL/TLS connections. This defaults to &quot;HIGH:!aNULL:@STRENGTH:!SSLv3&quot; (OpenSSL) or &quot;SECURE128:-VERS-SSL3.0&quot; (GnuTLS). Please see &#8216;man 1ssl ciphers&#8217; (OpenSSL) and &#8216;man 3 gnutls_priority_init&#8217; (GnuTLS) for details.</p>
<dt><code>DHFile</code> (string)</p>
<dd>Name of the Diffie-Hellman Parameter file. Can be created with GnuTLS &quot;certtool &#8211;generate-dh-params&quot; or &quot;openssl dhparam&quot;. If this file is not present, it will be generated on startup when ngIRCd was compiled with GnuTLS support (this may take some time). If ngIRCd was compiled with OpenSSL, then (Ephemeral)-Diffie-Hellman Key Exchanges and several Cipher Suites will not be available.</p>
<dt><code>KeyFile</code> (string)</p>
<dd>Filename of SSL Server Key to be used for SSL connections. This is required for SSL/TLS support.</p>
<dt><code>KeyFilePassword</code> (string)</p>
<dd>OpenSSL only: Password to decrypt the private key file.</p>
<dt><code>Ports</code> (list of numbers)</p>
<dd>Same as <code>Ports</code> , except that ngIRCd will expect incoming connections to be SSL/TLS encrypted. Common port numbers for SSL-encrypted IRC are 6669 and 6697. Default: none.</dl>
<h2>[Operator]</h2>
<p><i>[Operator]</i> sections are used to define IRC Operators. There may be more than one <i>[Operator]</i> block, one for each local operator.</p>
<dl>
<dt><code>Name</code> (string)</p>
<dd>ID of the operator (may be different of the nickname).</p>
<dt><code>Password</code> (string)</p>
<dd>Password of the IRC operator.</p>
<dt><code>Mask</code> (string)</p>
<dd>Mask that is to be checked before an /OPER for this account is accepted. Example: nick!ident@*.example.com</dl>
<h2>[Server]</h2>
<p>Other servers are configured in <i>[Server]</i> sections. If you configure a port for the connection, then this ngIRCd tries to connect to to the other server on the given port (active); if not, it waits for the other server to connect (passive). </p>
<p> ngIRCd supports &quot;server groups&quot;: You can assign an &quot;ID&quot; to every server with which you want this ngIRCd to link, and the daemon ensures that at any given time only one direct link exists to servers with the same ID. So if a server of a group won&#8217;t answer, ngIRCd tries to connect to the next server in the given group (=&quot;with the same ID&quot;), but never tries to connect to more than one server of this group simultaneously. </p>
<p> There may be more than one <i>[Server]</i> block.</p>
<dl>
<dt><code>Name</code> (string)</p>
<dd>IRC name of the remote server.</p>
<dt><code>Host</code> (string)</p>
<dd>Internet host name (or IP address) of the peer.</p>
<dt><code>Bind</code> (string)</p>
<dd>IP address to use as source IP for the outgoing connection. Default is to let the operating system decide.</p>
<dt><code>Port</code> (number)</p>
<dd>Port of the remote server to which ngIRCd should connect (active). If no port is assigned to a configured server, the daemon only waits for incoming connections (passive, default).</p>
<dt><code>MyPassword</code> (string)</p>
<dd>Own password for this connection. This password has to be configured as <code>PeerPassword</code> on the other server. Must not have &#8216;:&#8217; as first character.</p>
<dt><code>PeerPassword</code> (string)</p>
<dd>Foreign password for this connection. This password has to be configured as <code>MyPassword</code> on the other server.</p>
<dt><code>Group</code> (number)</p>
<dd>Group of this server (optional).</p>
<dt><code>Passive</code> (boolean)</p>
<dd>Disable automatic connection even if port value is specified. Default: false. You can use the IRC Operator command CONNECT later on to create the link.</p>
<dt><code>SSLConnect</code> (boolean)</p>
<dd>Connect to the remote server using TLS/SSL. Default: false.</p>
<dt><code>ServiceMask</code> (string)</p>
<dd>Define a (case insensitive) list of masks matching nicknames that should be treated as IRC services when introduced via this remote server, separated by commas (&quot;,&quot;). REGULAR SERVERS DON&#8217;T NEED this parameter, so leave it empty (which is the default).</dl>
<dl>
<dd>When you are connecting IRC services which mask as a IRC server and which use &quot;virtual users&quot; to communicate with, for example &quot;NickServ&quot; and &quot;ChanServ&quot;, you should set this parameter to something like &quot;*Serv&quot;, &quot;*Serv,OtherNick&quot;, or &quot;NickServ,ChanServ,XyzServ&quot;.</dl>
<h2>[Channel]</h2>
<p>Pre-defined channels can be configured in <i>[Channel]</i> sections. Such channels are created by the server when starting up and even persist when there are no more members left. </p>
<p> Persistent channels are marked with the mode &#8216;P&#8217;, which can be set and unset by IRC operators like other modes on the fly. </p>
<p> There may be more than one <i>[Channel]</i> block.</p>
<dl>
<dt><code>Name</code> (string)</p>
<dd>Name of the channel, including channel prefix (&quot;#&quot; or &quot;&amp;&quot;).</p>
<dt><code>Topic</code> (string)</p>
<dd>Topic for this channel.</p>
<dt><code>Modes</code> (string)</p>
<dd>Initial channel modes.</p>
<dt><code>Key</code> (string)</p>
<dd>Sets initial channel key (only relevant if channel mode &quot;k&quot; is set).</p>
<dt><code>KeyFile</code> (string)</p>
<dd>Path and file name of a &quot;key file&quot; containing individual channel keys for different users. The file consists of plain text lines with the following syntax (without spaces!):</dl>
<dl>
<dd>
<dl>
<dd><i>user</i> : <i>nick</i> : <i>key</i></dl>
<p> <i>user</i> and <i>nick</i> can contain the wildcard character &quot;*&quot;.<br />
 <i>key</i> is an arbitrary password. </p>
<p> Valid examples are: </p>
<dl>
<dd>*:*:KeY<br />
 *:nick:123<br />
 ~user:*:xyz</dl>
<p> The key file is read on each JOIN command when this channel has a key (channel mode +k). Access is granted, if a) the channel key set using the MODE +k command or b) one of the lines in the key file match. </p>
<p> <code>Please note:</code><br />
 The file is not reopened on each access, so you can modify and overwrite it without problems, but moving or deleting the file will have not effect until the daemon re-reads its configuration!</dl>
<dl>
<dt><code>MaxUsers</code> (number)</p>
<dd>Set maximum user limit for this channel (only relevant if channel mode &quot;l&quot; is set).</dl>
<h2>Hints</h2>
<p>It&#8217;s wise to use &quot;ngircd &#8211;configtest&quot; to validate the configuration file after changing it. See <code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) for details.</p>
<h2>Author</h2>
<p>Alexander Barton, &lt;alex [at] barton.de&gt;<br />
 Florian Westphal, &lt;fw [at] strlen.de&gt; </p>
<p> Homepage: <a rel="nofollow" href="http://ngircd.barton.de/">http://ngircd.barton.de/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ngircd/">ngircd</a></code>(8) </p>
