---
title: "argus(8)"
name: "argus"
section: "8"
letter: "a"
url: "/docs/linux/man/8-argus/"
description: "argus – audit record generation and utilization system"
---

<p>argus &#8211; audit record generation and utilization system</p>
<h2>Synopsis</h2>
<p><code>argus</code> [ <code>options</code> ] [ <code>filter expression</code> ]</p>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2015 QoSient, LLC All rights reserved.</p>
<h2>Description</h2>
<p> <code>Argus</code> is a data network transaction auditing tool that categorizes and tracks network packets that match the libpcap filter <i>expression</i> into a protocol-specific network flow transaction model. <code>Argus</code> reports on the transactions that it discovers, as periodic network flow data, that is suitable for historical and near real-time processing for forensics, trending and alarm/alerting. Designed to run as a daemon, <code>argus</code> reads packets directly from a network interface, classifies the packets into network transacations and appends the resulting network flow data to a log file or open socket connected to an <code>argus</code> client (such as <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code>). <code>Argus</code> can also read packet information from <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code> , <code><a href="/docs/linux/man/1-snoop/">snoop</a>(1)</code> , <code>NLANR&#8217;s Moat Time Sequence Header</code> or <code>Endaces ERF </code> raw packet files. <code>Argus</code> can also be configured to append its transaction logs to stdout. <code>Argus</code> can provide address based access control for its socket connection facility using <code>tcp_wrappers</code> , and it can provide strong authentication and confidentiality protection using <code>SASL2</code> technology. Refer to package documentation to enable each of these services. </p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Generate application byte metrics in each audit record.</p>
<dt><code>-b</code></p>
<dd>Dump the compiled packet-matching code to stdout and stop. This is used to debug filter expressions.</p>
<dt><code>-B</code></p>
<dd>&lt;addr&gt; Specify the bind interface address for remote access. Acceptable values are IP version 4 addresses. The default is to bind to INADDR_ANY address.</p>
<dt><code>-c</code></p>
<dd>&lt;dir&gt; Specify a chroot directory to use after privilege access is complete. Must be super user to use this option.</p>
<dt><code>-C</code></p>
<dd>Run argus in control plane capture mode. This sets the interface packet snap length to capture full packets, and to enable detailed flow tracking for supported control plane protocols.</p>
<dt><code>-d</code></p>
<dd>Run argus as a daemon. This will cause argus to do the things that Unix daemons do and return, if there were no errors, with argus running as a detached process.</p>
<dt><code>-D</code></p>
<dd>&lt;level&gt; Print debug messages to stderr. The higher the <code>&lt;level&gt;</code> the more information printed. Acceptable levels are 1-8.</p>
<dt><code>-e</code></p>
<dd>&lt;value&gt; Specify the source identifier for this <code>argus</code>. Acceptable values are numbers, strings, hostnames or ip address. Double quotes around the parameter are used to designate the string format. The longest supported string is 4 characeters long. Be sure and single quote or &#8216;escape&#8217; the double quotes so that the shell doesn&#8217;t gooble up the delimiters. </p>
<p> This option sets a global Source identifier that can be overriden by specific -i options. </p>
<pre> argus -e '&quot;arg1&quot;'
 argus -e \&quot;arg2\&quot;</pre>
<dt><code>-f</code></p>
<dd>When reading packets from a packet capture file, the -f option causes argus to not stop when end of file is reached, but rather to wait for additional packets to be appended to the input. The -f option is ignored if the standard input is a pipe, but not if it is a FIFO. </p>
<dt><code>-F</code></p>
<dd>Use <i>conffile</i> as a source of configuration information. Options set in this file override any other specification, and so this is the last word on option values.</p>
<dt><code>-g</code></p>
<dd>&lt;group&gt; Specify a group name to change to after privilege access is complete.</p>
<dt><code>-h</code></p>
<dd>Print an explanation of all the arguments.</p>
<dt><code>-i</code></p>
<dd>&lt;interface&gt; Specify the physical network <code>&lt;interface&gt;</code> to be audited. The default is the first network interface that is up and running. </p>
<p> The syntax for specifying the interface is the same format used in the argus.conf.5 file. The optional source id specification can be an IPv4 address, an integer, or a string denoted using double quotes. </p>
<pre> -i interface[/srcid]
 -i all[/srcid]
 -i dup:en0,en1/&quot;ap01&quot; ( en0 and en1 are in ingress and egress interfaces )
 -i bond:en0,en1/2.3.4.5 ( en0 and en1 are bonded interfaces )
 -i en0 en1 ( equivalent '-i bond:en0,en1' )
 -i dup:[bond:en0,en1],en2/3 ( in this case 3 is the srcid )
 -i en0/&quot;en0&quot; -i en1/&quot;en1&quot; ( equivalent '-i ind:en0/srcid,en1/srcid' )</pre>
