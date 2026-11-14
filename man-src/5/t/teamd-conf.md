---
title: "teamd-conf(5)"
name: "teamd-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-teamd-conf/"
description: "teamd.conf — libteam daemon configuration file"
---

<p>teamd.conf &#8212; libteam daemon configuration file</p>
<h2>Description</h2>
<p>teamd uses JSON format configuration.</p>
<h2>Options</h2>
<dl>
<dt><code>device </code>(string)</p>
<dd>Desired name of new team device.</p>
<dt><code>debug_level </code>(int)</p>
<dd>Level of debug messages. The higher it is the more debug messages will be printed. It is the same as adding &quot;-g&quot; command line options.</p>
<dl>
<dd>Default: <code>0</code> (disabled)</dl>
<dt><code>hwaddr </code>(string)</p>
<dd>Desired hardware address of new team device. Usual MAC address format is accepted.</p>
<dt><code>runner.name </code>(string)</p>
<dd>Name of team device. The following runners are available:</p>
<dl>
<dd><code>broadcast &#8212;</code> Simple runner which directs the team device to transmit packets via all ports. </p>
<p> <code>roundrobin &#8212;</code> Simple runner which directs the team device to transmits packets in a round-robin fashion. </p>
<p> <code>activebackup &#8212;</code> Watches for link changes and selects active port to be used for data transfers. </p>
<p> <code>loadbalance &#8212;</code> To do passive load balancing, runner only sets up BPF hash function which will determine port for packet transmit. To do active load balancing, runner moves hashes among available ports trying to reach perfect balance. </p>
<p> <code>lacp &#8212;</code> Implements 802.3ad LACP protocol. Can use same Tx port selection possibilities as loadbalance runner.</dl>
<dt><code>notify_peers.count </code>(int)</p>
<dd>Number of bursts of unsolicited NAs and gratuitous ARP packets sent after port is enabled or disabled.</p>
<dl>
<dd>Default: <code>0</code> (disabled) </p>
<p> Default for activebackup runner: <code>1</code></dl>
<dt><code>notify_peers.interval </code>(int)</p>
<dd>Value is positive number in milliseconds. Specifies an interval between bursts of notify-peer packets.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>mcast_rejoin.count </code>(int)</p>
<dd>Number of bursts of multicast group rejoin requests sent after port is enabled or disabled.</p>
<dl>
<dd>Default: <code>0</code> (disabled) </p>
<p> Default for activebackup runner: <code>1</code></dl>
<dt><code>mcast_rejoin.interval </code>(int)</p>
<dd>Value is positive number in milliseconds. Specifies an interval between bursts of multicast group rejoin requests.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>link_watch.name |</code> ports.PORTIFNAME.link_watch.name <code>(string)</code></p>
<dd>Name of link watcher to be used. The following link watchers are available:</p>
<dl>
<dd><code>ethtool &#8212;</code> Uses Libteam lib to get port ethtool state changes. </p>
<p> <code>arp_ping &#8212;</code> ARP requests are sent through a port. If an ARP reply is received, the link is considered to be up. </p>
<p> <code>nsna_ping &#8212;</code> Similar to the previous, except that it uses IPv6 Neighbor Solicitation / Neighbor Advertisement mechanism. This is an alternative to arp_ping and becomes handy in pure-IPv6 environments. </p>
<dl>
<dt><code>ports </code>(object)</p>
<dd>List of ports, network devices, to be used in a team device.</dl>
<p> See examples for more information.</dl>
<dt><code>ports.PORTIFNAME.queue_id </code>(int)</p>
<dd>ID of queue which this port should be mapped to.</p>
<dl>
<dd>Default: <code>None</code></dl>
</dl>
<h2>Active-Backup Runner Specific Options</h2>
<dl>
<dt><code>runner.hwaddr_policy </code>(string)</p>
<dd>This defines the policy of how hardware addresses of team device and port devices should be set during the team lifetime. The following are available:</p>
<dl>
<dd><code>same_all &#8212;</code> All ports will always have the same hardware address as the associated team device. </p>
<p> <code>by_active &#8212;</code> Team device adopts the hardware address of the currently active port. This is useful when the port device is not able to change its hardware address. </p>
<p> <code>only_active &#8212;</code> Only the active port adopts the hardware address of the team device. The others have their own. </p>
<p> Default: <code>same_all</code></dl>
</dl>
<dl>
<dt><code>ports.PORTIFNAME.prio </code>(int)</p>
<dd>Port priority. The higher number means higher priority.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>ports.PORTIFNAME.sticky </code>(bool)</p>
<dd>Flag which indicates if the port is sticky. If set, it means the port does not get unselected if another port with higher priority or better parameters becomes available.</p>
<dl>
<dd>Default: <code>false</code></dl>
</dl>
<h2>Load Balance Runner Specific Options</h2>
<dl>
<dt><code>runner.tx_hash </code>(array)</p>
<dd>List of fragment types (strings) which should be used for packet Tx hash computation. The following are available:</p>
<dl>
<dd><code>eth &#8212;</code> Uses source and destination MAC addresses. </p>
<p> <code>vlan &#8212;</code> Uses VLAN id. </p>
<p> <code>ipv4 &#8212;</code> Uses source and destination IPv4 addresses. </p>
<p> <code>ipv6 &#8212;</code> Uses source and destination IPv6 addresses. </p>
<p> <code>ip &#8212;</code> Uses source and destination IPv4 and IPv6 addresses. </p>
<p> <code>l3 &#8212;</code> Uses source and destination IPv4 and IPv6 addresses. </p>
<p> <code>tcp &#8212;</code> Uses source and destination TCP ports. </p>
<p> <code>udp &#8212;</code> Uses source and destination UDP ports. </p>
<p> <code>sctp &#8212;</code> Uses source and destination SCTP ports. </p>
<p> <code>l4 &#8212;</code> Uses source and destination TCP and UDP and SCTP ports.</dl>
<dt><code>runner.tx_balancer.name </code>(string)</p>
<dd>Name of active Tx balancer. Active Tx balancing is disabled by default. The only value available is <code>basic.</code></p>
<dl>
<dd>Default: <code>None</code></dl>
<dt><code>runner.tx_balancer.balancing_interval </code>(int)</p>
<dd>In tenths of a second. Periodic interval between rebalancing.</p>
<dl>
<dd>Default: <code>50</code></dl>
</dl>
<h2>Lacp Runner Specific Options</h2>
<dl>
<dt><code>runner.active </code>(bool)</p>
<dd>If active is <code>true</code> LACPDU frames are sent along the configured links periodically. If not, it acts as &quot;speak when spoken to&quot;.</p>
<dl>
<dd>Default: <code>true</code></dl>
</dl>
<dl>
<dt><code>runner.fast_rate </code>(bool)</p>
<dd>Option specifies the rate at which our link partner is asked to transmit LACPDU packets. If this is <code>true</code> then packets will be sent once per second. Otherwise they will be sent every 30 seconds.</p>
<dt><code>runner.tx_hash </code>(array)</p>
<dd>Same as for load balance runner.</p>
<dt><code>runner.tx_balancer.name </code>(string)</p>
<dd>Same as for load balance runner.</p>
<dt><code>runner.tx_balancer.balancing_interval </code>(int)</p>
<dd>Same as for load balance runner.</p>
<dt><code>runner.sys_prio </code>(int)</p>
<dd>System priority, value can be 0 &#8211; 65535.</p>
<dl>
<dd>Default: <code>255</code></dl>
<dt><code>runner.min_ports </code>(int)</p>
<dd>Specifies the minimum number of ports that must be active before asserting carrier in the master interface, value can be 1 &#8211; 255.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>runner.agg_select_policy </code>(string)</p>
<dd>This selects the policy of how the aggregators will be selected. The following are available:</p>
<dl>
<dd><code>lacp_prio &#8212;</code> Aggregator with highest priority according to LACP standard will be selected. Aggregator priority is affected by per-port option <code>lacp_prio.</code> </p>
<p> <code>lacp_prio_stable &#8212;</code> Same as previous one, except do not replace selected aggregator if it is still usable. </p>
<p> <code>bandwidth &#8212;</code> Select aggregator with highest total bandwidth. </p>
<p> <code>count &#8212;</code> Select aggregator with highest number of ports. </p>
<p> <code>port_options &#8212;</code> Aggregator with highest priority according to per-port options <code>prio </code>and <code>sticky </code> will be selected. This means that the aggregator containing the port with the highest priority will be selected unless at least one of the ports in the currently selected aggregator is sticky. </p>
<p> Default: <code>lacp_prio</code></dl>
<dt><code>ports.PORTIFNAME.lacp_prio </code>(int)</p>
<dd>Port priority according to LACP standard. The lower number means higher priority.</p>
<dt><code>ports.PORTIFNAME.lacp_key </code>(int)</p>
<dd>Port key according to LACP standard. It is only possible to aggregate ports with the same key.</p>
<dl>
<dd>Default: <code>0</code></dl>
</dl>
<h2>Ethtool Link Watch Specific Options</h2>
<dl>
<dt><code>link_watch.delay_up |</code> ports.PORTIFNAME.link_watch.delay_up <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the delay between the link coming up and the runner being notified about it.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>link_watch.delay_down |</code> ports.PORTIFNAME.link_watch.delay_down <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the delay between the link going down and the runner being notified about it.</p>
<dl>
<dd>Default: <code>0</code></dl>
</dl>
<h2>Arp Ping Link Watch Specific Options</h2>
<dl>
<dt><code>link_watch.interval |</code> ports.PORTIFNAME.link_watch.interval <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the interval between ARP requests being sent.</p>
<dt><code>link_watch.init_wait |</code> ports.PORTIFNAME.link_watch.init_wait <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the delay between link watch initialization and the first ARP request being sent.</p>
<dl>
<dd>Default: <code>0</code></dl>
<dt><code>link_watch.missed_max |</code> ports.PORTIFNAME.link_watch.missed_max <code>(int)</code></p>
<dd>Maximum number of missed ARP replies. If this number is exceeded, link is reported as down.</p>
<dl>
<dd>Default: <code>3</code></dl>
<dt><code>link_watch.source_host |</code> ports.PORTIFNAME.link_watch.source_host <code>(hostname)</code></p>
<dd>Hostname to be converted to IP address which will be filled into ARP request as source address.</p>
<dl>
<dd>Default: <code>0.0.0.0</code></dl>
<dt><code>link_watch.target_host |</code> ports.PORTIFNAME.link_watch.target_host <code>(hostname)</code></p>
<dd>Hostname to be converted to IP address which will be filled into ARP request as destination address.</p>
<dt><code>link_watch.validate_active |</code> ports.PORTIFNAME.link_watch.validate_active <code>(bool)</code></p>
<dd>Validate received ARP packets on active ports. If this is not set, all incoming ARP packets will be considered as a good reply.</p>
<dl>
<dd>Default: <code>false</code></dl>
<dt><code>link_watch.validate_inactive |</code> ports.PORTIFNAME.link_watch.validate_inactive <code>(bool)</code></p>
<dd>Validate received ARP packets on inactive ports. If this is not set, all incoming ARP packets will be considered as a good reply.</p>
<dl>
<dd>Default: <code>false</code></dl>
<dt><code>link_watch.send_always |</code> ports.PORTIFNAME.link_watch.send_always <code>(bool)</code></p>
<dd>By default, ARP requests are sent on active ports only. This option allows sending even on inactive ports.</dl>
<p> Default: <code>false</code></p>
<h2>Ns/Na Ping Link Watch Specific Options</h2>
<dl>
<dt><code>link_watch.interval |</code> ports.PORTIFNAME.link_watch.interval <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the interval between sending NS packets.</p>
<dt><code>link_watch.init_wait |</code> ports.PORTIFNAME.link_watch.init_wait <code>(int)</code></p>
<dd>Value is a positive number in milliseconds. It is the delay between link watch initialization and the first NS packet being sent.</p>
<dt><code>link_watch.missed_max |</code> ports.PORTIFNAME.link_watch.missed_max <code>(int)</code></p>
<dd>Maximum number of missed NA reply packets. If this number is exceeded, link is reported as down.</p>
<dl>
<dd>Default: <code>3</code></dl>
<dt><code>link_watch.target_host |</code> ports.PORTIFNAME.link_watch.target_host <code>(hostname)</code></p>
<dd>Hostname to be converted to IPv6 address which will be filled into NS packet as target address.</dl>
<h2>Examples</h2>
<pre><code>{
    &quot;device&quot;: &quot;team0&quot;,
    &quot;runner&quot;: {&quot;name&quot;: &quot;roundrobin&quot;},
    &quot;ports&quot;: {&quot;eth1&quot;: {}, &quot;eth2&quot;: {}}
}</code></pre>
<p> Very basic configuration. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {&quot;name&quot;: &quot;activebackup&quot;},<br />
    &quot;link_watch&quot;: {&quot;name&quot;: &quot;ethtool&quot;},<br />
    &quot;ports&quot;: {<br />
        &quot;eth1&quot;: {<br />
            &quot;prio&quot;: -10,<br />
            &quot;sticky&quot;: true<br />
        },<br />
        &quot;eth2&quot;: {<br />
            &quot;prio&quot;: 100<br />
        }<br />
    }<br />
} This configuration uses active-backup runner with ethtool link watcher. Port eth2 has higher priority, but the sticky flag ensures that if eth1 becomes active, it stays active while the link remains up. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {&quot;name&quot;: &quot;activebackup&quot;},<br />
    &quot;link_watch&quot;: {<br />
        &quot;name&quot;: &quot;ethtool&quot;,<br />
        &quot;delay_up&quot;: 2500,<br />
        &quot;delay_down&quot;: 1000<br />
    },<br />
    &quot;ports&quot;: {<br />
        &quot;eth1&quot;: {<br />
            &quot;prio&quot;: -10,<br />
            &quot;sticky&quot;: true<br />
        },<br />
        &quot;eth2&quot;: {<br />
            &quot;prio&quot;: 100<br />
        }<br />
    }<br />
} Similar to the previous one. Only difference is that link changes are not propagated to the runner immediately, but delays are applied. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {&quot;name&quot;: &quot;activebackup&quot;},<br />
    &quot;link_watch&quot;: {<br />
        &quot;name&quot;: &quot;arp_ping&quot;,<br />
        &quot;interval&quot;: 100,<br />
        &quot;missed_max&quot;: 30,<br />
        &quot;target_host&quot;: &quot;192.168.23.1&quot;<br />
    },<br />
    &quot;ports&quot;: {<br />
        &quot;eth1&quot;: {<br />
            &quot;prio&quot;: -10,<br />
            &quot;sticky&quot;: true<br />
        },<br />
        &quot;eth2&quot;: {<br />
            &quot;prio&quot;: 100<br />
        }<br />
    }<br />
} This configuration uses ARP ping link watch. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {&quot;name&quot;: &quot;activebackup&quot;},<br />
    &quot;link_watch&quot;: [<br />
    {<br />
        &quot;name&quot;: &quot;arp_ping&quot;,<br />
        &quot;interval&quot;: 100,<br />
        &quot;missed_max&quot;: 30,<br />
        &quot;target_host&quot;: &quot;192.168.23.1&quot;<br />
    },<br />
    {<br />
        &quot;name&quot;: &quot;arp_ping&quot;,<br />
        &quot;interval&quot;: 50,<br />
        &quot;missed_max&quot;: 20,<br />
        &quot;target_host&quot;: &quot;192.168.24.1&quot;<br />
    }<br />
    ],<br />
    &quot;ports&quot;: {<br />
        &quot;eth1&quot;: {<br />
            &quot;prio&quot;: -10,<br />
            &quot;sticky&quot;: true<br />
        },<br />
        &quot;eth2&quot;: {<br />
            &quot;prio&quot;: 100<br />
        }<br />
    }<br />
} Similar to the previous one, only this time two link watchers are used at the same time. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {<br />
        &quot;name&quot;: &quot;loadbalance&quot;,<br />
        &quot;tx_hash&quot;: [&quot;eth&quot;, &quot;ipv4&quot;, &quot;ipv6&quot;]<br />
    },<br />
    &quot;ports&quot;: {&quot;eth1&quot;: {}, &quot;eth2&quot;: {}}<br />
} Configuration for hash-based passive Tx load balancing. {<br />
    &quot;device&quot;: &quot;team0&quot;,<br />
    &quot;runner&quot;: {<br />
        &quot;name&quot;: &quot;loadbalance&quot;,<br />
        &quot;tx_hash&quot;: [&quot;eth&quot;, &quot;ipv4&quot;, &quot;ipv6&quot;],<br />
        &quot;tx_balancer&quot;: {<br />
            &quot;name&quot;: &quot;basic&quot;<br />
        }<br />
    },<br />
    &quot;ports&quot;: {&quot;eth1&quot;: {}, &quot;eth2&quot;: {}}<br />
} Configuration for active Tx load balancing using basic load balancer. </p>
<pre><code>{
    &quot;device&quot;: &quot;team0&quot;,
    &quot;runner&quot;: {
        &quot;name&quot;: &quot;lacp&quot;,
        &quot;active&quot;: true,
        &quot;fast_rate&quot;: true,
        &quot;tx_hash&quot;: [&quot;eth&quot;, &quot;ipv4&quot;, &quot;ipv6&quot;]
    },
    &quot;link_watch&quot;: {&quot;name&quot;: &quot;ethtool&quot;},
    &quot;ports&quot;: {&quot;eth1&quot;: {}, &quot;eth2&quot;: {}}
}</code></pre>
<p> Configuration for connection to LACP capable counterpart.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-teamd/">teamd</a></code>(8), <code><a href="/docs/linux/man/8-teamdctl/">teamdctl</a></code>(8), <code><a href="/docs/linux/man/8-teamnl/">teamnl</a></code>(8), <code><a href="/docs/linux/man/1-bond2team/">bond2team</a></code>(1)</p>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libteam.</p>
