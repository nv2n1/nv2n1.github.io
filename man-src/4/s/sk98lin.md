---
title: "sk98lin(4)"
name: "sk98lin"
section: "4"
letter: "s"
url: "/docs/linux/man/4-sk98lin/"
description: "sk98lin – Marvell/SysKonnect Gigabit Ethernet driver v6.21"
---

<p>sk98lin &#8211; Marvell/SysKonnect Gigabit Ethernet driver v6.21</p>
<h2>Synopsis</h2>
<p><code>insmod sk98lin.o</code> [<code>Speed_A=</code><i>i,j,&#8230;</i>] [<code>Speed_B=</code><i>i,j,&#8230;</i>] [<code>AutoNeg_A=</code><i>i,j,&#8230;</i>] [<code>AutoNeg_B=</code><i>i,j,&#8230;</i>] [<code>DupCap_A=</code><i>i,j,&#8230;</i>] [<code>DupCap_B=</code><i>i,j,&#8230;</i>] [<code>FlowCtrl_A=</code><i>i,j,&#8230;</i>] [<code>FlowCtrl_B=</code><i>i,j,&#8230;</i>] [<code>Role_A=</code><i>i,j,&#8230;</i>] [<code>Role_B=</code><i>i,j,&#8230;</i>] [<code>ConType=</code><i>i,j,&#8230;</i>] [<code>Moderation=</code><i>i,j,&#8230;</i>] [<code>IntsPerSec=</code><i>i,j,&#8230;</i>] [<code>PrefPort=</code><i>i,j,&#8230;</i>] [<code>RlmtMode=</code><i>i,j,&#8230;</i>]</p>
<h2>Description</h2>
<p><code>Note</code>: This obsolete driver was removed from the kernel in version 2.6.26. <code>sk98lin</code> is the Gigabit Ethernet driver for Marvell and SysKonnect network adapter cards. It supports SysKonnect SK-98xx/SK-95xx compliant Gigabit Ethernet Adapter and any Yukon compliant chipset. When loading the driver using insmod, parameters for the network adapter cards might be stated as a sequence of comma separated commands. If for instance two network adapters are installed and AutoNegotiation on Port A of the first adapter should be ON, but on the Port A of the second adapter switched OFF, one must enter: </p>
<pre><code>insmod sk98lin.o AutoNeg_A=On,Off</code></pre>
<p> After <code>sk98lin</code> is bound to one or more adapter cards and the <i>/proc</i> file system is mounted on your system, a dedicated statistics file will be created in folder <i>/proc/net/sk98lin</i> for all ports of the installed network adapter cards. Those files are named <i>eth[x]</i> whereas <i>x</i> is the number of the interface that has been assigned to a dedicated port by the system. If loading is finished, any desired IP address can be assigned to the respective <i>eth[x]</i> interface using the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command. This causes the adapter to connect to the Ethernet and to display a status message on the console saying &quot;ethx: network connection up using port y&quot; followed by the configured or detected connection parameters. The <code>sk98lin</code> also supports large frames (also called jumbo frames). Using jumbo frames can improve throughput tremendously when transferring large amounts of data. To enable large frames, the MTU (maximum transfer unit) size for an interface is to be set to a high value. The default MTU size is 1500 and can be changed up to 9000 (bytes). Setting the MTU size can be done when assigning the IP address to the interface or later by using the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command with the mtu parameter. If for instance eth0 needs an IP address and a large frame MTU size, the following two commands might be used:<br />
&nbsp;<wbr>ifconfig eth0 10.1.1.1<br />
&nbsp;<wbr>ifconfig eth0 mtu 9000 Those two commands might even be combined into one:<br />
&nbsp;<wbr>ifconfig eth0 10.1.1.1 mtu 9000 Note that large frames can be used only if permitted by your network infrastructure. This means, that any switch being used in your Ethernet must also support large frames. Quite some switches support large frames, but need to be configured to do so. Most of the times, their default setting is to support only standard frames with an MTU size of 1500 (bytes). In addition to the switches inside the network, all network adapters that are to be used must also be enabled regarding jumbo frames. If an adapter is not set to receive large frames it will simply drop them. Switching back to the standard Ethernet frame size can be done by using the <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) command again:<br />
&nbsp;<wbr>ifconfig eth0 mtu 1500 The Marvell/SysKonnect Gigabit Ethernet driver for Linux is able to support VLAN and Link Aggregation according to IEEE standards 802.1, 802.1q, and 802.3ad. Those features are available only after installation of open source modules which can be found on the Internet: <i>VLAN</i>:<br />
 <i>Link</i> <i>Aggregation</i>:<br />
 Note that Marvell/SysKonnect does not offer any support for these open source modules and does not take the responsibility for any kind of failures or problems arising when using these modules.</p>
