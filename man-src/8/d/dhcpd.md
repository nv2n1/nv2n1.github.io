---
title: "dhcpd(8)"
name: "dhcpd"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcpd/"
description: "dhcpd – Dynamic Host Configuration Protocol Server"
---

<p>dhcpd &#8211; Dynamic Host Configuration Protocol Server</p>
<h2>Synopsis</h2>
<p><code>dhcpd</code> [ <code>-p</code> <i>port</i> ] [ <code>-f</code> ] [ <code>-d</code> ] [ <code>-q</code> ] [ <code>-t</code> | <code>-T</code> ] [ <code>-4</code> | <code>-6</code> ] [ <code>-s</code> <i>server</i> ] [ <code>-cf</code> <i>config-file</i> ] [ <code>-lf</code> <i>lease-file</i> ] [ <code>-pf</code> <i>pid-file</i> ] [ <code>&#8211;no-pid</code> ] [ <code>-tf</code> <i>trace-output-file</i> ] [ <code>-user</code> <i>user</i> ] [ <code>-group</code> <i>group</i> ] [ <code>-chroot</code> <i>dir</i> ] [ <code>-play</code> <i>trace-playback-file</i> ] [ <i>if0</i> [ <i>&#8230;ifN</i> ] ] </p>
<p> <code>dhcpd</code> &#8211;version</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP Server, dhcpd, implements the Dynamic Host Configuration Protocol (DHCP) and the Internet Bootstrap Protocol (BOOTP). DHCP allows hosts on a TCP/IP network to request and be assigned IP addresses, and also to discover information about the network to which they are attached. BOOTP provides similar functionality, with certain restrictions.</p>
<h2>Operation</h2>
<p>The DHCP protocol allows a host which is unknown to the network administrator to be automatically assigned a new IP address out of a pool of IP addresses for its network. In order for this to work, the network administrator allocates address pools in each subnet and enters them into the <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5) file. </p>
<p> There are two versions of the DHCP protocol DHCPv4 and DHCPv6. At startup the server may be started for one or the other via the <code>-4</code> or <code>-6</code> arguments. </p>
<p> On startup, dhcpd reads the <i>dhcpd.conf</i> file and stores a list of available addresses on each subnet in memory. When a client requests an address using the DHCP protocol, dhcpd allocates an address for it. Each client is assigned a lease, which expires after an amount of time chosen by the administrator (by default, one day). Before leases expire, the clients to which leases are assigned are expected to renew them in order to continue to use the addresses. Once a lease has expired, the client to which that lease was assigned is no longer permitted to use the leased IP address. </p>
<p> In order to keep track of leases across system reboots and server restarts, dhcpd keeps a list of leases it has assigned in the <a href="/docs/linux/man/5-dhcpd-leases/">dhcpd.leases</a>(5) file. Before dhcpd grants a lease to a host, it records the lease in this file and makes sure that the contents of the file are flushed to disk. This ensures that even in the event of a system crash, dhcpd will not forget about a lease that it has assigned. On startup, after reading the dhcpd.conf file, dhcpd reads the dhcpd.leases file to refresh its memory about what leases have been assigned. </p>
<p> New leases are appended to the end of the dhcpd.leases file. In order to prevent the file from becoming arbitrarily large, from time to time dhcpd creates a new dhcpd.leases file from its in-core lease database. Once this file has been written to disk, the old file is renamed <i>dhcpd.leases~</i>, and the new file is renamed dhcpd.leases. If the system crashes in the middle of this process, whichever dhcpd.leases file remains will contain all the lease information, so there is no need for a special crash recovery process. </p>
<p> BOOTP support is also provided by this server. Unlike DHCP, the BOOTP protocol does not provide a protocol for recovering dynamically-assigned addresses once they are no longer needed. It is still possible to dynamically assign addresses to BOOTP clients, but some administrative process for reclaiming addresses is required. By default, leases are granted to BOOTP clients in perpetuity, although the network administrator may set an earlier cutoff date or a shorter lease length for BOOTP leases if that makes sense. </p>
<p> BOOTP clients may also be served in the old standard way, which is to simply provide a declaration in the dhcpd.conf file for each BOOTP client, permanently assigning an address to each client. </p>
<p> Whenever changes are made to the dhcpd.conf file, dhcpd must be restarted. To restart dhcpd, send a SIGTERM (signal 15) to the process ID contained in <i>/var/run/dhcpd.pid</i>, and then re-invoke dhcpd. Because the DHCP server database is not as lightweight as a BOOTP database, dhcpd does not automatically restart itself when it sees a change to the dhcpd.conf file. </p>
<p> Note: We get a lot of complaints about this. We realize that it would be nice if one could send a SIGHUP to the server and have it reload the database. This is not technically impossible, but it would require a great deal of work, our resources are extremely limited, and they can be better spent elsewhere. So please don&#8217;t complain about this on the mailing list unless you&#8217;re prepared to fund a project to implement this feature, or prepared to do it yourself.</p>
<h2>Command Line</h2>
<p>The names of the network interfaces on which dhcpd should listen for broadcasts may be specified on the command line. This should be done on systems where dhcpd is unable to identify non-broadcast interfaces, but should not be required on other systems. If no interface names are specified on the command line dhcpd will identify all network interfaces which are up, eliminating non-broadcast interfaces if possible, and listen for DHCP broadcasts on each interface.</p>
<h2>Command Line Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Run as a DHCP server. This is the default and cannot be combined with <code>-6</code>.</p>
<dt><code>-6</code></p>
<dd>Run as a DHCPv6 server. This cannot be combined with <code>-4</code>.</p>
<dt><code>-p</code><i>&nbsp;<wbr>port</i></p>
<dd>The udp port number on which <code>dhcpd</code> should listen. If unspecified <code>dhcpd</code> uses the default port of 67. This is mostly useful for debugging purposes.</p>
<dt><code>-s</code><i>&nbsp;<wbr>address</i></p>
<dd>Specify an address or host name to which <code>dhcpd</code> should send replies rather than the broadcast address (255.255.255.255). This option is only supported in IPv4.</p>
<dt><code>-f</code></p>
<dd>Force <code>dhcpd</code> to run as a foreground process instead of as a daemon in the background. This is useful when running <code>dhcpd </code> under a debugger, or when running it out of inittab on System V systems.</p>
<dt><code>-d</code></p>
<dd>Send log messages to the standard error descriptor. This can be useful for debugging, and also at sites where a complete log of all dhcp activity must be kept but syslogd is not reliable or otherwise cannot be used. Normally, <code>dhcpd</code> will log all output using the <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> function with the log facility set to LOG_DAEMON. Note that <code>-d</code> implies <code>-f</code> (the daemon will not fork itself into the background).</p>
<dt><code>-q</code></p>
<dd>Be quiet at startup. This suppresses the printing of the entire copyright message during startup. This might be desirable when starting <code>dhcpd</code> from a system startup script (e.g., /etc/rc).</p>
<dt><code>-t</code></p>
<dd>Test the configuration file. The server tests the configuration file for correct syntax, but will not attempt to perform any network operations. This can be used to test a new configuration file automatically before installing it.</p>
<dt><code>-T</code></p>
<dd>Test the lease file. The server tests the lease file for correct syntax, but will not attempt to perform any network operations. This can be used to test a new leaes file automatically before installing it.</p>
<dt><code>-tf</code><i>&nbsp;<wbr>tracefile</i></p>
<dd>Specify a file into which the entire startup state of the server and all the transactions it processes are logged. This can be useful in submitting bug reports &#8211; if you are getting a core dump every so often, you can start the server with the <code>-tf</code> option and then, when the server dumps core, the trace file will contain all the transactions that led up to it dumping core, so that the problem can be easily debugged with <code>-play</code>.</p>
<dt><code>-play</code><i>&nbsp;<wbr>playfile</i></p>
<dd>Specify a file from which the entire startup state of the server and all the transactions it processed are read. The <code>-play</code> option must be specified with an alternate lease file, using the <code>-lf</code> switch, so that the DHCP server doesn&#8217;t wipe out your existing lease file with its test data. The DHCP server will refuse to operate in playback mode unless you specify an alternate lease file.</p>
<dt><code>&#8211;version</code></p>
<dd>Print version number and exit.</p>
<dt><code>-user</code><i>&nbsp;<wbr>user</i></p>
<dd>Setuid to user after completing privileged operations, such as creating sockets that listen on privileged ports.</p>
<dt><code>-group</code><i>&nbsp;<wbr>group</i></p>
<dd>Setgid to group after completing privileged operations, such as creating sockets that listen on privileged ports.</p>
<dt><code>-chroot</code><i>&nbsp;<wbr>dir</i></p>
<dd>Chroot to directory after processing the command line arguments, but before reading the configuration file.</dl>
<p> <i>Modifying default file locations:</i> The following options can be used to modify the locations <code>dhcpd</code> uses for it&#8217;s files. Because of the importance of using the same lease database at all times when running dhcpd in production, these options should be used <code>only</code> for testing lease files or database files in a non-production environment.</p>
<dl>
<dt><code>-cf</code><i>&nbsp;<wbr>config-file</i></p>
<dd>Path to alternate configuration file.</p>
<dt><code>-lf</code><i>&nbsp;<wbr>lease-file</i></p>
<dd>Path to alternate lease file.</p>
<dt><code>-pf</code><i>&nbsp;<wbr>pid-file</i></p>
<dd>Path to alternate pid file.</p>
<dt><code>&#8211;no-pid</code></p>
<dd>Option to disable writing pid files. By default the program will write a pid file. If the program is invoked with this option it will not check for an existing server process.</dl>
<h2>Configuration</h2>
<p>The syntax of the <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5) file is discussed separately. This section should be used as an overview of the configuration process, and the <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5) documentation should be consulted for detailed reference information.</p>
<h2>Subnets</h2>
<p>dhcpd needs to know the subnet numbers and netmasks of all subnets for which it will be providing service. In addition, in order to dynamically allocate addresses, it must be assigned one or more ranges of addresses on each subnet which it can in turn assign to client hosts as they boot. Thus, a very simple configuration providing DHCP support might look like this: </p>
<pre> subnet 239.252.197.0 netmask 255.255.255.0 {
 range 239.252.197.10 239.252.197.250;
 }</pre>
