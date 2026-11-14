---
title: "stunnel(8)"
name: "stunnel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stunnel/"
description: "stunnel – universal SSL tunnel"
---

<p>stunnel &#8211; universal SSL tunnel</p>
<h2>Synopsis</h2>
<dl>
<dt><code>Unix:</code></p>
<dd><code>stunnel</code> [&lt;filename&gt;] | -fd n | -help | -version | -sockets</p>
<dt><font SIZE="-1"><code>WIN32:</code></font></p>
<dd><code>stunnel</code> [ [-install | -uninstall | -start | -stop] | -exit]<br />
&nbsp;<wbr>[-quiet]&nbsp;<wbr>[&lt;filename&gt;]&nbsp;<wbr>]&nbsp;<wbr>| -help | -version | -sockets</dl>
<h2>Description</h2>
<p>The <code>stunnel</code> program is designed to work as <i></i><font SIZE="-1"><i>SSL</i></font><i></i> encryption wrapper between remote clients and local (<i>inetd</i>-startable) or remote servers. The concept is that having non-SSL aware daemons running on your system you can easily set them up to communicate with clients over secure <font SIZE="-1">SSL</font> channels. </p>
<p> <code>stunnel</code> can be used to add <font SIZE="-1">SSL</font> functionality to commonly used <i>Inetd</i> daemons like <font SIZE="-1">POP-2</font>, <font SIZE="-1">POP-3</font>, and <font SIZE="-1">IMAP</font> servers, to standalone daemons like <font SIZE="-1">NNTP</font>, <font SIZE="-1">SMTP</font> and <font SIZE="-1">HTTP</font>, and in tunneling <font SIZE="-1">PPP</font> over network sockets without changes to the source code. </p>
<p> This product includes cryptographic software written by Eric Young (eay [at] cryptsoft.com)</p>
<h2>Options</h2>
<dl>
<dt>&lt;<code>filename</code>&gt;</p>
<dd>Use specified configuration file</p>
<dt><code>-fd n</code> (Unix only)</p>
<dd>Read the config file from specified file descriptor</p>
<dt><code>-help</code></p>
<dd>Print <code>stunnel</code> help menu</p>
<dt><code>-version</code></p>
<dd>Print <code>stunnel</code> version and compile time defaults</p>
<dt><code>-sockets</code></p>
<dd>Print default socket options</p>
<dt><code>-install</code> (<font SIZE="-1">NT/2000/XP</font> only)</p>
<dd>Install <font SIZE="-1">NT</font> Service</p>
<dt><code>-uninstall</code> (<font SIZE="-1">NT/2000/XP</font> only)</p>
<dd>Uninstall <font SIZE="-1">NT</font> Service</p>
<dt><code>-start</code> (<font SIZE="-1">NT/2000/XP</font> only)</p>
<dd>Start <font SIZE="-1">NT</font> Service</p>
<dt><code>-stop</code> (<font SIZE="-1">NT/2000/XP</font> only)</p>
<dd>Stop <font SIZE="-1">NT</font> Service</p>
<dt><code>-exit</code> (Win32 only)</p>
<dd>Exit an already started stunnel</p>
<dt><code>-quiet</code> (<font SIZE="-1">NT/2000/XP</font> only)</p>
<dd>Don&#8217;t display any message boxes</dl>
<h2>Configuration File</h2>
<p>Each line of the configuration file can be either:</p>
<dl>
<dt>&bull;</p>
<dd>An empty line (ignored).</p>
<dt>&bull;</p>
<dd>A comment starting with &#8216;;&#8217; (ignored).</p>
<dt>&bull;</p>
<dd>An &#8216;option_name = option_value&#8217; pair.</p>
<dt>&bull;</p>
<dd>&#8216;[service_name]&#8217; indicating a start of a service definition.</dl>
<p> An address parameter of an option may be either:</p>
<dl>
<dt>&bull;</p>
<dd>A port number.</p>
<dt>&bull;</p>
<dd>A colon-separated pair of <font SIZE="-1">IP</font> address (either IPv4, IPv6, or domain name) and port number.</p>
<dt>&bull;</p>
<dd>A Unix socket path (Unix only).</dl>
<h3><font SIZE="-1">GLOBAL</font> <font SIZE="-1">OPTIONS</font></h3>
<dl>
<dt><code>chroot</code> = directory (Unix only)</p>
<dd>directory to chroot <code>stunnel</code> process </p>
<p> <code>chroot</code> keeps <code>stunnel</code> in chrooted jail. <i>CApath</i>, <i>CRLpath</i>, <i>pid</i> and <i>exec</i> are located inside the jail and the patches have to be relative to the directory specified with <code>chroot</code>. </p>
<p> Several functions of the operating system also need their files to be located within chroot jail, e.g.:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Delayed resolver typically needs /etc/nsswitch.conf and /etc/resolv.conf.</p>
<dt>&bull;</p>
<dd>Local time in log files needs /etc/timezone.</p>
<dt>&bull;</p>
<dd>Some other functions may need devices, e.g. /dev/zero or /dev/null.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>compression</code> = deflate | zlib | rle</p>
<dd>select data compression algorithm </p>
<p> default: no compression </p>
<p> deflate is the standard compression method as described in <font SIZE="-1">RFC</font> 1951. </p>
<p> zlib compression of <code>OpenSSL 0.9.8</code> or above is not backward compatible with <code>OpenSSL 0.9.7</code>. </p>
<p> rle compression is currently not implemented by the <code>OpenSSL</code> library.</p>
<dt><code>debug</code> = [facility.]level</p>
<dd>debugging level </p>
<p> Level is a one of the syslog level names or numbers emerg (0), alert (1), crit (2), err (3), warning (4), notice (5), info (6), or debug (7). All logs for the specified level and all levels numerically less than it will be shown. Use <i>debug = debug</i> or <i>debug = 7</i> for greatest debugging output. The default is notice (5). </p>
<p> The syslog facility &#8216;authpriv&#8217; will be used unless a facility name is supplied. (Facilities are not supported on Win32.) </p>
<p> Case is ignored for both facilities and levels.</p>
<dt><font SIZE="-1"><code>EGD</code></font> = egd path (Unix only)</p>
<dd>path to Entropy Gathering Daemon socket </p>
<p> Entropy Gathering Daemon socket to use to feed <code>OpenSSL</code> random number generator. (Available only if compiled with <code>OpenSSL 0.9.5a</code> or higher)</p>
<dt><code>engine</code> = auto | &lt;engine id&gt;</p>
<dd>select hardware engine </p>
<p> default: software-only cryptography </p>
<p> Here is an example of advanced engine configuration to read private key from an OpenSC engine </p>
<pre> engine=dynamic
 engineCtrl=SO_PATH:/usr/lib/opensc/engine_pkcs11.so
 engineCtrl=ID:pkcs11
 engineCtrl=LIST_ADD:1
 engineCtrl=LOAD
 engineCtrl=MODULE_PATH:/usr/lib/pkcs11/opensc-pkcs11.so
 engineCtrl=INIT
 [service]
 engineNum=1
 key=id_45</pre>
