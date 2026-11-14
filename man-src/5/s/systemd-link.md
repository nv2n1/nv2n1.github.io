---
title: "systemd-link(5)"
name: "systemd-link"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-link/"
description: "systemd.link – Network device configuration"
---

<p>systemd.link &#8211; Network device configuration</p>
<h2>Synopsis</h2>
<p><i>link</i>.link</p>
<h2>Description</h2>
<p>A plain ini-style text file that encodes configuration for matching network devices, used by <code><a href="/docs/linux/man/8-systemd-udevd/">systemd-udevd</a></code>(8) and in particular its <code>net_setup_link</code> builtin. See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax. </p>
<p> The link files are read from the files located in the system network directory /lib/systemd/network, the volatile runtime network directory /run/systemd/network, and the local administration network directory /etc/systemd/network. Link files must have the extension .link; other extensions are ignored. All link files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority, files in /run/ take precedence over files with the same name in /lib/. This can be used to override a system-supplied link file with a local file if needed. As a special case, an empty file (file size 0) or symlink with the same name pointing to /dev/null disables the configuration file entirely (it is &quot;masked&quot;). </p>
<p> Along with the link file foo.link, a &quot;drop-in&quot; directory foo.link.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be merged in the alphanumeric order and parsed after the main file itself has been parsed. This is useful to alter or add configuration settings, without having to modify the main configuration file. Each drop-in file must have appropriate section headers. </p>
<p> In addition to /etc/systemd/network, drop-in &quot;.d&quot; directories can be placed in /lib/systemd/network or /run/systemd/network directories. Drop-in files in /etc/ take precedence over those in /run/ which in turn take precedence over those in /lib/. Drop-in files under any of these directories take precedence over the main link file wherever located. </p>
<p> The link file contains a [Match] section, which determines if a given link file may be applied to a given device, as well as a [Link] section specifying how the device should be configured. The first (in lexical order) of the link files that matches a given device is applied. Note that a default file 99-default.link is shipped by the system. Any user-supplied .link should hence have a lexically earlier name to be considered at all. </p>
<p> See <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8) for diagnosing problems with .link files.</p>
<h2>[Match] Section Options</h2>
<p>A link file is said to match a device if all matches specified by the [Match] section are satisfied. When a link file does not contain valid settings in [Match] section, then the file will match all devices and <code>systemd-udevd</code> warns about that. Hint: to avoid the warning and to make it clear that all interfaces shall be matched, add the following: </p>
<dl>
<dd>
<pre>OriginalName=*</pre>
</dl>
<p> The following keys are accepted: </p>
<p> <i>MACAddress=</i></p>
<dl>
<dd>A whitespace-separated list of hardware addresses. Use full colon-, hyphen- or dot-delimited hexadecimal. See the example below. This option may appear more than once, in which case the lists are merged. If the empty string is assigned to this option, the list of hardware addresses defined prior to this is reset. </p>
<p> Example: </p>
<dl>
<dd>
<pre>MACAddress=01:23:45:67:89:ab 00-11-22-33-44-55 AABB.CCDD.EEFF</pre>
</dl>
</dl>
<p> <i>PermanentMACAddress=</i></p>
<dl>
<dd>A whitespace-separated list of hardware&#8217;s permanent addresses. While <i>MACAddress=</i> matches the device&#8217;s current MAC address, this matches the device&#8217;s permanent MAC address, which may be different from the current one. Use full colon-, hyphen- or dot-delimited hexadecimal. This option may appear more than once, in which case the lists are merged. If the empty string is assigned to this option, the list of hardware addresses defined prior to this is reset.</dl>
<p> <i>Path=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the persistent path, as exposed by the udev property <i>ID_PATH</i>.</dl>
<p> <i>Driver=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the driver currently bound to the device, as exposed by the udev property <i>ID_NET_DRIVER</i> of its parent device, or if that is not set, the driver as exposed by <code>ethtool -i</code> of the device itself. If the list is prefixed with a &quot;!&quot;, the test is inverted.</dl>
<p> <i>Type=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the device type, as exposed by <code>networkctl list</code>. If the list is prefixed with a &quot;!&quot;, the test is inverted. Some valid values are &quot;ether&quot;, &quot;loopback&quot;, &quot;wlan&quot;, &quot;wwan&quot;. Valid types are named either from the udev &quot;DEVTYPE&quot; attribute, or &quot;ARPHRD_&quot; macros in linux/if_arp.h, so this is not comprehensive.</dl>
<p> <i>Property=</i></p>
<dl>
<dd>A whitespace-separated list of udev property names with their values after equals sign (&quot;=&quot;). If multiple properties are specified, the test results are ANDed. If the list is prefixed with a &quot;!&quot;, the test is inverted. If a value contains white spaces, then please quote whole key and value pair. If a value contains quotation, then please escape the quotation with &quot;\&quot;. </p>
<p> Example: if a .link file has the following: </p>
<dl>
<dd>
<pre>Property=ID_MODEL_ID=9999 &quot;ID_VENDOR_FROM_DATABASE=vendor name&quot; &quot;KEY=with \&quot;quotation\&quot;&quot;</pre>
</dl>
<p> then, the .link file matches only when an interface has all the above three properties.</dl>
<p> <i>OriginalName=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the device name, as exposed by the udev property &quot;INTERFACE&quot;. This cannot be used to match on names that have already been changed from userspace. Caution is advised when matching on kernel-assigned names, as they are known to be unstable between reboots.</dl>
<p> <i>Host=</i></p>
<dl>
<dd>Matches against the hostname or machine ID of the host. See <i>ConditionHost=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Virtualization=</i></p>
<dl>
<dd>Checks whether the system is executed in a virtualized environment and optionally test whether it is a specific implementation. See <i>ConditionVirtualization=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>KernelCommandLine=</i></p>
<dl>
<dd>Checks whether a specific kernel command line option is set. See <i>ConditionKernelCommandLine=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>KernelVersion=</i></p>
<dl>
<dd>Checks whether the kernel version (as reported by <code>uname -r</code>) matches a certain expression. See <i>ConditionKernelVersion=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Architecture=</i></p>
<dl>
<dd>Checks whether the system is running on a specific architecture. See <i>ConditionArchitecture=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<p> <i>Firmware=</i></p>
<dl>
<dd>Checks whether the system is running on a machine with the specified firmware. See <i>ConditionFirmware=</i> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for details. When prefixed with an exclamation mark (&quot;!&quot;), the result is negated. If an empty string is assigned, then previously assigned value is cleared.</dl>
<h2>[Link] Section Options</h2>
<p>The [Link] section accepts the following keys: </p>
<p> <i>Description=</i></p>
<dl>
<dd>A description of the device.</dl>
<p> <i>Alias=</i></p>
<dl>
<dd>The <i>ifalias</i> interface property is set to this value.</dl>
<p> <i>MACAddressPolicy=</i></p>
<dl>
<dd>The policy by which the MAC address should be set. The available policies are: </p>
<p> <code>persistent</code></p>
<dl>
<dd>If the hardware has a persistent MAC address, as most hardware should, and if it is used by the kernel, nothing is done. Otherwise, a new MAC address is generated which is guaranteed to be the same on every boot for the given machine and the given device, but which is otherwise random. This feature depends on ID_NET_NAME_* properties to exist for the link. On hardware where these properties are not set, the generation of a persistent MAC address will fail.</dl>
<p> <code>random</code></p>
<dl>
<dd>If the kernel is using a random MAC address, nothing is done. Otherwise, a new address is randomly generated each time the device appears, typically at boot. Either way, the random address will have the &quot;unicast&quot; and &quot;locally administered&quot; bits set.</dl>
<p> <code>none</code></p>
<dl>
<dd>Keeps the MAC address assigned by the kernel. Or use the MAC address specified in <i>MACAddress=</i>.</dl>
<p> An empty string assignment is equivalent to setting &quot;none&quot;.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>The interface MAC address to use. For this setting to take effect, <i>MACAddressPolicy=</i> must either be unset, empty, or &quot;none&quot;.</dl>
<p> <i>NamePolicy=</i></p>
<dl>
<dd>An ordered, space-separated list of policies by which the interface name should be set. <i>NamePolicy=</i> may be disabled by specifying <code>net.ifnames=0</code> on the kernel command line. Each of the policies may fail, and the first successful one is used. The name is not set directly, but is exported to udev as the property <code>ID_NET_NAME</code>, which is, by default, used by a <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), rule to set <i>NAME</i>. The available policies are: </p>
<p> <code>kernel</code></p>
<dl>
<dd>If the kernel claims that the name it has set for a device is predictable, then no renaming is performed.</dl>
<p> <code>database</code></p>
<dl>
<dd>The name is set based on entries in the udev&#8217;s Hardware Database with the key <i>ID_NET_NAME_FROM_DATABASE</i>.</dl>
<p> <code>onboard</code></p>
<dl>
<dd>The name is set based on information given by the firmware for on-board devices, as exported by the udev property <i>ID_NET_NAME_ONBOARD</i>. See <code><a href="/docs/linux/man/7-systemd-net-naming-scheme/">systemd.net-naming-scheme</a></code>(7).</dl>
<p> <code>slot</code></p>
<dl>
<dd>The name is set based on information given by the firmware for hot-plug devices, as exported by the udev property <i>ID_NET_NAME_SLOT</i>. See <code><a href="/docs/linux/man/7-systemd-net-naming-scheme/">systemd.net-naming-scheme</a></code>(7).</dl>
<p> <code>path</code></p>
<dl>
<dd>The name is set based on the device&#8217;s physical location, as exported by the udev property <i>ID_NET_NAME_PATH</i>. See <code><a href="/docs/linux/man/7-systemd-net-naming-scheme/">systemd.net-naming-scheme</a></code>(7).</dl>
<p> <code>mac</code></p>
<dl>
<dd>The name is set based on the device&#8217;s persistent MAC address, as exported by the udev property <i>ID_NET_NAME_MAC</i>. See <code><a href="/docs/linux/man/7-systemd-net-naming-scheme/">systemd.net-naming-scheme</a></code>(7).</dl>
<p> <code>keep</code></p>
<dl>
<dd>If the device already had a name given by userspace (as part of creation of the device or a rename), keep it.</dl>
</dl>
<p> <i>Name=</i></p>
<dl>
<dd>The interface name to use. This option has lower precedence than <i>NamePolicy=</i>, so for this setting to take effect, <i>NamePolicy=</i> must either be unset, empty, disabled, or all policies configured there must fail. Also see the example below with &quot;Name=dmz0&quot;. </p>
<p> Note that specifying a name that the kernel might use for another interface (for example &quot;eth0&quot;) is dangerous because the name assignment done by udev will race with the assignment done by the kernel, and only one interface may use the name. Depending on the order of operations, either udev or the kernel will win, making the naming unpredictable. It is best to use some different prefix, for example &quot;internal0&quot;/&quot;external0&quot; or &quot;lan0&quot;/&quot;lan1&quot;/&quot;lan3&quot;.</dl>
<p> <i>AlternativeNamesPolicy=</i></p>
<dl>
<dd>A space-separated list of policies by which the interface&#8217;s alternative names should be set. Each of the policies may fail, and all successful policies are used. The available policies are &quot;database&quot;, &quot;onboard&quot;, &quot;slot&quot;, &quot;path&quot;, and &quot;mac&quot;. If the kernel does not support the alternative names, then this setting will be ignored.</dl>
<p> <i>AlternativeName=</i></p>
<dl>
<dd>The alternative interface name to use. This option can be specified multiple times. If the empty string is assigned to this option, the list is reset, and all prior assignments have no effect. If the kernel does not support the alternative names, then this setting will be ignored.</dl>
<p> <i>TransmitQueues=</i></p>
<dl>
<dd>Specifies the device&#8217;s number of transmit queues. An integer in the range 1&#8230;4096. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>ReceiveQueues=</i></p>
<dl>
<dd>Specifies the device&#8217;s number of receive queues. An integer in the range 1&#8230;4096. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TransmitQueueLength=</i></p>
<dl>
<dd>Specifies the transmit queue length of the device in number of packets. An unsigned integer in the range 0&#8230;4294967294. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>The maximum transmission unit in bytes to set for the device. The usual suffixes K, M, G are supported and are understood to the base of 1024.</dl>
<p> <i>BitsPerSecond=</i></p>
<dl>
<dd>The speed to set for the device, the value is rounded down to the nearest Mbps. The usual suffixes K, M, G are supported and are understood to the base of 1000.</dl>
<p> <i>Duplex=</i></p>
<dl>
<dd>The duplex mode to set for the device. The accepted values are <code>half</code> and <code>full</code>.</dl>
<p> <i>AutoNegotiation=</i></p>
<dl>
<dd>Takes a boolean. If set to yes, automatic negotiation of transmission parameters is enabled. Autonegotiation is a procedure by which two connected ethernet devices choose common transmission parameters, such as speed, duplex mode, and flow control. When unset, the kernel&#8217;s default will be used. </p>
<p> Note that if autonegotiation is enabled, speed and duplex settings are read-only. If autonegotiation is disabled, speed and duplex settings are writable if the driver supports multiple link modes.</dl>
<p> <i>WakeOnLan=</i></p>
<dl>
<dd>The Wake-on-LAN policy to set for the device. Takes the special value &quot;off&quot; which disables Wake-on-LAN, or space separated list of the following words: </p>
<p> <code>phy</code></p>
<dl>
<dd>Wake on PHY activity.</dl>
<p> <code>unicast</code></p>
<dl>
<dd>Wake on unicast messages.</dl>
<p> <code>multicast</code></p>
<dl>
<dd>Wake on multicast messages.</dl>
<p> <code>broadcast</code></p>
<dl>
<dd>Wake on broadcast messages.</dl>
<p> <code>arp</code></p>
<dl>
<dd>Wake on ARP.</dl>
<p> <code>magic</code></p>
<dl>
<dd>Wake on receipt of a magic packet.</dl>
<p> <code>secureon</code></p>
<dl>
<dd>Enable secureon(tm) password for MagicPacket(tm).</dl>
<p> Defaults to unset, and the device&#8217;s default will be used. This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared.</dl>
<p> <i>Port=</i></p>
<dl>
<dd>The port option is used to select the device port. The supported values are: </p>
<p> <code>tp</code></p>
<dl>
<dd>An Ethernet interface using Twisted-Pair cable as the medium.</dl>
<p> <code>aui</code></p>
<dl>
<dd>Attachment Unit Interface (AUI). Normally used with hubs.</dl>
<p> <code>bnc</code></p>
<dl>
<dd>An Ethernet interface using BNC connectors and co-axial cable.</dl>
<p> <code>mii</code></p>
<dl>
<dd>An Ethernet interface using a Media Independent Interface (MII).</dl>
<p> <code>fibre</code></p>
<dl>
<dd>An Ethernet interface using Optical Fibre as the medium.</dl>
</dl>
<p> <i>Advertise=</i></p>
<dl>
<dd>This sets what speeds and duplex modes of operation are advertised for auto-negotiation. This implies &quot;AutoNegotiation=yes&quot;. The supported values are: </p>
<p> <code>Table 1. Supported advertise values</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Advertise </code></td>
<td><code> Speed (Mbps) </code></td>
<td><code> Duplex Mode </code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>10baset-half</code> </td>
<td> 10 </td>
<td> half
</td>
</tr>
<tr VALIGN=top>
<td> <code>10baset-full</code> </td>
<td> 10 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>100baset-half</code> </td>
<td> 100 </td>
<td> half
</td>
</tr>
<tr VALIGN=top>
<td> <code>100baset-full</code> </td>
<td> 100 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>1000baset-half</code> </td>
<td> 1000 </td>
<td> half
</td>
</tr>
<tr VALIGN=top>
<td> <code>1000baset-full</code> </td>
<td> 1000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>10000baset-full</code> </td>
<td> 10000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>2500basex-full</code> </td>
<td> 2500 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>1000basekx-full</code> </td>
<td> 1000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>10000basekx4-full</code> </td>
<td> 10000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>10000basekr-full</code> </td>
<td> 10000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>10000baser-fec</code> </td>
<td> 10000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>20000basemld2-full</code> </td>
<td> 20000 </td>
<td> full
</td>
</tr>
<tr VALIGN=top>
<td> <code>20000basekr2-full</code> </td>
<td> 20000 </td>
<td> full
</td>
</tr>
</table>
<p> By default this is unset, i.e. all possible modes will be advertised. This option may be specified more than once, in which case all specified speeds and modes are advertised. If the empty string is assigned to this option, the list is reset, and all prior assignments have no effect.</dl>
<p> <i>ReceiveChecksumOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, hardware offload for checksumming of ingress network packets is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TransmitChecksumOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, hardware offload for checksumming of egress network packets is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TCPSegmentationOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, TCP Segmentation Offload (TSO) is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TCP6SegmentationOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, TCP6 Segmentation Offload (tx-tcp6-segmentation) is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>GenericSegmentationOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, Generic Segmentation Offload (GSO) is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>GenericReceiveOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, Generic Receive Offload (GRO) is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>LargeReceiveOffload=</i></p>
<dl>
<dd>Takes a boolean. If set to true, Large Receive Offload (LRO) is enabled. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>RxChannels=</i></p>
<dl>
<dd>Sets the number of receive channels (a number between 1 and 4294967295) .</dl>
<p> <i>TxChannels=</i></p>
<dl>
<dd>Sets the number of transmit channels (a number between 1 and 4294967295).</dl>
<p> <i>OtherChannels=</i></p>
<dl>
<dd>Sets the number of other channels (a number between 1 and 4294967295).</dl>
<p> <i>CombinedChannels=</i></p>
<dl>
<dd>Sets the number of combined set channels (a number between 1 and 4294967295).</dl>
<p> <i>RxBufferSize=</i></p>
<dl>
<dd>Takes an integer. Specifies the maximum number of pending packets in the NIC receive buffer. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>RxMiniBufferSize=</i></p>
<dl>
<dd>Takes an integer. Specifies the maximum number of pending packets in the NIC mini receive buffer. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>RxJumboBufferSize=</i></p>
<dl>
<dd>Takes an integer. Specifies the maximum number of pending packets in the NIC jumbo receive buffer. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TxBufferSize=</i></p>
<dl>
<dd>Takes an integer. Specifies the maximum number of pending packets in the NIC transmit buffer. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>RxFlowControl=</i></p>
<dl>
<dd>Takes a boolean. When set, enables receive flow control, also known as the ethernet receive PAUSE message (generate and send ethernet PAUSE frames). When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TxFlowControl=</i></p>
<dl>
<dd>Takes a boolean. When set, enables transmit flow control, also known as the ethernet transmit PAUSE message (respond to received ethernet PAUSE frames). When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>AutoNegotiationFlowControl=</i></p>
<dl>
<dd>Takes a boolean. When set, auto negotiation enables the interface to exchange state advertisements with the connected peer so that the two devices can agree on the ethernet PAUSE configuration. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>GenericSegmentOffloadMaxBytes=</i></p>
<dl>
<dd>Specifies the maximum size of a Generic Segment Offload (GSO) packet the device should accept. The usual suffixes K, M, G are supported and are understood to the base of 1024. An unsigned integer in the range 1&#8230;65536. Defaults to unset.</dl>
<p> <i>GenericSegmentOffloadMaxSegments=</i></p>
<dl>
<dd>Specifies the maximum number of Generic Segment Offload (GSO) segments the device should accept. An unsigned integer in the range 1&#8230;65535. Defaults to unset.</dl>
<h2>Examples</h2>
<p><code>Example 1.&nbsp;/lib/systemd/network/99-default.link</code> </p>
<p> The link file 99-default.link that is shipped with systemd defines the default naming policy for links. </p>
<dl>
<dd>
<pre>[Link]
NamePolicy=kernel database onboard slot path
MACAddressPolicy=persistent</pre>
</dl>
<p> <code>Example 2.&nbsp;/etc/systemd/network/10-dmz.link</code> </p>
<p> This example assigns the fixed name &quot;dmz0&quot; to the interface with the MAC address 00:a0:de:63:7a:e6: </p>
<dl>
<dd>
<pre>[Match]
MACAddress=00:a0:de:63:7a:e6
[Link]
Name=dmz0</pre>
</dl>
<p> <i>NamePolicy=</i> is not set, so <i>Name=</i> takes effect. We use the &quot;10-&quot; prefix to order this file early in the list. Note that it needs to be before &quot;99-link&quot;, i.e. it needs a numerical prefix, to have any effect at all. </p>
<p> <code>Example 3. Debugging </code><i>NamePolicy=</i> assignments </p>
<dl>
<dd>
<pre>$ sudo SYSTEMD_LOG_LEVEL=debug udevadm test-builtin net_setup_link /sys/class/net/hub0
...
Parsed configuration file /lib/systemd/network/99-default.link
Parsed configuration file /etc/systemd/network/10-eth0.link
ID_NET_DRIVER=cdc_ether
Config file /etc/systemd/network/10-eth0.link applies to device hub0
link_config: autonegotiation is unset or enabled, the speed and duplex are not writable.
hub0: Device has name_assign_type=4
Using default interface naming scheme 'v240'.
hub0: Policies didn't yield a name, using specified Name=hub0.
ID_NET_LINK_FILE=/etc/systemd/network/10-eth0.link
ID_NET_NAME=hub0
...</pre>
</dl>
<p> Explicit <i>Name=</i> configuration wins in this case. </p>
<dl>
<dd>
<pre>sudo SYSTEMD_LOG_LEVEL=debug udevadm test-builtin net_setup_link /sys/class/net/enp0s31f6
...
Parsed configuration file /lib/systemd/network/99-default.link
Parsed configuration file /etc/systemd/network/10-eth0.link
Created link configuration context.
ID_NET_DRIVER=e1000e
Config file /lib/systemd/network/99-default.link applies to device enp0s31f6
link_config: autonegotiation is unset or enabled, the speed and duplex are not writable.
enp0s31f6: Device has name_assign_type=4
Using default interface naming scheme 'v240'.
enp0s31f6: Policy *keep*: keeping existing userspace name
enp0s31f6: Device has addr_assign_type=0
enp0s31f6: MAC on the device already matches policy *persistent*
ID_NET_LINK_FILE=/lib/systemd/network/99-default.link
...</pre>
</dl>
<p> In this case, the interface was already renamed, so the <code>keep</code> policy specified as the first option in 99-default.link means that the existing name is preserved. If <code>keep</code> was removed, or if were in boot before the renaming has happened, we might get the following instead: </p>
<dl>
<dd>
<pre>enp0s31f6: Policy *path* yields &quot;enp0s31f6&quot;.
enp0s31f6: Device has addr_assign_type=0
enp0s31f6: MAC on the device already matches policy *persistent*
ID_NET_LINK_FILE=/lib/systemd/network/99-default.link
ID_NET_NAME=enp0s31f6
...</pre>
</dl>
<p> Please note that the details of output are subject to change. </p>
<p> <code>Example 4.&nbsp;/etc/systemd/network/10-internet.link</code> </p>
<p> This example assigns the fixed name &quot;internet0&quot; to the interface with the device path &quot;pci-0000:00:1a.0-*&quot;: </p>
<dl>
<dd>
<pre>[Match]
Path=pci-0000:00:1a.0-*
[Link]
Name=internet0</pre>
</dl>
<p> <code>Example 5.&nbsp;/etc/systemd/network/25-wireless.link</code> </p>
<p> Here&#8217;s an overly complex example that shows the use of a large number of [Match] and [Link] settings. </p>
<dl>
<dd>
<pre>[Match]
MACAddress=12:34:56:78:9a:bc
Driver=brcmsmac
Path=pci-0000:02:00.0-*
Type=wlan
Virtualization=no
Host=my-laptop
Architecture=x86-64
[Link]
Name=wireless0
MTUBytes=1450
BitsPerSecond=10M
WakeOnLan=magic
MACAddress=cb:a9:87:65:43:21</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8), <code><a href="/docs/linux/man/8-udevadm/">udevadm</a></code>(8), <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) </p>
