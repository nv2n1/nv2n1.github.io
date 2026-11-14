---
title: "nc6(1)"
name: "nc6"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nc6/"
description: "nc6 – network swiss army knife"
---

<h2>NAME</h2>
<p> nc6 &#8211; network swiss army knife</p>
<h2>SYNOPSIS</h2>
<p> <code>nc6</code> <i>[options&#8230;] hostname port</i><br />
 <code>nc6</code> <i>-l -p port [-s addr] [options&#8230;] [hostname] [port]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>netcat6</code> is a simple unix utility which reads and writes data across network connections, using the TCP or UDP protocol over IPv4 or IPv6 networks. It is designed to be a reliable &quot;back-end&quot; tool that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and exploration tool, since it can create almost any kind of connection you would need and has several interesting built-in capabilities. <code>netcat6</code> , or <code>nc6</code> as the actual program is named, should have been supplied long ago as another one of those cryptic but standard Unix tools. In the simplest usage, &quot; <code>nc6 host port</code> &quot; creates a TCP connection to the given port on the given target host. Your standard input is then sent to the host, and anything that comes back across the connection is sent to your standard output. This continues indefinitely, until the network side of the connection shuts down. Note that this behavior is different from most other applications which shut everything down and exit after an end-of-file on the standard input (though this style of operation can easily be enabled). netcat6 can also function as a server, by listening for inbound connections on arbitrary ports and then doing the same reading and writing. With minor limitations, netcat6 doesn&#8217;t really care if it runs in &quot;client&quot; or &quot;server&quot; mode &#8212; it still shovels data back and forth until there isn&#8217;t any more left. In this manual page, these two working modes are referred as &quot;connect mode&quot; and &quot;listen mode&quot;, respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-4</i></p>
<dd> Forces the use of IPv4.</p>
<dt><i>-6</i></p>
<dd> Forces the use of IPv6 and inhibits the use IPV4-mapped addresses.</p>
<dt><i>-b, &#8211;bluetooth</i></p>
<dd> With this option set, netcat6 will use bluetooth to establish connections. By default the L2CAP protocol will be used (also see &#8216;&#8211;sco&#8217;).</p>
<dt><i>&#8211;buffer-size=BYTES</i></p>
<dd> Set the buffer size for the local and remote endpoints. netcat6 does all reads into these buffers, so they should be large enough to minimize excessive reads from the socket and in UDP mode it should be large enough to receive an entire datagram (also see &#8216;&#8211;nru&#8217;). By default, the buffer size is 8 kilobytes for TCP connections and 128 kilobytes for UDP.</p>
<dt><i>&#8211;continuous</i></p>
<dd> Enable continuous accepting of connections in listen mode, like inetd. Must be used with &#8211;exec to specify the command to run locally (try &#8216;nc6 &#8211;continuous &#8211;exec cat -l -p &lt;port&gt;&#8217; to make a simple echo server).</p>
<dt><i>&#8211;disable-nagle</i></p>
<dd> Disable the use of the Nagle algorithm for TCP connections (see &quot;NAGLE ALGORITHM&quot;).</p>
<dt><i>-e, &#8211;exec=CMD</i></p>
<dd> Exec the listed CMD after a connect is established. All input from the remote client will be available on stdin to the command, and all output from the command will be sent back to the remote client.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Display a brief help listing.</p>
<dt><i>&#8211;half-close</i></p>
<dd> Properly handle (and send) TCP half closes for protocols that support them (eg. TCP). See &quot;HALF CLOSE&quot;.</p>
<dt><i>-l, &#8211;listen</i></p>
<dd> Selects listen mode (for inbound connects).</p>
<dt><i>&#8211;mtu=BYTES</i></p>
<dd> Set the Maximum Transmission Unit for the remote endpoint (network transmits). This is only really useful for datagram protocols like UDP. For TCP the MTU is determined by the kernel and this will only affect the amount that is passed to the kernel at any one time. There is no default MTU for TCP connections (and there should be no need to change this), and for UDP it is 8 kilobytes.</p>
<dt><i>-n</i></p>
<dd> Disables DNS queries &#8211; you&#8217;ll have to use numeric IP address instead of hostnames.</p>
<dt><i>&#8211;no-reuseaddr</i></p>
<dd> Disables the SO_REUSEADDR socket option (this is only useful in listen mode).</p>
<dt><i>&#8211;nru=BYTES</i></p>
<dd> Set the miNimum Receive Unit for the remote endpoint (network receives). Note that this does not mean that every network read will get the specified number of bytes, only that nc6 MUST be able to receive at least that amount of data when a read is done. This is only really useful for datagram protocols like UDP where the entire datagram must be received in one call or it is truncated. The default NRU for TCP connections is 1 byte, and 65536 bytes for UDP.</p>
<dt><i>-p, &#8211;port=PORT</i></p>
<dd> Sets the port number for the local endpoint of the connection.</p>
<dt><i>-q, &#8211;hold-timeout=SEC1[:SEC2]</i></p>
<dd> Sets the hold timeout(s) (see &quot;TIMEOUTS&quot;). Specifying just one value will set the hold timeout on the local endpoint, specifying a second value will set the hold timeout on the remote endpoint as well. Either value can be &#8216;0&#8217; (for instant timeout) or &#8216;-&#8216; (for no hold timeout, eg. infinite hold).</p>
<dt><i>-t, &#8211;idle-timeout=SEC</i></p>
<dd> Sets the idle timeout (see &quot;TIMEOUTS&quot;).</p>
<dt><i>&#8211;rcvbuf-size=SIZE</i></p>
<dd> Specify the size to be used for the kernel receive buffer for network sockets.</p>
<dt><i>&#8211;recv-only</i></p>
<dd> Only receive data, don&#8217;t transmit. This also disables any hold timeouts.</p>
<dt><i>-s, &#8211;address=ADDRESS</i></p>
<dd> Sets the source address for the local endpoint of the connection.</p>
<dt><i>&#8211;sco</i></p>
<dd> With this option set, netcat6 with use SCO over bluetooth (note that &#8216;-b&#8217; or &#8216;&#8211;bluetooth&#8217; must also be specified).</p>
<dt><i>&#8211;send-only</i></p>
<dd> Only send data, don&#8217;t receive. This also disables any hold timeouts.</p>
<dt><i>&#8211;sndbuf-size=SIZE</i></p>
<dd> Specify the size to be used for the kernel send buffer for network sockets.</p>
<dt><i>-u, &#8211;udp</i></p>
<dd> With this option set, netcat6 will use UDP as the transport protocol (TCP is the default).</p>
<dt><i>-v</i></p>
<dd> Enable verbose mode. This gives some basic information about what netcat6 is doing. Use it twice for extra verbosity.</p>
<dt><i>&#8211;version</i></p>
<dd> Print netcat6 version and exit.</p>
<dt><i>-w, &#8211;timeout=SECONDS</i></p>
<dd> Timeout for network connects and accepts (see &quot;TIMEOUTS&quot;).</p>
<dt><i>-x, &#8211;transfer</i></p>
<dd> File transfer mode (see &quot;FILE TRANSFER&quot;). If listen mode is specified, this is equivalent to &quot;&#8211;recv-only &#8211;buffer-size=65536&quot; otherwise it is equivalent to &quot;&#8211;send-only &#8211;buffer-size=65536&quot;. <i>-X, &#8211;rev-transfer</i> Reverse file transfer mode (see &quot;FILE TRANSFER&quot;). This transfers in the opposite direction to normal transfer. If listen mode is specified, this is equivalent to &quot;&#8211;send-only &#8211;buffer-size=65536&quot; otherwise it is equivalent to &quot;&#8211;recv-only &#8211;buffer-size=65536&quot;.</dl>
<h2>UDP</h2>
<p> UDP support in netcat6 works very well in both connect and in listen mode. When using UDP in listen mode netcat6 accepts UDP packets from any source that matches the optional address and/or port specified (if it was specified). However, once the first packet is received, netcat6 will only receive packets from that client in future. This is done by putting the UDP socket into &quot;connected&quot; state (see <a href="/docs/linux/man/4-udp/">udp</a>(4) and <a href="/docs/linux/man/2-connect/">connect</a>(2)). Packets from other sources are discarded by the kernel and an ICMP unreachable response is sent. When connecting to a remote host using UDP, nc6 will report that the connection is open regardless of whether a remote server is listening. This is because UDP is a connectionless protocol, and hence no connection establishment is actually required. However, after sending the first packet of data, a server may reply with an ICMP unreachable response causing nc6 to exit with a &#8216;Connection refused&#8217; error message. netcat6 allows for fine control over the buffer sizes, MTU&#8217;s and NRU&#8217;s for the connection, which is especially useful for UDP connections. See the &#8211;buffer-size, &#8211;mtu and &#8211;nru options.</p>
<h2>TIMEOUTS</h2>
<p> netcat6 currently implements a connect/accept timeout, and idle timeout, and hold timeouts on both the remote and local endpoints.</p>
<dl>
<dt>*</p>
<dd> The connect/accept timeout is optional and is specified with the -w or &#8211;timeout option. If a connection cannot be established within the specified time, nc6 will exit with a non-zero exit status. If the option is not specified, nc6 will wait forever when listening for new connections (in listen mode), and will use the standard operating system timeout when trying to connect to remote systems. Note that the connect timeout is essentially ignored when creating UDP connections to a remote server, as UDP is a connectionless protocol.</p>
<dt>*</p>
<dd> The idle timeout is optional and is specified with the -t or &#8211;idle-timeout option. If no data is sent or received from the remote host in the specified time, nc6 will exit with a non-zero exit status. The default is to not timeout idle connections.</p>
<dt>*</p>
<dd> The hold timeouts specify how long the connection should be held open after a given endpoint can no longer be read from (because EOF was received). When the hold timeout occurs for a given endpoint, no more data is read from the opposite endpoint. After data read from the timed out endpoint has been sent, then the connection is closed and nc6 exits.</p>
<dt>
<dd> For example, setting the hold time of the local endpoint to 5 would cause reading from the remote system to stop 5 seconds after stdin is closed (eg. by using ^D to send EOF). All buffered data to be sent to the remote system is then sent, after which nc6 exits successfully (if no errors occurred).</p>
<dt>
<dd> By default, the hold timeout is disabled for the local endpoint (essentially an &#8216;infinite&#8217; timeout), and the hold timeout is set to 0 for the remote endpoint (an &#8216;instant&#8217; timeout). This means that nc6 effectively exits immediately when the read from the remote server is closed.</p>
<dt>
<dd> In half close mode (see &quot;HALF CLOSE&quot;) all hold timeouts are disabled by default.</dl>
<h2>FILE TRANSFER</h2>
<p> netcat6 can be used to transfer files and data streams efficiently, using the &#8216;-x&#8217; or &#8216;&#8211;transfer&#8217; command line option (or the &#8216;-X&#8217; and &#8216;&#8211;rev-transfer&#8217; equivalents for transfer in the opposite direction). For example, to transfer a file from machine &#8216;foo.example.com&#8217; to machine &#8216;bar.example.com&#8217;, one would use the following technique. On &#8216;bar&#8217;, set up a listening nc6 on any local port:</p>
<dl>
<dt>
<dd>
<p> bar$ nc6 -x -l -p 7676 &gt; targetfile </p>
</dl>
<p> Then on &#8216;foo&#8217;, use nc6 to send the file to the listening nc6:</p>
<dl>
<dt>
<dd>
<p> foo$ nc6 -x bar.example.com 7676 &lt; sourcefile </p>
</dl>
<p> You can also use file transfer mode to pipe the output of programs over networks. For example, you can use tar with nc6 to copy entire directories:</p>
<dl>
<dt>
<dd>
<p> bar$ nc6 -x -l -p 7676 | tar xpzf &#8211; </p>
<p> foo$ tar cpzf &#8211; /home | nc6 -x bar.example.com 7676 </p>
</dl>
<p> The &#8216;-x&#8217; or &#8216;&#8211;transfer&#8217; option is just an alias for various other options which set the direction of transfer and increase the buffer sizes used. In listen mode, it is equivalent to &quot;&#8211;recv-only &#8211;buffer-size=65536&quot; otherwise it is equivalent to &quot;&#8211;send-only &#8211;buffer-size=65536&quot;. The normal file transfer mode options assume the file will be sent TO the netcat6 process that is in listen mode, FROM the netcat6 process that is connecting to it. To transfer the other way use the -X or &#8211;rev-transfer options.</p>
<h2>HALF CLOSE</h2>
<p> Stream based data transfers, such as TCP, have 2 separate streams &#8211; the receive and the transmit stream. Contrary to common belief, the streams can be closed independently of each other &#8211; in TCP this is called a half-close. In standard mode, netcat6 closes the entire remote connection when it detects that the remote receive stream has been closed. This is a common operation for most TCP applications, because it is unusual that a server will keep accepting data after it has indicated that it will no longer send any. netcat6 also doesn&#8217;t close it&#8217;s remote transmit when it has no more data to send (eg. when EOF has been received on stdin), so as not to confuse remote servers by making them think that netcat6 isn&#8217;t listening for data any more. However, some servers do make active use of TCP half-closes, and the default operation of netcat6 doesn&#8217;t work well with these services. For example, when using netcat6 to simulate a HTTP server, some HTTP clients close their transmit stream after they send their request. In default mode, netcat6 will close the entire connection before sending the response back to the client. However, by specifying the &quot;&#8211;half-close&quot; option, netcat6 will keep trying to send data to the remote server after the receive stream has closed. It will also close the remote transmit stream when there is no more data to send (EOF has been received on stdin).</p>
<h2>NAGLE ALGORITHM</h2>
<p> Named after its creator, John Nagle, the Nagle algorithm is used to combine together small writes to a TCP stream and thus decrease the number of packets that must be sent out on the network. This was designed as a means for dealing with what Nagle called the small packet problem, created when an application generates data one byte at a time, causing the network to be overloaded with packets. A single character originating from a keyboard could result in the an entire packet (the single byte plus packet headers) being sent onto the network. The algorithm can, under some situations, add a small delay before the data is sent out on the wire &#8211; so as to allow for this concatenation to occur. This is done in such a way that it is generally unnoticeable for normal applications, including interactive applications. There are some situations, such as real-time protocols, that can be adversely affected by this small delay, which is why it is possible to disable the Nagle algorithm on most systems, using the TCP_NODELAY socket option. <code>netcat6</code> provides the &#8216;&#8211;disable-nagle&#8217; command line option to disable the Nagle algorithm for the connection.</p>
<h2>ERRORS</h2>
<p> <code>netcat6</code> attempts to exit cleanly (exit value 0) when all data was sent or received successfully, and to exit with an error value otherwise. However, the specific definition of successfully varies depending on the way nc6 is run. In normal mode, nc6 exits successfully when all data from the remote machine has been received (up to and including an EOF), and the data has been output to the stdout without any errors. It DOES NOT indicate whether all data read from stdin has been successfully sent to the remote machine. In &#8211;half-close mode, nc6 exists successfully when an EOF has been received from both the remote machine AND from stdin, and all data has been successfully sent. Thus the exit status indicates that all data was transfered successfully. If hold timeouts (see &quot;TIMEOUTS&quot;) have been set for either the remote or local endpoint, nc6 will exit successfully if all buffered data from the endpoint that timed out is successfully sent. It DOES NOT indicate whether all data from the opposite endpoint was sent (or even read). For connectionless protocols like UDP there is no way of determining whether the remote system has stopped sending data, or if it will accept further data sent. So in UDP mode, nc6 will either never exit (until interrupted via ctrl-C) or will exit after an error when sending data to the remote system, in which case the exit code is a failure (exit value 1).</p>
<h2>VERSION</h2>
<p> This man page is current for version 1.0 of netcat6</p>
<h2>COPYRIGHT</h2>
<p> GPL.</p>
<h2>AUTHORS</h2>
<p>&nbsp;<wbr>Mauro Tortonesi&nbsp;<wbr>&lt;mauro [at] deepspace6.net&gt;<br />
&nbsp;<wbr>Chris Leishman&nbsp;<wbr>&lt;chris [at] leishman.org&gt; The original netcat was written by a guy we know as the Hobbit &lt;hobbit [at] avian.org&gt;. </p>
<h2>Index</h2>
