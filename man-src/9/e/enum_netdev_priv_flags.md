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
<dd>802.1Q VLAN device</dd></dl>
<p> IFF_EBRIDGE</p>
<dl>
<dd>Ethernet bridging device</dd></dl>
<p> IFF_BONDING</p>
<dl>
<dd>bonding master or slave</dd></dl>
<p> IFF_ISATAP</p>
<dl>
<dd>ISATAP interface (RFC4214)</dd></dl>
<p> IFF_WAN_HDLC</p>
<dl>
<dd>WAN HDLC device</dd></dl>
<p> IFF_XMIT_DST_RELEASE</p>
<dl>
<dd><code>dev_hard_start_xmit</code> is allowed to release skb-&gt;dst</dd></dl>
<p> IFF_DONT_BRIDGE</p>
<dl>
<dd>disallow bridging this ether dev</dd></dl>
<p> IFF_DISABLE_NETPOLL</p>
<dl>
<dd>disable netpoll at run-time</dd></dl>
<p> IFF_MACVLAN_PORT</p>
<dl>
<dd>device used as macvlan port</dd></dl>
<p> IFF_BRIDGE_PORT</p>
<dl>
<dd>device used as bridge port</dd></dl>
<p> IFF_OVS_DATAPATH</p>
<dl>
<dd>device used as Open vSwitch datapath port</dd></dl>
<p> IFF_TX_SKB_SHARING</p>
<dl>
<dd>The interface supports sharing skbs on transmit</dd></dl>
<p> IFF_UNICAST_FLT</p>
<dl>
<dd>Supports unicast filtering</dd></dl>
<p> IFF_TEAM_PORT</p>
<dl>
<dd>device used as team port</dd></dl>
<p> IFF_SUPP_NOFCS</p>
<dl>
<dd>device supports sending custom FCS</dd></dl>
<p> IFF_LIVE_ADDR_CHANGE</p>
<dl>
<dd>device supports hardware address change when it&#8217;s running</dd></dl>
<p> IFF_MACVLAN</p>
<dl>
<dd>Macvlan device</dd></dl>
<p> IFF_XMIT_DST_RELEASE_PERM</p>
<dl>
<dd>IFF_XMIT_DST_RELEASE not taking into account underlying stacked devices</dd></dl>
<p> IFF_IPVLAN_MASTER</p>
<dl>
<dd>IPvlan master device</dd></dl>
<p> IFF_IPVLAN_SLAVE</p>
<dl>
<dd>IPvlan slave device</dd></dl>
<p> IFF_L3MDEV_MASTER</p>
<dl>
<dd>device is an L3 master device</dd></dl>
<p> IFF_NO_QUEUE</p>
<dl>
<dd>device can run without qdisc attached</dd></dl>
<p> IFF_OPENVSWITCH</p>
<dl>
<dd>device is a Open vSwitch master</dd></dl>
<p> IFF_L3MDEV_SLAVE</p>
<dl>
<dd>device is enslaved to an L3 master device</dd></dl>
<p> IFF_TEAM</p>
<dl>
<dd>device is a team device</dd></dl>
<p> IFF_RXFH_CONFIGURED</p>
<dl>
<dd>device has had Rx Flow indirection table configured</dd></dl>
<p> IFF_PHONY_HEADROOM</p>
<dl>
<dd>the headroom value is controlled by an external entity (i.e. the master device for bridged veth)</dd></dl>
<p> IFF_MACSEC</p>
<dl>
<dd>device is a MACsec device</dd></dl>
<h2>Description</h2>
<p>These are the struct net_device, they are only set internally by drivers and used in the kernel. These flags are invisible to userspace; this means that the order of these flags can change during any kernel release. </p>
<p> You should have a pretty good reason to be extending these flags.</p>
<h2>Copyright</h2>
