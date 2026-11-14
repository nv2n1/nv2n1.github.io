---
title: "netplan(5)"
name: "netplan"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netplan/"
description: "netplan – YAML network configuration abstraction for various backends"
---

<p>netplan &#8211; YAML network configuration abstraction for various backends</p>
<h2>Synopsis</h2>
<p>netplan [ COMMAND | help ]</p>
<h2>Commands</h2>
<p>See netplan help for a list of available commands on this system.</p>
<h2>Description</h2>
<h3>Introduction</h3>
<p>Distribution installers, cloud instantiation, image builds for particular devices, or any other way to deploy an operating system put its desired network configuration into YAML configuration file(s). During early boot, the netplan &#8220;network renderer&#8221; runs which reads /{lib,etc,run}/netplan/*.yaml and writes configuration to /run to hand off control of devices to the specified networking daemon.</p>
<dl>
<dt>&bull;</p>
<dd>Configured devices get handled by systemd-networkd by default, unless explicitly marked as managed by a specific renderer (NetworkManager)</p>
<dt>&bull;</p>
<dd>Devices not covered by the network config do not get touched at all.</p>
<dt>&bull;</p>
<dd>Usable in initramfs (few dependencies and fast)</p>
<dt>&bull;</p>
<dd>No persistent generated config, only original YAML config</p>
<dt>&bull;</p>
<dd>Parser supports multiple config files to allow applications like libvirt or lxd to package up expected network config (virbr0, lxdbr0), or to change the global default policy to use NetworkManager for everything.</p>
<dt>&bull;</p>
<dd>Retains the flexibility to change backends/policy later or adjust to removing NetworkManager, as generated configuration is ephemeral.</dl>
<h3>General structure</h3>
<p>netplan&#8217;s configuration files use the YAML (<a rel="nofollow" href="http://yaml.org/spec/1.1/current.html)">http://yaml.org/spec/1.1/current.html)</a> format. All /{lib,etc,run}/netplan/*.yaml are considered. Lexicographically later files (regardless of in which directory they are) amend (new mapping keys) or override (same mapping keys) previous ones. A file in /run/netplan completely shadows a file with same name in /etc/netplan, and a file in either of those directories shadows a file with the same name in /lib/netplan. </p>
<p> The top-level node in a netplan configuration file is a network: mapping that contains version: 2 (the YAML currently being used by curtin, MaaS, etc. is version 1), and then device definitions grouped by their type, such as ethernets:, modems:, wifis:, or bridges:. These are the types that our renderer can understand and are supported by our backends. </p>
<p> Each type block contains device definitions as a map where the keys (called &#8220;configuration IDs&#8221;) are defined as below.</p>
<h3>Device configuration IDs</h3>
<p>The key names below the per-device-type definition maps (like ethernets:) are called &#8220;ID&#8221;s. They must be unique throughout the entire set of configuration files. Their primary purpose is to serve as anchor names for composite devices, for example to enumerate the members of a bridge that is currently being defined. </p>
<p> If an interface is defined with an ID in a configuration file; it will be brought up by the applicable renderer. To not have netplan touch an interface at all, it should be completely omitted from the netplan configuration files. </p>
<p> There are two physically/structurally different classes of device definitions, and the ID field has a different interpretation for each:</p>
<dl>
<dt><code>Physical devices</code></p>
<dd>(Examples: ethernet, modem, wifi) These can dynamically come and go between reboots and even during runtime (hotplugging). In the generic case, they can be selected by match: rules on desired properties, such as name/name pattern, MAC address, driver, or device paths. In general these will match any number of devices (unless they refer to properties which are unique such as the full path or MAC address), so without further knowledge about the hardware these will always be considered as a group.</p>
<dl>
<dd>It is valid to specify no match rules at all, in which case the ID field is simply the interface name to be matched. This is mostly useful if you want to keep simple cases simple, and it&#8217;s how network device configuration has been done for a long time. </p>
<p> If there are match: rules, then the ID field is a purely opaque name which is only being used for references from definitions of compound devices in the config.</dl>
<dt><code>Virtual devices</code></p>
<dd>(Examples: veth, bridge, bond) These are fully under the control of the config file(s) and the network stack. I. e. these devices are being created instead of matched. Thus match: and set-name: are not applicable for these, and the ID field is the name of the created virtual device.</dl>
<h3>Common properties for physical device types</h3>
<dl>
<dt>match (mapping)</p>
<dd>This selects a subset of available physical devices by various hardware properties. The following configuration will then apply to all matching devices, as soon as they appear. All specified properties must match.</p>
<dl>
<dd>
<dl>
<dt>name (scalar)</p>
<dd>Current interface name. Globs are supported, and the primary use case for matching on names, as selecting one fixed name can be more easily achieved with having no match: at all and just using the ID (see above). Note that currently only networkd supports globbing, NetworkManager does not.</p>
<dt>macaddress (scalar)</p>
<dd>Device&#8217;s MAC address in the form &#8220;XX:XX:XX:XX:XX:XX&#8221;. Globs are not allowed.</p>
<dt>driver (scalar)</p>
<dd>Kernel driver name, corresponding to the DRIVER udev property. Globs are supported. Matching on driver is only supported with networkd.</dl>
<p> Examples:</p>
<dl>
<dt>&bull;</p>
<dd>all cards on second PCI bus:</p>
<dl>
<dd>
<dl>
<dd>
<pre> match:
 name: enp2*</pre>
</dl>
</dl>
<dt>&bull;</p>
<dd>fixed MAC address:</p>
<dl>
<dd>
<dl>
<dd>
<pre> match:
 macaddress: 11:22:33:AA:BB:FF</pre>
</dl>
</dl>
<dt>&bull;</p>
<dd>first card of driver ixgbe:</p>
<dl>
<dd>
<dl>
<dd>
<pre> match:
 driver: ixgbe
 name: en*s0</pre>
</dl>
</dl>
</dl>
</dl>
<dt>set-name (scalar)</p>
<dd>When matching on unique properties such as path or MAC, or with additional assumptions such as &#8220;there will only ever be one wifi device&#8221;, match rules can be written so that they only match one device. Then this property can be used to give that device a more specific/desirable/nicer name than the default from udev&#8217;s ifnames. Any additional device that satisfies the match rules will then fail to get renamed and keep the original kernel name (and dmesg will show an error).</p>
<dt>wakeonlan (bool)</p>
<dd>Enable wake on LAN. Off by default.</p>
<dt>emit-lldp (bool)</p>
<dd>(networkd backend only) Whether to emit LLDP packets. Off by default.</dl>
<h3>Common properties for all device types</h3>
<dl>
<dt>renderer (scalar)</p>
<dd>Use the given networking backend for this definition. Currently supported are networkd and NetworkManager. This property can be specified globally in networks:, for a device type (in e. g. ethernets:) or for a particular device definition. Default is networkd.</p>
<dl>
<dd>The renderer property has one additional acceptable value for vlan objects (i. e. defined in vlans:): sriov. If a vlan is defined with the sriov renderer for an SR-IOV Virtual Function interface, this causes netplan to set up a hardware VLAN filter for it. There can be only one defined per VF.</dl>
<dt>dhcp4 (bool)</p>
<dd>Enable DHCP for IPv4. Off by default.</p>
<dt>dhcp6 (bool)</p>
<dd>Enable DHCP for IPv6. Off by default. This covers both stateless DHCP &#8211; where the DHCP server supplies information like DNS nameservers but not the IP address &#8211; and stateful DHCP, where the server provides both the address and the other information.</p>
<dl>
<dd>If you are in an IPv6-only environment with completely stateless autoconfiguration (SLAAC with RDNSS), this option can be set to cause the interface to be brought up. (Setting accept-ra alone is not sufficient.) Autoconfiguration will still honour the contents of the router advertisement and only use DHCP if requested in the RA. </p>
<p> Note that <a href="/docs/linux/man/8-rdnssd/">rdnssd</a>(8) is required to use RDNSS with networkd. No extra software is required for NetworkManager.</dl>
<dt>ipv6-mtu (scalar)</p>
<dd>Set the IPv6 MTU (only supported with networkd backend). Note that needing to set this is an unusual requirement.</p>
<dl>
<dd>Requires feature: ipv6-mtu</dl>
<dt>ipv6-privacy (bool)</p>
<dd>Enable IPv6 Privacy Extensions (RFC 4941) for the specified interface, and prefer temporary addresses. Defaults to false &#8211; no privacy extensions. There is currently no way to have a private address but prefer the public address.</p>
<dt>link-local (sequence of scalars)</p>
<dd>Configure the link-local addresses to bring up. Valid options are `ipv4&#8242; and `ipv6&#8242;, which respectively allow enabling IPv4 and IPv6 link local addressing. If this field is not defined, the default is to enable only IPv6 link-local addresses. If the field is defined but configured as an empty set, IPv6 link-local addresses are disabled as well as IPv4 link- local addresses.</p>
<dl>
<dd>This feature enables or disables link-local addresses for a protocol, but the actual implementation differs per backend. On networkd, this directly changes the behavior and may add an extra address on an interface. When using the NetworkManager backend, enabling link-local has no effect if the interface also has DHCP enabled. </p>
<p> Example to enable only IPv4 link-local: link-local: [ ipv4 ] Example to enable all link-local addresses: link-local: [ ipv4, ipv6 ] Example to disable all link-local addresses: link-local: [ ]</dl>
<dt>critical (bool)</p>
<dd>(networkd backend only) Designate the connection as &#8220;critical to the system&#8221;, meaning that special care will be taken by systemd-networkd to not release the assigned IP when the daemon is restarted.</p>
<dt>dhcp-identifier (scalar)</p>
<dd>When set to `mac&#8217;; pass that setting over to systemd-networkd to use the device&#8217;s MAC address as a unique identifier rather than a RFC4361-compliant Client ID. This has no effect when NetworkManager is used as a renderer.</p>
<dt>dhcp4-overrides (mapping)</p>
<dd>(networkd backend only) Overrides default DHCP behavior; see the DHCP Overrides section below.</p>
<dt>dhcp6-overrides (mapping)</p>
<dd>(networkd backend only) Overrides default DHCP behavior; see the DHCP Overrides section below.</p>
<dt>accept-ra (bool)</p>
<dd>Accept Router Advertisement that would have the kernel configure IPv6 by itself. When enabled, accept Router Advertisements. When disabled, do not respond to Router Advertisements. If unset use the host kernel default setting.</p>
<dt>addresses (sequence of scalars)</p>
<dd>Add static addresses to the interface in addition to the ones received through DHCP or RA. Each sequence entry is in CIDR notation, i. e. of the form addr/prefixlen. addr is an IPv4 or IPv6 address as recognized by <a href="/docs/linux/man/3-inet_pton/">inet_pton</a>(3) and prefixlen the number of bits of the subnet.</p>
<dl>
<dd>For virtual devices (bridges, bonds, vlan) if there is no address configured and DHCP is disabled, the interface may still be brought online, but will not be addressable from the network. </p>
<p> Example: addresses: [192.168.14.2/24, &quot;2001:1::1/64&quot;]</dl>
<dt>ipv6-address-generation (scalar)</p>
<dd>Configure method for creating the address for use with RFC4862 IPv6 Stateless Address Autoconfiguration. Possible values are eui64 or stable-privacy.</p>
<dt>gateway4, gateway6 (scalar)</p>
<dd>Set default gateway for IPv4/6, for manual address configuration. This requires setting addresses too. Gateway IPs must be in a form recognized by <a href="/docs/linux/man/3-inet_pton/">inet_pton</a>(3).</p>
<dl>
<dd>Example for IPv4: gateway4: 172.16.0.1 Example for IPv6: gateway6: &quot;2001:4::1&quot;</dl>
<dt>nameservers (mapping)</p>
<dd>Set DNS servers and search domains, for manual address configuration. There are two supported fields: addresses: is a list of IPv4 or IPv6 addresses similar to gateway*, and search: is a list of search domains.</p>
<dl>
<dd>Example:</p>
<dl>
<dd>
<pre>ethernets:
 id0:
 [...]
 nameservers:
 search: [lab, home]
 addresses: [8.8.8.8, &quot;FEDC::1&quot;]</pre>
</dl>
</dl>
<dt>macaddress (scalar)</p>
<dd>Set the device&#8217;s MAC address. The MAC address must be in the form &#8220;XX:XX:XX:XX:XX:XX&#8221;.</p>
<dl>
<dd>Note: This will not work reliably for devices matched by name only and rendered by networkd, due to interactions with device renaming in udev. Match devices by MAC when setting MAC addresses. </p>
<p> Example:</p>
<dl>
<dd>
<pre>ethernets:
 id0:
 match:
 macaddress: 52:54:00:6b:3c:58
 [...]
 macaddress: 52:54:00:6b:3c:59</pre>
</dl>
</dl>
<dt>mtu (scalar)</p>
<dd>Set the Maximum Transmission Unit for the interface. The default is 1500. Valid values depend on your network interface.</p>
<dl>
<dd>Note: This will not work reliably for devices matched by name only and rendered by networkd, due to interactions with device renaming in udev. Match devices by MAC when setting MTU.</dl>
<dt>optional (bool)</p>
<dd>An optional device is not required for booting. Normally, networkd will wait some time for device to become configured before proceeding with booting. However, if a device is marked as optional, networkd will not wait for it. This is only supported by networkd, and the default is false.</p>
<dl>
<dd>Example:</p>
<dl>
<dd>
<pre>ethernets:
 eth7:
 # this is plugged into a test network that is often
 # down - don't wait for it to come up during boot.
 dhcp4: true
 optional: true</pre>
</dl>
</dl>
<dt>optional-addresses (sequence of scalars)</p>
<dd>Specify types of addresses that are not required for a device to be considered online. This changes the behavior of backends at boot time to avoid waiting for addresses that are marked optional, and thus consider the interface as &#8220;usable&#8221; sooner. This does not disable these addresses, which will be brought up anyway.</p>
<dl>
<dd>Example:</p>
<dl>
<dd>
<pre>ethernets:
 eth7:
 dhcp4: true
 dhcp6: true
 optional-addresses: [ ipv4-ll, dhcp6 ]</pre>
</dl>
</dl>
<dt>routes (mapping)</p>
<dd>Configure static routing for the device; see the Routing section below.</p>
<dt>routing-policy (mapping)</p>
<dd>Configure policy routing for the device; see the Routing section below.</dl>
<h3>DHCP Overrides</h3>
<p>Several DHCP behavior overrides are available. Most currently only have any effect when using the networkd backend, with the exception of use-routes and route-metric. </p>
<p> Overrides only have an effect if the corresponding dhcp4 or dhcp6 is set to true. </p>
<p> If both dhcp4 and dhcp6 are true, the networkd backend requires that dhcp4-overrides and dhcp6-overrides contain the same keys and values. If the values do not match, an error will be shown and the network configuration will not be applied. </p>
<p> When using the NetworkManager backend, different values may be specified for dhcp4-overrides and dhcp6-overrides, and will be applied to the DHCP client processes as specified in the netplan YAML. </p>
<p> : The dhcp4-overrides and dhcp6-overrides mappings override the default DHCP behavior.</p>
<dl>
<dd>
<pre> ``use-dns`` (bool)
 : Default: ``true``. When ``true``, the DNS servers received from the
 DHCP server will be used and take precedence over any statically
 configured ones. Currently only has an effect on the ``networkd``
 backend.
 ``use-ntp`` (bool)
 : Default: ``true``. When ``true``, the NTP servers received from the
 DHCP server will be used by systemd-timesyncd and take precedence
 over any statically configured ones. Currently only has an effect on
 the ``networkd`` backend.
 ``send-hostname`` (bool)
 : Default: ``true``. When ``true``, the machine's hostname will be sent
 to the DHCP server. Currently only has an effect on the ``networkd``
 backend.
 ``use-hostname`` (bool)
 : Default: ``true``. When ``true``, the hostname received from the DHCP
 server will be set as the transient hostname of the system. Currently
 only has an effect on the ``networkd`` backend.
 ``use-mtu`` (bool)
 : Default: ``true``. When ``true``, the MTU received from the DHCP
 server will be set as the MTU of the network interface. When ``false``,
 the MTU advertised by the DHCP server will be ignored. Currently only
 has an effect on the ``networkd`` backend.
 ``hostname`` (scalar)
 : Use this value for the hostname which is sent to the DHCP server,
 instead of machine's hostname. Currently only has an effect on the
 ``networkd`` backend.
 ``use-routes`` (bool)
 : Default: ``true``. When ``true``, the routes received from the DHCP
 server will be installed in the routing table normally. When set to
 ``false``, routes from the DHCP server will be ignored: in this case,
 the user is responsible for adding static routes if necessary for
 correct network operation. This allows users to avoid installing a
 default gateway for interfaces configured via DHCP. Available for
 both the ``networkd`` and ``NetworkManager`` backends.
 ``route-metric`` (scalar)
 : Use this value for default metric for automatically-added routes.
 Use this to prioritize routes for devices by setting a higher metric
 on a preferred interface. Available for both the ``networkd`` and
 ``NetworkManager`` backends.
 ``use-domains`` (scalar)
 : Takes a boolean, or the special value &quot;route&quot;. When true, the domain 
 name received from the DHCP server will be used as DNS search domain
 over this link, similar to the effect of the Domains= setting. If set
 to &quot;route&quot;, the domain name received from the DHCP server will be 
 used for routing DNS queries only, but not for searching, similar to
 the effect of the Domains= setting when the argument is prefixed with
 &quot;~&quot;.
 **Requires feature: dhcp-use-domains**</pre>
</dl>
<h3>Routing</h3>
<p>Complex routing is possible with netplan. Standard static routes as well as policy routing using routing tables are supported via the networkd backend. </p>
<p> These options are available for all types of interfaces.</p>
<dl>
<dt>routes (mapping)</p>
<dd>The routes block defines standard static routes for an interface. At least to and via must be specified.</p>
<dl>
<dd>For from, to, and via, both IPv4 and IPv6 addresses are recognized, and must be in the form addr/prefixlen or addr.</p>
<dl>
<dt>from (scalar)</p>
<dd>Set a source IP address for traffic going through the route.</p>
<dt>to (scalar)</p>
<dd>Destination address for the route.</p>
<dt>via (scalar)</p>
<dd>Address to the gateway to use for this route.</p>
<dt>on-link (bool)</p>
<dd>When set to &#8220;true&#8221;, specifies that the route is directly connected to the interface.</p>
<dt>metric (scalar)</p>
<dd>The relative priority of the route. Must be a positive integer value.</p>
<dt>type (scalar)</p>
<dd>The type of route. Valid options are &#8220;unicast&#8221; (default), &#8220;unreachable&#8221;, &#8220;blackhole&#8221; or &#8220;prohibit&#8221;.</p>
<dt>scope (scalar)</p>
<dd>The route scope, how wide-ranging it is to the network. Possible values are &#8220;global&#8221;, &#8220;link&#8221;, or &#8220;host&#8221;.</p>
<dt>table (scalar)</p>
<dd>The table number to use for the route. In some scenarios, it may be useful to set routes in a separate routing table. It may also be used to refer to routing policy rules which also accept a table parameter. Allowed values are positive integers starting from 1. Some values are already in use to refer to specific routing tables: see /etc/iproute2/rt_tables.</dl>
</dl>
<dt>routing-policy (mapping)</p>
<dd>The routing-policy block defines extra routing policy for a network, where traffic may be handled specially based on the source IP, firewall marking, etc.</p>
<dl>
<dd>For from, to, both IPv4 and IPv6 addresses are recognized, and must be in the form addr/prefixlen or addr.</p>
<dl>
<dt>from (scalar)</p>
<dd>Set a source IP address to match traffic for this policy rule.</p>
<dt>to (scalar)</p>
<dd>Match on traffic going to the specified destination.</p>
<dt>table (scalar)</p>
<dd>The table number to match for the route. In some scenarios, it may be useful to set routes in a separate routing table. It may also be used to refer to routes which also accept a table parameter. Allowed values are positive integers starting from 1. Some values are already in use to refer to specific routing tables: see /etc/iproute2/rt_tables.</p>
<dt>priority (scalar)</p>
<dd>Specify a priority for the routing policy rule, to influence the order in which routing rules are processed. A higher number means lower priority: rules are processed in order by increasing priority number.</p>
<dt>mark (scalar)</p>
<dd>Have this routing policy rule match on traffic that has been marked by the iptables firewall with this value. Allowed values are positive integers starting from 1.</p>
<dt>type-of-service (scalar)</p>
<dd>Match this policy rule based on the type of service number applied to the traffic.</dl>
</dl>
</dl>
<h3>Authentication</h3>
<p>Netplan supports advanced authentication settings for ethernet and wifi interfaces, as well as individual wifi networks, by means of the auth block.</p>
<dl>
<dt>auth (mapping)</p>
<dd>Specifies authentication settings for a device of type ethernets:, or an access-points: entry on a wifis: device.</p>
<dl>
<dd>The auth block supports the following properties:</p>
<dl>
<dt>key-management (scalar)</p>
<dd>The supported key management modes are none (no key management); psk (WPA with pre-shared key, common for home wifi); eap (WPA with EAP, common for enterprise wifi); and 802.1x (used primarily for wired Ethernet connections).</p>
<dt>password (scalar)</p>
<dd>The password string for EAP, or the pre-shared key for WPA-PSK.</dl>
<p> The following properties can be used if key-management is eap or 802.1x:</p>
<dl>
<dt>method (scalar)</p>
<dd>The EAP method to use. The supported EAP methods are tls (TLS), peap (Protected EAP), and ttls (Tunneled TLS).</p>
<dt>identity (scalar)</p>
<dd>The identity to use for EAP.</p>
<dt>anonymous-identity (scalar)</p>
<dd>The identity to pass over the unencrypted channel if the chosen EAP method supports passing a different tunnelled identity.</p>
<dt>ca-certificate (scalar)</p>
<dd>Path to a file with one or more trusted certificate authority (CA) certificates.</p>
<dt>client-certificate (scalar)</p>
<dd>Path to a file containing the certificate to be used by the client during authentication.</p>
<dt>client-key (scalar)</p>
<dd>Path to a file containing the private key corresponding to client-certificate.</p>
<dt>client-key-password (scalar)</p>
<dd>Password to use to decrypt the private key specified in client-key if it is encrypted.</p>
<dt>phase2-auth (scalar)</p>
<dd>Phase 2 authentication mechanism.</dl>
</dl>
</dl>
<h3>Properties for device type ethernets:</h3>
<p>Ethernet device definitions, beyond common ones described above, also support some additional properties that can be used for SR-IOV devices.</p>
<dl>
<dt>link (scalar)</p>
<dd>(SR-IOV devices only) The link property declares the device as a Virtual Function of the selected Physical Function device, as identified by the given netplan id.</dl>
<p> Example:</p>
<dl>
<dd>
<pre>ethernets:
 enp1: {...}
 enp1s16f1:
 link: enp1</pre>
<dt>virtual-function-count (scalar)</p>
<dd>(SR-IOV devices only) In certain special cases VFs might need to be configured outside of netplan. For such configurations virtual-function-count can be optionally used to set an explicit number of Virtual Functions for the given Physical Function. If unset, the default is to create only as many VFs as are defined in the netplan configuration. This should be used for special cases only.</dl>
<h3>Properties for device type modems:</h3>
<p>GSM/CDMA modem configuration is only supported for the NetworkManager backend. systemd-networkd does not support modems.</p>
<dl>
<dt>apn (scalar)</p>
<dd>Set the carrier APN (Access Point Name). This can be omitted if auto-config is enabled.</p>
<dt>auto-config (bool)</p>
<dd>Specify whether to try and autoconfigure the modem by doing a lookup of the carrier against the Mobile Broadband Provider database. This may not work for all carriers.</p>
<dt>device-id (scalar)</p>
<dd>Specify the device ID (as given by the WWAN management service) of the modem to match. This can be found using mmcli.</p>
<dt>network-id (scalar)</p>
<dd>Specify the Network ID (GSM LAI format). If this is specified, the device will not roam networks.</p>
<dt>number (scalar)</p>
<dd>The number to dial to establish the connection to the mobile broadband network. (Deprecated for GSM)</p>
<dt>password (scalar)</p>
<dd>Specify the password used to authenticate with the carrier network. This can be omitted if auto-config is enabled.</p>
<dt>pin (scalar)</p>
<dd>Specify the SIM PIN to allow it to operate if a PIN is set.</p>
<dt>sim-id (scalar)</p>
<dd>Specify the SIM unique identifier (as given by the WWAN management service) which this connection applies to. If given, the connection will apply to any device also allowed by device-id which contains a SIM card matching the given identifier.</p>
<dt>sim-operator-id (scalar)</p>
<dd>Specify the MCC/MNC string (such as &#8220;310260&#8221; or &#8220;21601&#8221;) which identifies the carrier that this connection should apply to. If given, the connection will apply to any device also allowed by device-id and sim-id which contains a SIM card provisioned by the given operator.</p>
<dt>username (scalar)</p>
<dd>Specify the username used to authentiate with the carrier network. This can be omitted if auto-config is enabled.</dl>
<h3>Properties for device type wifis:</h3>
<p>Note that systemd-networkd does not natively support wifi, so you need wpasupplicant installed if you let the networkd renderer handle wifi.</p>
<dl>
<dt>access-points (mapping)</p>
<dd>This provides pre-configured connections to NetworkManager. Note that users can of course select other access points/SSIDs. The keys of the mapping are the SSIDs, and the values are mappings with the following supported properties:</p>
<dl>
<dd>
<dl>
<dt>password (scalar)</p>
<dd>Enable WPA2 authentication and set the passphrase for it. If neither this nor an auth block are given, the network is assumed to be open. The setting</p>
<dl>
<dd>
<dl>
<dd>
<pre> password: &quot;S3kr1t&quot;</pre>
</dl>
<p> is equivalent to</p>
<dl>
<dd>
<pre> auth:
 key-management: psk
 password: &quot;S3kr1t&quot;</pre>
</dl>
</dl>
<dt>mode (scalar)</p>
<dd>Possible access point modes are infrastructure (the default), ap (create an access point to which other devices can connect), and adhoc (peer to peer networks without a central access point). ap is only supported with NetworkManager.</p>
<dt>bssid (scalar)</p>
<dd>If specified, directs the device to only associate with the given access point.</p>
<dt>band (scalar)</p>
<dd>Possible bands are 5GHz (for 5GHz 802.11a) and 2.4GHz (for 2.4GHz 802.11), do not restrict the 802.11 frequency band of the network if unset (the default).</p>
<dt>channel (scalar)</p>
<dd>Wireless channel to use for the Wi-Fi connection. Because channel numbers overlap between bands, this property takes effect only if the band property is also set.</dl>
</dl>
<dt>wakeonwlan (sequence of scalars)</p>
<dd>This enables WakeOnWLan on supported devices. Not all drivers support all options. May be any combination of any, disconnect, magic_pkt, gtk_rekey_failure, eap_identity_req, four_way_handshake, rfkill_release or tcp (NetworkManager only). Or the exclusive default flag (the default).</dl>
<h3>Properties for device type bridges:</h3>
<dl>
<dt>interfaces (sequence of scalars)</p>
<dd>All devices matching this ID list will be added to the bridge. This may be an empty list, in which case the bridge will be brought online with no member interfaces.</p>
<dl>
<dd>Example:</p>
<dl>
<dd>
<pre> ethernets:
 switchports:
 match: {name: &quot;enp2*&quot;}
 [...]
 bridges:
 br0:
 interfaces: [switchports]</pre>
</dl>
</dl>
<dt>parameters (mapping)</p>
<dd>Customization parameters for special bridging options. Time intervals may need to be expressed as a number of seconds or milliseconds: the default value type is specified below. If necessary, time intervals can be qualified using a time suffix (such as &#8220;s&#8221; for seconds, &#8220;ms&#8221; for milliseconds) to allow for more control over its behavior.</p>
<dl>
<dd>
<dl>
<dt>ageing-time (scalar)</p>
<dd>Set the period of time to keep a MAC address in the forwarding database after a packet is received. This maps to the AgeingTimeSec= property when the networkd renderer is used. If no time suffix is specified, the value will be interpreted as seconds.</p>
<dt>priority (scalar)</p>
<dd>Set the priority value for the bridge. This value should be a number between 0 and 65535. Lower values mean higher priority. The bridge with the higher priority will be elected as the root bridge.</p>
<dt>port-priority (scalar)</p>
<dd>Set the port priority to . The priority value is a number between 0 and 63. This metric is used in the designated port and root port selection algorithms.</p>
<dt>forward-delay (scalar)</p>
<dd>Specify the period of time the bridge will remain in Listening and Learning states before getting to the Forwarding state. This field maps to the ForwardDelaySec= property for the networkd renderer. If no time suffix is specified, the value will be interpreted as seconds.</p>
<dt>hello-time (scalar)</p>
<dd>Specify the interval between two hello packets being sent out from the root and designated bridges. Hello packets communicate information about the network topology. When the networkd renderer is used, this maps to the HelloTimeSec= property. If no time suffix is specified, the value will be interpreted as seconds.</p>
<dt>max-age (scalar)</p>
<dd>Set the maximum age of a hello packet. If the last hello packet is older than that value, the bridge will attempt to become the root bridge. This maps to the MaxAgeSec= property when the networkd renderer is used. If no time suffix is specified, the value will be interpreted as seconds.</p>
<dt>path-cost (scalar)</p>
<dd>Set the cost of a path on the bridge. Faster interfaces should have a lower cost. This allows a finer control on the network topology so that the fastest paths are available whenever possible.</p>
<dt>stp (bool)</p>
<dd>Define whether the bridge should use Spanning Tree Protocol. The default value is &#8220;true&#8221;, which means that Spanning Tree should be used.</dl>
</dl>
</dl>
<h3>Properties for device type bonds:</h3>
<dl>
<dt>interfaces (sequence of scalars)</p>
<dd>All devices matching this ID list will be added to the bond.</p>
<dl>
<dd>Example:</p>
<dl>
<dd>
<pre> ethernets:
 switchports:
 match: {name: &quot;enp2*&quot;}
 [...]
 bonds:
 bond0:
 interfaces: [switchports]</pre>
</dl>
</dl>
<dt>parameters (mapping)</p>
<dd>Customization parameters for special bonding options. Time intervals may need to be expressed as a number of seconds or milliseconds: the default value type is specified below. If necessary, time intervals can be qualified using a time suffix (such as &#8220;s&#8221; for seconds, &#8220;ms&#8221; for milliseconds) to allow for more control over its behavior.</p>
<dl>
<dd>
<dl>
<dt>mode (scalar)</p>
<dd>Set the bonding mode used for the interfaces. The default is balance-rr (round robin). Possible values are balance-rr, active-backup, balance-xor, broadcast, 802.3ad, balance-tlb, and balance-alb.</p>
<dt>lacp-rate (scalar)</p>
<dd>Set the rate at which LACPDUs are transmitted. This is only useful in 802.3ad mode. Possible values are slow (30 seconds, default), and fast (every second).</p>
<dt>mii-monitor-interval (scalar)</p>
<dd>Specifies the interval for MII monitoring (verifying if an interface of the bond has carrier). The default is 0; which disables MII monitoring. This is equivalent to the MIIMonitorSec= field for the networkd backend. If no time suffix is specified, the value will be interpreted as milliseconds.</p>
<dt>min-links (scalar)</p>
<dd>The minimum number of links up in a bond to consider the bond interface to be up.</p>
<dt>transmit-hash-policy (scalar)</p>
<dd>Specifies the transmit hash policy for the selection of slaves. This is only useful in balance-xor, 802.3ad and balance-tlb modes. Possible values are layer2, layer3+4, layer2+3, encap2+3, and encap3+4.</p>
<dt>ad-select (scalar)</p>
<dd>Set the aggregation selection mode. Possible values are stable, bandwidth, and count. This option is only used in 802.3ad mode.</p>
<dt>all-slaves-active (bool)</p>
<dd>If the bond should drop duplicate frames received on inactive ports, set this option to false. If they should be delivered, set this option to true. The default value is false, and is the desirable behavior in most situations.</p>
<dt>arp-interval (scalar)</p>
<dd>Set the interval value for how frequently ARP link monitoring should happen. The default value is 0, which disables ARP monitoring. For the networkd backend, this maps to the ARPIntervalSec= property. If no time suffix is specified, the value will be interpreted as milliseconds.</p>
<dt>arp-ip-targets (sequence of scalars)</p>
<dd>IPs of other hosts on the link which should be sent ARP requests in order to validate that a slave is up. This option is only used when arp-interval is set to a value other than 0. At least one IP address must be given for ARP link monitoring to function. Only IPv4 addresses are supported. You can specify up to 16 IP addresses. The default value is an empty list.</p>
<dt>arp-validate (scalar)</p>
<dd>Configure how ARP replies are to be validated when using ARP link monitoring. Possible values are none, active, backup, and all.</p>
<dt>arp-all-targets (scalar)</p>
<dd>Specify whether to use any ARP IP target being up as sufficient for a slave to be considered up; or if all the targets must be up. This is only used for active-backup mode when arp-validate is enabled. Possible values are any and all.</p>
<dt>up-delay (scalar)</p>
<dd>Specify the delay before enabling a link once the link is physically up. The default value is 0. This maps to the UpDelaySec= property for the networkd renderer. This option is only valid for the miimon link monitor. If no time suffix is specified, the value will be interpreted as milliseconds.</p>
<dt>down-delay (scalar)</p>
<dd>Specify the delay before disabling a link once the link has been lost. The default value is 0. This maps to the DownDelaySec= property for the networkd renderer. This option is only valid for the miimon link monitor. If no time suffix is specified, the value will be interpreted as milliseconds.</p>
<dt>fail-over-mac-policy (scalar)</p>
<dd>Set whether to set all slaves to the same MAC address when adding them to the bond, or how else the system should handle MAC addresses. The possible values are none, active, and follow.</p>
<dt>gratuitous-arp (scalar)</p>
<dd>Specify how many ARP packets to send after failover. Once a link is up on a new slave, a notification is sent and possibly repeated if this value is set to a number greater than 1. The default value is 1 and valid values are between 1 and 255. This only affects active-backup mode.</p>
<dl>
<dd>For historical reasons, the misspelling gratuitious-arp is also accepted and has the same function.</dl>
<dt>packets-per-slave (scalar)</p>
<dd>In balance-rr mode, specifies the number of packets to transmit on a slave before switching to the next. When this value is set to 0, slaves are chosen at random. Allowable values are between 0 and 65535. The default value is 1. This setting is only used in balance-rr mode.</p>
<dt>primary-reselect-policy (scalar)</p>
<dd>Set the reselection policy for the primary slave. On failure of the active slave, the system will use this policy to decide how the new active slave will be chosen and how recovery will be handled. The possible values are always, better, and failure.</p>
<dt>resend-igmp (scalar)</p>
<dd>In modes balance-rr, active-backup, balance-tlb and balance-alb, a failover can switch IGMP traffic from one slave to another.</p>
<dl>
<dd>This parameter specifies how many IGMP membership reports are issued on a failover event. Values range from 0 to 255. 0 disables sending membership reports. Otherwise, the first membership report is sent on failover and subsequent reports are sent at 200ms intervals.</dl>
<dt>learn-packet-interval (scalar)</p>
<dd>Specify the interval between sending learning packets to each slave. The value range is between 1 and 0x7fffffff. The default value is 1. This option only affects balance-tlb and balance-alb modes. Using the networkd renderer, this field maps to the LearnPacketIntervalSec= property. If no time suffix is specified, the value will be interpreted as seconds.</p>
<dt>primary (scalar)</p>
<dd>Specify a device to be used as a primary slave, or preferred device to use as a slave for the bond (ie. the preferred device to send data through), whenever it is available. This only affects active-backup, balance-alb, and balance-tlb modes.</dl>
</dl>
</dl>
<h3>Properties for device type tunnels:</h3>
<p>Tunnels allow traffic to pass as if it was between systems on the same local network, although systems may be far from each other but reachable via the Internet. They may be used to support IPv6 traffic on a network where the ISP does not provide the service, or to extend and &#8220;connect&#8221; separate local networks. Please see <a rel="nofollow" href="https://en.wikipedia.org/wiki/Tunneling_protocol">https://en.wikipedia.org/wiki/Tunneling_protocol</a> for more general information about tunnels.</p>
<dl>
<dt>mode (scalar)</p>
<dd>Defines the tunnel mode. Valid options are sit, gre, ip6gre, ipip, ipip6, ip6ip6, vti, and vti6. Additionally, the networkd backend also supports gretap and ip6gretap modes. In addition, the NetworkManager backend supports isatap tunnels.</p>
<dt>local (scalar)</p>
<dd>Defines the address of the local endpoint of the tunnel.</p>
<dt>remote (scalar)</p>
<dd>Defines the address of the remote endpoint of the tunnel.</p>
<dt>key (scalar or mapping)</p>
<dd>Define keys to use for the tunnel. The key can be a number or a dotted quad (an IPv4 address). It is used for identification of IP transforms. This is only required for vti and vti6 when using the networkd backend, and for gre or ip6gre tunnels when using the NetworkManager backend.</p>
<dl>
<dd>This field may be used as a scalar (meaning that a single key is specified and to be used for both input and output key), or as a mapping, where you can then further specify input and output.</p>
<dl>
<dt>input (scalar)</p>
<dd>The input key for the tunnel</p>
<dt>output (scalar)</p>
<dd>The output key for the tunnel</dl>
</dl>
</dl>
<p> Examples:</p>
<dl>
<dd>
<pre>tunnels:
 tun0:
 mode: gre
 local: ...
 remote: ...
 keys:
 input: 1234
 output: 5678
tunnels:
 tun0:
 mode: vti6
 local: ...
 remote: ...
 key: 59568549</pre>
<dt>keys (scalar or mapping)</p>
<dd>Alternate name for the key field. See above.</dl>
<h3>Properties for device type vlans:</h3>
<dl>
<dt>id (scalar)</p>
<dd>VLAN ID, a number between 0 and 4094.</p>
<dt>link (scalar)</p>
<dd>netplan ID of the underlying device definition on which this VLAN gets created.</dl>
<p> Example:</p>
<dl>
<dd>
<pre>ethernets:
 eno1: {...}
vlans:
 en-intra:
 id: 1
 link: eno1
 dhcp4: yes
 en-vpn:
 id: 2
 link: eno1
 addresses: ...</pre>
</dl>
<h3>Backend-specific configuration parameters</h3>
<p>In addition to the other fields available to configure interfaces, some backends may require to record some of their own parameters in netplan, especially if the netplan definitions are generated automatically by the consumer of that backend. Currently, this is only used with NetworkManager.</p>
<dl>
<dt>networkmanager (mapping)</p>
<dd>Keeps the NetworkManager-specific configuration parameters used by the daemon to recognize connections.</p>
<dl>
<dd>
<dl>
<dt>name (scalar)</p>
<dd>Set the display name for the connection.</p>
<dt>uuid (scalar)</p>
<dd>Defines the UUID (unique identifier) for this connection, as generated by NetworkManager itself.</p>
<dt>stable-id (scalar)</p>
<dd>Defines the stable ID (a different form of a connection name) used by NetworkManager in case the name of the connection might otherwise change, such as when sharing connections between users.</p>
<dt>device (scalar)</p>
<dd>Defines the interface name for which this connection applies.</dl>
</dl>
</dl>
<h3>Examples</h3>
<p>Configure an ethernet device with networkd, identified by its name, and enable DHCP:</p>
<dl>
<dd>
<pre>network:
 version: 2
 ethernets:
 eno1:
 dhcp4: true</pre>
</dl>
<p> This is an example of a static-configured interface with multiple IPv4 addresses and multiple gateways with networkd, with equal route metric levels, and static DNS nameservers (Google DNS for this example):</p>
<dl>
<dd>
<pre>network:
 version: 2
 renderer: networkd
 ethernets:
 eno1:
 addresses:
 - 10.0.0.10/24
 - 11.0.0.11/24
 nameservers:
 addresses:
 - 8.8.8.8
 - 8.8.4.4
 routes:
 - to: 0.0.0.0/0
 via: 10.0.0.1
 metric: 100
 - to: 0.0.0.0/0
 via: 11.0.0.1
 metric: 100</pre>
</dl>
<p> This is a complex example which shows most available features:</p>
<dl>
<dd>
<pre>network:
 version: 2
 # if specified, can only realistically have that value, as networkd cannot
 # render wifi/3G.
 renderer: NetworkManager
 ethernets:
 # opaque ID for physical interfaces, only referred to by other stanzas
 id0:
 match:
 macaddress: 00:11:22:33:44:55
 wakeonlan: true
 dhcp4: true
 addresses:
 - 192.168.14.2/24
 - 192.168.14.3/24
 - &quot;2001:1::1/64&quot;
 gateway4: 192.168.14.1
 gateway6: &quot;2001:1::2&quot;
 nameservers:
 search: [foo.local, bar.local]
 addresses: [8.8.8.8]
 routes:
 - to: 0.0.0.0/0
 via: 11.0.0.1
 table: 70
 on-link: true
 metric: 3
 routing-policy:
 - to: 10.0.0.0/8
 from: 192.168.14.2/24
 table: 70
 priority: 100
 - to: 20.0.0.0/8
 from: 192.168.14.3/24
 table: 70
 priority: 50
 # only networkd can render on-link routes and routing policies
 renderer: networkd
 lom:
 match:
 driver: ixgbe
 # you are responsible for setting tight enough match rules
 # that only match one device if you use set-name
 set-name: lom1
 dhcp6: true
 switchports:
 # all cards on second PCI bus unconfigured by
 # themselves, will be added to br0 below
 # note: globbing is not supported by NetworkManager
 match:
 name: enp2*
 mtu: 1280
 wifis:
 all-wlans:
 # useful on a system where you know there is
 # only ever going to be one device
 match: {}
 access-points:
 &quot;Joe's home&quot;:
 # mode defaults to &quot;infrastructure&quot; (client)
 password: &quot;s3kr1t&quot;
 # this creates an AP on wlp1s0 using hostapd
 # no match rules, thus the ID is the interface name
 wlp1s0:
 access-points:
 &quot;guest&quot;:
 mode: ap
 # no WPA config implies default of open
 bridges:
 # the key name is the name for virtual (created) interfaces
 # no match: and set-name: allowed
 br0:
 # IDs of the components; switchports expands into multiple interfaces
 interfaces: [wlp1s0, switchports]
 dhcp4: true</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-netplan-generate/">netplan-generate</a>(8), <a href="/docs/linux/man/8-netplan-apply/">netplan-apply</a>(8), <a href="/docs/linux/man/8-netplan-try/">netplan-try</a>(8), <a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8), <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)</p>
<h2>Authors</h2>
<p>Mathieu Trudel-Lapierre (&lt;cyphermox [at] ubuntu.com&gt;); Martin Pitt (&lt;martin.pitt [at] ubuntu.com&gt;).</p>
