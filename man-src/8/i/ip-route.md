---
title: "ip-route(8)"
name: "ip-route"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-route/"
description: "ip-route – routing table management"
---

<p>ip-route &#8211; routing table management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ ip-OPTIONS ]

route

{ COMMAND |

    help }
</code></pre>
<p> <code>ip route</code> { <code>show</code> | <code>flush</code> } <i>SELECTOR</i><br />
 <code>ip route save</code> <i>SELECTOR</i><br />
 <code>ip route restore</code><br />
 <code>ip route get</code> <i>ROUTE_GET_FLAGS</i> <i>ADDRESS</i> [ <code>from</code><i> ADDRESS </i><code>iif</code><i> STRING</i> ] [ <code>oif</code> <i>STRING</i> ] [ <code>mark</code> <i>MARK</i> ] [ <code>tos</code> <i>TOS</i> ] [ <code>vrf</code> <i>NAME</i> ] [ <code>ipproto</code> <i>PROTOCOL</i> ] [ <code>sport</code> <i>NUMBER</i> ] [ <code>dport</code> <i>NUMBER</i> ]<br />
 <code>ip route</code> { <code>add</code> | <code>del</code> | <code>change</code> | <code>append</code> | replace<code> } </code> <i>ROUTE</i> </p>
<pre><code>SELECTOR :=

[ root

PREFIX ] [

match

PREFIX ] [

exact

PREFIX ] [

table

TABLE_ID ] [

vrf

NAME ] [

proto

RTPROTO ] [

type

TYPE ] [

scope

SCOPE ]
ROUTE := NODE_SPEC [ INFO_SPEC ]
NODE_SPEC := [ TYPE ] PREFIX [

tos

TOS ] [

table

TABLE_ID ] [

proto

RTPROTO ] [

scope

SCOPE ] [

metric

METRIC ] [

ttl-propagate

{ enabled | disabled } ]
INFO_SPEC := { NH |

    nhid

    ID } OPTIONS FLAGS [

nexthop

NH ] ...
NH := [

encap

ENCAP ] [

via

[
FAMILY ] ADDRESS ] [

dev

STRING ] [

weight

NUMBER ] NHFLAGS
FAMILY := [

inet | inet6 | mpls | bridge | link ]
OPTIONS := FLAGS [

mtu

NUMBER ] [

advmss

NUMBER ] [

as

[
to

]
ADDRESS ]

rtt

TIME ] [

rttvar

TIME ] [

reordering

NUMBER ] [

window

NUMBER ] [

cwnd

NUMBER ] [

ssthresh

NUMBER ] [

realms

REALM ] [

rto_min

TIME ] [

initcwnd

NUMBER ] [

initrwnd

NUMBER ] [

features

FEATURES ] [

quickack

BOOL ] [

congctl

NAME ] [

pref

PREF ] [

expires

TIME ] [

fastopen_no_cookie

BOOL ]
TYPE := [

unicast | local | broadcast | multicast | throw | unreachable | prohibit | blackhole | nat ]
TABLE_ID := [

local| main | default | all |

NUMBER ]
SCOPE := [

host | link | global |

NUMBER ]
NHFLAGS := [

onlink | pervasive ]
RTPROTO := [

kernel | boot | static |

NUMBER ]
FEATURES := [

ecn | ]
PREF := [

low | medium | high ]
ENCAP := [

ENCAP_MPLS | ENCAP_IP | ENCAP_BPF |

ENCAP_SEG6 | ENCAP_SEG6LOCAL | ENCAP_IOAM6 ]
ENCAP_MPLS :=

mpls [

LABEL ] [

ttl

TTL ]
ENCAP_IP :=

ip

id

TUNNEL_ID

dst

REMOTE_IP [

src

SRC ] [

tos

TOS ] [

ttl

TTL ]
ENCAP_BPF :=

bpf [

in

PROG ] [

out

PROG ] [

xmit

PROG ] [

headroom

SIZE ]
ENCAP_SEG6 :=

seg6

mode [

encap | inline | l2encap ]

segs

SEGMENTS [

hmac

KEYID ]
ENCAP_SEG6LOCAL :=

seg6local

action

