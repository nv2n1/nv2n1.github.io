---
title: "argus-conf(5)"
name: "argus-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-argus-conf/"
description: "argus.conf – argus resource file."
---

<p><code>argus.conf</code> &#8211; <code>argus</code> resource file.</p>
<h2>Synopsis</h2>
<p><code>argus.conf</code></p>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2015 QoSient, LLC All rights reserved.</p>
<h2>Description</h2>
<p>This is the canonical argus configuration file. All options that argus supports can be turned on or modified using this configuration format. Argus will search for a system /etc/argus.conf file and will open it and use it to seed all configuration options.conf. Previous versions of Argus supported searching for argus.conf in $ARGUSPATH, $ARGUSHOME, $ARGUSHOME/lib, $HOME, and $HOME/lib, but this support is deprecated. All values in this file can be overriden by command line options, or other configuration files of this format when specified in using the -F option. Argus will read any number of configuration files using the -F option, and command-line order is very important. </p>
<h2>Variable Syntax</h2>
<p>Variable assignments must be of the form: </p>
<pre> VARIABLE=</pre>
<p>with no white space between the VARIABLE and the &#8216;=&#8217; sign. Quotes are optional for string arguments, but if you want to embed comments, then quotes are required.</p>
<h2>Argus_Flow_Type / Argus_Flow_Key</h2>
<p>The Argus can be configured to support a large number of flow types. The Argus can provide either type, i.e. uni-directional or bi-directional flow tracking and the flow can be further defined by specifying the key. The argus supports a set of well known key strategies, such as &#8216;CLASSIC_5_TUPLE&#8217;, &#8216;LAYER_3_MATRIX&#8217;, &#8216;LAYER_2_MATRIX&#8217;, formulate key strategies from a list of the specific objects that the Argus understands. See the man page for a complete description. </p>
<p> The default is the classic 5-tuple IP flow, CLASSIC_5_TUPLE. </p>
<p> There is no commandline equivalent. </p>
<pre><code>ARGUS_FLOW_TYPE=</code>&quot;Bidirectional&quot;
<code>ARGUS_FLOW_KEY=</code>&quot;CLASSIC_5_TUPLE&quot;</pre>
<h2>Argus_Daemon</h2>
<p>Argus is capable of running as a daemon, doing all the right things that daemons do. When this configuration is used for the system daemon process, say for /etc/argus.conf, this variable should be set to &quot;yes&quot;. </p>
<p> In the examples seen in the ./support/Startup/argus scripts, this value is set to &quot;yes&quot;, as the system startup strategy requires the program to daemonize themselves, returning a value to the system, hopefully quickly. Some systems, however, want to daemonize the tasks themselves, and those cases, the value must be set to &quot;no&quot;. </p>
<p> which requires that this variable be set to &quot;yes&quot;. </p>
<p> The default value is to not run as a daemon. </p>
<p> Commandline equivalent -d </p>
<p> <code>ARGUS_DAEMON=</code>no</p>
<h2>Argus_Monitor_Id</h2>
<p>Argus Monitor Data is uniquely identifiable based on the source identifier that is included in each output record. This is to allow you to work with Argus Data from multiple monitors at the same time. The ID is 32 bits long, and argus suppors a number of formats as legitimate values. Argus support unsigned ints, IPv4 addresses and 4 bytes strings, as values. </p>
<p> The formats are discerned from the values provided. Double-quoted values are treated as strings, and are truncated to 4 characters. Non-quoted values are tested for whether they are hostnames, and if not, then they are tested wheter they are numbers. </p>
<p> The configuration allows for you to use host names, however, do have some understanding how `hostname` will be resolved by the nameserver before commiting to this strategy completely. </p>
<p> For convenience, argus supports the notion of &quot;`hostname`&quot; for assigning the probe&#8217;s id. This is to support management of large deployments, so you can have one argus.conf file that works for a lot of probes. </p>
<p> For security, argus does not rely on system programs, like hostname.1. It implements the logic of hostname itself, so don&#8217;t try to run arbitrary programs using this method, because it won&#8217;t work. </p>
<p> Commandline equivalent -e </p>
<pre><code>ARGUS_MONITOR_ID</code>=`hostname` // IPv4 address returned
<code>ARGUS_MONITOR_ID</code>=10.2.45.3 // IPv4 address
<code>ARGUS_MONITOR_ID</code>=2435 // Number
<code>ARGUS_MONITOR_ID</code>=&quot;en0&quot; // String</pre>
<h2>Argus_Access_Port</h2>
<p>Argus monitors can provide a real-time remote access port for collecting Argus data. This is a TCP based port service and the default port number is tcp/561, the &quot;experimental monitor&quot; service. This feature is disabled by default, and can be forced off by setting it to zero (0). </p>
<p> When you do want to enable this service, 561 is a good choice, as all ra* clients are configured to try this port by default. </p>
<p> Commandline equivalent -P </p>
<p> <code>ARGUS_ACCESS_PORT=</code>561</p>
<h2>Argus_Bind_Ip</h2>
<p>When remote access is enabled (see above), you can specify that Argus should bind only to a specific IP address. This is useful, for example, in restricting access to the local host, or binding to a private interface while capturing from another. </p>
<p> You can provide multiple addresses, separated by commas, or on multiple lines. </p>
<p> The default is to bind to any IP address. </p>
<p> Commandline equivalent -B </p>
<pre><code>ARGUS_BIND_IP=</code>&quot;::1,127.0.0.1&quot;
<code>ARGUS_BIND_IP=</code>&quot;127.0.0.1&quot;
<code>ARGUS_BIND_IP=</code>&quot;192.168.0.68&quot;</pre>
<h2>Argus_Interface</h2>
<p>By default, Argus will open the first appropriate interface on a system that it encounters. For systems that have only one network interface, this is a reasonable thing to do. But, when there are more than one suitable interface, you should specify the interface(s) Argus should use either on the command line or in this file. </p>
<p> Argus can track packets from any or all interfaces, concurrently. The interfaces can be tracked as:<br />
&nbsp;<wbr>&nbsp;<wbr>1.&nbsp;<wbr>&nbsp;<wbr>independant &#8211; this is where argus tracks flows from each<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interface independant from the packets seen on any other<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interface.&nbsp;<wbr>&nbsp;<wbr>This is useful for hosts/routers that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>have full-duplex interfaces, and you want to distinguish<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>flows based on their interface. There is an option to specify<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a distinct srcid to each independant modeler. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>2.&nbsp;<wbr>&nbsp;<wbr>duplex &#8211; where argus tracks packets from 2 interfaces<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>as if they were two half duplex streams of the same link.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Because there is a single modeler tracking the 2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interfaces, there is a single srcid that can be passed as<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>an option. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>3.&nbsp;<wbr>&nbsp;<wbr>bonded &#8211; where argus tracks packets from multiple interfaces<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>as if they were from the same stream.&nbsp;<wbr>&nbsp;<wbr>Because there is a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>single modeler tracking the 2 interfaces, there is a single<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>srcid that can be passed as an option. </p>
<p>&nbsp;<wbr>Interfaces can be specified as groups using&nbsp;<wbr>&#8216;[&#8216;,&#8217;]&#8217;&nbsp;<wbr>notation, to build<br />
&nbsp;<wbr>flexible definitions of packet sources.&nbsp;<wbr>&nbsp;<wbr>However, each interface<br />
&nbsp;<wbr>should be referenced only once&nbsp;<wbr>(this is due to performance and OS<br />
&nbsp;<wbr>limitations, so if your OS has no problem with this, go ahead). </p>
<p>&nbsp;<wbr>The lo&nbsp;<wbr>(loopback)&nbsp;<wbr>interface will be included only if it is specifically<br />
&nbsp;<wbr>indicated in the option. </p>
<p>&nbsp;<wbr>The syntax for specifying this either on the command line or in this file:<br />
&nbsp;<wbr>-i ind:all<br />
&nbsp;<wbr>-i dup:en0,en1/srcid<br />
&nbsp;<wbr>-i bond:en0,en1/srcid<br />
&nbsp;<wbr>-i dup:[bond:en0,en1],en2/srcid<br />
&nbsp;<wbr>-i en0/srcid -i en1/srcid&nbsp;<wbr>&nbsp;<wbr>(equivalent&nbsp;<wbr>&#8216;-i ind:en0/srcid,en1/srcid&#8217;)<br />
&nbsp;<wbr>-i en0 en1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(equivalent&nbsp;<wbr>&#8216;-i bond:en0,en1&#8217;) </p>
<p>&nbsp;<wbr>In all cases, if there is a&nbsp;<wbr>&quot;-e srcid&quot;&nbsp;<wbr>provided, this is used as the<br />
&nbsp;<wbr>default.&nbsp;<wbr>&nbsp;<wbr>If a srcid is specified using this option, it overrides<br />
&nbsp;<wbr>the default. </p>
<p>&nbsp;<wbr>Srcid&#8217;s are specified using the notion used for ARGUS_MONITOR_ID, as above. </p>
<p> Commandline equivalent -i </p>
<pre><code>ARGUS_INTERFACE</code>=any
<code>ARGUS_INTERFACE</code>=ind:all
<code>ARGUS_INTERFACE</code>=ind:en0/192.168.0.68,en2/192.168.2.1
<code>ARGUS_INTERFACE</code>=ind:en0/&quot;en0&quot;,en2/19234
<code>ARGUS_INTERFACE</code>=en0</pre>
<h2>Argus_Go_Promiscuous</h2>
<p>By default, Argus will put its interface in promiscuous mode in order to monitor all the traffic that can be collected. This can put an undo load on systems. </p>
<p> If the intent is to monitor only the network activity of the specific system, say to measure the performance of an HTTP service or DNS service, you&#8217;ll want to turn promiscuous mode off. </p>
<p> The default value goes into prmiscuous mode. </p>
<p> Commandline equivalent -p </p>
<pre><code>ARGUS_GO_PROMISCUOUS=</code>yes</pre>
<h2>Argus_Chroot_Dir</h2>
<p>Argus supports <a href="/docs/linux/man/2-chroot/">chroot</a>(2) in order to control the file system that argus exists in and can access. Generally used when argus is running with privileges, this limits the negative impacts that argus could inflict on its host machine. </p>
<p> This option will cause the output file names to be relative to this directory, and so consider this when trying to find your output files. </p>
<p> Commandline equivalent -c dir </p>
<pre><code>ARGUS_CHROOT_DIR=</code>/chroot_dir</pre>
<h2>Argus_Setuser_Id</h2>
<p>Argus can be directed to change its user id using the setuid() system call. This is can used when argus is started as root, in order to access privileged resources, but then after the resources are opened, this directive will cause argus to change its user id value to a &#8216;lesser&#8217; capable account. Recommended when argus is running as daemon. </p>
<p> Commandline equivalent -u user </p>
<pre><code>ARGUS_SETUSER_ID=</code>user</pre>
<h2>Argus_Setgroup_Id</h2>
<p>Argus can be directed to change its group id using the setgid() system call. This is can used when argus is started as root, in order to access privileged resources, but then after the resources are opened, this directive can be used to change argu&#8217;s group id value to a &#8216;lesser&#8217; capable account. Recommended when argus is running as daemon. </p>
<p> Commandline equivalent -g group </p>
<pre><code>ARGUS_SETGROUP_ID=</code>group</pre>
<h2>Argus_Output_File</h2>
<p>Argus can write its output to one or a number of files, default limit is 5 concurrent files, each with their own independant filters. </p>
<p> The format is: </p>
<pre> ARGUS_OUTPUT_FILE=/full/path/file/name
 ARGUS_OUTPUT_FILE=/full/path/file/name &quot;filter&quot;</pre>
<p>Most sites will have argus write to a file, for reliablity and performance. The example file name is used here as supporting programs, such as ./support/Archive/argusarchive are configured to use this file. </p>
<p> Commandline equivalent -w </p>
<pre><code>ARGUS_OUTPUT_FILE=</code>/var/log/argus/argus.out</pre>
<h2>Argus_Output_Stream</h2>
<p>Argus can write its output to one or a number of remote hosts. The default limit is 5 concurrent output streams, each with their own independant filters. </p>
<p> The format is:<br />
&nbsp;<wbr>&nbsp;<wbr>ARGUS_OUTPUT_STREAM=&quot;URI&nbsp;<wbr>[filter]&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>ARGUS_OUTPUT_STREAN=&quot;argus-<a href="udp://host:port">udp://host:port</a>&nbsp;<wbr>&#8216;tcp and not udp&#8217;&quot; </p>
<p> Most sites will have argus listen() for remote sites to request argus data, but for some sites and applications sending records without registration is desired. This option will cause argus to transmit records that match the optional filter, to the configured targets using UDP as the transport mechanism. </p>
<p> Commandline equivalent -w argus-<a href="udp://host:port">udp://host:port</a> </p>
<pre><code>ARGUS_OUTPUT_STREAM=</code>argus-<a href="udp://224.0.20.21:561">udp://224.0.20.21:561</a></pre>
<h2>Argus_Set_Pid</h2>
<p>When Argus is configured to run as a daemon, with the -d option, Argus can store its pid in a file, to aid in managing the running daemon. However, creating a system pid file requires privileges that may not be appropriate for all cases. </p>
<p> When configured to generate a pid file, if Argus cannot create the pid file, it will fail to run. This variable, and the directory the pid is written to, is available to override the default, in case this gets in your way. </p>
<p> The default value is to generate a pid. The default path for the pid file, is &#8216;/var/run&#8217;. </p>
<p> No Commandline equivalent </p>
<pre><code>ARGUS_SET_PID=</code>yes
<code>ARGUS_PID_PATH=</code>/var/run</pre>
<h2>Argus_Flow_Status_Interval</h2>
<p>Argus will periodically report on a flow&#8217;s activity every ARGUS_FLOW_STATUS_INTERVAL seconds, as long as there is new activity on the flow. This is so that you can get a view into the activity of very long lived flows. The default is 60 seconds, but this number may be too low or too high depending on your uses. </p>
<p> The default value is 60 seconds, but argus does support a minimum value of 1. This is very useful for doing measurements in a controlled experimental environment where the number of flows is &lt; 1000. </p>
<p> Commandline equivalent -S </p>
<p> <code>ARGUS_FLOW_STATUS_INTERVAL=</code>60</p>
<h2>Argus_Mar_Status_Interval</h2>
<p>Argus will periodically report on a its own health, providing interface status, total packet and bytes counts, packet drop rates, and flow oriented statistics. </p>
<p> These records can be used as &quot;keep alives&quot; for periods when there is no network traffic to be monitored. </p>
<p> The default value is 300 seconds, but a value of 60 seconds is very common. </p>
<p> Commandline equivalent -M </p>
<p> <code>ARGUS_MAR_STATUS_INTERVAL=</code>300</p>
<h2>Argus_Debug_Level</h2>
<p>If compiled to support this option, Argus is capable of generating a lot of debug information. </p>
<p> The default value is zero (0). </p>
<p> Commandline equivalent -D </p>
<p> <code>ARGUS_DEBUG_LEVEL=</code>0</p>
<h2>Argus_Generate_Packet_Size</h2>
<p>Argus can be configured to generate packet size information on a per flow basis, which provides the max and min packet size seen . The default value is to not generate this data. </p>
<p> Commandline equivalent -Z </p>
<pre><code>ARGUS_GENERATE_PACKET_SIZE=</code>yes</pre>
<h2>Argus_Generate_Jitter_Data</h2>
<p>Argus can be configured to generate packet jitter information on a per flow basis. The default value is to not generate this data. </p>
<p> Commandline equivalent -J </p>
<p>&nbsp;<wbr> <code>ARGUS_GENERATE_JITTER_DATA=</code>no</p>
<h2>Argus_Generate_Mac_Data</h2>
<p>Argus can be configured to not provide MAC addresses in it audit data. This is available if MAC address tracking and audit is not a requirement. </p>
<p> The default value is to not generate this data. </p>
<p> Commandline equivalent -m </p>
<pre><code>ARGUS_GENERATE_MAC_DATA=</code>no</pre>
<h2>Argus_Generate_Appbyte_Metric</h2>
<p>Argus can be configured to generate metrics that include the application byte counts as well as the packet count and byte counters. </p>
<p> Commandline equivalent -A<br />
&nbsp;<wbr> </p>
<pre><code>ARGUS_GENERATE_APPBYTE_METRIC=</code>no</pre>
<h2>Argus_Generate_Tcp_Perf_Metric</h2>
<p>Argus by default, generates extended metrics for TCP that include the connection setup time, window sizes, base sequence numbers, and retransmission counters. You can suppress this detailed information using this variable. </p>
<p> No commandline equivalent </p>
<pre><code>ARGUS_GENERATE_TCP_PERF_METRIC=</code>yes</pre>
<h2>Argus_Generate_Bidirectional_Timestamps</h2>
<p>Argus by default, generates a single pair of timestamps, for the first and last packet seen on a given flow, during the obseration period. For bi-directional flows, this results in loss of some information. By setting this variable to &#8216;yes&#8217;, argus will store start and ending timestamps for both directions of the flow. </p>
<p> No commandline equivalent </p>
<pre><code>ARGUS_GENERATE_BIDIRECTIONAL_TIMESTAMPS=</code>no</pre>
<h2>Argus_Capture_Data_Len</h2>
<p>Argus can be configured to capture a number of user data bytes from the packet stream. </p>
<p> The default value is to not generate this data. </p>
<p> Commandline equivalent -U </p>
<p>&nbsp;<wbr> <code>ARGUS_CAPTURE_DATA_LEN=</code>0</p>
<h2>Argus_Filter_Optimizer</h2>
<p>Argus uses the packet filter capabilities of libpcap. If there is a need to not use the libpcap filter optimizer, you can turn it off here. The default is to leave it on. </p>
<p> Commandline equivalent -O </p>
<p> <code>ARGUS_FILTER_OPTIMIZER=</code>yes</p>
<h2>Argus_Filter</h2>
<p>You can provide a filter expression here, if you like. It should be limited to 2K in length. The default is to not filter. </p>
<p> No Commandline equivalent </p>
<p> <code>ARGUS_FILTER=</code>&quot;&quot;</p>
<h2>Argus_Packet_Capture_File</h2>
<p>Argus allows you to capture packets in tcpdump() format if the source of the packets is a tcpdump() formatted file or live packet source. </p>
<p> Specify the path to the packet capture file here. </p>
<pre><code>ARGUS_PACKET_CAPTURE_FILE=</code>&quot;/var/log/argus/packet.out&quot;</pre>
<h2>Argus_Ssf</h2>
<p>Argus supports the use of SASL to provide strong authentication and confidentiality protection. </p>
<p> The policy that argus uses is controlled through the use of a minimum and maximum allowable protection strength, which is standard for SASL based appliations. Set these variable to control this policy. The default is no security policy. </p>
<pre><code>ARGUS_MIN_SSF=</code>0
<code>ARGUS_MAX_SSF=</code>0</pre>
<h2>Argus_Pcap_Buf_Size</h2>
<p>Argus supports setting the pcap buffer size. You can use the abbreviations K, M, G to specify thousands, millions or billions of bytes. </p>
<pre><code>ARGUS_PCAP_BUF_SIZE=</code>1G</pre>
<h2>Argus_Env</h2>
<p>Argus supports setting environment variables to enable functions required by the kernel or shared libraries. This feature is intended to support libraries such as the net pf_ring support for libpcap as supported by code at <a rel="nofollow" href="http://public.lanl.gov/cpw/">http://public.lanl.gov/cpw/</a> </p>
<p> Setting environment variables in this way does not affect internal argus variable in any way. As a result, you can&#8217;t set ARGUS_PATH using this feature. </p>
<p> Care should must be taken to assure that the value given the variable conform&#8217;s to your systems putenv.3 system call. You can have as many of these directives as you like. </p>
<p> The example below is intended to set a libpcap ring buffer length to 300MB, if your system supports this feature. </p>
<pre><code>ARGUS_ENV=</code>&quot;PCAP_MEMORY=300000&quot;</pre>
<h2>Argus_Tunnel_Discovery</h2>
<p>Argus can be configured to discover tunneling protocols above the UDP transport header, specifically Teredo (IPv6 over UDP). The algorithm is simple and so, having this on by default may generate false tunnel matching. </p>
<p> The default is to not turn this feature on. </p>
<pre><code>ARGUS_TUNNEL_DISCOVERY=</code>no</pre>
<h2>Argus_Event_Data</h2>
<p>Argus supports the generation of host originated processes to gather additional data and statistics. These include periodic processes to poll for SNMP data, as an example, or to collect host statistics through reading procfs(). Or single run programs that run at a specified time. </p>
<p> These argus events, are generated from the complete list of ARGUS_EVENT_DATA directives that are specified here. </p>
<pre>The syntax is:
 Syntax is: &quot;method:path|prog:interval[:postproc]&quot;
 Where: method = [ &quot;file&quot; | &quot;prog&quot; ]
 pathname | program = &quot;%s&quot;
 interval = %d[smhd] [ zero means run once ]
 postproc = [ &quot;compress&quot; | &quot;compress2&quot; ]
<code>ARGUS_EVENT_DATA=</code>&quot;file:/proc/vmstat:30s:compress&quot;
<code>ARGUS_EVENT_DATA=</code>&quot;prog:/usr/local/bin/ralsof:30s:compress&quot;</pre>
<h2>Argus_Keystroke</h2>
<p>This version of Argus supports keystroke detection and counting for TCP connections, with specific algorithmic support for SSH connections. </p>
<p> The ARGUS_KEYSTROKE variable turns the feature on. Values for this variable are: </p>
<pre> <code>ARGUS_KEYSTROKE=</code>&quot;yes&quot; - turn on TCP flow tracking
 <code>ARGUS_KEYSTROKE=</code>&quot;tcp&quot; - turn on TCP flow tracking
 <code>ARGUS_KEYSTROKE=</code>&quot;ssh&quot; - turn on SSH specific flow tracking
 <code>ARGUS_KEYSTROKE=</code>&quot;no&quot; [default]</pre>
<p>The algorithm uses a number of variables, all of which can be modifed using the ARGUS_KEYSTROKE_CONF descriptor, which is a semicolon (&#8216;;&#8217;) separated set of variable assignments. Here is the list of supported variables: </p>
<pre> <code>DC_MIN</code> - (int) Minimum client datagram payload size in bytes
 <code>DC_MAX</code> - (int) Maximum client datagram payload size in bytes
 <code>GS_MAX</code> - (int) Maximum server packet gap
 <code>DS_MIN</code> - (int) Minimum server datagram payload size in bytes
 <code>DS_MAX</code> - (int) Maximum server datagram payload size in bytes
 <code>IC_MIN</code> - (int) Minimum client interpacket arrival time (microseconds)
 <code>LCS_MAX</code> - (int) Maximum something - Not sure what this is
 <code>GPC_MAX</code> - (int) Maximum client packet gap
 <code>ICR_MIN</code> - (float) Minimum client/server interpacket arrival ratio
 <code>ICR_MAX</code> - (float) Maximum client/server interpacket arrival ratio</pre>
<p>All variables have default values, this variable is used to override those values. The syntax for the variable is: </p>
<pre> ARGUS_KEYSTROKE_CONF=&quot;DC_MIN=20;DS_MIN=20&quot;
<code>ARGUS_KEYSTROKE</code>=&quot;no&quot;
<code>ARGUS_KEYSTROKE_CONF</code>=&quot;&quot;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
