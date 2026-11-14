---
title: "keepalived-conf(5)"
name: "keepalived-conf"
section: "5"
letter: "k"
url: "/docs/linux/man/5-keepalived-conf/"
description: "/etc/keepalived/keepalived.conf – configuration file for keepalived"
---

<p>/etc/keepalived/keepalived.conf &#8211; configuration file for keepalived</p>
<h2>Description</h2>
<p><code>keepalived.conf</code> is the configuration file which describes all the keepalived keywords. keywords are placed in hierachies of blocks (and subblocks), each layer being delimited by &#8216;{&#8216; and &#8216;}&#8217; pairs. </p>
<p> Comments start with &#8216;#&#8217; or &#8216;!&#8217; to the end of the line and can start anywhere in a line.</p>
<h2>Top Hierachy</h2>
<p><code>GLOBAL CONFIGURATION</code> </p>
<p> <code>VRRPD CONFIGURATION</code> </p>
<p> <code>LVS CONFIGURATION</code></p>
<h2>Global Configuration</h2>
<p>contains subblocks of <code>Global definitions</code> and <code>Static routes</code></p>
<h2>Global definitions</h2>
<p>&nbsp;<wbr>global_defs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Block id<br />
&nbsp;<wbr>{&nbsp;<wbr><br />
&nbsp;<wbr>notification_email&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>To:<br />
&nbsp;<wbr>&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>admin [at] example1.com&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>}<br />
&nbsp;<wbr>#&nbsp;<wbr>From: from address that will be in header<br />
&nbsp;<wbr>notification_email_from admin [at] example.com&nbsp;<wbr><br />
&nbsp;<wbr>smtp_server 127.0.0.1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>IP<br />
&nbsp;<wbr>smtp_connect_timeout 30&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>integer, seconds<br />
&nbsp;<wbr>router_id my_hostname&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>string identifying the machine,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>(doesn&#8217;t have to be hostname).<br />
&nbsp;<wbr>vrrp_mcast_group4 224.0.0.18&nbsp;<wbr>#&nbsp;<wbr>optional, default 224.0.0.18<br />
&nbsp;<wbr>vrrp_mcast_group6 ff02::12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>optional, default ff02::12<br />
&nbsp;<wbr>enable_traps&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>enable SNMP traps<br />
&nbsp;<wbr>}</p>
<h2>Static routes/addresses</h2>
<p>keepalived can configure static addresses and routes. These addresses are <code>NOT</code> moved by vrrpd, they stay on the machine. If you already have IPs and routes on your machines and your machines can ping each other, you don&#8217;t need this section. </p>
<p> The syntax is the same as for virtual addresses and virtual routes. </p>
<p>&nbsp;<wbr>static_ipaddress<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>192.168.1.1/24 dev eth0 scope global<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>static_routes<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>192.168.2.0/24 via 192.168.1.100 dev eth0<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>}</p>
<h2>Vrrpd Configuration</h2>
<p>contains subblocks of <code>VRRP synchronization group(s)</code> and <code>VRRP instance(s)</code></p>
<h2>VRRP synchronization group(s)</h2>
<p>&nbsp;<wbr>#string, name of group of IPs that failover together<br />
&nbsp;<wbr>vrrp_sync_group VG_1&nbsp;<wbr>{&nbsp;<wbr><br />
&nbsp;<wbr>group&nbsp;<wbr>{<br />
inside_network&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>name of vrrp_instance&nbsp;<wbr>(below)&nbsp;<wbr><br />
outside_network&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>One for each moveable IP.&nbsp;<wbr><br />
&#8230;&nbsp;<wbr><br />
&nbsp;<wbr>}<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>notify scripts and alerts are optional<br />
&nbsp;<wbr>#<br />
&nbsp;<wbr>#&nbsp;<wbr>filenames of scripts to run on transitions<br />
&nbsp;<wbr>#&nbsp;<wbr>can be unquoted&nbsp;<wbr>(if just filename)&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>or quoted&nbsp;<wbr>(if has parameters)<br />
&nbsp;<wbr>#&nbsp;<wbr>to MASTER transition<br />
&nbsp;<wbr>notify_master&nbsp;<wbr>/path/to_master.sh&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>to BACKUP transition<br />
&nbsp;<wbr>notify_backup&nbsp;<wbr>/path/to_backup.sh&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>FAULT transition&nbsp;<wbr><br />
&nbsp;<wbr>notify_fault&nbsp;<wbr>&quot;/path/fault.sh VG_1&quot;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>for ANY state transition.<br />
&nbsp;<wbr>#&nbsp;<wbr>&quot;notify&quot;&nbsp;<wbr>script is called AFTER the&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>notify_*&nbsp;<wbr>script(s)&nbsp;<wbr>and is executed&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>with 3 arguments provided by keepalived<br />
&nbsp;<wbr>#&nbsp;<wbr>(ie don&#8217;t include parameters in the notify line).<br />
&nbsp;<wbr>#&nbsp;<wbr>arguments<br />
&nbsp;<wbr>#&nbsp;<wbr>$1&nbsp;<wbr>=&nbsp;<wbr>&quot;GROUP&quot;|&quot;INSTANCE&quot;<br />
&nbsp;<wbr>#&nbsp;<wbr>$2&nbsp;<wbr>=&nbsp;<wbr>name of group or instance<br />
&nbsp;<wbr>#&nbsp;<wbr>$3&nbsp;<wbr>=&nbsp;<wbr>target state of transition&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(&quot;MASTER&quot;|&quot;BACKUP&quot;|&quot;FAULT&quot;)<br />
&nbsp;<wbr>notify&nbsp;<wbr>/path/notify.sh&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Send email notifcation during state transition,&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>using addresses in global_defs above.<br />
&nbsp;<wbr>smtp_alert<br />
&nbsp;<wbr>}</p>
<h2>VRRP instance(s)</h2>
<p>describes the moveable IP for each instance of a group in vrrp_sync_group. Here are described two IPs (on inside_network and on outside_network), on machine &quot;my_hostname&quot;, which belong to the group VG_1 and which will transition together on any state change. </p>
<p>&nbsp;<wbr>#You will need to write another block for outside_network.<br />
&nbsp;<wbr>vrrp_instance inside_network&nbsp;<wbr>{<br />
&nbsp;<wbr>#&nbsp;<wbr>Initial state, MASTER|BACKUP<br />
&nbsp;<wbr>#&nbsp;<wbr>As soon as the other machine(s)&nbsp;<wbr>come up,&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>an election will be held and the machine&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>with the highest&nbsp;<wbr>&quot;priority&quot;&nbsp;<wbr>will become MASTER.<br />
&nbsp;<wbr>#&nbsp;<wbr>So the entry here doesn&#8217;t matter a whole lot.<br />
&nbsp;<wbr>state MASTER </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>interface for inside_network, bound by vrrp<br />
&nbsp;<wbr>interface eth0 </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Use VRRP Virtual MAC.<br />
&nbsp;<wbr>use_vmac&nbsp;<wbr>&lt;VMAC_INTERFACE&gt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Send/Recv VRRP messages from base interface instead of<br />
&nbsp;<wbr>#&nbsp;<wbr>VMAC interface<br />
&nbsp;<wbr>vmac_xmit_base </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Ignore VRRP interface faults&nbsp;<wbr>(default unset)<br />
&nbsp;<wbr>dont_track_primary </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>optional, monitor these as well.&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>go to FAULT state if any of these go down.<br />
&nbsp;<wbr>track_interface&nbsp;<wbr>{<br />
eth0&nbsp;<wbr><br />
eth1&nbsp;<wbr><br />
&#8230;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>default IP for binding vrrpd is the primary IP&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>on interface. If you want to hide location of vrrpd,&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>use this IP as src_addr for multicast or unicast vrrp<br />
&nbsp;<wbr>#&nbsp;<wbr>packets.&nbsp;<wbr>(since it&#8217;s multicast, vrrpd will get the reply&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>packet no matter what src_addr is used).<br />
&nbsp;<wbr>#&nbsp;<wbr>optional<br />
&nbsp;<wbr>mcast_src_ip&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr><br />
&nbsp;<wbr>unicast_src_ip&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Do not send VRRP adverts over VRRP multicast group.<br />
&nbsp;<wbr>#&nbsp;<wbr>Instead it sends adverts to the following list of<br />
&nbsp;<wbr>#&nbsp;<wbr>ip addresses using unicast design fashion. It can<br />
&nbsp;<wbr>#&nbsp;<wbr>be cool to use VRRP FSM and features in a networking<br />
&nbsp;<wbr>#&nbsp;<wbr>environement where multicast is not supported&nbsp;<wbr>!<br />
&nbsp;<wbr>#&nbsp;<wbr>IP Addresses specified can IPv4 as well as IPv6<br />
&nbsp;<wbr>unicast_peer&nbsp;<wbr>{<br />
&lt;IPADDR&gt;<br />
&#8230;<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Binding interface for lvs syncd<br />
&nbsp;<wbr>lvs_sync_daemon_interface eth1&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>delay for gratuitous ARP after transition to MASTER<br />
&nbsp;<wbr>garp_master_delay 10&nbsp;<wbr>#&nbsp;<wbr>secs, default 5&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>arbitary unique number 0..255<br />
&nbsp;<wbr>#&nbsp;<wbr>used to differentiate multiple instances of vrrpd<br />
&nbsp;<wbr>#&nbsp;<wbr>running on the same NIC&nbsp;<wbr>(and hence same socket).<br />
&nbsp;<wbr>virtual_router_id 51 </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>for electing MASTER, highest priority wins.<br />
&nbsp;<wbr>#&nbsp;<wbr>to be MASTER, make 50 more than other machines.<br />
&nbsp;<wbr>priority 100 </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>VRRP Advert interval, secs&nbsp;<wbr>(use default)<br />
&nbsp;<wbr>advert_int 1<br />
&nbsp;<wbr>authentication&nbsp;<wbr>{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Authentication block<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>PASS||AH<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>PASS &#8211; Simple Passwd&nbsp;<wbr>(suggested)&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>AH &#8211; IPSEC&nbsp;<wbr>(not recommended))<br />
&nbsp;<wbr>&nbsp;<wbr>auth_type PASS<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Password for accessing vrrpd.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>should be the same for all machines.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Only the first eight&nbsp;<wbr>(8)&nbsp;<wbr>characters are used.<br />
&nbsp;<wbr>&nbsp;<wbr>auth_pass 1234<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>#addresses add|del on change to MASTER, to BACKUP.<br />
&nbsp;<wbr>#With the same entries on other machines,<br />
&nbsp;<wbr>#the opposite transition will be occuring.<br />
&nbsp;<wbr>virtual_ipaddress&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR&gt;/&lt;MASK&gt;&nbsp;<wbr>brd&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>dev&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>scope&nbsp;<wbr>&lt;SCOPE&gt;&nbsp;<wbr>label&nbsp;<wbr>&lt;LABEL&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>192.168.200.17/24 dev eth1<br />
&nbsp;<wbr>&nbsp;<wbr>192.168.200.18/24 dev eth2 label eth2:1<br />
&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>#VRRP IP excluded from VRRP<br />
&nbsp;<wbr>#optional.<br />
&nbsp;<wbr>#For cases with large numbers&nbsp;<wbr>(eg 200)&nbsp;<wbr>of IPs&nbsp;<wbr><br />
&nbsp;<wbr>#on the same interface. To decrease the number&nbsp;<wbr><br />
&nbsp;<wbr>#of packets sent in adverts, you can exclude&nbsp;<wbr><br />
&nbsp;<wbr>#most IPs from adverts.<br />
&nbsp;<wbr>#The IPs are add|del as for virtual_ipaddress.<br />
&nbsp;<wbr>virtual_ipaddress_excluded&nbsp;<wbr>{&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR&gt;/&lt;MASK&gt;&nbsp;<wbr>brd&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>dev&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>scope&nbsp;<wbr>&lt;SCOPE&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR&gt;/&lt;MASK&gt;&nbsp;<wbr>brd&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>dev&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>scope&nbsp;<wbr>&lt;SCOPE&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>}<br />
&nbsp;<wbr>#&nbsp;<wbr>routes add|del when changing to MASTER, to BACKUP<br />
&nbsp;<wbr>virtual_routes&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>src&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>[to]&nbsp;<wbr>&lt;IPADDR&gt;/&lt;MASK&gt;&nbsp;<wbr>via|gw&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>[or&nbsp;<wbr>&lt;IPADDR&gt;]&nbsp;<wbr>dev&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>scope&nbsp;<wbr>&lt;SCOPE&gt;&nbsp;<wbr>tab<br />
&nbsp;<wbr>&nbsp;<wbr>src 192.168.100.1 to 192.168.109.0/24 via 192.168.200.254 dev eth1<br />
&nbsp;<wbr>&nbsp;<wbr>192.168.110.0/24 via 192.168.200.254 dev eth1<br />
&nbsp;<wbr>&nbsp;<wbr>192.168.111.0/24 dev eth2<br />
&nbsp;<wbr>&nbsp;<wbr>192.168.112.0/24 via 192.168.100.254 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>192.168.113.0/24 via 192.168.200.254 or 192.168.100.254 dev eth1<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>blackhole 192.168.114.0/24</p>
<p>&nbsp;<wbr>} </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>VRRP will normally preempt a lower priority<br />
&nbsp;<wbr>#&nbsp;<wbr>machine when a higher priority machine comes<br />
&nbsp;<wbr>#&nbsp;<wbr>online.&nbsp;<wbr>&nbsp;<wbr>&quot;nopreempt&quot;&nbsp;<wbr>allows the lower priority<br />
&nbsp;<wbr>#&nbsp;<wbr>machine to maintain the master role, even when<br />
&nbsp;<wbr>#&nbsp;<wbr>a higher priority machine comes back online.<br />
&nbsp;<wbr>#&nbsp;<wbr>NOTE: For this to work, the initial state of this<br />
&nbsp;<wbr>#&nbsp;<wbr>entry must be BACKUP.<br />
&nbsp;<wbr>nopreempt </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Seconds after startup until preemption<br />
&nbsp;<wbr>#&nbsp;<wbr>(if not disabled by&nbsp;<wbr>&quot;nopreempt&quot;).<br />
&nbsp;<wbr>#&nbsp;<wbr>Range: 0&nbsp;<wbr>(default)&nbsp;<wbr>to 1,000<br />
&nbsp;<wbr>#&nbsp;<wbr>NOTE: For this to work, the initial state of this<br />
&nbsp;<wbr>#&nbsp;<wbr>entry must be BACKUP.<br />
&nbsp;<wbr>preempt_delay 300&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>waits 5 minutes </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Debug level, not implemented yet.<br />
&nbsp;<wbr>debug </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>notify scripts, alert as above<br />
&nbsp;<wbr>notify_master&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;<br />
&nbsp;<wbr>notify_backup&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;<br />
&nbsp;<wbr>notify_fault&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;&nbsp;<wbr><br />
&nbsp;<wbr>notify&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;&nbsp;<wbr><br />
&nbsp;<wbr>smtp_alert&nbsp;<wbr><br />
&nbsp;<wbr>}</p>
<h2>Lvs Configuration</h2>
<p>contains subblocks of <code>Virtual server group(s)</code> and <code>Virtual server(s)</code> </p>
<p> The subblocks contain arguments for <i><a href="/docs/linux/man/8-ipvsadm/">ipvsadm</a>(8). </i> A knowlege of <i><a href="/docs/linux/man/8-ipvsadm/">ipvsadm</a>(8)</i> will be helpful here.</p>
<h2>Virtual server group(s)</h2>
<p>&nbsp;<wbr>#&nbsp;<wbr>optional<br />
&nbsp;<wbr>#&nbsp;<wbr>this groups allows a service on a real_server&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>to belong to multiple virtual services&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>and to be only health checked once.<br />
&nbsp;<wbr>#&nbsp;<wbr>Only for very large LVSs.<br />
&nbsp;<wbr>virtual_server_group&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>#VIP port<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>&lt;PORT&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>#<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&lt;IPADDR RANGE&gt;&nbsp;<wbr>has the form&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>XXX.YYY.ZZZ.WWW-VVV eg 192.168.200.1-10&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>range includes both .1 and .10 address<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR RANGE&gt;&nbsp;<wbr>&lt;PORT&gt;#&nbsp;<wbr>VIP range VPORT<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;IPADDR RANGE&gt;&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>fwmark&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>fwmark<br />
&nbsp;<wbr>&nbsp;<wbr>fwmark&nbsp;<wbr>&lt;INT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230; }</p>
<h2>Virtual server(s)</h2>
<p>A virtual_server can be a declaration of one of</p>
<dl>
<dt><code>vip vport (IPADDR PORT pair)</code></p>
<dd>
<dt><code>fwmark &lt;INT&gt;</code></p>
<dd>
<dt><code>(virtual server) group &lt;STRING&gt;</code></p>
<dd>&nbsp;<wbr>#setup service<br />
&nbsp;<wbr>virtual_server IP port |<br />
&nbsp;<wbr>virtual_server fwmark int |<br />
&nbsp;<wbr>virtual_server group string<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>#&nbsp;<wbr>delay timer for service polling<br />
&nbsp;<wbr>delay_loop&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>LVS scheduler&nbsp;<wbr><br />
&nbsp;<wbr>lb_algo rr|wrr|lc|wlc|lblc|sh|dh&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>Enable One-Packet-Scheduling for UDP&nbsp;<wbr>(-O in ipvsadm)<br />
&nbsp;<wbr>ops<br />
&nbsp;<wbr>#&nbsp;<wbr>LVS forwarding method<br />
&nbsp;<wbr>lb_kind NAT|DR|TUN&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>LVS persistence timeout, sec<br />
&nbsp;<wbr>persistence_timeout&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>LVS granularity mask&nbsp;<wbr>(-M in ipvsadm)<br />
&nbsp;<wbr>persistence_granularity&nbsp;<wbr>&lt;NETMASK&gt;&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>Only TCP is implemented<br />
&nbsp;<wbr>protocol TCP&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>If VS IP address is not set,&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>suspend healthchecker&#8217;s activity<br />
&nbsp;<wbr>ha_suspend<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>VirtualHost string for HTTP_GET or SSL_GET<br />
&nbsp;<wbr>#&nbsp;<wbr>eg virtualhost&nbsp;<wbr><a rel="nofollow" href="http://www.firewall.loc">www.firewall.loc</a><br />
&nbsp;<wbr>virtualhost&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Assume silently all RSs down and healthchecks<br />
&nbsp;<wbr>#&nbsp;<wbr>failed on start. This helps preventing false<br />
&nbsp;<wbr>#&nbsp;<wbr>positive actions on startup. Alpha mode is<br />
&nbsp;<wbr>#&nbsp;<wbr>disabled by default.<br />
&nbsp;<wbr>alpha </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>On daemon shutdown, consider quorum and RS<br />
&nbsp;<wbr>#&nbsp;<wbr>down notifiers for execution, where appropriate.<br />
&nbsp;<wbr>#&nbsp;<wbr>Omega mode is disabled by default.<br />
&nbsp;<wbr>omega </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Minimum total weight of all live servers in<br />
&nbsp;<wbr>#&nbsp;<wbr>the pool necessary to operate VS with no<br />
&nbsp;<wbr>#&nbsp;<wbr>quality regression. Defaults to 1.<br />
&nbsp;<wbr>quorum&nbsp;<wbr>&lt;INT&gt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Tolerate this much weight units compared to the<br />
&nbsp;<wbr>#&nbsp;<wbr>nominal quorum, when considering quorum gain<br />
&nbsp;<wbr>#&nbsp;<wbr>or loss. A flap dampener. Defaults to 0.<br />
&nbsp;<wbr>hysteresis&nbsp;<wbr>&lt;INT&gt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Script to launch when quorum is gained.<br />
&nbsp;<wbr>quorum_up&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Script to launch when quorum is lost.<br />
&nbsp;<wbr>quorum_down&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>setup realserver(s) </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>RS to add when all realservers are down<br />
&nbsp;<wbr>sorry_server&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>#&nbsp;<wbr>applies inhibit_on_failure behaviour to the<br />
&nbsp;<wbr>#&nbsp;<wbr>preceding sorry_server directive<br />
&nbsp;<wbr>sorry_server_inhibit<br />
&nbsp;<wbr><br />
&nbsp;<wbr>#&nbsp;<wbr>one entry for each realserver&nbsp;<wbr><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<p>&nbsp;<wbr>real_server&nbsp;<wbr>&lt;IPADDR&gt;&nbsp;<wbr>&lt;PORT&gt;&nbsp;<wbr><br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>relative weight to use, default: 1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weight&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Set weight to 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>when healthchecker detects failure<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>inhibit_on_failure&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Script to launch when healthchecker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>considers service as up.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>notify_up&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Script to launch when healthchecker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>considers service as down.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>notify_down&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>pick one healthchecker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>HTTP_GET|SSL_GET|TCP_CHECK|SMTP_CHECK|MISC_CHECK </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>HTTP and SSL healthcheckers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>HTTP_GET|SSL_GET&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>A url to test<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>can have multiple entries here<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>url&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#eg path&nbsp;<wbr>/&nbsp;<wbr>, or path&nbsp;<wbr>/mrtg2/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>path&nbsp;<wbr>&lt;STRING&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>healthcheck needs status_code<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>or status_code and digest<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Digest computed with genhash<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>eg digest 9b3a0c85a887a256d6939da88aabd8cd<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>digest&nbsp;<wbr>&lt;STRING&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>status code returned in the HTTP header<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>eg status_code 200<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>status_code&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>number of get retry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nb_get_retry&nbsp;<wbr>&lt;INT&gt;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>delay before retry<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delay_before_retry&nbsp;<wbr>&lt;INT&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>========&nbsp;<wbr>generic connection options<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional IP address to connect to.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is real server&#8217;s IP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_ip&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional port to connect to if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is real server&#8217;s port<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional interface to use to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bindto&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional source port to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bind_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional connection timeout in seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is 5 seconds<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_timeout&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional fwmark to mark all outgoing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checker pakets with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fwmark&nbsp;<wbr>&lt;INTEGER&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional random delay to begin initial check for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>maximum N seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Useful to scatter multiple simultaneous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checks to the same RS. Enabled by default, with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the maximum at delay_loop. Specify 0 to disable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>warmup&nbsp;<wbr>&lt;INT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>#HTTP_GET|SSL_GET </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#TCP healthchecker&nbsp;<wbr>(bind to IP port)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TCP_CHECK&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>========&nbsp;<wbr>generic connection options<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional IP address to connect to.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is real server&#8217;s IP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_ip&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional port to connect to if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is real server&#8217;s port<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional interface to use to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bindto&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional source port to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bind_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional connection timeout in seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is 5 seconds<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_timeout&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional fwmark to mark all outgoing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checker pakets with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fwmark&nbsp;<wbr>&lt;INTEGER&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional random delay to begin initial check for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>maximum N seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Useful to scatter multiple simultaneous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checks to the same RS. Enabled by default, with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the maximum at delay_loop. Specify 0 to disable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>warmup&nbsp;<wbr>&lt;INT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>#TCP_CHECK </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>SMTP healthchecker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>SMTP_CHECK<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>An optional host interface to check.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>If no host directives are present, only<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the ip address of the real server will<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>be checked.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>host&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>========&nbsp;<wbr>generic connection options<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional IP address to connect to.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>The default is real server&#8217;s IP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_ip&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional port to connect to if not<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the default of 25<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional interface to use to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bindto&nbsp;<wbr>&lt;IP ADDRESS&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional source port to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>originate the connection from<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>bind_port&nbsp;<wbr>&lt;PORT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional per-host connection timeout.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Default is outer-scope connect_timeout<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_timeout&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional fwmark to mark all outgoing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checker pakets with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fwmark&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Connection and read/write timeout<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>in seconds. The default is 5 seconds<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>connect_timeout&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Number of times to retry a failed check<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>retry&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Delay in seconds before retrying<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>delay_before_retry&nbsp;<wbr>&lt;INTEGER&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional string to use for the smtp HELO request<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>helo_name&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional random delay to begin initial check for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>maximum N seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Useful to scatter multiple simultaneous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checks to the same RS. Enabled by default, with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the maximum at delay_loop. Specify 0 to disable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>warmup&nbsp;<wbr>&lt;INT&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}&nbsp;<wbr>#SMTP_CHECK </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#MISC healthchecker, run a program<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MISC_CHECK&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>External system script or program<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>misc_path&nbsp;<wbr>&lt;STRING&gt;|&lt;QUOTED-STRING&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Script execution timeout<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>misc_timeout&nbsp;<wbr>&lt;INT&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Optional random delay to begin initial check for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>maximum N seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Useful to scatter multiple simultaneous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>checks to the same RS. Enabled by default, with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>the maximum at delay_loop. Specify 0 to disable<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>warmup&nbsp;<wbr>&lt;INT&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>If set, exit code from healthchecker is used<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>to dynamically adjust the weight as follows:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit status 0: svc check success, weight<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unchanged.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit status 1: svc check failed.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exit status 2-255: svc check success, weight<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>changed to 2 less than exit status.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(for example: exit status of 255 would set<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>weight to 253)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>misc_dynamic<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}<br />
&nbsp;<wbr>}&nbsp;<wbr>#&nbsp;<wbr>realserver defn<br />
&nbsp;<wbr>}&nbsp;<wbr>#&nbsp;<wbr>virtual service </p>
</dl>
<h2>Author</h2>
<p>Joseph Mack.<br />
 Information derived from doc/keepalived.conf.SYNOPSIS, doc/samples/keepalived.conf.* and Changelog by Alexandre Cassen for keepalived-1.1.4, and from HOWTOs by Adam Fletcher and Vince Worthington.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ipvsadm/">ipvsadm</a>(8), ip &#8211;help. </p>
