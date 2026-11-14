---
title: "networkmanager(5)"
name: "networkmanager"
section: "5"
letter: "n"
url: "/docs/linux/man/5-networkmanager/"
description: "NetworkManager.conf – NetworkManager configuration file"
---

<p>NetworkManager.conf &#8211; NetworkManager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/NetworkManager/NetworkManager.conf, /etc/NetworkManager/conf.d/<i>name</i>.conf</p>
<h2>Description</h2>
<p>This is a configuration file for NetworkManager. It is used to set up various aspects of NetworkManager&#8217;s behavior. The location of the file may be changed through use of the <code>&#8211;config</code> argument for NetworkManager. </p>
<p> If a default NetworkManager.conf is provided by your distribution&#8217;s packages, you should not modify it, since your changes may get overwritten by package updates. Instead, you can add additional .conf files to the conf.d directory. These will be read in order, with later files overriding earlier ones.</p>
<h2>File Format</h2>
<p>The configuration file format is so-called key file (sort of ini-style format). It consists of sections (groups) of key-value pairs. Lines beginning with a &#8216;#&#8217; and blank lines are considered comments. Sections are started by a header line containing the section enclosed in &#8216;[&#8216; and &#8216;]&#8217;, and ended implicitly by the start of the next section or the end of the file. Each key-value pair must be contained in a section. </p>
<p> For keys that take a list of devices as their value, you can specify devices by their MAC addresses or interface names, or &quot;*&quot; to specify all devices. </p>
<p> Minimal system settings configuration file looks like this: </p>
<dl>
<dd>
<pre> [main]
 plugins=keyfile</pre>
