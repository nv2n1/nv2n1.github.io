---
title: "ntp(5)"
name: "ntp"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp/"
description: "ntp.conf – Server Options"
---

<p>ntp.conf &#8211; Server Options</p>
<h2>&nbsp;<wbr></h2>
<p>Following is a description of the configuration commands in NTPv4. There are two classes of commands, configuration commands that configure an association with a remote server, peer or reference clock, and auxilliary commands that specify environmental variables that control various related operations. </p>
<h2>Configuration Commands</h2>
<p>The various modes are determined by the command keyword and the required IP address. Addresses are classed by type as (s) a remote server or peer (IPv4 class A, B and C), (b) the broadcast address of a local interface, (m) a multicast address (IPv4 class D), or (r) a reference clock address (127.127.x.x). The options that can be used with these commands are listed below. </p>
<p> If the Basic Socket Interface Extensions for IPv6 (RFC-2553) is detected, support for the IPv6 address family is generated in addition to the default support of the IPv4 address family. IPv6 addresses can be identified by the presence of colons &quot;:&quot; in the address field. IPv6 addresses can be used almost everywhere where IPv4 addresses can be used, with the exception of reference clock addresses, which are always IPv4. Note that in contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. </p>
<p> There are three types of associations: persistent, preemptable and ephemeral. Persistent associations are mobilized by a configuration command and never demobilized. Preemptable associations, which are new to NTPv4, are mobilized by a configuration command which includes the <code>prempt</code> flag and are demobilized by timeout or error. Ephemeral associations are mobilized upon arrival of designated messages and demobilized by timeout or error. </p>
<dl>
<dd>
<dl>
<dt><code>server </code><i>address</i><code> [options &#8230;]</code></p>
<dd>
<dt><code>peer </code><i>address</i><code> [options &#8230;]</code></p>
<dd>
<dt><code>broadcast </code><i>address</i><code> [options &#8230;]</code></p>
<dd>
<dt><code>manycastclient </code><i>address</i><code> [options &#8230;]</code></p>
<dd>These four commands specify the time server name or address to be used and the mode in which to operate. The <i>address</i> can be either a DNS name or a IP address in dotted-quad notation. Additional information on association behavior can be found in the Association Management page.</p>
<dl>
<dd>
<dl>
<dt><code>server</code></p>
<dd>For type s and r addresses (only), this command normally mobilizes a persistent client mode association with the specified remote server or local reference clock. If the <code>preempt</code> flag is specified, a preemptable association is mobilized instead. In client mode the client clock can synchronize to the remote server or local reference clock, but the remote server can never be synchronized to the client clock. This command should NOT be used for type <code>b</code> or <code>m</code> addresses.</p>
<dt><code>peer</code></p>
<dd>For type s addresses (only), this command mobilizes a persistent symmetric-active mode association with the specified remote peer. In this mode the local clock can be synchronized to the remote peer or the remote peer can be synchronized to the local clock. This is useful in a network of servers where, depending on various failure scenarios, either the local or remote peer may be the better source of time. This command should NOT be used for type <code>b</code>, <code>m</code> or <code>r</code> addresses.</p>
<dt><code>broadcast</code></p>
<dd>For type <code>b</code> and <code>m</code> addresses (only), this command mobilizes a persistent broadcast mode association. Multiple commands can be used to specify multiple local broadcast interfaces (subnets) and/or multiple multicast groups. Note that local broadcast messages go only to the interface associated with the subnet specified, but multicast messages go to all interfaces. In broadcast mode the local server sends periodic broadcast messages to a client population at the <i></i><code>address</code><i></i> specified, which is usually the broadcast address on (one of) the local network(s) or a multicast address assigned to NTP. The IANA has assigned the multicast group address IPv4 224.0.1.1 and IPv6 ff05::101 (site local) exclusively to NTP, but other nonconflicting addresses can be used to contain the messages within administrative boundaries. Ordinarily, this specification applies only to the local server operating as a sender; for operation as a broadcast client, see the <code>broadcastclient</code> or <code>multicastclient</code> commands below.</p>
<dt><code>manycastclient</code></p>
<dd>For type <code>m</code> addresses (only), this command mobilizes a preemptable manycast client mode association for the multicast group address specified. In this mode a specific address must be supplied which matches the address used on the <code>manycastserver</code> command for the designated manycast servers. The NTP multicast address 224.0.1.1 assigned by the IANA should NOT be used, unless specific means are taken to avoid spraying large areas of the Internet with these messages and causing a possibly massive implosion of replies at the sender. The <code>manycastclient</code> command specifies that the host is to operate in client mode with the remote servers that are discovered as the result of broadcast/multicast messages. The client broadcasts a request message to the group address associated with the specified <i></i><code>address</code><i></i> and specifically enabled servers respond to these messages. The client selects the servers providing the best time and continues as with the <code>server </code>command. The remaining servers are discarded as if never heard.</dl>
</dl>
</dl>
</dl>
<h2>Command Options</h2>
<dl>
<dd>
<dl>
<dt><code>autokey</code></p>
<dd>All packets sent to and received from the server or peer are to include authentication fields encrypted using the autokey scheme described in the Authentication Options page. This option is valid with all commands.</p>
<dt><code>burst</code></p>
<dd>When the server is reachable, send a burst of eight packets instead of the usual one. The packet spacing is normally 2 s; however, the spacing between the first and second packets can be changed with the <code>calldelay</code> command to allow additional time for a modem or ISDN call to complete. This option is valid with only the <code>server</code> command and is a recommended option with this command when the <code>maxpoll</code> option is 11 or greater.</p>
<dt><code>iburst</code></p>
<dd>When the server is unreachable, send a burst of eight packets instead of the usual one. The packet spacing is normally 2 s; however, the spacing between the first and second packets can be changed with the <code>calldelay</code> command to allow additional time for a modem or ISDN call to complete. This option is valid with only the <code>server</code> command and is a recommended option with this command.</p>
<dt><code>key</code> <i></i><code>key</code><i></i></p>
<dd>All packets sent to and received from the server or peer are to include authentication fields encrypted using the specified <i></i><code>key</code><i></i> identifier with values from 1 to 65534, inclusive. The default is to include no encryption field. This option is valid with all commands.</p>
<dt><code>minpoll </code><i>minpoll</i></p>
<dd>
<dt><code>maxpoll </code><i>maxpoll</i></p>
<dd>These options specify the minimum and maximum poll intervals for NTP messages, in seconds as a power of two. The maximum poll interval defaults to 10 (1,024 s), but can be increased by the <code>maxpoll</code> option to an upper limit of 17 (36.4 h). The minimum poll interval defaults to 6 (64 s), but can be decreased by the <code>minpoll</code> option to a lower limit of 3 (8 s). These option are valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>noselect</code></p>
<dd>Marks the server as unused, except for display purposes. The server is discarded by the selection algorithm. This option is valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>preempt</code></p>
<dd>Specifies the association as preemptable rather than the default persistent. This option is valied only with the <code>server</code> command.</p>
<dt><code>prefer</code></p>
<dd>Marks the server as preferred. All other things being equal, this host will be chosen for synchronization among a set of correctly operating hosts. See the Mitigation Rules and the <code>prefer</code> Keyword page for further information. This option is valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>true</code></p>
<dd>Force the association to assume truechimer status; that is, always survive the selection and clustering algorithms. This option can be used with any association, but is most useful for reference clocks with large jitter on the serial port and precision pulse-per-second (PPS) signals. Caution: this option defeats the algorithms designed to cast out falsetickers and can allow these sources to set the system clock. This option is valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>ttl </code><i>ttl</i></p>
<dd>This option is used only with broadcast server and manycast client modes. It specifies the time-to-live <i></i><code>ttl</code><i></i> to use on broadcast server and multicast server and the maximum <i></i><code>ttl</code><i></i> for the expanding ring search with manycast client packets. Selection of the proper value, which defaults to 127, is something of a black art and should be coordinated with the network administrator.</p>
<dt><code>version </code><i>version</i></p>
<dd>Specifies the version number to be used for outgoing NTP packets. Versions 1-4 are the choices, with version 4 the default. This option is valid only with the <code>server,</code> <code>peer</code> and <code>broadcast</code> commands.</dl>
</dl>
<h2>Auxilliary Commands</h2>
<dl>
<dd>
<dl>
<dt><code>broadcastclient [novolley]</code></p>
<dd>This command enables reception of broadcast server messages to any local interface (type <code>b</code>) address. Ordinarily, upon receiving a message for the first time, the broadcast client measures the nominal server propagation delay using a brief client/server exchange with the server, after which it continues in listen-only mode. If the <code>novolley</code> keyword is present, the exchange is not used and the value specified in the <code>broadcastdelay</code> command is used or, if the <code>broadcastdelay</code> command is not used, the default 4.0 ms. Note that, in order to avoid accidental or malicious disruption in this mode, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page. Note that the <code>novolley</code> keyword is incompatible with public key authentication.</p>
<dt><code>manycastserver </code><i>address</i><code> [&#8230;]</code></p>
<dd>This command enables reception of manycast client messages to the multicast group address(es) (type <code>m</code>) specified. At least one address is required. The NTP multicast address 224.0.1.1 assigned by the IANA should NOT be used, unless specific means are taken to limit the span of the reply and avoid a possibly massive implosion at the original sender. Note that, in order to avoid accidental or malicious disruption in this mode, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page.</p>
<dt><code>multicastclient </code><i>address</i><code> [&#8230;]</code></p>
<dd>This command enables reception of multicast server messages to the multicast group address(es) (type <code>m</code>) specified. Upon receiving a message for the first time, the multicast client measures the nominal server propagation delay using a brief client/server exchange with the server, then enters the broadcast client mode, in which it synchronizes to succeeding multicast messages. Note that, in order to avoid accidental or malicious disruption in this mode, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page.</dl>
</dl>
<h2>Bugs</h2>
<p>The syntax checking is not picky; some combinations of ridiculous and even hilarious options and modes may not be detected. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/5-ntp_auth/">ntp_auth</a>(5), <a href="/docs/linux/man/5-ntp_mon/">ntp_mon</a>(5), <a href="/docs/linux/man/5-ntp_acc/">ntp_acc</a>(5), <a href="/docs/linux/man/5-ntp_clock/">ntp_clock</a>(5), <a href="/docs/linux/man/5-ntp_misc/">ntp_misc</a>(5) Primary source of documentation: /usr/share/doc/ntp-* This file was automatically generated from HTML source. </p>
