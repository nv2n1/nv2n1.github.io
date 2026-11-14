---
title: "systemd-network(5)"
name: "systemd-network"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-network/"
description: "systemd.network – Network configuration"
---

<p>systemd.network &#8211; Network configuration</p>
<h2>Synopsis</h2>
<p><i>network</i>.network</p>
<h2>Description</h2>
<p>A plain ini-style text file that encodes network configuration for matching network interfaces, used by <code><a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a></code>(8). See <code><a href="/docs/linux/man/7-systemd-syntax/">systemd.syntax</a></code>(7) for a general description of the syntax. </p>
<p> The main network file must have the extension .network; other extensions are ignored. Networks are applied to links whenever the links appear. </p>
<p> The .network files are read from the files located in the system network directories /lib/systemd/network and /usr/local/lib/systemd/network, the volatile runtime network directory /run/systemd/network and the local administration network directory /etc/systemd/network. All configuration files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority, files in /run/ take precedence over files with the same name under /usr/. This can be used to override a system-supplied configuration file with a local file if needed. As a special case, an empty file (file size 0) or symlink with the same name pointing to /dev/null disables the configuration file entirely (it is &quot;masked&quot;). </p>
<p> Along with the network file foo.network, a &quot;drop-in&quot; directory foo.network.d/ may exist. All files with the suffix &quot;.conf&quot; from this directory will be merged in the alphanumeric order and parsed after the main file itself has been parsed. This is useful to alter or add configuration settings, without having to modify the main configuration file. Each drop-in file must have appropriate section headers. </p>
<p> In addition to /etc/systemd/network, drop-in &quot;.d&quot; directories can be placed in /lib/systemd/network or /run/systemd/network directories. Drop-in files in /etc/ take precedence over those in /run/ which in turn take precedence over those in /lib/. Drop-in files under any of these directories take precedence over the main network file wherever located.</p>
<h2>[Match] Section Options</h2>
<p>The network file contains a [Match] section, which determines if a given network file may be applied to a given device; and a [Network] section specifying how the device should be configured. The first (in lexical order) of the network files that matches a given device is applied, all later files are ignored, even if they match as well. </p>
<p> A network file is said to match a network interface if all matches specified by the [Match] section are satisfied. When a network file does not contain valid settings in [Match] section, then the file will match all interfaces and <code>systemd-networkd</code> warns about that. Hint: to avoid the warning and to make it clear that all interfaces shall be matched, add the following: </p>
<dl>
<dd>
<pre>Name=*</pre>
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
<p> <i>Name=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the device name, as exposed by the udev property &quot;INTERFACE&quot;, or device&#8217;s alternative names. If the list is prefixed with a &quot;!&quot;, the test is inverted.</dl>
<p> <i>WLANInterfaceType=</i></p>
<dl>
<dd>A whitespace-separated list of wireless network type. Supported values are &quot;ad-hoc&quot;, &quot;station&quot;, &quot;ap&quot;, &quot;ap-vlan&quot;, &quot;wds&quot;, &quot;monitor&quot;, &quot;mesh-point&quot;, &quot;p2p-client&quot;, &quot;p2p-go&quot;, &quot;p2p-device&quot;, &quot;ocb&quot;, and &quot;nan&quot;. If the list is prefixed with a &quot;!&quot;, the test is inverted.</dl>
<p> <i>SSID=</i></p>
<dl>
<dd>A whitespace-separated list of shell-style globs matching the SSID of the currently connected wireless LAN. If the list is prefixed with a &quot;!&quot;, the test is inverted.</dl>
<p> <i>BSSID=</i></p>
<dl>
<dd>A whitespace-separated list of hardware address of the currently connected wireless LAN. Use full colon-, hyphen- or dot-delimited hexadecimal. See the example in <i>MACAddress=</i>. This option may appear more than once, in which case the lists are merged. If the empty string is assigned to this option, the list is reset.</dl>
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
<p> <i>MACAddress=</i></p>
<dl>
<dd>The hardware address to set for the device.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>The maximum transmission unit in bytes to set for the device. The usual suffixes K, M, G, are supported and are understood to the base of 1024. </p>
<p> Note that if IPv6 is enabled on the interface, and the MTU is chosen below 1280 (the minimum MTU for IPv6) it will automatically be increased to this value.</dl>
<p> <i>ARP=</i></p>
<dl>
<dd>Takes a boolean. If set to true, the ARP (low-level Address Resolution Protocol) for this interface is enabled. When unset, the kernel&#8217;s default will be used. </p>
<p> For example, disabling ARP is useful when creating multiple MACVLAN or VLAN virtual interfaces atop a single lower-level physical interface, which will then only serve as a link/&quot;bridge&quot; device aggregating traffic to the same physical link and not participate in the network otherwise. Defaults to unset.</dl>
<p> <i>Multicast=</i></p>
<dl>
<dd>Takes a boolean. If set to true, the multicast flag on the device is enabled. Defaults to unset.</dl>
<p> <i>AllMulticast=</i></p>
<dl>
<dd>Takes a boolean. If set to true, the driver retrieves all multicast packets from the network. This happens when multicast routing is enabled. Defaults to unset.</dl>
<p> <i>Promiscuous=</i></p>
<dl>
<dd>Takes a boolean. If set to true, promiscuous mode of the interface is enabled. Defaults to unset.</dl>
<p> <i>Unmanaged=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, no attempts are made to bring up or configure matching links, equivalent to when there are no matching network files. Defaults to &quot;no&quot;. </p>
<p> This is useful for preventing later matching network files from interfering with certain interfaces that are fully controlled by other applications.</dl>
<p> <i>Group=</i></p>
<dl>
<dd>Link groups are similar to port ranges found in managed switches. When network interfaces are added to a numbered group, operations on all the interfaces from that group can be performed at once. Takes an unsigned integer in the range 0&#8230;4294967295. Defaults to unset.</dl>
<p> <i>RequiredForOnline=</i></p>
<dl>
<dd>Takes a boolean or a minimum operational state and an optional maximum operational state. Please see <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1) for possible operational states. When &quot;yes&quot;, the network is deemed required when determining whether the system is online (including when running <code>systemd-networkd-wait-online</code>). When &quot;no&quot;, the network is ignored when determining the online state. When a minimum operational state and an optional maximum operational state are set, &quot;yes&quot; is implied, and this controls the minimum and maximum operational state required for the network interface to be considered online. </p>
<p> Defaults to &quot;yes&quot; when <i>ActivationPolicy=</i> is not set, or set to &quot;up&quot;, &quot;always-up&quot;, or &quot;bound&quot;. Defaults to &quot;no&quot; when <i>ActivationPolicy=</i> is set to &quot;manual&quot; or &quot;down&quot;. This is forced to &quot;no&quot; when <i>ActivationPolicy=</i> is set to &quot;always-down&quot;. </p>
<p> The network will be brought up normally (as configured by <i>ActivationPolicy=</i>), but in the event that there is no address being assigned by DHCP or the cable is not plugged in, the link will simply remain offline and be skipped automatically by <code>systemd-networkd-wait-online</code> if &quot;RequiredForOnline=no&quot;.</dl>
<p> <i>RequiredFamilyForOnline=</i></p>
<dl>
<dd>Takes an address family. When specified, an IP address in the given family is deemed required when determining whether the link is online (including when running <code>systemd-networkd-wait-online</code>). Takes one of &quot;ipv4&quot;, &quot;ipv6&quot;, &quot;both&quot;, or &quot;any&quot;. Defaults to &quot;any&quot;. Note that this option has no effect if &quot;RequiredForOnline=no&quot;, or if &quot;RequiredForOnline=&quot; specifies a minimum operational state below &quot;degraded&quot;.</dl>
<p> <i>ActivationPolicy=</i></p>
<dl>
<dd>Specifies the policy for <code>systemd-networkd</code> managing the link administrative state. Specifically, this controls how <code>systemd-networkd</code> changes the network device&#8217;s &quot;IFF_UP&quot; flag, which is sometimes controlled by system administrators by running e.g., <code>ip link set dev eth0 up</code> or <code>ip link set dev eth0 down</code>, and can also be changed with <code>networkctl up eth0</code> or <code>networkctl down eth0</code>. </p>
<p> Takes one of &quot;up&quot;, &quot;always-up&quot;, &quot;manual&quot;, &quot;always-down&quot;, &quot;down&quot;, or &quot;bound&quot;. When &quot;manual&quot;, <code>systemd-networkd</code> will not change the link&#8217;s admin state automatically; the system administrator must bring the interface up or down manually, as desired. When &quot;up&quot; (the default) or &quot;always-up&quot;, or &quot;down&quot; or &quot;always-down&quot;, <code>systemd-networkd</code> will set the link up or down, respectively, when the interface is (re)configured. When &quot;always-up&quot; or &quot;always-down&quot;, <code>systemd-networkd</code> will set the link up or down, respectively, any time <code>systemd-networkd</code> detects a change in the administrative state. When <i>BindCarrier=</i> is also set, this is automatically set to &quot;bound&quot; and any other value is ignored. </p>
<p> When the policy is set to &quot;down&quot; or &quot;manual&quot;, the default value of <i>RequiredForOnline=</i> is &quot;no&quot;. When the policy is set to &quot;always-down&quot;, the value of <i>RequiredForOnline=</i> forced to &quot;no&quot;. </p>
<p> The administrative state is not the same as the carrier state, so using &quot;always-up&quot; does not mean the link will never lose carrier. The link carrier depends on both the administrative state as well as the network device&#8217;s physical connection. However, to avoid reconfiguration failures, when using &quot;always-up&quot;, <i>IgnoreCarrierLoss=</i> is forced to true.</dl>
<h2>[Sr-Iov] Section Options</h2>
<p>The [SR-IOV] section accepts the following keys. Specify several [SR-IOV] sections to configure several SR-IOVs. SR-IOV provides the ability to partition a single physical PCI resource into virtual PCI functions which can then be injected into a VM. In the case of network VFs, SR-IOV improves north-south network performance (that is, traffic with endpoints outside the host machine) by allowing traffic to bypass the host machine&#8217;s network stack. </p>
<p> <i>VirtualFunction=</i></p>
<dl>
<dd>Specifies a Virtual Function (VF), lightweight PCIe function designed solely to move data in and out. Takes an unsigned integer in the range 0&#8230;2147483646. This option is compulsory.</dl>
<p> <i>VLANId=</i></p>
<dl>
<dd>Specifies VLAN ID of the virtual function. Takes an unsigned integer in the range 1&#8230;4095.</dl>
<p> <i>QualityOfService=</i></p>
<dl>
<dd>Specifies quality of service of the virtual function. Takes an unsigned integer in the range 1&#8230;4294967294.</dl>
<p> <i>VLANProtocol=</i></p>
<dl>
<dd>Specifies VLAN protocol of the virtual function. Takes &quot;802.1Q&quot; or &quot;802.1ad&quot;.</dl>
<p> <i>MACSpoofCheck=</i></p>
<dl>
<dd>Takes a boolean. Controls the MAC spoof checking. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>QueryReceiveSideScaling=</i></p>
<dl>
<dd>Takes a boolean. Toggle the ability of querying the receive side scaling (RSS) configuration of the virtual function (VF). The VF RSS information like RSS hash key may be considered sensitive on some devices where this information is shared between VF and the physical function (PF). When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>Trust=</i></p>
<dl>
<dd>Takes a boolean. Allows to set trust mode of the virtual function (VF). When set, VF users can set a specific feature which may impact security and/or performance. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>LinkState=</i></p>
<dl>
<dd>Allows to set the link state of the virtual function (VF). Takes a boolean or a special value &quot;auto&quot;. Setting to &quot;auto&quot; means a reflection of the physical function (PF) link state, &quot;yes&quot; lets the VF to communicate with other VFs on this host even if the PF link state is down, &quot;no&quot; causes the hardware to drop any packets sent by the VF. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MACAddress=</i></p>
<dl>
<dd>Specifies the MAC address for the virtual function.</dl>
<h2>[Network] Section Options</h2>
<p>The [Network] section accepts the following keys: </p>
<p> <i>Description=</i></p>
<dl>
<dd>A description of the device. This is only used for presentation purposes.</dl>
<p> <i>DHCP=</i></p>
<dl>
<dd>Enables DHCPv4 and/or DHCPv6 client support. Accepts &quot;yes&quot;, &quot;no&quot;, &quot;ipv4&quot;, or &quot;ipv6&quot;. Defaults to &quot;no&quot;. </p>
<p> Note that DHCPv6 will by default be triggered by Router Advertisement, if that is enabled, regardless of this parameter. By enabling DHCPv6 support explicitly, the DHCPv6 client will be started regardless of the presence of routers on the link, or what flags the routers pass. See &quot;IPv6AcceptRA=&quot;. </p>
<p> Furthermore, note that by default the domain name specified through DHCP, on Ubuntu, are used for name resolution. See option <code>UseDomains=</code> below. </p>
<p> See the [DHCPv4] or [DHCPv6] sections below for further configuration options for the DHCP client support.</dl>
<p> <i>DHCPServer=</i></p>
<dl>
<dd>Takes a boolean. If set to &quot;yes&quot;, DHCPv4 server will be started. Defaults to &quot;no&quot;. Further settings for the DHCP server may be set in the [DHCPServer] section described below.</dl>
<p> <i>LinkLocalAddressing=</i></p>
<dl>
<dd>Enables link-local address autoconfiguration. Accepts <code>yes</code>, <code>no</code>, <code>ipv4</code>, and <code>ipv6</code>. An IPv6 link-local address is configured when <code>yes</code> or <code>ipv6</code>. An IPv4 link-local address is configured when <code>yes</code> or <code>ipv4</code> and when DHCPv4 autoconfiguration has been unsuccessful for some time. (IPv4 link-local address autoconfiguration will usually happen in parallel with repeated attempts to acquire a DHCPv4 lease). </p>
<p> Defaults to <code>no</code> when <i>Bridge=yes</i> is set, and <code>ipv6</code> otherwise.</dl>
<p> <i>IPv6LinkLocalAddressGenerationMode=</i></p>
<dl>
<dd>Specifies how IPv6 link local address is generated. Takes one of &quot;eui64&quot;, &quot;none&quot;, &quot;stable-privacy&quot; and &quot;random&quot;. When unset, &quot;stable-privacy&quot; is used if <i>IPv6StableSecretAddress=</i> is specified, and if not, &quot;eui64&quot; is used. Note that if <i>LinkLocalAddressing=</i> is &quot;no&quot; or &quot;ipv4&quot;, then <i>IPv6LinkLocalAddressGenerationMode=</i> will be ignored. Also, even if <i>LinkLocalAddressing=</i> is &quot;yes&quot; or &quot;ipv6&quot;, setting <i>IPv6LinkLocalAddressGenerationMode=none</i> disables to configure an IPv6 link-local address.</dl>
<p> <i>IPv6StableSecretAddress=</i></p>
<dl>
<dd>Takes an IPv6 address. The specified address will be used as a stable secret for generating IPv6 link-local address. If this setting is specified, and <i>IPv6LinkLocalAddressGenerationMode=</i> is unset, then <i>IPv6LinkLocalAddressGenerationMode=stable-privacy</i> is implied. If this setting is not specified, and &quot;stable-privacy&quot; is set to <i>IPv6LinkLocalAddressGenerationMode=</i>, then a stable secret address will be generated from the local machine ID and the interface name.</dl>
<p> <i>IPv4LLRoute=</i></p>
<dl>
<dd>Takes a boolean. If set to true, sets up the route needed for non-IPv4LL hosts to communicate with IPv4LL-only hosts. Defaults to false.</dl>
<p> <i>DefaultRouteOnDevice=</i></p>
<dl>
<dd>Takes a boolean. If set to true, sets up the default route bound to the interface. Defaults to false. This is useful when creating routes on point-to-point interfaces. This is equivalent to e.g. the following, </p>
<dl>
<dd>
<pre>ip route add default dev veth99</pre>
</dl>
<p> or, </p>
<dl>
<dd>
<pre>[Route]
Gateway=0.0.0.0</pre>
</dl>
<p> Currently, there are no way to specify e.g., the table for the route configured by this setting. To configure the default route with such an additional property, please use the following instead: </p>
<dl>
<dd>
<pre>[Route]
Gateway=0.0.0.0
Table=1234</pre>
</dl>
</dl>
<p> <i>IPv6Token=</i></p>
<dl>
<dd>Specifies an optional address generation mode for the Stateless Address Autoconfiguration (SLAAC). Supported modes are &quot;prefixstable&quot; and &quot;static&quot;. </p>
<p> When the mode is set to &quot;static&quot;, an IPv6 address must be specified after a colon (&quot;:&quot;), and the lower bits of the supplied address are combined with the upper bits of a prefix received in a Router Advertisement (RA) message to form a complete address. Note that if multiple prefixes are received in an RA message, or in multiple RA messages, addresses will be formed from each of them using the supplied address. This mode implements SLAAC but uses a static interface identifier instead of an identifier generated by using the EUI-64 algorithm. Because the interface identifier is static, if Duplicate Address Detection detects that the computed address is a duplicate (in use by another node on the link), then this mode will fail to provide an address for that prefix. If an IPv6 address without mode is specified, then &quot;static&quot; mode is assumed. </p>
<p> When the mode is set to &quot;prefixstable&quot; the m[blue]<code>RFC 7217</code>m[]<font SIZE="-2">[1]</font> algorithm for generating interface identifiers will be used. This mode can optionally take an IPv6 address separated with a colon (&quot;:&quot;). If an IPv6 address is specified, then an interface identifier is generated only when a prefix received in an RA message matches the supplied address. </p>
<p> If no address generation mode is specified (which is the default), or a received prefix does not match any of the addresses provided in &quot;prefixstable&quot; mode, then the EUI-64 algorithm will be used to form an interface identifier for that prefix. This mode is also SLAAC, but with a potentially stable interface identifier which does not directly map to the interface&#8217;s hardware address. </p>
<p> Note that the &quot;prefixstable&quot; algorithm uses both the interface name and MAC address as input to the hash to compute the interface identifier, so if either of those are changed the resulting interface identifier (and address) will change, even if the prefix received in the RA message has not changed. </p>
<p> This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared. </p>
<p> Examples: </p>
<dl>
<dd>
<pre>IPv6Token=::1a:2b:3c:4d
IPv6Token=static:::1a:2b:3c:4d
IPv6Token=prefixstable
IPv6Token=prefixstable:2002:da8:1::</pre>
</dl>
</dl>
<p> <i>LLMNR=</i></p>
<dl>
<dd>Takes a boolean or &quot;resolve&quot;. When true, enables m[blue]<code>Link-Local Multicast Name Resolution</code>m[]<font SIZE="-2">[2]</font> on the link. When set to &quot;resolve&quot;, only resolution is enabled, but not host registration and announcement. Defaults to true. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>MulticastDNS=</i></p>
<dl>
<dd>Takes a boolean or &quot;resolve&quot;. When true, enables m[blue]<code>Multicast DNS</code>m[]<font SIZE="-2">[3]</font> support on the link. When set to &quot;resolve&quot;, only resolution is enabled, but not host or service registration and announcement. Defaults to false. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>DNSOverTLS=</i></p>
<dl>
<dd>Takes a boolean or &quot;opportunistic&quot;. When true, enables m[blue]<code>DNS-over-TLS</code>m[]<font SIZE="-2">[4]</font> support on the link. When set to &quot;opportunistic&quot;, compatibility with non-DNS-over-TLS servers is increased, by automatically turning off DNS-over-TLS servers in this case. This option defines a per-interface setting for <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5)&#8217;s global <i>DNSOverTLS=</i> option. Defaults to false. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>DNSSEC=</i></p>
<dl>
<dd>Takes a boolean or &quot;allow-downgrade&quot;. When true, enables m[blue]<code>DNSSEC</code>m[]<font SIZE="-2">[5]</font> DNS validation support on the link. When set to &quot;allow-downgrade&quot;, compatibility with non-DNSSEC capable networks is increased, by automatically turning off DNSSEC in this case. This option defines a per-interface setting for <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5)&#8217;s global <i>DNSSEC=</i> option. Defaults to false. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>DNSSECNegativeTrustAnchors=</i></p>
<dl>
<dd>A space-separated list of DNSSEC negative trust anchor domains. If specified and DNSSEC is enabled, look-ups done via the interface&#8217;s DNS server will be subject to the list of negative trust anchors, and not require authentication for the specified domains, or anything below it. Use this to disable DNSSEC authentication for specific private domains, that cannot be proven valid using the Internet DNS hierarchy. Defaults to the empty list. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>LLDP=</i></p>
<dl>
<dd>Controls support for Ethernet LLDP packet reception. LLDP is a link-layer protocol commonly implemented on professional routers and bridges which announces which physical port a system is connected to, as well as other related data. Accepts a boolean or the special value &quot;routers-only&quot;. When true, incoming LLDP packets are accepted and a database of all LLDP neighbors maintained. If &quot;routers-only&quot; is set only LLDP data of various types of routers is collected and LLDP data about other types of devices ignored (such as stations, telephones and others). If false, LLDP reception is disabled. Defaults to &quot;routers-only&quot;. Use <code><a href="/docs/linux/man/1-networkctl/">networkctl</a></code>(1) to query the collected neighbor data. LLDP is only available on Ethernet links. See <i>EmitLLDP=</i> below for enabling LLDP packet emission from the local system.</dl>
<p> <i>EmitLLDP=</i></p>
<dl>
<dd>Controls support for Ethernet LLDP packet emission. Accepts a boolean parameter or the special values &quot;nearest-bridge&quot;, &quot;non-tpmr-bridge&quot; and &quot;customer-bridge&quot;. Defaults to false, which turns off LLDP packet emission. If not false, a short LLDP packet with information about the local system is sent out in regular intervals on the link. The LLDP packet will contain information about the local hostname, the local machine ID (as stored in <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5)) and the local interface name, as well as the pretty hostname of the system (as set in <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5)). LLDP emission is only available on Ethernet links. Note that this setting passes data suitable for identification of host to the network and should thus not be enabled on untrusted networks, where such identification data should not be made available. Use this option to permit other systems to identify on which interfaces they are connected to this system. The three special values control propagation of the LLDP packets. The &quot;nearest-bridge&quot; setting permits propagation only to the nearest connected bridge, &quot;non-tpmr-bridge&quot; permits propagation across Two-Port MAC Relays, but not any other bridges, and &quot;customer-bridge&quot; permits propagation until a customer bridge is reached. For details about these concepts, see m[blue]<code>IEEE 802.1AB-2016</code>m[]<font SIZE="-2">[6]</font>. Note that configuring this setting to true is equivalent to &quot;nearest-bridge&quot;, the recommended and most restricted level of propagation. See <i>LLDP=</i> above for an option to enable LLDP reception.</dl>
<p> <i>BindCarrier=</i></p>
<dl>
<dd>A link name or a list of link names. When set, controls the behavior of the current link. When all links in the list are in an operational down state, the current link is brought down. When at least one link has carrier, the current interface is brought up. </p>
<p> This forces <i>ActivationPolicy=</i> to be set to &quot;bound&quot;.</dl>
<p> <i>Address=</i></p>
<dl>
<dd>A static IPv4 or IPv6 address and its prefix length, separated by a &quot;/&quot; character. Specify this key more than once to configure several addresses. The format of the address must be as described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3). This is a short-hand for an [Address] section only containing an Address key (see below). This option may be specified more than once. </p>
<p> If the specified address is &quot;0.0.0.0&quot; (for IPv4) or &quot;::&quot; (for IPv6), a new address range of the requested size is automatically allocated from a system-wide pool of unused ranges. Note that the prefix length must be equal or larger than 8 for IPv4, and 64 for IPv6. The allocated range is checked against all current network interfaces and all known network configuration files to avoid address range conflicts. The default system-wide pool consists of 192.168.0.0/16, 172.16.0.0/12 and 10.0.0.0/8 for IPv4, and fd00::/8 for IPv6. This functionality is useful to manage a large number of dynamically created network interfaces with the same network configuration and automatic address range assignment.</dl>
<p> <i>Gateway=</i></p>
<dl>
<dd>The gateway address, which must be in the format described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3). This is a short-hand for a [Route] section only containing a Gateway key. This option may be specified more than once.</dl>
<p> <i>DNS=</i></p>
<dl>
<dd>A DNS server address, which must be in the format described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3). This option may be specified more than once. Each address can optionally take a port number separated with &quot;:&quot;, a network interface name or index separated with &quot;%&quot;, and a Server Name Indication (SNI) separated with &quot;#&quot;. When IPv6 address is specified with a port number, then the address must be in the square brackets. That is, the acceptable full formats are &quot;111.222.333.444:9953%ifname#example.com&quot; for IPv4 and &quot;[1111:2222::3333]:9953%ifname#example.com&quot; for IPv6. If an empty string is assigned, then the all previous assignments are cleared. This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8).</dl>
<p> <i>Domains=</i></p>
<dl>
<dd>A whitespace-separated list of domains which should be resolved using the DNS servers on this link. Each item in the list should be a domain name, optionally prefixed with a tilde (&quot;~&quot;). The domains with the prefix are called &quot;routing-only domains&quot;. The domains without the prefix are called &quot;search domains&quot; and are first used as search suffixes for extending single-label hostnames (hostnames containing no dots) to become fully qualified domain names (FQDNs). If a single-label hostname is resolved on this interface, each of the specified search domains are appended to it in turn, converting it into a fully qualified domain name, until one of them may be successfully resolved. </p>
<p> Both &quot;search&quot; and &quot;routing-only&quot; domains are used for routing of DNS queries: look-ups for hostnames ending in those domains (hence also single label names, if any &quot;search domains&quot; are listed), are routed to the DNS servers configured for this interface. The domain routing logic is particularly useful on multi-homed hosts with DNS servers serving particular private DNS zones on each interface. </p>
<p> The &quot;routing-only&quot; domain &quot;~.&quot; (the tilde indicating definition of a routing domain, the dot referring to the DNS root domain which is the implied suffix of all valid DNS names) has special effect. It causes all DNS traffic which does not match another configured domain routing entry to be routed to DNS servers specified for this interface. This setting is useful to prefer a certain set of DNS servers if a link on which they are connected is available. </p>
<p> This setting is read by <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8). &quot;Search domains&quot; correspond to the <i>domain</i> and <i>search</i> entries in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5). Domain name routing has no equivalent in the traditional glibc API, which has no concept of domain name servers limited to a specific link.</dl>
<p> <i>DNSDefaultRoute=</i></p>
<dl>
<dd>Takes a boolean argument. If true, this link&#8217;s configured DNS servers are used for resolving domain names that do not match any link&#8217;s configured <i>Domains=</i> setting. If false, this link&#8217;s configured DNS servers are never used for such domains, and are exclusively used for resolving names that match at least one of the domains configured on this link. If not specified defaults to an automatic mode: queries not matching any link&#8217;s configured domains will be routed to this link if it has no routing-only domains configured.</dl>
<p> <i>NTP=</i></p>
<dl>
<dd>An NTP server address (either an IP address, or a hostname). This option may be specified more than once. This setting is read by <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8).</dl>
<p> <i>IPForward=</i></p>
<dl>
<dd>Configures IP packet forwarding for the system. If enabled, incoming packets on any network interface will be forwarded to any other interfaces according to the routing table. Takes a boolean, or the values &quot;ipv4&quot; or &quot;ipv6&quot;, which only enable IP packet forwarding for the specified address family. This controls the net.ipv4.ip_forward and net.ipv6.conf.all.forwarding sysctl options of the network interface (see m[blue]<code>ip-sysctl.txt</code>m[]<font SIZE="-2">[7]</font> for details about sysctl options). Defaults to &quot;no&quot;. </p>
<p> Note: this setting controls a global kernel option, and does so one way only: if a network that has this setting enabled is set up the global setting is turned on. However, it is never turned off again, even after all networks with this setting enabled are shut down again. </p>
<p> To allow IP packet forwarding only between specific network interfaces use a firewall.</dl>
<p> <i>IPMasquerade=</i></p>
<dl>
<dd>Configures IP masquerading for the network interface. If enabled, packets forwarded from the network interface will be appear as coming from the local host. Takes one of &quot;ipv4&quot;, &quot;ipv6&quot;, &quot;both&quot;, or &quot;no&quot;. Defaults to &quot;no&quot;. If enabled, this automatically sets <i>IPForward=</i> to one of &quot;ipv4&quot;, &quot;ipv6&quot; or &quot;yes&quot;. </p>
<p> Note. Any positive boolean values such as &quot;yes&quot; or &quot;true&quot; are now deprecated. Please use one of the values in the above.</dl>
<p> <i>IPv6PrivacyExtensions=</i></p>
<dl>
<dd>Configures use of stateless temporary addresses that change over time (see m[blue]<code>RFC 4941</code>m[]<font SIZE="-2">[8]</font>, Privacy Extensions for Stateless Address Autoconfiguration in IPv6). Takes a boolean or the special values &quot;prefer-public&quot; and &quot;kernel&quot;. When true, enables the privacy extensions and prefers temporary addresses over public addresses. When &quot;prefer-public&quot;, enables the privacy extensions, but prefers public addresses over temporary addresses. When false, the privacy extensions remain disabled. When &quot;kernel&quot;, the kernel&#8217;s default setting will be left in place. Defaults to &quot;no&quot;.</dl>
<p> <i>IPv6AcceptRA=</i></p>
<dl>
<dd>Takes a boolean. Controls IPv6 Router Advertisement (RA) reception support for the interface. If true, RAs are accepted; if false, RAs are ignored. When RAs are accepted, they may trigger the start of the DHCPv6 client if the relevant flags are set in the RA data, or if no routers are found on the link. The default is to disable RA reception for bridge devices or when IP forwarding is enabled, and to enable it otherwise. Cannot be enabled on bond devices and when link local addressing is disabled. </p>
<p> Further settings for the IPv6 RA support may be configured in the [IPv6AcceptRA] section, see below. </p>
<p> Also see m[blue]<code>ip-sysctl.txt</code>m[]<font SIZE="-2">[7]</font> in the kernel documentation regarding &quot;accept_ra&quot;, but note that systemd&#8217;s setting of <code>1</code> (i.e. true) corresponds to kernel&#8217;s setting of <code>2</code>. </p>
<p> Note that kernel&#8217;s implementation of the IPv6 RA protocol is always disabled, regardless of this setting. If this option is enabled, a userspace implementation of the IPv6 RA protocol is used, and the kernel&#8217;s own implementation remains disabled, since <code>systemd-networkd</code> needs to know all details supplied in the advertisements, and these are not available from the kernel if the kernel&#8217;s own implementation is used.</dl>
<p> <i>IPv6DuplicateAddressDetection=</i></p>
<dl>
<dd>Configures the amount of IPv6 Duplicate Address Detection (DAD) probes to send. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv6HopLimit=</i></p>
<dl>
<dd>Configures IPv6 Hop Limit. For each router that forwards the packet, the hop limit is decremented by 1. When the hop limit field reaches zero, the packet is discarded. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv4AcceptLocal=</i></p>
<dl>
<dd>Takes a boolean. Accept packets with local source addresses. In combination with suitable routing, this can be used to direct packets between two local interfaces over the wire and have them accepted properly. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv4RouteLocalnet=</i></p>
<dl>
<dd>Takes a boolean. When true, the kernel does not consider loopback addresses as martian source or destination while routing. This enables the use of 127.0.0.0/8 for local routing purposes. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv4ProxyARP=</i></p>
<dl>
<dd>Takes a boolean. Configures proxy ARP for IPv4. Proxy ARP is the technique in which one host, usually a router, answers ARP requests intended for another machine. By &quot;faking&quot; its identity, the router accepts responsibility for routing packets to the &quot;real&quot; destination. See m[blue]<code>RFC 1027</code>m[]<font SIZE="-2">[9]</font>. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv6ProxyNDP=</i></p>
<dl>
<dd>Takes a boolean. Configures proxy NDP for IPv6. Proxy NDP (Neighbor Discovery Protocol) is a technique for IPv6 to allow routing of addresses to a different destination when peers expect them to be present on a certain physical link. In this case a router answers Neighbour Advertisement messages intended for another machine by offering its own MAC address as destination. Unlike proxy ARP for IPv4, it is not enabled globally, but will only send Neighbour Advertisement messages for addresses in the IPv6 neighbor proxy table, which can also be shown by <code>ip -6 neighbour show proxy</code>. systemd-networkd will control the per-interface `proxy_ndp` switch for each configured interface depending on this option. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv6ProxyNDPAddress=</i></p>
<dl>
<dd>An IPv6 address, for which Neighbour Advertisement messages will be proxied. This option may be specified more than once. systemd-networkd will add the <code>IPv6ProxyNDPAddress=</code> entries to the kernel&#8217;s IPv6 neighbor proxy table. This option implies <code>IPv6ProxyNDP=yes</code> but has no effect if <code>IPv6ProxyNDP</code> has been set to false. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>IPv6SendRA=</i></p>
<dl>
<dd>Whether to enable or disable Router Advertisement sending on a link. Takes a boolean value. When enabled, prefixes configured in [IPv6Prefix] sections and routes configured in [IPv6RoutePrefix] sections are distributed as defined in the [IPv6SendRA] section. If <i>DHCPv6PrefixDelegation=</i> is enabled, then the delegated prefixes are also distributed. See <i>DHCPv6PrefixDelegation=</i> setting and the [IPv6SendRA], [IPv6Prefix], [IPv6RoutePrefix], and [DHCPv6PrefixDelegation] sections for more configuration options.</dl>
<p> <i>DHCPv6PrefixDelegation=</i></p>
<dl>
<dd>Takes a boolean value. When enabled, requests prefixes using a DHCPv6 client configured on another link. By default, an address within each delegated prefix will be assigned, and the prefixes will be announced through IPv6 Router Advertisement when <i>IPv6SendRA=</i> is enabled. Such default settings can be configured in [DHCPv6PrefixDelegation] section. Defaults to disabled.</dl>
<p> <i>IPv6MTUBytes=</i></p>
<dl>
<dd>Configures IPv6 maximum transmission unit (MTU). An integer greater than or equal to 1280 bytes. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>BatmanAdvanced=</i>, <i>Bond=</i>, <i>Bridge=</i>, <i>VRF=</i></p>
<dl>
<dd>The name of the B.A.T.M.A.N. Advanced, bond, bridge, or VRF interface to add the link to. See <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5).</dl>
<p> <i>IPVLAN=</i>, <i>IPVTAP=</i>, <i>L2TP=</i>, <i>MACsec=</i>, <i>MACVLAN=</i>, <i>MACVTAP=</i>, <i>Tunnel=</i>, <i>VLAN=</i>, <i>VXLAN=</i>, <i>Xfrm=</i></p>
<dl>
<dd>The name of an IPVLAN, IPVTAP, L2TP, MACsec, MACVLAN, MACVTAP, tunnel, VLAN, VXLAN, or Xfrm to be created on the link. See <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5). This option may be specified more than once.</dl>
<p> <i>ActiveSlave=</i></p>
<dl>
<dd>Takes a boolean. Specifies the new active slave. The &quot;ActiveSlave=&quot; option is only valid for following modes: &quot;active-backup&quot;, &quot;balance-alb&quot; and &quot;balance-tlb&quot;. Defaults to false.</dl>
<p> <i>PrimarySlave=</i></p>
<dl>
<dd>Takes a boolean. Specifies which slave is the primary device. The specified device will always be the active slave while it is available. Only when the primary is off-line will alternate devices be used. This is useful when one slave is preferred over another, e.g. when one slave has higher throughput than another. The &quot;PrimarySlave=&quot; option is only valid for following modes: &quot;active-backup&quot;, &quot;balance-alb&quot; and &quot;balance-tlb&quot;. Defaults to false.</dl>
<p> <i>ConfigureWithoutCarrier=</i></p>
<dl>
<dd>Takes a boolean. Allows networkd to configure a specific link even if it has no carrier. Defaults to false. If <code>IgnoreCarrierLoss=</code> is not explicitly set, it will default to this value.</dl>
<p> <i>IgnoreCarrierLoss=</i></p>
<dl>
<dd>Takes a boolean. Allows networkd to retain both the static and dynamic configuration of the interface even if its carrier is lost. When unset, the value specified with <code>ConfigureWithoutCarrier=</code> is used. </p>
<p> When <i>ActivationPolicy=</i> is set to &quot;always-up&quot;, this is forced to &quot;true&quot;.</dl>
<p> <i>KeepConfiguration=</i></p>
<dl>
<dd>Takes a boolean or one of &quot;static&quot;, &quot;dhcp-on-stop&quot;, &quot;dhcp&quot;. When &quot;static&quot;, <code>systemd-networkd</code> will not drop static addresses and routes on starting up process. When set to &quot;dhcp-on-stop&quot;, <code>systemd-networkd</code> will not drop addresses and routes on stopping the daemon. When &quot;dhcp&quot;, the addresses and routes provided by a DHCP server will never be dropped even if the DHCP lease expires. This is contrary to the DHCP specification, but may be the best choice if, e.g., the root filesystem relies on this connection. The setting &quot;dhcp&quot; implies &quot;dhcp-on-stop&quot;, and &quot;yes&quot; implies &quot;dhcp&quot; and &quot;static&quot;. Defaults to &quot;no&quot;.</dl>
<h2>[Address] Section Options</h2>
<p>An [Address] section accepts the following keys. Specify several [Address] sections to configure several addresses. </p>
<p> <i>Address=</i></p>
<dl>
<dd>As in the [Network] section. This key is mandatory. Each [Address] section can contain one <i>Address=</i> setting.</dl>
<p> <i>Peer=</i></p>
<dl>
<dd>The peer address in a point-to-point connection. Accepts the same format as the <i>Address=</i> key.</dl>
<p> <i>Broadcast=</i></p>
<dl>
<dd>Takes an IPv4 address or boolean value. The address must be in the format described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3). If set to true, then the IPv4 broadcast address will be derived from the <i>Address=</i> setting. If set to false, then the broadcast address will not be set. Defaults to true, except for wireguard interfaces, where it default to false.</dl>
<p> <i>Label=</i></p>
<dl>
<dd>An address label.</dl>
<p> <i>PreferredLifetime=</i></p>
<dl>
<dd>Allows the default &quot;preferred lifetime&quot; of the address to be overridden. Only three settings are accepted: &quot;forever&quot;, &quot;infinity&quot;, which is the default and means that the address never expires, and &quot;0&quot;, which means that the address is considered immediately &quot;expired&quot; and will not be used, unless explicitly requested. A setting of <code>PreferredLifetime=0</code> is useful for addresses which are added to be used only by a specific application, which is then configured to use them explicitly.</dl>
<p> <i>Scope=</i></p>
<dl>
<dd>The scope of the address, which can be &quot;global&quot; (valid everywhere on the network, even through a gateway), &quot;link&quot; (only valid on this device, will not traverse a gateway) or &quot;host&quot; (only valid within the device itself, e.g. 127.0.0.1) or an unsigned integer in the range 0&#8230;255. Defaults to &quot;global&quot;.</dl>
<p> <i>RouteMetric=</i></p>
<dl>
<dd>The metric of the prefix route, which is pointing to the subnet of the configured IP address, taking the configured prefix length into account. Takes an unsigned integer in the range 0&#8230;4294967295. When unset or set to 0, the kernel&#8217;s default value is used. This setting will be ignored when <i>AddPrefixRoute=</i> is false.</dl>
<p> <i>HomeAddress=</i></p>
<dl>
<dd>Takes a boolean. Designates this address the &quot;home address&quot; as defined in m[blue]<code>RFC 6275</code>m[]<font SIZE="-2">[10]</font>. Supported only on IPv6. Defaults to false.</dl>
<p> <i>DuplicateAddressDetection=</i></p>
<dl>
<dd>Takes one of &quot;ipv4&quot;, &quot;ipv6&quot;, &quot;both&quot;, &quot;none&quot;. When &quot;ipv4&quot;, performs IPv4 Address Conflict Detection. See m[blue]<code>RFC 5227</code>m[]<font SIZE="-2">[11]</font>. When &quot;ipv6&quot;, performs IPv6 Duplicate Address Detection. See m[blue]<code>RFC 4862</code>m[]<font SIZE="-2">[12]</font>. Defaults to &quot;ipv4&quot; for IPv4 link-local addresses, &quot;ipv6&quot; for IPv6 addresses, and &quot;none&quot; otherwise.</dl>
<p> <i>ManageTemporaryAddress=</i></p>
<dl>
<dd>Takes a boolean. If true the kernel manage temporary addresses created from this one as template on behalf of Privacy Extensions m[blue]<code>RFC 3041</code>m[]<font SIZE="-2">[13]</font>. For this to become active, the use_tempaddr sysctl setting has to be set to a value greater than zero. The given address needs to have a prefix length of 64. This flag allows using privacy extensions in a manually configured network, just like if stateless auto-configuration was active. Defaults to false.</dl>
<p> <i>AddPrefixRoute=</i></p>
<dl>
<dd>Takes a boolean. When true, the prefix route for the address is automatically added. Defaults to true.</dl>
<p> <i>AutoJoin=</i></p>
<dl>
<dd>Takes a boolean. Joining multicast group on ethernet level via <code>ip maddr</code> command would not work if we have an Ethernet switch that does IGMP snooping since the switch would not replicate multicast packets on ports that did not have IGMP reports for the multicast addresses. Linux vxlan interfaces created via <code>ip link add vxlan</code> or networkd&#8217;s netdev kind vxlan have the group option that enables then to do the required join. By extending ip address command with option &quot;autojoin&quot; we can get similar functionality for openvswitch (OVS) vxlan interfaces as well as other tunneling mechanisms that need to receive multicast traffic. Defaults to &quot;no&quot;.</dl>
<h2>[Neighbor] Section Options</h2>
<p>A [Neighbor] section accepts the following keys. The neighbor section adds a permanent, static entry to the neighbor table (IPv6) or ARP table (IPv4) for the given hardware address on the links matched for the network. Specify several [Neighbor] sections to configure several static neighbors. </p>
<p> <i>Address=</i></p>
<dl>
<dd>The IP address of the neighbor.</dl>
<p> <i>LinkLayerAddress=</i></p>
<dl>
<dd>The link layer address (MAC address or IP address) of the neighbor.</dl>
<h2>[Ipv6Addresslabel] Section Options</h2>
<p>An [IPv6AddressLabel] section accepts the following keys. Specify several [IPv6AddressLabel] sections to configure several address labels. IPv6 address labels are used for address selection. See m[blue]<code>RFC 3484</code>m[]<font SIZE="-2">[14]</font>. Precedence is managed by userspace, and only the label itself is stored in the kernel. </p>
<p> <i>Label=</i></p>
<dl>
<dd>The label for the prefix, an unsigned integer in the range 0-4294967294. 0xffffffff is reserved. This setting is mandatory.</dl>
<p> <i>Prefix=</i></p>
<dl>
<dd>IPv6 prefix is an address with a prefix length, separated by a slash &quot;/&quot; character. This key is mandatory.</dl>
<h2>[Routingpolicyrule] Section Options</h2>
<p>An [RoutingPolicyRule] section accepts the following keys. Specify several [RoutingPolicyRule] sections to configure several rules. </p>
<p> <i>TypeOfService=</i></p>
<dl>
<dd>Takes a number between 0 and 255 that specifies the type of service to match.</dl>
<p> <i>From=</i></p>
<dl>
<dd>Specifies the source address prefix to match. Possibly followed by a slash and the prefix length.</dl>
<p> <i>To=</i></p>
<dl>
<dd>Specifies the destination address prefix to match. Possibly followed by a slash and the prefix length.</dl>
<p> <i>FirewallMark=</i></p>
<dl>
<dd>Specifies the iptables firewall mark value to match (a number between 1 and 4294967295). Optionally, the firewall mask (also a number between 1 and 4294967295) can be suffixed with a slash (&quot;/&quot;), e.g., &quot;7/255&quot;.</dl>
<p> <i>Table=</i></p>
<dl>
<dd>Specifies the routing table identifier to lookup if the rule selector matches. Takes one of predefined names &quot;default&quot;, &quot;main&quot;, and &quot;local&quot;, and names defined in <i>RouteTable=</i> in <code><a href="/docs/linux/man/5-networkd-conf/">networkd.conf</a></code>(5), or a number between 1 and 4294967295. Defaults to &quot;main&quot;.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>Specifies the priority of this rule. <i>Priority=</i> is an unsigned integer in the range 0&#8230;4294967295. Higher number means lower priority, and rules get processed in order of increasing number. Defaults to unset, and the kernel will pick a value dynamically.</dl>
<p> <i>IncomingInterface=</i></p>
<dl>
<dd>Specifies incoming device to match. If the interface is loopback, the rule only matches packets originating from this host.</dl>
<p> <i>OutgoingInterface=</i></p>
<dl>
<dd>Specifies the outgoing device to match. The outgoing interface is only available for packets originating from local sockets that are bound to a device.</dl>
<p> <i>SourcePort=</i></p>
<dl>
<dd>Specifies the source IP port or IP port range match in forwarding information base (FIB) rules. A port range is specified by the lower and upper port separated by a dash. Defaults to unset.</dl>
<p> <i>DestinationPort=</i></p>
<dl>
<dd>Specifies the destination IP port or IP port range match in forwarding information base (FIB) rules. A port range is specified by the lower and upper port separated by a dash. Defaults to unset.</dl>
<p> <i>IPProtocol=</i></p>
<dl>
<dd>Specifies the IP protocol to match in forwarding information base (FIB) rules. Takes IP protocol name such as &quot;tcp&quot;, &quot;udp&quot; or &quot;sctp&quot;, or IP protocol number such as &quot;6&quot; for &quot;tcp&quot; or &quot;17&quot; for &quot;udp&quot;. Defaults to unset.</dl>
<p> <i>InvertRule=</i></p>
<dl>
<dd>A boolean. Specifies whether the rule is to be inverted. Defaults to false.</dl>
<p> <i>Family=</i></p>
<dl>
<dd>Takes a special value &quot;ipv4&quot;, &quot;ipv6&quot;, or &quot;both&quot;. By default, the address family is determined by the address specified in <i>To=</i> or <i>From=</i>. If neither <i>To=</i> nor <i>From=</i> are specified, then defaults to &quot;ipv4&quot;.</dl>
<p> <i>User=</i></p>
<dl>
<dd>Takes a username, a user ID, or a range of user IDs separated by a dash. Defaults to unset.</dl>
<p> <i>SuppressPrefixLength=</i></p>
<dl>
<dd>Takes a number <i>N</i> in the range 0&#8230;128 and rejects routing decisions that have a prefix length of <i>N</i> or less. Defaults to unset.</dl>
<p> <i>Type=</i></p>
<dl>
<dd>Specifies Routing Policy Database (RPDB) rule type. Takes one of &quot;blackhole&quot;, &quot;unreachable&quot; or &quot;prohibit&quot;.</dl>
<h2>[Nexthop] Section Options</h2>
<p>The [NextHop] section is used to manipulate entries in the kernel&#8217;s &quot;nexthop&quot; tables. The [NextHop] section accepts the following keys. Specify several [NextHop] sections to configure several hops. </p>
<p> <i>Id=</i></p>
<dl>
<dd>The id of the next hop. Takes an unsigned integer in the range 1&#8230;4294967295. If left unspecified, then automatically chosen by kernel.</dl>
<p> <i>Gateway=</i></p>
<dl>
<dd>As in the [Network] section.</dl>
<p> <i>Family=</i></p>
<dl>
<dd>Takes one of the special values &quot;ipv4&quot; or &quot;ipv6&quot;. By default, the family is determined by the address specified in <i>Gateway=</i>. If <i>Gateway=</i> is not specified, then defaults to &quot;ipv4&quot;.</dl>
<p> <i>OnLink=</i></p>
<dl>
<dd>Takes a boolean. If set to true, the kernel does not have to check if the gateway is reachable directly by the current machine (i.e., attached to the local network), so that we can insert the nexthop in the kernel table without it being complained about. Defaults to &quot;no&quot;.</dl>
<p> <i>Blackhole=</i></p>
<dl>
<dd>Takes a boolean. If enabled, packets to the corresponding routes are discarded silently, and <i>Gateway=</i> cannot be specified. Defaults to &quot;no&quot;.</dl>
<p> <i>Group=</i></p>
<dl>
<dd>Takes a whitespace separated list of nexthop IDs. Each ID must be in the range 1&#8230;4294967295. Optionally, each nexthop ID can take a weight after a colon (&quot;<i>id</i>[:<i>weight</i>]&quot;). The weight must be in the range 1&#8230;255. If the weight is not specified, then it is assumed that the weight is 1. This setting cannot be specified with <i>Gateway=</i>, <i>Family=</i>, <i>Blackhole=</i>. This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared. Defaults to unset.</dl>
<h2>[Route] Section Options</h2>
<p>The [Route] section accepts the following keys. Specify several [Route] sections to configure several routes. </p>
<p> <i>Gateway=</i></p>
<dl>
<dd>Takes the gateway address or the special values &quot;_dhcp4&quot; and &quot;_ipv6ra&quot;. If &quot;_dhcp4&quot; or &quot;_ipv6ra&quot; is set, then the gateway address provided by DHCPv4 or IPv6 RA is used.</dl>
<p> <i>GatewayOnLink=</i></p>
<dl>
<dd>Takes a boolean. If set to true, the kernel does not have to check if the gateway is reachable directly by the current machine (i.e., attached to the local network), so that we can insert the route in the kernel table without it being complained about. Defaults to &quot;no&quot;.</dl>
<p> <i>Destination=</i></p>
<dl>
<dd>The destination prefix of the route. Possibly followed by a slash and the prefix length. If omitted, a full-length host route is assumed.</dl>
<p> <i>Source=</i></p>
<dl>
<dd>The source prefix of the route. Possibly followed by a slash and the prefix length. If omitted, a full-length host route is assumed.</dl>
<p> <i>Metric=</i></p>
<dl>
<dd>The metric of the route. Takes an unsigned integer in the range 0&#8230;4294967295. Defaults to unset, and the kernel&#8217;s default will be used.</dl>
<p> <i>IPv6Preference=</i></p>
<dl>
<dd>Specifies the route preference as defined in m[blue]<code>RFC 4191</code>m[]<font SIZE="-2">[15]</font> for Router Discovery messages. Which can be one of &quot;low&quot; the route has a lowest priority, &quot;medium&quot; the route has a default priority or &quot;high&quot; the route has a highest priority.</dl>
<p> <i>Scope=</i></p>
<dl>
<dd>The scope of the IPv4 route, which can be &quot;global&quot;, &quot;site&quot;, &quot;link&quot;, &quot;host&quot;, or &quot;nowhere&quot;: </p>
<dl>
<dd>&bull; &quot;global&quot; means the route can reach hosts more than one hop away.</dl>
<dl>
<dd>&bull; &quot;site&quot; means an interior route in the local autonomous system.</dl>
<dl>
<dd>&bull; &quot;link&quot; means the route can only reach hosts on the local network (one hop away).</dl>
<dl>
<dd>&bull; &quot;host&quot; means the route will not leave the local machine (used for internal addresses like 127.0.0.1).</dl>
<dl>
<dd>&bull; &quot;nowhere&quot; means the destination doesn&#8217;t exist.</dl>
<p> For IPv4 route, defaults to &quot;host&quot; if <i>Type=</i> is &quot;local&quot; or &quot;nat&quot;, and &quot;link&quot; if <i>Type=</i> is &quot;broadcast&quot;, &quot;multicast&quot;, or &quot;anycast&quot;. In other cases, defaults to &quot;global&quot;. The value is not used for IPv6.</dl>
<p> <i>PreferredSource=</i></p>
<dl>
<dd>The preferred source address of the route. The address must be in the format described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3).</dl>
<p> <i>Table=</i></p>
<dl>
<dd>The table identifier for the route. Takes one of predefined names &quot;default&quot;, &quot;main&quot;, and &quot;local&quot;, and names defined in <i>RouteTable=</i> in <code><a href="/docs/linux/man/5-networkd-conf/">networkd.conf</a></code>(5), or a number between 1 and 4294967295. The table can be retrieved using <code>ip route show table </code><i>num</i>. If unset and <i>Type=</i> is &quot;local&quot;, &quot;broadcast&quot;, &quot;anycast&quot;, or &quot;nat&quot;, then &quot;local&quot; is used. In other cases, defaults to &quot;main&quot;.</dl>
<p> <i>Protocol=</i></p>
<dl>
<dd>The protocol identifier for the route. Takes a number between 0 and 255 or the special values &quot;kernel&quot;, &quot;boot&quot;, &quot;static&quot;, &quot;ra&quot; and &quot;dhcp&quot;. Defaults to &quot;static&quot;.</dl>
<p> <i>Type=</i></p>
<dl>
<dd>Specifies the type for the route. Takes one of &quot;unicast&quot;, &quot;local&quot;, &quot;broadcast&quot;, &quot;anycast&quot;, &quot;multicast&quot;, &quot;blackhole&quot;, &quot;unreachable&quot;, &quot;prohibit&quot;, &quot;throw&quot;, &quot;nat&quot;, and &quot;xresolve&quot;. If &quot;unicast&quot;, a regular route is defined, i.e. a route indicating the path to take to a destination network address. If &quot;blackhole&quot;, packets to the defined route are discarded silently. If &quot;unreachable&quot;, packets to the defined route are discarded and the ICMP message &quot;Host Unreachable&quot; is generated. If &quot;prohibit&quot;, packets to the defined route are discarded and the ICMP message &quot;Communication Administratively Prohibited&quot; is generated. If &quot;throw&quot;, route lookup in the current routing table will fail and the route selection process will return to Routing Policy Database (RPDB). Defaults to &quot;unicast&quot;.</dl>
<p> <i>InitialCongestionWindow=</i></p>
<dl>
<dd>The TCP initial congestion window is used during the start of a TCP connection. During the start of a TCP session, when a client requests a resource, the server&#8217;s initial congestion window determines how many packets will be sent during the initial burst of data without waiting for acknowledgement. Takes a number between 1 and 1023. Note that 100 is considered an extremely large value for this option. When unset, the kernel&#8217;s default (typically 10) will be used.</dl>
<p> <i>InitialAdvertisedReceiveWindow=</i></p>
<dl>
<dd>The TCP initial advertised receive window is the amount of receive data (in bytes) that can initially be buffered at one time on a connection. The sending host can send only that amount of data before waiting for an acknowledgment and window update from the receiving host. Takes a number between 1 and 1023. Note that 100 is considered an extremely large value for this option. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>QuickAck=</i></p>
<dl>
<dd>Takes a boolean. When true enables TCP quick ack mode for the route. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>FastOpenNoCookie=</i></p>
<dl>
<dd>Takes a boolean. When true enables TCP fastopen without a cookie on a per-route basis. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TTLPropagate=</i></p>
<dl>
<dd>Takes a boolean. When true enables TTL propagation at Label Switched Path (LSP) egress. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>The maximum transmission unit in bytes to set for the route. The usual suffixes K, M, G, are supported and are understood to the base of 1024. </p>
<p> Note that if IPv6 is enabled on the interface, and the MTU is chosen below 1280 (the minimum MTU for IPv6) it will automatically be increased to this value.</dl>
<p> <i>IPServiceType=</i></p>
<dl>
<dd>Takes string; &quot;CS6&quot; or &quot;CS4&quot;. Used to set IP service type to CS6 (network control) or CS4 (Realtime). Defaults to CS6.</dl>
<p> <i>TCPAdvertisedMaximumSegmentSize=</i></p>
<dl>
<dd>Specifies the Path MSS (in bytes) hints given on TCP layer. The usual suffixes K, M, G, are supported and are understood to the base of 1024. An unsigned integer in the range 1-4294967294. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MultiPathRoute=</i><i>address</i><i>[@</i><i>name</i><i>] [</i><i>weight</i><i>]</i></p>
<dl>
<dd>Configures multipath route. Multipath routing is the technique of using multiple alternative paths through a network. Takes gateway address. Optionally, takes a network interface name or index separated with &quot;@&quot;, and a weight in 1..256 for this multipath route separated with whitespace. This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared.</dl>
<p> <i>NextHop=</i></p>
<dl>
<dd>Specifies the nexthop id. Takes an unsigned integer in the range 1&#8230;4294967295. If set, the corresponding [NextHop] section must be configured. Defaults to unset.</dl>
<h2>[Dhcpv4] Section Options</h2>
<p>The [DHCPv4] section configures the DHCPv4 client, if it is enabled with the <i>DHCP=</i> setting described above: </p>
<p> <i>SendHostname=</i></p>
<dl>
<dd>When true (the default), the machine&#8217;s hostname (or the value specified with <i>Hostname=</i>, described below) will be sent to the DHCP server. Note that the hostname must consist only of 7-bit ASCII lower-case characters and no spaces or dots, and be formatted as a valid DNS domain name. Otherwise, the hostname is not sent even if this option is true.</dl>
<p> <i>Hostname=</i></p>
<dl>
<dd>Use this value for the hostname which is sent to the DHCP server, instead of machine&#8217;s hostname. Note that the specified hostname must consist only of 7-bit ASCII lower-case characters and no spaces or dots, and be formatted as a valid DNS domain name.</dl>
<p> <i>MUDURL=</i></p>
<dl>
<dd>When configured, the specified Manufacturer Usage Description (MUD) URL will be sent to the DHCPv4 server. Takes a URL of length up to 255 characters. A superficial verification that the string is a valid URL will be performed. DHCPv4 clients are intended to have at most one MUD URL associated with them. See m[blue]<code>RFC 8520</code>m[]<font SIZE="-2">[16]</font>. </p>
<p> MUD is an embedded software standard defined by the IETF that allows IoT device makers to advertise device specifications, including the intended communication patterns for their device when it connects to the network. The network can then use this to author a context-specific access policy, so the device functions only within those parameters.</dl>
<p> <i>ClientIdentifier=</i></p>
<dl>
<dd>The DHCPv4 client identifier to use. Takes one of <code>mac</code>, <code>duid</code> or <code>duid-only</code>. If set to <code>mac</code>, the MAC address of the link is used. If set to <code>duid</code>, an RFC4361-compliant Client ID, which is the combination of IAID and DUID (see below), is used. If set to <code>duid-only</code>, only DUID is used, this may not be RFC compliant, but some setups may require to use this. Defaults to <code>duid</code>.</dl>
<p> <i>VendorClassIdentifier=</i></p>
<dl>
<dd>The vendor class identifier used to identify vendor type and configuration.</dl>
<p> <i>UserClass=</i></p>
<dl>
<dd>A DHCPv4 client can use UserClass option to identify the type or category of user or applications it represents. The information contained in this option is a string that represents the user class of which the client is a member. Each class sets an identifying string of information to be used by the DHCP service to classify clients. Takes a whitespace-separated list of strings.</dl>
<p> <i>DUIDType=</i></p>
<dl>
<dd>Override the global <i>DUIDType=</i> setting for this network. See <code><a href="/docs/linux/man/5-networkd-conf/">networkd.conf</a></code>(5) for a description of possible values.</dl>
<p> <i>DUIDRawData=</i></p>
<dl>
<dd>Override the global <i>DUIDRawData=</i> setting for this network. See <code><a href="/docs/linux/man/5-networkd-conf/">networkd.conf</a></code>(5) for a description of possible values.</dl>
<p> <i>IAID=</i></p>
<dl>
<dd>The DHCP Identity Association Identifier (IAID) for the interface, a 32-bit unsigned integer.</dl>
<p> <i>Anonymize=</i></p>
<dl>
<dd>Takes a boolean. When true, the options sent to the DHCP server will follow the m[blue]<code>RFC 7844</code>m[]<font SIZE="-2">[17]</font> (Anonymity Profiles for DHCP Clients) to minimize disclosure of identifying information. Defaults to false. </p>
<p> This option should only be set to true when <i>MACAddressPolicy=</i> is set to <code>random</code> (see <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5)). </p>
<p> When true, <i>SendHostname=</i>, <i>ClientIdentifier=</i>, <i>VendorClassIdentifier=</i>, <i>UserClass=</i>, <i>RequestOptions=</i>, <i>SendOption=</i>, <i>SendVendorOption=</i>, and <i>MUDURL=</i> are ignored. </p>
<p> With this option enabled DHCP requests will mimic those generated by Microsoft Windows, in order to reduce the ability to fingerprint and recognize installations. This means DHCP request sizes will grow and lease data will be more comprehensive than normally, though most of the requested data is not actually used.</dl>
<p> <i>RequestOptions=</i></p>
<dl>
<dd>Sets request options to be sent to the server in the DHCPv4 request options list. A whitespace-separated list of integers in the range 1&#8230;254. Defaults to unset.</dl>
<p> <i>SendOption=</i></p>
<dl>
<dd>Send an arbitrary raw option in the DHCPv4 request. Takes a DHCP option number, data type and data separated with a colon (&quot;<i>option</i>:<i>type</i>:<i>value</i>&quot;). The option number must be an integer in the range 1&#8230;254. The type takes one of &quot;uint8&quot;, &quot;uint16&quot;, &quot;uint32&quot;, &quot;ipv4address&quot;, or &quot;string&quot;. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Defaults to unset.</dl>
<p> <i>SendVendorOption=</i></p>
<dl>
<dd>Send an arbitrary vendor option in the DHCPv4 request. Takes a DHCP option number, data type and data separated with a colon (&quot;<i>option</i>:<i>type</i>:<i>value</i>&quot;). The option number must be an integer in the range 1&#8230;254. The type takes one of &quot;uint8&quot;, &quot;uint16&quot;, &quot;uint32&quot;, &quot;ipv4address&quot;, or &quot;string&quot;. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Defaults to unset.</dl>
<p> <i>UseDNS=</i></p>
<dl>
<dd>When true (the default), the DNS servers received from the DHCP server will be used. </p>
<p> This corresponds to the <code>nameserver</code> option in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5).</dl>
<p> <i>RoutesToDNS=</i></p>
<dl>
<dd>When true, the routes to the DNS servers received from the DHCP server will be configured. When <i>UseDNS=</i> is disabled, this setting is ignored. Defaults to true.</dl>
<p> <i>UseNTP=</i></p>
<dl>
<dd>When true (the default), the NTP servers received from the DHCP server will be used by systemd-timesyncd.service.</dl>
<p> <i>RoutesToNTP=</i></p>
<dl>
<dd>When true, the routes to the NTP servers received from the DHCP server will be configured. When <i>UseNTP=</i> is disabled, this setting is ignored. Defaults to true.</dl>
<p> <i>UseSIP=</i></p>
<dl>
<dd>When true (the default), the SIP servers received from the DHCP server will be collected and made available to client programs.</dl>
<p> <i>UseMTU=</i></p>
<dl>
<dd>When true, the interface maximum transmission unit from the DHCP server will be used on the current link. If <i>MTUBytes=</i> is set, then this setting is ignored. Defaults to false.</dl>
<p> <i>UseHostname=</i></p>
<dl>
<dd>When true (the default), the hostname received from the DHCP server will be set as the transient hostname of the system.</dl>
<p> <i>UseDomains=</i></p>
<dl>
<dd>Takes a boolean, or the special value <code>route</code>. When true, the domain name received from the DHCP server will be used as DNS search domain over this link, similar to the effect of the <code>Domains=</code> setting. If set to <code>route</code>, the domain name received from the DHCP server will be used for routing DNS queries only, but not for searching, similar to the effect of the <code>Domains=</code> setting when the argument is prefixed with &quot;~&quot;. Defaults to true on Ubuntu. </p>
<p> It is recommended to enable this option only on trusted networks, as setting this affects resolution of all hostnames, in particular of single-label names. It is generally safer to use the supplied domain only as routing domain, rather than as search domain, in order to not have it affect local resolution of single-label names. </p>
<p> When set to true, this setting corresponds to the <code>domain</code> option in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5).</dl>
<p> <i>UseRoutes=</i></p>
<dl>
<dd>When true (the default), the static routes will be requested from the DHCP server and added to the routing table with a metric of 1024, and a scope of <code>global</code>, <code>link</code> or <code>host</code>, depending on the route&#8217;s destination and gateway. If the destination is on the local host, e.g., 127.x.x.x, or the same as the link&#8217;s own address, the scope will be set to <code>host</code>. Otherwise if the gateway is null (a direct route), a <code>link</code> scope will be used. For anything else, scope defaults to <code>global</code>.</dl>
<p> <i>RouteMetric=</i></p>
<dl>
<dd>Set the routing metric for routes specified by the DHCP server. Takes an unsigned integer in the range 0&#8230;4294967295. Defaults to 1024.</dl>
<p> <i>RouteTable=</i><i>num</i></p>
<dl>
<dd>The table identifier for DHCP routes (a number between 1 and 4294967295, or 0 to unset). The table can be retrieved using <code>ip route show table </code><i>num</i>. </p>
<p> When used in combination with <i>VRF=</i>, the VRF&#8217;s routing table is used when this parameter is not specified.</dl>
<p> <i>RouteMTUBytes=</i></p>
<dl>
<dd>Specifies the MTU for the DHCP routes. Please see the [Route] section for further details.</dl>
<p> <i>UseGateway=</i></p>
<dl>
<dd>When true, the gateway will be requested from the DHCP server and added to the routing table with a metric of 1024, and a scope of <code>link</code>. When unset, the value specified with <i>UseRoutes=</i> is used.</dl>
<p> <i>UseTimezone=</i></p>
<dl>
<dd>When true, the timezone received from the DHCP server will be set as timezone of the local system. Defaults to false.</dl>
<p> <i>FallbackLeaseLifetimeSec=</i></p>
<dl>
<dd>Allows to set DHCPv4 lease lifetime when DHCPv4 server does not send the lease lifetime. Takes one of &quot;forever&quot; or &quot;infinity&quot;. The latter means that the address never expires. Defaults to unset.</dl>
<p> <i>RequestBroadcast=</i></p>
<dl>
<dd>Request the server to use broadcast messages before the IP address has been configured. This is necessary for devices that cannot receive RAW packets, or that cannot receive packets at all before an IP address has been configured. On the other hand, this must not be enabled on networks where broadcasts are filtered out.</dl>
<p> <i>MaxAttempts=</i></p>
<dl>
<dd>Specifies how many times the DHCPv4 client configuration should be attempted. Takes a number or &quot;infinity&quot;. Defaults to &quot;infinity&quot;. Note that the time between retries is increased exponentially, up to approximately one per minute, so the network will not be overloaded even if this number is high. The default is suitable in most circumstances.</dl>
<p> <i>ListenPort=</i></p>
<dl>
<dd>Set the port from which the DHCP client packets originate.</dl>
<p> <i>DenyList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv4 addresses. DHCP offers from servers in the list are rejected. Note that if <i>AllowList=</i> is configured then <i>DenyList=</i> is ignored.</dl>
<p> <i>AllowList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv4 addresses. DHCP offers from servers in the list are accepted.</dl>
<p> <i>SendRelease=</i></p>
<dl>
<dd>When true, the DHCPv4 client sends a DHCP release packet when it stops. Defaults to true.</dl>
<p> <i>SendDecline=</i></p>
<dl>
<dd>A boolean. When &quot;true&quot;, the DHCPv4 client receives the IP address from the DHCP server. After a new IP is received, the DHCPv4 client performs IPv4 Duplicate Address Detection. If duplicate use is detected, the DHCPv4 client rejects the IP by sending a <code>DHCPDECLINE</code> packet and tries to obtain an IP address again. See m[blue]<code>RFC 5224</code>m[]<font SIZE="-2">[11]</font>. Defaults to &quot;unset&quot;.</dl>
<h2>[Dhcpv6] Section Options</h2>
<p>The [DHCPv6] section configures the DHCPv6 client, if it is enabled with the <i>DHCP=</i> setting described above, or invoked by the IPv6 Router Advertisement: </p>
<p> <i>MUDURL=</i>, <i>IAID=</i>, <i>DUIDType=</i>, <i>DUIDRawData=</i>, <i>RequestOptions=</i></p>
<dl>
<dd>As in the [DHCPv4] section.</dl>
<p> <i>SendOption=</i></p>
<dl>
<dd>As in the [DHCPv4] section, however because DHCPv6 uses 16-bit fields to store option numbers, the option number is an integer in the range 1&#8230;65536.</dl>
<p> <i>SendVendorOption=</i></p>
<dl>
<dd>Send an arbitrary vendor option in the DHCPv6 request. Takes an enterprise identifier, DHCP option number, data type, and data separated with a colon (&quot;<i>enterprise identifier</i>:<i>option</i>:<i>type</i>:<i>value</i>&quot;). Enterprise identifier is an unsigned integer in the range 1&#8230;4294967294. The option number must be an integer in the range 1&#8230;254. Data type takes one of &quot;uint8&quot;, &quot;uint16&quot;, &quot;uint32&quot;, &quot;ipv4address&quot;, &quot;ipv6address&quot;, or &quot;string&quot;. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Defaults to unset.</dl>
<p> <i>UserClass=</i></p>
<dl>
<dd>A DHCPv6 client can use User Class option to identify the type or category of user or applications it represents. The information contained in this option is a string that represents the user class of which the client is a member. Each class sets an identifying string of information to be used by the DHCP service to classify clients. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Takes a whitespace-separated list of strings. Note that currently <code>NUL</code> bytes are not allowed.</dl>
<p> <i>VendorClass=</i></p>
<dl>
<dd>A DHCPv6 client can use VendorClass option to identify the vendor that manufactured the hardware on which the client is running. The information contained in the data area of this option is contained in one or more opaque fields that identify details of the hardware configuration. Takes a whitespace-separated list of strings.</dl>
<p> <i>PrefixDelegationHint=</i></p>
<dl>
<dd>Takes an IPv6 address with prefix length in the same format as the <i>Address=</i> in the [Network] section. The DHCPv6 client will include a prefix hint in the DHCPv6 solicitation sent to the server. The prefix length must be in the range 1-128. Defaults to unset.</dl>
<p> <i>UseAddress=</i></p>
<dl>
<dd>When true (the default), the IP addresses provided by the DHCPv6 server will be assigned.</dl>
<p> <i>UseDNS=</i>, <i>UseNTP=</i>, <i>UseHostname=</i>, <i>UseDomains=</i></p>
<dl>
<dd>As in the [DHCPv4] section.</dl>
<p> <i>ForceDHCPv6PDOtherInformation=</i></p>
<dl>
<dd>Takes a boolean that enforces DHCPv6 stateful mode when the &#8216;Other information&#8217; bit is set in Router Advertisement messages. By default setting only the &#8216;O&#8217; bit in Router Advertisements makes DHCPv6 request network information in a stateless manner using a two-message Information Request and Information Reply message exchange. m[blue]<code>RFC 7084</code>m[]<font SIZE="-2">[19]</font>, requirement WPD-4, updates this behavior for a Customer Edge router so that stateful DHCPv6 Prefix Delegation is also requested when only the &#8216;O&#8217; bit is set in Router Advertisements. This option enables such a CE behavior as it is impossible to automatically distinguish the intention of the &#8216;O&#8217; bit otherwise. By default this option is set to false, enable it if no prefixes are delegated when the device should be acting as a CE router.</dl>
<p> <i>WithoutRA=</i></p>
<dl>
<dd>Allows DHCPv6 client to start without router advertisements&#8217;s managed or other address configuration flag. Takes one of &quot;solicit&quot; or &quot;information-request&quot;. Defaults to unset.</dl>
<p> <i>RapidCommit=</i></p>
<dl>
<dd>Takes a boolean. The DHCPv6 client can obtain configuration parameters from a DHCPv6 server through a rapid two-message exchange (solicit and reply). When the rapid commit option is enabled by both the DHCPv6 client and the DHCPv6 server, the two-message exchange is used, rather than the default four-message exchange (solicit, advertise, request, and reply). The two-message exchange provides faster client configuration and is beneficial in environments in which networks are under a heavy load. See m[blue]<code>RFC 3315</code>m[]<font SIZE="-2">[20]</font> for details. Defaults to true.</dl>
<h2>[Dhcpv6Prefixdelegation] Section Options</h2>
<p>The [DHCPv6PrefixDelegation] section configures delegated prefixes assigned by DHCPv6 server. The settings in this section are used only when <i>DHCPv6PrefixDelegation=</i> setting is enabled. </p>
<p> <i>SubnetId=</i></p>
<dl>
<dd>Configure a specific subnet ID on the interface from a (previously) received prefix delegation. You can either set &quot;auto&quot; (the default) or a specific subnet ID (as defined in m[blue]<code>RFC 4291</code>m[]<font SIZE="-2">[21]</font>, section 2.5.4), in which case the allowed value is hexadecimal, from 0 to 0x7fffffffffffffff inclusive.</dl>
<p> <i>Announce=</i></p>
<dl>
<dd>Takes a boolean. When enabled, and <i>IPv6SendRA=</i> in [Network] section is enabled, the delegated prefixes are distributed through the IPv6 Router Advertisement. Defaults to yes.</dl>
<p> <i>Assign=</i></p>
<dl>
<dd>Takes a boolean. Specifies whether to add an address from the delegated prefixes which are received from the WAN interface by the DHCPv6 Prefix Delegation. When true (on LAN interfce), the EUI-64 algorithm will be used by default to form an interface identifier from the delegated prefixes. See also <i>Token=</i> setting below. Defaults to yes.</dl>
<p> <i>Token=</i></p>
<dl>
<dd>Specifies an optional address generation mode for assigning an address in each delegated prefix. Takes an IPv6 address. When set, the lower bits of the supplied address is combined with the upper bits of each delegatad prefix received from the WAN interface by the DHCPv6 Prefix Delegation to form a complete address. When <i>Assign=</i> is disabled, this setting is ignored. When unset, the EUI-64 algorithm will be used to form addresses. Defaults to unset.</dl>
<p> <i>ManageTemporaryAddress=</i></p>
<dl>
<dd>As in the [Address] section, but defaults to true.</dl>
<p> <i>RouteMetric=</i></p>
<dl>
<dd>The metric of the route to the delegated prefix subnet. Takes an unsigned integer in the range 0&#8230;4294967295. When unset or set to 0, the kernel&#8217;s default value is used.</dl>
<h2>[Ipv6Acceptra] Section Options</h2>
<p>The [IPv6AcceptRA] section configures the IPv6 Router Advertisement (RA) client, if it is enabled with the <i>IPv6AcceptRA=</i> setting described above: </p>
<p> <i>UseDNS=</i></p>
<dl>
<dd>When true (the default), the DNS servers received in the Router Advertisement will be used. </p>
<p> This corresponds to the <code>nameserver</code> option in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5).</dl>
<p> <i>UseDomains=</i></p>
<dl>
<dd>Takes a boolean, or the special value &quot;route&quot;. When true, the domain name received via IPv6 Router Advertisement (RA) will be used as DNS search domain over this link, similar to the effect of the <code>Domains=</code> setting. If set to &quot;route&quot;, the domain name received via IPv6 RA will be used for routing DNS queries only, but not for searching, similar to the effect of the <code>Domains=</code> setting when the argument is prefixed with &quot;~&quot;. Defaults to true on Ubuntu. </p>
<p> It is recommended to enable this option only on trusted networks, as setting this affects resolution of all hostnames, in particular of single-label names. It is generally safer to use the supplied domain only as routing domain, rather than as search domain, in order to not have it affect local resolution of single-label names. </p>
<p> When set to true, this setting corresponds to the <code>domain</code> option in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5).</dl>
<p> <i>RouteTable=</i><i>num</i></p>
<dl>
<dd>The table identifier for the routes received in the Router Advertisement (a number between 1 and 4294967295, or 0 to unset). The table can be retrieved using <code>ip route show table </code><i>num</i>.</dl>
<p> <i>RouteMetric=</i></p>
<dl>
<dd>Set the routing metric for the routes received in the Router Advertisement. Takes an unsigned integer in the range 0&#8230;4294967295. Defaults to 1024.</dl>
<p> <i>UseAutonomousPrefix=</i></p>
<dl>
<dd>When true (the default), the autonomous prefix received in the Router Advertisement will be used and take precedence over any statically configured ones.</dl>
<p> <i>UseOnLinkPrefix=</i></p>
<dl>
<dd>When true (the default), the onlink prefix received in the Router Advertisement will be used and takes precedence over any statically configured ones.</dl>
<p> <i>RouterDenyList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 router addresses. Any information advertised by the listed router is ignored.</dl>
<p> <i>RouterAllowList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 router addresses. Only information advertised by the listed router is accepted. Note that if <i>RouterAllowList=</i> is configured then <i>RouterDenyList=</i> is ignored.</dl>
<p> <i>PrefixDenyList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 prefixes. IPv6 prefixes supplied via router advertisements in the list are ignored.</dl>
<p> <i>PrefixAllowList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 prefixes. IPv6 prefixes supplied via router advertisements in the list are allowed. Note that if <i>PrefixAllowList=</i> is configured then <i>PrefixDenyList=</i> is ignored.</dl>
<p> <i>RouteDenyList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 route prefixes. IPv6 route prefixes supplied via router advertisements in the list are ignored.</dl>
<p> <i>RouteAllowList=</i></p>
<dl>
<dd>A whitespace-separated list of IPv6 route prefixes. IPv6 route prefixes supplied via router advertisements in the list are allowed. Note that if <i>RouteAllowList=</i> is configured then <i>RouteDenyList=</i> is ignored.</dl>
<p> <i>DHCPv6Client=</i></p>
<dl>
<dd>Takes a boolean, or the special value &quot;always&quot;. When true or &quot;always&quot;, the DHCPv6 client will be started when the RA has the managed or other information flag. If set to &quot;always&quot;, the DHCPv6 client will also be started in managed mode when neither managed nor other information flag is set in the RA. Defaults to true.</dl>
<h2>[Dhcpserver] Section Options</h2>
<p>The [DHCPServer] section contains settings for the DHCP server, if enabled via the <i>DHCPServer=</i> option described above: </p>
<p> <i>ServerAddress=</i></p>
<dl>
<dd>Specifies server address for the DHCP server. Takes an IPv4 address with prefix length, for example &quot;192.168.0.1/24&quot;. This setting may be useful when the link on which the DHCP server is running has multiple static addresses. When unset, one of static addresses in the link will be automatically selected. Defaults to unset.</dl>
<p> <i>PoolOffset=</i>, <i>PoolSize=</i></p>
<dl>
<dd>Configures the pool of addresses to hand out. The pool is a contiguous sequence of IP addresses in the subnet configured for the server address, which does not include the subnet nor the broadcast address. <i>PoolOffset=</i> takes the offset of the pool from the start of subnet, or zero to use the default value. <i>PoolSize=</i> takes the number of IP addresses in the pool or zero to use the default value. By default, the pool starts at the first address after the subnet address and takes up the rest of the subnet, excluding the broadcast address. If the pool includes the server address (the default), this is reserved and not handed out to clients.</dl>
<p> <i>DefaultLeaseTimeSec=</i>, <i>MaxLeaseTimeSec=</i></p>
<dl>
<dd>Control the default and maximum DHCP lease time to pass to clients. These settings take time values in seconds or another common time unit, depending on the suffix. The default lease time is used for clients that did not ask for a specific lease time. If a client asks for a lease time longer than the maximum lease time, it is automatically shortened to the specified time. The default lease time defaults to 1h, the maximum lease time to 12h. Shorter lease times are beneficial if the configuration data in DHCP leases changes frequently and clients shall learn the new settings with shorter latencies. Longer lease times reduce the generated DHCP network traffic.</dl>
<p> <i>UplinkInterface=</i></p>
<dl>
<dd>Specifies name or index of uplink interface, or one of the special values &quot;:none&quot; and &quot;:auto&quot;. When emitting DNS, NTP, or SIP servers are enabled but no servers are specified, the servers configured in the uplink interface will be emitted. When &quot;:auto&quot;, the link which has default gateway with higher priority will be automatically selected. When &quot;:none&quot;, no uplink interface will be selected. Defaults to &quot;:auto&quot;.</dl>
<p> <i>EmitDNS=</i>, <i>DNS=</i></p>
<dl>
<dd><i>EmitDNS=</i> takes a boolean. Configures whether the DHCP leases handed out to clients shall contain DNS server information. Defaults to &quot;yes&quot;. The DNS servers to pass to clients may be configured with the <i>DNS=</i> option, which takes a list of IPv4 addresses. If the <i>EmitDNS=</i> option is enabled but no servers configured, the servers are automatically propagated from an &quot;uplink&quot; interface that has appropriate servers set. The &quot;uplink&quot; interface is determined by the default route of the system with the highest priority. Note that this information is acquired at the time the lease is handed out, and does not take uplink interfaces into account that acquire DNS server information at a later point. If no suitable uplink interface is found the DNS server data from /etc/resolv.conf is used. Also, note that the leases are not refreshed if the uplink network configuration changes. To ensure clients regularly acquire the most current uplink DNS server information, it is thus advisable to shorten the DHCP lease time via <i>MaxLeaseTimeSec=</i> described above.</dl>
<p> <i>EmitNTP=</i>, <i>NTP=</i>, <i>EmitSIP=</i>, <i>SIP=</i>, <i>EmitPOP3=</i>, <i>POP3=</i>, <i>EmitSMTP=</i>, <i>SMTP=</i>, <i>EmitLPR=</i>, <i>LPR=</i></p>
<dl>
<dd>Similar to the <i>EmitDNS=</i> and <i>DNS=</i> settings described above, these settings configure whether and what server information for the indicate protocol shall be emitted as part of the DHCP lease. The same syntax, propagation semantics and defaults apply as for <i>EmitDNS=</i> and <i>DNS=</i>.</dl>
<p> <i>EmitRouter=</i></p>
<dl>
<dd>Similar to the <i>EmitDNS=</i> setting described above, this setting configures whether the DHCP lease should contain the router option. The same syntax, propagation semantics and defaults apply as for <i>EmitDNS=</i>.</dl>
<p> <i>EmitTimezone=</i>, <i>Timezone=</i></p>
<dl>
<dd>Takes a boolean. Configures whether the DHCP leases handed out to clients shall contain timezone information. Defaults to &quot;yes&quot;. The <i>Timezone=</i> setting takes a timezone string (such as &quot;Europe/Berlin&quot; or &quot;UTC&quot;) to pass to clients. If no explicit timezone is set, the system timezone of the local host is propagated, as determined by the /etc/localtime symlink.</dl>
<p> <i>SendOption=</i></p>
<dl>
<dd>Send a raw option with value via DHCPv4 server. Takes a DHCP option number, data type and data (&quot;<i>option</i>:<i>type</i>:<i>value</i>&quot;). The option number is an integer in the range 1&#8230;254. The type takes one of &quot;uint8&quot;, &quot;uint16&quot;, &quot;uint32&quot;, &quot;ipv4address&quot;, &quot;ipv6address&quot;, or &quot;string&quot;. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Defaults to unset.</dl>
<p> <i>SendVendorOption=</i></p>
<dl>
<dd>Send a vendor option with value via DHCPv4 server. Takes a DHCP option number, data type and data (&quot;<i>option</i>:<i>type</i>:<i>value</i>&quot;). The option number is an integer in the range 1&#8230;254. The type takes one of &quot;uint8&quot;, &quot;uint16&quot;, &quot;uint32&quot;, &quot;ipv4address&quot;, or &quot;string&quot;. Special characters in the data string may be escaped using m[blue]<code>C-style escapes</code>m[]<font SIZE="-2">[18]</font>. This setting can be specified multiple times. If an empty string is specified, then all options specified earlier are cleared. Defaults to unset.</dl>
<p> <i>BindToInterface=</i></p>
<dl>
<dd>Takes a boolean value. When &quot;yes&quot;, DHCP server socket will be bound to its network interface and all socket communication will be restricted to this interface. Defaults to &quot;yes&quot;, except if <i>RelayTarget=</i> is used (see below), in which case it defaults defaults to &quot;no&quot;.</dl>
<p> <i>RelayTarget=</i></p>
<dl>
<dd>Takes an IPv4 address, which must be in the format described in <code><a href="/docs/linux/man/3-inet_pton/">inet_pton</a></code>(3). Turns this DHCP server into a DHCP relay agent. See m[blue]<code>RFC 1542</code>m[]<font SIZE="-2">[22]</font>. The address is the address of DHCP server or another relay agent to forward DHCP messages to and from.</dl>
<p> <i>RelayAgentCircuitId=</i></p>
<dl>
<dd>Specifies value for Agent Circuit ID suboption of Relay Agent Information option. Takes a string, which must be in the format &quot;string:<i>value</i>&quot;, where &quot;<i>value</i>&quot; should be replaced with the value of the suboption. Defaults to unset (means no Agent Circuit ID suboption is generated). Ignored if <i>RelayTarget=</i> is not specified.</dl>
<p> <i>RelayAgentRemoteId=</i></p>
<dl>
<dd>Specifies value for Agent Remote ID suboption of Relay Agent Information option. Takes a string, which must be in the format &quot;string:<i>value</i>&quot;, where &quot;<i>value</i>&quot; should be replaced with the value of the suboption. Defaults to unset (means no Agent Remote ID suboption is generated). Ignored if <i>RelayTarget=</i> is not specified.</dl>
<h2>[Dhcpserverstaticlease] Section Options</h2>
<p>The &quot;[DHCPServerStaticLease]&quot; section configures a static DHCP lease to assign a fixed IPv4 address to a specific device based on its MAC address. This section can be specified multiple times. </p>
<p> <i>MACAddress=</i></p>
<dl>
<dd>The hardware address of a device to match. This key is mandatory.</dl>
<p> <i>Address=</i></p>
<dl>
<dd>The IPv4 address that should be assigned to the device that was matched with <i>MACAddress=</i>. This key is mandatory.</dl>
<h2>[Ipv6Sendra] Section Options</h2>
<p>The [IPv6SendRA] section contains settings for sending IPv6 Router Advertisements and whether to act as a router, if enabled via the <i>IPv6SendRA=</i> option described above. IPv6 network prefixes or routes are defined with one or more [IPv6Prefix] or [IPv6RoutePrefix] sections. </p>
<p> <i>Managed=</i>, <i>OtherInformation=</i></p>
<dl>
<dd>Takes a boolean. Controls whether a DHCPv6 server is used to acquire IPv6 addresses on the network link when <i>Managed=</i> is set to &quot;true&quot; or if only additional network information can be obtained via DHCPv6 for the network link when <i>OtherInformation=</i> is set to &quot;true&quot;. Both settings default to &quot;false&quot;, which means that a DHCPv6 server is not being used.</dl>
<p> <i>RouterLifetimeSec=</i></p>
<dl>
<dd>Takes a timespan. Configures the IPv6 router lifetime in seconds. When set to 0, the host is not acting as a router. Defaults to 30 minutes.</dl>
<p> <i>RouterPreference=</i></p>
<dl>
<dd>Configures IPv6 router preference if <i>RouterLifetimeSec=</i> is non-zero. Valid values are &quot;high&quot;, &quot;medium&quot; and &quot;low&quot;, with &quot;normal&quot; and &quot;default&quot; added as synonyms for &quot;medium&quot; just to make configuration easier. See m[blue]<code>RFC 4191</code>m[]<font SIZE="-2">[15]</font> for details. Defaults to &quot;medium&quot;.</dl>
<p> <i>EmitDNS=</i>, <i>DNS=</i></p>
<dl>
<dd><i>DNS=</i> specifies a list of recursive DNS server IPv6 addresses that are distributed via Router Advertisement messages when <i>EmitDNS=</i> is true. <i>DNS=</i> also takes special value &quot;_link_local&quot;; in that case the IPv6 link local address is distributed. If <i>DNS=</i> is empty, DNS servers are read from the [Network] section. If the [Network] section does not contain any DNS servers either, DNS servers from the uplink with the highest priority default route are used. When <i>EmitDNS=</i> is false, no DNS server information is sent in Router Advertisement messages. <i>EmitDNS=</i> defaults to true.</dl>
<p> <i>EmitDomains=</i>, <i>Domains=</i></p>
<dl>
<dd>A list of DNS search domains distributed via Router Advertisement messages when <i>EmitDomains=</i> is true. If <i>Domains=</i> is empty, DNS search domains are read from the [Network] section. If the [Network] section does not contain any DNS search domains either, DNS search domains from the uplink with the highest priority default route are used. When <i>EmitDomains=</i> is false, no DNS search domain information is sent in Router Advertisement messages. <i>EmitDomains=</i> defaults to true.</dl>
<p> <i>DNSLifetimeSec=</i></p>
<dl>
<dd>Lifetime in seconds for the DNS server addresses listed in <i>DNS=</i> and search domains listed in <i>Domains=</i>.</dl>
<h2>[Ipv6Prefix] Section Options</h2>
<p>One or more [IPv6Prefix] sections contain the IPv6 prefixes that are announced via Router Advertisements. See m[blue]<code>RFC 4861</code>m[]<font SIZE="-2">[23]</font> for further details. </p>
<p> <i>AddressAutoconfiguration=</i>, <i>OnLink=</i></p>
<dl>
<dd>Takes a boolean to specify whether IPv6 addresses can be autoconfigured with this prefix and whether the prefix can be used for onlink determination. Both settings default to &quot;true&quot; in order to ease configuration.</dl>
<p> <i>Prefix=</i></p>
<dl>
<dd>The IPv6 prefix that is to be distributed to hosts. Similarly to configuring static IPv6 addresses, the setting is configured as an IPv6 prefix and its prefix length, separated by a &quot;/&quot; character. Use multiple [IPv6Prefix] sections to configure multiple IPv6 prefixes since prefix lifetimes, address autoconfiguration and onlink status may differ from one prefix to another.</dl>
<p> <i>PreferredLifetimeSec=</i>, <i>ValidLifetimeSec=</i></p>
<dl>
<dd>Preferred and valid lifetimes for the prefix measured in seconds. <i>PreferredLifetimeSec=</i> defaults to 604800 seconds (one week) and <i>ValidLifetimeSec=</i> defaults to 2592000 seconds (30 days).</dl>
<p> <i>Assign=</i></p>
<dl>
<dd>Takes a boolean. When true, adds an address from the prefix. Default to false.</dl>
<p> <i>RouteMetric=</i></p>
<dl>
<dd>The metric of the prefix route. Takes an unsigned integer in the range 0&#8230;4294967295. When unset or set to 0, the kernel&#8217;s default value is used. This setting is ignored when <i>Assign=</i> is false.</dl>
<h2>[Ipv6Routeprefix] Section Options</h2>
<p>One or more [IPv6RoutePrefix] sections contain the IPv6 prefix routes that are announced via Router Advertisements. See m[blue]<code>RFC 4191</code>m[]<font SIZE="-2">[15]</font> for further details. </p>
<p> <i>Route=</i></p>
<dl>
<dd>The IPv6 route that is to be distributed to hosts. Similarly to configuring static IPv6 routes, the setting is configured as an IPv6 prefix routes and its prefix route length, separated by a &quot;/&quot; character. Use multiple [IPv6PrefixRoutes] sections to configure multiple IPv6 prefix routes.</dl>
<p> <i>LifetimeSec=</i></p>
<dl>
<dd>Lifetime for the route prefix measured in seconds. <i>LifetimeSec=</i> defaults to 604800 seconds (one week).</dl>
<h2>[Bridge] Section Options</h2>
<p>The [Bridge] section accepts the following keys: </p>
<p> <i>UnicastFlood=</i></p>
<dl>
<dd>Takes a boolean. Controls whether the bridge should flood traffic for which an FDB entry is missing and the destination is unknown through this port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MulticastFlood=</i></p>
<dl>
<dd>Takes a boolean. Controls whether the bridge should flood traffic for which an MDB entry is missing and the destination is unknown through this port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MulticastToUnicast=</i></p>
<dl>
<dd>Takes a boolean. Multicast to unicast works on top of the multicast snooping feature of the bridge. Which means unicast copies are only delivered to hosts which are interested in it. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>NeighborSuppression=</i></p>
<dl>
<dd>Takes a boolean. Configures whether ARP and ND neighbor suppression is enabled for this port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>Learning=</i></p>
<dl>
<dd>Takes a boolean. Configures whether MAC address learning is enabled for this port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>HairPin=</i></p>
<dl>
<dd>Takes a boolean. Configures whether traffic may be sent back out of the port on which it was received. When this flag is false, then the bridge will not forward traffic back out of the receiving port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>UseBPDU=</i></p>
<dl>
<dd>Takes a boolean. Configures whether STP Bridge Protocol Data Units will be processed by the bridge port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>FastLeave=</i></p>
<dl>
<dd>Takes a boolean. This flag allows the bridge to immediately stop multicast traffic on a port that receives an IGMP Leave message. It is only used with IGMP snooping if enabled on the bridge. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>AllowPortToBeRoot=</i></p>
<dl>
<dd>Takes a boolean. Configures whether a given port is allowed to become a root port. Only used when STP is enabled on the bridge. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>ProxyARP=</i></p>
<dl>
<dd>Takes a boolean. Configures whether proxy ARP to be enabled on this port. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>ProxyARPWiFi=</i></p>
<dl>
<dd>Takes a boolean. Configures whether proxy ARP to be enabled on this port which meets extended requirements by IEEE 802.11 and Hotspot 2.0 specifications. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>MulticastRouter=</i></p>
<dl>
<dd>Configures this port for having multicast routers attached. A port with a multicast router will receive all multicast traffic. Takes one of &quot;no&quot; to disable multicast routers on this port, &quot;query&quot; to let the system detect the presence of routers, &quot;permanent&quot; to permanently enable multicast traffic forwarding on this port, or &quot;temporary&quot; to enable multicast routers temporarily on this port, not depending on incoming queries. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>Cost=</i></p>
<dl>
<dd>Sets the &quot;cost&quot; of sending packets of this interface. Each port in a bridge may have a different speed and the cost is used to decide which link to use. Faster interfaces should have lower costs. It is an integer value between 1 and 65535.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>Sets the &quot;priority&quot; of sending packets on this interface. Each port in a bridge may have a different priority which is used to decide which link to use. Lower value means higher priority. It is an integer value between 0 to 63. Networkd does not set any default, meaning the kernel default value of 32 is used.</dl>
<h2>[Bridgefdb] Section Options</h2>
<p>The [BridgeFDB] section manages the forwarding database table of a port and accepts the following keys. Specify several [BridgeFDB] sections to configure several static MAC table entries. </p>
<p> <i>MACAddress=</i></p>
<dl>
<dd>As in the [Network] section. This key is mandatory.</dl>
<p> <i>Destination=</i></p>
<dl>
<dd>Takes an IP address of the destination VXLAN tunnel endpoint.</dl>
<p> <i>VLANId=</i></p>
<dl>
<dd>The VLAN ID for the new static MAC table entry. If omitted, no VLAN ID information is appended to the new static MAC table entry.</dl>
<p> <i>VNI=</i></p>
<dl>
<dd>The VXLAN Network Identifier (or VXLAN Segment ID) to use to connect to the remote VXLAN tunnel endpoint. Takes a number in the range 1&#8230;16777215. Defaults to unset.</dl>
<p> <i>AssociatedWith=</i></p>
<dl>
<dd>Specifies where the address is associated with. Takes one of &quot;use&quot;, &quot;self&quot;, &quot;master&quot; or &quot;router&quot;. &quot;use&quot; means the address is in use. User space can use this option to indicate to the kernel that the fdb entry is in use. &quot;self&quot; means the address is associated with the port drivers fdb. Usually hardware. &quot;master&quot; means the address is associated with master devices fdb. &quot;router&quot; means the destination address is associated with a router. Note that it&#8217;s valid if the referenced device is a VXLAN type device and has route shortcircuit enabled. Defaults to &quot;self&quot;.</dl>
<p> <i>OutgoingInterface=</i></p>
<dl>
<dd>Specifies the name or index of the outgoing interface for the VXLAN device driver to reach the remote VXLAN tunnel endpoint. Defaults to unset.</dl>
<h2>[Bridgemdb] Section Options</h2>
<p>The [BridgeMDB] section manages the multicast membership entries forwarding database table of a port and accepts the following keys. Specify several [BridgeMDB] sections to configure several permanent multicast membership entries. </p>
<p> <i>MulticastGroupAddress=</i></p>
<dl>
<dd>Specifies the IPv4 or IPv6 multicast group address to add. This setting is mandatory.</dl>
<p> <i>VLANId=</i></p>
<dl>
<dd>The VLAN ID for the new entry. Valid ranges are 0 (no VLAN) to 4094. Optional, defaults to 0.</dl>
<h2>[Lldp] Section Options</h2>
<p>The [LLDP] section manages the Link Layer Discovery Protocol (LLDP) and accepts the following keys: </p>
<p> <i>MUDURL=</i></p>
<dl>
<dd>When configured, the specified Manufacturer Usage Descriptions (MUD) URL will be sent in LLDP packets. The syntax and semantics are the same as for <i>MUDURL=</i> in the [DHCPv4] section described above. </p>
<p> The MUD URLs received via LLDP packets are saved and can be read using the <code>sd_lldp_neighbor_get_mud_url()</code> function.</dl>
<h2>[Can] Section Options</h2>
<p>The [CAN] section manages the Controller Area Network (CAN bus) and accepts the following keys: </p>
<p> <i>BitRate=</i></p>
<dl>
<dd>The bitrate of CAN device in bits per second. The usual SI prefixes (K, M) with the base of 1000 can be used here. Takes a number in the range 1&#8230;4294967295.</dl>
<p> <i>SamplePoint=</i></p>
<dl>
<dd>Optional sample point in percent with one decimal (e.g. &quot;75%&quot;, &quot;87.5%&quot;) or permille (e.g. &quot;875‰&quot;).</dl>
<p> <i>DataBitRate=</i>, <i>DataSamplePoint=</i></p>
<dl>
<dd>The bitrate and sample point for the data phase, if CAN-FD is used. These settings are analogous to the <i>BitRate=</i> and <i>SamplePoint=</i> keys.</dl>
<p> <i>FDMode=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, CAN-FD mode is enabled for the interface. Note, that a bitrate and optional sample point should also be set for the CAN-FD data phase using the <i>DataBitRate=</i> and <i>DataSamplePoint=</i> keys.</dl>
<p> <i>FDNonISO=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, non-ISO CAN-FD mode is enabled for the interface. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>RestartSec=</i></p>
<dl>
<dd>Automatic restart delay time. If set to a non-zero value, a restart of the CAN controller will be triggered automatically in case of a bus-off condition after the specified delay time. Subsecond delays can be specified using decimals (e.g. &quot;0.1s&quot;) or a &quot;ms&quot; or &quot;us&quot; postfix. Using &quot;infinity&quot; or &quot;0&quot; will turn the automatic restart off. By default automatic restart is disabled.</dl>
<p> <i>Termination=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, the termination resistor will be selected for the bias network. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>TripleSampling=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, three samples (instead of one) are used to determine the value of a received bit by majority rule. When unset, the kernel&#8217;s default will be used.</dl>
<p> <i>BusErrorReporting=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, reporting of CAN bus errors is activated (those include single bit, frame format, and bit stuffing errors, unable to send dominant bit, unable to send recessive bit, bus overload, active error announcement, error occurred on transmission). When unset, the kernel&#8217;s default will be used. Note: in case of a CAN bus with a single CAN device, sending a CAN frame may result in a huge number of CAN bus errors.</dl>
<p> <i>ListenOnly=</i></p>
<dl>
<dd>Takes a boolean. When &quot;yes&quot;, listen-only mode is enabled. When the interface is in listen-only mode, the interface neither transmit CAN frames nor send ACK bit. Listen-only mode is important to debug CAN networks without interfering with the communication or acknowledge the CAN frame. When unset, the kernel&#8217;s default will be used.</dl>
<h2>[Qdisc] Section Options</h2>
<p>The [QDisc] section manages the traffic control queueing discipline (qdisc). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Specifies the parent Queueing Discipline (qdisc). Takes one of &quot;clsact&quot; or &quot;ingress&quot;. This is mandatory.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<h2>[Networkemulator] Section Options</h2>
<p>The [NetworkEmulator] section manages the queueing discipline (qdisc) of the network emulator. It can be used to configure the kernel packet scheduler and simulate packet delay and loss for UDP or TCP applications, or limit the bandwidth usage of a particular service to simulate internet connections. </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>DelaySec=</i></p>
<dl>
<dd>Specifies the fixed amount of delay to be added to all packets going out of the interface. Defaults to unset.</dl>
<p> <i>DelayJitterSec=</i></p>
<dl>
<dd>Specifies the chosen delay to be added to the packets outgoing to the network interface. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the maximum number of packets the qdisc may hold queued at a time. An unsigned integer in the range 0-4294967294. Defaults to 1000.</dl>
<p> <i>LossRate=</i></p>
<dl>
<dd>Specifies an independent loss probability to be added to the packets outgoing from the network interface. Takes a percentage value, suffixed with &quot;%&quot;. Defaults to unset.</dl>
<p> <i>DuplicateRate=</i></p>
<dl>
<dd>Specifies that the chosen percent of packets is duplicated before queuing them. Takes a percentage value, suffixed with &quot;%&quot;. Defaults to unset.</dl>
<h2>[Tokenbucketfilter] Section Options</h2>
<p>The [TokenBucketFilter] section manages the queueing discipline (qdisc) of token bucket filter (tbf). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>LatencySec=</i></p>
<dl>
<dd>Specifies the latency parameter, which specifies the maximum amount of time a packet can sit in the Token Bucket Filter (TBF). Defaults to unset.</dl>
<p> <i>LimitBytes=</i></p>
<dl>
<dd>Takes the number of bytes that can be queued waiting for tokens to become available. When the size is suffixed with K, M, or G, it is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset.</dl>
<p> <i>BurstBytes=</i></p>
<dl>
<dd>Specifies the size of the bucket. This is the maximum amount of bytes that tokens can be available for instantaneous transfer. When the size is suffixed with K, M, or G, it is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset.</dl>
<p> <i>Rate=</i></p>
<dl>
<dd>Specifies the device specific bandwidth. When suffixed with K, M, or G, the specified bandwidth is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. Defaults to unset.</dl>
<p> <i>MPUBytes=</i></p>
<dl>
<dd>The Minimum Packet Unit (MPU) determines the minimal token usage (specified in bytes) for a packet. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to zero.</dl>
<p> <i>PeakRate=</i></p>
<dl>
<dd>Takes the maximum depletion rate of the bucket. When suffixed with K, M, or G, the specified size is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. Defaults to unset.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>Specifies the size of the peakrate bucket. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset.</dl>
<h2>[Pie] Section Options</h2>
<p>The [PIE] section manages the queueing discipline (qdisc) of Proportional Integral controller-Enhanced (PIE). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the queue size in number of packets. When this limit is reached, incoming packets are dropped. An unsigned integer in the range 1&#8230;4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Flowqueuepie] Section Options</h2>
<p>The &quot;[FlowQueuePIE]&quot; section manages the queueing discipline (qdisc) of Flow Queue Proportional Integral controller-Enhanced (fq_pie). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the queue size in number of packets. When this limit is reached, incoming packets are dropped. An unsigned integer ranges 1 to 4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Stochasticfairblue] Section Options</h2>
<p>The [StochasticFairBlue] section manages the queueing discipline (qdisc) of stochastic fair blue (sfb). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the queue size in number of packets. When this limit is reached, incoming packets are dropped. An unsigned integer in the range 0-4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Stochasticfairnessqueueing] Section Options</h2>
<p>The [StochasticFairnessQueueing] section manages the queueing discipline (qdisc) of stochastic fairness queueing (sfq). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PerturbPeriodSec=</i></p>
<dl>
<dd>Specifies the interval in seconds for queue algorithm perturbation. Defaults to unset.</dl>
<h2>[Bfifo] Section Options</h2>
<p>The [BFIFO] section manages the queueing discipline (qdisc) of Byte limited Packet First In First Out (bfifo). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>LimitBytes=</i></p>
<dl>
<dd>Specifies the hard limit in bytes on the FIFO buffer size. The size limit prevents overflow in case the kernel is unable to dequeue packets as quickly as it receives them. When this limit is reached, incoming packets are dropped. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset and kernel default is used.</dl>
<h2>[Pfifo] Section Options</h2>
<p>The [PFIFO] section manages the queueing discipline (qdisc) of Packet First In First Out (pfifo). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the number of packets in the FIFO queue. The size limit prevents overflow in case the kernel is unable to dequeue packets as quickly as it receives them. When this limit is reached, incoming packets are dropped. An unsigned integer in the range 0-4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Pfifoheaddrop] Section Options</h2>
<p>The [PFIFOHeadDrop] section manages the queueing discipline (qdisc) of Packet First In First Out Head Drop (pfifo_head_drop). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>As in [PFIFO] section.</dl>
<h2>[Pfifofast] Section Options</h2>
<p>The [PFIFOFast] section manages the queueing discipline (qdisc) of Packet First In First Out Fast (pfifo_fast). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<h2>[Cake] Section Options</h2>
<p>The [CAKE] section manages the queueing discipline (qdisc) of Common Applications Kept Enhanced (CAKE). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>OverheadBytes=</i></p>
<dl>
<dd>Specifies that bytes to be addeded to the size of each packet. Bytes may be negative. Takes an integer in the range from -64 to 256. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>Bandwidth=</i></p>
<dl>
<dd>Specifies the shaper bandwidth. When suffixed with K, M, or G, the specified size is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Controlleddelay] Section Options</h2>
<p>The [ControlledDelay] section manages the queueing discipline (qdisc) of controlled delay (CoDel). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the queue size in number of packets. When this limit is reached, incoming packets are dropped. An unsigned integer in the range 0-4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>TargetSec=</i></p>
<dl>
<dd>Takes a timespan. Specifies the acceptable minimum standing/persistent queue delay. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>IntervalSec=</i></p>
<dl>
<dd>Takes a timespan. This is used to ensure that the measured minimum delay does not become too stale. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>ECN=</i></p>
<dl>
<dd>Takes a boolean. This can be used to mark packets instead of dropping them. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>CEThresholdSec=</i></p>
<dl>
<dd>Takes a timespan. This sets a threshold above which all packets are marked with ECN Congestion Experienced (CE). Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Deficitroundrobinscheduler] Section Options</h2>
<p>The [DeficitRoundRobinScheduler] section manages the queueing discipline (qdisc) of Deficit Round Robin Scheduler (DRR). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<h2>[Deficitroundrobinschedulerclass] Section Options</h2>
<p>The [DeficitRoundRobinSchedulerClass] section manages the traffic control class of Deficit Round Robin Scheduler (DRR). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, or a qdisc identifier. The qdisc identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>ClassId=</i></p>
<dl>
<dd>Configures the unique identifier of the class. It is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to unset.</dl>
<p> <i>QuantumBytes=</i></p>
<dl>
<dd>Specifies the amount of bytes a flow is allowed to dequeue before the scheduler moves to the next class. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to the MTU of the interface.</dl>
<h2>[Enhancedtransmissionselection] Section Options</h2>
<p>The [EnhancedTransmissionSelection] section manages the queueing discipline (qdisc) of Enhanced Transmission Selection (ETS). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>Bands=</i></p>
<dl>
<dd>Specifies the number of bands. An unsigned integer in the range 1-16. This value has to be at least large enough to cover the strict bands specified through the <i>StrictBands=</i> and bandwidth-sharing bands specified in <i>QuantumBytes=</i>.</dl>
<p> <i>StrictBands=</i></p>
<dl>
<dd>Specifies the number of bands that should be created in strict mode. An unsigned integer in the range 1-16.</dl>
<p> <i>QuantumBytes=</i></p>
<dl>
<dd>Specifies the white-space separated list of quantum used in band-sharing bands. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared.</dl>
<p> <i>PriorityMap=</i></p>
<dl>
<dd>The priority map maps the priority of a packet to a band. The argument is a whitespace separated list of numbers. The first number indicates which band the packets with priority 0 should be put to, the second is for priority 1, and so on. There can be up to 16 numbers in the list. If there are fewer, the default band that traffic with one of the unmentioned priorities goes to is the last one. Each band number must be in the range 0&#8230;255. This setting can be specified multiple times. If an empty string is assigned, then the all previous assignments are cleared.</dl>
<h2>[Genericrandomearlydetection] Section Options</h2>
<p>The [GenericRandomEarlyDetection] section manages the queueing discipline (qdisc) of Generic Random Early Detection (GRED). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>VirtualQueues=</i></p>
<dl>
<dd>Specifies the number of virtual queues. Takes an integer in the range 1&#8230;16. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>DefaultVirtualQueue=</i></p>
<dl>
<dd>Specifies the number of default virtual queue. This must be less than <i>VirtualQueue=</i>. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>GenericRIO=</i></p>
<dl>
<dd>Takes a boolean. It turns on the RIO-like buffering scheme. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Fairqueueingcontrolleddelay] Section Options</h2>
<p>The [FairQueueingControlledDelay] section manages the queueing discipline (qdisc) of fair queuing controlled delay (FQ-CoDel). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the real queue size. When this limit is reached, incoming packets are dropped. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>MemoryLimitBytes=</i></p>
<dl>
<dd>Specifies the limit on the total number of bytes that can be queued in this FQ-CoDel instance. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>Flows=</i></p>
<dl>
<dd>Specifies the number of flows into which the incoming packets are classified. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>TargetSec=</i></p>
<dl>
<dd>Takes a timespan. Specifies the acceptable minimum standing/persistent queue delay. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>IntervalSec=</i></p>
<dl>
<dd>Takes a timespan. This is used to ensure that the measured minimum delay does not become too stale. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>QuantumBytes=</i></p>
<dl>
<dd>Specifies the number of bytes used as the &quot;deficit&quot; in the fair queuing algorithm timespan. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>ECN=</i></p>
<dl>
<dd>Takes a boolean. This can be used to mark packets instead of dropping them. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>CEThresholdSec=</i></p>
<dl>
<dd>Takes a timespan. This sets a threshold above which all packets are marked with ECN Congestion Experienced (CE). Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Fairqueueing] Section Options</h2>
<p>The [FairQueueing] section manages the queueing discipline (qdisc) of fair queue traffic policing (FQ). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the real queue size. When this limit is reached, incoming packets are dropped. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>FlowLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the maximum number of packets queued per flow. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>QuantumBytes=</i></p>
<dl>
<dd>Specifies the credit per dequeue RR round, i.e. the amount of bytes a flow is allowed to dequeue at once. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>InitialQuantumBytes=</i></p>
<dl>
<dd>Specifies the initial sending rate credit, i.e. the amount of bytes a new flow is allowed to dequeue initially. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>MaximumRate=</i></p>
<dl>
<dd>Specifies the maximum sending rate of a flow. When suffixed with K, M, or G, the specified size is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>Buckets=</i></p>
<dl>
<dd>Specifies the size of the hash table used for flow lookups. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>OrphanMask=</i></p>
<dl>
<dd>Takes an unsigned integer. For packets not owned by a socket, fq is able to mask a part of hash and reduce number of buckets associated with the traffic. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>Pacing=</i></p>
<dl>
<dd>Takes a boolean, and enables or disables flow pacing. Defaults to unset and kernel&#8217;s default is used.</dl>
<p> <i>CEThresholdSec=</i></p>
<dl>
<dd>Takes a timespan. This sets a threshold above which all packets are marked with ECN Congestion Experienced (CE). Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Triviallinkequalizer] Section Options</h2>
<p>The [TrivialLinkEqualizer] section manages the queueing discipline (qdisc) of trivial link equalizer (teql). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>Id=</i></p>
<dl>
<dd>Specifies the interface ID &quot;N&quot; of teql. Defaults to &quot;0&quot;. Note that when teql is used, currently, the module <code>sch_teql</code> with <code>max_equalizers=N+1</code> option must be loaded before <code>systemd-networkd</code> is started.</dl>
<h2>[Hierarchytokenbucket] Section Options</h2>
<p>The [HierarchyTokenBucket] section manages the queueing discipline (qdisc) of hierarchy token bucket (htb). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>DefaultClass=</i></p>
<dl>
<dd>Takes the minor id in hexadecimal of the default class. Unclassified traffic gets sent to the class. Defaults to unset.</dl>
<p> <i>RateToQuantum=</i></p>
<dl>
<dd>Takes an unsigned integer. The DRR quantums are calculated by dividing the value configured in <i>Rate=</i> by <i>RateToQuantum=</i>.</dl>
<h2>[Hierarchytokenbucketclass] Section Options</h2>
<p>The [HierarchyTokenBucketClass] section manages the traffic control class of hierarchy token bucket (htb). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, or a qdisc identifier. The qdisc identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>ClassId=</i></p>
<dl>
<dd>Configures the unique identifier of the class. It is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to unset.</dl>
<p> <i>Priority=</i></p>
<dl>
<dd>Specifies the priority of the class. In the round-robin process, classes with the lowest priority field are tried for packets first.</dl>
<p> <i>QuantumBytes=</i></p>
<dl>
<dd>Specifies how many bytes to serve from leaf at once. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024.</dl>
<p> <i>MTUBytes=</i></p>
<dl>
<dd>Specifies the maximum packet size we create. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024.</dl>
<p> <i>OverheadBytes=</i></p>
<dl>
<dd>Takes an unsigned integer which specifies per-packet size overhead used in rate computations. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024.</dl>
<p> <i>Rate=</i></p>
<dl>
<dd>Specifies the maximum rate this class and all its children are guaranteed. When suffixed with K, M, or G, the specified size is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. This setting is mandatory.</dl>
<p> <i>CeilRate=</i></p>
<dl>
<dd>Specifies the maximum rate at which a class can send, if its parent has bandwidth to spare. When suffixed with K, M, or G, the specified size is parsed as Kilobits, Megabits, or Gigabits, respectively, to the base of 1000. When unset, the value specified with <i>Rate=</i> is used.</dl>
<p> <i>BufferBytes=</i></p>
<dl>
<dd>Specifies the maximum bytes burst which can be accumulated during idle period. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024.</dl>
<p> <i>CeilBufferBytes=</i></p>
<dl>
<dd>Specifies the maximum bytes burst for ceil which can be accumulated during idle period. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024.</dl>
<h2>[Heavyhitterfilter] Section Options</h2>
<p>The [HeavyHitterFilter] section manages the queueing discipline (qdisc) of Heavy Hitter Filter (hhf). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<p> <i>PacketLimit=</i></p>
<dl>
<dd>Specifies the hard limit on the queue size in number of packets. When this limit is reached, incoming packets are dropped. An unsigned integer in the range 0-4294967294. Defaults to unset and kernel&#8217;s default is used.</dl>
<h2>[Quickfairqueueing] Section Options</h2>
<p>The [QuickFairQueueing] section manages the queueing discipline (qdisc) of Quick Fair Queueing (QFQ). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, &quot;clsact&quot;, &quot;ingress&quot; or a class identifier. The class identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>Handle=</i></p>
<dl>
<dd>Configures the major number of unique identifier of the qdisc, known as the handle. Takes a hexadecimal number in the range 0x1-0xffff. Defaults to unset.</dl>
<h2>[Quickfairqueueingclass] Section Options</h2>
<p>The [QuickFairQueueingClass] section manages the traffic control class of Quick Fair Queueing (qfq). </p>
<p> <i>Parent=</i></p>
<dl>
<dd>Configures the parent Queueing Discipline (qdisc). Takes one of &quot;root&quot;, or a qdisc identifier. The qdisc identifier is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to &quot;root&quot;.</dl>
<p> <i>ClassId=</i></p>
<dl>
<dd>Configures the unique identifier of the class. It is specified as the major and minor numbers in hexadecimal in the range 0x1-Oxffff separated with a colon (&quot;major:minor&quot;). Defaults to unset.</dl>
<p> <i>Weight=</i></p>
<dl>
<dd>Specifies the weight of the class. Takes an integer in the range 1&#8230;1023. Defaults to unset in which case the kernel default is used.</dl>
<p> <i>MaxPacketBytes=</i></p>
<dl>
<dd>Specifies the maximum packet size in bytes for the class. When suffixed with K, M, or G, the specified size is parsed as Kilobytes, Megabytes, or Gigabytes, respectively, to the base of 1024. When unset, the kernel default is used.</dl>
<h2>[Bridgevlan] Section Options</h2>
<p>The [BridgeVLAN] section manages the VLAN ID configuration of a bridge port and accepts the following keys. Specify several [BridgeVLAN] sections to configure several VLAN entries. The <i>VLANFiltering=</i> option has to be enabled, see the [Bridge] section in <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5). </p>
<p> <i>VLAN=</i></p>
<dl>
<dd>The VLAN ID allowed on the port. This can be either a single ID or a range M-N. VLAN IDs are valid from 1 to 4094.</dl>
<p> <i>EgressUntagged=</i></p>
<dl>
<dd>The VLAN ID specified here will be used to untag frames on egress. Configuring <i>EgressUntagged=</i> implicates the use of <i>VLAN=</i> above and will enable the VLAN ID for ingress as well. This can be either a single ID or a range M-N.</dl>
<p> <i>PVID=</i></p>
<dl>
<dd>The Port VLAN ID specified here is assigned to all untagged frames at ingress. <i>PVID=</i> can be used only once. Configuring <i>PVID=</i> implicates the use of <i>VLAN=</i> above and will enable the VLAN ID for ingress as well.</dl>
<h2>Examples</h2>
<p><code>Example 1. Static network configuration</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/50-static.network
[Match]
Name=enp2s0
[Network]
Address=192.168.0.15/24
Gateway=192.168.0.1</pre>
</dl>
<p> This brings interface &quot;enp2s0&quot; up with a static address. The specified gateway will be used for a default route. </p>
<p> <code>Example 2. DHCP on ethernet links</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/80-dhcp.network
[Match]
Name=en*
[Network]
DHCP=yes</pre>
</dl>
<p> This will enable DHCPv4 and DHCPv6 on all interfaces with names starting with &quot;en&quot; (i.e. ethernet interfaces). </p>
<p> <code>Example 3. IPv6 Prefix Delegation</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/55-ipv6-pd-upstream.network
[Match]
Name=enp1s0
[Network]
DHCP=ipv6</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/56-ipv6-pd-downstream.network
[Match]
Name=enp2s0
[Network]
IPv6SendRA=yes
DHCPv6PrefixDelegation=yes</pre>
</dl>
<p> This will enable DHCPv6-PD on the interface enp1s0 as an upstream interface where the DHCPv6 client is running and enp2s0 as a downstream interface where the prefix is delegated to. The delegated prefixes are distributed by IPv6 Router Advertisement on the downstream network. </p>
<p> <code>Example 4. A bridge with two enslaved links</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/25-bridge-static.network
[Match]
Name=bridge0
[Network]
Address=192.168.0.15/24
Gateway=192.168.0.1
DNS=192.168.0.1</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/25-bridge-slave-interface-1.network
[Match]
Name=enp2s0
[Network]
Bridge=bridge0</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/25-bridge-slave-interface-2.network
[Match]
Name=wlp3s0
[Network]
Bridge=bridge0</pre>
</dl>
<p> This creates a bridge and attaches devices &quot;enp2s0&quot; and &quot;wlp3s0&quot; to it. The bridge will have the specified static address and network assigned, and a default route via the specified gateway will be added. The specified DNS server will be added to the global list of DNS resolvers. </p>
<p> <code>Example 5. Bridge port with VLAN forwarding</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/25-bridge-slave-interface-1.network
[Match]
Name=enp2s0
[Network]
Bridge=bridge0
[BridgeVLAN]
VLAN=1-32
PVID=42
EgressUntagged=42
[BridgeVLAN]
VLAN=100-200
[BridgeVLAN]
EgressUntagged=300-400</pre>
</dl>
<p> This overrides the configuration specified in the previous example for the interface &quot;enp2s0&quot;, and enables VLAN on that bridge port. VLAN IDs 1-32, 42, 100-400 will be allowed. Packets tagged with VLAN IDs 42, 300-400 will be untagged when they leave on this interface. Untagged packets which arrive on this interface will be assigned VLAN ID 42. </p>
<p> <code>Example 6. Various tunnels</code> </p>
<dl>
<dd>
<pre>/etc/systemd/network/25-tunnels.network
[Match]
Name=ens1
[Network]
Tunnel=ipip-tun
Tunnel=sit-tun
Tunnel=gre-tun
Tunnel=vti-tun</pre>
</dl>
<dl>
<dd>
<pre>/etc/systemd/network/25-tunnel-ipip.netdev
[NetDev]
Name=ipip-tun
Kind=ipip</pre>
</dl>
<dl>
<dd>
<pre>/etc/systemd/network/25-tunnel-sit.netdev
[NetDev]
Name=sit-tun
Kind=sit</pre>
</dl>
<dl>
<dd>
<pre>/etc/systemd/network/25-tunnel-gre.netdev
[NetDev]
Name=gre-tun
Kind=gre</pre>
</dl>
<dl>
<dd>
<pre>/etc/systemd/network/25-tunnel-vti.netdev
[NetDev]
Name=vti-tun
Kind=vti</pre>
</dl>
<p> This will bring interface &quot;ens1&quot; up and create an IPIP tunnel, a SIT tunnel, a GRE tunnel, and a VTI tunnel using it. </p>
<p> <code>Example 7. A bond device</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/30-bond1.network
[Match]
Name=bond1
[Network]
DHCP=ipv6</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/30-bond1.netdev
[NetDev]
Name=bond1
Kind=bond</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/30-bond1-dev1.network
[Match]
MACAddress=52:54:00:e9:64:41
[Network]
Bond=bond1</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/30-bond1-dev2.network
[Match]
MACAddress=52:54:00:e9:64:42
[Network]
Bond=bond1</pre>
</dl>
<p> This will create a bond device &quot;bond1&quot; and enslave the two devices with MAC addresses 52:54:00:e9:64:41 and 52:54:00:e9:64:42 to it. IPv6 DHCP will be used to acquire an address. </p>
<p> <code>Example 8. Virtual Routing and Forwarding (VRF)</code> </p>
<p> Add the &quot;bond1&quot; interface to the VRF master interface &quot;vrf1&quot;. This will redirect routes generated on this interface to be within the routing table defined during VRF creation. For kernels before 4.8 traffic won&#8217;t be redirected towards the VRFs routing table unless specific ip-rules are added. </p>
<dl>
<dd>
<pre># /etc/systemd/network/25-vrf.network
[Match]
Name=bond1
[Network]
VRF=vrf1</pre>
</dl>
<p> <code>Example 9. MacVTap</code> </p>
<p> This brings up a network interface &quot;macvtap-test&quot; and attaches it to &quot;enp0s25&quot;. </p>
<dl>
<dd>
<pre># /lib/systemd/network/25-macvtap.network
[Match]
Name=enp0s25
[Network]
MACVTAP=macvtap-test</pre>
</dl>
<p> <code>Example 10. A Xfrm interface with physical underlying device.</code> </p>
<dl>
<dd>
<pre># /etc/systemd/network/27-xfrm.netdev
[NetDev]
Name=xfrm0
Kind=xfrm
[Xfrm]
InterfaceId=7</pre>
</dl>
<dl>
<dd>
<pre># /etc/systemd/network/27-eth0.network
[Match]
Name=eth0
[Network]
Xfrm=xfrm0</pre>
</dl>
<p> This creates a &quot;xfrm0&quot; interface and binds it to the &quot;eth0&quot; device. This allows hardware based ipsec offloading to the &quot;eth0&quot; nic. If offloading is not needed, xfrm interfaces can be assigned to the &quot;lo&quot; device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5), <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 7217</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc7217">https://tools.ietf.org/html/rfc7217</a></dl>
<dt> 2.</p>
<dd>Link-Local Multicast Name Resolution</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4795">https://tools.ietf.org/html/rfc4795</a></dl>
<dt> 3.</p>
<dd>Multicast DNS</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6762">https://tools.ietf.org/html/rfc6762</a></dl>
<dt> 4.</p>
<dd>DNS-over-TLS</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc7858">https://tools.ietf.org/html/rfc7858</a></dl>
<dt> 5.</p>
<dd>DNSSEC</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4033">https://tools.ietf.org/html/rfc4033</a></dl>
<dt> 6.</p>
<dd>IEEE 802.1AB-2016</p>
<dl>
<dd><a rel="nofollow" href="https://standards.ieee.org/findstds/standard/802.1AB-2016.html">https://standards.ieee.org/findstds/standard/802.1AB-2016.html</a></dl>
<dt> 7.</p>
<dd>ip-sysctl.txt</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt">https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt</a></dl>
<dt> 8.</p>
<dd>RFC 4941</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4941">https://tools.ietf.org/html/rfc4941</a></dl>
<dt> 9.</p>
<dd>RFC 1027</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc1027">https://tools.ietf.org/html/rfc1027</a></dl>
<dt>10.</p>
<dd>RFC 6275</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6275">https://tools.ietf.org/html/rfc6275</a></dl>
<dt>11.</p>
<dd>RFC 5227</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc5227">https://tools.ietf.org/html/rfc5227</a></dl>
<dt>12.</p>
<dd>RFC 4862</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4862">https://tools.ietf.org/html/rfc4862</a></dl>
<dt>13.</p>
<dd>RFC 3041</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3041">https://tools.ietf.org/html/rfc3041</a></dl>
<dt>14.</p>
<dd>RFC 3484</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3484">https://tools.ietf.org/html/rfc3484</a></dl>
<dt>15.</p>
<dd>RFC 4191</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4191">https://tools.ietf.org/html/rfc4191</a></dl>
<dt>16.</p>
<dd>RFC 8520</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc8520">https://tools.ietf.org/html/rfc8520</a></dl>
<dt>17.</p>
<dd>RFC 7844</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc7844">https://tools.ietf.org/html/rfc7844</a></dl>
<dt>18.</p>
<dd>C-style escapes</p>
<dl>
<dd><a rel="nofollow" href="https://en.wikipedia.org/wiki/Escape_sequences_in_C#Table_of_escape_sequences">https://en.wikipedia.org/wiki/Escape_sequences_in_C#Table_of_escape_sequences</a></dl>
<dt>19.</p>
<dd>RFC 7084</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc7084">https://tools.ietf.org/html/rfc7084</a></dl>
<dt>20.</p>
<dd>RFC 3315</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3315#section-17.2.1">https://tools.ietf.org/html/rfc3315#section-17.2.1</a></dl>
<dt>21.</p>
<dd>RFC 4291</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4291#section-2.5.4">https://tools.ietf.org/html/rfc4291#section-2.5.4</a></dl>
<dt>22.</p>
<dd>RFC 1542</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc1542">https://tools.ietf.org/html/rfc1542</a></dl>
<dt>23.</p>
<dd>RFC 4861</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4861">https://tools.ietf.org/html/rfc4861</a></dl>
