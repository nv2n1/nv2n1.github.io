---
title: "socat(1)"
name: "socat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-socat/"
description: "socat – Multipurpose relay (SOcket CAT)"
---

<h2 class="name">NAME</h2>
<p> socat &#8211; Multipurpose relay (SOcket CAT)</p>
<h2>SYNOPSIS</h2>
<p> <tt>socat [options] &lt;address&gt; &lt;address&gt;</tt><br />
 <tt>socat -V</tt><br />
 <tt>socat -h[h[h]] | -?[?[?]]</tt><br />
 <tt>filan</tt><br />
 <tt>procan</tt> </p>
<h2>DESCRIPTION</h2>
<p> <code>Socat</code> is a command line based utility that establishes two bidirectional byte streams and transfers data between them. Because the streams can be constructed from a large set of different types of data sinks and sources (see address types), and because lots of address options may be applied to the streams, socat can be used for many different purposes. </p>
<p> <code>Filan</code> is a utility that prints information about its active file descriptors to stdout. It has been written for debugging <code>socat</code>, but might be useful for other purposes too. Use the -h option to find more infos. </p>
<p> <code>Procan</code> is a utility that prints information about process parameters to stdout. It has been written to better understand some UNIX process properties and for debugging <code>socat</code>, but might be useful for other purposes too. </p>
<p> The life cycle of a <code>socat</code> instance typically consists of four phases. </p>
<p> In the <i>init</i> phase, the command line options are parsed and logging is initialized. </p>
<p> During the <i>open</i> phase, <code>socat</code> opens the first address and afterwards the second address. These steps are usually blocking; thus, especially for complex address types like socks, connection requests or authentication dialogs must be completed before the next step is started. </p>
<p> In the <i>transfer</i> phase, <code>socat</code> watches both streams&#8217; read and write file descriptors via <tt>select()</tt> , and, when data is available on one side <i>and</i> can be written to the other side, socat reads it, performs newline character conversions if required, and writes the data to the write file descriptor of the other stream, then continues waiting for more data in both directions. </p>
<p> When one of the streams effectively reaches EOF, the <i>closing</i> phase begins. <code>Socat</code> transfers the EOF condition to the other stream, i.e. tries to shutdown only its write stream, giving it a chance to terminate gracefully. For a defined time <code>socat</code> continues to transfer data in the other direction, but then closes all remaining channels and terminates. </p>
<h2>OPTIONS</h2>
<p> <code>Socat</code> provides some command line options that modify the behaviour of the program. They have nothing to do with so called address options that are used as parts of address specifications. </p>
<dl>
<dt><tt>-V</tt></p>
<dd> Print version and available feature information to stdout, and exit.</p>
<dt><tt>-h | -?</tt></p>
<dd> Print a help text to stdout describing command line options and available address types, and exit.</p>
<dt><tt>-hh | -??</tt></p>
<dd> Like -h, plus a list of the short names of all available address options. Some options are platform dependend, so this output is helpful for checking the particular implementation.</p>
<dt><tt>-hhh | -???</tt></p>
<dd> Like -hh, plus a list of all available address option names.</p>
<dt><tt>-d</tt></p>
<dd> Without this option, only fatal and error messages are generated; applying this option also prints warning messages. See DIAGNOSTICS for more information.</p>
<dt><tt>-d -d</tt></p>
<dd> Prints fatal, error, warning, and notice messages.</p>
<dt><tt>-d -d -d</tt></p>
<dd> Prints fatal, error, warning, notice, and info messages.</p>
<dt><tt>-d -d -d -d</tt></p>
<dd> Prints fatal, error, warning, notice, info, and debug messages.</p>
<dt><tt>-D</tt></p>
<dd> Logs information about file descriptors before starting the transfer phase.</p>
<dt><tt>-ly[&lt;facility&gt;]</tt></p>
<dd> Writes messages to syslog instead of stderr; severity as defined with -d option. With optional &lt;facility&gt;, the syslog type can be selected, default is &quot;daemon&quot;.</p>
<dt><tt>-lf</tt><tt> &lt;logfile&gt;</tt></p>
<dd> Writes messages to &lt;logfile&gt; [filename] instead of stderr.</p>
<dt><tt>-ls</tt></p>
<dd> Writes messages to stderr (this is the default).</p>
<dt><tt>-lp</tt><tt>&lt;progname&gt;</tt></p>
<dd> Overrides the program name printed in error messages and used for constructing environment variable names.</p>
<dt><tt>-lu</tt></p>
<dd> Extends the timestamp of error messages to microsecond resolution. Does not work when logging to syslog.</p>
<dt><tt>-lm[&lt;facility&gt;]</tt></p>
<dd> Mixed log mode. During startup messages are printed to stderr; when <code>socat</code> starts the transfer phase loop or daemon mode (i.e. after opening all streams and before starting data transfer, or, with listening sockets with fork option, before the first accept call), it switches logging to syslog. With optional &lt;facility&gt;, the syslog type can be selected, default is &quot;daemon&quot;.</p>
<dt><tt>-lh</tt></p>
<dd> Adds hostname to log messages. Uses the value from environment variable HOSTNAME or the value retrieved with <tt>uname()</tt> if HOSTNAME is not set.</p>
<dt><tt>-v</tt></p>
<dd> Writes the transferred data not only to their target streams, but also to stderr. The output format is text with some conversions for readability, and prefixed with &quot;&gt; &quot; or &quot;&lt; &quot; indicating flow directions.</p>
<dt><tt>-x</tt></p>
<dd> Writes the transferred data not only to their target streams, but also to stderr. The output format is hexadecimal, prefixed with &quot;&gt; &quot; or &quot;&lt; &quot; indicating flow directions. Can be combined with <tt>-v</tt> .</p>
<dt><tt>-b</tt><tt>&lt;size&gt;</tt></p>
<dd> Sets the data transfer block &lt;size&gt; [size_t]. At most &lt;size&gt; bytes are transferred per step. Default is 8192 bytes.</p>
<dt><tt>-s</tt></p>
<dd> By default, <code>socat</code> terminates when an error occurred to prevent the process from running when some option could not be applied. With this option, <code>socat</code> is sloppy with errors and tries to continue. Even with this option, socat will exit on fatals, and will abort connection attempts when security checks failed.</p>
<dt><tt>-t</tt><tt>&lt;timeout&gt;</tt></p>
<dd> When one channel has reached EOF, the write part of the other channel is shut down. Then, <code>socat</code> waits &lt;timeout&gt; [timeval] seconds before terminating. Default is 0.5 seconds. This timeout only applies to addresses where write and read part can be closed independently. When during the timeout interval the read part gives EOF, socat terminates without awaiting the timeout.</p>
<dt><tt>-T</tt><tt>&lt;timeout&gt;</tt></p>
<dd> Total inactivity timeout: when socat is already in the transfer loop and nothing has happened for &lt;timeout&gt; [timeval] seconds (no data arrived, no interrupt occurred&#8230;) then it terminates. Useful with protocols like UDP that cannot transfer EOF.</p>
<dt><tt>-u</tt></p>
<dd> Uses unidirectional mode. The first address is only used for reading, and the second address is only used for writing (example).</p>
<dt><tt>-U</tt></p>
<dd> Uses unidirectional mode in reverse direction. The first address is only used for writing, and the second address is only used for reading.</p>
<dt><tt>-g</tt></p>
<dd> During address option parsing, don&#8217;t check if the option is considered useful in the given address environment. Use it if you want to force, e.g., appliance of a socket option to a serial device.</p>
<dt><tt>-L</tt><tt>&lt;lockfile&gt;</tt></p>
<dd> If lockfile exists, exits with error. If lockfile does not exist, creates it and continues, unlinks lockfile on exit.</p>
<dt><tt>-W</tt><tt>&lt;lockfile&gt;</tt></p>
<dd> If lockfile exists, waits until it disappears. When lockfile does not exist, creates it and continues, unlinks lockfile on exit.</p>
<dt><tt>-4</tt></p>
<dd> Use IP version 4 in case that the addresses do not implicitly or explicitly specify a version; this is the default.</p>
<dt><tt>-6</tt></p>
<dd> Use IP version 6 in case that the addresses do not implicitly or explicitly specify a version. </p>
</dl>
<h2>ADDRESS SPECIFICATIONS</h2>
<p> With the address command line arguments, the user gives <code>socat</code> instructions and the necessary information for establishing the byte streams. </p>
<p> An address specification usually consists of an address type keyword, zero or more required address parameters separated by &#8216;:&#8217; from the keyword and from each other, and zero or more address options separated by &#8216;,&#8217;. </p>
<p> The keyword specifies the address type (e.g., TCP4, OPEN, EXEC). For some keywords there exist synonyms (&#8216;-&#8216; for STDIO, TCP for TCP4). Keywords are case insensitive. For a few special address types, the keyword may be omitted: Address specifications starting with a number are assumed to be FD (raw file descriptor) addresses; if a &#8216;/&#8217; is found before the first &#8216;:&#8217; or &#8216;,&#8217;, GOPEN (generic file open) is assumed. </p>
<p> The required number and type of address parameters depend on the address type. E.g., TCP4 requires a server specification (name or address), and a port specification (number or service name). </p>
<p> Zero or more address options may be given with each address. They influence the address in some ways. Options consist of an option keyword or an option keyword and a value, separated by &#8216;=&#8217;. Option keywords are case insensitive. For filtering the options that are useful with an address type, each option is member of one option group. For each address type there is a set of option groups allowed. Only options belonging to one of these address groups may be used (except with option -g). </p>
<p> Address specifications following the above schema are also called <i>single</i> address specifications. Two single addresses can be combined with &quot;!!&quot; to form a <i>dual</i> type address for one channel. Here, the first address is used by <code>socat</code> for reading data, and the second address for writing data. There is no way to specify an option only once for being applied to both single addresses. </p>
<p> Usually, addresses are opened in read/write mode. When an address is part of a dual address specification, or when option -u or -U is used, an address might be used only for reading or for writing. Considering this is important with some address types. </p>
<p> With socat version 1.5.0 and higher, the lexical analysis tries to handle quotes and parenthesis meaningfully and allows escaping of special characters. If one of the characters ( { [ &#8216; is found, the corresponding closing character &#8211; ) } ] &#8216; &#8211; is looked for; they may also be nested. Within these constructs, socats special characters and strings : , !! are not handled specially. All those characters and strings can be escaped with \ or within &quot;&quot; </p>
<h2>ADDRESS TYPES</h2>
<p> This section describes the available address types with their keywords, parameters, and semantics. </p>
<dl>
<dt><tt>CREATE:&lt;filename&gt;</tt></p>
<dd> Opens &lt;filename&gt; with <tt>creat()</tt> and uses the file descriptor for writing. This address type requires write-only context, because a file opened with <tt>creat</tt> cannot be read from.<br />
 Flags like O_LARGEFILE cannot be applied. If you need them use OPEN with options create,create.<br />
 &lt;filename&gt; must be a valid existing or not existing path. If &lt;filename&gt; is a named pipe, <tt>creat()</tt> might block; if &lt;filename&gt; refers to a socket, this is an error.<br />
 Option groups: FD,REG,NAMED<br />
 Useful options: mode, user, group, unlink-early, unlink-late, append<br />
 See also: OPEN, GOPEN</p>
<dt><tt>EXEC:&lt;command-line&gt;</tt></p>
<dd> Forks a sub process that establishes communication with its parent process and invokes the specified program with <tt>execvp()</tt> . &lt;command-line&gt; is a simple command with arguments separated by single spaces. If the program name contains a &#8216;/&#8217;, the part after the last &#8216;/&#8217; is taken as ARGV[0]. If the program name is a relative path, the <tt>execvp()</tt> semantics for finding the program via <tt>$PATH</tt> apply. After successful program start, <code>socat</code> writes data to stdin of the process and reads from its stdout using a UNIX domain socket generated by <tt>socketpair()</tt> per default. (example)<br />
 Option groups: FD,SOCKET,EXEC,FORK,TERMIOS<br />
 Useful options: path, fdin, fdout, chroot, su, su-d, nofork, pty, stderr, ctty, setsid, pipes, login, sigint, sigquit<br />
 See also: SYSTEM</p>
<dt><tt>FD:&lt;fdnum&gt;</tt></p>
<dd> Uses the file descriptor &lt;fdnum&gt;. It must already exist as valid UN*X file descriptor.<br />
 Option groups: FD (TERMIOS,REG,SOCKET)<br />
 See also: STDIO, STDIN, STDOUT, STDERR</p>
<dt><tt>GOPEN:&lt;filename&gt;</tt></p>
<dd> (Generic open) This address type tries to handle any file system entry except directories usefully. &lt;filename&gt; may be a relative or absolute path. If it already exists, its type is checked. In case of a UNIX domain socket, <code>socat</code> connects; if connecting fails, <code>socat</code> assumes a datagram socket and uses <tt>sendto()</tt> calls. If the entry is not a socket, <code>socat</code> opens it applying the <tt>O_APPEND</tt> flag. If it does not exist, it is opened with flag <tt>O_CREAT</tt> as a regular file (example).<br />
 Option groups: FD,REG,SOCKET,NAMED,OPEN<br />
 See also: OPEN, CREATE, UNIX-CONNECT</p>
<dt>
<dd>
<dt><tt>IP-SENDTO:&lt;host&gt;:&lt;protocol&gt;</tt></p>
<dd> Opens a raw IP socket. Depending on host specification or option pf, IP protocol version 4 or 6 is used. It uses &lt;protocol&gt; to send packets to &lt;host&gt; [IP address] and receives packets from host, ignores packets from other hosts. Protocol 255 uses the raw socket with the IP header being part of the data.<br />
 Option groups: FD,SOCKET,IP4,IP6<br />
 Useful options: pf, ttl<br />
 See also: IP4-SENDTO, IP6-SENDTO, IP-RECVFROM, IP-RECV, UDP-SENDTO, UNIX-SENDTO</p>
<dt><tt>INTERFACE:&lt;interface&gt;</tt></p>
<dd> Communicates with a network connected on an interface using raw packets including link level data. &lt;interface&gt; is the name of the network interface. Currently only available on Linux. Option groups: FD,SOCKET<br />
 Useful options: pf, type<br />
 See also: ip-recv</p>
<dt><tt>IP4-SENDTO:&lt;host&gt;:&lt;protocol&gt;</tt></p>
<dd> Like IP-SENDTO, but always uses IPv4.<br />
 Option groups: FD,SOCKET,IP4 </p>
<dt><tt>IP6-SENDTO:&lt;host&gt;:&lt;protocol&gt;</tt></p>
<dd> Like IP-SENDTO, but always uses IPv6.<br />
 Option groups: FD,SOCKET,IP6 </p>
<dt>
<dd>
<dt><tt>IP-DATAGRAM:&lt;address&gt;:&lt;protocol&gt;</tt></p>
<dd> Sends outgoing data to the specified address which may in particular be a broadcast or multicast address. Packets arriving on the local socket are checked if their source addresses match RANGE or TCPWRAP options. This address type can for example be used for implementing symmetric or asymmetric broadcast or multicast communications.<br />
 Option groups: FD, SOCKET, IP4, IP6, RANGE<br />
 Useful options: bind, range, tcpwrap, broadcast, ip-multicast-loop, ip-multicast-ttl, ip-multicast-if, ip-add-membership, ttl, tos, pf<br />
 See also: IP4-DATAGRAM, IP6-DATAGRAM, IP-SENDTO, IP-RECVFROM, IP-RECV, UDP-DATAGRAM</p>
<dt><tt>IP4-DATAGRAM:&lt;host&gt;:&lt;protocol&gt;</tt></p>
<dd> Like IP-DATAGRAM, but always uses IPv4. (example)<br />
 Option groups: FD,SOCKET,IP4,RANGE </p>
<dt><tt>IP6-DATAGRAM:&lt;host&gt;:&lt;protocol&gt;</tt></p>
<dd> Like IP-DATAGRAM, but always uses IPv6. Please note that IPv6 does not know broadcasts.<br />
 Option groups: FD,SOCKET,IP6,RANGE </p>
<dt>
<dd>
<dt><tt>IP-RECVFROM:&lt;protocol&gt;</tt></p>
<dd> Opens a raw IP socket of &lt;protocol&gt;. Depending on option pf, IP protocol version 4 or 6 is used. It receives one packet from an unspecified peer and may send one or more answer packets to that peer. This mode is particularly useful with fork option where each arriving packet &#8211; from arbitrary peers &#8211; is handled by its own sub process. This allows a behaviour similar to typical UDP based servers like ntpd or named.<br />
 Please note that the reply packets might be fetched as incoming traffic when sender and receiver IP address are identical because there is no port number to distinguish the sockets.<br />
 This address works well with IP-SENDTO address peers (see above). Protocol 255 uses the raw socket with the IP header being part of the data.<br />
 Option groups: FD,SOCKET,IP4,IP6,CHILD,RANGE<br />
 Useful options: pf, fork, range, ttl, broadcast<br />
 See also: IP4-RECVFROM, IP6-RECVFROM, IP-SENDTO, IP-RECV, UDP-RECVFROM, UNIX-RECVFROM</p>
<dt><tt>IP4-RECVFROM:&lt;protocol&gt;</tt></p>
<dd> Like IP-RECVFROM, but always uses IPv4.<br />
 Option groups: FD,SOCKET,IP4,CHILD,RANGE </p>
<dt><tt>IP6-RECVFROM:&lt;protocol&gt;</tt></p>
<dd> Like IP-RECVFROM, but always uses IPv6.<br />
 Option groups: FD,SOCKET,IP6,CHILD,RANGE </p>
<dt>
<dd>
<dt><tt>IP-RECV:&lt;protocol&gt;</tt></p>
<dd> Opens a raw IP socket of &lt;protocol&gt;. Depending on option pf, IP protocol version 4 or 6 is used. It receives packets from multiple unspecified peers and merges the data. No replies are possible. It can be, e.g., addressed by socat IP-SENDTO address peers. Protocol 255 uses the raw socket with the IP header being part of the data.<br />
 Option groups: FD,SOCKET,IP4,IP6,RANGE<br />
 Useful options: pf, range<br />
 See also: IP4-RECV, IP6-RECV, IP-SENDTO, IP-RECVFROM, UDP-RECV, UNIX-RECV</p>
<dt><tt>IP4-RECV:&lt;protocol&gt;</tt></p>
<dd> Like IP-RECV, but always uses IPv4.<br />
 Option groups: FD,SOCKET,IP4,RANGE </p>
<dt><tt>IP6-RECV:&lt;protocol&gt;</tt></p>
<dd> Like IP-RECV, but always uses IPv6.<br />
 Option groups: FD,SOCKET,IP6,RANGE </p>
<dt>
<dd>
<dt><tt>OPEN:&lt;filename&gt;</tt></p>
<dd> Opens &lt;filename&gt; using the <tt>open()</tt> system call (example). This operation fails on UNIX domain sockets.<br />
 Note: This address type is rarly useful in bidirectional mode.<br />
 Option groups: FD,REG,NAMED,OPEN<br />
 Useful options: creat, excl, noatime, nofollow, append, rdonly, wronly, lock, readbytes, ignoreeof<br />
 See also: CREATE, GOPEN, UNIX-CONNECT</p>
<dt><tt>OPENSSL:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Tries to establish a SSL connection to &lt;port&gt; [TCP service] on &lt;host&gt; [IP address] using TCP/IP version 4 or 6 depending on address specification, name resolution, or option pf.<br />
 NOTE: The server certificate is only checked for validity against cafile or capath, but not for match with the server&#8217;s name or its IP address!<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,OPENSSL,RETRY<br />
 Useful options: cipher, method, verify, cafile, capath, certificate, key, compress, bind, pf, connect-timeout, sourceport, retry<br />
 See also: OPENSSL-LISTEN, TCP</p>
<dt><tt>OPENSSL-LISTEN:&lt;port&gt;</tt></p>
<dd> Listens on tcp &lt;port&gt; [TCP service]. The IP version is 4 or the one specified with pf. When a connection is accepted, this address behaves as SSL server.<br />
 Note: You probably want to use the certificate option with this address.<br />
 NOTE: The client certificate is only checked for validity against cafile or capath, but not for match with the client&#8217;s name or its IP address!<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,LISTEN,OPENSSL,CHILD,RANGE,RETRY<br />
 Useful options: pf, cipher, method, verify, cafile, capath, certificate, key, compress, fork, bind, range, tcpwrap, su, reuseaddr, retry<br />
 See also: OPENSSL, TCP-LISTEN</p>
<dt><tt>PIPE:&lt;filename&gt;</tt></p>
<dd> If &lt;filename&gt; already exists, it is opened. If it does not exist, a named pipe is created and opened. Beginning with socat version 1.4.3, the named pipe is removed when the address is closed (but see option unlink-close<br />
 Note: When a pipe is used for both reading and writing, it works as echo service.<br />
 Note: When a pipe is used for both reading and writing, and socat tries to write more bytes than the pipe can buffer (Linux 2.4: 2048 bytes), socat might block. Consider using socat option, e.g., <tt>-b 2048</tt><br />
 Option groups: FD,NAMED,OPEN<br />
 Useful options: rdonly, nonblock, group, user, mode, unlink-early<br />
 See also: unnamed pipe</p>
<dt><tt>PIPE</tt></p>
<dd> Creates an unnamed pipe and uses it for reading and writing. It works as an echo, because everything written to it appeares immediately as read data.<br />
 Note: When socat tries to write more bytes than the pipe can queue (Linux 2.4: 2048 bytes), socat might block. Consider, e.g., using option <tt>-b 2048</tt><br />
 Option groups: FD<br />
 See also: named pipe</p>
<dt><tt>PROXY:&lt;proxy&gt;:&lt;hostname&gt;:&lt;port&gt;</tt></p>
<dd> Connects to an HTTP proxy server on port 8080 using TCP/IP version 4 or 6 depending on address specification, name resolution, or option pf, and sends a CONNECT request for hostname:port. If the proxy grants access and succeeds to connect to the target, data transfer between socat and the target can start. Note that the traffic need not be HTTP but can be an arbitrary protocol.<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,HTTP,RETRY<br />
 Useful options: proxyport, ignorecr, proxyauth, resolve, crnl, bind, connect-timeout, mss, sourceport, retry<br />
 See also: SOCKS, TCP</p>
<dt><tt>PTY</tt></p>
<dd> Generates a pseudo terminal (pty) and uses its master side. Another process may open the pty&#8217;s slave side using it like a serial line or terminal. (example). If both the ptmx and the openpty mechanisms are available, ptmx is used (POSIX).<br />
 Option groups: FD,NAMED,PTY,TERMIOS<br />
 Useful options: link, openpty, wait-slave, mode, user, group<br />
 See also: UNIX-LISTEN, PIPE, EXEC, SYSTEM</p>
<dt><tt>READLINE</tt></p>
<dd> Uses GNU readline and history on stdio to allow editing and reusing input lines (example). This requires the GNU readline and history libraries. Note that stdio should be a (pseudo) terminal device, otherwise readline does not seem to work.<br />
 Option groups: FD,READLINE,TERMIOS<br />
 Useful options: history, noecho<br />
 See also: STDIO</p>
<dt><tt>SCTP-CONNECT:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Establishes an SCTP stream connection to the specified &lt;host&gt; [IP address] and &lt;port&gt; [TCP service] using TCP/IP version 4 or 6 depending on address specification, name resolution, or option pf.<br />
 Option groups: FD,SOCKET,IP4,IP6,SCTP,CHILD,RETRY<br />
 Useful options: bind, pf, connect-timeout, tos, mtudiscover, sctp-maxseg, sctp-nodelay, nonblock, sourceport, retry, readbytes<br />
 See also: SCTP4-CONNECT, SCTP6-CONNECT, SCTP-LISTEN, TCP-CONNECT</p>
<dt><tt>SCTP4-CONNECT:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like SCTP-CONNECT, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,IP4,SCTP,CHILD,RETRY </p>
<dt><tt>SCTP6-CONNECT:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like SCTP-CONNECT, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6,SCTP,CHILD,RETRY </p>
<dt><tt>SCTP-LISTEN:&lt;port&gt;</tt></p>
<dd> Listens on &lt;port&gt; [TCP service] and accepts a TCP/IP connection. The IP version is 4 or the one specified with address option pf, socat option (-4, -6), or environment variable SOCAT_DEFAULT_LISTEN_IP. Note that opening this address usually blocks until a client connects.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,SCTP,RETRY<br />
 Useful options: crnl, fork, bind, range, tcpwrap, pf, max-children, backlog, sctp-maxseg, sctp-nodelay, su, reuseaddr, retry, cool-write<br />
 See also: SCTP4-LISTEN, SCTP6-LISTEN, TCP-LISTEN, SCTP-CONNECT</p>
<dt><tt>SCTP4-LISTEN:&lt;port&gt;</tt></p>
<dd> Like SCTP-LISTEN, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4,SCTP,RETRY </p>
<dt><tt>SCTP6-LISTEN:&lt;port&gt;</tt></p>
<dd> Like SCTP-LISTEN, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP6,SCTP,RETRY </p>
<dt><tt>SOCKET-CONNECT:&lt;domain&gt;:&lt;protocol&gt;:&lt;remote-address&gt;</tt></p>
<dd> Creates a stream socket using the first and second given socket parameters and <tt>SOCK_STREAM</tt> (see man socket\(2)) and connects to the remote-address. The two socket parameters have to be specified by int numbers. Consult your OS documentation and include files to find the appropriate values. The remote-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Please note that you can &#8211; beyond the options of the specified groups &#8211; also use options of higher level protocols when you apply socat option -g.<br />
 Option groups: FD,SOCKET,CHILD,RETRY<br />
 Useful options: bind, setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: TCP, UDP-CONNECT, UNIX-CONNECT, SOCKET-LISTEN, SOCKET-SENDTO</p>
<dt><tt>SOCKET-DATAGRAM:&lt;domain&gt;:&lt;type&gt;:&lt;protocol&gt;:&lt;remote-address&gt;</tt></p>
<dd> Creates a datagram socket using the first three given socket parameters (see man socket\(2)) and sends outgoing data to the remote-address. The three socket parameters have to be specified by int numbers. Consult your OS documentation and include files to find the appropriate values. The remote-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Please note that you can &#8211; beyond the options of the specified groups &#8211; also use options of higher level protocols when you apply socat option -g.<br />
 Option groups: FD,SOCKET,RANGE<br />
 Useful options: bind, range, setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: UDP-DATAGRAM, IP-DATAGRAM, SOCKET-SENDTO, SOCKET-RECV, SOCKET-RECVFROM</p>
<dt><tt>SOCKET-LISTEN:&lt;domain&gt;:&lt;protocol&gt;:&lt;local-address&gt;</tt></p>
<dd> Creates a stream socket using the first and second given socket parameters and <tt>SOCK_STREAM</tt> (see man socket\(2)) and waits for incoming connections on local-address. The two socket parameters have to be specified by int numbers. Consult your OS documentation and include files to find the appropriate values. The local-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Please note that you can &#8211; beyond the options of the specified groups &#8211; also use options of higher level protocols when you apply socat option -g.<br />
 Option groups: FD,SOCKET,LISTEN,RANGE,CHILD,RETRY<br />
 Useful options: setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: TCP, UDP-CONNECT, UNIX-CONNECT, SOCKET-LISTEN, SOCKET-SENDTO, SOCKET-SENDTO</p>
<dt><tt>SOCKET-RECV:&lt;domain&gt;:&lt;type&gt;:&lt;protocol&gt;:&lt;local-address&gt;</tt></p>
<dd> Creates a socket using the three given socket parameters (see man socket\(2)) and binds it to &lt;local-address&gt;. Receives arriving data. The three parameters have to be specified by int numbers. Consult your OS documentation and include files to find the appropriate values. The local-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Option groups: FD,SOCKET,RANGE<br />
 Useful options: range, setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: UDP-RECV, IP-RECV, UNIX-RECV, SOCKET-DATAGRAM, SOCKET-SENDTO, SOCKET-RECVFROM</p>
<dt><tt>SOCKET-RECVFROM:&lt;domain&gt;:&lt;type&gt;:&lt;protocol&gt;:&lt;local-address&gt;</tt></p>
<dd> Creates a socket using the three given socket parameters (see man socket\(2)) and binds it to &lt;local-address&gt;. Receives arriving data and sends replies back to the sender. The first three parameters have to be specified as int numbers. Consult your OS documentation and include files to find the appropriate values. The local-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Option groups: FD,SOCKET,CHILD,RANGE<br />
 Useful options: fork, range, setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: UDP-RECVFROM, IP-RECVFROM, UNIX-RECVFROM, SOCKET-DATAGRAM, SOCKET-SENDTO, SOCKET-RECV</p>
<dt><tt>SOCKET-SENDTO:&lt;domain&gt;:&lt;type&gt;:&lt;protocol&gt;:&lt;remote-address&gt;</tt></p>
<dd> Creates a socket using the three given socket parameters (see man socket\(2)). Sends outgoing data to the given address and receives replies. The three parameters have to be specified as int numbers. Consult your OS documentation and include files to find the appropriate values. The remote-address must be the data representation of a sockaddr structure without sa_family and (BSD) sa_len components.<br />
 Option groups: FD,SOCKET<br />
 Useful options: bind, setsockopt-int, setsockopt-bin, setsockopt-string<br />
 See also: UDP-SENDTO, IP-SENDTO, UNIX-SENDTO, SOCKET-DATAGRAM, SOCKET-RECV SOCKET-RECVFROM</p>
<dt><tt>SOCKS4:&lt;socks-server&gt;:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Connects via &lt;socks-server&gt; [IP address] to &lt;host&gt; [IPv4 address] on &lt;port&gt; [TCP service], using socks version 4 protocol over IP version 4 or 6 depending on address specification, name resolution, or option pf (example).<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,SOCKS4,RETRY<br />
 Useful options: socksuser, socksport, sourceport, pf, retry<br />
 See also: SOCKS4A, PROXY, TCP</p>
<dt><tt>SOCKS4A:&lt;socks-server&gt;:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> like SOCKS4, but uses socks protocol version 4a, thus leaving host name resolution to the socks server.<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,SOCKS4,RETRY </p>
<dt><tt>STDERR</tt></p>
<dd> Uses file descriptor 2.<br />
 Option groups: FD (TERMIOS,REG,SOCKET)<br />
 See also: FD</p>
<dt><tt>STDIN</tt></p>
<dd> Uses file descriptor 0.<br />
 Option groups: FD (TERMIOS,REG,SOCKET)<br />
 Useful options: readbytes<br />
 See also: FD</p>
<dt><tt>STDIO</tt></p>
<dd> Uses file descriptor 0 for reading, and 1 for writing.<br />
 Option groups: FD (TERMIOS,REG,SOCKET)<br />
 Useful options: readbytes<br />
 See also: FD</p>
<dt><tt>STDOUT</tt></p>
<dd> Uses file descriptor 1.<br />
 Option groups: FD (TERMIOS,REG,SOCKET)<br />
 See also: FD</p>
<dt><tt>SYSTEM:&lt;shell-command&gt;</tt></p>
<dd> Forks a sub process that establishes communication with its parent process and invokes the specified program with <tt>system()</tt> . Please note that &lt;shell-command&gt; [string] must not contain &#8216;,&#8217; or &quot;!!&quot;, and that shell meta characters may have to be protected. After successful program start, <code>socat</code> writes data to stdin of the process and reads from its stdout.<br />
 Option groups: FD,SOCKET,EXEC,FORK,TERMIOS<br />
 Useful options: path, fdin, fdout, chroot, su, su-d, nofork, pty, stderr, ctty, setsid, pipes, sigint, sigquit<br />
 See also: EXEC</p>
<dt><tt>TCP:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Connects to &lt;port&gt; [TCP service] on &lt;host&gt; [IP address] using TCP/IP version 4 or 6 depending on address specification, name resolution, or option pf.<br />
 Option groups: FD,SOCKET,IP4,IP6,TCP,RETRY<br />
 Useful options: crnl, bind, pf, connect-timeout, tos, mtudiscover, mss, nodelay, nonblock, sourceport, retry, readbytes<br />
 See also: TCP4, TCP6, TCP-LISTEN, UDP, SCTP-CONNECT, UNIX-CONNECT</p>
<dt><tt>TCP4:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like TCP, but only supports IPv4 protocol (example).<br />
 Option groups: FD,SOCKET,IP4,TCP,RETRY </p>
<dt><tt>TCP6:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like TCP, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6,TCP,RETRY </p>
<dt><tt>TCP-LISTEN:&lt;port&gt;</tt></p>
<dd> Listens on &lt;port&gt; [TCP service] and accepts a TCP/IP connection. The IP version is 4 or the one specified with address option pf, socat option (-4, -6), or environment variable SOCAT_DEFAULT_LISTEN_IP. Note that opening this address usually blocks until a client connects.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,TCP,RETRY<br />
 Useful options: crnl, fork, bind, range, tcpwrap, pf, max-children, backlog, mss, su, reuseaddr, retry, cool-write<br />
 See also: TCP4-LISTEN, TCP6-LISTEN, UDP-LISTEN, SCTP-LISTEN, UNIX-LISTEN, OPENSSL-LISTEN, TCP-CONNECT</p>
<dt><tt>TCP4-LISTEN:&lt;port&gt;</tt></p>
<dd> Like TCP-LISTEN, but only supports IPv4 protocol (example).<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4,TCP,RETRY </p>
<dt><tt>TCP6-LISTEN:&lt;port&gt;</tt></p>
<dd> Like TCP-LISTEN, but only supports IPv6 protocol.<br />
 Additional useful option: ipv6only<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP6,TCP,RETRY </p>
<dt><tt>TUN[:&lt;if-addr&gt;/&lt;bits&gt;]</tt></p>
<dd> Creates a Linux TUN/TAP device and optionally assignes it the address and netmask given by the parameters. The resulting network interface is almost ready for use by other processes; socat serves its &quot;wire side&quot;. This address requires read and write access to the tunnel cloning device, usually <tt>/dev/net/tun</tt> , as well as permission to set some <tt>ioctl()s</tt>. <code>Option iff-up is required to immediately activate the interface!</code><br />
 Option groups: FD,NAMED,OPEN,TUN<br />
 Useful options: iff-up, tun-device, tun-name, tun-type, iff-no-pi<br />
 See also: ip-recv</p>
<dt><tt>UDP:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Connects to &lt;port&gt; [UDP service] on &lt;host&gt; [IP address] using UDP/IP version 4 or 6 depending on address specification, name resolution, or option pf.<br />
 Please note that, due to UDP protocol properties, no real connection is established; data has to be sent for `connecting&#8217; to the server, and no end-of-file condition can be transported.<br />
 Option groups: FD,SOCKET,IP4,IP6<br />
 Useful options: ttl, tos, bind, sourceport, pf<br />
 See also: UDP4, UDP6, UDP-LISTEN, TCP, IP</p>
<dt><tt>UDP4:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,IP4 </p>
<dt><tt>UDP6:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6 </p>
<dt><tt>UDP-DATAGRAM:&lt;address&gt;:&lt;port&gt;</tt></p>
<dd> Sends outgoing data to the specified address which may in particular be a broadcast or multicast address. Packets arriving on the local socket are checked for the correct remote port and if their source addresses match RANGE or TCPWRAP options. This address type can for example be used for implementing symmetric or asymmetric broadcast or multicast communications.<br />
 Option groups: FD,SOCKET,IP4,IP6,RANGE<br />
 Useful options: bind, range, tcpwrap, broadcast, ip-multicast-loop, ip-multicast-ttl, ip-multicast-if, ip-add-membership, ttl, tos, sourceport, pf<br />
 See also: UDP4-DATAGRAM, UDP6-DATAGRAM, UDP-SENDTO, UDP-RECVFROM, UDP-RECV, UDP-CONNECT, UDP-LISTEN, IP-DATAGRAM</p>
<dt><tt>UDP4-DATAGRAM:&lt;address&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP-DATAGRAM, but only supports IPv4 protocol (example1, example2).<br />
 Option groups: FD,SOCKET,IP4, RANGE</p>
<dt><tt>UDP6-DATAGRAM:&lt;address&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP-DATAGRAM, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6,RANGE</p>
<dt><tt>UDP-LISTEN:&lt;port&gt;</tt></p>
<dd> Waits for a UDP/IP packet arriving on &lt;port&gt; [UDP service] and `connects&#8217; back to sender. The accepted IP version is 4 or the one specified with option pf. Please note that, due to UDP protocol properties, no real connection is established; data has to arrive from the peer first, and no end-of-file condition can be transported. Note that opening this address usually blocks until a client connects.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6<br />
 Useful options: fork, bind, range, pf<br />
 See also: UDP, UDP4-LISTEN, UDP6-LISTEN, TCP-LISTEN</p>
<dt><tt>UDP4-LISTEN:&lt;port&gt;</tt></p>
<dd> Like UDP-LISTEN, but only support IPv4 protocol.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP4 </p>
<dt><tt>UDP6-LISTEN:&lt;port&gt;</tt></p>
<dd> Like UDP-LISTEN, but only support IPv6 protocol.<br />
 Option groups: FD,SOCKET,LISTEN,CHILD,RANGE,IP6 </p>
<dt><tt>UDP-SENDTO:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Communicates with the specified peer socket, defined by &lt;port&gt; [UDP service] on &lt;host&gt; [IP address], using UDP/IP version 4 or 6 depending on address specification, name resolution, or option pf. It sends packets to and receives packets from that peer socket only. This address effectively implements a datagram client. It works well with socat UDP-RECVFROM and UDP-RECV address peers.<br />
 Option groups: FD,SOCKET,IP4,IP6<br />
 Useful options: ttl, tos, bind, sourceport, pf<br />
 See also: UDP4-SENDTO, UDP6-SENDTO, UDP-RECVFROM, UDP-RECV, UDP-CONNECT, UDP-LISTEN, IP-SENDTO</p>
<dt><tt>UDP4-SENDTO:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP-SENDTO, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,IP4</p>
<dt><tt>UDP6-SENDTO:&lt;host&gt;:&lt;port&gt;</tt></p>
<dd> Like UDP-SENDTO, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6</p>
<dt>
<dd>
<dt><tt>UDP-RECVFROM:&lt;port&gt;</tt></p>
<dd> Creates a UDP socket on &lt;port&gt; [UDP service] using UDP/IP version 4 or 6 depending on option pf. It receives one packet from an unspecified peer and may send one or more answer packets to that peer. This mode is particularly useful with fork option where each arriving packet &#8211; from arbitrary peers &#8211; is handled by its own sub process. This allows a behaviour similar to typical UDP based servers like ntpd or named. This address works well with socat UDP-SENDTO address peers.<br />
 Option groups: FD,SOCKET,IP4,IP6,CHILD,RANGE<br />
 Useful options: fork, ttl, tos, bind, sourceport, pf<br />
 See also: UDP4-RECVFROM, UDP6-RECVFROM, UDP-SENDTO, UDP-RECV, UDP-CONNECT, UDP-LISTEN, IP-RECVFROM, UNIX-RECVFROM</p>
<dt><tt>UDP4-RECVFROM:&lt;port&gt;</tt></p>
<dd> Like UDP-RECVFROM, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,IP4,CHILD,RANGE</p>
<dt><tt>UDP6-RECVFROM:&lt;port&gt;</tt></p>
<dd> Like UDP-RECVFROM, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6,CHILD,RANGE</p>
<dt>
<dd>
<dt><tt>UDP-RECV:&lt;port&gt;</tt></p>
<dd> Creates a UDP socket on &lt;port&gt; [UDP service] using UDP/IP version 4 or 6 depending on option pf. It receives packets from multiple unspecified peers and merges the data. No replies are possible. It works well with, e.g., socat UDP-SENDTO address peers; it behaves similar to a syslog server.<br />
 Option groups: FD,SOCKET,IP4,IP6,RANGE<br />
 Useful options: fork, pf, bind, sourceport, ttl, tos<br />
 See also: UDP4-RECV, UDP6-RECV, UDP-SENDTO, UDP-RECVFROM, UDP-CONNECT, UDP-LISTEN, IP-RECV, UNIX-RECV</p>
<dt><tt>UDP4-RECV:&lt;port&gt;</tt></p>
<dd> Like UDP-RECV, but only supports IPv4 protocol.<br />
 Option groups: FD,SOCKET,IP4,RANGE</p>
<dt><tt>UDP6-RECV:&lt;port&gt;</tt></p>
<dd> Like UDP-RECV, but only supports IPv6 protocol.<br />
 Option groups: FD,SOCKET,IP6,RANGE</p>
<dt>
<dd>
<dt><tt>UNIX-CONNECT:&lt;filename&gt;</tt></p>
<dd> Connects to &lt;filename&gt; assuming it is a UNIX domain socket. If &lt;filename&gt; does not exist, this is an error; if &lt;filename&gt; is not a UNIX domain socket, this is an error; if &lt;filename&gt; is a UNIX domain socket, but no process is listening, this is an error.<br />
 Option groups: FD,SOCKET,NAMED,RETRY,UNIX<br />
 ) Useful options: bind<br />
 See also: UNIX-LISTEN, UNIX-SENDTO, TCP</p>
<dt>
<dd>
<dt><tt>UNIX-LISTEN:&lt;filename&gt;</tt></p>
<dd> Listens on &lt;filename&gt; using a UNIX domain stream socket and accepts a connection. If &lt;filename&gt; exists and is not a socket, this is an error. If &lt;filename&gt; exists and is a UNIX domain socket, binding to the address fails (use option unlink-early!). Note that opening this address usually blocks until a client connects. Beginning with socat version 1.4.3, the file system entry is removed when this address is closed (but see option unlink-close) (example).<br />
 Option groups: FD,SOCKET,NAMED,LISTEN,CHILD,RETRY,UNIX<br />
 Useful options: fork, umask, mode, user, group, unlink-early<br />
 See also: UNIX-CONNECT, UNIX-RECVFROM, UNIX-RECV, TCP-LISTEN</p>
<dt>
<dd>
<dt><tt>UNIX-SENDTO:&lt;filename&gt;</tt></p>
<dd> Communicates with the specified peer socket, defined by [&lt;filename&gt;] assuming it is a UNIX domain datagram socket. It sends packets to and receives packets from that peer socket only. Please note that it might be neccessary to bind the local socket to an address (e.g. <tt>/tmp/sock1</tt>, which must not exist before). This address type works well with socat UNIX-RECVFROM and UNIX-RECV address peers.<br />
 Option groups: FD,SOCKET,NAMED,UNIX<br />
 Useful options: bind<br />
 See also: UNIX-RECVFROM, UNIX-RECV, UNIX-CONNECT, UDP-SENDTO, IP-SENDTO</p>
<dt>
<dd>
<dt><tt>UNIX-RECVFROM:&lt;filename&gt;</tt></p>
<dd> Creates a UNIX domain datagram socket [&lt;filename&gt;]. Receives one packet and may send one or more answer packets to that peer. This mode is particularly useful with fork option where each arriving packet &#8211; from arbitrary peers &#8211; is handled by its own sub process. This address works well with socat UNIX-SENDTO address peers.<br />
 Option groups: FD,SOCKET,NAMED,CHILD,UNIX<br />
 Useful options: fork<br />
 See also: UNIX-SENDTO, UNIX-RECV, UNIX-LISTEN, UDP-RECVFROM, IP-RECVFROM</p>
<dt>
<dd>
<dt><tt>UNIX-RECV:&lt;filename&gt;</tt></p>
<dd> Creates a UNIX domain datagram socket [&lt;filename&gt;]. Receives packets from multiple unspecified peers and merges the data. No replies are possible. It can be, e.g., addressed by socat UNIX-SENDTO address peers. It behaves similar to a syslog server. Option groups: FD,SOCKET,NAMED,UNIX<br />
 See also: UNIX-SENDTO, UNIX-RECVFROM, UNIX-LISTEN, UDP-RECV, IP-RECV</p>
<dt>
<dd>
<dt><tt>UNIX-CLIENT:&lt;filename&gt;</tt></p>
<dd> Communicates with the specified peer socket, defined by [&lt;filename&gt;] assuming it is a UNIX domain socket. It first tries to connect and, if that fails, assumes it is a datagram socket, thus supporting both types.<br />
 Option groups: FD,SOCKET,NAMED,UNIX<br />
 Useful options: bind<br />
 See also: UNIX-CONNECT, UNIX-SENDTO, GOPEN</p>
<dt>
<dd>
<dt><tt>ABSTRACT-CONNECT:&lt;string&gt;</tt></p>
<dd>
<dt><tt>ABSTRACT-LISTEN:&lt;string&gt;</tt></p>
<dd>
<dt><tt>ABSTRACT-SENDTO:&lt;string&gt;</tt></p>
<dd>
<dt><tt>ABSTRACT-RECVFROM:&lt;string&gt;</tt></p>
<dd>
<dt><tt>ABSTRACT-RECV:&lt;string&gt;</tt></p>
<dd>
<dt><tt>ABSTRACT-CLIENT:&lt;string&gt;</tt></p>
<dd> The ABSTRACT addresses are almost identical to the related UNIX addresses except that they do not address file system based sockets but an alternate UNIX domain address space. To archieve this the socket address strings are prefixed with &quot;