<p>Multiple address ranges may be specified like this: </p>
<pre> subnet 239.252.197.0 netmask 255.255.255.0 {
 range 239.252.197.10 239.252.197.107;
 range 239.252.197.113 239.252.197.250;
 }</pre>
<p>If a subnet will only be provided with BOOTP service and no dynamic address assignment, the range clause can be left out entirely, but the subnet statement must appear.</p>
<h2>Lease Lengths</h2>
<p>DHCP leases can be assigned almost any length from zero seconds to infinity. What lease length makes sense for any given subnet, or for any given installation, will vary depending on the kinds of hosts being served. </p>
<p> For example, in an office environment where systems are added from time to time and removed from time to time, but move relatively infrequently, it might make sense to allow lease times of a month or more. In a final test environment on a manufacturing floor, it may make more sense to assign a maximum lease length of 30 minutes &#8211; enough time to go through a simple test procedure on a network appliance before packaging it up for delivery. </p>
<p> It is possible to specify two lease lengths: the default length that will be assigned if a client doesn&#8217;t ask for any particular lease length, and a maximum lease length. These are specified as clauses to the subnet command: </p>
<pre> subnet 239.252.197.0 netmask 255.255.255.0 {
 range 239.252.197.10 239.252.197.107;
 default-lease-time 600;
 max-lease-time 7200;
 }</pre>
