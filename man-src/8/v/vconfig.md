---
title: "vconfig(8)"
name: "vconfig"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vconfig/"
description: "vconfig – VLAN (802.1q) configuration program."
---

<p>vconfig &#8211; VLAN (802.1q) configuration program.</p>
<h2>Synopsis</h2>
<p><code>vconfig</code> <i>[lots of long options]</i></p>
<h2>Description</h2>
<p>The <code>vconfig</code> program allows you to create and remove vlan-devices on a vlan enabled kernel. Vlan-devices are virtual ethernet devices which represents the virtual lans on the physical lan.</p>
<h2>Options</h2>
<dl>
<dt><code>add [interface-name] [vlan-id]</code></p>
<dd>Creates a vlan-device on [interface-name]. The resulting vlan-device will be called according to the nameing convention set.</p>
<dt><code>rem [vlan-device]</code></p>
<dd>Removes the named vlan-device.</p>
<dt><code>set_flag [vlan-device] 0 | 1</code></p>
<dd>When 1, ethernet header reorders are turned on. Dumping the device will appear as a common ethernet device without vlans. When 0(default) however, ethernet headers are not reordered, which results in vlan tagged packets when dumping the device. Usually the default gives no problems, but some packet filtering programs might have problems with it.</p>
<dd><code>set_egress_map [vlan-device] [skb-priority] [vlan-qos]</code> This flags that outbound packets with a particular skb-priority should be tagged with the particular vlan priority vlan-qos. The default vlan priority is 0.</p>
<dd><code>set_ingress_map [vlan-device] [skb-priority] [vlan-qos]</code> This flags that inbound packets with the particular vlan priority vlan-qos should be queued with a particular skb-priority. The default skb-priority is 0.</p>
<dd><code>set_name_type VLAN_PLUS_VID | VLAN_PLUS_VID_NO_PAD | DEV_PLUS_VID | DEV_PLUS_VID_NO_PAD</code> Sets the way vlan-device names are created. Use vconfig without arguments to see the different formats.</p>
<dd></dl>
<h2>Notes</h2>
<p>VLAN will use Broadcom&#8217;s NICE interface when the network device supports it. This is necessary, since usually the hardware of these devices already removes the vlan tag from the ethernet packet. The set_flag option on vlan-devices created on such a physical network device will be ignored. Dumping the network-device will show only untagged(non-vlan) traffic, and dumping the vlan-devices will only show traffic intended for that vlan, without the tags.</p>
<h2>Files</h2>
<p><i>/proc/net/vlan/config</i><br />
 <i>/proc/net/vlan/[vlan-device]</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ip/">ip</a>(8), <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)</p>
<h2>Authors</h2>
<p>This manual page was written by Ard van Breemen &lt;ard [at] kwaak.net&gt;<br />
 The vlan patch is written by Ben Greear &lt;greearb [at] candelatech.com&gt;</p>
