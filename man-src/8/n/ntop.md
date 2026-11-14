---
title: "ntop(8)"
name: "ntop"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntop/"
description: "ntop – display top network users"
---

<p>ntop &#8211; display top network users</p>
<h2>Synopsis</h2>
<p><code>ntop</code> [<code>@filename</code>] [<code>-a</code>|<code>&#8211;access-log-file</code> <i>&lt;path&gt;</i>] [<code>-b</code>|<code>&#8211;disable-decoders</code>] [<code>-c</code>|<code>&#8211;sticky-hosts</code>] [<code>-e</code>|<code>&#8211;max-table-rows</code>] [<code>-f</code>|<code>&#8211;traffic-dump-file</code> <i>file&gt;</i>] [<code>-g</code>|<code>&#8211;track-local-hosts</code>] [<code>-h</code>|<code>&#8211;help</code>] [<code>-j</code>|<code>&#8211;create-other-packets</code>] [<code>-l</code>|<code>&#8211;pcap-log</code> <i>&lt;path&gt;</i>] [<code>-m</code>|<code>&#8211;local-subnets</code> <i>&lt;addresses&gt;</i>] [<code>-n</code>|<code>&#8211;numeric-ip-addresses</code>] [<code>-o</code>|<code>&#8211;no-mac</code>] [<code>-p</code>|<code>&#8211;protocols</code> <i>&lt;list&gt;</i>] [<code>-q</code>|<code>&#8211;create-suspicious-packets</code>] [<code>-r</code>|<code>&#8211;refresh-time</code> <i>&lt;number&gt;</i>] [<code>-s</code>|<code>&#8211;no-promiscuous</code>] [<code>-t</code>|<code>&#8211;trace-level</code> <i>&lt;number&gt;</i>] [<code>-x</code> <i>&lt;max_num_hash_entries&gt;</i>] [<code>-w</code>|<code>&#8211;http-server</code> <i>&lt;port&gt;</i>] [<code>-z</code>|<code>&#8211;disable-sessions</code>] [<code>-A</code>|<code>&#8211;set-admin-password</code> <i>password</i>] [<code>-B</code>|<code>&#8211;filter-expression</code> <i>expression</i>] [<code>-C</code> <i>&lt;config</i>mode&gt;<i>]</i> [<code>-D</code>|<code>&#8211;domain</code> <i>&lt;name&gt;</i>] [<code>-F</code>|<code>&#8211;flow-spec</code> <i>&lt;specs&gt;</i>] [<code>-M</code>|<code>&#8211;no-interface-merge</code>] [<code>-N</code>|<code>&#8211;wwn-map</code> <i>&lt;path&gt;</i>] [<code>-O</code>|<code>&#8212;-output-packet-path</code> <i>&lt;path&gt;</i>] [<code>-P</code>|<code>&#8211;db-file-path</code> <i>&lt;path&gt;</i>] [<code>-Q</code>|<code>&#8211;spool-file-path</code> <i>&lt;path&gt;</i>] [<code>-U</code>|<code>&#8211;mapper</code> <i>&lt;URL&gt;</i>] [<code>-V</code>|<code>&#8211;version]</code> [<code>-X</code> <i>&lt;max_num_TCP_sessions&gt;</i>] [<code>&#8211;disable-instantsessionpurge</code>] [<code>&#8211;disable-mutexextrainfo</code>] [<code>&#8211;disable-schedyield</code>] [<code>&#8211;disable-stopcap</code>] [<code>&#8211;fc-only</code>] [<code>&#8211;instance</code>] [<code>&#8211;no-fc</code>] [<code>&#8211;no-invalid-lun</code>] [<code>&#8211;p3p-cp</code>] [<code>&#8211;p3p-uri</code>] [<code>&#8211;skip-version-check</code>] [<code>&#8211;w3c</code>] [<code>-4</code>|<code>&#8211;ipv4]</code> [<code>-6</code>|<code>&#8211;ipv6]</code> Unix options: [<code>-d</code>|<code>&#8211;daemon</code>] [<code>-i</code>|<code>&#8211;interface</code> <i>&lt;name&gt;</i>] [<code>-u</code>|<code>&#8211;user</code> <i>&lt;user&gt;</i>] [<code>-K</code>|<code>&#8211;enable-debug</code>] [<code>-L</code>] [<code>&#8211;pcap_setnonblock</code>] [<code>&#8211;use-syslog=</code> <i>&lt;facility&gt;</i>] [<code>&#8211;webserver-queue</code> <i>&lt;number&gt;</i>] Windows option: [<code>-i</code>|<code>&#8211;interface</code> <i>&lt;number|name&gt;</i>] OpenSSL options: [<code>-W</code>|<code>&#8211;https-server</code> <i>&lt;port&gt;</i>] [<code>&#8211;ssl-watchdog</code>] </p>
<h2>Description</h2>
<p><code>ntop</code> shows the current network usage. It displays a list of hosts that are currently using the network and reports information concerning the (IP and non-IP) traffic generated and received by each host. <code>ntop</code> may operate as a front-end collector (sFlow and/or netFlow plugins) or as a stand-alone collector/display program. A web browser is needed to access the information captured by the <code>ntop</code> program. <code>ntop</code> is a hybrid layer 2 / layer 3 network monitor, that is by default it uses the layer 2 Media Access Control (MAC) addresses AND the layer 3 tcp/ip addresses. <code>ntop</code> is capable of associating the two, so that ip and non-ip traffic (e.g. arp, rarp) are combined for a complete picture of network activity. </p>
<h2>Command-Line Options</h2>
<p>@filename The text of <code>filename</code> is copied &#8211; ignoring line breaks and comment lines (anything following a #) &#8211; into the command line. <code>ntop</code> behaves as if all of the text had simply been typed directly on the command line. For example, if the command line is &quot;-t 3 @d -u ntop&quot; and file d contains just the line &#8216;-d&#8217;, then the effective command line is -t 3 -d -u ntop. Multiple @s are permitted. Nested @s (an @ inside the file) are not permitted. </p>
<p> Remember, most <code>ntop </code> options are &quot;sticky&quot;, that is they just set an internal flag. Invoking them multiple times doesn&#8217;t change <code>ntop&#8217;s </code> behavior. However, options that set a value, such as &#8211;trace-level, will use the LAST value given: &#8211;trace-level 2 &#8211;trace-level 3 will run as &#8211;trace-level 3.<br />
&nbsp;<wbr> Beginning with 3.1, many command-line options may also be set via the web browser interface. These changes take effect on the next run of and on each subsequent run until changed. </p>
<p> 2 -a &#8211;access-log-file By default <code>ntop</code> does not maintain a log of HTTP requests to the internal web server. Use this parameter to request logging and to specify the location of the file where these HTTP requests are logged. </p>
<p> Each log entry is in Apache-like style. The only difference between Apache and <code>ntop</code> logs is that an additional column has been added which has the time (in milliseconds) that <code>ntop </code> needed to serve the request. Log entries look like this: </p>
<pre>192.168.1.1 - - [04/Sep/2003:20:38:55 -0500] - &quot;GET / HTTP/1.1&quot; 200 1489 4
192.168.1.1 - - [04/Sep/2003:20:38:55 -0500] - &quot;GET /index_top.html HTTP/1.1&quot; 200 1854 4
192.168.1.1 - - [04/Sep/2003:20:38:55 -0500] - &quot;GET /index_inner.html HTTP/1.1&quot; 200 1441 7
192.168.1.1 - - [04/Sep/2003:20:38:56 -0500] - &quot;GET /index_left.html HTTP/1.1&quot; 200 1356 4
192.168.1.1 - - [04/Sep/2003:20:38:56 -0500] - &quot;GET /home_.html HTTP/1.1&quot; 200 154/617 9
192.168.1.1 - - [04/Sep/2003:20:38:56 -0500] - &quot;GET /home.html HTTP/1.1&quot; 200 1100/3195 10
192.168.1.1 - - [04/Sep/2003:20:38:56 -0500] - &quot;GET /About.html HTTP/1.1&quot; 200 2010 10</pre>
<p>This parameter is the complete file name of the access log. In prior releases it was erroneously called &#8211;access-log-path. </p>
<p> 2 -b &#8211;disable-decoders This parameter disables protocol decoders. </p>
<p> Protocol decoders examine and collect information about layer 2 protocols such as NetBIOS or Netware SAP, as well as about specific tcp/ip (layer 3) protocols, such as DNS, http and ftp. </p>
<p> This support is specifically coded for each protocol and is different from the capability to count raw information (packets and bytes) by protocol specified by the -p | &#8211;protocols parameter, below. </p>
<p> Decoding protocols is a significant consumer of resources. If the <code>ntop</code> host is underpowered or monitoring a very busy network, you may wish to disable protocol decoding via this parameter. It may also be appropriate to use this parameter if you believe that <code>ntop</code> has problems handling some protocols that occur on your network. </p>
<p> Even if decoding is disabled, ftp-data traffic is still decoded to look for passive ftp port commands. </p>
<p> 2 -c &#8211;sticky-hosts Use this parameter to prevent idle hosts from being purged from memory. </p>
<p> By default idle hosts are periodically purged from memory. An idle host is identified when no packets from or to that host have been monitored for the period of time defined by the value of PARM_HOST_PURGE_MINIMUM_IDLE in globals-defines.h. </p>
<p> If you use this option, all hosts &#8211; active and idle &#8211; are retained in memory for the duration of the <code>ntop</code> run. </p>
<p> P2P users, port scans, popular web servers and other activity will cause <code>ntop</code> to record data about a large number of hosts. On an active network, this will consume a significant &#8211; and always growing &#8211; amount of memory. It is strongly recommended that you use a filtering expression to limit the hosts which are stored if you use &#8211;sticky-hosts. </p>
<p> The idle purge is a statistical one &#8211; a random selection of the eligible hosts will be purged during each cycle. Thus it is possible on a busy system for an idle host to remain in the <code>ntop</code> tables and appear &#8216;active&#8217; for some considerable time after it is truly idle. </p>
<p> 2 -d &#8211;daemon This parameter causes ntop to become a daemon, i.e. a task which runs in the background without connection to a specific terminal. To use <code>ntop</code> other than as a casual monitoring tool, you probably will want to use this option. </p>
<p> <code>WARNING:</code> If you are running as a daemon, the messages from <code>ntop </code> will be &#8216;printed&#8217; on to stdout and thus dropped. You probably don&#8217;t want to do this. So remember to also use the -L or &#8211;use-syslog options to save the messages into the system log. </p>
<p> 2 -e &#8211;max-table-rows This defines the maximum number of lines that <code>ntop</code> will display on each generated HTML page. If there are more lines to be displayed than this setting permits, only part of the data will be displayed. There will be page forward/back arrows placed at the bottom of the page for navigation between pages. </p>
<p> 2 -f &#8211;traffic-dump-file By default, <code>ntop</code> captures traffic from network interface cards (NICs) or from netFlow/sFlow probes. However, <code>ntop</code> can also read data from a file &#8211; typically a tcpdump capture or the output from one of the <code>ntop</code> packet capture options. </p>
<p> if you specify -f, <code>ntop</code> will not capture any traffic from NICs during or after the file has been read. netFlow/sFlow capture &#8211; if enabled &#8211; would still be active. </p>
<p> This option is mostly used for debug purposes. </p>
<p> 2 -g &#8211;track-local-hosts By default, <code>ntop</code> tracks all hosts that it sees from packets captured on the various NICs. Use this parameter to tell <code>ntop </code> to capture data only about local hosts. Local hosts are defined based on the addresses of the NICs and those networks identified as local via the -m | &#8211;local-subnets parameter. </p>
<p> This parameter is useful on large networks or those that see many hosts, (e.g. a border router or gateway), where information about remote hosts is not desired/required to be tracked. </p>
<p> 2 -h &#8211;help Print help information for <code>ntop,</code> including usage and parameters. </p>
<p> 2 -i &#8211;interface Specifies the network interface or interfaces to be used by <code>ntop</code> for network monitoring. </p>
<p> If multiple interfaces are used (this feature is available only if ntop is compiled with thread support) their names must be separated with a comma. For instance -i &quot;eth0,lo&quot;. </p>
<p> If not specified, the default is the first Ethernet device, e.g. eth0. The specific device that is &#8216;first&#8217; is highly system dependent. Especially on systems where the device name reflects the driver name instead of the type of interface. </p>
<p> By default, traffic information obtained by all the interfaces is merged together as if the traffic was seen by only one interface. Use the -M parameter to keep traffic separate by interface. </p>
<p> If you do not want <code>ntop</code> to monitor any interfaces, use -i none. </p>
<p> Under Windows, the parameter value is either the number of the interface or its name, e.g. {6252C14C-44C9-49D9-BF59-B2DC18C7B811}. Run <code>ntop</code> -h to see a list of interface name-number mappings (at the end of the help information). </p>
<p> 2 -j &#8211;create-other-packets This parameter causes <code>ntop</code> to create a dump file of the &#8216;other&#8217; network traffic captured. One file is created for each network interface where &lt;path&gt;/ntop-other-pkts.&lt;device&gt;.pcap, where &lt;path&gt; is defined by the -O | &#8211;output-packet-path parameter. This file is useful for understanding these unclassifed packets. </p>
<p> 2 -l &#8211;pcap-log This parameter causes a dump file to be created of the network traffic captured by <code>ntop</code> in tcpdump (pcap) format. This file is useful for debug, and may be read back into <code>ntop</code> by the -f | &#8211;traffic-dump-file parameter. The dump is made after processing any filter expression ( never even sees filtered packets). </p>
<p> The output file will be named <i>&lt;path&gt;/&lt;log&gt;.&lt;device&gt;.pcap</i> (Windows: <i>&lt;path&gt;/&lt;log&gt;.pcap</i> ), where &lt;path&gt; is defined by the -O | &#8211;output-packet-path parameter and &lt;log&gt; is defined by this -l | &#8211;pcap-log parameter. </p>
<p> 2 -m &#8211;local-subnets <code>ntop</code> determines the ip addresses and netmasks for each active interface. Any traffic on those networks is considered local. This parameter allows the user to define additional networks and subnetworks whose traffic is also considered local in <code>ntop</code> reports. All other hosts are considered remote. </p>
<p> Commas separate multiple network values. Both netmask and CIDR notation may be used, even mixed together, for instance &quot;131.114.21.0/24,10.0.0.0/255.0.0.0&quot;. </p>
<p> The local subnet &#8211; as defined by the interface address(es) &#8211; is/are always local and do not need to be specified. If you do give the same value as a NIC&#8217;s local address, a harmless warning message is issued. </p>
<p> 2 -n &#8211;numeric-ip-addresses By default, <code>ntop</code> resolves IP addresses using a combination of active (explicit) DNS queries and passive sniffing. Sniffing of DNS responses occurs when <code>ntop</code> receives a network packet containing the response to some other user&#8217;s DNS query. <code>ntop</code> captures this information and enters it into <code>ntop&#8217;s</code> DNS cache, in expectation of shortly seeing traffic addressed to that host. This way <code>ntop</code> significantly reduces the number of DNS queries it makes. </p>
<p> This parameter causes <code>ntop</code> to skip DNS resolution, showing only numeric IP addresses instead of the symbolic names. This option can useful when the DNS is not present or quite slow. </p>
<p> 2 -o &#8211;no-mac <code>ntop</code> is a hybrid layer 2/3 network monitor. That is, it uses both the lower level, physical device address &#8211; the MAC (Media Access Control) address &#8211; and the higher level, logical, tcp/ip address (the familiar <a rel="nofollow" href="http://www.ntop.org">www.ntop.org</a> or 131.114.21.9 address). This allows <code>ntop </code> to link the logical addresses to a physical machine with multiple addresses (This occurs with virtual hosts or additional addresses assigned to the interface, etc.) to present consolidated reporting. </p>
<p> This parameter specifies that <code>ntop</code> should not trust the MAC addresses but just use the IP addresses. </p>
<p> Normally, since the MAC address must be globally unique, the dual nature of <code>ntop </code> is a benefit and provides far better information about the network than is available via a pure layer 2 or pure layer 3 monitor. </p>
<p> Under certain circumstances &#8211; whenever <code>ntop</code> is started on an interface where MAC addresses cannot be really trusted &#8211; you may require this option. </p>
<p> Situations which may require this option include port/VLAN mirror, some cases with switches and spanning tree protocol, and (reportedly) some specific models of Ethernet switches which re-write MAC addresses of the packets they process. Normally, you discover that this option is necessary when you observe that hosts seem to change their addresses or information about different machines get lumped together. </p>
<p> Note that with this option, information which is dependent upon the MAC addresses (non tcp/ip protocols like IPX) will not be collected nor displayed. </p>
<p> 2 -p &#8211;protocols This parameter is used to specify the TCP/UDP protocols that <code>ntop</code> will monitor. The format is &lt;label&gt;=&lt;protocol list&gt; [, &lt;label&gt;=&lt;protocol list&gt;], where label is used to symbolically identify the &lt;protocol list&gt;. The format of &lt;protocol list&gt; is &lt;protocol&gt;[|&lt;protocol&gt;], where &lt;protocol&gt; is either a valid protocol specified inside the /etc/services file or a numeric port range (e.g. 80, or 6000-6500). </p>
<p> A simple example is &#8211;protocols=&quot;HTTP=http|www|https|3128,FTP=ftp|ftp-data&quot;, which reduces the protocols displayed on the &quot;IP&quot; pages to three: </p>
<pre>Host Domain Data HTTP FTP Other IP
ns2.attbi.com &lt;flag&gt; 954 63.9 % 0 0 954
64.124.83.112.akamai.com &lt;flag&gt; 240 16.1 % 240 0 0
64.124.83.99.akamai.com &lt;flag&gt; 240 16.1 % 240 0 0
toolbarqueries.google.com &lt;flag&gt; 60 4.0 % 60 0 0</pre>
<p>If the &lt;protocol list&gt; is very long you may store it in a file (for instance protocol.list). To do so, specify the file name instead of the &lt;protocol list&gt; on the command line. e.g. <code>ntop -p protocol.list</code> </p>
<p> If the -p parameter is omitted the following default value is used: </p>
<pre> FTP=ftp|ftp-data
 HTTP=http|www|https|3128 3128 is Squid, the HTTP cache
 DNS=name|domain
 Telnet=telnet|login
 NBios-IP=netbios-ns|netbios-dgm|netbios-ssn
 Mail=pop-2|pop-3|pop3|kpop|smtp|imap|imap2
 DHCP-BOOTP=67-68
 SNMP=snmp|snmp-trap
 NNTP=nntp
 NFS=mount|pcnfs|bwnfs|nfsd|nfsd-status
 X11=6000-6010
 SSH=22
 Peer-to-Peer Protocols
 ----------------------
 Gnutella=6346|6347|6348
 Kazaa=1214
 WinMX=6699|7730
 DirectConnect=0 Dummy port as this is a pure P2P protocol
 eDonkey=4661-4665
 Instant Messenger
 -----------------
 Messenger=1863|5000|5001|5190-5193</pre>
<p>NOTE: To resolve protocol names to port numbers, they must be specified in the system file used to list tcp/udp protocols and ports, which is typically /etc/services file. You will have to match the names in that file, exactly. Missing or unspecified (non-standard) ports must be specified by number, such as 3128 in our examples above. </p>
<p> If you have a file named /etc/protocols, don&#8217;t get confused by it, as that&#8217;s the Ethernet protocol numbers, which are not what you&#8217;re looking for. </p>
<p> 2 -q &#8211;create-suspicious-packets This parameter tells <code>ntop </code> to create a dump file of suspicious packets. </p>
<p> There are many, many, things that cause a packet to be labeled as &#8216;suspicious&#8217;, including: </p>
<pre> Detected ICMP fragment
 Detected Land Attack against host
 Detected overlapping/tiny packet fragment
 Detected traffic on a diagnostic port
 Host performed ACK/FIN/NULL scan
 Host rejected TCP session
 HTTP/FTP/SMTP/SSH detected at wrong port
 Malformed TCP/UDP/ICMP packet (packet too short)
 Packet # %u too long
 Received a ICMP protocol Unreachable from host
 Sent ICMP Administratively Prohibited packet to host
 Smurf packet detected for host
 TCP connection with no data exchanged
 TCP session reset without completing 3-way handshake
 Two MAC addresses found for the same IP address
 UDP data to a closed port
 Unknown protocol (no HTTP/FTP/SMTP/SSH) detected (on port 80/21/25/22)
 Unusual ICMP options</pre>
<p>When this parameter is used, one file is created for each network interface where suspicious packets are found. The file is in tcpdump (pcap) format and is named &lt;path&gt;/ntop-suspicious-pkts.&lt;device&gt;.pcap, where &lt;path&gt; is defined by the -O | &#8211;output-packet-path parameter. </p>
<p> 2 -r &#8211;refresh-time Specifies the delay (in seconds) between automatic screen updates for those generated HTML pages which support them. This parameter allows you to leave your browser window open and have it always displaying nearly real-time data from <code>ntop.</code> </p>
<p> The default is 3 seconds. Please note that if the delay is very short (1 second for instance), <code>ntop </code> might not be able to process all of the network traffic. </p>
<p> 2 -s &#8211;no-promiscuous Use this parameter to prevent from setting the interface(s) into promiscuous mode. </p>
<p> An interface in promiscuous mode will accept ALL Ethernet frames, regardless of whether they directed (addressed) to the specific network interface (NIC) or not. This is an essential part of enabling <code>ntop</code> to monitor an entire network. (Without promiscuous mode, <code>ntop</code> will only see traffic directed to the specific host it is running on, plus broadcast traffic such as the arp and dhcp protocols. </p>
<p> Even if you use this parameter, the interface could well be in promiscuous mode if another application enabled it. </p>
<p> <code>ntop</code> passes this setting on to libpcap, the packet capture library. On many systems, a non-promiscuous open of the network interface will fail, since the libpcap function on most systems require it to capture raw packets ( <code>ntop</code> captures raw packets so that we may view and analyze the layer 2 &#8211; MAC &#8211; information). </p>
<p> Thus on most systems, <code>ntop</code> must probably still be started as root, and this option is largely ornamental. If it fails, you will see a ***FATALERROR*** message referring to pcap_open_live() and then an information message, &quot;Sorry, but on this system, even with -s, it appears that ntop must be started as root&quot;. </p>
<p> 2 -t &#8211;trace-level This parameter specifies the &#8216;information&#8217; level of messages that you wish <code>ntop</code> to display (on stdout or to the log). The higher the trace level number the more information that is displayed. The trace level ranges between 0 (no trace) and 5 (full debug tracings). </p>
<p> The default trace value is 3. </p>
<p> Trace level 0 is not quite zero messages. Fatal errors and certain startup/shutdown messages are always displayed. Trace level 1 is used to display errors only, level 2 for both errors and warnings, and level 3 displays error, warning and informational messages. </p>
<p> Trace level 4 is called &#8216;noisy&#8217; and it is &#8211; generating many messages about the internal functioning of <code>ntop.</code> Trace level 5 and above are &#8216;noisy&#8217; plus extra logs, i.e. all possible messages, with a file:line tag prepended to every message. </p>
<p> 2 -u &#8211;user Specifies the user <code>ntop</code> should run as after it initializes. </p>
<p> <code>ntop</code> must normally be started as root so that it has sufficient privileges to open the network interfaces in promiscuous mode and to receive raw frames. See the discussion of -s | &#8211;no-promiscuous above, if you wish to try starting <code>ntop</code> as a non-root user. </p>
<p> Shortly after starting up, <code>ntop</code> becomes the user you specify here, which normally has substantially reduced privileges, such as no login shell. This is the userid which owns <code>ntop&#8217;s</code> database and output files. </p>
<p> The value specified may be either a username or a numeric user id. The group id used will be the primary group of the user specified. </p>
<p> If this parameter is not specified, ntop will try to switch first to &#8216;nobody&#8217; and then to &#8216;anonymous&#8217; before giving up. </p>
<p> NOTE: This should not be root unless you really understand the security risks. In order to prevent this by accident, the only way to run <code>ntop</code> as root is to explicitly specify -u root. <code>Don&#8217;t do it.</code> </p>
<p> -x -X <code>ntop</code> creates a new hash/list entry for each new host/TCP session seen. In case of DOS (Denial Of Service) an attacker can easily exhaust all the host available memory because ntop is creating entries for dummy hosts. In order to avoid this you can set an upper limit in order to limit the memory ntop can use. </p>
<p> 2 -w &#8211;http-server 2 -W &#8211;https-server <code>ntop</code> offers an embedded web server to present the information that has been so painstakingly gathered. An external HTTP server is NOT required NOR supported. The <code>ntop</code> web server is embedded into the application. These parameters specify the port (and optionally the address (i.e. interface)) of the <code>ntop</code> web server. </p>
<p> For example, if started with -w 3000 (the default port), the URL to access <code>ntop</code> is <a rel="nofollow" href="http://hostname:3000/.">http://hostname:3000/.</a> If started with a full specification, e.g. -w 192.168.1.1:3000, <code>ntop</code> listens on only that address/port combination. </p>
<p> If -w is set to 0 the web server will not listen for http:// connections. </p>
<p> -W operates similarly, but controls the port for the https:// connections. </p>
<p> Some examples: </p>
<p> <code>ntop -w 3000 -W 0 </code> (this is the default setting) HTTP requests on port 3000 and no HTTPS.<br />
&nbsp;<wbr> <code>ntop -w 80 -W 443 </code> Both HTTP and HTTPS have been enabled on their most common ports.<br />
&nbsp;<wbr> <code>ntop -w 0 -W 443 </code> HTTP disabled, HTTPS enabled on the common port. </p>
<p> Certain sensitive, configuration pages of the <code>ntop</code> web server are protected by a userid/password. By default, these are the user/URL administration, filter, shutdown and reset stats are password protected<br />
&nbsp;<wbr>and are accessible initially only to user&nbsp;<wbr> <code>admin</code> with a password set during the first run of <code>ntop.</code> </p>
<p> Users can modify/add/delete users/URLs using ntop itself &#8211; see the Admin tab. </p>
<p> The passwords, userids and URLs to protect with passwords are stored in a database file. Passwords are stored in an encrypted form in the database for further security. Best practices call for securing that database so that only the <code>ntop</code> user can read it. </p>
<p> There is a discussion in docs/FAQ about further securing the <code>ntop</code> environment. </p>
<p> 2 -z &#8211;disable-sessions This parameter disables TCP session tracking. Use it for better performance or when you don&#8217;t really need/care to track sessions. </p>
<p> 2 -A &#8211;set-admin-password This parameter is used to start <code>ntop</code> , set the admin password and quit. It is quite useful for installers that need to automatically set the password for the admin user. </p>
<p> -A and &#8211;set-admin-password (without a value) will prompt the user for the password. </p>
<p> You may also use this parameter to set a specific value using &#8211;set-admin-password=value. <code>The = is REQUIRED and no spaces are permitted!</code> </p>
<p> If you attempt to run <code>ntop</code> as a daemon without setting a password, a FATAL ERROR message is generated and <code>ntop</code> stops. </p>
<p> 2 -B &#8211;filter-expression Filters allows the user to restrict the traffic seen by <code>ntop</code> on just about any imaginable item. </p>
<p> The filter expression is set at run time by this parameter, but it may be changed during the <code>ntop</code> run on the Admin | Change Filter web page. </p>
<p> The basic format is <code>-B filter</code> , where the quotes are <code>REQUIRED</code> </p>
<p> The syntax of the filter expression uses the same BPF (Berkeley Packet Filter) expressions used by other packages such as tcpdump </p>
<p> For instance, suppose you are interested only in the traffic generated/received by the host jake.unipi.it. <code>ntop</code> can then be started with the following filter: </p>
<p> <code>ntop -B src host jake.unipi.it or dst host jake.unipi.it</code> </p>
<p> or in shorthand: </p>
<p> <code>ntop -B host jake.unipi.it or host jake.unipi.it</code> </p>
<p> See the &#8216;expression&#8217; section of the <code>tcpdump</code> man page &#8211; usually available at <a rel="nofollow" href="http://www.tcpdump.org/tcpdump_man.html">http://www.tcpdump.org/tcpdump_man.html</a> &#8211; for further information and the best quick guide to BPF filters currently available. </p>
<p> WARNING: If you are using complex filter expressions, especially those with =s or meaningful spaces in them, be sure and use the long option format, &#8211;filter-expression=&quot;xxxx&quot; and not -B &quot;xxxx&quot;. </p>
<p> 2 -C This instruments ntop to be used in two configurations: host and network mode. In host mode (default) ntop works as usual: the IP addresses received are those of real hosts. In host mode the IP addresses received are those of the C-class network to which the address belongs. Using ntop in network mode is extremely useful when installed in a traffic exchange (e.g. in the middle of the Internet) whereas the host mode should be used when ntop is installed on the edge of a network (e.g. inside a company). The network mode significantly reduces the amount of work ntop has to perform and it has to be used whenever ntop is used to find out how the network traffic flows and not to pin-point specific hosts. </p>
<p> 2 -D &#8211;domain This identifies the local domain suffix, e.g. ntop.org. It may be necessary, if <code>ntop</code> is having difficulty determining it from the interface. </p>
<p> 2 -F &#8211;flow-spec It is used to specify network flows similar to more powerful applications such as NeTraMet. A flow is a stream of captured packets that match a specified rule. The format is </p>
<p> <code>&lt;flow-label&gt;='&lt;matching expression&gt;'[,&lt;flow-label&gt;='&lt;matching expression&gt;&#8217;]</code> </p>
<p> , where the label is used to symbolically identify the flow specified by the expression. The expression is a bpf (Berkeley Packet Filter) expression. If an expression is specified, then the information concerning flows can be accessed following the HTML link named &#8216;List NetFlows&#8217;. </p>
<p> For instance define two flows with the following expression <code>LucaHosts=&#8217;host jake.unipi.it or host pisanino.unipi.it&#8217;,GatewayRoutedPkts=&#8217;gateway gateway.unipi.it&#8217;.</code> </p>
<p> All the traffic sent/received by hosts jake.unipi.it or pisanino.unipi.it is collected by <code>ntop</code> and added to the LucaHosts flow, whereas all the packet routed by the gateway gateway.unipi.it are added to the GatewayRoutedPkts flow. If the flows list is very long you may store in a file (for instance flows.list) and specify the file name instead of the actual flows list (in the above example, this would be &#8216;ntop -F flows.list&#8217;). </p>
<p> Note that the double quotations around the entire flow expression are required. </p>
<p> 2 -K &#8211;enable-debug Use this parameter to simplify application debug. It does three things: 1. Does not fork() on the &quot;read only&quot; html pages. 2. Displays mutex values on the configuration (info.html) page. 3. (If available &#8211; glibc/gcc) Activates an automated backtrace on application errors. </p>
<p> 2 -L &#8211;use-syslog=facility Use this parameter to send log messages to the system log instead of stdout. </p>
<p> -L and the simple form &#8211;use-syslog use the default log facility, defined as LOG_DAEMON in the #define symbol DEFAULT_SYSLOG_FACILITY in globals-defines.h. </p>
<p> The complex form, &#8211;use-syslog=facility will set the log facility to whatever value (e.g. local3, security) you specify. <code>The = is REQUIRED and no spaces are allowed!</code> </p>
<p> This setting applies both to <code>ntop</code> and to any child fork()ed for reporting. If this parameter is not specified, any fork()ed child will use the default value and will log it&#8217;s messages to the system log (this occurs because the fork()ed child must give up it&#8217;s access to the parents stdout). </p>
<p> Because various systems do not make the permissible names available, we have a table at the end of globals-core.c. Look for myFacilityNames. </p>
<p> 2 -M &#8211;no-interface-merge By default, <code>ntop </code> merges the data collected from all of the interfaces (NICs) it is monitoring into a single set of counters. </p>
<p> If you have a simple network, say a small LAN with a connection to the internet, merging data is good as it gives you a better picture of the whole network. For larger, more complex networks, this may not be desirable. You may also have other reasons for wishing to monitor each interface separately, for example DMZ vs. LAN traffic. </p>
<p> This option instructs <code>ntop</code> not to merge network interfaces together. This means that <code>ntop </code> will collect statistics for each interface and report them separately. </p>
<p> Only ONE interface may be reported on at a time &#8211; use the <code>Admin | Switch NIC </code> option on the web server to select which interface to report upon. </p>
<p> Note that activating either the netFlow and/or sFlow plugins will force the setting of -M. Once enabled, you cannot go back. </p>
<p> 2 -N &#8211;wwn-map This options names the file providing the map of WWN to FCID/VSAN ids. </p>
<p> 2 -O &#8211;output-packet-path This parameter defines the base path for the ntop-suspicious-pkts.XXX.pcap and normal packet dump files. </p>
<p> If this parameter is not specified, the default value is the config.h parameter CFG_DBFILE_DIR, which is set during ./configure from the &#8211;localstatedir= parameter. If &#8211;localstatedir is not specified, it defaults to the &#8211;prefix value plus /var (e.g. /usr/local/var). </p>
<p> Be aware that this may not be what you expect when running <code>ntop</code> as a daemon or Windows service. Setting an explicit and absolute path value is <code>STRONGLY</code> recommended if you use this facility. </p>
<p> 2 -P &#8211;db-file-path 2 -Q &#8211;spool-file-path These parameters specify where <code>ntop</code> stores database files. </p>
<p> There are two types, &#8216;temporary&#8217; &#8211; that is ones which need not be retained from <code>ntop</code> run to <code>ntop</code> run, and &#8216;permanent&#8217;, which must be retained (or recreated). </p>
<p> The &#8216;permanent&#8217; databases are the preferences, &quot;prefsCache.db&quot; and the password file, &quot;ntop_pw.db&quot;. These are stored in the -P | &#8211;db-file-path specified location. </p>
<p> Certain plugins use the -P | &#8211;db-file-path specified location for their database (&quot;LsWatch.db&quot;) or (as a default value) for files (&#8230;/rrd/&#8230;). </p>
<p> The &#8216;temporary&#8217; databases are the address queue, &quot;addressQueue.db&quot;, the cached DNS resolutions, &quot;dnsCache.db&quot; and the MAC prefix (vendor table), &quot;macPrefix.db&quot;. </p>
<p> If only -P | &#8211;db-file-path is specified, it is used for both types of databases. </p>
<p> The directories named must allow read/write and file creation by the <code>ntop</code> user. For security, nobody else should have even read access to these files. </p>
<p> Note that the default value is the config.h parameter CFG_DBFILE_DIR. This is set during ./configure from the &#8211;localstatedir= parameter. If &#8211;localstatedir is not specified, it defaults to the &#8211;prefix value plus /var (e.g. /usr/local/var). </p>
<p> This may not be what you expect when running <code>ntop</code> as a daemon or Windows service. </p>
<p> Note that on versions of <code>ntop</code> prior to 2.3, these parameters defaulted to &quot;.&quot; (the current working directory, e.g. the value returned by the pwd command) and caused havoc as it was different when <code>ntop</code> was run from the command line, vs. run via cron, vs. run from an initialization script. </p>
<p> Setting an explicit and absolute path value is <code>STRONGLY</code> recommended. </p>
<p> 2 -U &#8211;mapper Specifies the URL of the mapper.pl utility. </p>
<p> If provided, <code>ntop</code> creates a clickable hyperlink on the &#8216;Info about host xxxxxx&#8217; page to this URL by appending ?host=xxxxx. Any type of host lookup could be performed, but this is intended to lookup the geographical location of the host. </p>
<p> A cgi-based mapper interface to <a rel="nofollow" href="http://www.multimap.com">http://www.multimap.com</a> is part of the <code>ntop </code> distribution [see www/Perl/mapper.pl]). </p>
<p> 2 -V &#8211;version Prints <code>ntop </code> version information and then exits. </p>
<p> 2 -W &#8211;https-server (See the joint documentation with the -w parameter, above) </p>
<p> &#8211;disable-instantsessionpurge <code>ntop</code> sets completed sessions as &#8216;timed out&#8217; and then purge them almost instantly, which is not the behavior you might expect from the discussions about purge timeouts. This switch makes ntop respect the timeouts for completed sessions. It is NOT the default because a busy web server may have 100s or 1000s of completed sessions and this would significantly increase the amount of memory <code>ntop</code> uses. </p>
<p> &#8211;disable-mutexextrainfo <code>ntop</code> stores extra information about the locks and unlocks of the protective mutexes it uses. Since <code>ntop</code> uses fine-grained locking, this information is updated frequently. On some OSes, the system calls used to collect this informatio (getpid() and gettimeofday()) are expensive. This option disables the extra information. It should have no processing impact on <code>ntop</code><br />
&nbsp;<wbr>&#8211; however should <code>ntop</code> actually deadlock, we would lose the information that sometimes tells us why. </p>
<p> &#8211;disable-schedyield <code>ntop</code> uses sched_yield() calls for better interactive performance. Under some situations, primarily under RedHat Linux 8.0, this can deadlock, causing the <code>ntop</code> web server to stop responding, although <code>ntop</code> appears to still be operational according to the ps command. Use this switch to disable these calls, IF you are seeing deadlocks. </p>
<p> &#8211;disable-stopcap Return <code>ntop </code> to the old (v2.1) behavior on a memory error. The default of stopcap enabled makes the web interface available albeit with static content until <code>ntop</code> is shutdown. </p>
<p> &#8211;fc-only </p>
<p> Display only Fibre Channel statistics. </p>
<p> &#8211;instance </p>
<p> You can run multiple instances of <code>ntop</code> simultaneously by specifying different -P values (typically through separate ntop.conf files). If you set a value for this parameter (available only on the command line), you (1) display the &#8216;instance&#8217; name on every web page and (2) alter the log prefix from &quot;NTOP&quot; to your chosen value. </p>
<p> If you want to make the tag more obvious, create a .instance class in style.css, e.g.: </p>
<p>.instance&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>color:&nbsp;<wbr>#666666;<br />
&nbsp;<wbr>&nbsp;<wbr>font-size: 18pt;<br />
} </p>
<p> Note (UNIX): To run completely different versions of the <code>ntop</code> binary, you need to compile and install into a different library (using ./configure &#8211;prefix) and then specify the LD_LIBRARY_PATH before invoking, e.g. </p>
<p> LD_LIBRARY_PATH=/devel/lib/ntop/:&#8230; /devel/bin/ntop &#8230;args&#8230; </p>
<p> If present, a file of the form &lt;instance&gt;_ntop_logo.gif will be used instead of the normal ntop_logo.gif. This is tested for ONLY once, at the beginning of the run. The EXACT word(s) of the &#8211;instance flag are used, without testing if they make a proper file name. If &#8211; for any reason &#8211; the file is not found, an informational message is logged and the normal logo file is used. To construct your own logo, make it a 300&#215;40 transparent gif. </p>
<p> NOTE: On the web pages, <code>ntop </code> uses the dladdr() function. The original Solaris routine had a bug, replicated in FreeBSD (and possibly other places) where it uses the ARGV[0] value &#8211; which might be erroneous &#8211; instead of the actual file name. If the &#8216;running from&#8217; value looks bogus but the &#8216;libaries in&#8217; value looks ok, go with the libarary. </p>
<p> &#8211;no-fc </p>
<p> Disable processing &amp; Display of Fibre Channel </p>
<p> &#8211;no-invalid-lun </p>
<p> Don&#8217;t display Invalid LUN information. </p>
<p> &#8211;p3p-cp &#8211;p3p-uri </p>
<p> P3P is a W3C recommendation &#8211; <a rel="nofollow" href="http://www.w3.org/TR/P3P/">http://www.w3.org/TR/P3P/</a> &#8211; for specifying personal information a site collects and what it does with the information. These parameters allow to return P3P information. We do not supply samples. </p>
<p> &#8211;pcap_setnonblock On some platforms, the <code>ntop </code> web server will hang or appear to hang (it actually just responds incredibly slowly to the first request from a browser session), while the rest of <code>ntop</code> runs just fine. This is known to be an issue under FreeBSD 4.x. </p>
<p> This option sets the non-blocking option (assuming it&#8217;s available in the version of libpcap that is installed). </p>
<p> While this works around the problem (by turing an interupt driven process into a poll), it also MAY signifcantly increases the cpu usage of <code>ntop.</code> Although it does not actually interfere with other work, seeing <code>ntop</code> use 80-90% or more of the cpu is not uncommon &#8211; don&#8217;t say we didn&#8217;t warn you. </p>
<p> <code>THIS OPTION IS OFFICIALLY UNSUPPORTED</code> and used at your own risk. Read the docs/FAQ write-up. </p>
<p> &#8211;skip-version-check By default, <code>ntop</code> accesses a remote file to periodically check if the most current version is running. This option disables that check. Please review the privacy notice at the bottom of this page for more information. By default, the recheck period is slightly more than 15 days. This can be adjusted via a constant in globals-defines.h. If the result of the initial check indicates that the <code>ntop</code> version is a &#8216;new development&#8217; version (that is newer than the latest published development version), the recheck is disabled. This is because which fixes and enhancements were present/absent from the code. </p>
<p> NOTE: At present, the recheck does not work under Windows. </p>
<p> &#8211;ssl-watchdog </p>
<p> Enable a watchdog for webserver hangs. These usually happen when connecting with older browsers. The user gets nothing back and other users can&#8217;t connect. Internally, packet processing continues but there is no way to access the data through the web server or shutdown ntop cleanly. With the watchdog, a timeout occurs after 3 seconds, and processing continues with a log message. Unfortunately, the user sees nothing &#8211; it just looks like a failed connection. (also available as a ./configure option, &#8211;enable-sslwatchdog)<br />
&nbsp;<wbr> &#8211;w3c By default, <code>ntop</code> generates displayable but not great html. There are a number of tags we do not generate because they cause problems with older browsers which are still commonly used or are important to look good on real-world browsers. This flag tells <code>ntop</code> to generate &#8216;BETTER&#8217; (but not perfect) w3c compliant html 4.01 output. This in no way addresses all of the compatibility and markup issues. Over time, we would like to make <code>ntop</code> more compatible, but it will never be 100%. If you find any issues, please report them to ntop-dev. </p>
<p> 2 -4 &#8211;ipv4 Use IPv4 connections. </p>
<p> 2 -6 &#8211;ipv6 Use IPv6 connections</p>
<h2>Web Views</h2>
<p>While <code>ntop</code> is running, multiple users can access the traffic information using their web browsers. <code>ntop</code> does not generate &#8216;fancy&#8217; or &#8216;complex&#8217; html, although it does use frames, shallowly nested tables and makes some use of JavaScript and Cascading Style Sheets. </p>
<p> Beginning with release 3.1, the menus are cascading dropdowns via JSCookMenu. With release 3.2, this extends to plugins. </p>
<p> We do not expect problems with any current web browser, but our ability to test with less common ones is very limited. Testing has included Firefox and Internet Explorer, with very limited testing on other current common browsers such as Opera. </p>
<p> In documentation and this man page, when we refer to a page such as Admin | Switch NIC, we mean the Broad category &quot;Admin&quot; and the detailed item &quot;Switch NIC&quot; on that Admin menu.</p>
<h2>Notes</h2>
<p><code>ntop</code> requires a number of external tools and libraries to operate. Certain other tools are optional, but add to the program&#8217;s capabilities. &#8211;webserver-queue Specifies the maximum number of web server requests for the tcp/ip stack to retain in it&#8217;s queue awaiting delivery to the <code>ntop</code> web server. Requests in excess of this queue may be dropped (allowing for retransmission) or rejected at the tcp/ip stack level, depending upon the OS. Whatever happens, happens at the OS level, without any information being delivered to <code>ntop</code> Required libraries include: <code>libpcap</code> from <a rel="nofollow" href="http://www.tcpdump.org/,">http://www.tcpdump.org/,</a> version 0.7.2 or newer. 0.8.3 or newer is strongly recommended. The Windows version makes use of <code>WinPcap</code> (libpcap for Windows) which may be downloaded from <a rel="nofollow" href="http://winpcap.polito.it/install/default.htm.">http://winpcap.polito.it/install/default.htm.</a> WARNING: The 2.x releases of <code>WinPcap</code> will NOT support SMP machines. <code>gdbm</code> from <a rel="nofollow" href="http://www.gnu.org/software/gdbm/gdbm.html">http://www.gnu.org/software/gdbm/gdbm.html</a> <code>ntop</code> requires a POSIX threads library. As of <code>ntop</code> 3.2, the single-threaded version of <code>ntop</code> is no longer available. The <code>gd</code> 2.x library, for the creation of png files, available at <a rel="nofollow" href="http://www.boutell.com/gd/.">http://www.boutell.com/gd/.</a> The <code>libpng</code> 1.2.x library, for the creation of png files, available at <a rel="nofollow" href="http://www.libpng.org/pub/png/libpng.html.">http://www.libpng.org/pub/png/libpng.html.</a> <code>ntop </code> should support both gd 1.X and libpng 1.0.x libraries but this has not been tested. Note that there are incompatibilities if you compile with one version of these libraries and then run with the other. Please read the discussion in docs/FAQ before reporting ANY problems of this nature. (if an https:// server is desired) <code>openSSL</code> from the OpenSSL project available at <a rel="nofollow" href="http://www.openssl.org.">http://www.openssl.org.</a> The <code>rrdtool</code> library is required by the rrd plugin. rrdtool creates &#8216;Round-Robin databases&#8217; which are used to store and graph historical data in a format that permits long duration retention without growing larger over time. The rrdtool home page is <a rel="nofollow" href="http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/">http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/</a> <code>ntop</code> includes a limited version of rrdtool 1.0.49 in the myrrd/ directory. Users of <code>ntop </code> 3.2 should not need to specifically install rrdtool. The <code>sflow</code> Plugin is courtesy of and supported by InMon Corporation, <a rel="nofollow" href="http://www.inmon.com/sflowTools.htm.">http://www.inmon.com/sflowTools.htm.</a> There are other optional libraries. See the output of ./configure for a fuller listing. Tool locations are current as of August 2005 &#8211; please send email to report new locations or dead links. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a></code>(8). <code><a href="/docs/linux/man/3-pcap/">pcap</a></code>(3). </p>
<h2>Privacy Notice</h2>
<p>By default at startup and at periodic intervals, the <code>ntop</code> program will retrieve a file containing current ntop program version information. Retrieving this file allows this <code>ntop</code> instance to confirm that it is running the most current version. </p>
<p> The retrieval is done using standard http:// requests, which will create log records on the hosting system. These log records do contain information which identifies a specific <code>ntop</code> site. Accordingly, you are being notified that this individually identifiable information is being transmitted and recorded. </p>
<p> You may request &#8211; via the <code>&#8211;skip-version-check</code> run-time option &#8211; that this check be eliminated. If you use this option, no individually identifiable information is transmitted or recorded, because the entire retrieval and check is skipped. </p>
<p> We ask you to allow this retrieval and check, because it benefits both you and the <code>ntop</code> developers. It benefits you because you will be automatically notified if the <code>ntop</code> program version is obsolete, becomes unsupported or is no longer current. It benefits the developers of <code>ntop</code> because it allows us to determine the number of active <code>ntop</code> instances, and the operating system/versions that users are running <code>ntop</code> under. This allows us to focus development resources on systems like those our users are using <code>ntop</code> on. </p>
<p> The individually identifiable information is contained in the web server log records which are automatically created each time the version file is retrieved. This is a function of the web server and not of <code>ntop</code> , but we do take advantage of it. The log record shows the IP address of the requestor (the <code>ntop</code> instance) and a User-Agent header field. We place information in the User-Agent header as follows: </p>
<p>&nbsp;<wbr>ntop/&lt;version&gt;&nbsp;<wbr><br />
&nbsp;<wbr>host/&lt;name from config.guess&gt;<br />
&nbsp;<wbr>distro/&lt;if one&gt;<br />
&nbsp;<wbr>release/&lt;of the distro, also if one&gt;&nbsp;<wbr><br />
&nbsp;<wbr>kernrlse/&lt;kernel version or release&gt;&nbsp;<wbr><br />
&nbsp;<wbr>GCC/&lt;version&gt;<br />
&nbsp;<wbr>config()&nbsp;<wbr>&lt;condensed parameters from ./configure&gt;<br />
&nbsp;<wbr>run()&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;condensed flags &#8211; no data &#8211; from the execution line&gt;<br />
&nbsp;<wbr>libpcap/&lt;version&gt;<br />
&nbsp;<wbr>gdbm/&lt;version&gt;<br />
&nbsp;<wbr>openssl/&lt;version&gt;<br />
&nbsp;<wbr>zlib/&lt;version&gt;<br />
&nbsp;<wbr>access/&lt;http, https, both or none&gt;<br />
&nbsp;<wbr>interfaces()&nbsp;<wbr>&lt;given interface names&gt; </p>
<p> For example: </p>
<p>&nbsp;<wbr>ntop/2.2.98 host/i686-pc-linux-gnu distro/redhat release/9 kernrlse/2.4.20-8smp<br />
&nbsp;<wbr>GCC/3.2.2 config(i18n)&nbsp;<wbr>run(i;&nbsp;<wbr>u;&nbsp;<wbr>P;&nbsp;<wbr>w;&nbsp;<wbr>t;&nbsp;<wbr>logextra;&nbsp;<wbr>m;&nbsp;<wbr>instantsessionpurge;&nbsp;<wbr><br />
&nbsp;<wbr>schedyield;&nbsp;<wbr>d;&nbsp;<wbr>usesyslog=;&nbsp;<wbr>t)&nbsp;<wbr>gdbm/1.8.0 openssl/0.9.7a zlib/1.1.4<br />
&nbsp;<wbr>access/http interfaces(eth0,eth1) </p>
<p> Distro and release information is determined at compile time and consists of information typically found in the /etc/release (or similar) file. See the <code>ntop</code> tool linuxrelease for how this is determined. </p>
<p> gcc compiler version (if available) is the internal version #s for the gcc compiler, e.g. 3.2.3. </p>
<p> kernrlse is the Linux Kernel version or the xBSD &#8216;release&#8217; such as 4.9-RELEASE and is determined from the uname data (if it&#8217;s available). </p>
<p> The ./configure parameters are stripped of directory paths, leading -s, etc. to create a short form that shows us what ./configure parameters people are using. </p>
<p> Similarly, the run time parameters are stripped of data and paths, just showing which flags are being used. </p>
<p> The libpcap, gdbm, openssl and zlib versions come from the strings returned by the various inquiry functions (if they&#8217;re availabe). </p>
<p> Here&#8217;s a sample log record: </p>
<p> 67.xxx.xxx.xxx &#8211; &#8211; [28/Dec/2003:12:11:46 -0500] &quot;GET /version.xml HTTP/1.0&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>200 1568&nbsp;<wbr><a rel="nofollow" href="http://www.burtonstrauss.com">www.burtonstrauss.com</a>&nbsp;<wbr>&quot;-&quot;&nbsp;<wbr>&quot;ntop/2.2.98 host/i686-pc-linux-gnu<br />
&nbsp;<wbr>&nbsp;<wbr>distro/redhat release/9 kernrlse/2.4.20-8smp GCC/3.2.2 config(i18n)<br />
&nbsp;<wbr>&nbsp;<wbr>run(i;&nbsp;<wbr>u;&nbsp;<wbr>P;&nbsp;<wbr>w;&nbsp;<wbr>t;&nbsp;<wbr>logextra;&nbsp;<wbr>m;&nbsp;<wbr>instantsessionpurge;&nbsp;<wbr>schedyield;&nbsp;<wbr>d;<br />
&nbsp;<wbr>&nbsp;<wbr>usesyslog=)&nbsp;<wbr>libpcap/0.8 gdbm/1.8.0 openssl/0.9.7a zlib/1.1.4 access/http<br />
&nbsp;<wbr>&nbsp;<wbr>interfaces(eth0,eth1,eth2)&quot;&nbsp;<wbr>&quot;-&quot;</p>
<h2>User Support</h2>
<p>Please send bug reports to the ntop-dev &lt;ntop-dev [at] ntop.org&gt; mailing list. The ntop &lt;ntop [at] ntop.org&gt; mailing list is used for discussing ntop usage issues. In order to post messages on the lists a (free) subscription is required to limit/avoid spam. Please do NOT contact the author directly unless this is a personal question. </p>
<p> Commercial support is available upon request. Please see the ntop site for further info. </p>
<p> Please send code patches to &lt;patch [at] ntop.org&gt;.</p>
<h2>Author</h2>
<p>ntop&#8217;s author is Luca Deri (<a rel="nofollow" href="http://luca.ntop.org/)">http://luca.ntop.org/)</a> who can be reached at &lt;deri [at] ntop.org&gt;.</p>
<h2>Licence</h2>
<p>ntop is distributed under the GNU GPL licence (<a rel="nofollow" href="http://www.gnu.org/">http://www.gnu.org/</a>).</p>
<h2>Acknowledgments</h2>
<p>The author acknowledges the Centro Serra of the University of Pisa, Italy (<a rel="nofollow" href="http://www-serra.unipi.it/)">http://www-serra.unipi.it/)</a> for hosting the ntop sites (both web and mailing lists), and Burton Strauss &lt;burton [at] ntopsupport.com&gt; for his help and user assistance. Many thanks to Stefano Suin &lt;stefano [at] ntop.org&gt; and Rocco Carbone &lt;rocco [at] ntop.org&gt; for contributing to the project.</p>