<p>This particular subnet declaration specifies a default lease time of 600 seconds (ten minutes), and a maximum lease time of 7200 seconds (two hours). Other common values would be 86400 (one day), 604800 (one week) and 2592000 (30 days). </p>
<p> Each subnet need not have the same lease&#8212;in the case of an office environment and a manufacturing environment served by the same DHCP server, it might make sense to have widely disparate values for default and maximum lease times on each subnet.</p>
<h2>BOOTP Support</h2>
<p>Each BOOTP client must be explicitly declared in the dhcpd.conf file. A very basic client declaration will specify the client network interface&#8217;s hardware address and the IP address to assign to that client. If the client needs to be able to load a boot file from the server, that file&#8217;s name must be specified. A simple bootp client declaration might look like this: </p>
<pre> host haagen {
 hardware ethernet 08:00:2b:4c:59:23;
 fixed-address 239.252.197.9;
 filename &quot;/tftpboot/haagen.boot&quot;;
 }</pre>
<h2>Options</h2>
<p>DHCP (and also BOOTP with Vendor Extensions) provide a mechanism whereby the server can provide the client with information about how to configure its network interface (e.g., subnet mask), and also how the client can access various network services (e.g., DNS, IP routers, and so on). </p>
<p> These options can be specified on a per-subnet basis, and, for BOOTP clients, also on a per-client basis. In the event that a BOOTP client declaration specifies options that are also specified in its subnet declaration, the options specified in the client declaration take precedence. A reasonably complete DHCP configuration might look something like this: </p>
<pre> subnet 239.252.197.0 netmask 255.255.255.0 {
 range 239.252.197.10 239.252.197.250;
 default-lease-time 600 max-lease-time 7200;
 option subnet-mask 255.255.255.0;
 option broadcast-address 239.252.197.255;
 option routers 239.252.197.1;
 option domain-name-servers 239.252.197.2, 239.252.197.3;
 option domain-name &quot;isc.org&quot;;
 }</pre>