<dt><code>engineCtrl</code> = command[:parameter]</p>
<dd>control hardware engine </p>
<p> Special commands &#8220;<font SIZE="-1">LOAD</font>&#8221; and &#8220;<font SIZE="-1">INIT</font>&#8221; can be used to load and initialize the engine cryptogaphic module.</p>
<dt><code>fips</code> = yes | no</p>
<dd>Enable or disable <font SIZE="-1">FIPS</font> 140-2 mode. </p>
<p> This option allows to disable entering <font SIZE="-1">FIPS</font> mode if <code>stunnel</code> was compiled with <font SIZE="-1">FIPS</font> 140-2 support. </p>
<p> default: yes</p>
<dt><code>foreground</code> = yes | no (Unix only)</p>
<dd>foreground mode </p>
<p> Stay in foreground (don&#8217;t fork) and log to stderr instead of via syslog (unless <i>output</i> is specified). </p>
<p> default: background in daemon mode</p>
<dt><code>output</code> = file</p>
<dd>append log messages to a file </p>
<p> /dev/stdout device can be used to send log messages to the standard output (for example to log them with daemontools splogger).</p>
<dt><code>pid</code> = file (Unix only)</p>
<dd>pid file location </p>
<p> If the argument is empty, then no pid file will be created. </p>
<p> <i>pid</i> path is relative to <i>chroot</i> directory if specified.</p>
<dt><code>RNDbytes</code> = bytes</p>
<dd>bytes to read from random seed files </p>
<p> Number of bytes of data read from random seed files. With <font SIZE="-1">SSL</font> versions less than <code>0.9.5a</code>, also determines how many bytes of data are considered sufficient to seed the <font SIZE="-1">PRNG</font>. More recent <code>OpenSSL</code> versions have a builtin function to determine when sufficient randomness is available.</p>
<dt><code>RNDfile</code> = file</p>
<dd>path to file with random seed data </p>
<p> The <font SIZE="-1">SSL</font> library will use data from this file first to seed the random number generator.</p>
<dt><code>RNDoverwrite</code> = yes | no</p>
<dd>overwrite the random seed files with new random data </p>
<p> default: yes</p>
<dt><code>service</code> = servicename (Unix only)</p>
<dd>use specified string as <i>inetd</i> mode service name for <font SIZE="-1">TCP</font> Wrapper library </p>
<p> default: stunnel</p>
<dt><code>setgid</code> = groupname (Unix only)</p>
<dd><i>setgid()</i> to groupname in daemon mode and clears all other groups</p>
<dt><code>setuid</code> = username (Unix only)</p>
<dd><i>setuid()</i> to username in daemon mode</p>
<dt><code>socket</code> = a|l|r:option=value[:value]</p>
<dd>Set an option on accept/local/remote socket </p>
<p> The values for linger option are l_onof:l_linger. The values for time are tv_sec:tv_usec. </p>
<p> Examples: </p>
<pre> socket = l:SO_LINGER=1:60
 set one minute timeout for closing local socket
 socket = r:SO_OOBINLINE=yes
 place out-of-band data directly into the
 receive data stream for remote sockets
 socket = a:SO_REUSEADDR=no
 disable address reuse (enabled by default)
 socket = a:SO_BINDTODEVICE=lo
 only accept connections on loopback interface</pre>
<dt><code>syslog</code> = yes | no (Unix only)</p>
<dd>enable logging via syslog </p>
<p> default: yes</p>
<dt><code>taskbar</code> = yes | no (<font SIZE="-1">WIN32</font> only)</p>
<dd>enable the taskbar icon </p>
<p> default: yes</dl>
<h3>SERVICE-LEVEL <font SIZE="-1">OPTIONS</font></h3>
<p>Each configuration section begins with service name in square brackets. The service name is used for libwrap (<font SIZE="-1">TCP</font> Wrappers) access control and lets you distinguish <code>stunnel</code> services in your log files. </p>
<p> Note that if you wish to run <code>stunnel</code> in <i>inetd</i> mode (where it is provided a network socket by a server such as <i>inetd</i>, <i>xinetd</i>, or <i>tcpserver</i>) then you should read the section entitled <i></i><font SIZE="-1"><i>INETD</i></font><i> </i><font SIZE="-1"><i>MODE</i></font><i></i> below.</p>
<dl>
<dt><code>accept</code> = address</p>
<dd>accept connections on specified address </p>
<p> If no host specified, defaults to all IPv4 addresses for the local host. </p>
<p> To listen on all IPv6 addresses use: </p>
<pre> accept = :::port</pre>
<dt><code>CApath</code> = directory</p>
<dd>Certificate Authority directory </p>
<p> This is the directory in which <code>stunnel</code> will look for certificates when using the <i>verify</i>. Note that the certificates in this directory should be named <font SIZE="-1">XXXXXXXX</font>.0 where <font SIZE="-1">XXXXXXXX</font> is the hash value of the <font SIZE="-1">DER</font> encoded subject of the cert. </p>
<p> The hash algorithm has been changed in <code>OpenSSL 1.0.0</code>. It is required to c_rehash the directory on upgrade from <code>OpenSSL 0.x.x</code> to <code>OpenSSL 1.x.x</code>. </p>
<p> <i>CApath</i> path is relative to <i>chroot</i> directory if specified.</p>
<dt><code>CAfile</code> = certfile</p>
<dd>Certificate Authority file </p>
<p> This file contains multiple <font SIZE="-1">CA</font> certificates, used with the <i>verify</i>.</p>
<dt><code>cert</code> = pemfile</p>
<dd>certificate chain <font SIZE="-1">PEM</font> file name </p>
<p> A <font SIZE="-1">PEM</font> is always needed in server mode. Specifying this flag in client mode will use this certificate chain as a client side certificate chain. Using client side certs is optional. The certificates must be in <font SIZE="-1">PEM</font> format and must be sorted starting with the certificate to the highest level (root <font SIZE="-1">CA</font>).</p>
<dt><code>ciphers</code> = cipherlist</p>
<dd>Select permitted <font SIZE="-1">SSL</font> ciphers </p>
<p> A colon delimited list of the ciphers to allow in the <font SIZE="-1">SSL</font> connection. For example <font SIZE="-1">DES-CBC3-SHA:IDEA-CBC-MD5</font></p>
<dt><code>client</code> = yes | no</p>
<dd>client mode (remote service uses <font SIZE="-1">SSL</font>) </p>
<p> default: no (server mode)</p>
<dt><code>connect</code> = address</p>
<dd>connect to a remote address </p>
<p> If no host is specified, the host defaults to localhost. </p>
<p> Multiple <code>connect</code> options are allowed in a single service section. </p>
<p> If host resolves to multiple addresses and/or if multiple <i>connect</i> options are specified, then the remote address is chosen using a round-robin algorithm.</p>
<dt><code>CRLpath</code> = directory</p>
<dd>Certificate Revocation Lists directory </p>
<p> This is the directory in which <code>stunnel</code> will look for CRLs when using the <i>verify</i>. Note that the CRLs in this directory should be named <font SIZE="-1">XXXXXXXX</font>.r0 where <font SIZE="-1">XXXXXXXX</font> is the hash value of the <font SIZE="-1">CRL</font>. </p>
<p> The hash algorithm has been changed in <code>OpenSSL 1.0.0</code>. It is required to c_rehash the directory on upgrade from <code>OpenSSL 0.x.x</code> to <code>OpenSSL 1.x.x</code>. </p>
<p> <i>CRLpath</i> path is relative to <i>chroot</i> directory if specified.</p>
<dt><code>CRLfile</code> = certfile</p>
<dd>Certificate Revocation Lists file </p>
<p> This file contains multiple CRLs, used with the <i>verify</i>.</p>
<dt><code>curve</code> = nid</p>
<dd>specify <font SIZE="-1">ECDH</font> curve name for server </p>
<p> To get a list of supported curves use: </p>
<pre> openssl ecparam -list_curves</pre>
<p>default: prime256v1</p>
<dt><code>delay</code> = yes | no</p>
<dd>delay <font SIZE="-1">DNS</font> lookup for &#8216;connect&#8217; option </p>
<p> This option is useful for dynamic <font SIZE="-1">DNS</font>, or when <font SIZE="-1">DNS</font> is not available during <code>stunnel</code> startup (road warrior <font SIZE="-1">VPN</font>, dial-up configurations).</p>
<dt><code>engineNum</code> = engine number</p>
<dd>select engine number to read private key </p>
<p> The engines are numbered starting from 1.</p>
<dt><code>exec</code> = executable_path</p>
<dd>execute local inetd-type program </p>
<p> <i>exec</i> path is relative to <i>chroot</i> directory if specified.</p>
<dt><code>execargs</code> = $0 $1 $2 &#8230;</p>
<dd>arguments for <i>exec</i> including program name ($0) </p>
<p> Quoting is currently not supported. Arguments are separated with arbitrary number of whitespaces.</p>
<dt><code>failover</code> = rr | prio</p>
<dd>Failover strategy for multiple &#8220;connect&#8221; targets. </p>
<pre> rr (round robin) - fair load distribution
 prio (priority) - use the order specified in config file</pre>
<p>default: rr</p>
<dt><code>ident</code> = username</p>
<dd>use <font SIZE="-1">IDENT</font> (<font SIZE="-1">RFC</font> 1413) username checking</p>
<dt><code>key</code> = keyfile</p>
<dd>private key for certificate specified with <i>cert</i> option </p>
<p> Private key is needed to authenticate certificate owner. Since this file should be kept secret it should only be readable to its owner. On Unix systems you can use the following command: </p>
<pre> chmod 600 keyfile</pre>
<p>default: value of <i>cert</i> option</p>
<dt><code>libwrap</code> = yes | no</p>
<dd>Enable or disable the use of /etc/hosts.allow and /etc/hosts.deny. </p>
<p> default: yes</p>
<dt><code>local</code> = host</p>
<dd><font SIZE="-1">IP</font> of the outgoing interface is used as source for remote connections. Use this option to bind a static local <font SIZE="-1">IP</font> address, instead.</p>
<dt><code>sni</code> = service_name:server_name_pattern (server mode)</p>
<dd>Use the service as a slave service (a name-based virtual server) for Server Name Indication <font SIZE="-1">TLS</font> extension (<font SIZE="-1">RFC</font> 3546). </p>
<p> <i>service_name</i> specifies the master service that accepts client connections with <i>accept</i> option. <i>server_name_pattern</i> specifies the host name to be redirected. The pattern may start with &#8216;*&#8217; character, e.g. &#8216;*.example.com&#8217;. Multiple slave services are normally specified for a single master service. <i>sni</i> option can also be specified more than once within a single slave service. </p>
<p> This service, as well as the master service, may not be configured in client mode. </p>
<p> <i>connect</i> option of the slave service is ignored when <i>protocol</i> option is specified, as <i>protocol</i> connects remote host before <font SIZE="-1">TLS</font> handshake. </p>
<p> Libwrap checks (Unix only) are performed twice: with master service name after <font SIZE="-1">TCP</font> connection is accepted, and with slave service name during <font SIZE="-1">TLS</font> handshake. </p>
<p> Option <i>sni</i> is only available when compiled with <code>OpenSSL 1.0.0</code> and later.</p>
<dt><code>sni</code> = server_name (client mode)</p>
<dd>Use the parameter as the value of <font SIZE="-1">TLS</font> Server Name Indication (<font SIZE="-1">RFC</font> 3546) extension. </p>
<p> Option <i>sni</i> is only available when compiled with <code>OpenSSL 1.0.0</code> and later.</p>
<dt><font SIZE="-1"><code>OCSP</code></font> = url</p>
<dd>select <font SIZE="-1">OCSP</font> server for certificate verification</p>
<dt><code>OCSPflag</code> = flag</p>
<dd>specify <font SIZE="-1">OCSP</font> server flag </p>
<p> Several <i>OCSPflag</i> can be used to specify multiple flags. </p>
<p> currently supported flags: <font SIZE="-1">NOCERTS</font>, <font SIZE="-1">NOINTERN</font> <font SIZE="-1">NOSIGS</font>, <font SIZE="-1">NOCHAIN</font>, <font SIZE="-1">NOVERIFY</font>, <font SIZE="-1">NOEXPLICIT</font>, <font SIZE="-1">NOCASIGN</font>, <font SIZE="-1">NODELEGATED</font>, <font SIZE="-1">NOCHECKS</font>, <font SIZE="-1">TRUSTOTHER</font>, <font SIZE="-1">RESPID_KEY</font>, <font SIZE="-1">NOTIME</font></p>
<dt><code>options</code> = SSL_options</p>
<dd><code>OpenSSL</code> library options </p>
<p> The parameter is the <code>OpenSSL</code> option name as described in the <i><a href="//www.systutorials.com/docs/linux/man/3ssl-SSL_CTX_set_options/">SSL_CTX_set_options</a>(3ssl)</i> manual, but without <i></i><font SIZE="-1"><i>SSL_OP_</i></font><i></i> prefix. Several <i>options</i> can be used to specify multiple options. </p>
<p> For example for compatibility with erroneous Eudora <font SIZE="-1">SSL</font> implementation the following option can be used: </p>
<pre> options = DONT_INSERT_EMPTY_FRAGMENTS</pre>
<dt><code>protocol</code> = proto</p>
<dd>application protocol to negotiate <font SIZE="-1">SSL</font> </p>
<p> This option enables initial, protocol-specific negotiation of the <font SIZE="-1">SSL/TLS</font> encryption. <i>protocol</i> option should not be used with <font SIZE="-1">SSL</font> encryption on a separate port. </p>
<p> Currently supported protocols:</p>
<dl>
<dd>
<dl>
<dt><i>cifs</i></p>
<dd>Proprietary (undocummented) extension of <font SIZE="-1">CIFS</font> protocol implemented in Samba. Support for this extension was dropped in Samba 3.0.0.</p>
<dt><i>connect</i></p>
<dd>Based on <font SIZE="-1">RFC</font> 2817 &#8211; <i>Upgrading to </i><font SIZE="-1"><i>TLS</i></font><i> Within </i><font SIZE="-1"><i>HTTP/1</i></font><i>.1</i>, section 5.2 &#8211; <i>Requesting a Tunnel with </i><font SIZE="-1"><i>CONNECT</i></font><i></i> </p>
<p> This protocol is only supported in client mode.</p>
<dt><i>imap</i></p>
<dd>Based on <font SIZE="-1">RFC</font> 2595 &#8211; <i>Using </i><font SIZE="-1"><i>TLS</i></font><i> with </i><font SIZE="-1"><i>IMAP</i></font><i>, </i><font SIZE="-1"><i>POP3</i></font><i> and </i><font SIZE="-1"><i>ACAP</i></font><i></i></p>
<dt><i>nntp</i></p>
<dd>Based on <font SIZE="-1">RFC</font> 4642 &#8211; <i>Using Transport Layer Security (</i><font SIZE="-1"><i>TLS</i></font><i>) with Network News Transfer Protocol (</i><font SIZE="-1"><i>NNTP</i></font><i>)</i> </p>
<p> This protocol is only supported in client mode.</p>
<dt><i>pgsql</i></p>
<dd>Based on <a rel="nofollow" href="http://www.postgresql.org/docs/8.3/static/protocol-flow.html#AEN73982">http://www.postgresql.org/docs/8.3/static/protocol-flow.html#AEN73982</a></p>
<dt><i>pop3</i></p>
<dd>Based on <font SIZE="-1">RFC</font> 2449 &#8211; <i></i><font SIZE="-1"><i>POP3</i></font><i> Extension Mechanism</i></p>
<dt><i>proxy</i></p>
<dd>Haproxy client <font SIZE="-1">IP</font> address <a rel="nofollow" href="http://haproxy.1wt.eu/download/1.5/doc/proxy-protocol.txt">http://haproxy.1wt.eu/download/1.5/doc/proxy-protocol.txt</a></p>
<dt><i>smtp</i></p>
<dd>Based on <font SIZE="-1">RFC</font> 2487 &#8211; <i></i><font SIZE="-1"><i>SMTP</i></font><i> Service Extension for Secure </i><font SIZE="-1"><i>SMTP</i></font><i> over </i><font SIZE="-1"><i>TLS</i></font><i></i></dl>
</dl>
<dl>
<dd></dl>
<dt><code>protocolAuthentication</code> = auth_type</p>
<dd>authentication type for protocol negotiations </p>
<p> currently supported: basic, <font SIZE="-1">NTLM</font> </p>
<p> Currently authentication type only applies to the &#8216;connect&#8217; protocol. </p>
<p> default: basic</p>
<dt><code>protocolHost</code> = host:port</p>
<dd>destination address for protocol negotiations </p>
<p> <i>protocolHost</i> specifies the final <font SIZE="-1">SSL</font> server to be connected by the proxy, and not the proxy server directly connected by <code>stunnel</code>. The proxy server should be specified with the &#8216;connect&#8217; option. </p>
<p> Currently protocol destination address only applies to &#8216;connect&#8217; protocol.</p>
<dt><code>protocolPassword</code> = password</p>
<dd>password for protocol negotiations</p>
<dt><code>protocolUsername</code> = username</p>
<dd>username for protocol negotiations</p>
<dt><code>pty</code> = yes | no (Unix only)</p>
<dd>allocate pseudo terminal for &#8216;exec&#8217; option</p>
<dt><code>renegotiation</code> = yes | no</p>
<dd>support <font SIZE="-1">SSL</font> renegotiation </p>
<p> Applications of the <font SIZE="-1">SSL</font> renegotiation include some authentication scenarios, or re-keying long lasting connections. </p>
<p> On the other hand this feature can facilitate a trivial CPU-exhaustion DoS attack: </p>
<p> <a rel="nofollow" href="http://vincent.bernat.im/en/blog/2011-ssl-dos-mitigation.html">http://vincent.bernat.im/en/blog/2011-ssl-dos-mitigation.html</a> </p>
<p> Please note that disabling <font SIZE="-1">SSL</font> renegotiation does not fully mitigate this issue. </p>
<p> default: yes (if supported by <code>OpenSSL</code>)</p>
<dt><code>reset</code> = yes | no</p>
<dd>attempt to use <font SIZE="-1">TCP</font> <font SIZE="-1">RST</font> flag to indicate an error </p>
<p> This option is not supported on some platforms. </p>
<p> default: yes</p>
<dt><code>retry</code> = yes | no</p>
<dd>reconnect a connect+exec section after it&#8217;s disconnected </p>
<p> default: no</p>
<dt><code>sessionCacheSize</code> = size</p>
<dd>session cache size </p>
<p> <i>sessionCacheSize</i> specifies the maximum number of the internal session cache entries. </p>
<p> The value of 0 can be used for unlimited size. It is not recommended for production use due to the risk of memory exhaustion DoS attack.</p>
<dt><code>sessionCacheTimeout</code> = timeout</p>
<dd>session cache timeout </p>
<p> This is the number of seconds to keep cached <font SIZE="-1">SSL</font> sessions.</p>
<dt><code>sessiond</code> = host:port</p>
<dd>address of sessiond <font SIZE="-1">SSL</font> cache server</p>
<dt><code>sslVersion</code> = version</p>
<dd>select version of <font SIZE="-1">SSL</font> protocol </p>
<p> Allowed options: all, SSLv2, SSLv3, TLSv1, TLSv1.1, TLSv1.2</p>
<dt><code>stack</code> = bytes (except for <font SIZE="-1">FORK</font> model)</p>
<dd>thread stack size</p>
<dt><code>TIMEOUTbusy</code> = seconds</p>
<dd>time to wait for expected data</p>
<dt><code>TIMEOUTclose</code> = seconds</p>
<dd>time to wait for close_notify (set to 0 for buggy <font SIZE="-1">MSIE</font>)</p>
<dt><code>TIMEOUTconnect</code> = seconds</p>
<dd>time to wait to connect a remote host</p>
<dt><code>TIMEOUTidle</code> = seconds</p>
<dd>time to keep an idle connection</p>
<dt><code>transparent</code> = none | source | destination | both (Unix only)</p>
<dd>enable transparent proxy support on selected platforms </p>
<p> Supported values:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>Disable transparent proxy support. This is the default.</p>
<dt><i>source</i></p>
<dd>Re-write address to appear as if wrapped daemon is connecting from the <font SIZE="-1">SSL</font> client machine instead of the machine running <code>stunnel</code>. </p>
<p> This option is currently available in:</p>
<dl>
<dd>
<dl>
<dt>Remote mode (<i>connect</i> option) on <i>Linux &gt;=2.6.28</i></p>
<dd>This configuration requires <code>stunnel</code> to be executed as root and without <i>setuid</i> option. </p>
<p> This configuration requires the following setup for iptables and routing (possibly in /etc/rc.local or equivalent file): </p>
<pre> iptables -t mangle -N DIVERT
 iptables -t mangle -A PREROUTING -p tcp -m socket -j DIVERT
 iptables -t mangle -A DIVERT -j MARK --set-mark 1
 iptables -t mangle -A DIVERT -j ACCEPT
 ip rule add fwmark 1 lookup 100
 ip route add local 0.0.0.0/0 dev lo table 100
 echo 0 &gt;/proc/sys/net/ipv4/conf/lo/rp_filter</pre>
<p><code>stunnel</code> must also to be executed as root and without <i>setuid</i> option.</p>
<dt>Remote mode (<i>connect</i> option) on <i>Linux 2.2.x</i></p>
<dd>This configuration requires kernel to be compiled with <i>transparent proxy</i> option. Connected service must be installed on a separate host. Routing towards the clients has to go through the <code>stunnel</code> box. </p>
<p> <code>stunnel</code> must also to be executed as root and without <i>setuid</i> option.</p>
<dt>Remote mode (<i>connect</i> option) on <i>FreeBSD &gt;=8.0</i></p>
<dd>This configuration requires additional firewall and routing setup. <code>stunnel</code> must also to be executed as root and without <i>setuid</i> option.</p>
<dt>Local mode (<i>exec</i> option)</p>
<dd>This configuration works by pre-loading <i>libstunnel.so</i> shared library. _RLD_LIST environment variable is used on Tru64, and <font SIZE="-1">LD_PRELOAD</font> variable on other platforms.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>destination</i></p>
<dd>Original destination is used instead of <i>connect</i> option. </p>
<p> A service section for transparent destination may look like this: </p>
<pre> [transparent]
 client=yes
 accept=&lt;stunnel_port&gt;
 transparent=destination</pre>
<p>This configuration requires the following setup for iptables (possibly in /etc/rc.local or equivalent file): </p>
<pre> /sbin/iptables -I INPUT -i eth0 -p tcp --dport &lt;stunnel_port&gt; -j ACCEPT
 /sbin/iptables -t nat -I PREROUTING -i eth0 -p tcp --dport &lt;redirected_port&gt; -j DNAT --to-destination &lt;local_ip&gt;:&lt;stunnel_port&gt;</pre>
<p>Transparent destination option is currently only supported on Linux.</p>
<dt><i>both</i></p>
<dd>Use both <i>source</i> and <i>destination</i> transparent proxy.</dl>
</dl>
<dl>
<dd>Two legacy options are also supported for backward compatibility:</p>
<dl>
<dt><i>yes</i></p>
<dd>This options has been renamed to <i>source</i>.</p>
<dt><i>no</i></p>
<dd>This options has been renamed to <i>none</i>.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>verify</code> = level</p>
<dd>verify peer certificate</p>
<dl>
<dd>
<dl>
<dt>level 0</p>
<dd>Request and ignore peer certificate.</p>
<dt>level 1</p>
<dd>Verify peer certificate if present.</p>
<dt>level 2</p>
<dd>Verify peer certificate.</p>
<dt>level 3</p>
<dd>Verify peer with locally installed certificate.</p>
<dt>level 4</p>
<dd>Ignore <font SIZE="-1">CA</font> chain and only verify peer certificate.</p>
<dt>default</p>
<dd>No verify.</dl>
</dl>
<dl>
<dd>It is important to understand, that this option was solely designed for access control and not for authorization. Specifically for level 2 every non-revoked certificate is accepted regardless of its Common Name. For this reason a dedicated <font SIZE="-1">CA</font> should be used with level 2, and not a generic <font SIZE="-1">CA</font> commonly used for webservers. Level 3 is preferred for point-to-point connections.</dl>
</dl>
<h2>Return Value</h2>
<p><code>stunnel</code> returns zero on success, non-zero on error.</p>
<h2>Signals</h2>
<p>The following signals can be used to control <code>stunnel</code> in Unix environment:</p>
<dl>
<dt><font SIZE="-1">SIGHUP</font></p>
<dd>Force a reload of the configuration file. </p>
<p> Some global options will not be reloaded:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>chroot</p>
<dt>&bull;</p>
<dd>foreground</p>
<dt>&bull;</p>
<dd>pid</p>
<dt>&bull;</p>
<dd>setgid</p>
<dt>&bull;</p>
<dd>setuid</dl>
</dl>
<dl>
<dd>The use of &#8216;setuid&#8217; option will also prevent <code>stunnel</code> from binding privileged (&lt;1024) ports during configuration reloading. </p>
<p> When &#8216;chroot&#8217; option is used, <code>stunnel</code> will look for all its files (including configuration file, certificates, log file and pid file) within the chroot jail.</dl>
<dt><font SIZE="-1">SIGUSR1</font></p>
<dd>Close and reopen <code>stunnel</code> log file. This function can be used for log rotation.</p>
<dt><font SIZE="-1">SIGTERM</font>, <font SIZE="-1">SIGQUIT</font>, <font SIZE="-1">SIGINT</font></p>
<dd>Shut <code>stunnel</code> down.</dl>
<p> The result of sending any other signals to the server is undefined.</p>
<h2>Examples</h2>
<p>In order to provide <font SIZE="-1">SSL</font> encapsulation to your local <i>imapd</i> service, use </p>
<pre> [imapd]
 accept = 993
 exec = /usr/sbin/imapd
 execargs = imapd</pre>
<p>If you want to provide tunneling to your <i>pppd</i> daemon on port 2020, use something like </p>
<pre> [vpn]
 accept = 2020
 exec = /usr/sbin/pppd
 execargs = pppd local
 pty = yes</pre>
<p>If you want to use <code>stunnel</code> in <i>inetd</i> mode to launch your imapd process, you&#8217;d use this <i>stunnel.conf</i>. Note there must be no <i>[service_name]</i> section. </p>
<pre> exec = /usr/sbin/imapd
 execargs = imapd</pre>
<h2>Notes</h2>
<h3><font SIZE="-1">RESTRICTIONS</font></h3>
<p><code>stunnel</code> cannot be used for the <font SIZE="-1">FTP</font> daemon because of the nature of the <font SIZE="-1">FTP</font> protocol which utilizes multiple ports for data transfers. There are available <font SIZE="-1">SSL</font> enabled versions of <font SIZE="-1">FTP</font> and telnet daemons, however.</p>
<h3><font SIZE="-1">INETD</font> <font SIZE="-1">MODE</font></h3>
<p>The most common use of <code>stunnel</code> is to listen on a network port and establish communication with either a new port via the connect option, or a new program via the <i>exec</i> option. However there is a special case when you wish to have some other program accept incoming connections and launch <code>stunnel</code>, for example with <i>inetd</i>, <i>xinetd</i>, or <i>tcpserver</i>. </p>
<p> For example, if you have the following line in <i>inetd.conf</i>: </p>
<pre> imaps stream tcp nowait root /usr/bin/stunnel stunnel /etc/stunnel/imaps.conf</pre>
<p>In these cases, the <i>inetd</i>-style program is responsible for binding a network socket (<i>imaps</i> above) and handing it to <code>stunnel</code> when a connection is received. Thus you do not want <code>stunnel</code> to have any <i>accept</i> option. All the <i>Service Level Options</i> should be placed in the global options section, and no <i>[service_name]</i> section will be present. See the <i></i><font SIZE="-1"><i>EXAMPLES</i></font><i></i> section for example configurations.</p>
<h3><font SIZE="-1">CERTIFICATES</font></h3>
<p>Each <font SIZE="-1">SSL</font> enabled daemon needs to present a valid X.509 certificate to the peer. It also needs a private key to decrypt the incoming data. The easiest way to obtain a certificate and a key is to generate them with the free <code>OpenSSL</code> package. You can find more information on certificates generation on pages listed below. </p>
<p> The order of contents of the <i>.pem</i> file is important. It should contain the unencrypted private key first, then a signed certificate (not certificate request). There should be also empty lines after certificate and private key. Plaintext certificate information appended on the top of generated certificate should be discarded. So the file should look like this: </p>
<pre> -----BEGIN RSA PRIVATE KEY-----
 [encoded key]
 -----END RSA PRIVATE KEY-----
 [empty line]
 -----BEGIN CERTIFICATE-----
 [encoded certificate]
 -----END CERTIFICATE-----
 [empty line]</pre>
<h3><font SIZE="-1">RANDOMNESS</font></h3>
<p><code>stunnel</code> needs to seed the <font SIZE="-1">PRNG</font> (pseudo random number generator) in order for <font SIZE="-1">SSL</font> to use good randomness. The following sources are loaded in order until sufficient random data has been gathered:</p>
<dl>
<dt>&bull;</p>
<dd>The file specified with the <i>RNDfile</i> flag.</p>
<dt>&bull;</p>
<dd>The file specified by the <font SIZE="-1">RANDFILE</font> environment variable, if set.</p>
<dt>&bull;</p>
<dd>The file .rnd in your home directory, if <font SIZE="-1">RANDFILE</font> not set.</p>
<dt>&bull;</p>
<dd>The file specified with &#8216;&#8211;with-random&#8217; at compile time.</p>
<dt>&bull;</p>
<dd>The contents of the screen if running on Windows.</p>
<dt>&bull;</p>
<dd>The egd socket specified with the <i></i><font SIZE="-1"><i>EGD</i></font><i></i> flag.</p>
<dt>&bull;</p>
<dd>The egd socket specified with &#8216;&#8211;with-egd-sock&#8217; at compile time.</p>
<dt>&bull;</p>
<dd>The /dev/urandom device.</dl>
<p> With recent (<code>OpenSSL 0.9.5a</code> or later) version of <font SIZE="-1">SSL</font> it will stop loading random data automatically when sufficient entropy has been gathered. With previous versions it will continue to gather from all the above sources since no <font SIZE="-1">SSL</font> function exists to tell when enough data is available. </p>
<p> Note that on Windows machines that do not have console user interaction (mouse movements, creating windows, etc.) the screen contents are not variable enough to be sufficient, and you should provide a random file for use with the <i>RNDfile</i> flag. </p>
<p> Note that the file specified with the <i>RNDfile</i> flag should contain random data &#8212; that means it should contain different information each time <code>stunnel</code> is run. This is handled automatically unless the <i>RNDoverwrite</i> flag is used. If you wish to update this file manually, the <i>openssl rand</i> command in recent versions of <code>OpenSSL</code>, would be useful. </p>
<p> Important note: If /dev/urandom is available, <code>OpenSSL</code> often seeds the <font SIZE="-1">PRNG</font> with it while checking the random state. On systems with /dev/urandom <code>OpenSSL</code> is likely to use it even though it is listed at the very bottom of the list above. This is the behaviour of <code>OpenSSL</code> and not <code>stunnel</code>.</p>
<h3><font SIZE="-1">DH</font> <font SIZE="-1">PARAMETERS</font></h3>
<p>Stunnel 4.40 and later contains hardcoded 2048-bit <font SIZE="-1">DH</font> parameters. </p>
<p> It is also possible to specify <font SIZE="-1">DH</font> parameters in the certificate file: </p>
<pre> openssl dhparam 2048 &gt;&gt; stunnel.pem</pre>
<p><font SIZE="-1">DH</font> parameter generation may take several minutes.</p>
<h2>Files</h2>
<dl>
<dt><i>stunnel.conf</i></p>
<dd><code>stunnel</code> configuration file</dl>
<h2>Bugs</h2>
<p>Option <i>execargs</i> and Win32 command line does not support quoting.</p>
<h2>See Also</h2>
<dl>
<dt><i><a href="/docs/linux/man/8-tcpd/">tcpd</a></i>(8)</p>
<dd>access control facility for internet services</p>
<dt><i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8)</p>
<dd>internet &#8216;super-server&#8217;</p>
<dt><i><a rel="nofollow" href="http://www.stunnel.org/">http://www.stunnel.org/</a></i></p>
<dd><code>stunnel</code> homepage</p>
<dt><i><a rel="nofollow" href="http://www.openssl.org/">http://www.openssl.org/</a></i></p>
<dd><code>OpenSSL</code> project website</dl>
<h2>Author</h2>
<dl>
<dt>Michał Trojnara</p>
<dd>&lt;<i>Michal.Trojnara [at] mirt.net</i>&gt; </p>
</dl>
