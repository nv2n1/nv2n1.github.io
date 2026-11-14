---
title: "nm-system-settings-conf(5)"
name: "nm-system-settings-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nm-system-settings-conf/"
description: "NetworkManager.conf – NetworkManager configuration file"
---

<p>NetworkManager.conf &#8211; NetworkManager configuration file</p>
<h2>Synopsis</h2>
<p>/etc/NetworkManager/NetworkManager.conf, /etc/NetworkManager/conf.d/<i>name</i>.conf, /run/NetworkManager/conf.d/<i>name</i>.conf, /usr/lib/NetworkManager/conf.d/<i>name</i>.conf, /var/lib/NetworkManager/NetworkManager-intern.conf</p>
<h2>Description</h2>
<p>NetworkManager.conf is the configuration file for NetworkManager. It is used to set up various aspects of NetworkManager&#8217;s behavior. The location of the main file and configuration directories may be changed through use of the <code>&#8211;config</code>, <code>&#8211;config-dir</code>, <code>&#8211;system-config-dir</code>, and <code>&#8211;intern-config</code> argument for NetworkManager, respectively. </p>
<p> If a default NetworkManager.conf is provided by your distribution&#8217;s packages, you should not modify it, since your changes may get overwritten by package updates. Instead, you can add additional .conf files to the /etc/NetworkManager/conf.d directory. These will be read in order, with later files overriding earlier ones. Packages might install further configuration snippets to /usr/lib/NetworkManager/conf.d. This directory is parsed first, even before NetworkManager.conf. Scripts can also put per-boot configuration into /run/NetworkManager/conf.d. This directory is parsed second, also before NetworkManager.conf. The loading of a file /run/NetworkManager/conf.d/<i>name</i>.conf can be prevented by adding a file /etc/NetworkManager/conf.d/<i>name</i>.conf. Likewise, a file /usr/lib/NetworkManager/conf.d/<i>name</i>.conf can be shadowed by putting a file of the same name to either /etc/NetworkManager/conf.d or /run/NetworkManager/conf.d. </p>
<p> NetworkManager can overwrite certain user configuration options via D-Bus or other internal operations. In this case it writes those changes to /var/lib/NetworkManager/NetworkManager-intern.conf. This file is not intended to be modified by the user, but it is read last and can shadow user configuration from NetworkManager.conf. </p>
<p> Certain settings from the configuration can be reloaded at runtime either by sending SIGHUP signal or via D-Bus&#8217; Reload call. </p>
<p> NetworkManager does not require any configuration in NetworkManager.conf. Depending on your use case, you may remove all files to restore the default configuration (factory reset). But note that your distribution or other packages may drop configuration snippets for NetworkManager, such that they are part of the factory default.</p>
<h2>File Format</h2>
<p>The configuration file format is so-called key file (sort of ini-style format). It consists of sections (groups) of key-value pairs. Lines beginning with a &#8216;#&#8217; and blank lines are considered comments. Sections are started by a header line containing the section enclosed in &#8216;[&#8216; and &#8216;]&#8217;, and ended implicitly by the start of the next section or the end of the file. Each key-value pair must be contained in a section. </p>
<p> For keys that take a list of devices as their value, you can specify devices by their MAC addresses or interface names, or &quot;*&quot; to specify all devices. See the section called &#8220;Device List Format&#8221; below. </p>
<p> A simple configuration file looks like this: </p>
<dl>
<dd>
<pre>[main]
plugins=keyfile</pre>
</dl>
<p> As an extension to the normal keyfile format, you can also append a value to a previously-set list-valued key by doing: </p>
<dl>
<dd>
<pre>plugins+=another-plugin
plugins-=remove-me</pre>
</dl>
<h2>Main Section</h2>
<p><i>plugins</i></p>
<dl>
<dd>Lists system settings plugin names separated by &#8216;,&#8217;. These plugins are used to read and write system-wide connection profiles. When multiple plugins are specified, the connections are read from all listed plugins. When writing connections, the plugins will be asked to save the connection in the order listed here; if the first plugin cannot write out that connection type (or can&#8217;t write out any connections) the next plugin is tried, etc. If none of the plugins can save the connection, an error is returned to the user. </p>
<p> The default value and the number of available plugins is distro-specific. See the section called &#8220;PLUGINS&#8221; below for the available plugins. Note that NetworkManager&#8217;s native keyfile plugin is always appended to the end of this list (if it doesn&#8217;t already appear earlier in the list).</dl>
<p> <i>monitor-connection-files</i></p>
<dl>
<dd>This setting is deprecated and has no effect. Profiles from disk are never automatically reloaded. Use for example nmcli connection (re)load for that.</dl>
<p> <i>auth-polkit</i></p>
<dl>
<dd>Whether the system uses PolicyKit for authorization. If true, non-root requests are authorized using PolicyKit. Requests from root (user ID zero) are always granted without asking PolicyKit. If false, all requests will be allowed and PolicyKit is not used. If set to root-only PolicyKit is not used and all requests except root are denied. The default value is true.</dl>
<p> <i>dhcp</i></p>
<dl>
<dd>This key sets up what DHCP client NetworkManager will use. Allowed values are dhclient, dhcpcd, and internal. The dhclient and dhcpcd options require the indicated clients to be installed. The internal option uses a built-in DHCP client which is not currently as featureful as the external clients. </p>
<p> If this key is missing, it defaults to internal. If the chosen plugin is not available, clients are looked for in this order: dhclient, dhcpcd, internal.</dl>
<p> <i>no-auto-default</i></p>
<dl>
<dd>Specify devices for which NetworkManager shouldn&#8217;t create default wired connection (Auto eth0). By default, NetworkManager creates a temporary wired connection for any Ethernet device that is managed and doesn&#8217;t have a connection configured. List a device in this option to inhibit creating the default connection for the device. May have the special value * to apply to all devices. </p>
<p> When the default wired connection is deleted or saved to a new persistent connection by a plugin, the device is added to a list in the file /var/lib/NetworkManager/no-auto-default.state to prevent creating the default connection for that device again. </p>
<p> See the section called &#8220;Device List Format&#8221; for the syntax how to specify a device. </p>
<p> Example: </p>
<dl>
<dd>
<pre>no-auto-default=00:22:68:5c:5d:c4,00:1e:65:ff:aa:ee
no-auto-default=eth0,eth1
no-auto-default=*</pre>
</dl>
</dl>
<p> <i>ignore-carrier</i></p>
<dl>
<dd>This setting is deprecated for the per-device setting ignore-carrier which overwrites this setting if specified (See <i>ignore-carrier</i>). Otherwise, it is a list of matches to specify for which device carrier should be ignored. See the section called &#8220;Device List Format&#8221; for the syntax how to specify a device. Note that master types like bond, bridge, and team ignore carrier by default. You can however revert that default using the &quot;except:&quot; specifier (or better, use the per-device setting instead of the deprecated setting).</dl>
<p> <i>assume-ipv6ll-only</i></p>
<dl>
<dd>Specify devices for which NetworkManager will try to generate a connection based on initial configuration when the device only has an IPv6 link-local address. </p>
<p> See the section called &#8220;Device List Format&#8221; for the syntax how to specify a device.</dl>
<p> <i>configure-and-quit</i></p>
<dl>
<dd>This option is no longer useful to configure in NetworkManager.conf file. It can however also be configured on the command line with the same values, where it has some use. </p>
<p> When set to &#8216;initrd&#8217;, NetworkManager does not connect to D-Bus and quits after configuring the network. This is an implementation detail how the NetworkManager module of dracut can run NetworkManager. An alternative to this is having NetworkManager as a systemd service with D-Bus in initrd. </p>
<p> The value &#8216;true&#8217; is unsupported since version 1.36. Previously this was a mode where NetworkManager would quit after configuring the network and run helper processes for DHCP and SLAAC. </p>
<p> Otherwise, NetworkManager runs a system service with D-Bus and does not quit during normal operation.</dl>
<p> <i>hostname-mode</i></p>
<dl>
<dd>Set the management mode of the hostname. This parameter will affect only the transient hostname. If a valid static hostname is set, NetworkManager will skip the update of the hostname despite the value of this option. An hostname empty or equal to &#8216;localhost&#8217;, &#8216;localhost6&#8217;, &#8216;localhost.localdomain&#8217; or &#8216;localhost6.localdomain&#8217; is considered invalid. </p>
<p> default: NetworkManager will update the hostname with the one provided via DHCP or reverse DNS lookup of the IP address on the connection with the default route or on any connection with the property hostname.only-from-default set to &#8216;false&#8217;. Connections are considered in order of increasing value of the hostname.priority property. In case multiple connections have the same priority, connections activated earlier are considered first. If no hostname can be determined in such way, the hostname will be updated to the last one set outside NetworkManager or to &#8216;localhost.localdomain&#8217;. </p>
<p> dhcp: this is similar to &#8216;default&#8217;, with the difference that after trying to get the DHCP hostname, reverse DNS lookup is not done. Note that selecting this option is equivalent to setting the property &#8216;hostname.from-dns-lookup&#8217; to &#8216;false&#8217; globally for all connections in NetworkManager.conf. </p>
<p> none: NetworkManager will not manage the transient hostname and will never set it.</dl>
<p> <i>dns</i></p>
<dl>
<dd>Set the DNS processing mode. </p>
<p> If the key is unspecified, default is used, unless /etc/resolv.conf is a symlink to /run/systemd/resolve/stub-resolv.conf, /run/systemd/resolve/resolv.conf, /lib/systemd/resolv.conf or /usr/lib/systemd/resolv.conf. In that case, systemd-resolved is chosen automatically. </p>
<p> default: NetworkManager will update /etc/resolv.conf to reflect the nameservers provided by currently active connections. The rc-manager setting (below) controls how this is done. </p>
<p> dnsmasq: NetworkManager will run dnsmasq as a local caching nameserver, using &quot;Conditional Forwarding&quot; if you are connected to a VPN, and then update resolv.conf to point to the local nameserver. It is possible to pass custom options to the dnsmasq instance by adding them to files in the &quot;/etc/NetworkManager/dnsmasq.d/&quot; directory. Note that when multiple upstream servers are available, dnsmasq will initially contact them in parallel and then use the fastest to respond, probing again other servers after some time. This behavior can be modified passing the &#8216;all-servers&#8217; or &#8216;strict-order&#8217; options to dnsmasq (see the manual page for more details). </p>
<p> systemd-resolved: NetworkManager will push the DNS configuration to systemd-resolved </p>
<p> unbound: NetworkManager will talk to unbound and dnssec-triggerd, using &quot;Conditional Forwarding&quot; with DNSSEC support. /etc/resolv.conf will be managed by dnssec-trigger daemon. This option is deprecated. Note that dnssec-trigger ships a NetworkManager dispatcher script so this DNS plugin is not necessary. </p>
<p> none: NetworkManager will not modify resolv.conf. This implies rc-manager unmanaged </p>
<p> Note that the plugins dnsmasq, systemd-resolved and unbound are caching local nameservers. Hence, when NetworkManager writes /run/NetworkManager/resolv.conf and /etc/resolv.conf (according to rc-manager setting below), the name server there will be localhost only. NetworkManager also writes a file /run/NetworkManager/no-stub-resolv.conf that contains the original name servers pushed to the DNS plugin. </p>
<p> When using dnsmasq and systemd-resolved per-connection added dns servers will always be queried using the device the connection has been activated on.</dl>
<p> <i>rc-manager</i></p>
<dl>
<dd>Set the resolv.conf management mode. This option is about how NetworkManager writes to /etc/resolv.conf, if at all. The default value depends on NetworkManager build options, and this version of NetworkManager was build with a default of &quot;&quot;. Regardless of this setting, NetworkManager will always write its version of resolv.conf to its runtime state directory as /run/NetworkManager/resolv.conf. </p>
<p> If you configure dns=none or make /etc/resolv.conf immutable with chattr +i, NetworkManager will ignore this setting and always choose unmanaged (below). </p>
<p> auto: if systemd-resolved plugin is configured via the dns setting or if it gets detected as main DNS plugin, NetworkManager will update systemd-resolved without touching /etc/resolv.conf. Alternatively, if resolvconf or netconfig are enabled at compile time and the respective binary is found, NetworkManager will automatically use it. Note that if you install or uninstall these binaries, you need to reload the rc-manager setting with SIGHUP or systemctl reload NetworkManager. As last fallback it uses the symlink option (see next). </p>
<p> symlink: If /etc/resolv.conf is a regular file or does not exist, NetworkManager will write the file directly. If /etc/resolv.conf is instead a symlink, NetworkManager will leave it alone. Unless the symlink points to the internal file /run/NetworkManager/resolv.conf, in which case the symlink will be updated to emit an inotify notification. This allows the user to conveniently instruct NetworkManager not to manage /etc/resolv.conf by replacing it with a symlink. </p>
<p> file: NetworkManager will write /etc/resolv.conf as regular file. If it finds a symlink to an existing target, it will follow the symlink and update the target instead. In no case will an existing symlink be replaced by a file. Note that older versions of NetworkManager behaved differently and would replace dangling symlinks with a plain file. </p>
<p> resolvconf: NetworkManager will run resolvconf to update the DNS configuration. </p>
<p> netconfig: NetworkManager will run netconfig to update the DNS configuration. </p>
<p> unmanaged: don&#8217;t touch /etc/resolv.conf. </p>
<p> none: deprecated alias for symlink.</dl>
<p> <i>systemd-resolved</i></p>
<dl>
<dd>Send the connection DNS configuration to systemd-resolved. Defaults to &quot;true&quot;. </p>
<p> Note that this setting is complementary to the <i>dns</i> setting. You can keep this enabled while using <i>dns</i> set to another DNS plugin alongside systemd-resolved, or <i>dns</i> set to systemd-resolved to configure the system resolver to use systemd-resolved. </p>
<p> If systemd-resolved is enabled, the connectivity check resolves the hostname per-device.</dl>
<p> <i>debug</i></p>
<dl>
<dd>Comma separated list of options to aid debugging. This value will be combined with the environment variable NM_DEBUG. Currently, the following values are supported: </p>
<p> RLIMIT_CORE: set ulimit -c unlimited to write out core dumps. Beware, that a core dump can contain sensitive information such as passwords or configuration settings. </p>
<p> fatal-warnings: set g_log_set_always_fatal() to core dump on warning messages from glib. This is equivalent to the &#8211;g-fatal-warnings command line option.</dl>
<p> <i>autoconnect-retries-default</i></p>
<dl>
<dd>The number of times a connection activation should be automatically tried before switching to another one. This value applies only to connections that can auto-connect and have a connection.autoconnect-retries property set to -1. If not specified, connections will be tried 4 times. Setting this value to 1 means to try activation once, without retry.</dl>
<p> <i>slaves-order</i></p>
<dl>
<dd>This key specifies in which order slave connections are auto-activated on boot or when the master activates them. Allowed values are name (order connection by interface name, the default), or index (order slaves by their kernel index).</dl>
<p> <i>firewall-backend</i></p>
<dl>
<dd>The firewall backend for configuring masquerading with shared mode. Set to either iptables, nftables or none. iptables and nftables require iptables and nft application, respectively. none means to skip firewall configuration if the users wish to manage firewall themselves. If unspecified, it will be auto detected.</dl>
<p> <i>iwd-config-path</i></p>
<dl>
<dd>If the value is &quot;auto&quot; (the default), IWD is queried for its current state directory when it appears on D-Bus &#8212; the directory where IWD keeps its network configuration files &#8212; usually /var/lib/iwd. NetworkManager will then attempt to write copies of new or modified Wi-Fi connection profiles, converted into the IWD format, into this directory thus making IWD connection properties editable. NM will overwrite existing files without preserving their contents. </p>
<p> The path can also be overriden by pointing to a specific existing and writable directory. On the other hand setting this to an empty string or any other value disables the profile conversion mechanism. </p>
<p> This mechanism allows editing connection profile settings such as the 802.1x configuration using NetworkManager clients. Without it such changes have no effect in IWD.</dl>
<h2>Keyfile Section</h2>
<p>This section contains keyfile-plugin-specific options, and is normally only used when you are not using any other distro-specific plugin. </p>
<p> <i>hostname</i></p>
<dl>
<dd>This key is deprecated and has no effect since the hostname is now stored in /etc/hostname or other system configuration files according to build options.</dl>
<p> <i>path</i></p>
<dl>
<dd>The location where keyfiles are read and stored. This defaults to &quot;/etc/NetworkManager/system-connections&quot;.</dl>
<p> <i>unmanaged-devices</i></p>
<dl>
<dd>Set devices that should be ignored by NetworkManager. </p>
<p> A device unmanaged due to this option is strictly unmanaged and cannot be overruled by using the API like <code>nmcli device set $IFNAME managed yes</code>. Also, a device that is unmanaged for other reasons, like an udev rule, cannot be made managed with this option (e.g. by using an except: specifier). These two points make it different from the device*.managed option which for that reason may be a better choice. </p>
<p> See the section called &#8220;Device List Format&#8221; for the syntax on how to specify a device. </p>
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
<dd>The default logging verbosity level. One of OFF, ERR, WARN, INFO, DEBUG, TRACE. The ERR level logs only critical errors. WARN logs warnings that may reflect operation. INFO logs various informational messages that are useful for tracking state and operations. DEBUG enables verbose logging for debugging purposes. TRACE enables even more verbose logging then DEBUG level. Subsequent levels also log all messages from earlier levels; thus setting the log level to INFO also logs error and warning messages.</dl>
<p> <i>domains</i></p>
<dl>
<dd>The following log domains are available: PLATFORM, RFKILL, ETHER, WIFI, BT, MB, DHCP4, DHCP6, PPP, WIFI_SCAN, IP4, IP6, AUTOIP4, DNS, VPN, SHARING, SUPPLICANT, AGENTS, SETTINGS, SUSPEND, CORE, DEVICE, OLPC, WIMAX, INFINIBAND, FIREWALL, ADSL, BOND, VLAN, BRIDGE, DBUS_PROPS, TEAM, CONCHECK, DCB, DISPATCH, AUDIT, SYSTEMD, VPN_PLUGIN, PROXY. </p>
<p> In addition, these special domains can be used: NONE, ALL, DEFAULT, DHCP, IP. </p>
<p> You can specify per-domain log level overrides by adding a colon and a log level to any domain. E.g., &quot;WIFI:DEBUG,WIFI_SCAN:OFF&quot;.</dl>
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
<dd>AUTOIP4 : AutoIP operations</dl>
<dl>
<dd>DNS : Domain Name System related operations</dl>
<dl>
<dd>VPN : Virtual Private Network connections and operations</dl>
<dl>
<dd>SHARING : Connection sharing. With TRACE level log queries for dnsmasq instance</dl>
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
<dd>AUDIT : Audit records</dl>
<dl>
<dd>SYSTEMD : Messages from internal libsystemd</dl>
<dl>
<dd>VPN_PLUGIN : logging messages from VPN plugins</dl>
<dl>
<dd>PROXY : logging messages for proxy handling</dl>
<dl>
<dd>&nbsp;</dl>
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
<dd>&nbsp;</dl>
<dl>
<dd>HW : deprecated alias for &quot;PLATFORM&quot;</dl>
<p> In general, the logfile should not contain passwords or private data. However, you are always advised to check the file before posting it online or attaching to a bug report. VPN_PLUGIN is special as it might reveal private information of the VPN plugins with verbose levels. Therefore this domain will be excluded when setting ALL or DEFAULT to more verbose levels then INFO.</dl>
<p> <i>backend</i></p>
<dl>
<dd>The logging backend. Supported values are &quot;syslog&quot; and &quot;journal&quot;. When NetworkManager is started with &quot;&#8211;debug&quot; in addition all messages will be printed to stderr. If unspecified, the default is &quot;journal&quot;.</dl>
<p> <i>audit</i></p>
<dl>
<dd>Whether the audit records are delivered to auditd, the audit daemon. If false, audit records will be sent only to the NetworkManager logging system. If set to true, they will be also sent to auditd. The default value is true.</dl>
<h2>Connection Section</h2>
<p>Specify default values for connections. </p>
<p> Such default values are only consulted if the corresponding per-connection property explicitly allows for that. That means, all these properties correspond to a property of the connection profile (for example connection.mud-url). Only if the per-profile property is set to a special value that indicates to use the default, the default value from NetworkManager.conf is consulted. It depends on the property, which is the special value that indicates fallback to the default, but it usually is something like empty, unset values or special numeric values like 0 or -1. That means the effectively used value can first always be configured for each profile, and these default values only matter if the per-profile values explicitly indicates to use the default from NetworkManager.conf. </p>
<p> Example: </p>
<dl>
<dd>
<pre>[connection]
ipv6.ip6-privacy=0</pre>
</dl>
<h3>Supported Properties</h3>
<p>Not all properties can be overwritten, only the following properties are supported to have their default values configured (see <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for details). </p>
<p> <i>802-1x.auth-timeout</i></p>
<dl>
<dd></dl>
<p> <i>cdma.mtu</i></p>
<dl>
<dd></dl>
<p> <i>connection.auth-retries</i></p>
<dl>
<dd>If left unspecified, the default value is 3 tries before failing the connection.</dl>
<p> <i>connection.autoconnect-slaves</i></p>
<dl>
<dd></dl>
<p> <i>connection.mud-url</i></p>
<dl>
<dd>If unspecified, MUD URL defaults to &quot;none&quot;.</dl>
<p> <i>connection.lldp</i></p>
<dl>
<dd></dl>
<p> <i>connection.llmnr</i></p>
<dl>
<dd>If unspecified, the ultimate default values depends on the DNS plugin. With systemd-resolved the default currently is &quot;yes&quot; (2) and for all other plugins &quot;no&quot; (0).</dl>
<p> <i>connection.mdns</i></p>
<dl>
<dd>If unspecified, the ultimate default values depends on the DNS plugin. With systemd-resolved the default currently is &quot;no&quot; (0) and for all other plugins also &quot;no&quot; (0).</dl>
<p> <i>connection.dns-over-tls</i></p>
<dl>
<dd>If unspecified, the ultimate default values depends on the DNS plugin. With systemd-resolved the default currently is global setting and for all other plugins &quot;no&quot; (0).</dl>
<p> <i>connection.stable-id</i></p>
<dl>
<dd></dl>
<p> <i>ethernet.cloned-mac-address</i></p>
<dl>
<dd>If left unspecified, it defaults to &quot;preserve&quot;.</dl>
<p> <i>ethernet.generate-mac-address-mask</i></p>
<dl>
<dd></dl>
<p> <i>ethernet.mtu</i></p>
<dl>
<dd>If configured explicitly to 0, the MTU is not reconfigured during device activation unless it is required due to IPv6 constraints. If left unspecified, a DHCP/IPv6 SLAAC provided value is used or the MTU is not reconfigured during activation.</dl>
<p> <i>ethernet.wake-on-lan</i></p>
<dl>
<dd></dl>
<p> <i>gsm.mtu</i></p>
<dl>
<dd></dl>
<p> <i>hostname.from-dhcp</i></p>
<dl>
<dd></dl>
<p> <i>hostname.from-dns-lookup</i></p>
<dl>
<dd></dl>
<p> <i>hostname.only-from-default</i></p>
<dl>
<dd></dl>
<p> <i>hostname.priority</i></p>
<dl>
<dd></dl>
<p> <i>infiniband.mtu</i></p>
<dl>
<dd>If configured explicitly to 0, the MTU is not reconfigured during device activation unless it is required due to IPv6 constraints. If left unspecified, a DHCP/IPv6 SLAAC provided value is used or the MTU is left unspecified on activation.</dl>
<p> <i>ip-tunnel.mtu</i></p>
<dl>
<dd>If configured explicitly to 0, the MTU is not reconfigured during device activation unless it is required due to IPv6 constraints. If left unspecified, a DHCP/IPv6 SLAAC provided value is used or a default of 1500.</dl>
<p> <i>ipv4.dad-timeout</i></p>
<dl>
<dd></dl>
<p> <i>ipv4.dhcp-client-id</i></p>
<dl>
<dd></dl>
<p> <i>ipv4.dhcp-iaid</i></p>
<dl>
<dd>If left unspecified, it defaults to &quot;ifname&quot;.</dl>
<p> <i>ipv4.dhcp-hostname-flags</i></p>
<dl>
<dd>If left unspecified, the value 3 (fqdn-encoded,fqdn-serv-update) is used.</dl>
<p> <i>ipv4.dhcp-timeout</i></p>
<dl>
<dd>If left unspecified, the default value for the interface type is used.</dl>
<p> <i>ipv4.dhcp-vendor-class-identifier</i></p>
<dl>
<dd>If left unspecified, the default is to not send the DHCP option to the server.</dl>
<p> <i>ipv4.dns-priority</i></p>
<dl>
<dd>If unspecified or zero, use 50 for VPN profiles and 100 for other profiles.</dl>
<p> <i>ipv4.required-timeout</i></p>
<dl>
<dd></dl>
<p> <i>ipv4.route-metric</i></p>
<dl>
<dd></dl>
<p> <i>ipv4.route-table</i></p>
<dl>
<dd>If left unspecified, routes are only added to the main table. Note that this is different from explicitly selecting the main table 254, because of how NetworkManager removes extraneous routes from the tables.</dl>
<p> <i>ipv6.ra-timeout</i></p>
<dl>
<dd>If left unspecified, the default value depends on the sysctl solicitation settings.</dl>
<p> <i>ipv6.dhcp-duid</i></p>
<dl>
<dd>If left unspecified, it defaults to &quot;lease&quot;.</dl>
<p> <i>ipv6.dhcp-iaid</i></p>
<dl>
<dd>If left unspecified, it defaults to &quot;ifname&quot;.</dl>
<p> <i>ipv6.dhcp-hostname-flags</i></p>
<dl>
<dd>If left unspecified, the value 1 (fqdn-serv-update) is used.</dl>
<p> <i>ipv6.dhcp-timeout</i></p>
<dl>
<dd>If left unspecified, the default value for the interface type is used.</dl>
<p> <i>ipv6.dns-priority</i></p>
<dl>
<dd>If unspecified or zero, use 50 for VPN profiles and 100 for other profiles.</dl>
<p> <i>ipv6.ip6-privacy</i></p>
<dl>
<dd>If ipv6.ip6-privacy is unset, use the content of &quot;/proc/sys/net/ipv6/conf/default/use_tempaddr&quot; as last fallback.</dl>
<p> <i>ipv6.required-timeout</i></p>
<dl>
<dd></dl>
<p> <i>ipv6.route-metric</i></p>
<dl>
<dd></dl>
<p> <i>ipv6.route-table</i></p>
<dl>
<dd>If left unspecified, routes are only added to the main table. Note that this is different from explicitly selecting the main table 254, because of how NetworkManager removes extraneous routes from the tables.</dl>
<p> <i>sriov.autoprobe-drivers</i></p>
<dl>
<dd>If left unspecified, drivers are autoprobed when the SR-IOV VF gets created.</dl>
<p> <i>vpn.timeout</i></p>
<dl>
<dd>If left unspecified, default value of 60 seconds is used.</dl>
<p> <i>wifi.ap-isolation</i></p>
<dl>
<dd>If left unspecified, AP isolation is disabled.</dl>
<p> <i>wifi.cloned-mac-address</i></p>
<dl>
<dd>If left unspecified, it defaults to &quot;preserve&quot;.</dl>
<p> <i>wifi.generate-mac-address-mask</i></p>
<dl>
<dd></dl>
<p> <i>wifi.mac-address-randomization</i></p>
<dl>
<dd>If left unspecified, MAC address randomization is disabled. This setting is deprecated for wifi.cloned-mac-address.</dl>
<p> <i>wifi.mtu</i></p>
<dl>
<dd>If configured explicitly to 0, the MTU is not reconfigured during device activation unless it is required due to IPv6 constraints. If left unspecified, a DHCP/IPv6 SLAAC provided value is used or a default of 1500.</dl>
<p> <i>wifi.powersave</i></p>
<dl>
<dd>If left unspecified, the default value &quot;ignore&quot; will be used.</dl>
<p> <i>wifi-sec.pmf</i></p>
<dl>
<dd>If left unspecified, the default value &quot;optional&quot; will be used.</dl>
<p> <i>wifi-sec.fils</i></p>
<dl>
<dd>If left unspecified, the default value &quot;optional&quot; will be used.</dl>
<p> <i>wifi.wake-on-wlan</i></p>
<dl>
<dd></dl>
<p> <i>wireguard.mtu</i></p>
<dl>
<dd></dl>
<h3>Sections</h3>
<p>You can configure multiple connection sections, by having different sections with a name that all start with &quot;connection&quot;. Example: </p>
<dl>
<dd>
<pre>[connection]
ipv6.ip6-privacy=0
connection.autoconnect-slaves=1
vpn.timeout=120
[connection-wifi-wlan0]
match-device=interface-name:wlan0
ipv4.route-metric=50
[connection-wifi-other]
match-device=type:wifi
ipv4.route-metric=55
ipv6.ip6-privacy=1</pre>
</dl>
<p> The sections within one file are considered in order of appearance, with the exception that the [connection] section is always considered last. In the example above, this order is [connection-wifi-wlan0], [connection-wlan-other], and [connection]. When checking for a default configuration value, the sections are searched until the requested value is found. In the example above, &quot;ipv4.route-metric&quot; for wlan0 interface is set to 50, and for all other Wi-Fi typed interfaces to 55. Also, Wi-Fi devices would have IPv6 private addresses enabled by default, but other devices would have it disabled. Note that also &quot;wlan0&quot; gets &quot;ipv6.ip6-privacy=1&quot;, because although the section &quot;[connection-wifi-wlan0]&quot; matches the device, it does not contain that property and the search continues. </p>
<p> When having different sections in multiple files, sections from files that are read later have higher priority. So within one file the priority of the sections is top-to-bottom. Across multiple files later definitions take precedence. </p>
<p> The following properties further control how a connection section applies. </p>
<p> <i>match-device</i></p>
<dl>
<dd>An optional device spec that restricts when the section applies. See the section called &#8220;Device List Format&#8221; for the possible values.</dl>
<p> <i>stop-match</i></p>
<dl>
<dd>An optional boolean value which defaults to no. If the section matches (based on match-device), further sections will not be considered even if the property in question is not present. In the example above, if [connection-wifi-wlan0] would have stop-match set to yes, the device wlan0 would have ipv6.ip6-privacy property unspecified. That is, the search for the property would not continue in the connection sections [connection-wifi-other] or [connection].</dl>
<h2>Device Section</h2>
<p>Contains per-device persistent configuration. </p>
<p> Example: </p>
<dl>
<dd>
<pre>[device]
match-device=interface-name:eth3
managed=1</pre>
</dl>
<h3>Supported Properties</h3>
<p>The following properties can be configured per-device. </p>
<p> <i>managed</i></p>
<dl>
<dd>Whether the device is managed or not. A device can be marked as managed via udev rules (ENV{NM_UNMANAGED}), or via setting plugins (keyfile.unmanaged-devices). This is yet another way. Note that this configuration can be overruled at runtime via D-Bus. Also, it has higher priority then udev rules.</dl>
<p> <i>carrier-wait-timeout</i></p>
<dl>
<dd>Specify the timeout for waiting for carrier in milliseconds. The default is 5000 milliseconds. This setting exists because certain drivers/hardware can take a long time to detect whether the cable is plugged in. </p>
<p> When the device loses carrier, NetworkManager does not react immediately. Instead, it waits for this timeout before considering the link lost. </p>
<p> Also, on startup, NetworkManager considers the device as busy for this time, as long as the device has no carrier. This delays startup-complete signal and NetworkManager-wait-online. Configuring this too high means to block NetworkManager-wait-online longer than necessary when booting with cable unplugged. Configuring it too low, means that NetworkManager will declare startup-complete too soon, although carrier is about to come and auto-activation to kick in. Note that if a profile only has static IP configuration or Layer 3 configuration disabled, then it can already autoconnect without carrier on the device. Once such a profile reaches full activated state, startup-complete is considered as reached even if the device has no carrier yet.</dl>
<p> <i>ignore-carrier</i></p>
<dl>
<dd>Specify devices for which NetworkManager will (partially) ignore the carrier state. Normally, for device types that support carrier-detect, such as Ethernet and InfiniBand, NetworkManager will only allow a connection to be activated on the device if carrier is present (ie, a cable is plugged in), and it will deactivate the device if carrier drops for more than a few seconds. </p>
<p> A device with carrier ignored will allow activating connections on that device even when it does not have carrier, provided that the connection uses only statically-configured IP addresses. Additionally, it will allow any active connection (whether static or dynamic) to remain active on the device when carrier is lost. </p>
<p> Note that the &quot;carrier&quot; property of NMDevices and device D-Bus interfaces will still reflect the actual device state; it&#8217;s just that NetworkManager will not make use of that information. </p>
<p> Master types like bond, bridge and team ignore carrier by default, while other device types react on carrier changes by default. </p>
<p> This setting overwrites the deprecated main.ignore-carrier setting above.</dl>
<p> <i>keep-configuration</i></p>
<dl>
<dd>On startup, NetworkManager tries to not interfere with interfaces that are already configured. It does so by generating a in-memory connection based on the interface current configuration. </p>
<p> If this generated connection matches one of the existing persistent connections, the persistent connection gets activated. If there is no match, the generated connection gets activated as &quot;external&quot;, which means that the connection is considered as active, but NetworkManager doesn&#8217;t actually touch the interface. </p>
<p> It is possible to disable this behavior by setting keep-configuration to no. In this way, on startup NetworkManager always tries to activate the most suitable persistent connection (the one with highest autoconnect-priority or, in case of a tie, the one activated most recently). </p>
<p> Note that when NetworkManager gets restarted, it stores the previous state in /run/NetworkManager; in particular it saves the UUID of the connection that was previously active so that it can be activated again after the restart. Therefore, keep-configuration does not have any effect on service restart.</dl>
<p> <i>allowed-connections</i></p>
<dl>
<dd>A list of connections that can be activated on the device. See the section called &#8220;Connection List Format&#8221; for the syntax to specify a connection. If this option is not specified, all connections can be potentially activated on the device, provided that the connection type and other settings match. </p>
<p> A notable use case for this is to filter which connections can be activated based on how they were created; see the origin keyword in the section called &#8220;Connection List Format&#8221;.</dl>
<p> <i>wifi.scan-rand-mac-address</i></p>
<dl>
<dd>Configures MAC address randomization of a Wi-Fi device during scanning. This defaults to yes in which case a random, locally-administered MAC address will be used. The setting wifi.scan-generate-mac-address-mask allows to influence the generated MAC address to use certain vendor OUIs. If disabled, the MAC address during scanning is left unchanged to whatever is configured. For the configured MAC address while the device is associated, see instead the per-connection setting wifi.cloned-mac-address.</dl>
<p> <i>wifi.backend</i></p>
<dl>
<dd>Specify the Wi-Fi backend used for the device. Currently, supported are wpa_supplicant and iwd (experimental). If unspecified, the default is &quot;wpa_supplicant&quot;.</dl>
<p> <i>wifi.scan-generate-mac-address-mask</i></p>
<dl>
<dd>Like the per-connection settings ethernet.generate-mac-address-mask and wifi.generate-mac-address-mask, this allows to configure the generated MAC addresses during scanning. See <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for details.</dl>
<p> <i>wifi.iwd.autoconnect</i></p>
<dl>
<dd>If wifi.backend is iwd, setting this to false forces IWD&#8217;s autoconnect mechanism to be disabled for this device and connections will only be initiated by NetworkManager whether commanded by a client or automatically. Leaving it true (default) stops NetworkManager from automatically initiating connections and allows IWD to use its network ranking and scanning logic to decide the best networks to autoconnect to next. Connections&#8217; autoconnect-priority, autoconnect-retries settings will be ignored. Other settings like permissions or multi-connect may interfere with IWD connection attempts.</dl>
<p> <i>sriov-num-vfs</i></p>
<dl>
<dd>Specify the number of virtual functions (VF) to enable for a PCI physical device that supports single-root I/O virtualization (SR-IOV).</dl>
<h3>Sections</h3>
<p>The [device] section works the same as the [connection] section. That is, multiple sections that all start with the prefix &quot;device&quot; can be specified. The settings &quot;match-device&quot; and &quot;stop-match&quot; are available to match a device section on a device. The order of multiple sections is also top-down within the file and later files overwrite previous settings. See &#8220;Sections&#8221; under the section called &#8220;CONNECTION SECTION&#8221; for details.</p>
<h2>Connectivity Section</h2>
<p>This section controls NetworkManager&#8217;s optional connectivity checking functionality. This allows NetworkManager to detect whether or not the system can actually access the internet or whether it is behind a captive portal. </p>
<p> Connectivity checking serves two purposes. For one, it exposes a connectivity state on D-Bus, which other applications may use. For example, Gnome&#8217;s portal helper uses this as signal to show a captive portal login page. The other use is that default-route of devices without global connectivity get a penalty of +20000 to the route-metric. This has the purpose to give a better default-route to devices that have global connectivity. For example, when being connected to WWAN and to a Wi-Fi network which is behind a captive portal, WWAN still gets preferred until login. </p>
<p> Note that your distribution might set /proc/sys/net/ipv4/conf/*/rp_filter to strict filtering. That works badly with per-device connectivity checking, which uses SO_BINDDEVICE to send requests on all devices. A strict rp_filter setting will reject any response and the connectivity check on all but the best route will fail. </p>
<p> <i>enabled</i></p>
<dl>
<dd>Whether connectivity check is enabled. Note that to enable connectivity check, a valid uri must also be configured. The value defaults to true, but since the uri is unset by default, connectivity check may be disabled. The main purpose of this option is to have a single flag to disable connectivity check. Note that this setting can also be set via D-Bus API at runtime. In that case, the value gets stored in /var/lib/NetworkManager/NetworkManager-intern.conf file.</dl>
<p> <i>uri</i></p>
<dl>
<dd>The URI of a web page to periodically request when connectivity is being checked. This page should return the header &quot;X-NetworkManager-Status&quot; with a value of &quot;online&quot;. Alternatively, its body content should be set to &quot;NetworkManager is online&quot;. The body content check can be controlled by the response option. If this option is blank or missing, connectivity checking is disabled.</dl>
<p> <i>interval</i></p>
<dl>
<dd>Specified in seconds; controls how often connectivity is checked when a network connection exists. If set to 0 connectivity checking is disabled. If missing, the default is 300 seconds.</dl>
<p> <i>response</i></p>
<dl>
<dd>If set, controls what body content NetworkManager checks for when requesting the URI for connectivity checking. Note that this only compares that the HTTP response starts with the specifid text, it does not compare the exact string. This behavior might change in the future, so avoid relying on it. If missing, the response defaults to &quot;NetworkManager is online&quot;. If set to empty, the HTTP server is expected to answer with status code 204 or send no data.</dl>
<h2>Global-Dns Section</h2>
<p>This section specifies global DNS settings that override connection-specific configuration. </p>
<p> <i>searches</i></p>
<dl>
<dd>A list of search domains to be used during hostname lookup.</dl>
<p> <i>options</i></p>
<dl>
<dd>A list of options to be passed to the hostname resolver.</dl>
<h2>Global-Dns-Domain Sections</h2>
<p>Sections with a name starting with the &quot;global-dns-domain-&quot; prefix allow to define global DNS configuration for specific domains. The part of section name after &quot;global-dns-domain-&quot; specifies the domain name a section applies to. More specific domains have the precedence over less specific ones and the default domain is represented by the wildcard &quot;*&quot;. A default domain section is mandatory. </p>
<p> <i>servers</i></p>
<dl>
<dd>A list of addresses of DNS servers to be used for the given domain.</dl>
<p> <i>options</i></p>
<dl>
<dd>A list of domain-specific DNS options. Not used at the moment.</dl>
<h2>.Config Sections</h2>
<p>This is a special section that contains options which apply to the configuration file that contains the option. </p>
<p> <i>enable</i></p>
<dl>
<dd>Defaults to &quot;true&quot;. If &quot;false&quot;, the configuration file will be skipped during loading. Note that the main configuration file NetworkManager.conf cannot be disabled. </p>
<dl>
<dd>
<pre># always skip loading the config file
[.config]
enable=false</pre>
</dl>
<p> You can also match against the version of NetworkManager. For example the following are valid configurations: </p>
<dl>
<dd>
<pre># only load on version 1.0.6
[.config]
enable=nm-version:1.0.6
# load on all versions 1.0.x, but not 1.2.x
[.config]
enable=nm-version:1.0
# only load on versions &gt;= 1.1.6. This does not match
# with version 1.2.0 or 1.4.4. Only the last digit is considered.
[.config]
enable=nm-version-min:1.1.6
# only load on versions &gt;= 1.2. Contrary to the previous
# example, this also matches with 1.2.0, 1.2.10, 1.4.4, etc.
[.config]
enable=nm-version-min:1.2
# Match against the maximum allowed version. The example matches
# versions 1.2.0, 1.2.2, 1.2.4. Again, only the last version digit
# is allowed to be smaller. So this would not match on 1.1.10.
[.config]
enable=nm-version-max:1.2.6</pre>
</dl>
<p> You can also match against the value of the environment variable NM_CONFIG_ENABLE_TAG, like: </p>
<dl>
<dd>
<pre># always skip loading the file when running NetworkManager with
# environment variable &quot;NM_CONFIG_ENABLE_TAG=TAG1&quot;
[.config]
enable=env:TAG1</pre>
</dl>
<p> More then one match can be specified. The configuration will be enabled if one of the predicates matches (&quot;or&quot;). The special prefix &quot;except:&quot; can be used to negate the match. Note that if one except-predicate matches, the entire configuration will be disabled. In other words, a except predicate always wins over other predicates. If the setting only consists of &quot;except:&quot; matches and none of the negative conditions are satisfied, the configuration is still enabled. </p>
<dl>
<dd>
<pre># enable the configuration either when the environment variable
# is present or the version is at least 1.2.0.
[.config]
enable=env:TAG2,nm-version-min:1.2
# enable the configuration for version &gt;= 1.2.0, but disable
# it when the environment variable is set to &quot;TAG3&quot;
[.config]
enable=except:env:TAG3,nm-version-min:1.2
# enable the configuration on &gt;= 1.3, &gt;= 1.2.6, and &gt;= 1.0.16.
# Useful if a certain feature is only present since those releases.
[.config]
enable=nm-version-min:1.3,nm-version-min:1.2.6,nm-version-min:1.0.16</pre>
</dl>
</dl>
<h2>Plugins</h2>
<p>Settings plugins for reading and writing connection profiles. The number of available plugins is distribution specific. </p>
<p> <i>keyfile</i></p>
<dl>
<dd>The keyfile plugin is the generic plugin that supports all the connection types and capabilities that NetworkManager has. It writes files out in an .ini-style format in /etc/NetworkManager/system-connections. See <code><a href="/docs/linux/man/5-nm-settings-keyfile/">nm-settings-keyfile</a></code>(5) for details about the file format. </p>
<p> The stored connection file may contain passwords, secrets and private keys in plain text, so it will be made readable only to root, and the plugin will ignore files that are readable or writable by any user or group other than root. See &quot;Secret flag types&quot; in <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5) for how to avoid storing passwords in plain text. </p>
<p> This plugin is always active, and will automatically be used to store any connections that aren&#8217;t supported by any other active plugin.</dl>
<p> <i>ifcfg-rh</i></p>
<dl>
<dd>This plugin is used on the Fedora and Red Hat Enterprise Linux distributions to read and write configuration from the standard /etc/sysconfig/network-scripts/ifcfg-* files. It currently supports reading Ethernet, Wi-Fi, InfiniBand, VLAN, Bond, Bridge, and Team connections. Enabling ifcfg-rh implicitly enables ibft plugin, if it is available. This can be disabled by adding no-ibft. See /usr/share/doc/initscripts/sysconfig.txt and <code><a href="/docs/linux/man/5-nm-settings-ifcfg-rh/">nm-settings-ifcfg-rh</a></code>(5) for more information about the ifcfg file format.</dl>
<p> <i>ifupdown</i></p>
<dl>
<dd>This plugin is used on the Debian and Ubuntu distributions, and reads Ethernet and Wi-Fi connections from /etc/network/interfaces. </p>
<p> This plugin is read-only; any connections (of any type) added from within NetworkManager when you are using this plugin will be saved using the keyfile plugin instead.</dl>
<p> <i>ibft</i>, <i>no-ibft</i></p>
<dl>
<dd>These plugins are deprecated and their selection has no effect. This is now handled by nm-initrd-generator.</dl>
<p> <i>ifcfg-suse</i>, <i>ifnet</i></p>
<dl>
<dd>These plugins are deprecated and their selection has no effect. The keyfile plugin should be used instead.</dl>
<h2>Appendix</h2>
<h3>Device List Format</h3>
<p>The configuration options main.no-auto-default, main.ignore-carrier, keyfile.unmanaged-devices, connection*.match-device and device*.match-device select devices based on a list of matchings. Devices can be specified using the following format: </p>
<p> *</p>
<dl>
<dd>Matches every device.</dl>
<p> IFNAME</p>
<dl>
<dd>Case sensitive match of interface name of the device. Globbing is not supported.</dl>
<p> HWADDR</p>
<dl>
<dd>Match the permanent MAC address of the device. Globbing is not supported</dl>
<p> interface-name:IFNAME, interface-name:~IFNAME</p>
<dl>
<dd>Case sensitive match of interface name of the device. Simple globbing is supported with * and ?. Ranges and escaping is not supported.</dl>
<p> interface-name:=IFNAME</p>
<dl>
<dd>Case sensitive match of interface name of the device. Globbing is disabled and IFNAME is taken literally.</dl>
<p> mac:HWADDR</p>
<dl>
<dd>Match the permanent MAC address of the device. Globbing is not supported</dl>
<p> s390-subchannels:HWADDR</p>
<dl>
<dd>Match the device based on the subchannel address. Globbing is not supported</dl>
<p> type:TYPE</p>
<dl>
<dd>Match the device type. Valid type names are as reported by &quot;nmcli -f GENERAL.TYPE device show&quot;. Globbing is not supported.</dl>
<p> driver:DRIVER</p>
<dl>
<dd>Match the device driver as reported by &quot;nmcli -f GENERAL.DRIVER,GENERAL.DRIVER-VERSION device show&quot;. &quot;DRIVER&quot; must match the driver name exactly and does not support globbing. Optionally, a driver version may be specified separated by &#8216;/&#8217;. Globbing is supported for the version.</dl>
<p> dhcp-plugin:DHCP</p>
<dl>
<dd>Match the configured DHCP plugin &quot;main.dhcp&quot;.</dl>
<p> except:SPEC</p>
<dl>
<dd>Negative match of a device. SPEC must be explicitly qualified with a prefix such as interface-name:. A negative match has higher priority then the positive matches above. </p>
<p> If there is a list consisting only of negative matches, the behavior is the same as if there is also match-all. That means, if none of all the negative matches is satisfied, the overall result is still a positive match. That means, &quot;except:interface-name:eth0&quot; is the same as &quot;*,except:interface-name:eth0&quot;.</dl>
<p> SPEC[,;]SPEC</p>
<dl>
<dd>Multiple specs can be concatenated with commas or semicolons. The order does not matter as matches are either inclusive or negative (except:), with negative matches having higher priority. </p>
<p> Backslash is supported to escape the separators &#8216;;&#8217; and &#8216;,&#8217;, and to express special characters such as newline (&#8216;
&#8217;), tabulator (&#8216;	&#8217;), whitespace (&#8216;\s&#8217;) and backslash (&#8216;\&#8217;). The globbing of interface names cannot be escaped. Whitespace is not a separator but will be trimmed between two specs (unless escaped as &#8216;\s&#8217;).</dl>
<p> Example: </p>
<dl>
<dd>
<pre>interface-name:em4
mac:00:22:68:1c:59:b1;mac:00:1E:65:30:D1:C4;interface-name:eth2
interface-name:vboxnet*,except:interface-name:vboxnet2
*,except:mac:00:22:68:1c:59:b1</pre>
</dl>
<h3>Connection List Format</h3>
<p>Connections can be specified using the following format: </p>
<p> *</p>
<dl>
<dd>Matches every connection.</dl>
<p> uuid:UUID</p>
<dl>
<dd>Match the connection by UUID, for example &quot;uuid:83037490-1d17-4986-a397-01f1db3a7fc2&quot;</dl>
<p> id=ID</p>
<dl>
<dd>Match the connection by name.</dl>
<p> origin:ORIGIN</p>
<dl>
<dd>Match the connection by origin, stored in the org.freedesktop.NetworkManager.origin tag of the user setting. For example, use &quot;except:origin:nm-initrd-generator&quot; to forbid activation of connections created by the initrd generator.</dl>
<p> except:SPEC</p>
<dl>
<dd>Negative match of a connection. A negative match has higher priority then the positive matches above. </p>
<p> If there is a list consisting only of negative matches, the behavior is the same as if there is also match-all. That means, if none of all the negative matches is satisfied, the overall result is still a positive match.</dl>
<p> SPEC[,;]SPEC</p>
<dl>
<dd>Multiple specs can be concatenated with commas or semicolons. The order does not matter as matches are either inclusive or negative (except:), with negative matches having higher priority. </p>
<p> Backslash is supported to escape the separators &#8216;;&#8217; and &#8216;,&#8217;, and to express special characters such as newline (&#8216;
&#8217;), tabulator (&#8216;	&#8217;), whitespace (&#8216;\s&#8217;) and backslash (&#8216;\&#8217;). Whitespace is not a separator but will be trimmed between two specs (unless escaped as &#8216;\s&#8217;).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/1-nmcli/">nmcli</a></code>(1), <code><a href="/docs/linux/man/7-nmcli-examples/">nmcli-examples</a></code>(7), <code><a href="/docs/linux/man/1-nm-online/">nm-online</a></code>(1), <code><a href="/docs/linux/man/5-nm-settings/">nm-settings</a></code>(5), <code><a href="/docs/linux/man/1-nm-applet/">nm-applet</a></code>(1), <code><a href="/docs/linux/man/1-nm-connection-editor/">nm-connection-editor</a></code>(1) </p>