<p>A bootp host on that subnet that needs to be in a different domain and use a different name server might be declared as follows: </p>
<pre> host haagen {
 hardware ethernet 08:00:2b:4c:59:23;
 fixed-address 239.252.197.9;
 filename &quot;/tftpboot/haagen.boot&quot;;
 option domain-name-servers 192.5.5.1;
 option domain-name &quot;vix.com&quot;;
 }</pre>
<p>A more complete description of the dhcpd.conf file syntax is provided in <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5).</p>
<h2>Omapi</h2>
<p>The DHCP server provides the capability to modify some of its configuration while it is running, without stopping it, modifying its database files, and restarting it. This capability is currently provided using OMAPI &#8211; an API for manipulating remote objects. OMAPI clients connect to the server using TCP/IP, authenticate, and can then examine the server&#8217;s current status and make changes to it. </p>
<p> Rather than implementing the underlying OMAPI protocol directly, user programs should use the dhcpctl API or OMAPI itself. Dhcpctl is a wrapper that handles some of the housekeeping chores that OMAPI does not do automatically. Dhcpctl and OMAPI are documented in <code><a href="/docs/linux/man/3-dhcpctl/">dhcpctl</a>(3)</code> and <code><a href="/docs/linux/man/3-omapi/">omapi</a>(3)</code>. </p>
<p> OMAPI exports objects, which can then be examined and modified. The DHCP server exports the following objects: lease, host, failover-state and group. Each object has a number of methods that are provided: lookup, create, and destroy. In addition, it is possible to look at attributes that are stored on objects, and in some cases to modify those attributes.</p>
<h2>The Lease Object</h2>
<p>Leases can&#8217;t currently be created or destroyed, but they can be looked up to examine and modify their state. </p>
<p> Leases have the following attributes: </p>
<p> <code>state </code><i>integer</i> lookup, examine</p>
<dl>
<dd>
<pre>1 = free
2 = active
3 = expired
4 = released
5 = abandoned
6 = reset
7 = backup
8 = reserved
9 = bootp</pre>
</dl>
<p> <code>ip-address </code><i>data</i> lookup, examine</p>
<dl>
<dd>The IP address of the lease.</dl>
<p> <code>dhcp-client-identifier </code><i>data</i> lookup, examine, update</p>
<dl>
<dd>The client identifier that the client used when it acquired the lease. Not all clients send client identifiers, so this may be empty.</dl>
<p> <code>client-hostname </code><i>data</i> examine, update</p>
<dl>
<dd>The value the client sent in the host-name option.</dl>
<p> <code>host </code><i>handle</i> examine</p>
<dl>
<dd>the host declaration associated with this lease, if any.</dl>
<p> <code>subnet </code><i>handle</i> examine</p>
<dl>
<dd>the subnet object associated with this lease (the subnet object is not currently supported).</dl>
<p> <code>pool </code><i>handle</i> examine</p>
<dl>
<dd>the pool object associated with this lease (the pool object is not currently supported).</dl>
<p> <code>billing-class </code><i>handle</i> examine</p>
<dl>
<dd>the handle to the class to which this lease is currently billed, if any (the class object is not currently supported).</dl>
<p> <code>hardware-address </code><i>data</i> examine, update</p>
<dl>
<dd>the hardware address (chaddr) field sent by the client when it acquired its lease.</dl>
<p> <code>hardware-type </code><i>integer</i> examine, update</p>
<dl>
<dd>the type of the network interface that the client reported when it acquired its lease.</dl>
<p> <code>ends </code><i>time</i> examine</p>
<dl>
<dd>the time when the lease&#8217;s current state ends, as understood by the client.</dl>
<p> <code>tstp </code><i>time</i> examine</p>
<dl>
<dd>the time when the lease&#8217;s current state ends, as understood by the server.</dl>
<p> <code>tsfp </code><i>time</i> examine</p>
<dl>
<dd>the adjusted time when the lease&#8217;s current state ends, as understood by the failover peer (if there is no failover peer, this value is undefined). Generally this value is only adjusted for expired, released, or reset leases while the server is operating in partner-down state, and otherwise is simply the value supplied by the peer.</dl>
<p> <code>atsfp </code><i>time</i> examine</p>
<dl>
<dd>the actual tsfp value sent from the peer. This value is forgotten when a lease binding state change is made, to facilitate retransmission logic.</dl>
<p> <code>cltt </code><i>time</i> examine</p>
<dl>
<dd>The time of the last transaction with the client on this lease.</dl>
<h2>The Host Object</h2>
<p>Hosts can be created, destroyed, looked up, examined and modified. If a host declaration is created or deleted using OMAPI, that information will be recorded in the dhcpd.leases file. It is permissible to delete host declarations that are declared in the dhcpd.conf file. </p>
<p> Hosts have the following attributes: </p>
<p> <code>name </code><i>data</i> lookup, examine, modify</p>
<dl>
<dd>the name of the host declaration. This name must be unique among all host declarations.</dl>
<p> <code>group </code><i>handle</i> examine, modify</p>
<dl>
<dd>the named group associated with the host declaration, if there is one.</dl>
<p> <code>hardware-address </code><i>data</i> lookup, examine, modify</p>
<dl>
<dd>the link-layer address that will be used to match the client, if any. Only valid if hardware-type is also present.</dl>
<p> <code>hardware-type </code><i>integer</i> lookup, examine, modify</p>
<dl>
<dd>the type of the network interface that will be used to match the client, if any. Only valid if hardware-address is also present.</dl>
<p> <code>dhcp-client-identifier </code><i>data</i> lookup, examine, modify</p>
<dl>
<dd>the dhcp-client-identifier option that will be used to match the client, if any.</dl>
<p> <code>ip-address </code><i>data</i> examine, modify</p>
<dl>
<dd>a fixed IP address which is reserved for a DHCP client that matches this host declaration. The IP address will only be assigned to the client if it is valid for the network segment to which the client is connected.</dl>
<p> <code>statements </code><i>data</i> modify</p>
<dl>
<dd>a list of statements in the format of the dhcpd.conf file that will be executed whenever a message from the client is being processed.</dl>
<p> <code>known </code><i>integer</i> examine, modify</p>
<dl>
<dd>if nonzero, indicates that a client matching this host declaration will be treated as <i>known</i> in pool permit lists. If zero, the client will not be treated as known.</dl>
<h2>The Group Object</h2>
<p>Named groups can be created, destroyed, looked up, examined and modified. If a group declaration is created or deleted using OMAPI, that information will be recorded in the dhcpd.leases file. It is permissible to delete group declarations that are declared in the dhcpd.conf file. </p>
<p> Named groups currently can only be associated with hosts &#8211; this allows one set of statements to be efficiently attached to more than one host declaration. </p>
<p> Groups have the following attributes: </p>
<p> <code>name </code><i>data</i></p>
<dl>
<dd>the name of the group. All groups that are created using OMAPI must have names, and the names must be unique among all groups.</dl>
<p> <code>statements </code><i>data</i></p>
<dl>
<dd>a list of statements in the format of the dhcpd.conf file that will be executed whenever a message from a client whose host declaration references this group is processed.</dl>
<h2>The Control Object</h2>
<p>The control object allows you to shut the server down. If the server is doing failover with another peer, it will make a clean transition into the shutdown state and notify its peer, so that the peer can go into partner down, and then record the &quot;recover&quot; state in the lease file so that when the server is restarted, it will automatically resynchronize with its peer. </p>
<p> On shutdown the server will also attempt to cleanly shut down all OMAPI connections. If these connections do not go down cleanly after five seconds, they are shut down preemptively. It can take as much as 25 seconds from the beginning of the shutdown process to the time that the server actually exits. </p>
<p> To shut the server down, open its control object and set the state attribute to 2.</p>
<h2>The Failover-State Object</h2>
<p>The failover-state object is the object that tracks the state of the failover protocol as it is being managed for a given failover peer. The failover object has the following attributes (please see <code>dhcpd.conf (5)</code> for explanations about what these attributes mean): </p>
<p> <code>name </code><i>data</i> examine</p>
<dl>
<dd>Indicates the name of the failover peer relationship, as described in the server&#8217;s <code>dhcpd.conf</code> file.</dl>
<p> <code>partner-address </code><i>data</i> examine</p>
<dl>
<dd>Indicates the failover partner&#8217;s IP address.</dl>
<p> <code>local-address </code><i>data</i> examine</p>
<dl>
<dd>Indicates the IP address that is being used by the DHCP server for this failover pair.</dl>
<p> <code>partner-port </code><i>data</i> examine</p>
<dl>
<dd>Indicates the TCP port on which the failover partner is listening for failover protocol connections.</dl>
<p> <code>local-port </code><i>data</i> examine</p>
<dl>
<dd>Indicates the TCP port on which the DHCP server is listening for failover protocol connections for this failover pair.</dl>
<p> <code>max-outstanding-updates </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the number of updates that can be outstanding and unacknowledged at any given time, in this failover relationship.</dl>
<p> <code>mclt </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the maximum client lead time in this failover relationship.</dl>
<p> <code>load-balance-max-secs </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the maximum value for the secs field in a client request before load balancing is bypassed.</dl>
<p> <code>load-balance-hba </code><i>data</i> examine</p>
<dl>
<dd>Indicates the load balancing hash bucket array for this failover relationship.</dl>
<p> <code>local-state </code><i>integer</i> examine, modify</p>
<dl>
<dd>Indicates the present state of the DHCP server in this failover relationship. Possible values for state are:</dl>
<dl>
<dd>
<pre>1 - startup
2 - normal
3 - communications interrupted
4 - partner down
5 - potential conflict
6 - recover
7 - paused
8 - shutdown
9 - recover done
10 - resolution interrupted
11 - conflict done
254 - recover wait</pre>
</dl>
<dl>
<dd>(Note that some of the above values have changed since DHCP 3.0.x.)</dl>
<dl>
<dd>In general it is not a good idea to make changes to this state. However, in the case that the failover partner is known to be down, it can be useful to set the DHCP server&#8217;s failover state to partner down. At this point the DHCP server will take over service of the failover partner&#8217;s leases as soon as possible, and will give out normal leases, not leases that are restricted by MCLT. If you do put the DHCP server into the partner-down when the other DHCP server is not in the partner-down state, but is not reachable, IP address assignment conflicts are possible, even likely. Once a server has been put into partner-down mode, its failover partner must not be brought back online until communication is possible between the two servers.</dl>
<p> <code>partner-state </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the present state of the failover partner.</dl>
<p> <code>local-stos </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the time at which the DHCP server entered its present state in this failover relationship.</dl>
<p> <code>partner-stos </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the time at which the failover partner entered its present state.</dl>
<p> <code>hierarchy </code><i>integer</i> examine</p>
<dl>
<dd>Indicates whether the DHCP server is primary (0) or secondary (1) in this failover relationship.</dl>
<p> <code>last-packet-sent </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the time at which the most recent failover packet was sent by this DHCP server to its failover partner.</dl>
<p> <code>last-timestamp-received </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the timestamp that was on the failover message most recently received from the failover partner.</dl>
<p> <code>skew </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the skew between the failover partner&#8217;s clock and this DHCP server&#8217;s clock</dl>
<p> <code>max-response-delay </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the time in seconds after which, if no message is received from the failover partner, the partner is assumed to be out of communication.</dl>
<p> <code>cur-unacked-updates </code><i>integer</i> examine</p>
<dl>
<dd>Indicates the number of update messages that have been received from the failover partner but not yet processed.</dl>
<h2>Files</h2>
<p><code>/etc/dhcp/dhcpd.conf, /var/lib/dhcpd/dhcpd.leases, /var/run/dhcpd.pid,</code> <code>/var/lib/dhcpd/dhcpd.leases~.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), <a href="/docs/linux/man/8-dhcrelay/">dhcrelay</a>(8), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), <a href="/docs/linux/man/5-dhcpd-leases/">dhcpd.leases</a>(5)</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8)</code> was originally written by Ted Lemon under a contract with Vixie Labs. Funding for this project was provided by Internet Systems Consortium. Version 3 of the DHCP server was funded by Nominum, Inc. Information about Internet Systems Consortium is available at <code><a rel="nofollow" href="https://www.isc.org/">https://www.isc.org/</a></code>.</p>
