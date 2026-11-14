---
title: "ovs-dpctl(8)"
name: "ovs-dpctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-dpctl/"
description: "ovs-dpctl – administer Open vSwitch datapaths"
---

<p>ovs-dpctl &#8211; administer Open vSwitch datapaths</p>
<h2>Synopsis</h2>
<p><code>ovs-dpctl</code> [<i>options</i>] <i>command </i>[<i>switch</i>] [<i>args</i>&#8230;]</p>
<h2>Description</h2>
<p>The <code>ovs-dpctl</code> program can create, modify, and delete Open vSwitch datapaths. A single machine may host any number of datapaths. </p>
<p> This program works only with datapaths that are implemented outside of <code>ovs-vswitchd</code> itself, such as the Linux and Windows kernel-based datapaths. To manage datapaths that are integrated into <code>ovs-vswitchd</code>, such as the userspace (<code>netdev</code>) datapath, use <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) to invoke the <code>dpctl/*</code> commands, which are documented in <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8). </p>
<p> A newly created datapath is associated with only one network device, a virtual network device sometimes called the datapath&#8217;s &#8220;local port&#8221;. A newly created datapath is not, however, associated with any of the host&#8217;s other network devices. To intercept and process traffic on a given network device, use the <code>add-if</code> command to explicitly add that network device to the datapath. </p>
<p> If <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8) is in use, use <code><a href="/docs/linux/man/8-ovs-vsctl/">ovs-vsctl</a></code>(8) instead of <code>ovs-dpctl</code>. </p>
<p> Most <code>ovs-dpctl</code> commands that work with datapaths take an argument that specifies the name of the datapath. Datapath names take the form [<i>type</i><code>@</code>]<i>name</i>, where <i>name</i> is the network device associated with the datapath&#8217;s local port. If <i>type</i> is given, it specifies the datapath provider of <i>name</i>, otherwise the default provider <code>system</code> is assumed. </p>
<p> The following commands manage datapaths.</p>
<dl>
<dt><code>add-dp </code><i>dp</i> [<i>netdev</i>[<code>,</code><i>option</i>]&#8230;]</p>
<dd>Creates datapath <i>dp</i>, with a local port also named <i>dp</i>. This will fail if a network device <i>dp</i> already exists.</p>
<dd>If <i>netdev</i>s are specified, <code>ovs-dpctl</code> adds them to the new datapath, just as if <code>add-if</code> was specified.</p>
<dt><code>del-dp </code><i>dp</i></p>
<dd>Deletes datapath <i>dp</i>. If <i>dp</i> is associated with any network devices, they are automatically removed.</p>
<dt><code>add-if </code><i>dp netdev</i>[<code>,</code><i>option</i>]&#8230;</p>
<dd>Adds each <i>netdev</i> to the set of network devices datapath <i>dp</i> monitors, where <i>dp</i> is the name of an existing datapath, and <i>netdev</i> is the name of one of the host&#8217;s network devices, e.g. <code>eth0</code>. Once a network device has been added to a datapath, the datapath has complete ownership of the network device&#8217;s traffic and the network device appears silent to the rest of the system.</p>
<dd>A <i>netdev</i> may be followed by a comma-separated list of options. The following options are currently supported:</p>
<dl>
<dd>
<dl>
<dt><code>type=</code><i>type</i></p>
<dd>Specifies the type of port to add. The default type is <code>system</code>.</p>
<dt><code>port_no=</code><i>port</i></p>
<dd>Requests a specific port number within the datapath. If this option is not specified then one will be automatically assigned.</p>
<dt><i>key</i><code>=</code><i>value</i></p>
<dd>Adds an arbitrary key-value option to the port&#8217;s configuration.</dl>
</dl>
<dd><code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5) documents the available port types and options.</p>
<dt><code>set-if </code><i>dp port</i>[<code>,</code><i>option</i>]&#8230;</p>
<dd>Reconfigures each <i>port</i> in <i>dp</i> as specified. An <i>option</i> of the form <i>key</i><code>=</code><i>value</i> adds the specified key-value option to the port or overrides an existing key&#8217;s value. An <i>option</i> of the form <i>key</i><code>=</code>, that is, without a value, deletes the key-value named <i>key</i>. The type and port number of a port cannot be changed, so <code>type</code> and <code>port_no</code> are only allowed if they match the existing configuration.</p>
<dt><code>del-if </code><i>dp netdev</i>&#8230;</p>
<dd>Removes each <i>netdev</i> from the list of network devices datapath <i>dp</i> monitors.</p>
<dt><code>dump-dps</code></p>
<dd>Prints the name of each configured datapath on a separate line.</p>
<dt> [<code>-s</code> | <code>&#8211;statistics</code>] <code>show </code>[<i>dp</i>&#8230;]</p>
<dd>Prints a summary of configured datapaths, including their datapath numbers and a list of ports connected to each datapath. (The local port is identified as port 0.) If <code>-s</code> or <code>&#8211;statistics</code> is specified, then packet and byte counters are also printed for each port.</p>
<dd>The datapath numbers consists of flow stats and mega flow mask stats.</p>
<dd>The &quot;lookups&quot; row displays three stats related to flow lookup triggered by processing incoming packets in the datapath. &quot;hit&quot; displays number of packets matches existing flows. &quot;missed&quot; displays the number of packets not matching any existing flow and require user space processing. &quot;lost&quot; displays number of packets destined for user space process but subsequently dropped before reaching userspace. The sum of &quot;hit&quot; and &quot;miss&quot; equals to the total number of packets datapath processed.</p>
<dd>The &quot;flows&quot; row displays the number of flows in datapath.</p>
<dd>The &quot;masks&quot; row displays the mega flow mask stats. This row is omitted for datapath not implementing mega flow. &quot;hit&quot; displays the total number of masks visited for matching incoming packets. &quot;total&quot; displays number of masks in the datapath. &quot;hit/pkt&quot; displays the average number of masks visited per packet; the ratio between &quot;hit&quot; and total number of packets processed by the datapath&quot;.</p>
<dd>If one or more datapaths are specified, information on only those datapaths are displayed. Otherwise, <code>ovs-dpctl</code> displays information about all configured datapaths.</dl>
<h3>Datapath Flow Table Debugging Commands</h3>
<p>The following commands are primarily useful for debugging Open vSwitch. The flow table entries (both matches and actions) that they work with are not OpenFlow flow entries. Instead, they are different and considerably simpler flows maintained by the Open vSwitch kernel module. Use <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8), instead, to work with OpenFlow flow entries. </p>
<p> The <i>dp</i> argument to each of these commands is optional when exactly one datapath exists, in which case that datapath is the default. When multiple datapaths exist, then a datapath name is required.</p>
<dl>
<dt> [<code>-m </code>| <code>&#8211;more</code>] <code>dump-flows</code> [<i>dp</i>] [<code>filter=</code><i>filter</i>]</p>
<dd>Prints to the console all flow entries in datapath <i>dp</i>&#8216;s flow table. Without <code>-m</code> or <code>&#8211;more</code>, output omits match fields that a flow wildcards entirely; with <code>-m</code> or <code>&#8211;more</code>, output includes all wildcarded fields.</p>
<dd>If <code>filter=</code><i>filter</i> is specified, only displays the flows that match the <i>filter</i>. <i>filter</i> is a flow in the form similiar to that accepted by <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8)&#8217;s <code>add-flow</code> command. (This is not an OpenFlow flow: besides other differences, it never contains wildcards.) The <i>filter</i> is also useful to match wildcarded fields in the datapath flow. As an example, <code>filter=&#8217;tcp,tp_src=100&#8242;</code> will match the datapath flow containing &#8216;<code>tcp(src=80/0xff00,dst=8080/0xff)</code>&#8216;.</p>
<dt><code>add-flow</code> [<i>dp</i>] <i>flow actions</i></p>
<dd>
<dt> [<code>&#8211;clear</code>] [<code>&#8211;may-create</code>] [<code>-s</code> | <code>&#8211;statistics</code>] <code>mod-flow</code> [<i>dp</i>] <i>flow actions</i></p>
<dd>Adds or modifies a flow in <i>dp</i>&#8216;s flow table that, when a packet matching <i>flow</i> arrives, causes <i>actions</i> to be executed.</p>
<dd>The <code>add-flow</code> command succeeds only if <i>flow</i> does not already exist in <i>dp</i>. Contrariwise, <code>mod-flow</code> without <code>&#8211;may-create</code> only modifies the actions for an existing flow. With <code>&#8211;may-create</code>, <code>mod-flow</code> will add a new flow or modify an existing one.</p>
<dd>If <code>-s</code> or <code>&#8211;statistics</code> is specified, then <code>mod-flow</code> prints the modified flow&#8217;s statistics. A flow&#8217;s statistics are the number of packets and bytes that have passed through the flow, the elapsed time since the flow last processed a packet (if ever), and (for TCP flows) the union of the TCP flags processed through the flow.</p>
<dd>With <code>&#8211;clear</code>, <code>mod-flow</code> zeros out the flow&#8217;s statistics. The statistics printed if <code>-s</code> or <code>&#8211;statistics</code> is also specified are those from just before clearing the statistics.</p>
<dt> [<code>-s</code> | <code>&#8211;statistics</code>] <code>del-flow</code> [<i>dp</i>] <i>flow</i></p>
<dd>Deletes the flow from <i>dp</i>&#8216;s flow table that matches <i>flow</i>. If <code>-s</code> or <code>&#8211;statistics</code> is specified, then <code>del-flow</code> prints the deleted flow&#8217;s statistics.</p>
<dt><code>get-flow</code> [<i>dp</i>] ufid:<i>ufid</i></p>
<dd>Fetches the flow from <i>dp</i>&#8216;s flow table with unique identifier <i>ufid</i>. <i>ufid</i> must be specified as a string of 32 hexadecimal characters.</p>
<dt><code>del-flows</code> [<i>dp</i>]</p>
<dd>Deletes all flow entries from datapath <i>dp</i>&#8216;s flow table.</dl>
<h3>Connection Tracking Table Debugging Commands</h3>
<p>The following commands are primarily useful for debugging the connection tracking entries in the datapath. </p>
<p> The <i>dp</i> argument to each of these commands is optional when exactly one datapath exists, in which case that datapath is the default. When multiple datapaths exist, then a datapath name is required. </p>
<p> <code>N.B.</code>(Linux specific): the <i>system</i> datapaths (i.e. the Linux kernel module Open vSwitch datapaths) share a single connection tracking table (which is also used by other kernel subsystems, such as iptables, nftables and the regular host stack). Therefore, the following commands do not apply specifically to one datapath.</p>
<dl>
<dt> [<code>-m</code> | <code>&#8211;more</code>] [<code>-s</code> | <code>&#8211;statistics</code>] <code>dump-conntrack</code> [<i>dp</i>] [<code>zone=</code><i>zone</i>]</p>
<dd>Prints to the console all the connection entries in the tracker used by <i>dp</i>. If <code>zone=</code><i>zone</i> is specified, only shows the connections in <code>zone</code>. With <code>&#8211;more</code>, some implementation specific details are included. With <code>&#8211;statistics</code> timeouts and timestamps are added to the output.</p>
<dt><code>flush-conntrack [</code><i>dp</i>] [<code>zone=</code><i>zone</i>]</p>
<dd>Flushes all the connection entries in the tracker used by <i>dp</i>. If <code>zone=</code><i>zone</i> is specified, only flushes the connections in <code>zone</code>.</dl>
<h2>Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;statistics</code></p>
<dd>Causes the <code>show</code> command to print packet and byte counters for each port within the datapaths that it shows.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;more</code></p>
<dd>Increases the verbosity of <code>dump-flows</code> output.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;timeout=</code><i>secs</i></p>
<dd>Limits <code>ovs-dpctl</code> runtime to approximately <i>secs</i> seconds. If the timeout expires, <code>ovs-dpctl</code> will exit with a <code>SIGALRM</code> signal.</p>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovs-dpctl</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd>Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovs-dpctl.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd>Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd>Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd><code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd><code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8) </p>