<dt><code>-J&nbsp;<wbr></code></p>
<dd>Generate packet peformance data in each audit record.</p>
<dt><code>-M</code></p>
<dd>&lt;secs&gt; Specify the interval in &lt;secs&gt; of argus status records. These records are used to report the internal status of argus itself. The default is 300 seconds.</p>
<dt><code>-m</code></p>
<dd>Provide MAC addresses information in <code>argus</code> records.</p>
<dt><code>-N &lt;packet count&gt;|&lt;packet range&gt;</code></p>
<dd>Specify the number of packets to process. You can give an absolute number, or a range with the syntax &quot;start-stop&quot;. Examples are:<br />
-N 27&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; read the first 27 packets.<br />
-N 1034-1434&nbsp;<wbr>&nbsp;<wbr>&#8211; read 100 packets starting with 1034.</p>
<dt><code>-O</code></p>
<dd>Turn off Berkeley Packet Filter optimizer. No reason to do this unless you think the optimizer generates bad code.</p>
<dt><code>-p</code></p>
<dd>Do not set the physical network interface in promiscuous mode. If the interface is already in promiscuous mode, this option may have no effect. Do this to audit only the traffic coming to and from the system argus is running on.</p>
<dt><code>-P</code></p>
<dd>&lt;portnum&gt; Specifies the <code>&lt;portnum&gt;</code> for remote client connection. The default is to not support remote access. Setting the value to zero (0) will forceably turn off the facility.</p>
<dt><code>-r &lt;[type:]file [type:]file &#8230; &gt;</code></p>
<dd>Read from <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1) ,</code> <code><a href="/docs/linux/man/1-snoop/">snoop</a>(1)</code> or <code>NLANR&#8217;s Moat Time Sequence Header</code> (tsh) packet capture files. If the packet capture file is a <code>tsh</code> format file, then the <code>-t</code> option must also be used. The file &quot;-&quot; specifies stdin as the source of packets. </p>
<p> The <code>type</code> provides the opportunity to specify what type of packet source to expect and process. Supported types are &#8221; (default) and &#8216;cisco&#8217;, where argus will process the payload of packets as netflow records, when found. </p>
<p> Argus will read from only one input packet file at a time, and will open the files in lexigraphic order. Care should be taken to ensure that the timestamps in the packets are ordered, or unexpected behavior may result. If the <code>-r</code> option is specified, <code>argus</code> will not put down a <code><a href="/docs/linux/man/2-listen/">listen</a>(2)</code> to support remote access.</p>
<dt><code>-R</code></p>
<dd>Generate argus records such that response times can be derived from transaction data.</p>
<dt><code>-s</code></p>
<dd>&lt;bytes&gt; Specify the packet snaplen.</p>
<dt><code>-S</code></p>
<dd>&lt;secs&gt; Specify the status reporting interval in &lt;secs&gt; for all traffic flows.</p>
<dt><code>-t</code></p>
<dd>Indicate that the expected packet capture input file is a <code>NLANR&#8217;s Moat Time Sequence Header</code> (tsh) packet capture file.</p>
<dt><code>-T timescale</code></p>
<dd>Specify a playback timescale for realtime processing of input packets.</p>
<dt><code>-u</code></p>
<dd>&lt;user&gt; Specify an account name to change to after privilege access is complete.</p>
<dt><code>-U</code></p>
<dd>Specify the number of user bytes to capture.</p>
<dt><code>-w</code></p>
<dd>&lt;file | stream [&quot;filter&quot;]&gt; Append transaction status records to <i>output-file</i> or write records to the URL based stream. Supported stream URLs are &#8216;argus-<a href="udp://host[:port]',">udp://host[:port]&#8217;,</a> where the default port is 561. An <i>output-file</i> of &#8216;-&#8216; directs <code>argus</code> to write the resulting <i>argus-file</i> output to <i>stdout</i>.</p>
<dt><code>-X</code></p>
<dd>Clear existing argus configuration. This removes any initialization done prior to encountering this flag. Allows you to eliminate the effects of the <i>/etc/argus.conf</i> file, or any argus.conf files that may have been loaded.</p>
<dt><code>-Z</code></p>
<dd>Collect packet size information. This options turns on packet size reporting for all flows. Argus will provide the mean, max, min and standard deviation of the packet sizes seen during the flow status interval.</p>
<dt><i>expression</i></p>
<dd>This <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code> expression specifies which transactions will be selected. If no <i>expression</i> is given, all transactions are selected. Otherwise, only transactions for which <i>expression</i> is `true&#8217; will be dumped. For a complete <i>expression</i> format description, please refer to the <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1)</code> man page. </p>
</dl>
<h2>Signals</h2>
<p><code>Argus</code> catches a number of <code><a href="/docs/linux/man/3-signal/">signal</a>(3)</code> events. The three signals <code>SIGHUP</code>, <code>SIGINT</code>, and <code>SIGTERM</code> cause <code>argus</code> to exit, writing TIMEDOUT status records for all currently active transactions. The signal <code>SIGUSR1</code> will turn on <code>debug</code> reporting, and subsequent <code>SIGUSR1</code> signals, will increment the <code>debug-level</code>. The signal <code>SIGUSR2</code> will cause <code>argus</code> to turn off all <code>debug</code> reporting.</p>
<h2>Files</h2>
<pre>/etc/argus.conf - argus daemon configuration file 
/var/run/argus.#.#.pid - PID file </pre>
<h2>Examples</h2>
<p>Run <code>argus</code> as a daemon, writing all its transaction status reports to <i>output-file</i>. This is the typical mode.</p>
<dl>
<dd>
<pre><code>argus -d -e `hostname` -w </code><i>output-file</i></pre>
</dl>
<p> If ICMP traffic is not of interest to you, you can filter out ICMP packets on input.</p>
<dl>
<dd>
<pre><code>argus -w </code><i>output-file</i> - ip and not icmp</pre>
</dl>
<p> Argus supports both input filtering and output filtering, and argus supports multiple output streams, each with their own independant filters. Output streams can be written to udp based sockets, to unicast or multicast addresses. </p>
<p> If you are interested in tracking IP traffic only (input filter) and want to report ICMP traffic to one output stream, and all other IP traffic in another output stream.</p>
<dl>
<dd>
<pre><code>argus -w </code><i>argus-<a href="udp://224.0.20.21:561">udp://224.0.20.21:561</a></i> &quot;icmp&quot; \
 -w <i>argus-<a href="udp://224.0.20.21:562">udp://224.0.20.21:562</a></i> &quot;not icmp&quot; - ip</pre>
</dl>
<p> Audit the network activity that is flowing between the two gateway routers, whose ethernet addresses are 00:08:03:2D:42:01 and 00:00:0C:18:29:F1. Without specifying an <i>output-file</i>, it is assumed that the transaction status reports will be written to a remote client. In this case we have changed the port that the remote client will use to port 430/tcp.</p>
<dl>
<dd>
<pre><code>argus -P 430 ether host (0:8:3:2d:42:1 and 0:0:c:18:29:f1)</code> &amp;</pre>
</dl>
<p> Audit each individual ICMP ECHO transaction from data in &lt;dir&gt;. You would do this to gather Round Trip Time (RTT) data within your network. Append the output to <i>output-file</i>.</p>
<dl>
<dd>
<pre><code>argus -R dir -w </code><i>output-file</i> &quot;echo&quot; - icmp</pre>
</dl>
<p> Audit all NFS transactions involving the server <i>fileserver</i> and increase the reporting interval to 3600 seconds (to provide high data reduction). Append the output to <i>output-file</i>.</p>
<dl>
<dd>
<pre><code>argus -S 3600 -w </code><i>output-file</i> - host fileserver and udp and port 2049 &amp;</pre>
</dl>
<p> Import flow data from pcap file containing Cisco flow data packets. Write output to stdout, to a <i>ra.1</i> instance.</p>
<dl>
<dd>
<pre><code>argus -r </code><i>cisco:pcap-file</i> -w - | ra 
</dl></pre>
<h2>Authors</h2>
<pre>Carter Bullard (carter [at] qosient.com)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8), <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1) </p>
