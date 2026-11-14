---
title: "enum_netdev_priv_flags(9)"
name: "enum_netdev_priv_flags"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_netdev_priv_flags/"
description: "enum_netdev_priv_flags – struct net_device priv_flags"
---

<p>enum_netdev_priv_flags &#8211; struct net_device priv_flags</p>
<h2>Synopsis</h2>
<pre>enum netdev_priv_flags {
 IFF_802_1Q_VLAN,
 IFF_EBRIDGE,
 IFF_BONDING,
 IFF_ISATAP,
 IFF_WAN_HDLC,
 IFF_XMIT_DST_RELEASE,
 IFF_DONT_BRIDGE,
 IFF_DISABLE_NETPOLL,
 IFF_MACVLAN_PORT,
 IFF_BRIDGE_PORT,
 IFF_OVS_DATAPATH,
 IFF_TX_SKB_SHARING,
 IFF_UNICAST_FLT,
 IFF_TEAM_PORT,
 IFF_SUPP_NOFCS,
 IFF_LIVE_ADDR_CHANGE,
 IFF_MACVLAN,
 IFF_XMIT_DST_RELEASE_PERM,
 IFF_IPVLAN_MASTER,
 IFF_IPVLAN_SLAVE,
 IFF_L3MDEV_MASTER,
 IFF_NO_QUEUE,
 IFF_OPENVSWITCH,
 IFF_L3MDEV_SLAVE,
 IFF_TEAM,
 IFF_RXFH_CONFIGURED,
 IFF_PHONY_HEADROOM,
 IFF_MACSEC
}; </pre>
<h2>Constants</h2>
<p>IFF_802_1Q_VLAN</p>
<dl>
<dd>802.1Q VLAN device</dl>
<p> IFF_EBRIDGE</p>
<dl>
<dd>Ethernet bridging device</dl>
<p> IFF_BONDING</p>
<dl>
<dd>bonding master or slave</dl>
<p> IFF_ISATAP</p>
<dl>
<dd>ISATAP interface (RFC4214)</dl>
<p> IFF_WAN_HDLC</p>
<dl>
<dd>WAN HDLC device</dl>
<p> IFF_XMIT_DST_RELEASE</p>
<dl>
<dd><code>dev_hard_start_xmit</code> is allowed to release skb-&gt;dst</dl>
<p> IFF_DONT_BRIDGE</p>
<dl>
<dd>disallow bridging this ether dev</dl>
<p> IFF_DISABLE_NETPOLL</p>
<dl>
<dd>disable netpoll at run-time</dl>
<p> IFF_MACVLAN_PORT</p>
<dl>
<dd>device used as macvlan port</dl>
<p> IFF_BRIDGE_PORT</p>
<dl>
<dd>device used as bridge port</dl>
<p> IFF_OVS_DATAPATH</p>
<dl>
<dd>device used as Open vSwitch datapath port</dl>
<p> IFF_TX_SKB_SHARING</p>
<dl>
<dd>The interface supports sharing skbs on transmit</dl>
<p> IFF_UNICAST_FLT</p>
<dl>
<dd>Supports unicast filtering</dl>
<p> IFF_TEAM_PORT</p>
<dl>
<dd>device used as team port</dl>
<p> IFF_SUPP_NOFCS</p>
<dl>
<dd>device supports sending custom FCS</dl>
<p> IFF_LIVE_ADDR_CHANGE</p>
<dl>
<dd>device supports hardware address change when it&#8217;s running</dl>
<p> IFF_MACVLAN</p>
<dl>
<dd>Macvlan device</dl>
<p> IFF_XMIT_DST_RELEASE_PERM</p>
<dl>
<dd>IFF_XMIT_DST_RELEASE not taking into account underlying stacked devices</dl>
<p> IFF_IPVLAN_MASTER</p>
<dl>
<dd>IPvlan master device</dl>
<p> IFF_IPVLAN_SLAVE</p>
<dl>
<dd>IPvlan slave device</dl>
<p> IFF_L3MDEV_MASTER</p>
<dl>
<dd>device is an L3 master device</dl>
<p> IFF_NO_QUEUE</p>
<dl>
<dd>device can run without qdisc attached</dl>
<p> IFF_OPENVSWITCH</p>
<dl>
<dd>device is a Open vSwitch master</dl>
<p> IFF_L3MDEV_SLAVE</p>
<dl>
<dd>device is enslaved to an L3 master device</dl>
<p> IFF_TEAM</p>
<dl>
<dd>device is a team device</dl>
<p> IFF_RXFH_CONFIGURED</p>
<dl>
<dd>device has had Rx Flow indirection table configured</dl>
<p> IFF_PHONY_HEADROOM</p>
<dl>
<dd>the headroom value is controlled by an external entity (i.e. the master device for bridged veth)</dl>
<p> IFF_MACSEC</p>
<dl>
<dd>device is a MACsec device</dl>
<h2>Description</h2>
<p>These are the struct net_device, they are only set internally by drivers and used in the kernel. These flags are invisible to userspace; this means that the order of these flags can change during any kernel release. </p>
<p> You should have a pretty good reason to be extending these flags.</p>
<h2>Copyright</h2>
