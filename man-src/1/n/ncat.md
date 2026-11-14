---
title: "ncat(1)"
name: "ncat"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncat/"
description: "ncat – Concatenate and redirect sockets"
---

<h2 class="name">NAME</h2>
<p> ncat &#8211; Concatenate and redirect sockets </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ncat</code> [<i>OPTIONS</i>&#8230;] [<i>hostname</i>] [<i>port</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>Ncat is a feature-packed networking utility which reads and writes data across networks from the command line. Ncat was written for the Nmap Project and is the culmination of the currently splintered family of Netcat incarnations. It is designed to be a reliable back-end tool to instantly provide network connectivity to other applications and users. Ncat will not only work with IPv4 and IPv6 but provides the user with a virtually limitless number of potential uses. </p>
<p> Among Ncat&#8217;s vast number of features there is the ability to chain Ncats together; redirection of TCP, UDP, and SCTP ports to other sites; SSL support; and proxy connections via SOCKS4 or HTTP proxies (with optional proxy authentication as well). Some general principles apply to most applications and thus give you the capability of instantly adding networking support to software that would normally never support it.</p>
<h2>OPTIONS SUMMARY</h2>
<dl>
<dt>
<dd>
<pre><code>
Ncat 7.60 ( https://nmap.org/ncat )
Usage: ncat [options] [hostname] [port]
Options taking a time assume seconds. Append 'ms' for milliseconds,
's' for seconds, 'm' for minutes, or 'h' for hours (e.g. 500ms).
  -4                         Use IPv4 only
  -6                         Use IPv6 only
  -U, --unixsock             Use Unix domain sockets only
  -C, --crlf                 Use CRLF for EOL sequence
  -c, --sh-exec &lt;command&gt;    Executes the given command via /bin/sh
  -e, --exec &lt;command&gt;       Executes the given command
      --lua-exec &lt;filename&gt;  Executes the given Lua script
  -g hop1[,hop2,...]         Loose source routing hop points (8 max)
  -G &lt;n&gt;                     Loose source routing hop pointer (4, 8, 12, ...)
  -m, --max-conns &lt;n&gt;        Maximum &lt;n&gt; simultaneous connections
  -h, --help                 Display this help screen
  -d, --delay &lt;time&gt;         Wait between read/writes
  -o, --output &lt;filename&gt;    Dump session data to a file
  -x, --hex-dump &lt;filename&gt;  Dump session data as hex to a file
  -i, --idle-timeout &lt;time&gt;  Idle read/write timeout
  -p, --source-port port     Specify source port to use
  -s, --source addr          Specify source address to use (doesn't affect -l)
  -l, --listen               Bind and listen for incoming connections
  -k, --keep-open            Accept multiple connections in listen mode
  -n, --nodns                Do not resolve hostnames via DNS
  -t, --telnet               Answer Telnet negotiations
  -u, --udp                  Use UDP instead of default TCP
      --sctp                 Use SCTP instead of default TCP
  -v, --verbose              Set verbosity level (can be used several times)
  -w, --wait &lt;time&gt;          Connect timeout
  -z                         Zero-I/O mode, report connection status only
      --append-output        Append rather than clobber specified output files
      --send-only            Only send data, ignoring received; quit on EOF
      --recv-only            Only receive data, never send anything
      --allow                Allow only given hosts to connect to Ncat
      --allowfile            A file of hosts allowed to connect to Ncat
      --deny                 Deny given hosts from connecting to Ncat
      --denyfile             A file of hosts denied from connecting to Ncat
      --broker               Enable Ncat's connection brokering mode
      --chat                 Start a simple Ncat chat server
      --proxy &lt;addr[:port]&gt;  Specify address of host to proxy through
      --proxy-type &lt;type&gt;    Specify proxy type ("http" or "socks4" or "socks5")
      --proxy-auth &lt;auth&gt;    Authenticate with HTTP or SOCKS proxy server
      --ssl                  Connect or listen with SSL
      --ssl-cert             Specify SSL certificate file (PEM) for listening
      --ssl-key              Specify SSL private key (PEM) for listening
      --ssl-verify           Verify trust and domain name of certificates
      --ssl-trustfile        PEM file containing trusted SSL certificates
      --ssl-ciphers          Cipherlist containing SSL ciphers to use
      --ssl-alpn             ALPN protocol list to use.
      --version              Display Ncat's version information and exit
See the ncat(1) manpage for full options, descriptions and usage examples
</code></pre>
</dl>
<h2>CONNECT MODE AND LISTEN MODE</h2>
<p> Ncat operates in one of two primary modes: connect mode and listen mode. Other modes, such as the HTTP proxy server, act as special cases of these two. In connect mode, Ncat works as a client. In listen mode it is a server. </p>
<p> In connect mode, the <i>hostname</i> and <i>port</i> arguments tell what to connect to. <i>hostname</i> is required, and may be a hostname or IP address. If <i>port</i> is supplied, it must be a decimal port number. If omitted, it defaults to 31337. </p>
<p> In listen mode, <i>hostname</i> and <i>port</i> control the address the server will bind to. Both arguments are optional in listen mode. If <i>hostname</i> is omitted, it defaults to listening on all available addresses over IPv4 and IPv6. If <i>port</i> is omitted, it defaults to 31337.</p>
<h2>PROTOCOL OPTIONS</h2>
<p> <code>-4</code> (IPv4 only)</p>
<dl>
<dt>
<dd> Force the use of IPv4 only.</dl>
<p> <code>-6</code> (IPv6 only)</p>
<dl>
<dt>
<dd> Force the use of IPv6 only.</dl>
<p> <code>-U</code>, <code>&#8211;unixsock</code> (Use Unix domain sockets)</p>
<dl>
<dt>
<dd> Use Unix domain sockets rather than network sockets. This option may be used on its own for stream sockets, or combined with <code>&#8211;udp</code> for datagram sockets. A description of <code>-U</code> mode is in the section called &#8220;UNIX DOMAIN SOCKETS&#8221;.</dl>
<p> <code>-u</code>, <code>&#8211;udp</code> (Use UDP)</p>
<dl>
<dt>
<dd> Use UDP for the connection (the default is TCP).</dl>
<p> <code>&#8211;sctp</code> (Use SCTP)</p>
<dl>
<dt>
<dd> Use SCTP for the connection (the default is TCP). SCTP support is implemented in TCP-compatible mode.</dl>
<h2>CONNECT MODE OPTIONS</h2>
<p> <code>-g </code><i>hop1</i><code>[,</code><i>hop2</i>,&#8230;] (Loose source routing)</p>
<dl>
<dt>
<dd> Sets hops for IPv4 loose source routing. You can use <code>-g</code> once with a comma-separated list of hops, use <code>-g</code> multiple times with single hops to build the list, or combine the two. Hops can be given as IP addresses or hostnames.</dl>
<p> <code>-G </code><i>ptr</i> (Set source routing pointer)</p>
<dl>
<dt>
<dd> Sets the IPv4 source route &#8220;pointer&#8221; for use with <code>-g</code>. The argument must be a multiple of 4 and no more than 28. Not all operating systems support setting this pointer to anything other than four.</dl>
<p> <code>-p </code><i>port</i>, <code>&#8211;source-port </code><i>port</i> (Specify source port)</p>
<dl>
<dt>
<dd> Set the port number for Ncat to bind to.</dl>
<p> <code>-s </code><i>host</i>, <code>&#8211;source </code><i>host</i> (Specify source address)</p>
<dl>
<dt>
<dd> Set the address for Ncat to bind to.</dl>
<h2>LISTEN MODE OPTIONS</h2>
<p> See the section called &#8220;ACCESS CONTROL OPTIONS&#8221; for information on limiting the hosts that may connect to the listening Ncat process. </p>
<p> <code>-l</code>, <code>&#8211;listen</code> (Listen for connections)</p>
<dl>
<dt>
<dd> Listen for connections rather than connecting to a remote machine</dl>
<p> <code>-m </code><i>numconns</i>, <code>&#8211;max-conns </code><i>numconns</i> (Specify maximum number of connections)</p>
<dl>
<dt>
<dd> The maximum number of simultaneous connections accepted by an Ncat instance. 100 is the default (60 on Windows).</dl>
<p> <code>-k</code>, <code>&#8211;keep-open</code> (Accept multiple connections)</p>
<dl>
<dt>
<dd> Normally a listening server accepts only one connection and then quits when the connection is closed. This option makes it accept multiple simultaneous connections and wait for more connections after they have all been closed. It must be combined with <code>&#8211;listen</code>. In this mode there is no way for Ncat to know when its network input is finished, so it will keep running until interrupted. This also means that it will never close its output stream, so any program reading from Ncat and looking for end-of-file will also hang.</dl>
<p> <code>&#8211;broker</code> (Connection brokering)</p>
<dl>
<dt>
<dd> Allow multiple parties to connect to a centralised Ncat server and communicate with each other. Ncat can broker communication between systems that are behind a NAT or otherwise unable to directly connect. This option is used in conjunction with <code>&#8211;listen</code>, which causes the <code>&#8211;listen</code> port to have broker mode enabled.</dl>
<p> <code>&#8211;chat</code> (Ad-hoc &#8220;chat server&#8221;)</p>
<dl>
<dt>
<dd> The <code>&#8211;chat</code> option enables chat mode, intended for the exchange of text between several users. In chat mode, connection brokering is turned on. Ncat prefixes each message received with an ID before relaying it to the other connections. The ID is unique for each connected client. This helps distinguish who sent what. Additionally, non-printing characters such as control characters are escaped to keep them from doing damage to a terminal.</dl>
<h2>SSL OPTIONS</h2>
<p> <code>&#8211;ssl</code> (Use SSL)</p>
<dl>
<dt>
<dd> In connect mode, this option transparently negotiates an SSL session with an SSL server to securely encrypt the connection. This is particularly handy for talking to SSL enabled HTTP servers, etc. </p>
<p> In server mode, this option listens for incoming SSL connections, rather than plain untunneled traffic. </p>
<p> In UDP connect mode, this option enables Datagram TLS (DTLS). This is not supported in server mode.</dl>
<p> <code>&#8211;ssl-verify</code> (Verify server certificates)</p>
<dl>
<dt>
<dd> In client mode, <code>&#8211;ssl-verify</code> is like <code>&#8211;ssl</code> except that it also requires verification of the server certificate. Ncat comes with a default set of trusted certificates in the file ca-bundle.crt. Some operating systems provide a default list of trusted certificates; these will also be used if available. Use <code>&#8211;ssl-trustfile</code> to give a custom list. Use <code>-v</code> one or more times to get details about verification failures. Ncat does not check for revoked certificates. </p>
<p> This option has no effect in server mode.</dl>
<p> <code>&#8211;ssl-cert </code><i>certfile.pem</i> (Specify SSL certificate)</p>
<dl>
<dt>
<dd> This option gives the location of a PEM-encoded certificate files used to authenticate the server (in listen mode) or the client (in connect mode). Use it in combination with <code>&#8211;ssl-key</code>.</dl>
<p> <code>&#8211;ssl-key </code><i>keyfile.pem</i> (Specify SSL private key)</p>
<dl>
<dt>
<dd> This option gives the location of the PEM-encoded private key file that goes with the certificate named with <code>&#8211;ssl-cert</code>.</dl>
<p> <code>&#8211;ssl-trustfile </code><i>cert.pem</i> (List trusted certificates)</p>
<dl>
<dt>
<dd> This option sets a list of certificates that are trusted for purposes of certificate verification. It has no effect unless combined with <code>&#8211;ssl-verify</code>. The argument to this option is the name of a PEM file containing trusted certificates. Typically, the file will contain certificates of certification authorities, though it may also contain server certificates directly. When this option is used, Ncat does not use its default certificates.</dl>
<p> <code>&#8211;ssl-ciphers </code><i>cipherlist</i> (Specify SSL ciphersuites)</p>
<dl>
<dt>
<dd> This option sets the list of ciphersuites that Ncat will use when connecting to servers or when accepting SSL connections from clients. The syntax is described in the OpenSSL <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1) man page, and defaults to ALL:!aNULL:!eNULL:!LOW:!EXP:!MD5:@STRENGTH</dl>
<p> <code>&#8211;ssl-alpn </code><i>ALPN list</i> (Specify ALPN protocol list)</p>
<dl>
<dt>
<dd> This option allows you to specify a comma-separated list of protocols to send via the Application-Layer Protocol Negotiation (ALPN) TLS extension. Not supported by all versions of OpenSSL.</dl>
<h2>PROXY OPTIONS</h2>
<p> <code>&#8211;proxy </code><i>host</i><code>[:</code><i>port</i><code>]</code> (Specify proxy address)</p>
<dl>
<dt>
<dd> Requests proxying through <i>host</i>:<i>port</i>, using the protocol specified by <code>&#8211;proxy-type</code>. </p>
<p> If no port is specified, the proxy protocol&#8217;s well-known port is used (1080 for SOCKS and 3128 for HTTP). However, when specifying an IPv6 HTTP proxy server using the IP address rather than the hostname, the port number MUST be specified as well. If the proxy requires authentication, use <code>&#8211;proxy-auth</code>.</dl>
<p> <code>&#8211;proxy-type </code><i>proto</i> (Specify proxy protocol)</p>
<dl>
<dt>
<dd> In connect mode, this option requests the protocol <i>proto</i> to connect through the proxy host specified by <code>&#8211;proxy</code>. In listen mode, this option has Ncat act as a proxy server using the specified protocol. </p>
<p> The currently available protocols in connect mode are http (CONNECT) and socks4 (SOCKSv4). The only server currently supported is http. If this option is not used, the default protocol is http.</dl>
<p> <code>&#8211;proxy-auth </code><i>user</i><code>[:</code><i>pass</i>] (Specify proxy credentials)</p>
<dl>
<dt>
<dd> In connect mode, gives the credentials that will be used to connect to the proxy server. In listen mode, gives the credentials that will be required of connecting clients. For use with <code>&#8211;proxy-type http</code>, the form should be user:pass. For <code>&#8211;proxy-type socks4</code>, it should be a username only.</dl>
<h2>COMMAND EXECUTION OPTIONS</h2>
<p> <code>-e </code><i>command</i>, <code>&#8211;exec </code><i>command</i> (Execute command)</p>
<dl>
<dt>
<dd> Execute the specified command after a connection has been established. The command must be specified as a full pathname. All input from the remote client will be sent to the application and responses sent back to the remote client over the socket, thus making your command-line application interactive over a socket. Combined with <code>&#8211;keep-open</code>, Ncat will handle multiple simultaneous connections to your specified port/application like inetd. Ncat will only accept a maximum, definable, number of simultaneous connections controlled by the <code>-m</code> option. By default this is set to 100 (60 on Windows).</dl>
<p> <code>-c </code><i>command</i>, <code>&#8211;sh-exec </code><i>command</i> (Execute command via sh)</p>
<dl>
<dt>
<dd> Same as <code>-e</code>, except it tries to execute the command via /bin/sh. This means you don&#8217;t have to specify the full path for the command, and shell facilities like environment variables are available.</dl>
<p> <code>&#8211;lua-exec </code><i>file</i> (Execute a .lua script)</p>
<dl>
<dt>
<dd> Runs the specified file as a Lua script after a connection has been established, using a built-in interpreter. Both the script&#8217;s standard input and the standard output are redirected to the connection data streams.</dl>
<p> All exec options add the following variables to the child&#8217;s environment: </p>
<p> <code>NCAT_REMOTE_ADDR</code>, <code>NCAT_REMOTE_PORT</code></p>
<dl>
<dt>
<dd> The IP address and port number of the remote host. In connect mode, it&#8217;s the target&#8217;s address; in listen mode, it&#8217;s the client&#8217;s address.</dl>
<p> <code>NCAT_LOCAL_ADDR</code>, <code>NCAT_LOCAL_PORT</code></p>
<dl>
<dt>
<dd> The IP address and port number of the local end of the connection.</dl>
<p> <code>NCAT_PROTO</code></p>
<dl>
<dt>
<dd> The protocol in use: one of TCP, UDP, and SCTP.</dl>
<h2>ACCESS CONTROL OPTIONS</h2>
<p> <code>&#8211;allow </code><i>host</i><code>[,</code><i>host</i>,&#8230;] (Allow connections)</p>
<dl>
<dt>
<dd> The list of hosts specified will be the only hosts allowed to connect to the Ncat process. All other connection attempts will be disconnected. In case of a conflict between <code>&#8211;allow</code> and <code>&#8211;deny</code>, <code>&#8211;allow</code> takes precedence. Host specifications follow the same syntax used by Nmap.</dl>
<p> <code>&#8211;allowfile </code><i>file</i> (Allow connections from file)</p>
<dl>
<dt>
<dd> This has the same functionality as <code>&#8211;allow</code>, except that the allowed hosts are provided in a new-line delimited allow file, rather than directly on the command line.</dl>
<p> <code>&#8211;deny </code><i>host</i><code>[,</code><i>host</i>,&#8230;] (Deny connections)</p>
<dl>
<dt>
<dd> Issue Ncat with a list of hosts that will not be allowed to connect to the listening Ncat process. Specified hosts will have their session silently terminated if they try to connect. In case of a conflict between <code>&#8211;allow</code> and <code>&#8211;deny</code>, <code>&#8211;allow</code> takes precedence. Host specifications follow the same syntax used by Nmap.</dl>
<p> <code>&#8211;denyfile </code><i>file</i> (Deny connections from file)</p>
<dl>
<dt>
<dd> This is the same functionality as <code>&#8211;deny</code>, except that excluded hosts are provided in a new-line delimited deny file, rather than directly on the command line.</dl>
<h2>TIMING OPTIONS</h2>
<p> These options accept a time parameter. This is specified in seconds by default, though you can append ms, s, m, or h to the value to specify milliseconds, seconds, minutes, or hours. </p>
<p> <code>-d </code><i>time</i>, <code>&#8211;delay </code><i>time</i> (Specify line delay)</p>
<dl>
<dt>
<dd> Set the delay interval for lines sent. This effectively limits the number of lines that Ncat will send in the specified period. This may be useful for low-bandwidth sites, or have other uses such as coping with annoying <code>iptables &#8211;limit</code> options.</dl>
<p> <code>-i </code><i>time</i>, <code>&#8211;idle-timeout </code><i>time</i> (Specify idle timeout)</p>
<dl>
<dt>
<dd> Set a fixed timeout for idle connections. If the idle timeout is reached, the connection is terminated.</dl>
<p> <code>-w </code><i>time</i>, <code>&#8211;wait </code><i>time</i> (Specify connect timeout)</p>
<dl>
<dt>
<dd> Set a fixed timeout for connection attempts.</dl>
<h2>OUTPUT OPTIONS</h2>
<p> <code>-o </code><i>file</i>, <code>&#8211;output </code><i>file</i> (Save session data)</p>
<dl>
<dt>
<dd> Dump session data to a file</dl>
<p> <code>-x </code><i>file</i>, <code>&#8211;hex-dump </code><i>file</i> (Save session data in hex)</p>
<dl>
<dt>
<dd> Dump session data in hex to a file.</dl>
<p> <code>&#8211;append-output</code> (Append output)</p>
<dl>
<dt>
<dd> Issue Ncat with <code>&#8211;append-ouput</code> along with <code>-o</code> and/or <code>-x</code> and it will append the resulted output rather than truncating the specified output files.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code> (Be verbose)</p>
<dl>
<dt>
<dd> Issue Ncat with <code>-v</code> and it will be verbose and display all kinds of useful connection based information. Use more than once (<code>-vv</code>, <code>-vvv</code>&#8230;) for greater verbosity.</dl>
<h2>MISC OPTIONS</h2>
<p> <code>-C</code>, <code>&#8211;crlf</code> (Use CRLF as EOL)</p>
<dl>
<dt>
<dd> This option tells Ncat to convert LF line endings to CRLF when taking input from standard input. This is useful for talking to some stringent servers directly from a terminal in one of the many common plain-text protocols that use CRLF for end-of-line.</dl>
<p> <code>-h</code>, <code>&#8211;help</code> (Help screen)</p>
<dl>
<dt>
<dd> Displays a short help screen with common options and parameters, and then exits.</dl>
<p> <code>&#8211;recv-only</code> (Only receive data)</p>
<dl>
<dt>
<dd> If this option is passed, Ncat will only receive data and will not try to send anything.</dl>
<p> <code>&#8211;send-only</code> (Only send data)</p>
<dl>
<dt>
<dd> If this option is passed, then Ncat will only send data and will ignore anything received. This option also causes Ncat to close the network connection and terminate after EOF is received on standard input.</dl>
<p> <code>&#8211;no-shutdown</code> (Do not shutdown into half-duplex mode)</p>
<dl>
<dt>
<dd> If this option is passed, Ncat will not invoke shutdown on a socket aftering seeing EOF on stdin. This is provided for backward-compatibility with OpenBSD netcat, which exhibits this behavior when executed with its &#8216;-d&#8217; option.</dl>
<p> <code>-t</code>, <code>&#8211;telnet</code> (Answer Telnet negotiations)</p>
<dl>
<dt>
<dd> Handle DO/DONT WILL/WONT Telnet negotiations. This makes it possible to script Telnet sessions with Ncat.</dl>
<p> <code>&#8211;version</code> (Display version)</p>
<dl>
<dt>
<dd> Displays the Ncat version number and exits.</dl>
<h2>UNIX DOMAIN SOCKETS</h2>
<p> The <code>-U</code> option (same as <code>&#8211;unixsock</code>) causes Ncat to use Unix domain sockets rather than network sockets. Unix domain sockets exist as an entry in the filesystem. You must give the name of a socket to connect to or to listen on. For example, to make a connection, </p>
<p> <code>ncat -U ~/unixsock</code> </p>
<p> To listen on a socket: </p>
<p> <code>ncat -l -U ~/unixsock</code> </p>
<p> Listen mode will create the socket if it doesn&#8217;t exist. The socket will continue to exist after the program ends. </p>
<p> Both stream and datagram domain sockets are supported. Use <code>-U</code> on its own for stream sockets, or combine it with <code>&#8211;udp</code> for datagram sockets. Datagram sockets require a source socket to connect from. By default, a source socket with a random filename will be created as needed, and deleted when the program ends. Use the <code>&#8211;source</code> with a path to use a source socket with a specific name.</p>
<h2>EXAMPLES</h2>
<p> Connect to example.org on TCP port 8080.</p>
<dl>
<dt>
<dd> <code>ncat example.org 8080</code></dl>
<p> Listen for connections on TCP port 8080.</p>
<dl>
<dt>
<dd> <code>ncat -l 8080</code></dl>
<p> Redirect TCP port 8080 on the local machine to host on port 80.</p>
<dl>
<dt>
<dd> <code>ncat &#8211;sh-exec &quot;ncat example.org 80&quot; -l 8080 &#8211;keep-open</code></dl>
<p> Bind to TCP port 8081 and attach /bin/bash for the world to access freely.</p>
<dl>
<dt>
<dd> <code>ncat &#8211;exec &quot;/bin/bash&quot; -l 8081 &#8211;keep-open</code></dl>
<p> Bind a shell to TCP port 8081, limit access to hosts on a local network, and limit the maximum number of simultaneous connections to 3.</p>
<dl>
<dt>
<dd> <code>ncat &#8211;exec &quot;/bin/bash&quot; &#8211;max-conns 3 &#8211;allow 192.168.0.0/24 -l 8081 &#8211;keep-open</code></dl>
<p> Connect to smtphost:25 through a SOCKS4 server on port 1080.</p>
<dl>
<dt>
<dd> <code>ncat &#8211;proxy socks4host &#8211;proxy-type socks4 &#8211;proxy-auth user smtphost 25</code></dl>
<p> Create an HTTP proxy server on localhost port 8888.</p>
<dl>
<dt>
<dd> <code>ncat -l &#8211;proxy-type http localhost 8888</code></dl>
<p> Send a file over TCP port 9899 from host2 (client) to host1 (server).</p>
<dl>
<dt>
<dd> HOST1$ <code>ncat -l 9899 &gt; outputfile</code> </p>
<p> HOST2$ <code>ncat HOST1 9899 &lt; inputfile</code></dl>
<p> Transfer in the other direction, turning Ncat into a &#8220;one file&#8221; server.</p>
<dl>
<dt>
<dd> HOST1$ <code>ncat -l 9899 &lt; inputfile</code> </p>
<p> HOST2$ <code>ncat HOST1 9899 &gt; outputfile</code></dl>
<h2>EXIT CODE</h2>
<p> The exit code reflects whether a connection was made and completed successfully. 0 means there was no error. 1 means there was a network error of some kind, for example &#8220;Connection refused&#8221; or &#8220;Connection reset&#8221;. 2 is reserved for all other errors, like an invalid option or a nonexistent file.</p>
<h2>BUGS</h2>
<p> Like its authors, Ncat isn&#8217;t perfect. But you can help make it better by sending bug reports or even writing patches. If Ncat doesn&#8217;t behave the way you expect, first upgrade to the latest version available from m[blue]<code><a rel="nofollow" href="https://nmap.org">https://nmap.org</a></code>m[]. If the problem persists, do some research to determine whether it has already been discovered and addressed. Try Googling the error message or browsing the nmap-dev archives at m[blue]<code><a rel="nofollow" href="http://seclists.org/">http://seclists.org/</a></code>m[]. </p>
<p> Read this full manual page as well. If nothing comes of this, mail a bug report to &lt;dev [at] nmap.org&gt;. Please include everything you have learned about the problem, as well as what version of Ncat you are running and what operating system version it is running on. Problem reports and Ncat usage questions sent to dev [at] nmap.org are far more likely to be answered than those sent to Fyodor directly. </p>
<p> Code patches to fix bugs are even better than bug reports. Basic instructions for creating patch files with your changes are available at m[blue]<code><a rel="nofollow" href="https://svn.nmap.org/nmap/HACKING">https://svn.nmap.org/nmap/HACKING</a></code>m[]. Patches may be sent to nmap-dev (recommended) or to Fyodor directly.</p>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> &bull; Chris Gibson &lt;chris [at] linuxops.net&gt;</dl>
<dl>
<dt>
<dd> &bull; Kris Katterjohn &lt;katterjohn [at] gmail.com&gt;</dl>
<dl>
<dt>
<dd> &bull; Mixter &lt;mixter [at] gmail.com&gt;</dl>
<dl>
<dt>
<dd> &bull; Fyodor &lt;fyodor [at] nmap.org&gt; (m[blue]<code><a rel="nofollow" href="http://insecure.org">http://insecure.org</a></code>m[])</dl>
<p> The original Netcat was written by *Hobbit* &lt;hobbit [at] avian.org&gt;. While Ncat isn&#8217;t built on any code from the &#8220;traditional&#8221; Netcat (or any other implementation), Ncat is most definitely based on Netcat in spirit and functionality.</p>
<h2>LEGAL NOTICES</h2>
<h3>Ncat Copyright and Licensing</h3>
<p> Ncat is (C) 2005-2012 Insecure.Com LLC. It is distributed as free and open source software under the same license terms as our Nmap software. Precise terms and further details are available from m[blue]<code><a rel="nofollow" href="https://nmap.org/man/man-legal.html">https://nmap.org/man/man-legal.html</a></code>m[].</p>
<h3>Creative Commons License for this Ncat Guide</h3>
<p> This Ncat Reference Guide is (C) 2005-2012 Insecure.Com LLC. It is hereby placed under version 3.0 of the m[blue]<code>Creative Commons Attribution License</code>m[]<font SIZE="-2">[1]</font>. This allows you redistribute and modify the work as you desire, as long as you credit the original source. Alternatively, you may choose to treat this document as falling under the same license as Ncap itself (discussed previously).</p>
<h3>Source Code Availability and Community Contributions</h3>
<p> Source is provided to this software because we believe users have a right to know exactly what a program is going to do before they run it. This also allows you to audit the software for security holes (none have been found so far). </p>
<p> Source code also allows you to port Nmap (which includes Ncat) to new platforms, fix bugs, and add new features. You are highly encouraged to send your changes to &lt;dev [at] nmap.org&gt; for possible incorporation into the main distribution. By sending these changes to Fyodor or one of the Insecure.Org development mailing lists, it is assumed that you are offering the Nmap Project (Insecure.Com LLC) the unlimited, non-exclusive right to reuse, modify, and relicense the code. Nmap will always be available open source, but this is important because the inability to relicense code has caused devastating problems for other Free Software projects (such as KDE and NASM). We also occasionally relicense the code to third parties as discussed in the Nmap man page. If you wish to specify special license conditions of your contributions, just say so when you send them.</p>
<h3>No Warranty</h3>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License v2.0 for more details at m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses/gpl-2.0.html">http://www.gnu.org/licenses/gpl-2.0.html</a></code>m[], or in the COPYING file included with Nmap.</p>
<h3>Inappropriate Usage</h3>
<p> Ncat should never be installed with special privileges (e.g. suid root). That would open up a major security vulnerability as other users on the system (or attackers) could use it for privilege escalation.</p>
<h3>Third-Party Software</h3>
<p> This product includes software developed by the m[blue]<code>Apache Software Foundation</code>m[]<font SIZE="-2">[2]</font>. A modified version of the m[blue]<code>Libpcap portable packet capture library</code>m[]<font SIZE="-2">[3]</font> is distributed along with Ncat. The Windows version of Ncat utilized the Libpcap-derived m[blue]<code>WinPcap library</code>m[]<font SIZE="-2">[4]</font> instead. Certain raw networking functions use the m[blue]<code>Libdnet</code>m[]<font SIZE="-2">[5]</font> networking library, which was written by Dug Song. A modified version is distributed with Ncat. Ncat can optionally link with the m[blue]<code>OpenSSL cryptography toolkit</code>m[]<font SIZE="-2">[6]</font> for SSL version detection support. All of the third-party software described in this paragraph is freely redistributable under BSD-style software licenses.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Creative Commons Attribution License</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://creativecommons.org/licenses/by/3.0/">http://creativecommons.org/licenses/by/3.0/</a></dl>
<dt> 2.</p>
<dd> Apache Software Foundation</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.apache.org">http://www.apache.org</a></dl>
<dt> 3.</p>
<dd> Libpcap portable packet capture library</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.tcpdump.org">http://www.tcpdump.org</a></dl>
<dt> 4.</p>
<dd> WinPcap library</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.winpcap.org">http://www.winpcap.org</a></dl>
<dt> 5.</p>
<dd> Libdnet</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://libdnet.sourceforge.net">http://libdnet.sourceforge.net</a></dl>
<dt> 6.</p>
<dd> OpenSSL cryptography toolkit</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.openssl.org">http://www.openssl.org</a></dl>
</dl>
<h2>Index</h2>