<h3>Parameters</h3>
<dl>
<dt><code>Speed_A=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is used to set the speed capabilities of port A of an adapter card. It is valid only for Yukon copper adapters. Possible values are: <i>10</i>, <i>100</i>, <i>1000</i> or <i>Auto</i> whereas <i>Auto</i> is the default. Usually, the speed is negotiated between the two ports during link establishment. If this fails, a port can be forced to a specific setting with this parameter.</p>
<dt><code>Speed_B=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is used to set the speed capabilities of port B of an adapter card. It is valid only for Yukon copper adapters. Possible values are: <i>10</i>, <i>100</i>, <i>1000</i> or <i>Auto</i> whereas <i>Auto</i> is the default. Usually, the speed is negotiated between the two ports during link establishment. If this fails, a port can be forced to a specific setting with this parameter.</p>
<dt><code>AutoNeg_A=</code><i>i,j,&#8230;</i></p>
<dd>Enables or disables the use of autonegotiation of port A of an adapter card. Possible values are: <i>On</i>, <i>Off</i> or <i>Sense</i> whereas <i>On</i> is the default. The <i>Sense</i> mode automatically detects whether the link partner supports auto-negotiation or not.</p>
<dt><code>AutoNeg_B=</code><i>i,j,&#8230;</i></p>
<dd>Enables or disables the use of autonegotiation of port B of an adapter card. Possible values are: <i>On</i>, <i>Off</i> or <i>Sense</i> whereas <i>On</i> is the default. The <i>Sense</i> mode automatically detects whether the link partner supports auto-negotiation or not.</p>
<dt><code>DupCap_A=</code><i>i,j,&#8230;</i></p>
<dd>This parameter indicates the duplex mode to be used for port A of an adapter card. Possible values are: <i>Half</i>, <i>Full</i> or <i>Both</i> whereas <i>Both</i> is the default. This parameter is relevant only if AutoNeg_A of port A is not set to <i>Sense</i>. If AutoNeg_A is set to <i>On</i>, all three values of DupCap_A ( <i>Half</i>, <i>Full</i> or <i>Both</i>) might be stated. If AutoNeg_A is set to <i>Off</i>, only DupCap_A values <i>Full</i> and <i>Half</i> are allowed. This DupCap_A parameter is useful if your link partner does not support all possible duplex combinations.</p>
<dt><code>DupCap_B=</code><i>i,j,&#8230;</i></p>
<dd>This parameter indicates the duplex mode to be used for port B of an adapter card. Possible values are: <i>Half</i>, <i>Full</i> or <i>Both</i> whereas <i>Both</i> is the default. This parameter is relevant only if AutoNeg_B of port B is not set to <i>Sense</i>. If AutoNeg_B is set to <i>On</i>, all three values of DupCap_B ( <i>Half</i>, <i>Full</i> or <i>Both</i>) might be stated. If AutoNeg_B is set to <i>Off</i>, only DupCap_B values <i>Full</i> and <i>Half</i> are allowed. This DupCap_B parameter is useful if your link partner does not support all possible duplex combinations.</p>
<dt><code>FlowCtrl_A=</code><i>i,j,&#8230;</i></p>
<dd>This parameter can be used to set the flow control capabilities the port reports during auto-negotiation. Possible values are: <i>Sym</i>, <i>SymOrRem</i>, <i>LocSend</i> or <i>None</i> whereas <i>SymOrRem</i> is the default. The different modes have the following meaning: </p>
<pre><code>Sym

= Symmetric

both link partners are allowed to send PAUSE frames

SymOrRem

= SymmetricOrRemote

both or only remote partner are allowed to send PAUSE frames

LocSend

= LocalSend

only local link partner is allowed to send PAUSE frames

