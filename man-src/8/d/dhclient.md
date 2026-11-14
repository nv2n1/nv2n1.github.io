---
title: "dhclient(8)"
name: "dhclient"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhclient/"
description: "dhclient – Dynamic Host Configuration Protocol Client"
---

<p>dhclient &#8211; Dynamic Host Configuration Protocol Client</p>
<h2>Synopsis</h2>
<p><code>dhclient</code> [ <code>-4</code> | <code>-6</code> ] [ <code>-S</code> ] [ <code>-N</code> [ <code>-N&#8230;</code> ] ] [ <code>-T</code> [ <code>-T&#8230;</code> ] ] [ <code>-P</code> [ <code>-P&#8230;</code> ] ] <code>-R</code> ] [ <code>-i</code> ] [ <code>-I</code> ] [ <code>-4o6</code> <i>port</i> ] [ <code>-D</code> <i>LL|LLT</i> ] [ <code>-p</code> <i>port-number</i> ] [ <code>-d</code> ] [ <code>-df</code> <i>duid-lease-file</i> ] [ <code>-e</code> <i>VAR=value</i> ] [ <code>-q</code> ] [ <code>-1</code> ] [ <code>-r</code> | <code>-x</code> ] [ <code>-lf</code> <i>lease-file</i> ] [ <code>-pf</code> <i>pid-file</i> ] [ <code>&#8211;no-pid</code> ] [ <code>-cf</code> <i>config-file</i> ] [ <code>-sf</code> <i>script-file</i> ] [ <code>-s</code> <i>server-addr</i> ] [ <code>-g</code> <i>relay</i> ] [ <code>-n</code> ] [ <code>-nw</code> ] [ <code>-w</code> ] [ <code>&#8211;dad-wait-time</code> <i>seconds</i> ] [ <code>&#8211;prefix-len-hint</code> <i>length</i> ] [ <code>&#8211;decline-wait-time</code> <i>seconds</i> ] [ <code>-v</code> ] [ <code>&#8211;version</code> ] [ <i>if0</i> [ <i>&#8230;ifN</i> ] ]</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP Client, <code>dhclient</code>, provides a means for configuring one or more network interfaces using the Dynamic Host Configuration Protocol, BOOTP protocol, or if these protocols fail, by statically assigning an address.</p>
<h2>Operation</h2>
<p>The DHCP protocol allows a host to contact a central server which maintains a list of IP addresses which may be assigned on one or more subnets. A DHCP client may request an address from this pool, and then use it on a temporary basis for communication on network. The DHCP protocol also provides a mechanism whereby a client can learn important details about the network to which it is attached, such as the location of a default router, the location of a name server, and so on. </p>
<p> There are two versions of the DHCP protocol DHCPv4 and DHCPv6. At startup the client may be started for one or the other via the <code>-4</code> or <code>-6</code> options. </p>
<p> On startup, <code>dhclient</code> reads the dhclient.conf for configuration instructions. It then gets a list of all the network interfaces that are configured in the current system. For each interface, it attempts to configure the interface using the DHCP protocol. </p>
<p> In order to keep track of leases across system reboots and server restarts, <code>dhclient</code> keeps a list of leases it has been assigned in the dhclient.leases file. On startup, after reading the dhclient.conf file, <code>dhclient</code> reads the dhclient.leases file to refresh its memory about what leases it has been assigned. </p>
<p> When a new lease is acquired, it is appended to the end of the dhclient.leases file. In order to prevent the file from becoming arbitrarily large, from time to time <code>dhclient</code> creates a new dhclient.leases file from its in-core lease database. The old version of the dhclient.leases file is retained under the name <i>dhclient.leases~</i> until the next time <code>dhclient</code> rewrites the database. </p>
<p> Old leases are kept around in case the DHCP server is unavailable when <code>dhclient</code> is first invoked (generally during the initial system boot process). In that event, old leases from the dhclient.leases file which have not yet expired are tested, and if they are determined to be valid, they are used until either they expire or the DHCP server becomes available. </p>
<p> A mobile host which may sometimes need to access a network on which no DHCP server exists may be preloaded with a lease for a fixed address on that network. When all attempts to contact a DHCP server have failed, <code>dhclient</code> will try to validate the static lease, and if it succeeds, will use that lease until it is restarted. </p>
<p> A mobile host may also travel to some networks on which DHCP is not available but BOOTP is. In that case, it may be advantageous to arrange with the network administrator for an entry on the BOOTP database, so that the host can boot quickly on that network rather than cycling through the list of old leases.</p>
<h2>Command Line</h2>
<p>The names of the network interfaces that <code>dhclient</code> should attempt to configure may be specified on the command line. If no interface names are specified on the command line <code>dhclient</code> will normally identify all network interfaces, eliminating non-broadcast interfaces if possible, and attempt to configure each interface. </p>
<p> It is also possible to specify interfaces by name in the dhclient.conf file. If interfaces are specified in this way, then the client will only configure interfaces that are either specified in the configuration file or on the command line, and will ignore all other interfaces. </p>
<p> The client normally prints no output during its startup sequence. It can be made to emit verbose messages displaying the startup sequence events until it has acquired an address by supplying the <code>-v</code> command line argument. In either case, the client logs messages using the <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> facility.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Use the DHCPv4 protocol to obtain an IPv4 address and configuration parameters. This is the default and cannot be combined with <code>-6</code>.</p>
<dt><code>-6</code></p>
<dd>Use the DHCPv6 protocol to obtain whatever IPv6 addresses are available along with configuration parameters. It cannot be combined with <code>-4</code>. The <code>-S -T -P -N</code> and <code>-D</code> arguments provide more control over aspects of the DHCPv6 processing. Note: it is not recommended to mix queries of different types together or even to share the lease file between them.</p>
<dt><code>-4o6</code><i>&nbsp;port</i></p>
<dd>Participate in the DHCPv4 over DHCPv6 protocol specified by RFC 7341. This associates a DHCPv4 and a DHCPv6 client to allow the v4 client to send v4 requests encapsulated in a v6 packet. Communication between the two clients is done on a pair of UDP sockets bound to ::1 <i>port</i> and <i>port + 1</i>. Both clients must be launched using the same <i>port</i> argument.</p>
<dt><code>-1</code></p>
<dd>Try to get a lease once. On failure exit with code 2. In DHCPv6 this sets the maximum duration of the initial exchange to <i>timeout</i> (from dhclient.conf with a default of sixty seconds).</p>
<dt><code>-d</code></p>
<dd>Force <code>dhclient</code> to run as a foreground process. Normally the DHCP client will run in the foreground until is has configured an interface at which time it will revert to running in the background. This option is useful when running the client under a debugger, or when running it out of inittab on System V systems. This implies <code>-v</code>.</p>
<dt><code>-nw</code></p>
<dd>Become a daemon immediately (nowait) rather than waiting until an IP address has been acquired.</p>
<dt><code>-q</code></p>
<dd>Be quiet at startup, this is the default.</p>
<dt><code>-v</code></p>
<dd>Enable verbose log messages.</p>
<dt><code>-w</code></p>
<dd>Continue running even if no broadcast interfaces were found. Normally DHCP client will exit if it isn&#8217;t able to identify any network interfaces to configure. On laptop computers and other computers with hot-swappable I/O buses, it is possible that a broadcast interface may be added after system startup. This flag can be used to cause the client not to exit when it doesn&#8217;t find any such interfaces. The <code><a href="/docs/linux/man/1-omshell/">omshell</a>(1)</code> program can then be used to notify the client when a network interface has been added or removed, so that the client can attempt to configure an IP address on that interface.</p>
<dt><code>-n</code></p>
<dd>Do not configure any interfaces. This is most likely to be useful in combination with the <code>-w</code> flag.</p>
<dt><code>-e</code><i>&nbsp;VAR=value</i></p>
<dd>Define additional environment variables for the environment where <code>dhclient-script</code> executes. You may specify multiple <code>-e</code> options on the command line.</p>
<dt><code>-r</code></p>
<dd>Release the current lease and stop the running DHCP client as previously recorded in the PID file. When shutdown via this method <code>dhclient-script</code> will be executed with the specific reason for calling the script set. The client normally doesn&#8217;t release the current lease as this is not required by the DHCP protocol but some cable ISPs require their clients to notify the server if they wish to release an assigned IP address.</p>
<dt><code>-x</code></p>
<dd>Stop the running DHCP client without releasing the current lease. Kills existing <code>dhclient</code> process as previously recorded in the PID file. When shutdown via this method <code>dhclient-script</code> will be executed with the specific reason for calling the script set.</p>
<dt><code>-p</code><i>&nbsp;port-number</i></p>
<dd>The UDP port number on which the DHCP client should listen and transmit. If unspecified, <code>dhclient</code> uses the default port of 68. This is mostly useful for debugging purposes. If a different port is specified on which the client should listen and transmit, the client will also use a different destination port &#8211; one less than the specified port.</p>
<dt><code>-s</code><i>&nbsp;server-addr</i></p>
<dd>Specify the server IP address or fully qualified domain name to use as a destination for DHCP protocol messages before <code>dhclient</code> has acquired an IP address. Normally, <code>dhclient</code> transmits these messages to 255.255.255.255 (the IP limited broadcast address). Overriding this is mostly useful for debugging purposes. This feature is not supported in DHCPv6 (<code>-6</code>) mode.</p>
<dt><code>-g</code><i>&nbsp;relay</i></p>
<dd>Set the giaddr field of all packets to the <i>relay</i> IP address simulating a relay agent. This is for testing purposes only and should not be expected to work in any consistent or useful way.</p>
<dt><code>-i</code></p>
<dd>Use a DUID with DHCPv4 clients. If no DUID is available in the lease file one will be constructed and saved. The DUID will be used to construct a RFC4361 style client id that will be included in the client&#8217;s messages. This client id can be overridden by setting a client id in the configuration file. Overriding the client id in this fashion is discouraged.</p>
<dt><code>-I</code></p>
<dd>Use the standard DDNS scheme from RFCs 4701 &amp; 4702.</p>
<dt>
<dt><code>&#8211;decline-wait-time</code><i>&nbsp;seconds</i></p>
<dd>
<dd>Specify the time (in seconds) that an IPv4 client should wait after declining an address before issuing a discover. The default is 10 seconds as recommended by RFC 2131, Section 3.1.5. A value of zero equates to no wait at all.</dl>
<p> <code>&#8211;version</code> Print version number and exit. </p>
<p> <i>Options available for DHCPv6 mode:</i></p>
<dl>
<dt><code>-S</code></p>
<dd>Use Information-request to get only stateless configuration parameters (i.e., without address). This implies <code>-6</code>. It also doesn&#8217;t rewrite the lease database.</p>
<dt><code>-T</code></p>
<dd>Ask for IPv6 temporary addresses, one set per <code>-T</code> flag. This implies <code>-6</code> and also disables the normal address query. See <code>-N</code> to restore it.</p>
<dt><code>-P</code></p>
<dd>Enable IPv6 prefix delegation. This implies <code>-6</code> and also disables the normal address query. See <code>-N</code> to restore it. Multiple prefixes can be requested with multiple <code>-P</code> flags. Note only one requested interface is allowed.</p>
<dt><code>-R</code></p>
<dd>Require that responses include all of the items requested by any <code>-N</code>, <code>-T</code>, or <code>-P</code> options. Normally even if the command line includes a number of these the client will be willing to accept the best lease it can even if the lease doesn&#8217;t include all of the requested items. This option causes the client to only accept leases that include all of the requested items. </p>
<p> Note well: enabling this may prevent the client from using any leases it receives if the servers aren&#8217;t configured to supply all of the items.</p>
<dt><code>-D</code><i>&nbsp;LL or LLT</i></p>
<dd>Override the default when selecting the type of DUID to use. By default, DHCPv6 <code>dhclient</code> creates an identifier based on the link-layer address (DUID-LL) if it is running in stateless mode (with <code>-S</code>, not requesting an address), or it creates an identifier based on the link-layer address plus a timestamp (DUID-LLT) if it is running in stateful mode (without <code>-S</code>, requesting an address). When DHCPv4 is configured to use a DUID using <code>-i</code> option the default is to use a DUID-LLT. <code>-D</code> overrides these default, with a value of either <i>LL</i> or <i>LLT</i>.</p>
<dt><code>-N</code></p>
<dd>Restore normal address query for IPv6. This implies <code>-6</code>. It is used to restore normal operation after using <code>-T</code> or <code>-P</code>. Multiple addresses can be requested with multiple <code>-N</code> flags.</p>
<dt><code>&#8211;address-prefix-len</code><i>&nbsp;length</i></p>
<dd>Specify the length of the prefix for IPv6 addresses. This value is passed by dhclient into the client script via the environment variable, ip6_prefixlen, when binding IPv6 addresses. The default value is 128. Alternatively you may change the default at compile time by setting DHCLIENT_DEFAULT_PREFIX_LEN in includes/site.h.</dl>
<dl>
<dt><code>&#8211;dad-wait-time</code><i>&nbsp;seconds</i></p>
<dd>Specify maximum time (in seconds) that the client should wait for the duplicate address detection (DAD) to complete on an interface. This value is propagated to the dhclient script in a dad_wait_time environment variable. If any of the IPv6 addresses on the interface are tentative (DAD is in progress), the script will wait for the specified number of seconds for DAD to complete. If the script ignores this variable the parameter has no effect.</dl>
<dl>
<dt><code>&#8211;prefix-len-hint</code><i>&nbsp;length</i></p>
<dd>When used in conjunction with -P, it directs the client to use the given length to use a prefix hint of, &quot;::/length&quot;, when requesting new prefixes.</dl>
<p> <i>Modifying default file locations:</i> The following options can be used to modify the locations a client uses for its files. They can be particularly useful if, for example, <code>/var/lib/dhcp</code> or <code>/var/run</code> have not been mounted when the DHCP client is started.</p>
<dl>
<dt><code>-cf</code><i>&nbsp;config-file</i></p>
<dd>Path to the client configuration file. If unspecified, the default <code>/etc/dhcp/dhclient.conf</code> is used. See <code><a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5)</code> for a description of this file.</p>
<dt><code>-df</code><i>&nbsp;duid-lease-file</i></p>
<dd>Path to a secondary lease file. If the primary lease file doesn&#8217;t contain a DUID this file will be searched. The DUID read from the secondary will be written to the primary. This option can be used to allow an IPv4 instance of the client to share a DUID with an IPv6 instance. After starting one of the instances the second can be started with this option pointing to the lease file of the first instance. There is no default. If no file is specified no search is made for a DUID should one not be found in the main lease file.</p>
<dt><code>-lf</code><i>&nbsp;lease-file</i></p>
<dd>Path to the lease database file. If unspecified, the default <code>/var/lib/dhcp/dhclient.leases</code> is used. See <code><a href="/docs/linux/man/5-dhclient-leases/">dhclient.leases</a>(5)</code> for a description of this file.</p>
<dt><code>-pf</code><i>&nbsp;pid-file</i></p>
<dd>Path to the process ID file. If unspecified, the default <code>/var/run/dhclient.pid</code> is used.</p>
<dt><code>&#8211;no-pid</code></p>
<dd>Option to disable writing pid files. By default the program will write a pid file. If the program is invoked with this option it will not attempt to kill any existing client processes even if invoked with <code>-r</code> or <code>-x</code>.</p>
<dt><code>-sf</code><i>&nbsp;script-file</i></p>
<dd>Path to the network configuration script invoked by <code>dhclient</code> when it gets a lease. If unspecified, the default <code>/sbin/dhclient-script</code> is used. See <code><a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8)</code> for a description of this file.</dl>
<h2>Ports</h2>
<p>During operations the client may use multiple UDP ports to provide different functions. Which ports are opened depends on both the way you compiled your code and the configuration you supply. The following should provide you an idea of what ports may be in use. </p>
<p> Normally a DHCPv4 client will open a raw UDP socket to receive and send most DHCPv4 packets. It also opens a fallback UDP socket for use in sending unicast packets. Normally these will both use the well known port number for BOOTPC. </p>
<p> For DHCPv6 the client opens a UDP socket on the well known client port and a fallback UDP socket on a random port for use in sending unicast messages. Unlike DHCPv4 the well known socket doesn&#8217;t need to be opened in raw mode. </p>
<p> If you have included an omapi port statement in your configuration file then the client will open a TCP socket on that port to listen for OMPAI connections. When something connects another port will be used for the established connection. </p>
<p> When DDNS is enabled at compile time (see includes/site.h) the client will open both a v4 and a v6 UDP socket on random ports. These ports are not opened unless/until the client first attempts to do an update. If the client is not configured to do updates, the ports will never be opened.</p>
<h2>Configuration</h2>
<p>The syntax of the <code><a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5)</code> file is discussed separately.</p>
<h2>Omapi</h2>
<p>The DHCP client provides some ability to control it while it is running, without stopping it. This capability is provided using OMAPI, an API for manipulating remote objects. OMAPI clients connect to the client using TCP/IP, authenticate, and can then examine the client&#8217;s current status and make changes to it. </p>
<p> Rather than implementing the underlying OMAPI protocol directly, user programs should use the dhcpctl API or OMAPI itself. Dhcpctl is a wrapper that handles some of the housekeeping chores that OMAPI does not do automatically. Dhcpctl and OMAPI are documented in <code><a href="/docs/linux/man/3-dhcpctl/">dhcpctl</a>(3)</code> and <code><a href="/docs/linux/man/3-omapi/">omapi</a>(3)</code>. Most things you&#8217;d want to do with the client can be done directly using the <code><a href="/docs/linux/man/1-omshell/">omshell</a>(1)</code> command, rather than having to write a special program.</p>
<h2>The Control Object</h2>
<p>The control object allows you to shut the client down, releasing all leases that it holds and deleting any DNS records it may have added. It also allows you to pause the client &#8211; this unconfigures any interfaces the client is using. You can then restart it, which causes it to reconfigure those interfaces. You would normally pause the client prior to going into hibernation or sleep on a laptop computer. You would then resume it after the power comes back. This allows PC cards to be shut down while the computer is hibernating or sleeping, and then reinitialized to their previous state once the computer comes out of hibernation or sleep. </p>
<p> The control object has one attribute &#8211; the state attribute. To shut the client down, set its state attribute to 2. It will automatically do a DHCPRELEASE. To pause it, set its state attribute to 3. To resume it, set its state attribute to 4.</p>
<h2>Environment Variables</h2>
<p>The following environment variables may be defined to override the builtin defaults for file locations. Note that use of the related command-line options will ignore the corresponding environment variable settings.</p>
<dl>
<dt><code>PATH_DHCLIENT_CONF</code></p>
<dd>The dhclient.conf configuration file.</p>
<dt><code>PATH_DHCLIENT_DB</code></p>
<dd>The dhclient.leases database.</p>
<dt><code>PATH_DHCLIENT_PID</code></p>
<dd>The dhclient PID file.</p>
<dt><code>PATH_DHCLIENT_SCRIPT</code></p>
<dd>The dhclient-script file.</dl>
<h2>Files</h2>
<p><code>/sbin/dhclient-script,</code> <code>/etc/dhcp/dhclient.conf, /var/lib/dhcp/dhclient.leases, /var/run/dhclient.pid,</code> <code>/var/lib/dhcp/dhclient.leases~.</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/8-dhcrelay/">dhcrelay</a>(8), <a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8), <a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5), <a href="/docs/linux/man/5-dhclient-leases/">dhclient.leases</a>(5), <a href="/docs/linux/man/5-dhcp-eval/">dhcp-eval</a>(5).</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code> To learn more about Internet Systems Consortium, see <code><a rel="nofollow" href="https://www.isc.org">https://www.isc.org</a></code> </p>
<p> This client was substantially modified and enhanced by Elliot Poger for use on Linux while he was working on the MosquitoNet project at Stanford. </p>
<p> The current version owes much to Elliot&#8217;s Linux enhancements, but was substantially reorganized and partially rewritten by Ted Lemon so as to use the same networking framework that the Internet Systems Consortium DHCP server uses. Much system-specific configuration code was moved into a shell script so that as support for more operating systems is added, it will not be necessary to port and maintain system-specific configuration code to these operating systems &#8211; instead, the shell script can invoke the native tools to accomplish the same purpose.</p>
