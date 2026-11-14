---
title: "iperf3(1)"
name: "iperf3"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iperf3/"
description: "iperf3 – perform network throughput tests"
---

<h2>NAME</h2>
<p> iperf3 &#8211; perform network throughput tests</p>
<h2>SYNOPSIS</h2>
<p> <code>iperf3 -s [</code> <i>options</i> <code>]</code><br />
 <code>iperf3 -c </code> <i>server</i> <code>[</code> <i>options</i> <code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> iperf3 is a tool for performing network throughput measurements. It can test either TCP or UDP throughput. To perform an iperf3 test the user must establish both a server and a client. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code> <i>n</i></p>
<dd> set server port to listen on/connect to to <i>n</i> (default 5201)</p>
<dt><code>-f</code>, <code>&#8211;format</code></p>
<dd> [kmKM] format to report: Kbits, Mbits, KBytes, MBytes</p>
<dt><code>-i</code>, <code>&#8211;interval</code> <i>n</i></p>
<dd> pause <i>n</i> seconds between periodic bandwidth reports; default is 1, use 0 to disable</p>
<dt><code>-F</code>, <code>&#8211;file</code> <i>name</i></p>
<dd> client-side: read from the file and write to the network, instead of using random data; server-side: read from the network and write to the file, instead of throwing the data away</p>
<dt><code>-A</code>, <code>&#8211;affinity</code> <i>n/n,m</i></p>
<dd> Set the CPU affinity, if possible (Linux and FreeBSD only). On both the client and server you can set the local affinity by using the <i>n</i> form of this argument (where <i>n</i> is a CPU number). In addition, on the client side you can override the server&#8217;s affinity for just that one test, using the <i>n,m</i> form of argument. Note that when using this feature, a process will only be bound to a single CPU (as opposed to a set containing potentialy multiple CPUs).</p>
<dt><code>-B</code>, <code>&#8211;bind</code> <i>host</i></p>
<dd> bind to a specific interface</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> give more detailed output</p>
<dt><code>-J</code>, <code>&#8211;json</code></p>
<dd> output in JSON format</p>
<dt><code>&#8211;logfile</code> <i>file</i></p>
<dd> send output to a log file.</p>
<dt><code>&#8211;forceflush</code></p>
<dd> force flushing output at every interval. Used to avoid buffering when sending output to pipe.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> emit debugging output. Primarily (perhaps exclusively) of use to developers.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show version information and quit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show a help synopsis </p>
</dl>
<h2>SERVER SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code></p>
<dd> run in server mode</p>
<dt><code>-D</code>, <code>&#8211;daemon</code></p>
<dd> run the server in background as a daemon</p>
<dt><code>-I</code>, <code>&#8211;pidfile</code> <i>file</i></p>
<dd> write a file with the process ID, most useful when running as a daemon.</p>
<dt><code>-1</code>, <code>&#8211;one-off</code></p>
<dd> handle one client connection, then exit. </p>
</dl>
<h2>CLIENT SPECIFIC OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;client</code> <i>host</i></p>
<dd> run in client mode, connecting to the specified server</p>
<dt><code>&#8211;sctp</code></p>
<dd> use SCTP rather than TCP (FreeBSD and Linux)</p>
<dt><code>-u</code>, <code>&#8211;udp</code></p>
<dd> use UDP rather than TCP</p>
<dt><code>-b</code>, <code>&#8211;bandwidth</code> <i>n</i>[KM]</p>
<dd> set target bandwidth to <i>n</i> bits/sec (default 1 Mbit/sec for UDP, unlimited for TCP). If there are multiple streams (-P flag), the bandwidth limit is applied separately to each stream. You can also add a &#8216;/&#8217; and a number to the bandwidth specifier. This is called &quot;burst mode&quot;. It will send the given number of packets without pausing, even if that temporarily exceeds the specified bandwidth limit. Setting the target bandwidth to 0 will disable bandwidth limits (particularly useful for UDP tests). This bandwidth limit is implemented internally inside iperf3, and is available on all platforms. Compare with the &#8211;fq-rate flag.</p>
<dt><code>&#8211;fq-rate</code> <i>n</i>[KM]</p>
<dd> Set a rate to be used with fair-queueing based socket-level pacing, in bits per second. This pacing (if specified) will be in addition to any pacing due to iperf3&#8217;s internal bandwidth pacing (-b flag), and both can be specified for the same test. Only available on platforms supporting the SO_MAX_PACING_RATE socket option (currently only Linux). The default is no fair-queueing based pacing.</p>
<dt><code>&#8211;no-fq-socket-pacing</code></p>
<dd> This option is deprecated and will be removed. It is equivalent to specifying &#8211;fq-rate=0.</p>
<dt><code>-t</code>, <code>&#8211;time</code> <i>n</i></p>
<dd> time in seconds to transmit for (default 10 secs)</p>
<dt><code>-n</code>, <code>&#8211;bytes</code> <i>n</i>[KM]</p>
<dd> number of bytes to transmit (instead of -t)</p>
<dt><code>-k</code>, <code>&#8211;blockcount</code> <i>n</i>[KM]</p>
<dd> number of blocks (packets) to transmit (instead of -t or -n)</p>
<dt><code>-l</code>, <code>&#8211;length</code> <i>n</i>[KM]</p>
<dd> length of buffer to read or write. For TCP tests, the default value is 128KB. In the case of UDP, iperf3 tries to dynamically determine a reasonable sending size based on the path MTU; if that cannot be determined it uses 1460 bytes as a sending size. For SCTP tests, the default size is 64KB.</p>
<dt><code>&#8211;cport</code> <i>port</i></p>
<dd> bind data streams to a specific client port (for TCP and UDP only, default is to use an ephemeral port)</p>
<dt><code>-P</code>, <code>&#8211;parallel</code> <i>n</i></p>
<dd> number of parallel client streams to run</p>
<dt><code>-R</code>, <code>&#8211;reverse</code></p>
<dd> run in reverse mode (server sends, client receives)</p>
<dt><code>-w</code>, <code>&#8211;window</code> <i>n</i>[KM]</p>
<dd> window size / socket buffer size (this gets sent to the server and used on that side too)</p>
<dt><code>-M</code>, <code>&#8211;set-mss</code> <i>n</i></p>
<dd> set TCP/SCTP maximum segment size (MTU &#8211; 40 bytes)</p>
<dt><code>-N</code>, <code>&#8211;no-delay</code></p>
<dd> set TCP/SCTP no delay, disabling Nagle&#8217;s Algorithm</p>
<dt><code>-4</code>, <code>&#8211;version4</code></p>
<dd> only use IPv4</p>
<dt><code>-6</code>, <code>&#8211;version6</code></p>
<dd> only use IPv6</p>
<dt><code>-S</code>, <code>&#8211;tos</code> <i>n</i></p>
<dd> set the IP &#8216;type of service&#8217;</p>
<dt><code>-L</code>, <code>&#8211;flowlabel</code> <i>n</i></p>
<dd> set the IPv6 flow label (currently only supported on Linux)</p>
<dt><code>-X</code>, <code>&#8211;xbind</code> <i>name</i></p>
<dd> Bind SCTP associations to a specific subset of links using <a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a>(3). The <code>&#8211;B</code> flag will be ignored if this flag is specified. Normally SCTP will include the protocol addresses of all active links on the local host when setting up an association. Specifying at least one <code>&#8211;X</code> name will disable this behaviour. This flag must be specified for each link to be included in the association, and is supported for both iperf servers and clients (the latter are supported by passing the first <code>&#8211;X</code> argument to <a href="/docs/linux/man/2-bind/">bind</a>(2)). Hostnames are accepted as arguments and are resolved using <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3). If the <code>&#8211;4</code> or <code>&#8211;6</code> flags are specified, names which do not resolve to addresses within the specified protocol family will be ignored.</p>
<dt><code>&#8211;nstreams</code> <i>n</i></p>
<dd> Set number of SCTP streams.</p>
<dt><code>-Z</code>, <code>&#8211;zerocopy</code></p>
<dd> Use a &quot;zero copy&quot; method of sending data, such as <a href="/docs/linux/man/2-sendfile/">sendfile</a>(2), instead of the usual <a href="/docs/linux/man/2-write/">write</a>(2).</p>
<dt><code>-O</code>, <code>&#8211;omit</code> <i>n</i></p>
<dd> Omit the first n seconds of the test, to skip past the TCP slow-start period.</p>
<dt><code>-T</code>, <code>&#8211;title</code> <i>str</i></p>
<dd> Prefix every output line with this string.</p>
<dt><code>-C</code>, <code>&#8211;congestion</code> <i>algo</i></p>
<dd> Set the congestion control algorithm (Linux and FreeBSD only). An older <code>&#8211;linux-congestion</code> synonym for this flag is accepted but is deprecated.</p>
<dt><code>&#8211;get-server-output</code></p>
<dd> Get the output from the server. The output format is determined by the server (in particular, if the server was invoked with the <code>&#8211;json</code> flag, the output will be in JSON format, otherwise it will be in human-readable format). If the client is run with <code>&#8211;json</code>, the server output is included in a JSON object; otherwise it is appended at the bottom of the human-readable output. </p>
</dl>
<h2>AUTHORS</h2>
<p> A list of the contributors to iperf3 can be found within the documentation located at <a rel="nofollow" href="http://software.es.net/iperf/dev.html#authors.">http://software.es.net/iperf/dev.html#authors.</a> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-libiperf/">libiperf</a>(3), <a rel="nofollow" href="http://software.es.net/iperf">http://software.es.net/iperf</a> </p>
<h2>Index</h2>