None

= None

no link partner is allowed to send PAUSE frames</code></pre>
<p> Note that this parameter is ignored if AutoNeg_A is set to <i>Off</i>.</p>
<dt><code>FlowCtrl_B=</code><i>i,j,&#8230;</i></p>
<dd>This parameter can be used to set the flow control capabilities the port reports during auto-negotiation. Possible values are: <i>Sym</i>, <i>SymOrRem</i>, <i>LocSend</i> or <i>None</i> whereas <i>SymOrRem</i> is the default. The different modes have the following meaning: <i>Sym</i> = Symmetric<br />
&nbsp;<wbr>both link partners are allowed to send PAUSE frames<br />
 <i>SymOrRem</i> = SymmetricOrRemote<br />
&nbsp;<wbr>both or only remote partner are allowed to send PAUSE frames<br />
 <i>LocSend</i> = LocalSend<br />
&nbsp;<wbr>only local link partner is allowed to send PAUSE frames<br />
 <i>None</i> = None<br />
&nbsp;<wbr>no link partner is allowed to send PAUSE frames<br />
 Note that this parameter is ignored if AutoNeg_B is set to <i>Off</i>.</p>
<dt><code>Role_A=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is valid only for 1000Base-T adapter cards. For two 1000Base-T ports to communicate, one must take the role of the master (providing timing information), while the other must be the slave. Possible values are: <i>Auto</i>, <i>Master</i> or <i>Slave</i> whereas <i>Auto</i> is the default. Usually, the role of a port is negotiated between two ports during link establishment, but if that fails the port A of an adapter card can be forced to a specific setting with this parameter.</p>
<dt><code>Role_B=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is valid only for 1000Base-T adapter cards. For two 1000Base-T ports to communicate, one must take the role of the master (providing timing information), while the other must be the slave. Possible values are: <i>Auto</i>, <i>Master</i> or <i>Slave</i> whereas <i>Auto</i> is the default. Usually, the role of a port is negotiated between two ports during link establishment, but if that fails the port B of an adapter card can be forced to a specific setting with this parameter.</p>
<dt><code>ConType=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is a combination of all five per-port parameters within one single parameter. This simplifies the configuration of both ports of an adapter card. The different values of this variable reflect the most meaningful combinations of port parameters. Possible values and their corresponding combination of per-port parameters: </p>
<pre>ConType | DupCap AutoNeg FlowCtrl Role Speed
--------+-------------------------------------------
<i>Auto</i> | Both On SymOrRem Auto Auto
<br>
<i>100FD</i> | Full Off None Auto 100
<br>
<i>100HD</i> | Half Off None Auto 100
<br>
<i>10FD</i> | Full Off None Auto 10
<br>
<i>10HD</i> | Half Off None Auto 10</pre>
<p>Stating any other port parameter together with this <i>ConType</i> parameter will result in a merged configuration of those settings. This is due to the fact, that the per-port parameters (e.g., <i>Speed_A</i>) have a higher priority than the combined variable <i>ConType</i>.</p>
<dt><code>Moderation=</code><i>i,j,&#8230;</i></p>
<dd>Interrupt moderation is employed to limit the maximum number of interrupts the driver has to serve. That is, one or more interrupts (which indicate any transmit or receive packet to be processed) are queued until the driver processes them. When queued interrupts are to be served, is determined by the <i>IntsPerSec</i> parameter, which is explained later below. Possible moderation modes are: <i>None</i>, <i>Static</i> or <i>Dynamic</i> whereas <i>None</i> is the default. The different modes have the following meaning: <i>None</i> No interrupt moderation is applied on the adapter card. Therefore, each transmit or receive interrupt is served immediately as soon as it appears on the interrupt line of the adapter card.<br />
 <i>Static</i> Interrupt moderation is applied on the adapter card. All transmit and receive interrupts are queued until a complete moderation interval ends. If such a moderation interval ends, all queued interrupts are processed in one big bunch without any delay. The term <i>Static</i> reflects the fact, that interrupt moderation is always enabled, regardless how much network load is currently passing via a particular interface. In addition, the duration of the moderation interval has a fixed length that never changes while the driver is operational.<br />
 <i>Dynamic</i> Interrupt moderation might be applied on the adapter card, depending on the load of the system. If the driver detects that the system load is too high, the driver tries to shield the system against too much network load by enabling interrupt moderation. If&#8212;at a later time&#8212;the CPU utilization decreases again (or if the network load is negligible) the interrupt moderation will automatically be disabled. Interrupt moderation should be used when the driver has to handle one or more interfaces with a high network load, which&#8212;as a consequence&#8212;leads also to a high CPU utilization. When moderation is applied in such high network load situations, CPU load might be reduced by 20-30% on slow computers. Note that the drawback of using interrupt moderation is an increase of the round-trip-time (RTT), due to the queuing and serving of interrupts at dedicated moderation times.</p>
