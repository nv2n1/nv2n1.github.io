---
title: "bridge(8)"
name: "bridge"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bridge/"
description: "bridge – show / manipulate bridge addresses and devices"
---

<p>bridge &#8211; show / manipulate bridge addresses and devices</p>
<h2>Synopsis</h2>
<pre><code>bridge

[ OPTIONS ] OBJECT { COMMAND |

    help }

OBJECT := {

    link | fdb | mdb | vlan | monitor }

OPTIONS := {

    -V[ersion] |
    -s[tatistics] |
    -n[etns] name |
    -b[atch] filename |
    -c[olor] |
    -p[retty] |
    -j[son] |
    -o[neline] }</code></pre>
<p> <code>bridge link set</code> <code>dev</code> <i>DEV</i> [ <code>cost</code> <i>COST</i> ] [ <code>priority</code> <i>PRIO</i> ] [ <code>state</code> <i>STATE</i> ] [ <code>guard</code> { <code>on</code> | <code>off</code> } ] [ <code>hairpin</code> { <code>on</code> | <code>off</code> } ] [ <code>fastleave</code> { <code>on</code> | <code>off</code> } ] [ <code>root_block</code> { <code>on</code> | <code>off</code> } ] [ <code>learning</code> { <code>on</code> | <code>off</code> } ] [ <code>learning_sync</code> { <code>on</code> | <code>off</code> } ] [ <code>flood</code> { <code>on</code> | <code>off</code> } ] [ <code>hwmode</code> { <code>vepa</code> | <code>veb</code> } ] [ <code>mcast_flood</code> { <code>on</code> | <code>off</code> } ] [ <code>mcast_to_unicast</code> { <code>on</code> | <code>off</code> } ] [ <code>neigh_suppress</code> { <code>on</code> | <code>off</code> } ] [ <code>vlan_tunnel</code> { <code>on</code> | <code>off</code> } ] [ <code>isolated</code> { <code>on</code> | <code>off</code> } ] [ <code>backup_port</code> <i>DEVICE</i> ] [ <code>nobackup_port</code> ] [ <code>self</code> ] [ <code>master</code> ]<br />
 <code>bridge link</code> [ <code>show</code> ] [ <code>dev</code> <i>DEV</i> ] </p>
<pre><code>bridge fdb { add | append | del | replace }

LLADDR

dev

DEV {

    local | static | dynamic } [

self ] [ master ] [ router ] [ use ] [ extern_learn ] [ sticky ] [

src_vni

VNI ] { [

    dst

    IPADDR ] [

    vni

    VNI ] [

    port

    PORT ] [

    via

    DEVICE ] |

    nhid

    NHID }</code></pre>
<p> <code>bridge fdb</code> [ [ <code>show</code> ] [ <code>br</code> <i>BRDEV</i> ] [ <code>brport</code> <i>DEV</i> ] [ <code>vlan</code> <i>VID</i> ] [ <code>state</code> <i>STATE</i> ] [ <code>dynamic</code> <i>] ]</i><br />
 <code>bridge fdb get</code> [ <code>to</code> <i>]</i> <i>LLADDR [ </i> <code>br</code> <i>BRDEV</i> ] <code>{ brport | dev }</code> <i>DEV</i> [ <code>vlan</code> <i>VID</i> ] [ <code>vni</code> <i>VNI</i> ] [ <code>self</code> ] [ <code>master</code> ] [ <code>dynamic</code> ]<br />
 <code>bridge mdb</code> { <code>add</code> | <code>del</code> } <code>dev</code> <i>DEV</i> <code>port</code> <i>PORT</i> <code>grp</code> <i>GROUP</i> [ <code>src</code> <i>SOURCE</i> ] [ <code>permanent</code> | <code>temp</code> ] [ <code>vid</code> <i>VID</i> ]<br />
 <code>bridge mdb show </code>[ <code>dev</code> <i>DEV</i> ]<br />
 <code>bridge vlan</code> { <code>add</code> | <code>del</code> } <code>dev</code> <i>DEV</i> <code>vid</code> <i>VID</i> [ <code>tunnel_info</code> <i>TUNNEL_ID</i> ] [ <code>pvid</code> ] [ <code>untagged</code> ] [ <code>self</code> ] [ <code>master</code> ]<br />
 <code>bridge vlan set</code> <code>dev</code> <i>DEV</i> <code>vid</code> <i>VID</i> [ <code>state</code> <i>STP_STATE</i> ]<br />
 <code>bridge vlan</code> [ <code>show</code> | <code>tunnelshow</code> ] [ <code>dev</code> <i>DEV</i> ]<br />
 <code>bridge monitor</code> [ <code>all</code> | <code>neigh</code> | <code>link</code> | <code>mdb</code> | <code>vlan</code> ] </p>
