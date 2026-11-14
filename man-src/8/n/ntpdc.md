---
title: "ntpdc(8)"
name: "ntpdc"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntpdc/"
description: "ntpdc – special NTP query program"
---

<p>ntpdc &#8211; special NTP query program</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntpdc [ -46dilnps ] [ -c </code><i>command</i><code> ] [ </code><i>host</i><code> ] [ &#8230; ]</code> </p>
<h2>Description</h2>
<p><code>ntpdc</code> is used to query the <code>ntpd</code> daemon about its current state and to request changes in that state. The program may be run either in interactive mode or controlled using command line arguments. Extensive state and statistics information is available through the <code>ntpdc</code> interface. In addition, nearly all the configuration options which can be specified at startup using ntpd&#8217;s configuration file may also be specified at run time using <code>ntpdc</code>46 If one or more request options are included on the command line when <code>ntpdc</code> is executed, each of the requests will be sent to the NTP servers running on each of the hosts given as command line arguments, or on localhost by default. If no request options are given, <code>ntpdc</code> will attempt to read commands from the standard input and execute these on the NTP server running on the first host given on the command line, again defaulting to localhost when no other host is specified. <code>ntpdc</code> will prompt for commands if the standard input is a terminal device. <code>ntpdc</code> uses NTP mode 7 packets to communicate with the NTP server, and hence can be used to query any compatible server on the network which permits it. Note that since NTP is a UDP protocol this communication will be somewhat unreliable, especially over large distances in terms of network topology. <code>ntpdc</code> makes no attempt to retransmit requests, and will time requests out if the remote host is not heard from within a suitable timeout time. The operation of <code>ntpdc</code> are specific to the particular implementation of the <code>ntpd</code> daemon and can be expected to work only with this and maybe some previous versions of the daemon. Requests from a remote <code>ntpdc</code> program which affect the state of the local server must be authenticated, which requires both the remote program and local server share a common key and key identifier. Note that in contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. </p>
<h2>Command Line Options</h2>
<p>Specifying a command line option other than <code>-i</code> or <code>-n</code> will cause the specified query (queries) to be sent to the indicated host(s) immediately. Otherwise, <code>ntpdc</code> will attempt to read interactive format commands from the standard input. </p>
<dl>
<dd>
<dl>
<dt><code>-4</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv4 namespace.</p>
<dt><code>-6</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv6 namespace.</p>
<dt><code>-c </code><i>command</i></p>
<dd>The following argument is interpreted as an interactive format command and is added to the list of commands to be executed on the specified host(s). Multiple -c options may be given.</p>
<dt><code>-d</code></p>
<dd>Turn on debugging mode.</p>
<dt><code>-i</code></p>
<dd>Force <code>ntpdc</code> to operate in interactive mode. Prompts will be written to the standard output and commands read from the standard input.</p>
<dt><code>-l</code></p>
<dd>Obtain a list of peers which are known to the server(s). This switch is equivalent to <code>-c listpeers</code>46</p>
<dt><code>-n</code></p>
<dd>Output all host addresses in dotted-quad numeric format rather than converting to the canonical host names.</p>
<dt><code>-p</code></p>
<dd>Print a list of the peers known to the server as well as a summary of their state. This is equivalent to <code>-c peers</code>46</p>
<dt><code>-s</code></p>
<dd>Print a list of the peers known to the server as well as a summary of their state, but in a slightly different format than the -p switch. This is equivalent to <code>-c dmpeers</code>46</dl>
</dl>
<h2>Interactive Commands</h2>
<p>Interactive format commands consist of a keyword followed by zero to four arguments. Only enough characters of the full keyword to uniquely identify the command need be typed. The output of a command is normally sent to the standard output, but optionally the output of individual commands may be sent to a file by appending a <code>&lt;</code>, followed by a file name, to the command line. </p>
<p> A number of interactive format commands are executed entirely within the <code>ntpdc</code> program itself and do not result in NTP mode 7 requests being sent to a server. These are described following. </p>
<dl>
<dd>
<dl>
<dt><code>? [ </code><i>command_keyword</i><code> ]</code></p>
<dd>
<dt><code>help [ </code><i>command_keyword</i><code> ]</code></p>
<dd>A <code>?</code> by itself will print a list of all the command keywords known to this incarnation of <code>ntpq</code>46 A <code>?</code> followed by a command keyword will print function and usage information about the command. This command is probably a better source of information about <code>ntpq</code> than this manual page.</p>
<dt><code>delay </code><i>milliseconds</i></p>
<dd>Specify a time interval to be added to timestamps included in requests which require authentication. This is used to enable (unreliable) server reconfiguration over long delay network paths or between machines whose clocks are unsynchronized. Actually the server does not now require timestamps in authenticated requests, so this command may be obsolete.</p>
<dt><code>host </code><i>hostname</i></p>
<dd>Set the host to which future queries will be sent. Hostname may be either a host name or a numeric address.</p>
<dt><code>hostnames [ yes | no ]</code></p>
<dd>If <code>yes</code> is specified, host names are printed in information displays. If <code>no</code> is specified, numeric addresses are printed instead. The default is <code>yes</code>, unless modified using the command line <code>-n</code> switch.</p>
<dt><code>keyid </code><i>keyid</i></p>
<dd>This command allows the specification of a key number to be used to authenticate configuration requests from ntpdc to the host(s). This must correspond to a key number which the host/server has been configured to use for this purpose (server options: <code>trustedkey</code>, and <code>requestkey</code>). If authentication is not enabled on the host(s) for ntpdc commands, the command <code>&quot;keyid 0&quot;</code> should be given; otherwise the <i>keyid</i> of the next subsequent <code>addpeer/addserver/broadcast </code> command will be used.</p>
<dt><code>quit</code></p>
<dd>Exit <code>ntpdc</code>46</p>
<dt><code>passwd</code></p>
<dd>This command prompts you to type in a password (which will not be echoed) which will be used to authenticate configuration requests. The password must correspond to the key configured for use by the NTP server for this purpose if such requests are to be successful.</p>
<dt><code>timeout </code><i>milliseconds</i></p>
<dd>Specify a timeout period for responses to server queries. The default is about 8000 milliseconds. Note that since <code>ntpdc</code> retries each query once after a timeout, the total waiting time for a timeout will be twice the timeout value set.</dl>
</dl>
<h2>Control Message Commands</h2>
<p>Query commands result in NTP mode 7 packets containing requests for information being sent to the server. These are read-only commands in that they make no modification of the server configuration state. </p>
<dl>
<dd>
<dl>
<dt><code>listpeers</code></p>
<dd>Obtains and prints a brief list of the peers for which the server is maintaining state. These should include all configured peer associations as well as those peers whose stratum is such that they are considered by the server to be possible future synchronization candidates.</p>
<dt><code>peers</code></p>
<dd>Obtains a list of peers for which the server is maintaining state, along with a summary of that state. Summary information includes the address of the remote peer, the local interface address (0.0.0.0 if a local address has yet to be determined), the stratum of the remote peer (a stratum of 16 indicates the remote peer is unsynchronized), the polling interval, in seconds, the reachability register, in octal, and the current estimated delay, offset and dispersion of the peer, all in seconds. The character in the left margin indicates the mode this peer entry is operating in. A <code>+</code> denotes symmetric active, a <code>&#8211;</code> indicates symmetric passive, a <code>=</code> means the remote server is being polled in client mode, a <code>^</code> indicates that the server is broadcasting to this address, a <code>~</code> denotes that the remote peer is sending broadcasts and a <code>*</code> marks the peer the server is currently synchronizing to. </p>
<p> The contents of the host field may be one of four forms. It may be a host name, an IP address, a reference clock implementation name with its parameter or <code>REFCLK(</code><i>implementation number</i><code>, </code><i>parameter</i><code>)</code>46 On <code>hostnames no</code> only IP-addresses will be displayed. </p>
<dt><code>dmpeers</code></p>
<dd>A slightly different peer summary list. Identical to the output of the <code>peers</code> command, except for the character in the leftmost column. Characters only appear beside peers which were included in the final stage of the clock selection algorithm. A <code>46</code> indicates that this peer was cast off in the falseticker detection, while a <code>+</code> indicates that the peer made it through. A <code>*</code> denotes the peer the server is currently synchronizing with.</p>
<dt><code>showpeer </code><i>peer_address</i><code> [&#8230;]</code></p>
<dd>Shows a detailed display of the current peer variables for one or more peers. Most of these values are described in the NTP Version 2 specification.</p>
<dt><code>pstats </code><i>peer_address</i><code> [&#8230;]</code></p>
<dd>Show per-peer statistic counters associated with the specified peer(s).</p>
<dt><code>clockinfo </code><i>clock_peer_address</i><code> [&#8230;]</code></p>
<dd>Obtain and print information concerning a peer clock. The values obtained provide information on the setting of fudge factors and other clock performance information.</p>
<dt><code>kerninfo</code></p>
<dd>Obtain and print kernel phase-lock loop operating parameters. This information is available only if the kernel has been specially modified for a precision timekeeping function.</p>
<dt><code>loopinfo [ oneline | multiline ]</code></p>
<dd>Print the values of selected loop filter variables. The loop filter is the part of NTP which deals with adjusting the local system clock. The <code>offset</code> is the last offset given to the loop filter by the packet processing code. The <code>frequency</code> is the frequency error of the local clock in parts-per-million (ppm). The <code>time_const</code> controls the stiffness of the phase-lock loop and thus the speed at which it can adapt to oscillator drift. The <code>watchdog timer</code> value is the number of seconds which have elapsed since the last sample offset was given to the loop filter. The <code>oneline</code> and <code>multiline</code> options specify the format in which this information is to be printed, with <code>multiline</code> as the default.</p>
<dt><code>sysinfo</code></p>
<dd>Print a variety of system state variables, i.e., state related to the local server. All except the last four lines are described in the NTP Version 3 specification, RFC-1305. The <code>system flags</code> show various system flags, some of which can be set and cleared by the <code>enable</code> and <code>disable</code> configuration commands, respectively. These are the <code>auth</code>, <code>bclient</code>, <code>monitor</code>, <code>pll</code>, <code>pps</code> and <code>stats</code> flags. See the <code>ntpd</code> documentation for the meaning of these flags. There are two additional flags which are read only, the <code>kernel_pll</code> and <code>kernel_pps</code>46 These flags indicate the synchronization status when the precision time kernel modifications are in use. The <code>kernel_pll</code> indicates that the local clock is being disciplined by the kernel, while the kernel_pps indicates the kernel discipline is provided by the PPS signal. </p>
<p> The <code>stability</code> is the residual frequency error remaining after the system frequency correction is applied and is intended for maintenance and debugging. In most architectures, this value will initially decrease from as high as 500 ppm to a nominal value in the range .01 to 0.1 ppm. If it remains high for some time after starting the daemon, something may be wrong with the local clock, or the value of the kernel variable <code>tick</code> may be incorrect. </p>
<p> The <code>broadcastdelay</code> shows the default broadcast delay, as set by the <code>broadcastdelay</code> configuration command. </p>
<p> The <code>authdelay</code> shows the default authentication delay, as set by the <code>authdelay</code> configuration command. </p>
<dt><code>sysstats</code></p>
<dd>Print statistics counters maintained in the protocol module.</p>
<dt><code>memstats</code></p>
<dd>Print statistics counters related to memory allocation code.</p>
<dt><code>iostats</code></p>
<dd>Print statistics counters maintained in the input-output module.</p>
<dt><code>timerstats</code></p>
<dd>Print statistics counters maintained in the timer/event queue support code.</p>
<dt><code>reslist</code></p>
<dd>Obtain and print the server&#8217;s restriction list. This list is (usually) printed in sorted order and may help to understand how the restrictions are applied.</p>
<dt><code>ifstats</code></p>
<dd>List interface statistics for interfaces used by ntpd for network communication.</p>
<dt><code>ifreload</code></p>
<dd>Force rescan of current system interfaces. Outputs interface statistics for interfaces that could possibly change. Marks unchanged interfaces with 46, added interfaces with + and deleted interfaces with -46</p>
<dt><code>monlist [ </code><i>version</i><code> ]</code></p>
<dd>Obtain and print traffic counts collected and maintained by the monitor facility. The version number should not normally need to be specified.</p>
<dt><code>clkbug </code><i>clock_peer_address</i><code> [&#8230;]</code></p>
<dd>Obtain debugging information for a reference clock driver. This information is provided only by some clock drivers and is mostly undecodable without a copy of the driver source in hand.</dl>
</dl>
<h2>Runtime Configuration Requests</h2>
<p>All requests which cause state changes in the server are authenticated by the server using a configured NTP key (the facility can also be disabled by the server by not configuring a key). The key number and the corresponding key must also be made known to <code>ntpdc</code>46 This can be done using the keyid and passwd commands, the latter of which will prompt at the terminal for a password to use as the encryption key. You will also be prompted automatically for both the key number and password the first time a command which would result in an authenticated request to the server is given. Authentication not only provides verification that the requester has permission to make such changes, but also gives an extra degree of protection again transmission errors. </p>
<p> Authenticated requests always include a timestamp in the packet data, which is included in the computation of the authentication code. This timestamp is compared by the server to its receive time stamp. If they differ by more than a small amount the request is rejected. This is done for two reasons. First, it makes simple replay attacks on the server, by someone who might be able to overhear traffic on your LAN, much more difficult. Second, it makes it more difficult to request configuration changes to your server from topologically remote hosts. While the reconfiguration facility will work well with a server on the local host, and may work adequately between time-synchronized hosts on the same LAN, it will work very poorly for more distant hosts. As such, if reasonable passwords are chosen, care is taken in the distribution and protection of keys and appropriate source address restrictions are applied, the run time reconfiguration facility should provide an adequate level of security. </p>
<p> The following commands all make authenticated requests. </p>
<dl>
<dd>
<dl>
<dt><code>addpeer </code><i>peer_address</i><code> [ </code><i>keyid</i><code> ] [ </code><i>version</i><code> ] [ minpoll# | prefer | iburst | burst | minpoll </code><i>N</i><code> | maxpoll </code><i>N</i><code> [&#8230;] ]</code></p>
<dd>
<dt><code>addpeer </code><i>peer_address</i><code> [ prefer | iburst | burst | minpoll </code><i>N</i><code> | maxpoll </code><i>N</i><code> | keyid</code><i>N</i><code> | version </code><i>N</i><code> [&#8230;] ]</code></p>
<dd>Add a configured peer association at the given address and operating in symmetric active mode. Note that an existing association with the same peer may be deleted when this command is executed, or may simply be converted to conform to the new configuration, as appropriate. If the <code>keyid</code> is nonzero, all outgoing packets to the remote server will have an authentication field attached encrypted with this key. If the value is 0 (or not given) no authentication will be done. If ntpdc&#8217;s key number has not yet been set (<i>e.g.,</i> by the keyid command), it will be set to this value. The <code>version#</code> can be 1 through 4 and defaults to 3. The remaining options are either a numeric value for <code>minpoll</code> or literals <code>prefer</code>, <code>iburst</code>, <code>burst</code>, <code>minpoll </code><i>N</i>, <code>keyid </code><i>N</i>, <code>version </code> <i>N</i>, or <code>maxpoll </code><i>N</i> (where <i>N</i> is a numeric value), and have the action as specified in the <code>peer</code> configuration file command of ntpd. See the Server Options page for further information. Each flag (or its absence) replaces the previous setting. The <code>prefer</code> keyword indicates a preferred peer (and thus will be used primarily for clock synchronisation if possible). The preferred peer also determines the validity of the PPS signal &#8211; if the preferred peer is suitable for synchronisation so is the PPS signal. The <code>dynamic</code> keyword allows association configuration even when no suitable network interface is found at configuration time. The dynamic interface update mechanism may complete the configuration when new interfaces appear (e.g. WLAN/PPP interfaces) at a later time and thus render the association operable.</p>
<dt><code>addserver </code><i>peer_address</i><code> [ </code><i>keyid</i><code> ] [ </code><i>version</i><code> ] [ minpoll# | prefer | iburst | burst | minpoll </code><i>N</i><code> | maxpoll </code><i>N</i><code> [&#8230;] ]</code></p>
<dd>
<dt><code>addserver </code><i>peer_address</i><code> [ prefer | iburst | burst | minpoll </code><i>N</i><code> | maxpoll </code><i>N</i><code> | keyid</code><i>N</i><code> | version </code><i>N</i><code> [&#8230;] ]</code></p>
<dd>Identical to the addpeer command, except that the operating mode is client.</p>
<dt><code>broadcast </code><i>peer_address</i><code> [ </code><i>keyid</i><code> ] [ </code><i>version</i><code> ] [ </code><i>prefer</i><code> ]</code></p>
<dd>Identical to the addpeer command, except that the operating mode is broadcast. In this case a valid non-zero key identifier and key are required. The <code>peer_address</code> parameter can be the broadcast address of the local network or a multicast group address assigned to NTP. If a multicast address, a multicast-capable kernel is required.</p>
<dt><code>unconfig </code><i>peer_address</i><code> [&#8230;]</code></p>
<dd>This command causes the configured bit to be removed from the specified peer(s). In many cases this will cause the peer association to be deleted. When appropriate, however, the association may persist in an unconfigured mode if the remote peer is willing to continue on in this fashion.</p>
<dt><code>fudge </code><i>peer_address</i><code> [ </code><i>time1</i><code> ] [ </code><i>time2</i><code> ] [ </code><i>stratum</i><code> ] [ </code><i>refid</i><code> ]</code></p>
<dd>This command provides a way to set certain data for a reference clock. See the source listing for further information.</p>
<dt><code>enable [ auth | bclient | calibrate | kernel | monitor | ntp | pps | stats]</code></p>
<dd>
<dt><code>disable [ auth | bclient | calibrate | kernel | monitor | ntp | pps | stats]</code></p>
<dd>These commands operate in the same way as the <code>enable</code> and <code>disable</code> configuration file commands of <code>ntpd</code>46 See the Miscellaneous Options page for further information.</p>
<dt><code>restrict </code><i>address mask flag</i><code> [ </code><i>flag</i><code> ]</code></p>
<dd>This command operates in the same way as the <code>restrict</code> configuration file commands of <code>ntpd</code>46</p>
<dt><code>unrestrict </code><i>address mask flag</i><code> [ </code><i>flag</i><code> ]</code></p>
<dd>Unrestrict the matching entry from the restrict list.</p>
<dt><code>delrestrict </code><i>address mask [ ntpport ]</i></p>
<dd>Delete the matching entry from the restrict list.</p>
<dt><code>readkeys</code></p>
<dd>Causes the current set of authentication keys to be purged and a new set to be obtained by rereading the keys file (which must have been specified in the <code>ntpd</code> configuration file). This allows encryption keys to be changed without restarting the server.</p>
<dt><code>trustedkey </code><i>keyid</i><code> [&#8230;]</code></p>
<dd>
<dt><code>untrustedkey </code><i>keyid</i><code> [&#8230;]</code></p>
<dd>These commands operate in the same way as the <code>trustedkey</code> and <code>untrustedkey</code> configuration file commands of <code>ntpd</code>46</p>
<dt><code>authinfo</code></p>
<dd>Returns information concerning the authentication module, including known keys and counts of encryptions and decryptions which have been done.</p>
<dt><code>traps</code></p>
<dd>Display the traps set in the server. See the source listing for further information.</p>
<dt><code>addtrap [ </code><i>address</i><code> ] [ </code><i>port</i><code> ] [ </code><i>interface</i><code> ]</code></p>
<dd>Set a trap for asynchronous messages. See the source listing for further information.</p>
<dt><code>clrtrap [ </code><i>address</i><code> ] [ </code><i>port</i><code> ] [ </code><i>interface</i><code>]</code></p>
<dd>Clear a trap for asynchronous messages. See the source listing for further information.</p>
<dt><code>reset</code></p>
<dd>Clear the statistics counters in various modules of the server. See the source listing for further information.</dl>
</dl>
<h2>Bugs</h2>
<p><code>ntpdc</code> is a crude hack. Much of the information it shows is deadly boring and could only be loved by its implementer. The program was designed so that new (and temporary) features were easy to hack in, at great expense to the program&#8217;s ease of use. Despite this, the program is occasionally useful. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
