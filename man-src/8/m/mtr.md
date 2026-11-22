---
title: "mtr(8)"
name: "mtr"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mtr/"
description: "mtr – a network diagnostic tool"
---

<p>mtr &#8211; a network diagnostic tool</p>
<h2>Synopsis</h2>
<p><code>mtr</code> [<code>-4</code>|<code>-6</code>] [<code>-F</code><i>&nbsp;FILENAME</i>] [<code>&#8211;report</code>] [<code>&#8211;report-wide</code>] [<code>&#8211;xml</code>] [<code>&#8211;gtk</code>] [<code>&#8211;curses</code>] [<code>&#8211;displaymode</code><i>&nbsp;MODE</i>] [<code>&#8211;raw</code>] [<code>&#8211;csv</code>] [<code>&#8211;json</code>] [<code>&#8211;split</code>] [<code>&#8211;no-dns</code>] [<code>&#8211;show-ips</code>] [<code>-o</code><i>&nbsp;FIELDS</i>] [<code>-y</code><i>&nbsp;IPINFO</i>] [<code>&#8211;aslookup</code>] [<code>-i</code><i>&nbsp;INTERVAL</i>] [<code>-c</code><i>&nbsp;COUNT</i>] [<code>-s</code><i>&nbsp;PACKETSIZE</i>] [<code>-B</code><i>&nbsp;BITPATTERN</i>] [<code>-G</code><i>&nbsp;GRACEPERIOD</i>] [<code>-Q</code><i>&nbsp;TOS</i>] [<code>&#8211;mpls</code>] [<code>-I</code><i>&nbsp;NAME</i>] [<code>-a</code><i>&nbsp;ADDRESS</i>] [<code>-f</code><i>&nbsp;FIRST-TTL</i>] [<code>-m</code><i>&nbsp;MAX-TTL</i>] [<code>-U</code><i>&nbsp;MAX-UNKNOWN</i>] [<code>&#8211;udp</code>] [<code>&#8211;tcp</code>] [<code>&#8211;sctp</code>] [<code>-P</code><i>&nbsp;PORT</i>] [<code>-L</code><i>&nbsp;LOCALPORT</i>] [<code>-Z</code><i>&nbsp;TIMEOUT</i>] [<code>-M</code><i>&nbsp;MARK</i>] <i>HOSTNAME</i></p>
<h2>Description</h2>
<p><code>mtr</code> combines the functionality of the <code>traceroute</code> and <code>ping</code> programs in a single network diagnostic tool. </p>
<p> As <code>mtr</code> starts, it investigates the network connection between the host <code>mtr</code> runs on and <code>HOSTNAME</code> by sending packets with purposely low TTLs. It continues to send packets with low TTL, noting the response time of the intervening routers. This allows <code>mtr</code> to print the response percentage and response times of the internet route to <code>HOSTNAME</code>. A sudden increase in packet loss or response time is often an indication of a bad (or simply overloaded) link. </p>
<p> The results are usually reported as round-trip-response times in milliseconds and the percentage of packet loss.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print the summary of command line argument options.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>Print the installed version of mtr.</dd>
<dt><code>-4</code></dt>
<dd>Use IPv4 only.</dd>
<dt><code>-6</code></dt>
<dd>Use IPv6 only. (IPV4 may be used for DNS lookups.)</dd>
<dt><code>-F </code><i>FILENAME</i>, <code>&#8211;filename </code><i>FILENAME</i></dt>
<dd>Reads the list of hostnames from the specified file.</dd>
<dt><code>-r</code>, <code>&#8211;report</code></dt>
<dd>This option puts <code>mtr</code> into <code>report</code> mode. When in this mode, <code>mtr</code> will run for the number of cycles specified by the <code>-c</code> option, and then print statistics and exit.</dd>
<dd>This mode is useful for generating statistics about network quality. Note that each running instance of <code>mtr</code> generates a significant amount of network traffic. Using <code>mtr</code> to measure the quality of your network may result in decreased network performance.</dd>
<dt><code>-w</code>, <code>&#8211;report-wide</code></dt>
<dd>This option puts <code>mtr</code> into <code>wide report</code> mode. When in this mode, <code>mtr</code> will not cut hostnames in the report.</dd>
<dt><code>-x</code>, <code>&#8211;xml</code></dt>
<dd>Use this option to tell <code>mtr</code> to use the xml output format. This format is better suited for automated processing of the measurement results.</dd>
<dt><code>-t</code>, <code>&#8211;curses</code></dt>
<dd>Use this option to force <code>mtr</code> to use the curses based terminal interface (if available). In case the list of hops exceeds the height of your terminal, you can use the <code>+</code> and <code>&#8211;</code> keys to scroll up and down half a page. </dd>
<p> <code>Ctrl</code>-L clears spurious error messages that may overwrite other parts of the display. </p>
<dt><code>&#8211;displaymode </code><i>MODE</i></dt>
<dd>Use this option to select the initial display mode: 0 (default) selects statistics, 1 selects the stripchart without latency information, and 2 selects the stripchart with latency information.</dd>
<dt><code>-g</code>, <code>&#8211;gtk</code></dt>
<dd>Use this option to force <code>mtr</code> to use the GTK+ based X11 window interface (if available). GTK+ must have been available on the system when <code>mtr</code> was built for this to work. See the GTK+ web page at for more information about GTK+.</dd>
<dt><code>-l</code>, <code>&#8211;raw</code></dt>
<dd>Use the raw output format. This format is better suited for archival of the measurement results. It could be parsed to be presented into any of the other display methods.</dd>
<dd>Example of the raw output format: </dd>
<pre>h 0 10.1.1.1
p 0 339
h 1 46.149.16.4
p 1 530
h 2 172.31.1.16
p 2 531
h 3 82.221.168.236
p 3 1523
h 5 195.130.211.8
p 5 1603
h 6 193.4.58.17
p 6 1127
h 7 193.4.58.17
d 7 <a rel="nofollow" href="http://www.isnic.is">www.isnic.is</a></pre>
<dt><code>-C</code>, <code>&#8211;csv</code></dt>
<dd>Use the Comma-Separated-Value (CSV) output format. (Note: The separator is actually a semi-colon &#8216;;&#8217;.)</dd>
<dd>Example of the CSV output format: </dd>
<pre>MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;1;r-76520-PROD.greenqloud.internal;288
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;2;46.149.16.4;2086
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;3;172.31.1.16;600
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;4;82.221.168.236;1163
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;5;???;0
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;6;rix-k2-gw.isnic.is;1654
MTR.0.86+git:16e39fc0;1435562787;OK;nic.is;7;<a rel="nofollow" href="http://www.isnic.is">www.isnic.is</a>;1036</pre>
<dt><code>-j</code>, <code>&#8211;json</code></dt>
<dd>Use this option to tell <code>mtr</code> to use the JSON output format. This format is better suited for automated processing of the measurement results. Jansson library must have been available on the system when <code>mtr</code> was built for this to work.</dd>
<dt><code>-p</code>, <code>&#8211;split</code></dt>
<dd>Use this option to set <code>mtr</code> to spit out a format that is suitable for a split-user interface.</dd>
<dt><code>-n</code>, <code>&#8211;no-dns</code></dt>
<dd>Use this option to force <code>mtr</code> to display numeric IP numbers and not try to resolve the host names.</dd>
<dt><code>-b</code>, <code>&#8211;show-ips</code></dt>
<dd>Use this option to tell <code>mtr</code> to display both the host names and numeric IP numbers. In split mode this adds an extra field to the output. In report mode, there is usually too little space to add the IPs, and they will be truncated. Use the wide report (-w) mode to see the IPs in report mode.</dd>
<dt><code>-o </code><i>FIELDS</i>, <code>&#8211;order </code><i>FIELDS</i></dt>
<dd>Use this option to specify which fields to display and in which order. You may use one or more space characters to separate fields.<br/>
 Available fields: <center></dd>
<table BORDER>
<tr VALIGN=top>
<td>L</td>
<td>Loss ratio
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td>Dropped packets
</td>
</tr>
<tr VALIGN=top>
<td>R</td>
<td>Received packets
</td>
</tr>
<tr VALIGN=top>
<td>S</td>
<td>Sent Packets
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Newest RTT(ms)
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>Min/Best RTT(ms)
</td>
</tr>
<tr VALIGN=top>
<td>A</td>
<td>Average RTT(ms)
</td>
</tr>
<tr VALIGN=top>
<td>W</td>
<td>Max/Worst RTT(ms)
</td>
</tr>
<tr VALIGN=top>
<td>V</td>
<td>Standard Deviation
</td>
</tr>
<tr VALIGN=top>
<td>G</td>
<td>Geometric Mean
</td>
</tr>
<tr VALIGN=top>
<td>J</td>
<td>Current Jitter
</td>
</tr>
<tr VALIGN=top>
<td>M</td>
<td>Jitter Mean/Avg.
</td>
</tr>
<tr VALIGN=top>
<td>X</td>
<td>Worst Jitter
</td>
</tr>
<tr VALIGN=top>
<td>I</td>
<td>Interarrival Jitter
</td>
</tr>
</table>
<p></center> </p>
<p> Example: -o &quot;LSD NBAW X&quot;</p>
<dt><code>-y </code><i>n</i>, <code>&#8211;ipinfo </code><i>n</i></dt>
<dd>Displays information about each IP hop. Valid values for <i>n</i> are: </dd>
<table>
<tr VALIGN=top>
<td>0</td>
<td>Display AS number (equivalent to <code>-z</code>)
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>Display IP prefix
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>Display country code of the origin AS
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>Display RIR (ripencc, arin, &#8230;)
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>Display the allocation date of the IP prefix
</td>
</tr>
</table>
<p> It is possible to cycle between these fields at runtime (using the <code>y</code> key).</p>
<dt><code>-z</code>, <code>&#8211;aslookup</code></dt>
<dd>Displays the Autonomous System (AS) number alongside each hop. Equivalent to <code>&#8211;ipinfo 0</code>.</dd>
<dd>Example (columns to the right not shown for clarity): </dd>
<pre>1. AS??? r-76520-PROD.greenqloud.internal
2. AS51969 46.149.16.4
3. AS??? 172.31.1.16
4. AS30818 82.221.168.236
5. ???
6. AS??? rix-k2-gw.isnic.is
7. AS1850 <a rel="nofollow" href="http://www.isnic.is">www.isnic.is</a></pre>
<dt><code>-i </code><i>SECONDS</i>, <code>&#8211;interval </code><i>SECONDS</i></dt>
<dd>Use this option to specify the positive number of seconds between ICMP ECHO requests. The default value for this parameter is one second. The root user may choose values between zero and one.</dd>
<dt><code>-c </code><i>COUNT</i>, <code>&#8211;report-cycles </code><i>COUNT</i></dt>
<dd>Use this option to set the number of pings sent to determine both the machines on the network and the reliability of those machines. Each cycle lasts one second.</dd>
<dt><code>-s </code><i>PACKETSIZE</i>, <code>&#8211;psize </code><i>PACKETSIZE</i></dt>
<dd>This option sets the packet size used for probing. It is in bytes, inclusive IP and ICMP headers. </dd>
<p> If set to a negative number, every iteration will use a different, random packet size up to that number.</p>
<dt><code>-B </code><i>NUM</i>, <code>&#8211;bitpattern </code><i>NUM</i></dt>
<dd>Specifies bit pattern to use in payload. Should be within range 0 &#8211; 255. If <i>NUM</i> is greater than 255, a random pattern is used.</dd>
<dt><code>-G </code><i>SECONDS</i>, <code>&#8211;gracetime </code><i>SECONDS</i></dt>
<dd>Use this option to specify the positive number of seconds to wait for responses after the final request. The default value is five seconds.</dd>
<dt><code>-Q </code><i>NUM</i>, <code>&#8211;tos </code><i>NUM</i></dt>
<dd>Specifies value for type of service field in IP header. Should be within range 0 &#8211; 255.</dd>
<dt><code>-e</code>, <code>&#8211;mpls</code></dt>
<dd>Use this option to tell <code>mtr</code> to display information from ICMP extensions for MPLS (RFC 4950) that are encoded in the response packets.</dd>
<dt><code>-I </code><i>NAME</i>, <code>&#8211;interface </code><i>NAME</i></dt>
<dd>Use the network interface with a specific name for sending network probes. This can be useful when you have multiple network interfaces with routes to your destination, for example both wired Ethernet and WiFi, and wish to test a particular interface.</dd>
<dt><code>-a </code><i>ADDRESS</i>, <code>&#8211;address </code><i>ADDRESS</i></dt>
<dd>Use this option to bind the outgoing socket to <i>ADDRESS</i>, so that all packets will be sent with <i>ADDRESS</i> as source address. NOTE that this option doesn&#8217;t apply to DNS requests (which could be and could not be what you want).</dd>
<dt><code>-f </code><i>NUM</i>, <code>&#8211;first-ttl </code><i>NUM</i></dt>
<dd>Specifies with what TTL to start. Defaults to 1.</dd>
<dt><code>-m </code><i>NUM</i>, <code>&#8211;max-ttl </code><i>NUM</i></dt>
<dd>Specifies the maximum number of hops (max time-to-live value) traceroute will probe. Default is 30.</dd>
<dt><code>-U </code><i>NUM</i>, <code>&#8211;max-unknown </code><i>NUM</i></dt>
<dd>Specifies the maximum unknown host. Default is 5.</dd>
<dt><code>-u</code>, <code>&#8211;udp</code></dt>
<dd>Use UDP datagrams instead of ICMP ECHO.</dd>
<dt><code>-T</code>, <code>&#8211;tcp</code></dt>
<dd>Use TCP SYN packets instead of ICMP ECHO. <i>PACKETSIZE</i> is ignored, since SYN packets can not contain data.</dd>
<dt><code>-S</code>, <code>&#8211;sctp</code></dt>
<dd>Use Stream Control Transmission Protocol packets instead of ICMP ECHO.</dd>
<dt><code>-P </code><i>PORT</i>, <code>&#8211;port </code><i>PORT</i></dt>
<dd>The target port number for TCP/SCTP/UDP traces.</dd>
<dt><code>-L </code><i>LOCALPORT</i>, <code>&#8211;localport </code><i>LOCALPORT</i></dt>
<dd>The source port number for UDP traces.</dd>
<dt><code>-Z </code><i>SECONDS</i>, <code>&#8211;timeout </code><i>SECONDS</i></dt>
<dd>The number of seconds to keep probe sockets open before giving up on the connection. Using large values for this, especially combined with a short interval, will use up a lot of file descriptors.</dd>
<dt><code>-M </code><i>MARK</i>, <code>&#8211;mark </code><i>MARK</i></dt>
<dd>Set the mark for each packet sent through this socket similar to the netfilter MARK target but socket-based. <i>MARK</i> is 32 unsigned integer. See <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for full description of this socket option.</dd></dl>
<h2>Environment</h2>
<p><code>mtr</code> recognizes a few environment variables.</p>
<dl>
<dt><code>MTR_OPTIONS</code></dt>
<dd>This environment variable allows one to specify options, as if they were passed on the command line. It is parsed before reading the actual command line options, so that options specified in <code>MTR_OPTIONS</code> are overridden by command-line options. </dd>
<p> Example: </p>
<p> <code>MTR_OPTIONS</code><i>=-4 -c 1</i> <code>mtr</code> <i>-6 localhost</i> </p>
<p> would send one probe (because of <i>-c 1</i>) towards <code>::1</code> (because of <i>-6</i>, which overrides the <i>-4</i> passed in <code>MTR_OPTIONS</code>).</p>
<dt><code>MTR_PACKET</code></dt>
<dd>A path to the <i>mtr-packet</i> executable, to be used for sending and receiving network probes. If <code>MTR_PACKET</code> is unset, the <code>PATH</code> will be used to search for an <i>mtr-packet</i> executable.</dd>
<dt><code>DISPLAY</code></dt>
<dd>Specifies an X11 server for the GTK+ frontend.</dd></dl>
<h2>Interactive Control</h2>
<p><code>mtr</code> can be controlled while it is running with the following keys:<br/>
&nbsp;<wbr>&nbsp;?|h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;help<br/>
&nbsp;<wbr>&nbsp;p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pause&nbsp;(SPACE to resume)<br/>
&nbsp;<wbr>&nbsp;d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switching display mode<br/>
&nbsp;<wbr>&nbsp;e&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggle MPLS information on/off<br/>
&nbsp;<wbr>&nbsp;n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggle DNS on/off<br/>
&nbsp;<wbr>&nbsp;r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reset all counters<br/>
&nbsp;<wbr>&nbsp;o str&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the columns to display, default str=&#8217;LRS N BAWV&#8217;<br/>
&nbsp;<wbr>&nbsp;j&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggle latency(LS NABWV)/jitter(DR AGJMXI)&nbsp;stats<br/>
&nbsp;<wbr>&nbsp;c&nbsp;&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;report cycle n, default n=infinite<br/>
&nbsp;<wbr>&nbsp;i&nbsp;&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the ping interval to n seconds, default n=1<br/>
&nbsp;<wbr>&nbsp;f&nbsp;&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the initial time-to-live(ttl), default n=1<br/>
&nbsp;<wbr>&nbsp;m&nbsp;&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the max time-to-live, default n=&nbsp;#&nbsp;of hops<br/>
&nbsp;<wbr>&nbsp;s&nbsp;&lt;n&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set the packet size to n or random(n&lt;0)<br/>
&nbsp;<wbr>&nbsp;b&nbsp;&lt;c&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set ping bit pattern to c(0..255)&nbsp;or random(c&lt;0)<br/>
&nbsp;<wbr>&nbsp;Q&nbsp;&lt;t&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;set ping packet&#8217;s TOS to t<br/>
&nbsp;<wbr>&nbsp;u&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch between ICMP ECHO and UDP datagrams<br/>
&nbsp;<wbr>&nbsp;y&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switching IP info<br/>
&nbsp;<wbr>&nbsp;z&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;toggle ASN info on/off<br/>
&nbsp;<wbr>&nbsp;q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit</p>
<h2>Bugs</h2>
<p>Some modern routers give a lower priority to ICMP ECHO packets than to other network traffic. Consequently, the reliability of these routers reported by <code>mtr</code> will be significantly lower than the actual reliability of these routers.</p>
<h2>Contact Information</h2>
<p>For the latest version, see the mtr web page at </p>
<p> For patches, bug reports, or feature requests, please open an issue on GitHub at:</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mtr-packet/">mtr-packet</a></code>(8), <code><a href="/docs/linux/man/8-traceroute/">traceroute</a></code>(8), <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), TCP/IP Illustrated (Stevens, ISBN 0201633469). </p>
