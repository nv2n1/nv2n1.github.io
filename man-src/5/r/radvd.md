---
title: "radvd(5)"
name: "radvd"
section: "5"
letter: "r"
url: "/docs/linux/man/5-radvd/"
description: "radvd.conf – configuration file of the router advertisement daemon radvd"
---

<p>radvd.conf &#8211; configuration file of the router advertisement daemon <code>radvd</code></p>
<h2>Description</h2>
<p>This file describes the information which is included in the router advertisement (RA) of a specific interface. The file contains one or more interface definitions of the form: </p>
<pre><code>interface </code>name <code>{</code>
 list of interface specific options
 list of prefix definitions
 list of clients (IPv6 addresses) to advertise to
 list of route definitions
 list of RDNSS definitions
 list of DNSSL definitions
 list of ABRO definitions
<code>};</code></pre>
<p>All the possible interface specific options are detailed below. Each option has to be terminated by a semicolon. Prefix definitions are of the form: </p>
<pre><code>prefix </code>prefix<code>/</code>length <code>{</code>
 list of prefix specific options
<code>};</code></pre>
<p>Prefix can be network prefix or the address of the interface. The address of interface should be used when using Mobile IPv6 extensions. Special prefix &quot;::/64&quot; is also supported on systems that implement getifaddrs() (on other systems, configuration activation fails and radvd exits). When configured, radvd picks all non-link-local prefix assigned to the interface and starts advertising it. This may be applicable in non-6to4 scenarios where the upstream prefix might change. This option is incompatible with Base6to4Interface option. AdvRouterAddr option is always enabled when this configuration is used. All the possible prefix specific options are described below. Each option has to be terminated by a semicolon. Decimal values are allowed only for MinDelayBetweenRAs, MaxRtrAdvInterval and MinRtrAdvInterval. Decimal values should be used only when using Mobile IPv6 extensions. Route definitions are of the form: </p>
<pre><code>route </code>prefix<code>/</code>length <code>{</code>
 list of route specific options
<code>};</code></pre>
<p>The prefix of a route definition should be network prefix; it can be used to advertise more specific routes to the hosts. RDNSS (Recursive DNS server) definitions are of the form: </p>
<pre><code>RDNSS </code>ip [ip] [ip] <code>{</code>
 list of rdnss specific options
<code>};</code></pre>
<p>DNSSL (DNS Search List) definitions are of the form: </p>
<pre><code>DNSSL </code>suffix [suffix] [suffix] [...] <code>{</code>
 list of dnssl specific options
<code>};</code></pre>
<p>By default radvd will send route advertisements so that every node on the link can use them. The list of clients (IPv6 address) to advertise to, and accept route solicitations from can be configured. If done, radvd does not send send messages to the multicast addresses but to the configured unicast addresses only. Solicitations from other addresses are refused. This is similar to UnicastOnly but includes periodic messages and incoming client access configuration. See examples section for a use case of this. The definitions are of the form: </p>
<pre><code>clients </code>{
 list of IPv6 addresses
<code>};</code></pre>
<p>ABRO (Authoritative Border Router Option) definitions are of the form: </p>
<pre><code>abro </code>prefix<code>/</code>length <code>{</code>
 list of abro specific options
<code>};</code></pre>
<p>Prefix can be network prefix or the address of the interface. </p>
<h2>Interface Specific Options</h2>
<dl>
<dt><code>IgnoreIfMissing</code> <code>on</code>|<code>off</code></p>
<dd>A flag indicating whether or not the interface is ignored if it does not exist at start-up. By default, radvd exits. </p>
<p> This is useful for dynamic interfaces which are not active when radvd starts or which are dynamically disabled and re-enabled during the time radvd runs. </p>
<p> Current versions of radvd automatically try to re-enable interfaces. </p>
<p> Enabling IgnoreIfMissing also quenches certain warnings in log messages relating to missing interfaces. </p>
<p> Default: on </p>
<dt><code>AdvSendAdvert</code> <code>on</code>|<code>off</code></p>
<dd>A flag indicating whether or not the router sends periodic router advertisements and responds to router solicitations. </p>
<p> This option no longer has to be specified first, but it needs to be <code>on</code> to enable advertisement on this interface. </p>
<p> Default: off </p>
<dt><code>UnicastOnly</code> <code>on</code>|<code>off</code></p>
<dd>Indicates that the interface link type only supports unicast. This will prevent unsolicited advertisements from being sent, and will cause solicited advertisements to be unicast to the soliciting node. This option is necessary for non-broadcast, multiple-access links, such as ISATAP. </p>
<p> Default: off </p>
<dt><code>MaxRtrAdvInterval </code>seconds</p>
<dd>The maximum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. </p>
<p> Must be no less than 4 seconds and no greater than 1800 seconds. </p>
<p> Minimum when using Mobile IPv6 extensions: 0.07. </p>
<p> For values less than 0.2 seconds, 0.02 seconds is added to account for scheduling granularities as specified in RFC3775. </p>
<p> Default: 600 seconds<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>MinRtrAdvInterval </code>seconds</p>
<dd>The minimum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. </p>
<p> Must be no less than 3 seconds and no greater than 0.75 * MaxRtrAdvInterval. </p>
<p> Minimum when using Mobile IPv6 extensions: 0.03. </p>
<p> Default: 0.33 * MaxRtrAdvInterval </p>
<dt><code>MinDelayBetweenRAs </code>seconds</p>
<dd>The minimum time allowed between sending multicast router advertisements from the interface, in seconds. </p>
<p> This applies to solicited multicast RAs. This is defined as the protocol constant MIN_DELAY_BETWEEN_RAS in RFC4861. MIPv6 redefines this parameter to have a minimum of 0.03 seconds. </p>
<p> Minimum when using Mobile IPv6 extensions: 0.03. </p>
<p> Default: 3 </p>
<dt><code>AdvManagedFlag</code> <code>on</code>|<code>off</code></p>
<dd>When set, hosts use the administered (stateful) protocol for address autoconfiguration in addition to any addresses autoconfigured using stateless address autoconfiguration. The use of this flag is described in RFC 4862. </p>
<p> Default: off </p>
<dt><code>AdvOtherConfigFlag</code> <code>on</code>|<code>off</code></p>
<dd>When set, hosts use the administered (stateful) protocol for autoconfiguration of other (non-address) information. The use of this flag is described in RFC 4862. </p>
<p> Default: off </p>
<dt><code>AdvLinkMTU </code>integer</p>
<dd>The MTU option is used in router advertisement messages to insure that all nodes on a link use the same MTU value in those cases where the link MTU is not well known. </p>
<p> If specified, i.e. not 0, must not be smaller than 1280 and not greater than the maximum MTU allowed for this link (e.g. ethernet has a maximum MTU of 1500. See RFC 4864). </p>
<p> Default: 0 </p>
<dt><code>AdvReachableTime </code>milliseconds</p>
<dd>The time, in milliseconds, that a node assumes a neighbor is reachable after having received a reachability confirmation. Used by the Neighbor Unreachability Detection algorithm (see Section 7.3 of RFC 4861). A value of zero means unspecified (by this router). </p>
<p> Must be no greater than 3,600,000 milliseconds (1 hour). </p>
<p> Default: 0 </p>
<dt><code>AdvRetransTimer </code>milliseconds</p>
<dd>The time, in milliseconds, between retransmitted Neighbor Solicitation messages. Used by address resolution and the Neighbor Unreachability Detection algorithm (see Sections 7.2 and 7.3 of RFC 4861). A value of zero means unspecified (by this router). </p>
<p> Default: 0 </p>
<dt><code>AdvCurHopLimit </code>integer</p>
<dd>The default value that should be placed in the Hop Count field of the IP header for outgoing (unicast) IP packets. The value should be set to the current diameter of the Internet. The value zero means unspecified (by this router). </p>
<p> Default: 64 </p>
<dt><code>AdvDefaultLifetime </code>seconds</p>
<dd>The lifetime associated with the default router in units of seconds. The maximum value corresponds to 18.2 hours. A lifetime of 0 indicates that the router is not a default router and should not appear on the default router list. The router lifetime applies only to the router&#8217;s usefulness as a default router; it does not apply to information contained in other message fields or options. Options that need time limits for their information include their own lifetime fields. </p>
<p> Must be either zero or between MaxRtrAdvInterval and 9000 seconds. </p>
<p> Default: 3 * MaxRtrAdvInterval (Minimum 1 second). </p>
<dt><code>AdvDefaultPreference</code> <code>low</code>|<code>medium</code>|<code>high</code></p>
<dd>The preference associated with the default router, as either &quot;low&quot;, &quot;medium&quot;, or &quot;high&quot;. </p>
<p> Default: medium </p>
<dt><code>AdvSourceLLAddress</code> <code>on</code>|<code>off</code></p>
<dd>When set, the link-layer address of the outgoing interface is included in the RA. </p>
<p> Default: on </p>
<dt><code>AdvHomeAgentFlag</code> <code>on</code>|<code>off</code></p>
<dd>When set, indicates that sending router is able to serve as Mobile IPv6 Home Agent. When set, minimum limits specified by Mobile IPv6 are used for MinRtrAdvInterval and MaxRtrAdvInterval. </p>
<p> Default: off </p>
<dt><code>AdvHomeAgentInfo</code> <code>on</code>|<code>off</code></p>
<dd>When set, Home Agent Information Option (specified by Mobile IPv6) is included in Router Advertisements. AdvHomeAgentFlag must also be set when using this option. </p>
<p> Default: off </p>
<dt><code>HomeAgentLifetime </code>seconds</p>
<dd>The length of time in seconds (relative to the time the packet is sent) that the router is offering Mobile IPv6 Home Agent services. A value 0 must not be used. The maximum lifetime is 65520 seconds (18.2 hours). This option is ignored, if AdvHomeAgentInfo is not set. </p>
<p> If both HomeAgentLifetime and HomeAgentPreference are set to their default values, Home Agent Information Option will not be sent. </p>
<p> Default: AdvDefaultLifetime </p>
<dt><code>HomeAgentPreference </code>integer</p>
<dd>The preference for the Home Agent sending this Router Advertisement. Values greater than 0 indicate more preferable Home Agent, values less than 0 indicate less preferable Home Agent. This option is ignored, if AdvHomeAgentInfo is not set. </p>
<p> If both HomeAgentLifetime and HomeAgentPreference are set to their default values, Home Agent Information Option will not be sent. </p>
<p> Default: 0 </p>
<dt><code>AdvMobRtrSupportFlag</code> <code>on</code>|<code>off</code></p>
<dd>When set, the Home Agent signals it supports Mobile Router registrations (specified by NEMO Basic). AdvHomeAgentInfo must also be set when using this option. </p>
<p> Default: off </p>
<dt><code>AdvIntervalOpt</code> <code>on</code>|<code>off</code></p>
<dd>When set, Advertisement Interval Option (specified by Mobile IPv6) is included in Router Advertisements. When set, minimum limits specified by Mobile IPv6 are used for MinRtrAdvInterval and MaxRtrAdvInterval. </p>
<p> The advertisement interval is based on the configured MaxRtrAdvInterval parameter except where this is less than 200ms. In this case, the advertised interval is ( MaxRtrAdvInterval + 20ms ). </p>
<p> Default: off </p>
</dl>
<h2>Prefix Specific Options</h2>
<dl>
<dt><code>AdvOnLink</code> <code>on</code>|<code>off</code></p>
<dd>When set, indicates that this prefix can be used for on-link determination. When not set the advertisement makes no statement about on-link or off-link properties of the prefix. For instance, the prefix might be used for address configuration with some of the addresses belonging to the prefix being on-link and others being off-link. </p>
<p> Default: on </p>
<dt><code>AdvAutonomous</code> <code>on</code>|<code>off</code></p>
<dd>When set, indicates that this prefix can be used for autonomous address configuration as specified in RFC 4862. </p>
<p> Default: on </p>
<dt><code>AdvRouterAddr</code> <code>on</code>|<code>off</code></p>
<dd>When set, indicates that the address of interface is sent instead of network prefix, as is required by Mobile IPv6. When set, minimum limits specified by Mobile IPv6 are used for MinRtrAdvInterval and MaxRtrAdvInterval. </p>
<p> Default: off </p>
<dt><code>AdvValidLifetime </code>seconds|<code>infinity</code></p>
<dd>The length of time in seconds (relative to the time the packet is sent) that the prefix is valid for the purpose of on-link determination. The symbolic value <code>infinity</code> represents infinity (i.e. a value of all one bits (0xffffffff)). The valid lifetime is also used by RFC 4862. </p>
<p> Note that clients will ignore AdvValidLifetime of an existing prefix if the lifetime is below two hours, as required in RFC 4862 Section 5.5.3 point e). </p>
<p> Note: RFC4861&#8217;s suggested default value is significantly longer: 30 days. </p>
<p> Default: 86400 seconds (1 day) </p>
<dt><code>AdvPreferredLifetime </code>seconds|<code>infinity</code></p>
<dd>The length of time in seconds (relative to the time the packet is sent) that addresses generated from the prefix via stateless address autoconfiguration remain preferred. The symbolic value <code>infinity</code> represents infinity (i.e. a value of all one bits (0xffffffff)). See RFC 4862. </p>
<p> Note: RFC4861&#8217;s suggested default value is significantly longer: 7 days. </p>
<p> Default: 14400 seconds (4 hours) </p>
<dt><code>DeprecatePrefix</code> <code>on</code>|<code>off</code></p>
<dd>Upon shutdown, this option will cause radvd to deprecate the prefix by announcing it in the radvd shutdown RA with a zero preferred lifetime and a valid lifetime slightly greater than 2 hours. This will encourage end-nodes using this prefix to deprecate any associated addresses immediately. Note that this option should only be used when only one router is announcing the prefix onto the link, otherwise end-nodes will deprecate associated addresses despite the prefix still being valid for preferred use. </p>
<p> See RFC4862, section 5.5.3., &quot;Router Advertisement Processing&quot;, part (e). </p>
<p> Default: off </p>
<dt><code>DecrementLifetimes</code> <code>on</code>|<code>off</code></p>
<dd>This option causes radvd to decrement the values of the preferred and valid lifetimes for the prefix over time. The lifetimes are decremented by the number of seconds since the last RA. If radvd receives a SIGUSR1 signal, it will reset the values of the preferred and valid lifetimes back to the initial values used by radvd when it started. If radvd never receives a SIGUSR1 signal, it will continue to decrement the lifetimes until the preferred lifetime reaches zero. After a final RA with a zero value preferred lifetime, radvd will cease to announce the prefix. If a SIGUSR1 signal then causes the lifetimes to be reset, the prefix will then re-appear in the RAs. </p>
<p> This option is intended to be used in conjunction with a DHCPv6 client that is using the Identity Association for Prefix Delegation (IA_PD) option to acquire a prefix from a Delegating Router for use by a Requesting Router. In this scenario, the prefix(es) from within the delegated prefix that are announced by radvd would age in parallel with and at the same rate as the delegated prefix, and expire at approximately the same time, if the delegated prefix&#8217;s life isn&#8217;t extended. </p>
<p> See RFC3633, &quot;IPv6 Prefix Options for Dynamic Host Configuration Protocol (DHCP) version 6&quot;. </p>
<p> Default: off </p>
<dt><code>Base6Interface </code>name</p>
<dd>If this options is specified, this prefix will be combined with the IPv6 address of the interface specified by <code>name. </code> The resulting prefix length will be 64. </p>
<dt><code>Base6to4Interface </code>name</p>
<dd>If this option is specified, this prefix will be combined with the IPv4 address of interface <code>name</code> to produce a valid 6to4 prefix. The first 16 bits of this prefix will be replaced by <code>2002</code> and the next 32 bits of this prefix will be replaced by the IPv4 address assigned to interface <code>name</code> at configuration time. The remaining 80 bits of the prefix (including the SLA ID) will be advertised as specified in the configuration file. See the next section for an example. </p>
<p> If interface <code>name</code> is not available at configuration time, a warning will be written to the log and this prefix will be disabled until radvd is reconfigured. </p>
<p> This option enables systems with dynamic IPv4 addresses to update their advertised 6to4 prefixes simply by restarting radvd or sending a SIGHUP signal to cause radvd to reconfigure itself. </p>
<p> Note that 6to4 prefixes derived from dynamically-assigned IPv4 addresses should be advertised with a significantly shorter lifetime (see the <code>AdvValidLifetime</code> and <code>AdvPreferredLifetime</code> options). </p>
<p> For more information on 6to4, see RFC 3056. </p>
<p> Default: 6to4 is not used </p>
</dl>
<h2>Route Specific Options</h2>
<dl>
<dt><code>AdvRouteLifetime </code>seconds|<code>infinity</code></p>
<dd>The lifetime associated with the route in units of seconds. The symbolic value <code>infinity</code> represents infinity (i.e. a value of all one bits (0xffffffff)). </p>
<p> Default: 3 * MaxRtrAdvInterval </p>
<dt><code>AdvRoutePreference</code> <code>low</code>|<code>medium</code>|<code>high</code></p>
<dd>The preference associated with the default router, as either &quot;low&quot;, &quot;medium&quot;, or &quot;high&quot;. </p>
<p> Default: medium </p>
<dt><code>RemoveRoute</code> <code>on</code>|<code>off</code></p>
<dd>Upon shutdown, announce this route with a zero second lifetime. This should cause the route to be immediately removed from the receiving end-nodes&#8217; route table. </p>
<p> Default: on </p>
</dl>
<h2>Rdnss Specific Options</h2>
<dl>
<dt><code>AdvRDNSSLifetime </code>seconds<code>|</code>infinity</p>
<dd>The maximum duration how long the RDNSS entries are used for name resolution. A value of 0 means the nameserver must no longer be used. The value, if not 0, must be at least MaxRtrAdvInterval. To ensure stale RDNSS info gets removed in a timely fashion, this should not be greater than 2*MaxRtrAdvInterval. </p>
<p> Default: 2*MaxRtrAdvInterval </p>
<dt><code>FlushRDNSS</code> <code>on</code>|<code>off</code></p>
<dd>Upon shutdown, announce the RDNSS entries with a zero second lifetime. This should cause the RDNSS addresses to be immediately removed from the end-nodes&#8217; list of Recursive DNS Servers. </p>
<p> Default: on </p>
</dl>
<h2>Dnssl Specific Options</h2>
<dl>
<dt><code>AdvDNSSLLifetime </code>seconds<code>|</code>infinity;</p>
<dd>The maximum duration how long the DNSSL entries are used for name resolution. A value of 0 means the suffix should no longer be used. The value, if not 0, must be at least MaxRtrAdvInterval. To ensure stale DNSSL info gets removed in a timely fashion, this should not be greater than 2*MaxRtrAdvInterval. </p>
<p> Default: 2*MaxRtrAdvInterval </p>
<dt><code>FlushDNSSL</code> <code>on</code>|<code>off</code></p>
<dd>Upon shutdown, announce the DNSSL entries with a zero second lifetime. This should cause the DNSSL entries to be immediately removed from the end-nodes&#8217; DNS search list. </p>
<p> Default: on </p>
</dl>
<h2>Abro Specific Options</h2>
<dl>
<dt><code>AdvValidLifeTime </code>seconds</p>
<dd>The time in units of that the set of border router information is valid. A value of all zero bits assumes a default value of 10,000(~one week). </p>
<dt><code>AdvVersionLow, AdvVersionHigh </code>unsigned<code>integer</code></p>
<dd>Both forms 32-bit unsigned version number corresponding to the set of information contained in RA message. </p>
</dl>
<h2>Examples</h2>
<pre>interface eth0
{
 AdvSendAdvert on;
 prefix 2001:db8:0:1::/64
 {
 AdvOnLink on;
 AdvAutonomous on;
 };
};</pre>
<p>It says that router advertisement daemon should advertise (AdvSendAdvert on;) the prefix 2001:db8:0:1:: which has a length of 64 on the interface eth0. Also the prefix should be marked as autonomous (AdvAutonomous on;) and as on-link (AdvOnLink on;). All the other options are left on their default values. </p>
<p> To support movement detection of Mobile IPv6 Mobile Nodes, the address of interface should be used instead of network prefix: </p>
<pre>interface eth0
{
 AdvSendAdvert on;
 prefix 2001:db8:0:1::4/64
 {
 AdvOnLink on;
 AdvAutonomous on;
 AdvRouterAddr on;
 };
};</pre>
<p>For 6to4 support, include the <code>Base6to4Interface</code> option in each prefix section. When using a dynamic IPv4 address, set small prefix lifetimes to prevent hosts from retaining unreachable prefixes after a new IPv4 address has been assigned. When advertising to on a dynamic interface (e.g., Bluetooth), skip the interface if it is not active yet. </p>
<pre>interface bnep0
{
 IgnoreIfMissing on;
 AdvSendAdvert on;
 # Advertise at least every 30 seconds
 MaxRtrAdvInterval 30;
 prefix 0:0:0:5678::/64
 {
 AdvOnLink on;
 AdvAutonomous on;
 Base6to4Interface ppp0;
 # Very short lifetimes for dynamic addresses
 AdvValidLifetime 300;
 AdvPreferredLifetime 120;
 };
};</pre>
<p>Since 6to4 is enabled, the prefix will be advertised as 2002:WWXX:YYZZ:5678::/64, where WW.XX.YY.ZZ is the IPv4 address of ppp0 at configuration time. (IPv6 addresses are written in hexadecimal whereas IPv4 addresses are written in decimal, so the IPv4 address WW.XX.YY.ZZ in the 6to4 prefix will be represented in hex.) </p>
<p> In this specific case, the configuration scripts may send HUP signal to radvd when taking bnep0 up or down to notify about the status; in the current radvd releases, sending HUP is no longer mandatory when the link comes back up. </p>
<pre>interface eth0
{
 AdvSendAdvert on;
 prefix 2001:db8:0:1::/64
 {
 AdvOnLink on;
 AdvAutonomous on;
 };
 clients
 {
 fe80::21f:16ff:fe06:3aab;
 fe80::21d:72ff:fe96:aaff;
 };
};</pre>
<p>This configuration would only announce the prefix to fe80::21f:16ff:fe06:3aab and fe80::21d:72ff:fe96:aaff. Furthermore, all RA requests of other clients are denied. </p>
<p> This may come in handy if you want to roll out IPv6 only partially because some clients are broken or untested. </p>
<p> For ABRO support </p>
<pre>interface lowpan0
{
 AdvSendAdvert on;
 UnicastOnly on;
 AdvCurHopLimit 255;
 prefix 2001:0db8:0100:f101::/64 {
 AdvOnLink on;
 AdvAutonomous on;
 AdvRouterAddr on;
 };
 abro fe80::a200:0:0:1/64 {
 AdvVersionLow 10;
 AdvVersionHigh 2;
 AdvValidLifeTime 2;
 };
};</pre>
<h2>Files</h2>
<pre>/usr/sbin/radvd
/etc/radvd.conf
/var/run/radvd/radvd.pid
/var/log/radvd.log</pre>
<h2>Credit</h2>
<p>The description of the different flags and variables is in large parts taken from RFC 4861.</p>
<h2>Rfcs</h2>
<p>Narten, T., Nordmark, E., Simpson, W., and H. Soliman, &quot;Neighbor Discovery for IP Version 6 (IPv6)&quot;, RFC 4861, September 2007. </p>
<p> Thomson, S., Narten, T., T. Jinmei, &quot;IPv6 Stateless Address Autoconfiguration&quot;, RFC 4862, September 2007. </p>
<p> Deering, S., and R. Hinden, &quot;IP Version 6 Addressing Architecture&quot;, RFC 4291, February 2006. </p>
<p> Conta, A., Deering, S., and M. Gupta &quot;Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6)&quot;, RFC 4443, March 2006. </p>
<p> Crawford, M., &quot;Transmission of IPv6 Packets over Ethernet Networks&quot;, RFC 2464, December 1998.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p> Carpenter B., K. Moore, &quot;Connection of IPv6 Domains via IPv4 Clouds&quot;, RFC 3056, February 2001. (6to4 specification) </p>
<p> Draves, R., D. Thaler, &quot;Default Router Preferences and More-Specific Routes&quot;, RFC 4191, November 2005. </p>
<p> Johnson, D., Perkins, C., and J. Arkko, &quot;Mobility Support in IPv6&quot;, RFC 3775, June 2004. </p>
<p> Devarapalli, V., Wakikawa, R., Petrescu, A., and P. Thubert &quot;Network Mobility (NEMO) Basic Support Protocol&quot;, RFC 3963, January 2005. </p>
<p> J. Jeong, S. Park, L. Beloeil, and S. Madanapalli, &quot;IPv6 Router Advertisement Options for DNS Configuration&quot;, RFC 6106, November 2010. </p>
<p> Z. Shelby, S. Chakrabarti, E. Nordmark and C. Bormann &quot; Neighbor Discovery Optimization for IPv6 over Low-Power Wireless Personal Area Networks (6LoWPANs)&quot;, RFC 6775, November 2012.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radvd/">radvd</a></code>(8), <code><a href="/docs/linux/man/8-radvdump/">radvdump</a></code>(8) </p>
<h2>Bugs</h2>
<p>radvd does not support splitting up RAs to multiple packets (RFC4861 6.2.3 last paragraph). In practise this limits advertising to ~45 prefixes on a link, but there is no reason to be able to so. </p>