SEG6_ACTION [

SEG6_ACTION_PARAM ] [

count ]
ENCAP_IOAM6 :=

ioam6

trace

prealloc

type

IOAM6_TRACE_TYPE

ns

IOAM6_NAMESPACE

size

IOAM6_TRACE_SIZE
ROUTE_GET_FLAGS :=

[

fibmatch

]
</code></pre>
<h2>Description</h2>
<p><code>ip route</code> is used to manipulate entries in the kernel routing tables. <code>Route types:</code> <code>unicast</code> &#8211; the route entry describes real paths to the destinations covered by the route prefix. <code>unreachable</code> &#8211; these destinations are unreachable. Packets are discarded and the ICMP message <i>host unreachable</i> is generated. The local senders get an <i>EHOSTUNREACH</i> error. <code>blackhole</code> &#8211; these destinations are unreachable. Packets are discarded silently. The local senders get an <i>EINVAL</i> error. <code>prohibit</code> &#8211; these destinations are unreachable. Packets are discarded and the ICMP message <i>communication administratively prohibited</i> is generated. The local senders get an <i>EACCES</i> error. <code>local</code> &#8211; the destinations are assigned to this host. The packets are looped back and delivered locally. <code>broadcast</code> &#8211; the destinations are broadcast addresses. The packets are sent as link broadcasts. <code>throw</code> &#8211; a special control route used together with policy rules. If such a route is selected, lookup in this table is terminated pretending that no route was found. Without policy routing it is equivalent to the absence of the route in the routing table. The packets are dropped and the ICMP message <i>net unreachable</i> is generated. The local senders get an <i>ENETUNREACH</i> error. <code>nat</code> &#8211; a special NAT route. Destinations covered by the prefix are considered to be dummy (or external) addresses which require translation to real (or internal) ones before forwarding. The addresses to translate to are selected with the attribute <code>via</code>. <code>Warning:</code> Route NAT is no longer supported in Linux 2.6. <code>anycast</code> &#8211; <i>not implemented</i> the destinations are <i>anycast</i> addresses assigned to this host. They are mainly equivalent to <code>local</code> with one difference: such addresses are invalid when used as the source address of any packet. <code>multicast</code> &#8211; a special type used for multicast routing. It is not present in normal routing tables. <code>Route tables:</code> Linux-2.x can pack routes into several routing tables identified by a number in the range from 1 to 2^32-1 or by name from the file <code>/etc/iproute2/rt_tables</code> By default all normal routes are inserted into the <code>main</code> table (ID 254) and the kernel only uses this table when calculating routes. Values (0, 253, 254, and 255) are reserved for built-in use. Actually, one other table always exists, which is invisible but even more important. It is the <code>local</code> table (ID 255). This table consists of routes for local and broadcast addresses. The kernel maintains this table automatically and the administrator usually need not modify it or even look at it. The multiple routing tables enter the game when <i>policy routing</i> is used.</p>
<dl>
<dt>ip route add</p>
<dd>add new route</p>
<dt>ip route change</p>
<dd>change route</p>
<dt>ip route replace</p>
<dd>change or add new one</p>
<dl>
<dd>
<dl>
<dt><code>to</code><i> TYPE PREFIX </i><code>(default)</code></p>
<dd>the destination prefix of the route. If <i>TYPE</i> is omitted, <code>ip</code> assumes type <code>unicast</code>. Other values of <i>TYPE</i> are listed above. <i>PREFIX</i> is an IP or IPv6 address optionally followed by a slash and the prefix length. If the length of the prefix is missing, <code>ip</code> assumes a full-length host route. There is also a special <i>PREFIX</i> <code>default</code> &#8211; which is equivalent to IP <code>0/0</code> or to IPv6 <code>::/0</code>.</p>
<dt><code>tos</code><i> TOS</i></p>
<dd>
<dt><code>dsfield</code><i> TOS</i></p>
<dd>the Type Of Service (TOS) key. This key has no associated mask and the longest match is understood as: First, compare the TOS of the route and of the packet. If they are not equal, then the packet may still match a route with a zero TOS. <i>TOS</i> is either an 8 bit hexadecimal number or an identifier from <code>/etc/iproute2/rt_dsfield</code>.</p>
<dt><code>metric</code><i> NUMBER</i></p>
<dd>
<dt><code>preference</code><i> NUMBER</i></p>
<dd>the preference value of the route. <i>NUMBER</i> is an arbitrary 32bit number, where routes with lower values are preferred.</p>
<dt><code>table</code><i> TABLEID</i></p>
<dd>the table to add this route to. <i>TABLEID</i> may be a number or a string from the file <code>/etc/iproute2/rt_tables</code>. If this parameter is omitted, <code>ip</code> assumes the <code>main</code> table, with the exception of <code>local</code>, <code>broadcast</code> and <code>nat</code> routes, which are put into the <code>local</code> table by default.</p>
<dt><code>vrf</code><i> NAME</i></p>
<dd>the vrf name to add this route to. Implicitly means the table associated with the VRF.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>the output device name.</p>
<dt><code>via</code><i> [ FAMILY ] ADDRESS</i></p>
<dd>the address of the nexthop router, in the address family FAMILY. Actually, the sense of this field depends on the route type. For normal <code>unicast</code> routes it is either the true next hop router or, if it is a direct route installed in BSD compatibility mode, it can be a local address of the interface. For NAT routes it is the first address of the block of translated IP destinations.</p>
<dt><code>src</code><i> ADDRESS</i></p>
<dd>the source address to prefer when sending to the destinations covered by the route prefix.</p>
<dt><code>realm</code><i> REALMID</i></p>
<dd>the realm to which this route is assigned. <i>REALMID</i> may be a number or a string from the file <code>/etc/iproute2/rt_realms</code>.</p>
<dt><code>mtu</code><i> MTU</i></p>
<dd>
<dt><code>mtu lock</code><i> MTU</i></p>
<dd>the MTU along the path to the destination. If the modifier <code>lock</code> is not used, the MTU may be updated by the kernel due to Path MTU Discovery. If the modifier <code>lock</code> is used, no path MTU discovery will be tried, all packets will be sent without the DF bit in IPv4 case or fragmented to MTU for IPv6.</p>
<dt><code>window</code><i> NUMBER</i></p>
<dd>the maximal window for TCP to advertise to these destinations, measured in bytes. It limits maximal data bursts that our TCP peers are allowed to send to us.</p>
<dt><code>rtt</code><i> TIME</i></p>
<dd>the initial RTT (&#8216;Round Trip Time&#8217;) estimate. If no suffix is specified the units are raw values passed directly to the routing code to maintain compatibility with previous releases. Otherwise if a suffix of s, sec or secs is used to specify seconds and ms, msec or msecs to specify milliseconds.</p>
<dt><code>rttvar</code><i> TIME </i><code>(Linux 2.3.15+ only)</code></p>
<dd>the initial RTT variance estimate. Values are specified as with <code>rtt</code> above.</p>
<dt><code>rto_min</code><i> TIME </i><code>(Linux 2.6.23+ only)</code></p>
<dd>the minimum TCP Retransmission TimeOut to use when communicating with this destination. Values are specified as with <code>rtt</code> above.</p>
<dt><code>ssthresh</code><i> NUMBER </i><code>(Linux 2.3.15+ only)</code></p>
<dd>an estimate for the initial slow start threshold.</p>
<dt><code>cwnd</code><i> NUMBER </i><code>(Linux 2.3.15+ only)</code></p>
<dd>the clamp for congestion window. It is ignored if the <code>lock</code> flag is not used.</p>
<dt><code>initcwnd</code><i> NUMBER </i><code>(Linux 2.5.70+ only)</code></p>
<dd>the initial congestion window size for connections to this destination. Actual window size is this value multiplied by the MSS (&#8220;Maximal Segment Size&#8221;) for same connection. The default is zero, meaning to use the values specified in RFC2414.</p>
<dt><code>initrwnd</code><i> NUMBER </i><code>(Linux 2.6.33+ only)</code></p>
<dd>the initial receive window size for connections to this destination. Actual window size is this value multiplied by the MSS of the connection. The default value is zero, meaning to use Slow Start value.</p>
<dt><code>features</code><i> FEATURES </i><code>(Linux</code><i>3.18+</i><code>only)</code></p>
<dd>Enable or disable per-route features. Only available feature at this time is <code>ecn</code> to enable explicit congestion notification when initiating connections to the given destination network. When responding to a connection request from the given network, ecn will also be used even if the <code>net.ipv4.tcp_ecn</code> sysctl is set to 0.</p>
<dt><code>quickack</code><i> BOOL </i><code>(Linux 3.11+ only)</code></p>
<dd>Enable or disable quick ack for connections to this destination.</p>
<dt><code>fastopen_no_cookie</code><i> BOOL </i><code>(Linux 4.15+ only)</code></p>
<dd>Enable TCP Fastopen without a cookie for connections to this destination.</p>
<dt><code>congctl</code><i> NAME </i><code>(Linux 3.20+ only)</code></p>
<dd>
<dt><code>congctl lock</code><i> NAME </i><code>(Linux 3.20+ only)</code></p>
<dd>Sets a specific TCP congestion control algorithm only for a given destination. If not specified, Linux keeps the current global default TCP congestion control algorithm, or the one set from the application. If the modifier <code>lock</code> is not used, an application may nevertheless overwrite the suggested congestion control algorithm for that destination. If the modifier <code>lock</code> is used, then an application is not allowed to overwrite the specified congestion control algorithm for that destination, thus it will be enforced/guaranteed to use the proposed algorithm.</p>
<dt><code>advmss</code><i> NUMBER </i><code>(Linux 2.3.15+ only)</code></p>
<dd>the MSS (&#8216;Maximal Segment Size&#8217;) to advertise to these destinations when establishing TCP connections. If it is not given, Linux uses a default value calculated from the first hop device MTU. (If the path to these destination is asymmetric, this guess may be wrong.)</p>
<dt><code>reordering</code><i> NUMBER </i><code>(Linux 2.3.15+ only)</code></p>
<dd>Maximal reordering on the path to this destination. If it is not given, Linux uses the value selected with <code>sysctl</code> variable <code>net/ipv4/tcp_reordering</code>.</p>
<dt><code>nexthop</code><i> NEXTHOP</i></p>
<dd>the nexthop of a multipath route. <i>NEXTHOP</i> is a complex value with its own syntax similar to the top level argument lists: <code>via</code><i> [ FAMILY ] ADDRESS</i> &#8211; is the nexthop router. <code>dev</code><i> NAME</i> &#8211; is the output device. <code>weight</code><i> NUMBER</i> &#8211; is a weight for this element of a multipath route reflecting its relative bandwidth or quality. The internal buffer used in iproute2 limits the maximum number of nexthops that may be specified in one go. If only <i>ADDRESS</i> is given, the current buffer size allows for 144 IPv6 nexthops and 253 IPv4 ones. For IPv4, this effectively limits the number of nexthops possible per route. With IPv6, further nexthops may be appended to the same route via <code>ip route append</code> command.</p>
<dt><code>scope</code><i> SCOPE_VAL</i></p>
<dd>the scope of the destinations covered by the route prefix. <i>SCOPE_VAL</i> may be a number or a string from the file <code>/etc/iproute2/rt_scopes</code>. If this parameter is omitted, <code>ip</code> assumes scope <code>global</code> for all gatewayed <code>unicast</code> routes, scope <code>link</code> for direct <code>unicast</code> and <code>broadcast</code> routes and scope <code>host</code> for <code>local</code> routes.</p>
<dt><code>protocol</code><i> RTPROTO</i></p>
<dd>the routing protocol identifier of this route. <i>RTPROTO</i> may be a number or a string from the file <code>/etc/iproute2/rt_protos</code>. If the routing protocol ID is not given, <code>ip assumes protocol</code> <code>boot</code> (i.e. it assumes the route was added by someone who doesn&#8217;t understand what they are doing). Several protocol values have a fixed interpretation. Namely: <code>redirect</code> &#8211; the route was installed due to an ICMP redirect. <code>kernel</code> &#8211; the route was installed by the kernel during autoconfiguration. <code>boot</code> &#8211; the route was installed during the bootup sequence. If a routing daemon starts, it will purge all of them. <code>static</code> &#8211; the route was installed by the administrator to override dynamic routing. Routing daemon will respect them and, probably, even advertise them to its peers. <code>ra</code> &#8211; the route was installed by Router Discovery protocol. The rest of the values are not reserved and the administrator is free to assign (or not to assign) protocol tags.</p>
<dt><code>onlink</code></p>
<dd>pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.</p>
<dt><code>pref</code><i> PREF</i></p>
<dd>the IPv6 route preference. <i>PREF</i> is a string specifying the route preference as defined in RFC4191 for Router Discovery messages. Namely: <code>low</code> &#8211; the route has a lowest priority <code>medium</code> &#8211; the route has a default priority <code>high</code> &#8211; the route has a highest priority</p>
<dt><code>nhid</code><i> ID</i></p>
<dd>use nexthop object with given id as nexthop specification.</p>
<dt><code>encap</code><i> ENCAPTYPE ENCAPHDR</i></p>
<dd>attach tunnel encapsulation attributes to this route. <i>ENCAPTYPE</i> is a string specifying the supported encapsulation type. Namely: <code>mpls</code> &#8211; encapsulation type MPLS <code>ip</code> &#8211; IP encapsulation (Geneve, GRE, VXLAN, &#8230;) <code>bpf</code> &#8211; Execution of BPF program <code>seg6</code> &#8211; encapsulation type IPv6 Segment Routing <code>seg6local</code> &#8211; local SRv6 segment processing <code>ioam6</code> &#8211; encapsulation type IPv6 IOAM <i>ENCAPHDR</i> is a set of encapsulation attributes specific to the <i>ENCAPTYPE.</i> <code>mpls</code> <i>MPLSLABEL</i> &#8211; mpls label stack with labels separated by <i>/</i> <code>ttl</code> <i>TTL</i> &#8211; TTL to use for MPLS header or 0 to inherit from IP header <code>ip</code> <code>id</code> <i>TUNNEL_ID</i> <code>dst</code> <i>REMOTE_IP</i> [ <code>src</code> <i>SRC</i> ] [ <code>tos</code> <i>TOS</i> ] [ <code>ttl</code> <i>TTL</i> ] [ <code>key</code> ] [ <code>csum</code> ] [ <code>seq</code> ] <code>bpf</code> <code>in</code> <i>PROG</i> &#8211; BPF program to execute for incoming packets <code>out</code> <i>PROG</i> &#8211; BPF program to execute for outgoing packets <code>xmit</code> <i>PROG</i> &#8211; BPF program to execute for transmitted packets <code>headroom</code> <i>SIZE</i> &#8211; Size of header BPF program will attach (xmit) <code>seg6</code> <code>mode inline</code> &#8211; Directly insert Segment Routing Header after IPv6 header <code>mode encap</code> &#8211; Encapsulate packet in an outer IPv6 header with SRH <code>mode l2encap</code> &#8211; Encapsulate ingress L2 frame within an outer IPv6 header and SRH <i>SEGMENTS</i> &#8211; List of comma-separated IPv6 addresses <i>KEYID</i> &#8211; Numerical value in decimal representation. See <code><a href="/docs/linux/man/8-ip-sr/">ip-sr</a></code>(8). <code>seg6local</code> <i>SEG6_ACTION</i> [ <i>SEG6_ACTION_PARAM</i> ] [ <code>count</code> ] &#8211; Operation to perform on matching packets. The optional <code>count</code> attribute is used to collect statistics on the processing of actions. Three counters are implemented: 1) packets correctly processed; 2) bytes correctly processed; 3) packets that cause a processing error (i.e., missing SID List, wrong SID List, etc). To retrieve the counters related to an action use the <code>-s</code> flag in the <code>show</code> command. The following actions are currently supported (<code>Linux 4.14+ only</code>). <code>End</code> &#8211; Regular SRv6 processing as intermediate segment endpoint. This action only accepts packets with a non-zero Segments Left value. Other matching packets are dropped. <code>End.X nh6</code> <i>NEXTHOP</i> &#8211; Regular SRv6 processing as intermediate segment endpoint. Additionally, forward processed packets to given next-hop. This action only accepts packets with a non-zero Segments Left value. Other matching packets are dropped. <code>End.DX6 nh6</code> <i>NEXTHOP</i> &#8211; Decapsulate inner IPv6 packet and forward it to the specified next-hop. If the argument is set to ::, then the next-hop is selected according to the local selection rules. This action only accepts packets with either a zero Segments Left value or no SRH at all, and an inner IPv6 packet. Other matching packets are dropped. <code>End.DT6</code> { <code>table</code> | <code>vrftable</code> } <i>TABLEID</i> &#8211; Decapsulate the inner IPv6 packet and forward it according to the specified lookup table. <i>TABLEID</i> is either a number or a string from the file <code>/etc/iproute2/rt_tables</code>. If <code>vrftable</code> is used, the argument must be a VRF device associated with the table id. Moreover, the VRF table associated with the table id must be configured with the VRF strict mode turned on (net.vrf.strict_mode=1). This action only accepts packets with either a zero Segments Left value or no SRH at all, and an inner IPv6 packet. Other matching packets are dropped. <code>End.DT4 vrftable</code> <i>TABLEID</i> &#8211; Decapsulate the inner IPv4 packet and forward it according to the specified lookup table. <i>TABLEID</i> is either a number or a string from the file <code>/etc/iproute2/rt_tables</code>. The argument must be a VRF device associated with the table id. Moreover, the VRF table associated with the table id must be configured with the VRF strict mode turned on (net.vrf.strict_mode=1). This action only accepts packets with either a zero Segments Left value or no SRH at all, and an inner IPv4 packet. Other matching packets are dropped. <code>End.DT46 vrftable</code> <i>TABLEID</i> &#8211; Decapsulate the inner IPv4 or IPv6 packet and forward it according to the specified lookup table. <i>TABLEID</i> is either a number or a string from the file <code>/etc/iproute2/rt_tables</code>. The argument must be a VRF device associated with the table id. Moreover, the VRF table associated with the table id must be configured with the VRF strict mode turned on (net.vrf.strict_mode=1). This action only accepts packets with either a zero Segments Left value or no SRH at all, and an inner IPv4 or IPv6 packet. Other matching packets are dropped. <code>End.B6 srh segs</code> <i>SEGMENTS</i> [ <code>hmac</code> <i>KEYID</i> ] &#8211; Insert the specified SRH immediately after the IPv6 header, update the DA with the first segment of the newly inserted SRH, then forward the resulting packet. The original SRH is not modified. This action only accepts packets with a non-zero Segments Left value. Other matching packets are dropped. <code>End.B6.Encaps srh segs</code> <i>SEGMENTS</i> [ <code>hmac</code> <i>KEYID</i> ] &#8211; Regular SRv6 processing as intermediate segment endpoint. Additionally, encapsulate the matching packet within an outer IPv6 header followed by the specified SRH. The destination address of the outer IPv6 header is set to the first segment of the new SRH. The source address is set as described in <code><a href="/docs/linux/man/8-ip-sr/">ip-sr</a></code>(8). <code>ioam6</code> <i>IOAM6_TRACE_TYPE</i> &#8211; List of IOAM data required in the trace, represented by a bitfield (24 bits). <i>IOAM6_NAMESPACE</i> &#8211; Numerical value to represent an IOAM namespace. See <code><a href="/docs/linux/man/8-ip-ioam/">ip-ioam</a></code>(8). <i>IOAM6_TRACE_SIZE</i> &#8211; Size, in octets, of the pre-allocated trace data block.</p>
<dt><code>expires</code><i> TIME </i><code>(Linux 4.4+ only)</code></p>
<dd>the route will be deleted after the expires time. <code>Only</code> support IPv6 at present.</p>
<dt><code>ttl-propagate</code> { <code>enabled</code> | <code>disabled</code> }</p>
<dd>Control whether TTL should be propagated from any encap into the un-encapsulated packet, overriding any global configuration. Only supported for MPLS at present.</dl>
</dl>
<dt>ip route delete</p>
<dd>delete route</p>
<dl>
<dd><code>ip route del</code> has the same arguments as <code>ip route add</code>, but their semantics are a bit different. Key values (<code>to</code>, <code>tos</code>, <code>preference</code> and <code>table</code>) select the route to delete. If optional attributes are present, <code>ip</code> verifies that they coincide with the attributes of the route to delete. If no route with the given key and attributes was found, <code>ip route del</code> fails.</dl>
<dt>ip route show</p>
<dd>list routes</p>
<dl>
<dd>the command displays the contents of the routing tables or the route(s) selected by some criteria.</p>
<dl>
<dt><code>to</code><i> SELECTOR </i><code>(default)</code></p>
<dd>only select routes from the given range of destinations. <i>SELECTOR</i> consists of an optional modifier (<code>root</code>, <code>match</code> or <code>exact</code>) and a prefix. <code>root</code><i> PREFIX</i> selects routes with prefixes not shorter than <i>PREFIX</i>. F.e. <code>root</code><i> 0/0</i> selects the entire routing table. <code>match</code><i> PREFIX</i> selects routes with prefixes not longer than <i>PREFIX</i>. F.e. <code>match</code><i> 10.0/16</i> selects <i>10.0/16</i>, <i>10/8</i> and <i>0/0</i>, but it does not select <i>10.1/16</i> and <i>10.0.0/24</i>. And <code>exact</code><i> PREFIX</i> (or just <i>PREFIX</i>) selects routes with this exact prefix. If neither of these options are present, <code>ip</code> assumes <code>root</code><i> 0/0</i> i.e. it lists the entire table.</p>
<dt><code>tos</code><i> TOS</i></p>
<dd>
<dt><code>dsfield</code><i> TOS</i></p>
<dd>only select routes with the given TOS.</p>
<dt><code>table</code><i> TABLEID</i></p>
<dd>show the routes from this table(s). The default setting is to show table <code>main</code>. <i>TABLEID</i> may either be the ID of a real table or one of the special values: <code>all</code> &#8211; list all of the tables. <code>cache</code> &#8211; dump the routing cache.</p>
<dt><code>vrf</code><i> NAME</i></p>
<dd>show the routes for the table associated with the vrf name</p>
<dt><code>cloned</code></p>
<dd>
<dt><code>cached</code></p>
<dd>list cloned routes i.e. routes which were dynamically forked from other routes because some route attribute (f.e. MTU) was updated. Actually, it is equivalent to <code>table cache</code>.</p>
<dt><code>from</code><i> SELECTOR</i></p>
<dd>the same syntax as for <code>to</code>, but it binds the source address range rather than destinations. Note that the <code>from</code> option only works with cloned routes.</p>
<dt><code>protocol</code><i> RTPROTO</i></p>
<dd>only list routes of this protocol.</p>
<dt><code>scope</code><i> SCOPE_VAL</i></p>
<dd>only list routes with this scope.</p>
<dt><code>type</code><i> TYPE</i></p>
<dd>only list routes of this type.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>only list routes going via this device.</p>
<dt><code>via</code><i> [ FAMILY ] PREFIX</i></p>
<dd>only list routes going via the nexthop routers selected by <i>PREFIX</i>.</p>
<dt><code>src</code><i> PREFIX</i></p>
<dd>only list routes with preferred source addresses selected by <i>PREFIX</i>.</p>
<dt><code>realm</code><i> REALMID</i></p>
<dd>
<dt><code>realms</code><i> FROMREALM/TOREALM</i></p>
<dd>only list routes with these realms.</dl>
</dl>
<dt>ip route flush</p>
<dd>flush routing tables</p>
<dl>
<dd>this command flushes routes selected by some criteria. The arguments have the same syntax and semantics as the arguments of <code>ip route show</code>, but routing tables are not listed but purged. The only difference is the default action: <code>show</code> dumps all the IP main routing table but <code>flush</code> prints the helper page. With the <code>-statistics</code> option, the command becomes verbose. It prints out the number of deleted routes and the number of rounds made to flush the routing table. If the option is given twice, <code>ip route flush</code> also dumps all the deleted routes in the format described in the previous subsection.</dl>
<dt>ip route get</p>
<dd>get a single route</p>
<dl>
<dd>this command gets a single route to a destination and prints its contents exactly as the kernel sees it.</p>
<dl>
<dt><code>fibmatch</code></p>
<dd>Return full fib lookup matched route. Default is to return the resolved dst entry</p>
<dt><code>to</code><i> ADDRESS </i><code>(default)</code></p>
<dd>the destination address.</p>
<dt><code>from</code><i> ADDRESS</i></p>
<dd>the source address.</p>
<dt><code>tos</code><i> TOS</i></p>
<dd>
<dt><code>dsfield</code><i> TOS</i></p>
<dd>the Type Of Service.</p>
<dt><code>iif</code><i> NAME</i></p>
<dd>the device from which this packet is expected to arrive.</p>
<dt><code>oif</code><i> NAME</i></p>
<dd>force the output device on which this packet will be routed.</p>
<dt><code>mark</code><i> MARK</i></p>
<dd>the firewall mark (<code>fwmark</code>)</p>
<dt><code>vrf</code><i> NAME</i></p>
<dd>force the vrf device on which this packet will be routed.</p>
<dt><code>ipproto</code><i> PROTOCOL</i></p>
<dd>ip protocol as seen by the route lookup</p>
<dt><code>sport</code><i> NUMBER</i></p>
<dd>source port as seen by the route lookup</p>
<dt><code>dport</code><i> NUMBER</i></p>
<dd>destination port as seen by the route lookup</p>
<dt><code>connected</code></p>
<dd>if no source address (option <code>from</code>) was given, relookup the route with the source set to the preferred address received from the first lookup. If policy routing is used, it may be a different route.  Note that this operation is not equivalent to <code>ip route show</code>. <code>show</code> shows existing routes. <code>get</code> resolves them and creates new clones if necessary. Essentially, <code>get</code> is equivalent to sending a packet along this path. If the <code>iif</code> argument is not given, the kernel creates a route to output packets towards the requested destination. This is equivalent to pinging the destination with a subsequent <code>ip route ls cache</code>, however, no packets are actually sent. With the <code>iif</code> argument, the kernel pretends that a packet arrived from this interface and searches for a path to forward the packet.</dl>
<dt>ip route save</p>
<dd>save routing table information to stdout</p>
<dl>
<dd>This command behaves like <code>ip route show</code> except that the output is raw data suitable for passing to <code>ip route restore</code>.</dl>
<dt>ip route restore</p>
<dd>restore routing table information from stdin</p>
<dl>
<dd>This command expects to read a data stream as returned from <code>ip route save</code>. It will attempt to restore the routing table information exactly as it was at the time of the save, so any translation of information in the stream (such as device indexes) must be done first. Any existing routes are left unchanged. Any routes specified in the data stream that already exist in the table will be ignored.</dl>
<h2>Notes</h2>
<p>Starting with Linux kernel version 3.6, there is no routing cache for IPv4 anymore. Hence <code>ip route show cached</code> will never print any entries on systems with this or newer kernel versions. </p>
<h2>Examples</h2>
<p>ip ro</p>
<dl>
<dd>Show all route entries in the kernel.</dl>
<p> ip route add default via 192.168.1.1 dev eth0</p>
<dl>
<dd>Adds a default route (for all addresses) via the local gateway 192.168.1.1 that can be reached on device eth0.</dl>
<p> ip route add 10.1.1.0/30 encap mpls 200/300 via 10.1.1.1 dev eth0</p>
<dl>
<dd>Adds an ipv4 route with mpls encapsulation attributes attached to it.</dl>
<p> ip -6 route add 2001:db8:1::/64 encap seg6 mode encap segs 2001:db8:42::1,2001:db8:ffff::2 dev eth0</p>
<dl>
<dd>Adds an IPv6 route with SRv6 encapsulation and two segments attached.</dl>
<p> ip -6 route add 2001:db8:1::/64 encap seg6local action End.DT46 vrftable 100 dev vrf100</p>
<dl>
<dd>Adds an IPv6 route with SRv6 decapsulation and forward with lookup in VRF table.</dl>
<p> ip -6 route add 2001:db8:1::/64 encap ioam6 trace prealloc type 0x800000 ns 1 size 12 dev eth0</p>
<dl>
<dd>Adds an IPv6 route with an IOAM Pre-allocated Trace encapsulation that only includes the hop limit and the node id, configured for the IOAM namespace 1 and a pre-allocated data block of 12 octets.</dl>
<p> ip route add 10.1.1.0/30 nhid 10</p>
<dl>
<dd>Adds an ipv4 route using nexthop object with id 10.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