<dt><code>IntsPerSec=</code><i>i,j,&#8230;</i></p>
<dd>This parameter determines the length of any interrupt moderation interval. Assuming that static interrupt moderation is to be used, an <i>IntsPerSec</i> parameter value of 2000 will lead to an interrupt moderation interval of 500 microseconds. Possible values for this parameter are in the range of 30&#8230;40000 (interrupts per second). The default value is 2000. This parameter is used only if either static or dynamic interrupt moderation is enabled on a network adapter card. This parameter is ignored if no moderation is applied. Note that the duration of the moderation interval is to be chosen with care. At first glance, selecting a very long duration (e.g., only 100 interrupts per second) seems to be meaningful, but the increase of packet-processing delay is tremendous. On the other hand, selecting a very short moderation time might compensate the use of any moderation being applied.</p>
<dt><code>PrefPort=</code><i>i,j,&#8230;</i></p>
<dd>This parameter is used to force the preferred port to A or B (on dual-port network adapters). The preferred port is the one that is used if both ports A and B are detected as fully functional. Possible values are: <i>A</i> or <i>B</i> whereas <i>A</i> is the default.</p>
<dt><code>RlmtMode=</code><i>i,j,&#8230;</i></p>
<dd>RLMT monitors the status of the port. If the link of the active port fails, RLMT switches immediately to the standby link. The virtual link is maintained as long as at least one &quot;physical&quot; link is up. This parameters states how RLMT should monitor both ports. Possible values are: <i>CheckLinkState</i>, <i>CheckLocalPort</i>, <i>CheckSeg</i> or <i>DualNet</i> whereas <i>CheckLinkState</i> is the default. The different modes have the following meaning: <i>CheckLinkState</i> Check link state only: RLMT uses the link state reported by the adapter hardware for each individual port to determine whether a port can be used for all network traffic or not.<br />
 <i>CheckLocalPort</i> In this mode, RLMT monitors the network path between the two ports of an adapter by regularly exchanging packets between them. This mode requires a network configuration in which the two ports are able to &quot;see&quot; each other (i.e., there must not be any router between the ports).<br />
 <i>CheckSeg</i> Check local port and segmentation: This mode supports the same functions as the CheckLocalPort mode and additionally checks network segmentation between the ports. Therefore, this mode is to be used only if Gigabit Ethernet switches are installed on the network that have been configured to use the Spanning Tree protocol.<br />
 <i>DualNet</i> In this mode, ports A and B are used as separate devices. If you have a dual port adapter, port A will be configured as <i>eth[x]</i> and port B as <i>eth[x+1]</i>. Both ports can be used independently with distinct IP addresses. The preferred port setting is not used. RLMT is turned off. Note that RLMT modes <i>CheckLocalPort</i> and <i>CheckLinkState</i> are designed to operate in configurations where a network path between the ports on one adapter exists. Moreover, they are not designed to work where adapters are connected back-to-back.</dl>
<h2>Files</h2>
<dl>
<dt><i>/proc/net/sk98lin/eth[x]</i></p>
<dd>The statistics file of a particular interface of an adapter card. It contains generic information about the adapter card plus a detailed summary of all transmit and receive counters.</p>
<dt><i>/usr/src/linux/Documentation/networking/sk98lin.txt</i></p>
<dd>This is the <i>README</i> file of the <i>sk98lin</i> driver. It contains a detailed installation HOWTO and describes all parameters of the driver. It denotes also common problems and provides the solution to them.</dl>
<h2>Bugs</h2>
<p>Report any bugs to linux [at] syskonnect.de</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
