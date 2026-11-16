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
<dt>&bull;</dt>
<dd>Configured devices get handled by systemd-networkd by default, unless explicitly marked as managed by a specific renderer (NetworkManager)</dd>
<dt>&bull;</dt>
<dd>Devices not covered by the network config do not get touched at all.</dd>
<dt>&bull;</dt>
<dd>Usable in initramfs (few dependencies and fast)</dd>
<dt>&bull;</dt>
<dd>No persistent generated config, only original YAML config</dd>
<dt>&bull;</dt>
<dd>Parser supports multiple config files to allow applications like libvirt or lxd to package up expected network config (virbr0, lxdbr0), or to change the global default policy to use NetworkManager for everything.</dd>
<dt>&bull;</dt>
<dd>Retains the flexibility to change backends/policy later or adjust to removing NetworkManager, as generated configuration is ephemeral.</dd></dl>
<h3>General structure</h3>
<p>netplan&#8217;s configuration files use the YAML (<a rel="nofollow" href="http://yaml.org/spec/1.1/current.html)">http://yaml.org/spec/1.1/current.html)</a> format. All /{lib,etc,run}/netplan/*.yaml are considered. Lexicographically later files (regardless of in which directory they are) amend (new mapping keys) or override (same mapping keys) previous ones. A file in /run/netplan completely shadows a file with same name in /etc/netplan, and a file in either of those directories shadows a file with the same name in /lib/netplan. </p>
<p> The top-level node in a netplan configuration file is a network: mapping that contains version: 2 (the YAML currently being used by curtin, MaaS, etc. is version 1), and then device definitions grouped by their type, such as ethernets:, modems:, wifis:, or bridges:. These are the types that our renderer can understand and are supported by our backends. </p>
<p> Each type block contains device definitions as a map where the keys (called &#8220;configuration IDs&#8221;) are defined as below.</p>
<h3>Device configuration IDs</h3>
<p>The key names below the per-device-type definition maps (like ethernets:) are called &#8220;ID&#8221;s. They must be unique throughout the entire set of configuration files. Their primary purpose is to serve as anchor names for composite devices, for example to enumerate the members of a bridge that is currently being defined. </p>
<p> If an interface is defined with an ID in a configuration file; it will be brought up by the applicable renderer. To not have netplan touch an interface at all, it should be completely omitted from the netplan configuration files. </p>
<p> There are two physically/structurally different classes of device definitions, and the ID field has a different interpretation for each:</p>
<dl>
<dt><code>Physical devices</code></dt>
<dd>(Examples: ethernet, modem, wifi) These can dynamically come and go between reboots and even during runtime (hotplugging). In the generic case, they can be selected by match: rules on desired properties, such as name/name pattern, MAC address, driver, or device paths. In general these will match any number of devices (unless they refer to properties which are unique such as the full path or MAC address), so without further knowledge about the hardware these will always be considered as a group.</dd>
<dl>
<dd>It is valid to specify no match rules at all, in which case the ID field is simply the interface name to be matched. This is mostly useful if you want to keep simple cases simple, and it&#8217;s how network device configuration has been done for a long time. </dd>
<p> If there are match: rules, then the ID field is a purely opaque name which is only being used for references from definitions of compound devices in the config.</dl>
<dt><code>Virtual devices</code></dt>
<dd>(Examples: veth, bridge, bond) These are fully under the control of the config file(s) and the network stack. I. e. these devices are being created instead of matched. Thus match: and set-name: are not applicable for these, and the ID field is the name of the created virtual device.</dd></dl>
<h3>Common properties for physical device types</h3>
<dl>
<dt>match (mapping)</dt>
<dd>This selects a subset of available physical devices by various hardware properties. The following configuration will then apply to all matching devices, as soon as they appear. All specified properties must match.</dd>
<dl>
<dd>
</dd><dl>
<dt>name (scalar)</dt>
<dd>Current interface name. Globs are supported, and the primary use case for matching on names, as selecting one fixed name can be more easily achieved with having no match: at all and just using the ID (see above). Note that currently only networkd supports globbing, NetworkManager does not.</dd>
<dt>macaddress (scalar)</dt>
<dd>Device&#8217;s MAC address in the form &#8220;XX:XX:XX:XX:XX:XX&#8221;. Globs are not allowed.</dd>
<dt>driver (scalar)</dt>
<dd>Kernel driver name, corresponding to the DRIVER udev property. Globs are supported. Matching on driver is only supported with networkd.</dd></dl>
<p> Examples:</p>
<dl>
<dt>&bull;</dt>
<dd>all cards on second PCI bus:</dd>
<dl>
<dd>
</dd><dl>
<dd>
<pre> match:
 name: enp2*</pre>
</dd></dl>
</dl>
<dt>&bull;</dt>
<dd>fixed MAC address:</dd>
<dl>
<dd>
</dd><dl>
<dd>
<pre> match:
 macaddress: 11:22:33:AA:BB:FF</pre>
</dd></dl>
</dl>
<dt>&bull;</dt>
<dd>first card of driver ixgbe:</dd>
<dl>
<dd>
</dd><dl>
<dd>
<pre> match:
 driver: ixgbe
 name: en*s0</pre>
</dd></dl>
</dl>
</dl>
</dl>
<dt>set-name (scalar)</dt>
<dd>When matching on unique properties such as path or MAC, or with additional assumptions such as &#8220;there will only ever be one wifi device&#8221;, match rules can be written so that they only match one device. Then this property can be used to give that device a more specific/desirable/nicer name than the default from udev&#8217;s ifnames. Any additional device that satisfies the match rules will then fail to get renamed and keep the original kernel name (and dmesg will show an error).</dd>
<dt>wakeonlan (bool)</dt>
<dd>Enable wake on LAN. Off by default.</dd>
<dt>emit-lldp (bool)</dt>
<dd>(networkd backend only) Whether to emit LLDP packets. Off by default.</dd></dl>
<h3>Common properties for all device types</h3>
<dl>
<dt>renderer (scalar)</dt>
<dd>Use the given networking backend for this definition. Currently supported are networkd and NetworkManager. This property can be specified globally in networks:, for a device type (in e. g. ethernets:) or for a particular device definition. Default is networkd.</dd>
<dl>
<dd>The renderer property has one additional acceptable value for vlan objects (i. e. defined in vlans:): sriov. If a vlan is defined with the sriov renderer for an SR-IOV Virtual Function interface, this causes netplan to set up a hardware VLAN filter for it. There can be only one defined per VF.</dd></dl>
<dt>dhcp4 (bool)</dt>
<dd>Enable DHCP for IPv4. Off by default.</dd>
<dt>dhcp6 (bool)</dt>
<dd>Enable DHCP for IPv6. Off by default. This covers both stateless DHCP &#8211; where the DHCP server supplies information like DNS nameservers but not the IP address &#8211; and stateful DHCP, where the server provides both the address and the other information.</dd>
<dl>
<dd>If you are in an IPv6-only environment with completely stateless autoconfiguration (SLAAC with RDNSS), this option can be set to cause the interface to be brought up. (Setting accept-ra alone is not sufficient.) Autoconfiguration will still honour the contents of the router advertisement and only use DHCP if requested in the RA. </dd>
<p> Note that <a href="/docs/linux/man/8-rdnssd/">rdnssd</a>(8) is required to use RDNSS with networkd. No extra software is required for NetworkManager.</dl>
<dt>ipv6-mtu (scalar)</dt>
<dd>Set the IPv6 MTU (only supported with networkd backend). Note that needing to set this is an unusual requirement.</dd>
<dl>
<dd>Requires feature: ipv6-mtu</dd></dl>
<dt>ipv6-privacy (bool)</dt>
<dd>Enable IPv6 Privacy Extensions (RFC 4941) for the specified interface, and prefer temporary addresses. Defaults to false &#8211; no privacy extensions. There is currently no way to have a private address but prefer the public address.</dd>
<dt>link-local (sequence of scalars)</dt>
<dd>Configure the link-local addresses to bring up. Valid options are `ipv4&#8242; and `ipv6&#8242;, which respectively allow enabling IPv4 and IPv6 link local addressing. If this field is not defined, the default is to enable only IPv6 link-local addresses. If the field is defined but configured as an empty set, IPv6 link-local addresses are disabled as well as IPv4 link- local addresses.</dd>
<dl>
<dd>This feature enables or disables link-local addresses for a protocol, but the actual implementation differs per backend. On networkd, this directly changes the behavior and may add an extra address on an interface. When using the NetworkManager backend, enabling link-local has no effect if the interface also has DHCP enabled. </dd>
<p> Example to enable only IPv4 link-local: link-local: [ ipv4 ] Example to enable all link-local addresses: link-local: [ ipv4, ipv6 ] Example to disable all link-local addresses: link-local: [ ]</dl>
<dt>critical (bool)</dt>
<dd>(networkd backend only) Designate the connection as &#8220;critical to the system&#8221;, meaning that special care will be taken by systemd-networkd to not release the assigned IP when the daemon is restarted.</dd>
<dt>dhcp-identifier (scalar)</dt>
<dd>When set to `mac&#8217;; pass that setting over to systemd-networkd to use the device&#8217;s MAC address as a unique identifier rather than a RFC4361-compliant Client ID. This has no effect when NetworkManager is used as a renderer.</dd>
<dt>dhcp4-overrides (mapping)</dt>
<dd>(networkd backend only) Overrides default DHCP behavior; see the DHCP Overrides section below.</dd>
<dt>dhcp6-overrides (mapping)</dt>
<dd>(networkd backend only) Overrides default DHCP behavior; see the DHCP Overrides section below.</dd>
<dt>accept-ra (bool)</dt>
<dd>Accept Router Advertisement that would have the kernel configure IPv6 by itself. When enabled, accept Router Advertisements. When disabled, do not respond to Router Advertisements. If unset use the host kernel default setting.</dd>
<dt>addresses (sequence of scalars)</dt>
<dd>Add static addresses to the interface in addition to the ones received through DHCP or RA. Each sequence entry is in CIDR notation, i. e. of the form addr/prefixlen. addr is an IPv4 or IPv6 address as recognized by inet_pton(3) and prefixlen the number of bits of the subnet.</dd>
<dl>
<dd>For virtual devices (bridges, bonds, vlan) if there is no address configured and DHCP is disabled, the interface may still be brought online, but will not be addressable from the network. </dd>
<p> Example: addresses: [192.168.14.2/24, &quot;2001:1::1/64&quot;]</dl>
<dt>ipv6-address-generation (scalar)</dt>
<dd>Configure method for creating the address for use with RFC4862 IPv6 Stateless Address Autoconfiguration. Possible values are eui64 or stable-privacy.</dd>
<dt>gateway4, gateway6 (scalar)</dt>
<dd>Set default gateway for IPv4/6, for manual address configuration. This requires setting addresses too. Gateway IPs must be in a form recognized by inet_pton(3).</dd>
<dl>
<dd>Example for IPv4: gateway4: 172.16.0.1 Example for IPv6: gateway6: &quot;2001:4::1&quot;</dd></dl>
<dt>nameservers (mapping)</dt>
<dd>Set DNS servers and search domains, for manual address configuration. There are two supported fields: addresses: is a list of IPv4 or IPv6 addresses similar to gateway*, and search: is a list of search domains.</dd>
<dl>
<dd>Example:</dd>
<dl>
<dd>
<pre>ethernets:
 id0:
 [...]
 nameservers:
 search: [lab, home]
 addresses: [8.8.8.8, &quot;FEDC::1&quot;]</pre>
</dd></dl>
</dl>
<dt>macaddress (scalar)</dt>
<dd>Set the device&#8217;s MAC address. The MAC address must be in the form &#8220;XX:XX:XX:XX:XX:XX&#8221;.</dd>
<dl>
<dd>Note: This will not work reliably for devices matched by name only and rendered by networkd, due to interactions with device renaming in udev. Match devices by MAC when setting MAC addresses. </dd>
<p> Example:</p>
<dl>
<dd>
<pre>ethernets:
 id0:
 match:
 macaddress: 52:54:00:6b:3c:58
 [...]
 macaddress: 52:54:00:6b:3c:59</pre>
</dd></dl>
</dl>
<dt>mtu (scalar)</dt>
<dd>Set the Maximum Transmission Unit for the interface. The default is 1500. Valid values depend on your network interface.</dd>
<dl>
<dd>Note: This will not work reliably for devices matched by name only and rendered by networkd, due to interactions with device renaming in udev. Match devices by MAC when setting MTU.</dd></dl>
<dt>optional (bool)</dt>
<dd>An optional device is not required for booting. Normally, networkd will wait some time for device to become configured before proceeding with booting. However, if a device is marked as optional, networkd will not wait for it. This is only supported by networkd, and the default is false.</dd>
<dl>
<dd>Example:</dd>
<dl>
<dd>
<pre>ethernets:
 eth7:
 # this is plugged into a test network that is often
 # down - don't wait for it to come up during boot.
 dhcp4: true
 optional: true</pre>
</dd></dl>
</dl>
<dt>optional-addresses (sequence of scalars)</dt>
<dd>Specify types of addresses that are not required for a device to be considered online. This changes the behavior of backends at boot time to avoid waiting for addresses that are marked optional, and thus consider the interface as &#8220;usable&#8221; sooner. This does not disable these addresses, which will be brought up anyway.</dd>
<dl>
<dd>Example:</dd>
<dl>
<dd>
<pre>ethernets:
 eth7:
 dhcp4: true
 dhcp6: true
 optional-addresses: [ ipv4-ll, dhcp6 ]</pre>
</dd></dl>
</dl>
<dt>routes (mapping)</dt>
<dd>Configure static routing for the device; see the Routing section below.</dd>
<dt>routing-policy (mapping)</dt>
<dd>Configure policy routing for the device; see the Routing section below.</dd></dl>
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
</dd></dl>
<h3>Routing</h3>
<p>Complex routing is possible with netplan. Standard static routes as well as policy routing using routing tables are supported via the networkd backend. </p>
<p> These options are available for all types of interfaces.</p>
<dl>
<dt>routes (mapping)</dt>
<dd>The routes block defines standard static routes for an interface. At least to and via must be specified.</dd>
<dl>
<dd>For from, to, and via, both IPv4 and IPv6 addresses are recognized, and must be in the form addr/prefixlen or addr.</dd>
<dl>
<dt>from (scalar)</dt>
<dd>Set a source IP address for traffic going through the route.</dd>
<dt>to (scalar)</dt>
<dd>Destination address for the route.</dd>
<dt>via (scalar)</dt>
<dd>Address to the gateway to use for this route.</dd>
<dt>on-link (bool)</dt>
<dd>When set to &#8220;true&#8221;, specifies that the route is directly connected to the interface.</dd>
<dt>metric (scalar)</dt>
<dd>The relative priority of the route. Must be a positive integer value.</dd>
<dt>type (scalar)</dt>
<dd>The type of route. Valid options are &#8220;unicast&#8221; (default), &#8220;unreachable&#8221;, &#8220;blackhole&#8221; or &#8220;prohibit&#8221;.</dd>
<dt>scope (scalar)</dt>
<dd>The route scope, how wide-ranging it is to the network. Possible values are &#8220;global&#8221;, &#8220;link&#8221;, or &#8220;host&#8221;.</dd>
<dt>table (scalar)</dt>
<dd>The table number to use for the route. In some scenarios, it may be useful to set routes in a separate routing table. It may also be used to refer to routing policy rules which also accept a table parameter. Allowed values are positive integers starting from 1. Some values are already in use to refer to specific routing tables: see /etc/iproute2/rt_tables.</dd></dl>
</dl>
<dt>routing-policy (mapping)</dt>
<dd>The routing-policy block defines extra routing policy for a network, where traffic may be handled specially based on the source IP, firewall marking, etc.</dd>
<dl>
<dd>For from, to, both IPv4 and IPv6 addresses are recognized, and must be in the form addr/prefixlen or addr.</dd>
<dl>
<dt>from (scalar)</dt>
<dd>Set a source IP address to match traffic for this policy rule.</dd>
<dt>to (scalar)</dt>
<dd>Match on traffic going to the specified destination.</dd>
<dt>table (scalar)</dt>
<dd>The table number to match for the route. In some scenarios, it may be useful to set routes in a separate routing table. It may also be used to refer to routes which also accept a table parameter. Allowed values are positive integers starting from 1. Some values are already in use to refer to specific routing tables: see /etc/iproute2/rt_tables.</dd>
<dt>priority (scalar)</dt>
<dd>Specify a priority for the routing policy rule, to influence the order in which routing rules are processed. A higher number means lower priority: rules are processed in order by increasing priority number.</dd>
<dt>mark (scalar)</dt>
<dd>Have this routing policy rule match on traffic that has been marked by the iptables firewall with this value. Allowed values are positive integers starting from 1.</dd>
<dt>type-of-service (scalar)</dt>
<dd>Match this policy rule based on the type of service number applied to the traffic.</dd></dl>
</dl>
</dl>
<h3>Authentication</h3>
<p>Netplan supports advanced authentication settings for ethernet and wifi interfaces, as well as individual wifi networks, by means of the auth block.</p>
<dl>
<dt>auth (mapping)</dt>
<dd>Specifies authentication settings for a device of type ethernets:, or an access-points: entry on a wifis: device.</dd>
<dl>
<dd>The auth block supports the following properties:</dd>
<dl>
<dt>key-management (scalar)</dt>
<dd>The supported key management modes are none (no key management); psk (WPA with pre-shared key, common for home wifi); eap (WPA with EAP, common for enterprise wifi); and 802.1x (used primarily for wired Ethernet connections).</dd>
<dt>password (scalar)</dt>
<dd>The password string for EAP, or the pre-shared key for WPA-PSK.</dd></dl>
<p> The following properties can be used if key-management is eap or 802.1x:</p>
<dl>
<dt>method (scalar)</dt>
<dd>The EAP method to use. The supported EAP methods are tls (TLS), peap (Protected EAP), and ttls (Tunneled TLS).</dd>
<dt>identity (scalar)</dt>
<dd>The identity to use for EAP.</dd>
<dt>anonymous-identity (scalar)</dt>
<dd>The identity to pass over the unencrypted channel if the chosen EAP method supports passing a different tunnelled identity.</dd>
<dt>ca-certificate (scalar)</dt>
<dd>Path to a file with one or more trusted certificate authority (CA) certificates.</dd>
<dt>client-certificate (scalar)</dt>
<dd>Path to a file containing the certificate to be used by the client during authentication.</dd>
<dt>client-key (scalar)</dt>
<dd>Path to a file containing the private key corresponding to client-certificate.</dd>
<dt>client-key-password (scalar)</dt>
<dd>Password to use to decrypt the private key specified in client-key if it is encrypted.</dd>
<dt>phase2-auth (scalar)</dt>
<dd>Phase 2 authentication mechanism.</dd></dl>
</dl>
</dl>
<h3>Properties for device type ethernets:</h3>
<p>Ethernet device definitions, beyond common ones described above, also support some additional properties that can be used for SR-IOV devices.</p>
<dl>
<dt>link (scalar)</dt>
<dd>(SR-IOV devices only) The link property declares the device as a Virtual Function of the selected Physical Function device, as identified by the given netplan id.</dd></dl>
<p> Example:</p>
<dl>
<dd>
<pre>ethernets:
 enp1: {...}
 enp1s16f1:
 link: enp1</pre>
</dd><dt>virtual-function-count (scalar)</dt>
<dd>(SR-IOV devices only) In certain special cases VFs might need to be configured outside of netplan. For such configurations virtual-function-count can be optionally used to set an explicit number of Virtual Functions for the given Physical Function. If unset, the default is to create only as many VFs as are defined in the netplan configuration. This should be used for special cases only.</dd></dl>
<h3>Properties for device type modems:</h3>
<p>GSM/CDMA modem configuration is only supported for the NetworkManager backend. systemd-networkd does not support modems.</p>
<dl>
<dt>apn (scalar)</dt>
<dd>Set the carrier APN (Access Point Name). This can be omitted if auto-config is enabled.</dd>
<dt>auto-config (bool)</dt>
<dd>Specify whether to try and autoconfigure the modem by doing a lookup of the carrier against the Mobile Broadband Provider database. This may not work for all carriers.</dd>
<dt>device-id (scalar)</dt>
<dd>Specify the device ID (as given by the WWAN management service) of the modem to match. This can be found using mmcli.</dd>
<dt>network-id (scalar)</dt>
<dd>Specify the Network ID (GSM LAI format). If this is specified, the device will not roam networks.</dd>
<dt>number (scalar)</dt>
<dd>The number to dial to establish the connection to the mobile broadband network. (Deprecated for GSM)</dd>
<dt>password (scalar)</dt>
<dd>Specify the password used to authenticate with the carrier network. This can be omitted if auto-config is enabled.</dd>
<dt>pin (scalar)</dt>
<dd>Specify the SIM PIN to allow it to operate if a PIN is set.</dd>
<dt>sim-id (scalar)</dt>
<dd>Specify the SIM unique identifier (as given by the WWAN management service) which this connection applies to. If given, the connection will apply to any device also allowed by device-id which contains a SIM card matching the given identifier.</dd>
<dt>sim-operator-id (scalar)</dt>
<dd>Specify the MCC/MNC string (such as &#8220;310260&#8221; or &#8220;21601&#8221;) which identifies the carrier that this connection should apply to. If given, the connection will apply to any device also allowed by device-id and sim-id which contains a SIM card provisioned by the given operator.</dd>
<dt>username (scalar)</dt>
<dd>Specify the username used to authentiate with the carrier network. This can be omitted if auto-config is enabled.</dd></dl>
<h3>Properties for device type wifis:</h3>
<p>Note that systemd-networkd does not natively support wifi, so you need wpasupplicant installed if you let the networkd renderer handle wifi.</p>
<dl>
<dt>access-points (mapping)</dt>
<dd>This provides pre-configured connections to NetworkManager. Note that users can of course select other access points/SSIDs. The keys of the mapping are the SSIDs, and the values are mappings with the following supported properties:</dd>
<dl>
<dd>
</dd><dl>
<dt>password (scalar)</dt>
<dd>Enable WPA2 authentication and set the passphrase for it. If neither this nor an auth block are given, the network is assumed to be open. The setting</dd>
<dl>
<dd>
</dd><dl>
<dd>
<pre> password: &quot;S3kr1t&quot;</pre>
</dd></dl>
<p> is equivalent to</p>
<dl>
<dd>
<pre> auth:
 key-management: psk
 password: &quot;S3kr1t&quot;</pre>
</dd></dl>
</dl>
<dt>mode (scalar)</dt>
<dd>Possible access point modes are infrastructure (the default), ap (create an access point to which other devices can connect), and adhoc (peer to peer networks without a central access point). ap is only supported with NetworkManager.</dd>
<dt>bssid (scalar)</dt>
<dd>If specified, directs the device to only associate with the given access point.</dd>
<dt>band (scalar)</dt>
<dd>Possible bands are 5GHz (for 5GHz 802.11a) and 2.4GHz (for 2.4GHz 802.11), do not restrict the 802.11 frequency band of the network if unset (the default).</dd>
<dt>channel (scalar)</dt>
<dd>Wireless channel to use for the Wi-Fi connection. Because channel numbers overlap between bands, this property takes effect only if the band property is also set.</dd></dl>
</dl>
<dt>wakeonwlan (sequence of scalars)</dt>
<dd>This enables WakeOnWLan on supported devices. Not all drivers support all options. May be any combination of any, disconnect, magic_pkt, gtk_rekey_failure, eap_identity_req, four_way_handshake, rfkill_release or tcp (NetworkManager only). Or the exclusive default flag (the default).</dd></dl>
<h3>Properties for device type bridges:</h3>
<dl>
<dt>interfaces (sequence of scalars)</dt>
<dd>All devices matching this ID list will be added to the bridge. This may be an empty list, in which case the bridge will be brought online with no member interfaces.</dd>
<dl>
<dd>Example:</dd>
<dl>
<dd>
<pre> ethernets:
 switchports:
 match: {name: &quot;enp2*&quot;}
 [...]
 bridges:
 br0:
 interfaces: [switchports]</pre>
</dd></dl>
</dl>
<dt>parameters (mapping)</dt>
<dd>Customization parameters for special bridging options. Time intervals may need to be expressed as a number of seconds or milliseconds: the default value type is specified below. If necessary, time intervals can be qualified using a time suffix (such as &#8220;s&#8221; for seconds, &#8220;ms&#8221; for milliseconds) to allow for more control over its behavior.</dd>
<dl>
<dd>
</dd><dl>
<dt>ageing-time (scalar)</dt>
<dd>Set the period of time to keep a MAC address in the forwarding database after a packet is received. This maps to the AgeingTimeSec= property when the networkd renderer is used. If no time suffix is specified, the value will be interpreted as seconds.</dd>
<dt>priority (scalar)</dt>
<dd>Set the priority value for the bridge. This value should be a number between 0 and 65535. Lower values mean higher priority. The bridge with the higher priority will be elected as the root bridge.</dd>
<dt>port-priority (scalar)</dt>
<dd>Set the port priority to . The priority value is a number between 0 and 63. This metric is used in the designated port and root port selection algorithms.</dd>
<dt>forward-delay (scalar)</dt>
<dd>Specify the period of time the bridge will remain in Listening and Learning states before getting to the Forwarding state. This field maps to the ForwardDelaySec= property for the networkd renderer. If no time suffix is specified, the value will be interpreted as seconds.</dd>
<dt>hello-time (scalar)</dt>
<dd>Specify the interval between two hello packets being sent out from the root and designated bridges. Hello packets communicate information about the network topology. When the networkd renderer is used, this maps to the HelloTimeSec= property. If no time suffix is specified, the value will be interpreted as seconds.</dd>
<dt>max-age (scalar)</dt>
<dd>Set the maximum age of a hello packet. If the last hello packet is older than that value, the bridge will attempt to become the root bridge. This maps to the MaxAgeSec= property when the networkd renderer is used. If no time suffix is specified, the value will be interpreted as seconds.</dd>
<dt>path-cost (scalar)</dt>
<dd>Set the cost of a path on the bridge. Faster interfaces should have a lower cost. This allows a finer control on the network topology so that the fastest paths are available whenever possible.</dd>
<dt>stp (bool)</dt>
<dd>Define whether the bridge should use Spanning Tree Protocol. The default value is &#8220;true&#8221;, which means that Spanning Tree should be used.</dd></dl>
</dl>
</dl>
<h3>Properties for device type bonds:</h3>
<dl>
<dt>interfaces (sequence of scalars)</dt>
<dd>All devices matching this ID list will be added to the bond.</dd>
<dl>
<dd>Example:</dd>
<dl>
<dd>
<pre> ethernets:
 switchports:
 match: {name: &quot;enp2*&quot;}
 [...]
 bonds:
 bond0:
 interfaces: [switchports]</pre>
</dd></dl>
</dl>
<dt>parameters (mapping)</dt>
<dd>Customization parameters for special bonding options. Time intervals may need to be expressed as a number of seconds or milliseconds: the default value type is specified below. If necessary, time intervals can be qualified using a time suffix (such as &#8220;s&#8221; for seconds, &#8220;ms&#8221; for milliseconds) to allow for more control over its behavior.</dd>
<dl>
<dd>
</dd><dl>
<dt>mode (scalar)</dt>
<dd>Set the bonding mode used for the interfaces. The default is balance-rr (round robin). Possible values are balance-rr, active-backup, balance-xor, broadcast, 802.3ad, balance-tlb, and balance-alb.</dd>
<dt>lacp-rate (scalar)</dt>
<dd>Set the rate at which LACPDUs are transmitted. This is only useful in 802.3ad mode. Possible values are slow (30 seconds, default), and fast (every second).</dd>
<dt>mii-monitor-interval (scalar)</dt>
<dd>Specifies the interval for MII monitoring (verifying if an interface of the bond has carrier). The default is 0; which disables MII monitoring. This is equivalent to the MIIMonitorSec= field for the networkd backend. If no time suffix is specified, the value will be interpreted as milliseconds.</dd>
<dt>min-links (scalar)</dt>
<dd>The minimum number of links up in a bond to consider the bond interface to be up.</dd>
<dt>transmit-hash-policy (scalar)</dt>
<dd>Specifies the transmit hash policy for the selection of slaves. This is only useful in balance-xor, 802.3ad and balance-tlb modes. Possible values are layer2, layer3+4, layer2+3, encap2+3, and encap3+4.</dd>
<dt>ad-select (scalar)</dt>
<dd>Set the aggregation selection mode. Possible values are stable, bandwidth, and count. This option is only used in 802.3ad mode.</dd>
<dt>all-slaves-active (bool)</dt>
<dd>If the bond should drop duplicate frames received on inactive ports, set this option to false. If they should be delivered, set this option to true. The default value is false, and is the desirable behavior in most situations.</dd>
<dt>arp-interval (scalar)</dt>
<dd>Set the interval value for how frequently ARP link monitoring should happen. The default value is 0, which disables ARP monitoring. For the networkd backend, this maps to the ARPIntervalSec= property. If no time suffix is specified, the value will be interpreted as milliseconds.</dd>
<dt>arp-ip-targets (sequence of scalars)</dt>
<dd>IPs of other hosts on the link which should be sent ARP requests in order to validate that a slave is up. This option is only used when arp-interval is set to a value other than 0. At least one IP address must be given for ARP link monitoring to function. Only IPv4 addresses are supported. You can specify up to 16 IP addresses. The default value is an empty list.</dd>
<dt>arp-validate (scalar)</dt>
<dd>Configure how ARP replies are to be validated when using ARP link monitoring. Possible values are none, active, backup, and all.</dd>
<dt>arp-all-targets (scalar)</dt>
<dd>Specify whether to use any ARP IP target being up as sufficient for a slave to be considered up; or if all the targets must be up. This is only used for active-backup mode when arp-validate is enabled. Possible values are any and all.</dd>
<dt>up-delay (scalar)</dt>
<dd>Specify the delay before enabling a link once the link is physically up. The default value is 0. This maps to the UpDelaySec= property for the networkd renderer. This option is only valid for the miimon link monitor. If no time suffix is specified, the value will be interpreted as milliseconds.</dd>
<dt>down-delay (scalar)</dt>
<dd>Specify the delay before disabling a link once the link has been lost. The default value is 0. This maps to the DownDelaySec= property for the networkd renderer. This option is only valid for the miimon link monitor. If no time suffix is specified, the value will be interpreted as milliseconds.</dd>
<dt>fail-over-mac-policy (scalar)</dt>
<dd>Set whether to set all slaves to the same MAC address when adding them to the bond, or how else the system should handle MAC addresses. The possible values are none, active, and follow.</dd>
<dt>gratuitous-arp (scalar)</dt>
<dd>Specify how many ARP packets to send after failover. Once a link is up on a new slave, a notification is sent and possibly repeated if this value is set to a number greater than 1. The default value is 1 and valid values are between 1 and 255. This only affects active-backup mode.</dd>
<dl>
<dd>For historical reasons, the misspelling gratuitious-arp is also accepted and has the same function.</dd></dl>
<dt>packets-per-slave (scalar)</dt>
<dd>In balance-rr mode, specifies the number of packets to transmit on a slave before switching to the next. When this value is set to 0, slaves are chosen at random. Allowable values are between 0 and 65535. The default value is 1. This setting is only used in balance-rr mode.</dd>
<dt>primary-reselect-policy (scalar)</dt>
<dd>Set the reselection policy for the primary slave. On failure of the active slave, the system will use this policy to decide how the new active slave will be chosen and how recovery will be handled. The possible values are always, better, and failure.</dd>
<dt>resend-igmp (scalar)</dt>
<dd>In modes balance-rr, active-backup, balance-tlb and balance-alb, a failover can switch IGMP traffic from one slave to another.</dd>
<dl>
<dd>This parameter specifies how many IGMP membership reports are issued on a failover event. Values range from 0 to 255. 0 disables sending membership reports. Otherwise, the first membership report is sent on failover and subsequent reports are sent at 200ms intervals.</dd></dl>
<dt>learn-packet-interval (scalar)</dt>
<dd>Specify the interval between sending learning packets to each slave. The value range is between 1 and 0x7fffffff. The default value is 1. This option only affects balance-tlb and balance-alb modes. Using the networkd renderer, this field maps to the LearnPacketIntervalSec= property. If no time suffix is specified, the value will be interpreted as seconds.</dd>
<dt>primary (scalar)</dt>
<dd>Specify a device to be used as a primary slave, or preferred device to use as a slave for the bond (ie. the preferred device to send data through), whenever it is available. This only affects active-backup, balance-alb, and balance-tlb modes.</dd></dl>
</dl>
</dl>
<h3>Properties for device type tunnels:</h3>
<p>Tunnels allow traffic to pass as if it was between systems on the same local network, although systems may be far from each other but reachable via the Internet. They may be used to support IPv6 traffic on a network where the ISP does not provide the service, or to extend and &#8220;connect&#8221; separate local networks. Please see <a rel="nofollow" href="https://en.wikipedia.org/wiki/Tunneling_protocol">https://en.wikipedia.org/wiki/Tunneling_protocol</a> for more general information about tunnels.</p>
<dl>
<dt>mode (scalar)</dt>
<dd>Defines the tunnel mode. Valid options are sit, gre, ip6gre, ipip, ipip6, ip6ip6, vti, and vti6. Additionally, the networkd backend also supports gretap and ip6gretap modes. In addition, the NetworkManager backend supports isatap tunnels.</dd>
<dt>local (scalar)</dt>
<dd>Defines the address of the local endpoint of the tunnel.</dd>
<dt>remote (scalar)</dt>
<dd>Defines the address of the remote endpoint of the tunnel.</dd>
<dt>key (scalar or mapping)</dt>
<dd>Define keys to use for the tunnel. The key can be a number or a dotted quad (an IPv4 address). It is used for identification of IP transforms. This is only required for vti and vti6 when using the networkd backend, and for gre or ip6gre tunnels when using the NetworkManager backend.</dd>
<dl>
<dd>This field may be used as a scalar (meaning that a single key is specified and to be used for both input and output key), or as a mapping, where you can then further specify input and output.</dd>
<dl>
<dt>input (scalar)</dt>
<dd>The input key for the tunnel</dd>
<dt>output (scalar)</dt>
<dd>The output key for the tunnel</dd></dl>
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
</dd><dt>keys (scalar or mapping)</dt>
<dd>Alternate name for the key field. See above.</dd></dl>
<h3>Properties for device type vlans:</h3>
<dl>
<dt>id (scalar)</dt>
<dd>VLAN ID, a number between 0 and 4094.</dd>
<dt>link (scalar)</dt>
<dd>netplan ID of the underlying device definition on which this VLAN gets created.</dd></dl>
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
</dd></dl>
<h3>Backend-specific configuration parameters</h3>
<p>In addition to the other fields available to configure interfaces, some backends may require to record some of their own parameters in netplan, especially if the netplan definitions are generated automatically by the consumer of that backend. Currently, this is only used with NetworkManager.</p>
<dl>
<dt>networkmanager (mapping)</dt>
<dd>Keeps the NetworkManager-specific configuration parameters used by the daemon to recognize connections.</dd>
<dl>
<dd>
</dd><dl>
<dt>name (scalar)</dt>
<dd>Set the display name for the connection.</dd>
<dt>uuid (scalar)</dt>
<dd>Defines the UUID (unique identifier) for this connection, as generated by NetworkManager itself.</dd>
<dt>stable-id (scalar)</dt>
<dd>Defines the stable ID (a different form of a connection name) used by NetworkManager in case the name of the connection might otherwise change, such as when sharing connections between users.</dd>
<dt>device (scalar)</dt>
<dd>Defines the interface name for which this connection applies.</dd></dl>
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
</dd></dl>
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
</dd></dl>
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
</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-netplan-generate/">netplan-generate</a>(8), <a href="/docs/linux/man/8-netplan-apply/">netplan-apply</a>(8), <a href="/docs/linux/man/8-netplan-try/">netplan-try</a>(8), <a href="/docs/linux/man/8-systemd-networkd/">systemd-networkd</a>(8), <a href="/docs/linux/man/8-networkmanager/">NetworkManager</a>(8)</p>
<h2>Authors</h2>
<p>Mathieu Trudel-Lapierre (&lt;cyphermox [at] ubuntu.com&gt;); Martin Pitt (&lt;martin.pitt [at] ubuntu.com&gt;).</p>
