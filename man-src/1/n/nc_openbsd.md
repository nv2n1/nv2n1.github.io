---
title: "nc_openbsd(1)"
name: "nc_openbsd"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nc_openbsd/"
description: "nc – arbitrary TCP and UDP connections and listens"
---

<h2 class="name">NAME</h2>
<p> <code>nc</code> &#8211; arbitrary TCP and UDP connections and listens </p>
<h2>SYNOPSIS</h2>
<p> <code>nc</code> [-<code>46bCDdFhklNnrStUuvZz </code>[-<code>I </code><i>length</i> ] ] [-<code>i </code><i>interval</i> ] [-<code>M </code><i>ttl</i> ] [-<code>m </code><i>minttl</i> ] [-<code>O </code><i>length</i> ] [-<code>P </code><i>proxy_username</i> ] [-<code>p </code><i>source_port</i> ] [-<code>q </code><i>seconds</i> ] [-<code>s </code><i>sourceaddr</i> ] [-<code>T </code><i>keyword</i> ] [-<code>V </code><i>rtable</i> ] [-<code>W </code><i>recvlimit</i> ] [-<code>w </code><i>timeout</i> ] [-<code>X </code><i>proxy_protocol</i> ] [-<code>x </code><i>proxy_address </i>[: <i>port</i> ] ] [<i>destination</i> ] [<i>port</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>nc</code> (or <code>netcat</code> utility is used for just about anything under the sun involving TCP, UDP, or UNIX sockets. It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning, and deal with both IPv4 and IPv6. Unlike <a href="/docs/linux/man/1-telnet/">telnet</a>(1), <code>nc</code> scripts nicely, and separates error messages onto standard error instead of sending them to standard output, as <a href="/docs/linux/man/1-telnet/">telnet</a>(1) does with some. </p>
<p> Common uses include: </p>
<ul>
<li> simple TCP proxies
<li> shell-script based HTTP clients and servers
<li> network daemon testing
<li> a SOCKS or HTTP ProxyCommand for <a href="/docs/linux/man/1-ssh/">ssh</a>(1)
<li> and much, much more </ul>
<p> The options are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd> Use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Use IPv6 addresses only.</p>
<dt><code>-b</code></p>
<dd> Allow broadcast.</p>
<dt><code>-C</code></p>
<dd> Send CRLF as line-ending. Each line feed (LF) character from the input data is translated into CR+LF before being written to the socket. Line feed characters that are already preceded with a carriage return (CR) are not translated. Received data is not affected.</p>
<dt><code>-D</code></p>
<dd> Enable debugging on the socket.</p>
<dt><code>-d</code></p>
<dd> Do not attempt to read from stdin.</p>
<dt><code>-F</code></p>
<dd> Pass the first connected socket using <a href="/docs/linux/man/2-sendmsg/">sendmsg</a>(2) to stdout and exit. This is useful in conjunction with &#8211;<code>X</code> to have <code>nc</code> perform connection setup with a proxy but then leave the rest of the connection to another program (e.g. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) using the ssh_config5 <code>ProxyUseFdpass</code> option). Cannot be used with &#8211;<code>U</code></p>
<dt><code>-h</code></p>
<dd> Print out the <code>nc</code> help text and exit.</p>
<dt><code>-I </code><i>length</i></p>
<dd> Specify the size of the TCP receive buffer.</p>
<dt><code>-i </code><i>interval</i></p>
<dd> Sleep for <i>interval</i> seconds between lines of text sent and received. Also causes a delay time between connections to multiple ports.</p>
<dt><code>-k</code></p>
<dd> When a connection is completed, listen for another one. Requires &#8211;<code>l</code> When used together with the &#8211;<code>u</code> option, the server socket is not connected and it can receive UDP datagrams from multiple hosts.</p>
<dt><code>-l</code></p>
<dd> Listen for an incoming connection rather than initiating a connection to a remote host. The <i>destination</i> and <i>port</i> to listen on can be specified either as non-optional arguments, or with options &#8211;<code>s</code> and &#8211;<code>p</code> respectively. Cannot be used together with &#8211;<code>x</code> or &#8211;<code>z</code> Additionally, any timeouts specified with the &#8211;<code>w</code> option are ignored.</p>
<dt><code>-M </code><i>ttl</i></p>
<dd> Set the TTL / hop limit of outgoing packets.</p>
<dt><code>-m </code><i>minttl</i></p>
<dd> Ask the kernel to drop incoming packets whose TTL / hop limit is under <i>minttl</i></p>
<dt><code>-N</code></p>
<dd> <a href="/docs/linux/man/2-shutdown/">shutdown</a>(2) the network socket after EOF on the input. Some servers require this to finish their work.</p>
<dt><code>-n</code></p>
<dd> Do not perform domain name resolution. If a name cannot be resolved without DNS, an error will be reported.</p>
<dt><code>-O </code><i>length</i></p>
<dd> Specify the size of the TCP send buffer.</p>
<dt><code>-P </code><i>proxy_username</i></p>
<dd> Specifies a username to present to a proxy server that requires authentication. If no username is specified then authentication will not be attempted. Proxy authentication is only supported for HTTP CONNECT proxies at present.</p>
<dt><code>-p </code><i>source_port</i></p>
<dd> Specify the source port <code>nc</code> should use, subject to privilege restrictions and availability.</p>
<dt><code>-q </code><i>seconds</i></p>
<dd> after EOF on stdin, wait the specified number of <i>seconds</i> and then quit. If <i>seconds</i> is negative, wait forever (default). Specifying a non-negative <i>seconds</i> implies &#8211;<code>N</code></p>
<dt><code>-r</code></p>
<dd> Choose source and/or destination ports randomly instead of sequentially within a range or in the order that the system assigns them.</p>
<dt><code>-S</code></p>
<dd> Enable the RFC 2385 TCP MD5 signature option.</p>
<dt><code>-s </code><i>sourceaddr</i></p>
<dd> Set the source address to send packets from, which is useful on machines with multiple interfaces. For UNIX datagram sockets, specifies the local temporary socket file to create and use so that datagrams can be received. Cannot be used together with &#8211;<code>x</code></p>
<dt><code>-T </code><i>keyword</i></p>
<dd> Change the IPv4 TOS/IPv6 traffic class value. <i>keyword</i> may be one of <code>critical</code> <code>inetcontrol</code> <code>lowcost</code> <code>lowdelay</code> <code>netcontrol</code> <code>throughput</code> <code>reliability</code> or one of the DiffServ Code Points: <code>ef</code> <code>af11 &#8230; af43</code> <code>cs0 &#8230; cs7</code> or a number in either hex or decimal.</p>
<dt><code>-t</code></p>
<dd> Send RFC 854 DON&#8217;T and WON&#8217;T responses to RFC 854 DO and WILL requests. This makes it possible to use <code>nc</code> to script telnet sessions.</p>
<dt><code>-U</code></p>
<dd> Use UNIX sockets. Cannot be used together with &#8211;<code>F</code> or &#8211;<code>x</code></p>
<dt><code>-u</code></p>
<dd> Use UDP instead of TCP. Cannot be used together with &#8211;<code>x</code> For UNIX sockets, use a datagram socket instead of a stream socket. If a UNIX socket is used, a temporary receiving socket is created in /tmp unless the &#8211;<code>s</code> flag is given.</p>
<dt><code>-V </code><i>rtable</i></p>
<dd> Set the routing table to be used.</p>
<dt><code>-v</code></p>
<dd> Produce more verbose output.</p>
<dt><code>-W </code><i>recvlimit</i></p>
<dd> Terminate after receiving <i>recvlimit</i> packets from the network.</p>
<dt><code>-w </code><i>timeout</i></p>
<dd> Connections which cannot be established or are idle timeout after <i>timeout</i> seconds. The &#8211;<code>w</code> flag has no effect on the &#8211;<code>l</code> option, i.e. <code>nc</code> will listen forever for a connection, with or without the &#8211;<code>w</code> flag. The default is no timeout.</p>
<dt><code>-X </code><i>proxy_protocol</i></p>
<dd> Use <i>proxy_protocol</i> when talking to the proxy server. Supported protocols are <code>4</code> (SOCKS v.4), <code>5</code> (SOCKS v.5) and <code>connect</code> (HTTPS proxy). If the protocol is not specified, SOCKS version 5 is used.</p>
<dt><code>-x </code><i>proxy_address </i>[: <i>port</i> ]</p>
<dd> Connect to <i>destination</i> using a proxy at <i>proxy_address</i> and <i>port</i> If <i>port</i> is not specified, the well-known port for the proxy protocol is used (1080 for SOCKS, 3128 for HTTPS). An IPv6 address can be specified unambiguously by enclosing <i>proxy_address</i> in square brackets. A proxy cannot be used with any of the options &#8211;<code>lsuU</code></p>
<dt><code>-Z</code></p>
<dd> DCCP mode.</p>
<dt><code>-z</code></p>
<dd> Only scan for listening daemons, without sending any data to them. Cannot be used together with &#8211;<code>l</code></dl>
<p> <i>destination</i> can be a numerical IP address or a symbolic hostname (unless the &#8211;<code>n</code> option is given). In general, a destination must be specified, unless the &#8211;<code>l</code> option is given (in which case the local host is used). For UNIX sockets, a destination is required and is the socket path to connect to (or listen on if the &#8211;<code>l</code> option is given). </p>
<p> <i>port</i> can be specified as a numeric port number or as a service name. Port ranges may be specified as numeric port numbers of the form <i>nn </i><code>&#8211; </code><i>mm</i> In general, a destination port must be specified, unless the &#8211;<code>U</code> option is given.</p>
<h2>CLIENT/SERVER MODEL</h2>
<p> It is quite simple to build a very basic client/server model using <code>nc.</code> On one console, start <code>nc</code> listening on a specific port for a connection. For example: </p>
<blockquote><p><tt>$ nc -l 1234</tt></p></blockquote>
<p> <code>nc</code> is now listening on port 1234 for a connection. On a second console (or a second machine) connect to the machine and port being listened on: </p>
<blockquote><p><tt>$ nc -N 127.0.0.1 1234</tt></p></blockquote>
<p> There should now be a connection between the ports. Anything typed at the second console will be concatenated to the first, and vice-versa. After the connection has been set up, <code>nc</code> does not really care which side is being used as a `server&#8217; and which side is being used as a `client&#8217; The connection may be terminated using an <code>EOF</code> (`^D&#8217; ) as the &#8211;<code>N</code> flag was given. </p>
<p> There is no &#8211;<code>c</code> or &#8211;<code>e</code> option in this netcat, but you still can execute a command after connection being established by redirecting file descriptors. Be cautious here because opening a port and let anyone connected execute arbitrary command on your site is DANGEROUS. If you really need to do this, here is an example: </p>
<p> On `server&#8217; side: </p>
<blockquote><p><tt>$ rm -f /tmp/f; mkfifo /tmp/f</tt></p></blockquote>
<blockquote><p><tt>$ cat /tmp/f | /bin/sh -i 2&gt;&amp;1 | nc -l 127.0.0.1 1234 &gt; /tmp/f</tt></p></blockquote>
<p> On `client&#8217; side: </p>
<blockquote><p><tt>$ nc host.example.com 1234</tt></p></blockquote>
<blockquote><p><tt>$ (shell prompt from host.example.com)</tt></p></blockquote>
<p> By doing this, you create a fifo at /tmp/f and make nc listen at port 1234 of address 127.0.0.1 on `server&#8217; side, when a `client&#8217; establishes a connection successfully to that port, /bin/sh gets executed on `server&#8217; side and the shell prompt is given to `client&#8217; side. </p>
<p> When connection is terminated, <code>nc</code> quits as well. Use &#8211;<code>k</code> if you want it keep listening, but if the command quits this option won&#8217;t restart it or keep <code>nc</code> running. Also don&#8217;t forget to remove the file descriptor once you don&#8217;t need it anymore: </p>
<blockquote><p><tt>$ rm -f /tmp/f</tt></p></blockquote>
<h2>DATA TRANSFER</h2>
<p> The example in the previous section can be expanded to build a basic data transfer model. Any information input into one end of the connection will be output to the other end, and input and output can be easily captured in order to emulate file transfer. </p>
<p> Start by using <code>nc</code> to listen on a specific port, with output captured into a file: </p>
<blockquote><p><tt>$ nc -l 1234 &gt; filename.out</tt></p></blockquote>
<p> Using a second machine, connect to the listening <code>nc</code> process, feeding it the file which is to be transferred: </p>
<blockquote><p><tt>$ nc -N host.example.com 1234 &lt; filename.in</tt></p></blockquote>
<p> After the file has been transferred, the connection will close automatically.</p>
<h2>TALKING TO SERVERS</h2>
<p> It is sometimes useful to talk to servers &#8220;by hand&#8221; rather than through a user interface. It can aid in troubleshooting, when it might be necessary to verify what data a server is sending in response to commands issued by the client. For example, to retrieve the home page of a web site: </p>
<blockquote>
<pre>
$ printf &quot;GET / HTTP/1.0

&quot; | nc host.example.com 80
</pre>
</blockquote>
<p> Note that this also displays the headers sent by the web server. They can be filtered, using a tool such as <a href="/docs/linux/man/1-sed/">sed</a>(1), if necessary. </p>
<p> More complicated examples can be built up when the user knows the format of requests required by the server. As another example, an email may be submitted to an SMTP server using: </p>
<blockquote>
<pre><code>
$ nc[-C] localhost 25 &lt;&lt; EOF
                             HELO host.example.com
                                 MAIL FROM : &lt;user[at] host.example.com&gt;
                                                 RCPT TO : &lt;user2[at] host.example.com&gt;
                                                               DATA
                                                                   Body of email.
                                                                       .QUIT
                                                                           EOF
</code></pre>
</blockquote>
<h2>PORT SCANNING</h2>
<p> It may be useful to know which ports are open and running services on a target machine. The &#8211;<code>z</code> flag can be used to tell <code>nc</code> to report open ports, rather than initiate a connection. Usually it&#8217;s useful to turn on verbose output to stderr by use this option in conjunction with &#8211;<code>v</code> option. </p>
<p> For example: </p>
<blockquote>
<pre><code>
$ nc - zv host.example.com 20 - 30 Connection to host.example.com 22 port[tcp / ssh] succeeded !Connection to host.example.com 25 port[tcp / smtp] succeeded !
</code></pre>
</blockquote>
<p> The port range was specified to limit the search to ports 20 &#8211; 30, and is scanned by increasing order (unless the &#8211;<code>r</code> flag is set). </p>
<p> You can also specify a list of ports to scan, for example: </p>
<blockquote>
<pre>
$ nc -zv host.example.com http 20 22-23
nc: connect to host.example.com 80 (tcp) failed: Connection refused
nc: connect to host.example.com 20 (tcp) failed: Connection refused
Connection to host.example.com port [tcp/ssh] succeeded!
nc: connect to host.example.com 23 (tcp) failed: Connection refused
</pre>
</blockquote>
<p> The ports are scanned by the order you given (unless the &#8211;<code>r</code> flag is set). </p>
<p> Alternatively, it might be useful to know which server software is running, and which versions. This information is often contained within the greeting banners. In order to retrieve these, it is necessary to first make a connection, and then break the connection when the banner has been retrieved. This can be accomplished by specifying a small timeout with the &#8211;<code>w</code> flag, or perhaps by issuing a Qq Dv QUIT command to the server: </p>
<blockquote>
<pre>
$ echo &quot;QUIT&quot; | nc host.example.com 20-30
SSH-1.99-OpenSSH_3.6.1p2
Protocol mismatch.
220 host.example.com IMS SMTP Receiver Version 0.84 Ready
</pre>
</blockquote>
<h2>EXAMPLES</h2>
<p> Open a TCP connection to port 42 of host.example.com, using port 31337 as the source port, with a timeout of 5 seconds: </p>
<blockquote><p><tt>$ nc -p 31337 -w 5 host.example.com 42</tt></p></blockquote>
<p> Open a UDP connection to port 53 of host.example.com: </p>
<blockquote><p><tt>$ nc -u host.example.com 53</tt></p></blockquote>
<p> Open a TCP connection to port 42 of host.example.com using 10.1.2.3 as the IP for the local end of the connection: </p>
<blockquote><p><tt>$ nc -s 10.1.2.3 host.example.com 42</tt></p></blockquote>
<p> Create and listen on a UNIX stream socket: </p>
<blockquote><p><tt>$ nc -lU /var/tmp/dsocket</tt></p></blockquote>
<p> Connect to port 42 of host.example.com via an HTTP proxy at 10.2.3.4, port 8080. This example could also be used by <a href="/docs/linux/man/1-ssh/">ssh</a>(1); see the <code>ProxyCommand</code> directive in ssh_config5 for more information. </p>
<blockquote><p><tt>$ nc -x10.2.3.4:8080 -Xconnect host.example.com 42</tt></p></blockquote>
<p> The same example again, this time enabling proxy authentication with username &#8220;ruser&#8221; if the proxy requires it: </p>
<blockquote><p><tt>$ nc -x10.2.3.4:8080 -Xconnect -Pruser host.example.com 42</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cat/">cat</a>(1), <a href="/docs/linux/man/1-ssh/">ssh</a>(1)</p>
<h2>AUTHORS</h2>
<p> Original implementation by An *Hobbit* Aq Mt hobbit [at] avian.org .<br />
 Rewritten with IPv6 support by An Eric Jackson Aq Mt ericj [at] monkey.org .<br />
 Modified for Debian port by Aron Xu Aq aron [at] debian.org .</p>
<h2>CAVEATS</h2>
<p> UDP port scans using the &#8211;<code>uz</code> combination of flags will always report success irrespective of the target machine&#8217;s state. However, in conjunction with a traffic sniffer either on the target machine or an intermediary device, the &#8211;<code>uz</code> combination could be useful for communications diagnostics. Note that the amount of UDP traffic generated may be limited either due to hardware resources and/or configuration settings. </p>
<h2>Index</h2>
