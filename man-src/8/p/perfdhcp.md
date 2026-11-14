---
title: "perfdhcp(8)"
name: "perfdhcp"
section: "8"
letter: "p"
url: "/docs/linux/man/8-perfdhcp/"
description: "perfdhcp – DHCP benchmarking tool"
---

<p>perfdhcp &#8211; DHCP benchmarking tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>perfdhcp</code> [<code>-1</code>] [<code>-4|-6</code>] [<code>-A&nbsp;<wbr></code><i>encapsulation-level</i>] [<code>-a&nbsp;<wbr></code><i>aggressivity</i>] [<code>-b&nbsp;<wbr></code><i>base</i>] [<code>-B</code>] [<code>-c</code>] [<code>-d&nbsp;<wbr></code><i>drop-time</i>] [<code>-D&nbsp;<wbr></code><i>max-drop</i>] [<code>-e&nbsp;<wbr></code><i>lease-type</i>] [<code>-E&nbsp;<wbr></code><i>time-offset</i>] [<code>-f&nbsp;<wbr></code><i>renew-rate</i>] [<code>-F&nbsp;<wbr></code><i>release-rate</i>] [<code>-h</code>] [<code>-i</code>] [<code>-I&nbsp;<wbr></code><i>ip-offset</i>] [<code>-l&nbsp;<wbr></code><i>local-address|interface</i>] [<code>-L&nbsp;<wbr></code><i>local-port</i>] [<code>-M&nbsp;<wbr></code><i>mac-list-file</i>] [<code>-n&nbsp;<wbr></code><i>num-request</i>] [<code>-O&nbsp;<wbr></code><i>random-offset</i>] [<code>-p&nbsp;<wbr></code><i>test-period</i>] [<code>-P&nbsp;<wbr></code><i>preload</i>] [<code>-r&nbsp;<wbr></code><i>rate</i>] [<code>-R&nbsp;<wbr></code><i>num-clients</i>] [<code>-s&nbsp;<wbr></code><i>seed</i>] [<code>-S&nbsp;<wbr></code><i>srvid-offset</i>] [<code>-t&nbsp;<wbr></code><i>report</i>] [<code>-T&nbsp;<wbr></code><i>template-file</i>] [<code>-v</code>] [<code>-W&nbsp;<wbr></code><i>wrapped</i>] [<code>-x&nbsp;<wbr></code><i>diagnostic-selector</i>] [<code>-X&nbsp;<wbr></code><i>xid-offset</i>] [server]</dl>
<h2>Description</h2>
<p><code>perfdhcp</code></p>
<dd>is a DHCP benchmarking tool. It provides a way of measuring the performance of DHCP servers by generating large amounts of traffic from simulated multiple clients. It is able to test both IPv4 and IPv6 servers, and provides statistics concerning response times and the number of requests that are dropped. </p>
<p> By default, tests are run using the full four-packet exchange sequence (DORA for DHCPv4, SARR for DHCPv6). An option is provided to run tests using the initial two-packet exchange (DO and SA) instead. It is also possible to configure perfdhcp to send DHCPv6 RENEW and RELEASE messages at a specified rate in parallel with the DHCPv6 four-way exchanges. </p>
<p> When running a performance test, <code>perfdhcp</code> will exchange packets with the server under test as fast as possible unless the <code>-r</code> is given to limit the request rate. The length of the test can be limited by setting a threshold on any or all of the number of requests made by <code>perfdhcp</code>, the elapsed time, or the number of requests dropped by the server.</p>
<h2>Templates</h2>
<p>To allow the contents of packets sent to the server to be customized, <code>perfdhcp</code> allows the specification of template files that determine the contents of the packets. For example, the customized packet may contain a DHCPv6 ORO to request a set of options to be returned by the server, or it may contain the Client FQDN option to request that server performs DNS updates. This may be used to discover performance bottlenecks for different server configurations (e.g. DDNS enabled or disabled). </p>
<p> Up to two template files can be specified on the command line, each file representing the contents of a particular type of packet, the type being determined by the test being carried out. For example, if testing DHCPv6: </p>
<dl>
<dd>&bull; With no template files specified on the command line, <code>perfdhcp</code> will generate both SOLICIT and REQUEST packets.</dl>
<dl>
<dd>&bull; With one template file specified, that file will be used as the pattern for SOLICIT packets: <code>perfdhcp</code> will generate the REQUEST packets.</dl>
<dl>
<dd>&bull; With two template files given on the command line, the first will be used as the pattern for SOLICIT packets, the second as the pattern for REQUEST packets.</dl>
<p> (Similar determination applies to DHCPv4&#8217;s DISCOVER and REQUEST packets.) </p>
<p> The template file holds the DHCP packet represented as a stream of ASCII hexadecimal digits and it excludes any IP/UDP stack headers. The template file must not contain any characters other than hexadecimal digits and spaces. Spaces are discarded when the template file is parsed (so in the file, &#8217;12B4&#8242; is the same as &#8217;12 B4&#8242; which is the same as &#8216;1 2 B 4&#8217;) </p>
<p> The template files should be used in conjunction with the command line parameters which specify offsets of the data fields being modified in outbound packets. For example, the <code>-E </code><i>time-offset</i> switch specifies the offset of the DHCPv6 Elapsed Time option in the packet template. If the offset is specified, perfdhcp will inject the current elapsed time value into this field before sending the packet to the server. </p>
<p> In many scenarios, <code>perfdhcp</code> needs to simulate multiple clients (having unique client identifier). Since packets for each client are generated from the same template file, it is necessary to randomize the client identifier (or HW address in DHCPv4) in the packet created from it. The <code>-O </code><i>random-offset</i> option allows specification of the offset in the template where randomization should be performed. It is important to note that this offset points to the end (not the beginning) of the client identifier (or HW address field). The number of bytes being randomized depends on the number of simulated clients. If the number of simulated clients is between 1 and 255, only one byte (to which randomization offset points) will be randomized. If the number of simulated clients is between 256 and 65535, two bytes will be randomized. Note, that two last bytes of the client identifier will be randomized in this case: the byte which randomization offset parameter points to, and the one which precedes it (random-offset &#8211; 1). If the number of simulated clients exceeds 65535, three bytes will be randomized; and so on. </p>
<p> Templates may be currently used to generate packets being sent to the server in 4-way exchanges, i.e. SOLICIT, REQUEST (DHCPv6) and DISCOVER, REQUEST (DHCPv4). They cannot be used when RENEW or RELEASE packets are being sent.</p>
<h2>Options</h2>
<p><code>-1</code></p>
<dl>
<dd>Take the server-ID option from the first received message.</dl>
<p> <code>-4</code></p>
<dl>
<dd>DHCPv4 operation; this is the default. It is incompatible with the <code>-6</code> option.</dl>
<p> <code>-6</code></p>
<dl>
<dd>DHCPv6 operation. This is incompatible with the <code>-4</code> option.</dl>
<p> <code>-a </code><i>aggressivity</i></p>
<dl>
<dd>When the target sending rate is not yet reached, control how many exchanges are initiated before the next pause. This is a positive integer and defaults to 1.</dl>
<p> <code>-b </code><i>basetype=value</i></p>
<dl>
<dd>The base MAC or DUID used to simulate different clients. The <i>basetype</i> may be &quot;mac&quot; or &quot;duid&quot;. (The keyword &quot;ether&quot; may alternatively used for MAC.) The <code>-b</code> option can be specified multiple times. The MAC address must consist of six octets separated by single (:) or double (::) colons, for example: mac=00:0c:01:02:03:04. The DUID value is a hexadecimal string: it must be at least six octets long and must not be longer than 64 bytes and the length must be less than 128 hexadecimal digits, for example: duid=0101010101010101010110111F14.</dl>
<p> <code>-d </code><i>drop-time</i></p>
<dl>
<dd>Specify the time after which a request is treated as having been lost. The value is given in seconds and may contain a fractional component. The default is 1 second.</dl>
<p> <code>-e </code><i>lease-type</i></p>
<dl>
<dd>Specifies the type of lease being requested from the server. It may be one of the following: </p>
<p> address-only</p>
<dl>
<dd>Only regular addresses (v4 or v6) will be requested.</dl>
<p> prefix-only</p>
<dl>
<dd>Only IPv6 prefixes will be requested.</dl>
<p> address-and-prefix</p>
<dl>
<dd>Both IPv6 addresses and prefixes will be requested.</dl>
<p> The <code>-e prefix-only</code> and <code>-e address-and-prefix</code> forms may not be used with the <code>-4</code> option.</dl>
<p> <code>-f </code><i>renew-rate</i></p>
<dl>
<dd>Rate at which DHCPv4 or DHCPv6 renew requests are sent to a server. This value is only valid when used in conjunction with the exchange rate (given by <code>-r </code><i>rate</i>). Furthermore the sum of this value and the release-rate (given by <code>-F </code><i> rate</i>) must be equal to or less than the exchange rate.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Print help and exit.</dl>
<p> <code>-i</code></p>
<dl>
<dd>Do only the initial part of the exchange: DISCOVER-OFFER if <code>-4</code> is selected, SOLICIT-ADVERTISE if <code>-6</code> is chosen. </p>
<p> <code>-i</code> is incompatible with the following options: <code>-1</code>, <code>-d</code>, <code>-D</code>, <code>-E</code>, <code>-S</code>, <code>-I</code> and <code>-F</code>. In addition, it cannot be used with multiple instances of <code>-O</code>, <code>-T</code> and <code>-X</code>.</dl>
<p> <code>-l </code><i>local-addr|interface</i></p>
<dl>
<dd>For DHCPv4 operation, specify the local hostname/address to use when communicating with the server. By default, the interface address through which traffic would normally be routed to the server is used. For DHCPv6 operation, specify the name of the network interface through which exchanges are initiated.</dl>
<p> <code>-L </code><i>local-port</i></p>
<dl>
<dd>Specify the local port to use. This must be zero or a positive integer up to 65535. A value of 0 (the default) allows <code>perfdhcp</code> to choose its own port.</dl>
<p> <code>-M </code><i>mac-list-file</i></p>
<dl>
<dd>A text file containing a list of MAC addresses, one per line. If provided, a MAC address will be choosen randomly from this list for every new exchange. In the DHCPv6 case, MAC addresses are used to generate DUID-LLs. This parameter must not be used in conjunction with the -b parameter.</dl>
<p> <code>-P </code><i>preload</i></p>
<dl>
<dd>Initiate <i>preload</i> exchanges back to back at startup. <i>preload</i> must be 0 (the default) or a positive integer.</dl>
<p> <code>-r </code><i>rate</i></p>
<dl>
<dd>Initiate <i>rate</i> DORA/SARR (or if <code>-i</code> is given, DO/SA) exchanges per second. A periodic report is generated showing the number of exchanges which were not completed, as well as the average response latency. The program continues until interrupted, at which point a final report is generated.</dl>
<p> <code>-R </code><i>num-clients</i></p>
<dl>
<dd>Specify how many different clients are used. With a value of 1 (the default), all requests seem to come from the same client. <i>num-clients</i> must be a positive number.</dl>
<p> <code>-s </code><i>seed</i></p>
<dl>
<dd>Specify the seed for randomization, making runs of <code>perfdhcp</code> repeatable. <i>seed</i> is 0 or a positive integer. The value 0 means that a seed is not used; this is the default.</dl>
<p> <code>-T </code><i>template-file</i></p>
<dl>
<dd>The name of a file containing the template to use as a stream of hexadecimal digits. This may be specified up to two times and controls the contents of the packets sent (see the &quot;TEMPLATES&quot; section above).</dl>
<p> <code>-v</code></p>
<dl>
<dd>Print the version of this program.</dl>
<p> <code>-w </code><i>wrapped</i></p>
<dl>
<dd>Command to call with a single parameter of &quot;start&quot; or &quot;stop&quot; at the beginning/end of the program.</dl>
<p> <code>-x </code><i>diagnostic-selector</i></p>
<dl>
<dd>Include extended diagnostics in the output. <i>diagnostic-selector</i> is a string of single-keywords specifying the operations for which verbose output is desired. The selector key letters are: </p>
<p> a</p>
<dl>
<dd>Print the decoded command line arguments.</dl>
<p> e</p>
<dl>
<dd>Print the exit reason.</dl>
<p> i</p>
<dl>
<dd>Print rate processing details.</dl>
<p> s</p>
<dl>
<dd>Print the first server-ID.</dl>
<p> t</p>
<dl>
<dd>When finished, print timers of all successful exchanges.</dl>
<p> T</p>
<dl>
<dd>When finished, print templates</dl>
</dl>
<h3>DHCPv4-Only Options</h3>
<p>The following options only apply for DHCPv4 (i.e. when <code>-4</code> is given). </p>
<p> <code>-B</code></p>
<dl>
<dd>Force broadcast handling.</dl>
<h3>DHCPv6-Only Options</h3>
<p>The following options only apply for DHCPv6 (i.e. when <code>-6</code> is given). </p>
<p> <code>-c</code></p>
<dl>
<dd>Add a rapid commit option (exchanges will be SOLICIT-ADVERTISE).</dl>
<p> <code>-F </code><i>release-rate</i></p>
<dl>
<dd>Rate at which IPv6 RELEASE requests are sent to a server. This value is only valid when used in conjunction with the exchange rate (given by <code>-r </code><i>rate</i>). Furthermore the sum of this value and the renew-rate (given by <code>-f </code><i>rate</i>) must be equal to or less than the exchange rate.</dl>
<p> <code>-A </code><i>encapsulation-level</i></p>
<dl>
<dd>Specifies that relayed traffic must be generated. The argument specifies the level of encapsulation, i.e. how many relay agents are simulated. Currently the only supported <i>encapsulation-level</i> value is 1, which means that the generated traffic is an equivalent of the traffic passing through a single relay agent.</dl>
<h3>Template-Related Options</h3>
<p>The following options may only be used in conjunction with <code>-T</code> and control how <code>perfdhcp</code> modifies the template. The options may be specified multiple times on the command line; each occurrence affects the corresponding template file (see &quot;TEMPLATES&quot; above). </p>
<p> <code>-E </code><i>time-offset</i></p>
<dl>
<dd>Offset of the (DHCPv4) secs field or (DHCPv6) elapsed-time option in the (second i.e. REQUEST) template and must be 0 or a positive integer: a value of 0 disables this.</dl>
<p> <code>-I </code><i>ip-offset</i></p>
<dl>
<dd>Offset of the (DHCPv4) IP address in the requested-IP option / (DHCPv6) IA_NA option in the (second/request) template.</dl>
<p> <code>-O </code><i>random-offset</i></p>
<dl>
<dd>Offset of the last octet to randomize in the template. <i>random-offset</i> must be an integer greater than 3. The <code>-T</code> switch must be given to use this option.</dl>
<p> <code>-S </code><i>srvid-offset</i></p>
<dl>
<dd>Offset of the server-ID option in the (second/request) template. <i>srvid-offset</i> must be a positive integer, and the switch can only be used when the template option (<code>-T</code>) is also given.</dl>
<p> <code>-X </code><i>xid-offset</i></p>
<dl>
<dd>Offset of the transaction ID (xid) in the template. <i>xid-offset</i> must be a positive integer, and the switch can only be used when the template option (<code>-T</code>) is also given.</dl>
<h3>Options Controlling a Test</h3>
<p>The following options may only be used in conjunction with <code>-r</code> and control both the length of the test and the frequency of reports. </p>
<p> <code>-D </code><i>max-drop</i></p>
<dl>
<dd>Abort the test if more than <i>max-drop</i> requests have been dropped. Use <code>-D 0</code> to abort if even a single request has been dropped. If <i>max-drop</i> includes the suffix &#8216;%&#8217;, it specifies a maximum percentage of requests that may be dropped before abort. In this case, testing of the threshold begins after 10 requests have been expected to be received.</dl>
<p> <code>-n </code><i>num-requests</i></p>
<dl>
<dd>Initiate <i>num-request</i> transactions. No report is generated until all transactions have been initiated/waited-for, after which a report is generated and the program terminates.</dl>
<p> <code>-p </code><i>test-period</i></p>
<dl>
<dd>Send requests for <i>test-period</i>, which is specified in the same manner as <code>-d</code>. This can be used as an alternative to <code>-n</code>, or both options can be given, in which case the testing is completed when either limit is reached.</dl>
<p> <code>-t </code><i>interval</i></p>
<dl>
<dd>Sets the delay (in seconds) between two successive reports.</dl>
<h3>Arguments</h3>
<p>server</p>
<dl>
<dd>Server to test, specified as an IP address. In the DHCPv6 case, the special name &#8216;all&#8217; can be used to refer to All_DHCP_Relay_Agents_and_Servers (the multicast address FF02::1:2), or the special name &#8216;servers&#8217; to refer to All_DHCP_Servers (the multicast address FF05::1:3). The server is mandatory except where the <code>-l</code> option is given to specify an interface, in which case it defaults to &#8216;all&#8217;.</dl>
<h2>Errors</h2>
<p><code>perfdhcp</code> can report the following errors in the packet exchange: </p>
<p> tooshort</p>
<dl>
<dd>A message was received that was too short.</dl>
<p> orphans</p>
<dl>
<dd>Received a message which doesn&#8217;t match one sent to the server (i.e. it is a duplicate message, a message that has arrived after an excessive delay, or one that is just not recognized).</dl>
<p> locallimit</p>
<dl>
<dd>Reached local system limits when sending a message.</dl>
<h2>Exit Status</h2>
<p><code>perfdhcp</code> can exit with one of the following status codes: </p>
<p> 0</p>
<dl>
<dd>Success.</dl>
<p> 1</p>
<dl>
<dd>General error.</dl>
<p> 2</p>
<dl>
<dd>Error in command-line arguments.</dl>
<p> 3</p>
<dl>
<dd>No general failures in operation, but one or more exchanges were unsuccessful.</dl>
<h2>Mailing Lists And Support</h2>
<p>There are two mailing lists available for Kea project. kea-users (kea-users at lists.isc.org) is intended for Kea users, while kea-dev (kea-dev at lists.isc.org) is intended for Kea developers, prospective contributors and other advanced users. Both lists are available at <a rel="nofollow" href="http://lists.isc.org.">http://lists.isc.org.</a> The community provides best effort type of support on both of those lists. </p>
<p> ISC provides professional support for Kea services. See <a rel="nofollow" href="https://www.isc.org/kea/">https://www.isc.org/kea/</a> for details.</p>
<h2>History</h2>
<p>The <code>perfdhcp</code> tool was initially coded in October 2011 by John DuBois, Francis Dupont and Marcin Siodelski of ISC. Kea 1.0.0 that included perfdhcp was released in December 2015.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kea-dhcp4/">kea-dhcp4</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp6/">kea-dhcp6</a></code>(8), <code><a href="/docs/linux/man/8-kea-dhcp-ddns/">kea-dhcp-ddns</a></code>(8), <code><a href="/docs/linux/man/8-kea-admin/">kea-admin</a></code>(8), <code><a href="/docs/linux/man/8-keactrl/">keactrl</a></code>(8), <code><a href="/docs/linux/man/8-kea-lfc/">kea-lfc</a></code>(8), Kea Administrator&#8217;s Guide.</p>
<h2>Author</h2>
<p>The Kea software has been written by a number of engineers working for ISC: Tomek Mrugalski, Stephen Morris, Marcin Siodelski, Thomas Markwalder, Francis Dupont, Jeremy C. Reed, Wlodek Wencel and Shawn Routhier. That list is roughly in the chronological order in which the authors made their first contribution. For a complete list of authors and contributors, see AUTHORS file.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2016 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
