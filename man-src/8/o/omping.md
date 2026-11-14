---
title: "omping(8)"
name: "omping"
section: "8"
letter: "o"
url: "/docs/linux/man/8-omping/"
description: "omping – test IP multicast"
---

<p><code>omping</code> &#8211; test IP multicast</p>
<h2>Synopsis</h2>
<p>[-<code>46CDEFqVv </code>[-<code>c </code><i>count</i> ] ] [-<code>i </code><i>interval</i> ] [-<code>M </code><i>transport_method</i> ] [-<code>m </code><i>mcast_addr</i> ] [-<code>O </code><i>op_mode</i> ] [-<code>p </code><i>port</i> ] [-<code>R </code><i>rcvbuf</i> ] [-<code>r </code><i>rate_limit</i> ] [-<code>S </code><i>sndbuf</i> ] [-<code>T </code><i>timeout</i> ] [-<code>t </code><i>ttl</i> ] [-<code>w </code><i>wait_time</i> ] <i>remote_addr&#8230;</i></p>
<h2>Description</h2>
<p>The is program which uses User Datagram Protocol to determine if computer is able to send and/or receive IP unicast and multicast or Broadcast packets from the network. It&#8217;s designed to be used in very similar way as <a href="/docs/linux/man/8-ping/">ping</a>(8) and also has some features of the <a href="/docs/linux/man/8-fping/">fping</a>(8) command. Where <a href="/docs/linux/man/8-ping/">ping</a>(8) and differ is in who replies. In <a href="/docs/linux/man/8-ping/">ping</a>(8) replies are sent by the operating system and with another instance of sends the reply. This mean that must be running on all computers to test sending/receiving IP multicast/broadcast. Its arguments are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd>Force usage of IPv4.</p>
<dt><code>-6</code></p>
<dd>Force usage of IPv6.</p>
<dt><code>-C</code></p>
<dd>Display continuous statistics for every reply message.</p>
<dt><code>-D</code></p>
<dd>Disable packet duplicate detection. Option is default for interval 0.</p>
<dt><code>-E</code></p>
<dd>Default behaviour when every client is in stop state is to exit. This may happen if all server sends stop message or if <i>count</i> query messages was sent. This option changes default behaviour and doesn&#8217;t quit automatically.</p>
<dt><code>-F</code></p>
<dd>Allow entering of arguments which are not allowed or not recommended by the specification. This is typically the interval parameter. This option may be used multiple times.</p>
<dt><code>-q</code></p>
<dd>Quiet output. Nothing is displayed except state changes and summary. Option can be used twice and then only summary is displayed.</p>
<dt><code>-V</code></p>
<dd>Display version and quit. Option can be used twice and then remote version is displayed.</p>
<dt><code>-v</code></p>
<dd>Set level of verbosity. Parameter can be used multiple times to achieve higher verbosity.</p>
<dt><code>-c </code><i>count</i></p>
<dd>Number of request packets to send to each target. After sending <i>count</i> query messages, given client is put to stop state and it is no longer sending query messages.</p>
<dt><code>-i </code><i>interval</i></p>
<dd>Wait <i>interval</i> seconds between sending each request packet. Float values are supported in millisecond precision. It&#8217;s possible to set there 0 with meaning that packets are sent ether after previous unicast reply is received or after 1 millisecond, depending on which of these intervals is smaller. The default is to wait for one second between each packet.</p>
<dt><code>-M </code><i>transport_method</i></p>
<dd>Set transport method to use. This can be <code>asm</code> for Any-source Multicast, <code>ssm</code> for Source-specific Multicast and <code>ipbc</code> for IP Broadcast.</p>
<dt><code>-m </code><i>mcast_addr</i></p>
<dd>Multicast or broadcast address to listen on for multicast/broadcast answer messages. Default is 232.43.211.234 for IPv4 and ff3e::4321:1234 for IPv6 multicast, or broadcast address of local interface for Broadcast.</p>
<dt><code>-O </code><i>op_mode</i></p>
<dd>can be running in three different modes. Default and recommended mode for quick testing is <code>normal</code> mode, when behaves like client and server together. It sends queries and is able to respond them. Finally the <code>client</code> mode sends queries, but never respond to other nodes.</p>
<dt><code>-p </code><i>port</i></p>
<dd>Port to bind and listen on for both unicast and multicast/broadcast messages. Default is 4321.</p>
<dt><code>-R </code><i>rcvbuf</i></p>
<dd>Set socket rcvbuf. Minimum value for this option is 2048. If not specified, rcvbuf is not changed and default OS provided value is used.</p>
<dt><code>-r </code><i>rate_limit</i></p>
<dd>Rate limit interval between two query messages to <i>rate_limit</i> seconds. Default value is same as <i>interval</i> given by &#8211;<code>i</code> option. Rate limiting can be disabled by specifying 0 as value. Rate limiting is by default disabled for &#8211;<code>i</code> with 0 seconds.</p>
<dt><code>-S </code><i>sndbuf</i></p>
<dd>Set socket sndbuf. Minimum value for this option is 2048. If not specified, sndbuf is not changed and default OS provided value is used.</p>
<dt><code>-T </code><i>timeout</i></p>
<dd>Specify a timeout, in seconds, before exits regardless of how many packets have been received.</p>
<dt><code>-t </code><i>ttl</i></p>
<dd>Time-To-Live of sent packets.</p>
<dt><code>-w </code><i>wait_time</i></p>
<dd>after is stopped (by sending SIGINT or timeout expire) it is moved to special state when no queries are made and server answer all queries by server response (stop message). This makes possible to give correct (unbiased) result of lost packets on other nodes. Default is 3 times interval or 1 second, depending which one is larger. Also special value 0 can be used to not wait at all or -1 which means wait forever (this can be still terminated by sending SIGINT).</p>
<dt><i>remote_addr</i></p>
<dd>List of addresses to test. One of them must be address of local internet interface. This local address is used for bind and listening on for unicast packets. It&#8217;s also used to determine which interface should be used for sending multicast/broadcast replies.</dl>
<p> Program is normally terminated by SIGINT. After signal receive summary is displayed. You can also display summary during running by sending SIGINFO or SIGUSR1 signal. </p>
<p> When using for fault isolation, it should first be run against local internet interface only, to verify that the local network interface is up and running, and firewall is correctly configured. This mode is available by entering only local IP address.</p>
<h2>Exit Status</h2>
<p>Ex -std</p>
<h2>Examples</h2>
<p>The following commands and output is a typical way how to find-out and solve network problems using omping. In this situation, we have 3 computers named node-01, node-02 and node-03 with IP addresses 192.168.1.101 &#8211; 192.168.1.103. Let&#8217;s run the following command on all of them. </p>
<blockquote><p><tt>$ omping node-01 node-02 node-03</tt></p></blockquote>
<p> on all of nodes we should be able to seen similar output </p>
<blockquote><p><tt>node-01 : waiting for response msg</tt></p></blockquote>
<blockquote><p><tt>node-03 : waiting for response msg</tt></p></blockquote>
<blockquote><p><tt>node-01 : joined (S,G) = (*, 232.43.211.234), pinging</tt></p></blockquote>
<blockquote><p><tt>node-03 : joined (S,G) = (*, 232.43.211.234), pinging</tt></p></blockquote>
<blockquote><p><tt>node-01 : unicast, seq=1, size=69 bytes, dist=0, time=0.192ms</tt></p></blockquote>
<blockquote><p><tt>node-01 : multicast, seq=1, size=69 bytes, dist=0, time=0.284ms</tt></p></blockquote>
<blockquote><p><tt>node-03 : unicast, seq=1, size=69 bytes, dist=0, time=0.279ms</tt></p></blockquote>
<blockquote><p><tt>node-03 : multicast, seq=1, size=69 bytes, dist=0, time=0.360ms</tt></p></blockquote>
<p> The first two lines tell us, that node-02 (actual node) is waiting for a response message from node-01 and node-03. The second two lines contain information, that we were successfully able to send an init message and also received a response message from remote nodes. Both of these messages are unicast, so we are able to send and receive unicast messages on a given port. If all of nodes are up and is running on all of them, but we are not able to receive a response message, it&#8217;s time to check connectivity between nodes. First make sure that you are able to <a href="/docs/linux/man/8-ping/">ping</a>(8) them. If so, make sure that your firewall allows port 4321 to receive udp packets. </p>
<p> The next line tells us that we were able to receive a 69 byte unicast response message from node-01, with a sequence number of 1. The distance between the computers is 0 so they are on the same link net. Time between send and receive packet was 0.192 ms, that is also the current average time and lastly there were no lost packets. </p>
<p> The 6th line tells us the same information as the previous one, but the received message is a multicast message. It means, that multicast is probably well configured. </p>
<p> The 7th and 8th lines are same as previous two one but for node-03. </p>
<p> If the node is able to receive unicast packets, but never multicast, it means that multicast configuration is incorrect. It&#8217;s recommended to turn off your firewall. If multicast packets start to arrive, great. If not, the problem is hidden in the switches/routers between the nodes. Contact your system administrator to allow multicast traffic on the switch or router. </p>
<p> is terminated by SIGINT signal (CTRL-c). Summary statistics are shown </p>
<blockquote><p><tt>node-01 : unicast, xmt/rcv/%loss = 18/18/0%, min/avg/max/std-dev = 0.177/0.301/0.463/0.073</tt></p></blockquote>
<blockquote><p><tt>node-01 : multicast, xmt/rcv/%loss = 18/18/0%, min/avg/max/std-dev = 0.193/0.335/0.547/0.090</tt></p></blockquote>
<blockquote><p><tt>node-03 : unicast, xmt/rcv/%loss = 21/21/0%, min/avg/max/std-dev = 0.272/0.299/0.327/0.017</tt></p></blockquote>
<blockquote><p><tt>node-03 : multicast, xmt/rcv/%loss = 21/20/4% (seq&gt;=2 0%), min/avg/max/std-dev = 0.347/0.388/0.575/0.055</tt></p></blockquote>
<p> Last line has additional information (seq&gt;=2 %0) which means, that after receiving first multicast packet with seq number 2, no other multicast packet was lost. Because creating multicast tree is time consuming, it&#8217;s pretty normal to lost first few multicast packets. rcv field can also be formatted like </p>
<blockquote><p><tt>node-01 : unicast, xmt/rcv/%loss = 3/3+1/0%, min/avg/max/std-dev = 0.294/0.299/0.305/0.006</tt></p></blockquote>
<p> This means, that 1 duplicate packet was received. It&#8217;s possible to find out duplicate packet by looking to output and find line which has following format </p>
<blockquote><p><tt>node-01 : unicast, seq=2 (dup), size=69 bytes, dist=0, time=0.469ms</tt></p></blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-fping/">fping</a>(8), <a href="/docs/linux/man/8-ping/">ping</a>(8)</p>
<h2>Standards</h2>
<p>uses Internet-Draft draft-ietf-mboned-ssmping-08 as underlaying protocol and tries to be as compliant as possible.</p>
<h2>Authors</h2>
<p>The utility was written by An Jan Friesse Aq jfriesse [at] redhat.com .</p>
<h2>Bugs</h2>
<dt><code>Some OSes may not have support for receiving TTL from packet.</code></p>
<dd>then cannot provide distance information.</p>
<dt><code>Some OSes may not provide information about packet receive. Less precise actual time is then used.</code></p>
<dd>
<dd>highly depends on precise <a href="/docs/linux/man/2-poll/">poll</a>(2) and <a href="/docs/linux/man/3-gettimeofday/">gettimeofday</a>(3) functions. If OS doesn&#8217;t provide at least milliseconds precision, results may be incorrect.</dl>
