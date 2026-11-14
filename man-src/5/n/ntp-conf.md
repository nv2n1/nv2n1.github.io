---
title: "ntp-conf(5)"
name: "ntp-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp-conf/"
description: "ntp.conf – Server Options"
---

<p>ntp.conf &#8211; Server Options</p>
<h2>&nbsp;<wbr></h2>
<p>Following is a description of the configuration commands in NTPv4. There are two classes of commands, configuration commands that configure an association with a remote server, peer or reference clock, and auxilliary commands that specify environmental variables that control various related operations. The various modes described on the Association Management page are determined by the command keyword and the DNS name or IP address. Addresses are classed by type as (s) a remote server or peer (IPv4 class A, B and C), (b) the IP broadcast address of a local interface, (m) a multicast address (IPv4 class D), or (r) a reference clock address (127.127.x.x). For type m addresses the IANA has assigned the multicast group address IPv4 224.0.1.1 and IPv6 ff05::101 (site local) exclusively to NTP, but other nonconflicting addresses can be used. If the Basic Socket Interface Extensions for IPv6 (RFC-2553) is detected, support for the IPv6 address family is generated in addition to the default IPv4 address family. IPv6 addresses can be identified by the presence of colons &quot;:&quot; in the address field. IPv6 addresses can be used almost everywhere where IPv4 addresses can be used, with the exception of reference clock addresses, which are always IPv4. Note that in contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. </p>
<h2>Configuration Commands</h2>
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
<dd>
<dt><code>pool </code><i>address</i><code> [options &#8230;]</code></p>
<dd>
<dt><code>unpeer [</code><i>address</i><code> | </code><i>associd</i><code>]</code></p>
<dd>These commands specify the time server name or address to be used and the mode in which to operate. The <i>address</i> can be either a DNS name or a IPv4 or IPv6 address in standard notation. In general, multiple commands of each type can be used for different server and peer addresses or multicast groups.</p>
<dl>
<dd>
<dl>
<dt><code>server</code></p>
<dd>For type s and r addresses (only), this command mobilizes a persistent client mode association with the specified remote server or local reference clock. If the <code>preempt</code> flag is specified, a preemptable client mode association is mobilized instead.</p>
<dt><code>peer</code></p>
<dd>For type s addresses (only), this command mobilizes a persistent symmetric-active mode association with the specified remote peer.</p>
<dt><code>broadcast</code></p>
<dd>For type b and m addressees (only), this command mobilizes a persistent broadcast or multicast server mode association. Note that type b messages go only to the interface specified, but type m messages go to all interfaces.</p>
<dt><code>manycastclient</code></p>
<dd>For type m addresses (only), this command mobilizes a manycast client mode association for the multicast group address specified. In this mode the address must match the address specified on the <code>manycastserver</code> command of one or more designated manycast servers.</p>
<dt><code>pool</code></p>
<dd>For type s messages (only) this command mobilizes a client mode association for servers implementing the pool automatic server discovery scheme described on the Association Management page. The address is a DNS name in the form <i>area</i><code>46pool.ntp.org</code>, where <i>area</i> is a qualifier designating the server geographic area such as <code>us</code> or <code>europe</code>46</p>
<dt><code>unpeer</code></p>
<dd>This command removes a previously configured association. An address or association ID can be used to identify the association. Either an IP address or DNS name can be used. This command is most useful when supplied via <code>ntpq</code> runtime configuration commands <code>:config</code> and <code>config-from-file</code>46</dl>
</dl>
</dl>
</dl>
<h2>Command Options</h2>
<dl>
<dd>
<dl>
<dt><code>autokey</code></p>
<dd>Send and receive packets authenticated by the Autokey scheme described in the Authentication Options page. This option is mutually exclusive with the <code>key</code> option.</p>
<dt><code>burst</code></p>
<dd>When the server is reachable, send a burst of eight packets instead of the usual one. The packet spacing is normally 2 s; however, the spacing between the first and second packets can be changed with the <code>calldelay</code> command to allow additional time for a modem or ISDN call to complete. This option is valid only with the <code>server</code> command and type s addressesa. It is a recommended option when the <code>maxpoll</code> option is greater than 10 (1024 s).</p>
<dt><code>iburst</code></p>
<dd>When the server is unreachable, send a burst of eight packets instead of the usual one. The packet spacing is normally 2 s; however, the spacing between the first and second packets can be changed with the <code>calldelay</code> command to allow additional time for a modem or ISDN call to complete. This option is valid only with the <code>server</code> command and type s addresses. It is a recommended option with this command.</p>
<dt><code>key</code> <i></i><code>key</code><i></i></p>
<dd>Send and receive packets authenticated by the symmetric key scheme described in the Authentication Options page. The <i></i><code>key</code><i></i> specifies the key identifier with values from 1 to 65534, inclusive. This option is mutually exclusive with the <code>autokey</code> option.</p>
<dt><code>minpoll </code><i>minpoll</p>
<dd>
<dt></i><code>maxpoll </code><i>maxpoll</i></p>
<dd>These options specify the minimum and maximum poll intervals for NTP messages, in seconds as a power of two. The maximum poll interval defaults to 10 (1024 s), but can be increased by the <code>maxpoll</code> option to an upper limit of 17 (36 h). The minimum poll interval defaults to 6 (64 s), but can be decreased by the <code>minpoll</code> option to a lower limit of 3 (8 s).</p>
<dt><code>mode </code><i>option</i></p>
<dd>Pass the <i>option</i> to a reference clock driver, where <i>option</i> is an integer in the range from 0 to 255, inclusive. This option is valid only with type r addresses.</p>
<dt><code>noselect</code></p>
<dd>Marks the server or peer to be ignored by the selection algorithm but visible to the monitoring program. This option is ignored with the <code>broadcast</code> command.</p>
<dt><code>preempt</code></p>
<dd>Specifies the association as preemptable rather than the default persistent. This option is ignored with the <code>broadcast</code> command and is most useful with the <code>manycastclient</code> and <code>pool</code> commands.</p>
<dt><code>prefer</code></p>
<dd>Mark the server as preferred. All other things being equal, this host will be chosen for synchronization among a set of correctly operating hosts. See the Mitigation Rules and the <code>prefer</code> Keyword page for further information. This option is valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>true</code></p>
<dd>Mark the association to assume truechimer status; that is, always survive the selection and clustering algorithms. This option can be used with any association, but is most useful for reference clocks with large jitter on the serial port and precision pulse-per-second (PPS) signals. Caution: this option defeats the algorithms designed to cast out falsetickers and can allow these sources to set the system clock. This option is valid only with the <code>server</code> and <code>peer</code> commands.</p>
<dt><code>ttl </code><i>ttl</i></p>
<dd>This option specifies the time-to-live <i></i><code>ttl</code><i></i> for the <code>broadcast</code> command and the maximum <i></i><code>ttl</code><i></i> for the expanding ring search used by the <code>manycastclient</code> command. Selection of the proper value, which defaults to 127, is something of a black art and should be coordinated with the network administrator. This option is invalid with type r addresses.</p>
<dt><code>version </code><i>version</i></p>
<dd>Specifies the version number to be used f or outgoing NTP packets. Versions 1-4 are the choices, with version 4 the default.</p>
<dt><code>xleave</code></p>
<dd>Operate in interleaved mode (symmetric and broadcast modes only). (see NTP Interleaved Modes)</dl>
</dl>
<h2>Auxilliary Commands</h2>
<dl>
<dd>
<dl>
<dt><code>broadcastclient</code></p>
<dd>Enable reception of broadcast server messages to any local interface (type b address). Ordinarily, upon receiving a broadcast message for the first time, the broadcast client measures the nominal server propagation delay using a brief client/server exchange, after which it continues in listen-only mode. If a nonzero value is specified in the <code>broadcastdelay</code> command, the value becomes the delay and the volley is not executed. Note: the <code>novolley</code> option has been deprecated for future enhancements. Note that, in order to avoid accidental or malicious disruption in this mode, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page. Note that the <code>novolley</code> keyword is incompatible with public key authentication.</p>
<dt><code>manycastserver </code><i>address</i><code> [&#8230;]</code></p>
<dd>Enable reception of manycast client messages (type m)to the multicast group address(es) (type m) specified. At least one address is required. Note that, in order to avoid accidental or malicious disruption, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page.</p>
<dt><code>multicastclient </code><i>address</i><code> [&#8230;]</code></p>
<dd>Enable reception of multicast server messages to the multicast group address(es) (type m) specified. Upon receiving a message for the first time, the multicast client measures the nominal server propagation delay using a brief client/server exchange with the server, then enters the broadcast client mode, in which it synchronizes to succeeding multicast messages. Note that, in order to avoid accidental or malicious disruption in this mode, both the server and client should operate using symmetric key or public key authentication as described in the Authentication Options page.</dl>
</dl>
<h2>Bugs</h2>
<p>The syntax checking is not picky; some combinations of ridiculous and even hilarious options and modes may not be detected. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/5-ntp_auth/">ntp_auth</a>(5), <a href="/docs/linux/man/5-ntp_mon/">ntp_mon</a>(5), <a href="/docs/linux/man/5-ntp_acc/">ntp_acc</a>(5), <a href="/docs/linux/man/5-ntp_clock/">ntp_clock</a>(5), <a href="/docs/linux/man/5-ntp_misc/">ntp_misc</a>(5) The official HTML documentation. This file was automatically generated from HTML source. </p>