<h2>Options</h2>
<dl>
<dt><code>-V</code>,<code> -Version</code></p>
<dd>print the version of the <code>bridge</code> utility and exit. </p>
<dt><code>-s</code>,<code> -stats,</code> -statistics</p>
<dd>output more information. If this option is given multiple times, the amount of information increases. As a rule, the information is statistics or some time values. </p>
<dt><code>-d</code>,<code> -details</code></p>
<dd>print detailed information about bridge vlan filter entries or MDB router ports. </p>
<dt><code>-n</code>,<code> -net</code>,<code> -netns </code>&lt;NETNS&gt;</p>
<dd>switches <code>bridge</code> to the specified network namespace <i>NETNS</i>. Actually it just simplifies executing of: </p>
<p> <code>ip netns exec</code> <i>NETNS</i> <code>bridge</code> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<p> to </p>
<p> <code>bridge</code> -n[etns] <i>NETNS</i> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<dt><code>-b,</code> -batch <code>&lt;FILENAME&gt;</code></p>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of bridge command. </p>
<dt><code>-force</code></p>
<dd>Don&#8217;t terminate bridge command on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </p>
<dt><code>-c</code>[<code>color</code>][<code>=</code>{<code>always</code>|<code>auto</code>|<code>never</code>}</p>
<dd>Configure color output. If parameter is omitted or <code>always</code>, color output is enabled regardless of stdout state. If parameter is <code>auto</code>, stdout is checked to be a terminal before enabling color output. If parameter is <code>never</code>, color output is disabled. If specified multiple times, the last one takes precedence. This flag is ignored if <code>-json</code> is also given. </p>
<dt><code>-j,</code> -json</p>
<dd>Output results in JavaScript Object Notation (JSON). </p>
<dt><code>-p,</code> -pretty</p>
<dd>When combined with -j generate a pretty JSON output. </p>
<dt><code>-o,</code> -oneline</p>
<dd>output each record on a single line, replacing line feeds with the <code>&#8216;\&#8217;</code> character. This is convenient when you want to count records with <code><a href="/docs/linux/man/1-wc/">wc</a></code>(1) or to <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) the output. </p>
</dl>
<h2>Bridge &#8211; Command Syntax</h2>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>link</code></p>
<dd>&#8211; Bridge port. </p>
<dt><code>fdb</code></p>
<dd>&#8211; Forwarding Database entry. </p>
<dt><code>mdb</code></p>
<dd>&#8211; Multicast group database entry. </p>
<dt><code>vlan</code></p>
<dd>&#8211; VLAN filter list. </p>
</dl>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. As a rule, it is possible to <code>add</code>,<code> delete</code> and <code>show</code> (or <code>list</code> ) objects, but some objects do not allow all of these operations or have some additional commands. The <code>help</code> command is available for all objects. It prints out a list of available commands and argument syntax conventions. </p>
<p> If no command is given, some default command is assumed. Usually it is <code>list</code> or, if the objects of this class cannot be listed, <code>help</code>.</p>
<h2>bridge link &#8211; bridge port</h2>
<p><code>link</code> objects correspond to the port devices of the bridge. </p>
<p> The corresponding commands set and display port status and bridge specific attributes.</p>
<h3>bridge link set &#8211; set bridge specific attributes on a port</h3>
<dl>
<dt><code>dev</code><i> NAME </i></p>
<dd>interface name of the bridge port </p>
<dt><code>cost</code><i> COST </i></p>
<dd>the STP path cost of the specified port. </p>
<dt><code>priority</code><i> PRIO </i></p>
<dd>the STP port priority. The priority value is an unsigned 8-bit quantity (number between 0 and 255). This metric is used in the designated port an droot port selection algorithms. </p>
<dt><code>state</code><i> STATE </i></p>
<dd>the operation state of the port. Except state 0 (disable STP or BPDU filter feature), this is primarily used by user space STP/RSTP implementation. One may enter port state name (case insensitive), or one of the numbers below. Negative inputs are ignored, and unrecognized names return an error. </p>
<p> <code>0</code> &#8211; port is in STP <code>DISABLED</code> state. Make this port completely inactive for STP. This is also called BPDU filter and could be used to disable STP on an untrusted port, like a leaf virtual devices. </p>
<p> <code>1</code> &#8211; port is in STP <code>LISTENING</code> state. Only valid if STP is enabled on the bridge. In this state the port listens for STP BPDUs and drops all other traffic frames. </p>
<p> <code>2</code> &#8211; port is in STP <code>LEARNING</code> state. Only valid if STP is enabled on the bridge. In this state the port will accept traffic only for the purpose of updating MAC address tables. </p>
<p> <code>3</code> &#8211; port is in STP <code>FORWARDING</code> state. Port is fully active. </p>
<p> <code>4</code> &#8211; port is in STP <code>BLOCKING</code> state. Only valid if STP is enabled on the bridge. This state is used during the STP election process. In this state, port will only process STP BPDUs. </p>
<dt><code>guard on </code>or<code> guard off </code></p>
<dd>Controls whether STP BPDUs will be processed by the bridge port. By default, the flag is turned off allowed BPDU processing. Turning this flag on will disables the bridge port if a STP BPDU packet is received. </p>
<p> If running Spanning Tree on bridge, hostile devices on the network may send BPDU on a port and cause network failure. Setting <code>guard on</code> will detect and stop this by disabling the port. The port will be restarted if link is brought down, or removed and reattached. For example if guard is enable on eth0: </p>
<p> <code>ip link set dev eth0 down; ip link set dev eth0 up</code> </p>
<dt><code>hairpin on </code>or<code> hairpin off </code></p>
<dd>Controls whether traffic may be send back out of the port on which it was received. This option is also called reflective relay mode, and is used to support basic VEPA (Virtual Ethernet Port Aggregator) capabilities. By default, this flag is turned off and the bridge will not forward traffic back out of the receiving port. </p>
<dt><code>fastleave on </code>or<code> fastleave off </code></p>
<dd>This flag allows the bridge to immediately stop multicast traffic on a port that receives IGMP Leave message. It is only used with IGMP snooping is enabled on the bridge. By default the flag is off. </p>
<dt><code>root_block on </code>or<code> root_block off </code></p>
<dd>Controls whether a given port is allowed to become root port or not. Only used when STP is enabled on the bridge. By default the flag is off. </p>
<p> This feature is also called root port guard. If BPDU is received from a leaf (edge) port, it should not be elected as root port. This could be used if using STP on a bridge and the downstream bridges are not fully trusted; this prevents a hostile guest from rerouting traffic. </p>
<dt><code>learning on </code>or<code> learning off </code></p>
<dd>Controls whether a given port will learn MAC addresses from received traffic or not. If learning if off, the bridge will end up flooding any traffic for which it has no FDB entry. By default this flag is on. </p>
<dt><code>learning_sync on </code>or<code> learning_sync off </code></p>
<dd>Controls whether a given port will sync MAC addresses learned on device port to bridge FDB. </p>
<dt><code>flood on </code>or<code> flood off </code></p>
<dd>Controls whether unicast traffic for which there is no FDB entry will be flooded towards this given port. By default this flag is on. </p>
<dt><code>hwmode</code></p>
<dd>Some network interface cards support HW bridge functionality and they may be configured in different modes. Currently support modes are: </p>
<p> <code>vepa</code> &#8211; Data sent between HW ports is sent on the wire to the external switch. </p>
<p> <code>veb</code> &#8211; bridging happens in hardware. </p>
<dt><code>mcast_flood on </code>or<code> mcast_flood off </code></p>
<dd>Controls whether multicast traffic for which there is no MDB entry will be flooded towards this given port. By default this flag is on. </p>
<dt><code>mcast_to_unicast on </code>or<code> mcast_to_unicast off </code></p>
<dd>Controls whether a given port will replicate packets using unicast instead of multicast. By default this flag is off. </p>
<p> This is done by copying the packet per host and changing the multicast destination MAC to a unicast one accordingly. </p>
<p> <code>mcast_to_unicast</code> works on top of the multicast snooping feature of the bridge. Which means unicast copies are only delivered to hosts which are interested in it and signalized this via IGMP/MLD reports previously. </p>
<p> This feature is intended for interface types which have a more reliable and/or efficient way to deliver unicast packets than broadcast ones (e.g. WiFi). </p>
<p> However, it should only be enabled on interfaces where no IGMPv2/MLDv1 report suppression takes place. IGMP/MLD report suppression issue is usually overcome by the network daemon (supplicant) enabling AP isolation and by that separating all STAs. </p>
<p> Delivery of STA-to-STA IP multicast is made possible again by enabling and utilizing the bridge hairpin mode, which considers the incoming port as a potential outgoing port, too (see <code>hairpin</code> option). Hairpin mode is performed after multicast snooping, therefore leading to only deliver reports to STAs running a multicast router. </p>
<dt><code>neigh_suppress on </code>or<code> neigh_suppress off </code></p>
<dd>Controls whether neigh discovery (arp and nd) proxy and suppression is enabled on the port. By default this flag is off. </p>
<dt><code>vlan_tunnel on </code>or<code> vlan_tunnel off </code></p>
<dd>Controls whether vlan to tunnel mapping is enabled on the port. By default this flag is off. </p>
<dt><code>isolated on </code>or<code> isolated off </code></p>
<dd>Controls whether a given port will be isolated, which means it will be able to communicate with non-isolated ports only. By default this flag is off. </p>
<dt><code>backup_port</code><i> DEVICE</i></p>
<dd>If the port loses carrier all traffic will be redirected to the configured backup port </p>
<dt><code>nobackup_port</code></p>
<dd>Removes the currently configured backup port </p>
<dt><code>self</code></p>
<dd>link setting is configured on specified physical device </p>
<dt><code>master</code></p>
<dd>link setting is configured on the software bridge (default) </p>
<dt><code>-t</code>,<code> -timestamp</code></p>
<dd>display current time when using monitor option. </p>
</dl>
<h3>bridge link show &#8211; list ports configuration for all bridges.</h3>
<p>This command displays port configuration and flags for all bridges. </p>
<p> To display port configuration and flags for a specific bridge, use the &quot;ip link show master &lt;bridge_device&gt;&quot; command.</p>
<h2>bridge fdb &#8211; forwarding database management</h2>
<p><code>fdb</code> objects contain known Ethernet addresses on a link. </p>
<p> The corresponding commands display fdb entries, add new entries, append entries, and delete old ones.</p>
<h3>bridge fdb add &#8211; add a new fdb entry</h3>
<p>This command creates a new fdb entry. </p>
<dl>
<dt><code>LLADDR</code></p>
<dd>the Ethernet MAC address. </p>
<dt><code>dev</code><i> DEV</i></p>
<dd>the interface to which this address is associated. </p>
<p> <code>local</code> &#8211; is a local permanent fdb entry, which means that the bridge will not forward frames with this destination MAC address and VLAN ID, but terminate them locally. This flag is default unless &quot;static&quot; or &quot;dynamic&quot; are explicitly specified. </p>
<p> <code>permanent</code> &#8211; this is a synonym for &quot;local&quot; </p>
<p> <code>static</code> &#8211; is a static (no arp) fdb entry </p>
<p> <code>dynamic</code> &#8211; is a dynamic reachable age-able fdb entry </p>
<p> <code>self</code> &#8211; the operation is fulfilled directly by the driver for the specified network device. If the network device belongs to a master like a bridge, then the bridge is bypassed and not notified of this operation (and if the device does notify the bridge, it is driver-specific behavior and not mandated by this flag, check the driver for more details). The &quot;bridge fdb add&quot; command can also be used on the bridge device itself, and in this case, the added fdb entries will be locally terminated (not forwarded). In the latter case, the &quot;self&quot; flag is mandatory. The flag is set by default if &quot;master&quot; is not specified. </p>
<p> <code>master</code> &#8211; if the specified network device is a port that belongs to a master device such as a bridge, the operation is fulfilled by the master device&#8217;s driver, which may in turn notify the port driver too of the address. If the specified device is a master itself, such as a bridge, this flag is invalid. </p>
<p> <code>router</code> &#8211; the destination address is associated with a router. Valid if the referenced device is a VXLAN type device and has route short circuit enabled. </p>
<p> <code>use</code> &#8211; the address is in use. User space can use this option to indicate to the kernel that the fdb entry is in use. </p>
<p> <code>extern_learn</code> &#8211; this entry was learned externally. This option can be used to indicate to the kernel that an entry was hardware or user-space controller learnt dynamic entry. Kernel will not age such an entry. </p>
<p> <code>sticky</code> &#8211; this entry will not change its port due to learning. </p>
<p> The next command line parameters apply only when the specified device <i>DEV</i> is of type VXLAN.</p>
<dt><code>dst</code><i> IPADDR</i></p>
<dd>the IP address of the destination VXLAN tunnel endpoint where the Ethernet MAC ADDRESS resides. </p>
<dt><code>src_vni</code><i> VNI</i></p>
<dd>the src VNI Network Identifier (or VXLAN Segment ID) this entry belongs to. Used only when the vxlan device is in external or collect metadata mode. If omitted the value specified at vxlan device creation will be used. </p>
<dt><code>vni</code><i> VNI</i></p>
<dd>the VXLAN VNI Network Identifier (or VXLAN Segment ID) to use to connect to the remote VXLAN tunnel endpoint. If omitted the value specified at vxlan device creation will be used. </p>
<dt><code>port</code><i> PORT</i></p>
<dd>the UDP destination PORT number to use to connect to the remote VXLAN tunnel endpoint. If omitted the default value is used. </p>
<dt><code>via</code><i> DEVICE</i></p>
<dd>device name of the outgoing interface for the VXLAN device driver to reach the remote VXLAN tunnel endpoint. </p>
<dt><code>nhid</code><i> NHID </i></p>
<dd>ecmp nexthop group for the VXLAN device driver to reach remote VXLAN tunnel endpoints. </p>
</dl>
<h3>bridge fdb append &#8211; append a forwarding database entry</h3>
<p>This command adds a new fdb entry with an already known <i>LLADDR</i>. Valid only for multicast link layer addresses. The command adds support for broadcast and multicast Ethernet MAC addresses. The Ethernet MAC address is added multiple times into the forwarding database and the vxlan device driver sends a copy of the data packet to each entry found. </p>
<p> The arguments are the same as with <code>bridge fdb add</code>.</p>
<h3>bridge fdb delete &#8211; delete a forwarding database entry</h3>
<p>This command removes an existing fdb entry. </p>
<p> The arguments are the same as with <code>bridge fdb add</code>.</p>
<h3>bridge fdb replace &#8211; replace a forwarding database entry</h3>
<p>If no matching entry is found, a new one will be created instead. </p>
<p> The arguments are the same as with <code>bridge fdb add</code>.</p>
<h3>bridge fdb show &#8211; list forwarding entries.</h3>
<p>This command displays the current forwarding table. </p>
<p> With the <code>-statistics</code> option, the command becomes verbose. It prints out the last updated and last used time for each entry.</p>
<h3>bridge fdb get &#8211; get bridge forwarding entry.</h3>
<p>lookup a bridge forwarding table entry. </p>
<dl>
<dt><code>LLADDR</code></p>
<dd>the Ethernet MAC address. </p>
<dt><code>dev</code><i> DEV</i></p>
<dd>the interface to which this address is associated. </p>
<dt><code>brport</code><i> DEV</i></p>
<dd>the bridge port to which this address is associated. same as dev above. </p>
<dt><code>br</code><i> DEV</i></p>
<dd>the bridge to which this address is associated. </p>
<dt><code>self</code></p>
<dd>&#8211; the address is associated with the port drivers fdb. Usually hardware. </p>
<dt><code>master</code></p>
<dd>&#8211; the address is associated with master devices fdb. Usually software (default). </p>
</dl>
<h2>bridge mdb &#8211; multicast group database management</h2>
<p><code>mdb</code> objects contain known IP or L2 multicast group addresses on a link. </p>
<p> The corresponding commands display mdb entries, add new entries, and delete old ones.</p>
<h3>bridge mdb add &#8211; add a new multicast group database entry</h3>
<p>This command creates a new mdb entry. </p>
<dl>
<dt><code>dev</code><i> DEV</i></p>
<dd>the interface where this group address is associated. </p>
<dt><code>port</code><i> PORT</i></p>
<dd>the port whose link is known to have members of this multicast group. </p>
<dt><code>grp</code><i> GROUP</i></p>
<dd>the multicast group address (IPv4, IPv6 or L2 multicast) whose members reside on the link connected to the port. </p>
<p> <code>permanent</code> &#8211; the mdb entry is permanent. Optional for IPv4 and IPv6, mandatory for L2. </p>
<p> <code>temp</code> &#8211; the mdb entry is temporary (default) </p>
<dt><code>src</code><i> SOURCE</i></p>
<dd>optional source IP address of a sender for this multicast group. If IGMPv3 for IPv4, or MLDv2 for IPv6 respectively, are enabled it will be included in the lookup when forwarding multicast traffic. </p>
<dt><code>vid</code><i> VID</i></p>
<dd>the VLAN ID which is known to have members of this multicast group. </p>
</dl>
<h3>bridge mdb delete &#8211; delete a multicast group database entry</h3>
<p>This command removes an existing mdb entry. </p>
<p> The arguments are the same as with <code>bridge mdb add</code>.</p>
<h3>bridge mdb show &#8211; list multicast group database entries</h3>
<p>This command displays the current multicast group membership table. The table is populated by IGMP and MLD snooping in the bridge driver automatically. It can be altered by <code>bridge mdb add</code> and <code>bridge mdb del</code> commands manually too. </p>
<dl>
<dt><code>dev</code><i> DEV</i></p>
<dd>the interface only whose entries should be listed. Default is to list all bridge interfaces. </p>
</dl>
<p> With the <code>-details</code> option, the command becomes verbose. It prints out the ports known to have a connected router. </p>
<p> With the <code>-statistics</code> option, the command displays timer values for mdb and router port entries.</p>
<h2>bridge vlan &#8211; VLAN filter list</h2>
<p><code>vlan</code> objects contain known VLAN IDs for a link. </p>
<p> The corresponding commands display vlan filter entries, add new entries, and delete old ones.</p>
<h3>bridge vlan add &#8211; add a new vlan filter entry</h3>
<p>This command creates a new vlan filter entry. </p>
<dl>
<dt><code>dev</code><i> NAME</i></p>
<dd>the interface with which this vlan is associated. </p>
<dt><code>vid</code><i> VID</i></p>
<dd>the VLAN ID that identifies the vlan. </p>
<dt><code>tunnel_info</code><i> TUNNEL_ID</i></p>
<dd>the TUNNEL ID that maps to this vlan. The tunnel id is set in dst_metadata for every packet that belongs to this vlan (applicable to bridge ports with vlan_tunnel flag set). </p>
<dt><code>pvid</code></p>
<dd>the vlan specified is to be considered a PVID at ingress. Any untagged frames will be assigned to this VLAN. </p>
<dt><code>untagged</code></p>
<dd>the vlan specified is to be treated as untagged on egress. </p>
<dt><code>self</code></p>
<dd>the vlan is configured on the specified physical device. Required if the device is the bridge device. </p>
<dt><code>master</code></p>
<dd>the vlan is configured on the software bridge (default). </p>
</dl>
<h3>bridge vlan delete &#8211; delete a vlan filter entry</h3>
<p>This command removes an existing vlan filter entry. </p>
<p> The arguments are the same as with <code>bridge vlan add.</code> The <code>pvid </code>and<code> untagged</code> flags are ignored.</p>
<h3>bridge vlan set &#8211; change vlan filter entry&#8217;s options</h3>
<p>This command changes vlan filter entry&#8217;s options. </p>
<dl>
<dt><code>dev</code><i> NAME</i></p>
<dd>the interface with which this vlan is associated. </p>
<dt><code>vid</code><i> VID</i></p>
<dd>the VLAN ID that identifies the vlan. </p>
<dt><code>state</code><i> STP_STATE </i></p>
<dd>the operation state of the vlan. One may enter STP state name (case insensitive), or one of the numbers below. Negative inputs are ignored, and unrecognized names return an error. Note that the state is set only for the vlan of the specified device, e.g. if it is a bridge port then the state will be set only for the vlan of the port. </p>
<p> <code>0</code> &#8211; vlan is in STP <code>DISABLED</code> state. Make this vlan completely inactive for STP. This is also called BPDU filter and could be used to disable STP on an untrusted vlan. </p>
<p> <code>1</code> &#8211; vlan is in STP <code>LISTENING</code> state. Only valid if STP is enabled on the bridge. In this state the vlan listens for STP BPDUs and drops all other traffic frames. </p>
<p> <code>2</code> &#8211; vlan is in STP <code>LEARNING</code> state. Only valid if STP is enabled on the bridge. In this state the vlan will accept traffic only for the purpose of updating MAC address tables. </p>
<p> <code>3</code> &#8211; vlan is in STP <code>FORWARDING</code> state. This is the default vlan state. </p>
<p> <code>4</code> &#8211; vlan is in STP <code>BLOCKING</code> state. Only valid if STP is enabled on the bridge. This state is used during the STP election process. In this state, the vlan will only process STP BPDUs. </p>
</dl>
<h3>bridge vlan show &#8211; list vlan configuration.</h3>
<p>This command displays the current VLAN filter table. </p>
<p> With the <code>-details</code> option, the command becomes verbose. It displays the per-vlan options. </p>
<p> With the <code>-statistics</code> option, the command displays per-vlan traffic statistics.</p>
<h3>bridge vlan tunnelshow &#8211; list vlan tunnel mapping.</h3>
<p>This command displays the current vlan tunnel info mapping.</p>
<h2>bridge monitor &#8211; state monitoring</h2>
<p>The <code>bridge</code> utility can monitor the state of devices and addresses continuously. This option has a slightly different format. Namely, the <code>monitor</code> command is the first in the command line and then the object list follows: </p>
<p> <code>bridge monitor</code> [ <code>all</code> | <i>OBJECT-LIST</i> ] </p>
<p> <i>OBJECT-LIST</i> is the list of object types that we want to monitor. It may contain <code>link</code>, <code>fdb</code>, <code>vlan</code> and <code>mdb</code>. If no <code>file</code> argument is given, <code>bridge</code> opens RTNETLINK, listens on it and dumps state changes in the format described in previous sections. </p>
<p> If a file name is given, it does not listen on RTNETLINK, but opens the file containing RTNETLINK messages saved in binary format and dumps them.</p>
<h2>Notes</h2>
<p>This command uses facilities added in Linux 3.0. Although the forwarding table is maintained on a per-bridge device basis the bridge device is not part of the syntax. This is a limitation of the underlying netlink neighbour message protocol. When displaying the forwarding table, entries for all bridges are displayed. Add/delete/modify commands determine the underlying bridge device based on the bridge to which the corresponding ethernet device is attached. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Bugs</h2>
<p>Please direct bugreports and patches to: <code>&lt;netdev [at] vger.kernel.org&gt;</code> </p>
<h2>Author</h2>
<p>Original Manpage by Stephen Hemminger</p>