</dl>
<p> As an extension to the normal keyfile format, you can also append a value to a previously-set list-valued key by doing: </p>
<dl>
<dd>
<pre> plugins+=another-plugin</pre>
</dl>
<h2>Main Section</h2>
<p><i>plugins</i></p>
<dl>
<dd>Lists system settings plugin names separated by &#8216;,&#8217;. These plugins are used to read and write system-wide connections. When multiple plugins are specified, the connections are read from all listed plugins. When writing connections, the plugins will be asked to save the connection in the order listed here; if the first plugin cannot write out that connection type (or can&#8217;t write out any connections) the next plugin is tried, etc. If none of the plugins can save the connection, an error is returned to the user. </p>
<p> If NetworkManager defines a distro-specific network-configuration plugin for your system, then that will normally be listed here. (See below for the available plugins.) Note that the keyfile plugin is always appended to the end of this list (if it doesn&#8217;t already appear earlier in the list), so if there is no distro-specific plugin for your system then you can leave this key unset and NetworkManager will default to using keyfile.</dl>
<p> <i>monitor-connection-files</i></p>
<dl>
<dd>Whether the configured settings plugin(s) should set up file monitors and immediately pick up changes made to connection files while NetworkManager is running. This is disabled by default; NetworkManager will only read the connection files at startup, and when explicitly requested via the ReloadConnections D-Bus call. If this key is set to &#8216;true&#8217;, then NetworkManager will reload connection files any time they changed.</dl>
<p> <i>dhcp</i></p>
<dl>
<dd>This key sets up what DHCP client NetworkManager will use. Presently dhclient and dhcpcd are supported. The client configured here should be available on your system too. If this key is missing, available DHCP clients are looked for in this order: dhclient, dhcpcd.</dl>
<p> <i>no-auto-default</i></p>
<dl>
<dd>Comma-separated list of devices for which NetworkManager shouldn&#8217;t create default wired connection (Auto eth0). By default, NetworkManager creates a temporary wired connection for any Ethernet device that is managed and doesn&#8217;t have a connection configured. List a device in this option to inhibit creating the default connection for the device. May have the special value * to apply to all devices. </p>
<p> When the default wired connection is deleted or saved to a new persistent connection by a plugin, the device is added to a list in the file /var/run/NetworkManager/no-auto-default.state to prevent creating the default connection for that device again. </p>
<dl>
<dd>
<pre> no-auto-default=00:22:68:5c:5d:c4,00:1e:65:ff:aa:ee
 no-auto-default=eth0,eth1
 no-auto-default=*</pre>
</dl>
</dl>
<p> <i>ignore-carrier</i></p>
<dl>
<dd>Comma-separated list of devices for which NetworkManager will (partially) ignore the carrier state. Normally, for device types that support carrier-detect, such as Ethernet and InfiniBand, NetworkManager will only allow a connection to be activated on the device if carrier is present (ie, a cable is plugged in), and it will deactivate the device if carrier drops for more than a few seconds. </p>
<p> Listing a device here will allow activating connections on that device even when it does not have carrier, provided that the connection uses only statically-configured IP addresses. Additionally, it will allow any active connection (whether static or dynamic) to remain active on the device when carrier is lost. </p>
<p> May have the special value * to apply to all devices. </p>
<p> Note that the &quot;carrier&quot; property of NMDevices and device D-Bus interfaces will still reflect the actual device state; it&#8217;s just that NetworkManager will not make use of that information.</dl>
<p> <i>dns</i></p>
<dl>
<dd>Set the DNS (resolv.conf) processing mode. </p>
<p> default: The default if the key is not specified. NetworkManager will update resolv.conf to reflect the nameservers provided by currently active connections. </p>
<p> dnsmasq: NetworkManager will run dnsmasq as a local caching nameserver, using a &quot;split DNS&quot; configuration if you are connected to a VPN, and then update resolv.conf to point to the local nameserver. </p>
<p> unbound: NetworkManager will talk to unbound and dnssec-triggerd, providing a &quot;split DNS&quot; configuration with DNSSEC support. The /etc/resolv.conf will be managed by dnssec-trigger daemon. </p>
<p> none: NetworkManager will not modify resolv.conf.</dl>
<p> <i>debug</i></p>
<dl>
<dd>Comma separated list of options to aid debugging. This value will be combined with the environment variable NM_DEBUG. Currently the following values are supported: </p>
<p> RLIMIT_CORE: set ulimit -c unlimited to write out core dumps.</dl>
<h2>Keyfile Section</h2>
<p>This section contains keyfile-plugin-specific options, and is normally only used when you are not using any other distro-specific plugin. </p>
<p> <i>hostname</i></p>
<dl>
<dd>Set a persistent hostname.</dl>
<p> <i>unmanaged-devices</i></p>
<dl>
<dd>Set devices that should be ignored by NetworkManager when using the keyfile plugin. Devices are specified in the following format: </p>
<p> mac:&lt;hwaddr&gt; or interface-name:&lt;ifname&gt;. Here hwaddr is the MAC address of the device to be ignored, in hex-digits-and-colons notation. ifname is the interface name of the ignored device. </p>
<p> Multiple entries are separated with semicolons. No spaces are allowed in the value. </p>
<p> Example: </p>
<dl>
<dd>
<pre>unmanaged-devices=interface-name:em4
unmanaged-devices=mac:00:22:68:1c:59:b1;mac:00:1E:65:30:D1:C4;interface-name:eth2</pre>
</dl>
</dl>
<h2>Ifupdown Section</h2>
<p>This section contains ifupdown-specific options and thus only has effect when using the ifupdown plugin. </p>
<p> <i>managed</i></p>
<dl>
<dd>If set to true, then interfaces listed in /etc/network/interfaces are managed by NetworkManager. If set to false, then any interface listed in /etc/network/interfaces will be ignored by NetworkManager. Remember that NetworkManager controls the default route, so because the interface is ignored, NetworkManager may assign the default route to some other interface. </p>
<p> The default value is false.</dl>
<h2>Logging Section</h2>
<p>This section controls NetworkManager&#8217;s logging. Any settings here are overridden by the <code>&#8211;log-level</code> and <code>&#8211;log-domains</code> command-line options. </p>
<p> <i>level</i></p>
<dl>
<dd>The default logging verbosity level. One of ERR, WARN, INFO, DEBUG, TRACE. The ERR level logs only critical errors. WARN logs warnings that may reflect operation. INFO logs various informational messages that are useful for tracking state and operations. DEBUG enables verbose logging for debugging purposes. TRACE enables even more verbose logging then DEBUG level. Subsequent levels also log all messages from earlier levels; thus setting the log level to INFO also logs error and warning messages.</dl>
<p> <i>domains</i></p>
<dl>
<dd>The following log domains are available: PLATFORM, RFKILL, ETHER, WIFI, BT, MB, DHCP4, DHCP6, PPP, WIFI_SCAN, IP4, IP6, AUTOIP4, DNS, VPN, SHARING, SUPPLICANT, AGENTS, SETTINGS, SUSPEND, CORE, DEVICE, OLPC, WIMAX, INFINIBAND, FIREWALL, ADSL, BOND, VLAN, BRIDGE, DBUS_PROPS, TEAM, CONCHECK, DCB, DISPATCH. </p>
<p> In addition, these special domains can be used: NONE, ALL, DEFAULT, DHCP, IP. </p>
<p> You can specify per-domain log level overrides by adding a colon and a log level to any domain. E.g., &quot;WIFI:DEBUG&quot;.</dl>
<dl>
<dd>Domain descriptions:</p>
<dl>
<dd>PLATFORM : OS (platform) operations</dl>
<dl>
<dd>RFKILL : RFKill subsystem operations</dl>
<dl>
<dd>ETHER : Ethernet device operations</dl>
<dl>
<dd>WIFI : Wi-Fi device operations</dl>
<dl>
<dd>BT : Bluetooth operations</dl>
<dl>
<dd>MB : Mobile broadband operations</dl>
<dl>
<dd>DHCP4 : DHCP for IPv4</dl>
<dl>
<dd>DHCP6 : DHCP for IPv6</dl>
<dl>
<dd>PPP : Point-to-point protocol operations</dl>
<dl>
<dd>WIFI_SCAN : Wi-Fi scanning operations</dl>
<dl>
<dd>IP4 : IPv4-related operations</dl>
<dl>
<dd>IP6 : IPv6-related operations</dl>
<dl>
<dd>AUTOIP4 : AutoIP (avahi) operations</dl>
<dl>
<dd>DNS : Domain Name System related operations</dl>
<dl>
<dd>VPN : Virtual Private Network connections and operations</dl>
<dl>
<dd>SHARING : Connection sharing</dl>
<dl>
<dd>SUPPLICANT : WPA supplicant related operations</dl>
<dl>
<dd>AGENTS : Secret agents operations and communication</dl>
<dl>
<dd>SETTINGS : Settings/config service operations</dl>
<dl>
<dd>SUSPEND : Suspend/resume</dl>
<dl>
<dd>CORE : Core daemon and policy operations</dl>
<dl>
<dd>DEVICE : Activation and general interface operations</dl>
<dl>
<dd>OLPC : OLPC Mesh device operations</dl>
<dl>
<dd>WIMAX : WiMAX device operations</dl>
<dl>
<dd>INFINIBAND : InfiniBand device operations</dl>
<dl>
<dd>FIREWALL : FirewallD related operations</dl>
<dl>
<dd>ADSL : ADSL device operations</dl>
<dl>
<dd>BOND : Bonding operations</dl>
<dl>
<dd>VLAN : VLAN operations</dl>
<dl>
<dd>BRIDGE : Bridging operations</dl>
<dl>
<dd>DBUS_PROPS : D-Bus property changes</dl>
<dl>
<dd>TEAM : Teaming operations</dl>
<dl>
<dd>CONCHECK : Connectivity check</dl>
<dl>
<dd>DCB : Data Center Bridging (DCB) operations</dl>
<dl>
<dd>DISPATCH : Dispatcher scripts</dl>
<dl>
<dd>&nbsp;<wbr></dl>
<dl>
<dd>NONE : when given by itself logging is disabled</dl>
<dl>
<dd>ALL : all log domains</dl>
<dl>
<dd>DEFAULT : default log domains</dl>
<dl>
<dd>DHCP : shortcut for &quot;DHCP4,DHCP6&quot;</dl>
<dl>
<dd>IP : shortcut for &quot;IP4,IP6&quot;</dl>
<dl>
<dd>&nbsp;<wbr></dl>
<dl>
<dd>HW : deprecated alias for &quot;PLATFORM&quot;</dl>
</dl>
<h2>Connectivity Section</h2>
<p>This section controls NetworkManager&#8217;s optional connectivity checking functionality. This allows NetworkManager to detect whether or not the system can actually access the internet or whether it is behind a captive portal. </p>
<p> <i>uri</i></p>
<dl>
<dd>The URI of a web page to periodically request when connectivity is being checked. This page should return the header &quot;X-NetworkManager-Status&quot; with a value of &quot;online&quot;. Alternatively, it&#8217;s body content should be set to &quot;NetworkManager is online&quot;. The body content check can be controlled by the response option. If this option is blank or missing, connectivity checking is disabled.</dl>
<p> <i>interval</i></p>
<dl>
<dd>Specified in seconds; controls how often connectivity is checked when a network connection exists. If set to 0 connectivity checking is disabled. If missing, the default is 300 seconds.</dl>
<p> <i>response</i></p>
<dl>
<dd>If set controls what body content NetworkManager checks for when requesting the URI for connectivity checking. If missing, defaults to &quot;NetworkManager is online&quot;</dl>
<h2>Plugins</h2>
<p><i>keyfile</i></p>
<dl>
<dd>The keyfile plugin is the generic plugin that supports all the connection types and capabilities that NetworkManager has. It writes files out in an .ini-style format in /etc/NetworkManager/system-connections. </p>
<p> The stored connection file may contain passwords and private keys, so it will be made readable only to root, and the plugin will ignore files that are readable or writeable by any user or group other than root. </p>
<p> This plugin is always active, and will automatically be used to store any connections that aren&#8217;t supported by any other active plugin.</dl>
<p> <i>ifcfg-rh</i></p>
<dl>
<dd>This plugin is used on the Fedora and Red Hat Enterprise Linux distributions to read and write configuration from the standard /etc/sysconfig/network-scripts/ifcfg-* files. It currently supports reading Ethernet, Wi-Fi, InfiniBand, VLAN, Bond, Bridge, and Team connections.</dl>
<p> <i>ifcfg-suse</i></p>
<dl>
<dd>This plugin is only provided for simple backward compatibility with SUSE and OpenSUSE configuration. Most setups should be using the keyfile plugin instead. The ifcfg-suse plugin supports reading Ethernet and Wi-Fi connections, but does not support saving any connection types.</dl>
<p> <i>ifupdown</i></p>
<dl>
<dd>This plugin is used on the Debian and Ubuntu distributions, and reads Ethernet and Wi-Fi connections from /etc/network/interfaces. </p>
<p> This plugin is read-only; any connections (of any type) added from within NetworkManager when you are using this plugin will be saved using the keyfile plugin instead.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/5-nmcli-examples/">nmcli-examples</a></code>(5), <code><a href="/docs/linux/man/1-nm-online/">nm-online</a></code>(1), <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1) </p>
