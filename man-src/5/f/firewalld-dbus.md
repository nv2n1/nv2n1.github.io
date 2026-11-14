---
title: "firewalld-dbus(5)"
name: "firewalld-dbus"
section: "5"
letter: "f"
url: "/docs/linux/man/5-firewalld-dbus/"
description: "firewalld.dbus – firewalld D-Bus interface description"
---

<p>firewalld.dbus &#8211; firewalld D-Bus interface description</p>
<h2>Object Paths</h2>
<p>This is the basic firewalld object path structure. The used interfaces are explained below in the section called &#8220;INTERFACES&#8221;. </p>
<dl>
<dd>
<pre>/org/fedoraproject/FirewallD1
 Interfaces
 org.fedoraproject.FirewallD1
 org.fedoraproject.FirewallD1.direct
 org.fedoraproject.FirewallD1.ipset
 org.fedoraproject.FirewallD1.policies
 org.fedoraproject.FirewallD1.zone
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties
/org/fedoraproject/FirewallD1/config
 Interfaces
 org.fedoraproject.FirewallD1.config
 org.fedoraproject.FirewallD1.config.direct
 org.fedoraproject.FirewallD1.config.policies
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties
/org/fedoraproject/FirewallD1/config/zone/i
 Interfaces
 org.fedoraproject.FirewallD1.config.zone
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties
/org/fedoraproject/FirewallD1/config/service/i
 Interfaces:
 org.fedoraproject.FirewallD1.config.service
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties
/org/fedoraproject/FirewallD1/config/ipset/i
 Interfaces
 org.fedoraproject.FirewallD1.config.ipset
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties
/org/fedoraproject/FirewallD1/config/icmptype/i
 Interfaces
 org.fedoraproject.FirewallD1.config.icmptype
 org.freedesktop.DBus.Introspectable
 org.freedesktop.DBus.Properties</pre>
</dl>
<h2>Interfaces</h2>
<h3>org.fedoraproject.FirewallD1</h3>
<p>This interface contains general runtime operations, like: reloading, panic mode, default zone handling, getting services and icmp types and their settings. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>authorizeAll() → Nothing</p>
<dl>
<dd>Initiate authorization for the complete firewalld D-Bus interface. This method it mostly useful for configuration applications.</dl>
<p> completeReload() → Nothing</p>
<dl>
<dd>Reload firewall completely, even netfilter kernel modules. This will most likely terminate active connections, because state information is lost. This option should only be used in case of severe firewall problems. For example if there are state information problems that no connection can be established with correct firewall rules.</dl>
<p> disablePanicMode() → Nothing</p>
<dl>
<dd>Disable panic mode. After disabling panic mode established connections might work again, if panic mode was enabled for a short period of time. </p>
<p> Possible errors: NOT_ENABLED, COMMAND_FAILED</dl>
<p> enablePanicMode() → Nothing</p>
<dl>
<dd>Enable panic mode. All incoming and outgoing packets are dropped, active connections will expire. Enable this only if there are serious problems with your network environment. </p>
<p> Possible errors: ALREADY_ENABLED, COMMAND_FAILED</dl>
<p> getAutomaticHelpers() → s</p>
<dl>
<dd>Return the AutomaticHelpers value. For the secure use of iptables and connection tracking helpers it is recommended to turn AutomaticHelpers off. But this might have side effects on other services using the netfilter helpers as the sysctl setting in <i>/proc/sys/net/netfilter/nf_conntrack_helper</i> will be changed. With the system setting, the default value set in the kernel or with sysctl will be used. Possible values are: <i>yes</i>, <i>no</i> and <i>system</i>. The default value is <i>system</i>.</dl>
<p> getDefaultZone() → s</p>
<dl>
<dd>Return default zone.</dl>
<p> getHelperSettings(s: <i>helper</i>) → (sssssa(ss))</p>
<dl>
<dd>Return runtime settings of given <i>helper</i>. For getting permanent settings see org.fedoraproject.FirewallD1.config.helper.Methods.getSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>family</i>, <i>module</i> and array of <i>ports</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>helper</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>family (s)</i>: see <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module (s)</i>: see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_HELPER</dl>
<p> getHelpers() → as</p>
<dl>
<dd>Return array of helper names (s) in runtime configuration. For permanent configuration see org.fedoraproject.FirewallD1.config.Methods.listHelpers.</dl>
<p> getIcmpTypeSettings(s: <i>icmptype</i>) → (sssas)</p>
<dl>
<dd>Return runtime settings of given <i>icmptype</i>. For getting permanent settings see org.fedoraproject.FirewallD1.config.icmptype.Methods.getSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>destinations</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (as)</i>: array, either empty or containing strings &#8216;ipv4&#8217; or &#8216;ipv6&#8217;, see <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_ICMPTYPE</dl>
<p> getLogDenied() → s</p>
<dl>
<dd>Retruns the LogDenied value. If LogDenied is enabled, then logging rules are added right before reject and drop rules in the INPUT, FORWARD and OUTPUT chains for the default rules and also final reject and drop rules in zones. Possible values are: <i>all</i>, <i>unicast</i>, <i>broadcast</i>, <i>multicast</i> and <i>off</i>. The default value is <i>off</i></dl>
<p> getServiceSettings(s: <i>service</i>) → (sssa(ss)asa{ss}asa(ss))</p>
<dl>
<dd>Return runtime settings of given <i>service</i>. For getting permanent settings see org.fedoraproject.FirewallD1.config.service.Methods.getSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>ports</i> (port, protocol), array of <i>module names</i>, dictionary of <i>destinations</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module names (as)</i>: array of kernel netfilter helpers, see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (a{ss})</i>: dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols, see <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_SERVICE</dl>
<p> getZoneSettings(s: <i>zone</i>) → (sssbsasa(ss)asba(ssss)asasasasa(ss))</p>
<dl>
<dd>Return runtime settings of given <i>zone</i>. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>UNUSED</i>, <i>target</i>, array of <i>services</i>, array of <i>ports</i> (port, protocol), array of <i>icmp-blocks</i>, <i>masquerade</i>, array of <i>forward-ports</i> (port, protocol, to-port, to-addr), array of <i>interfaces</i>, array of <i>sources</i>, array of <i>rich rules</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>UNUSED (b)</i>: this boolean value is no longer used for anything.</p>
<dl>
<dd></dl>
<p> <i>target (s)</i>: see <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>services (as)</i>: array of service names, see <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>icmp-blocks (as)</i>: array of icmp-blocks. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>masquerade (b)</i>: see <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>forward-ports (a(ssss))</i>: array of (port, protocol, to-port, to-addr). See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>interfaces (as)</i>: array of interfaces. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source addresses (as)</i>: array of source addresses. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>rich rules (as)</i>: array of rich-language rules. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols, see <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_ZONE</dl>
<p> listIcmpTypes() → as</p>
<dl>
<dd>Return array of names (s) of icmp types in runtime configuration. For permanent configuration see org.fedoraproject.FirewallD1.config.Methods.listIcmpTypes.</dl>
<p> listServices() → as</p>
<dl>
<dd>Return array of service names (s) in runtime configuration. For permanent configuration see org.fedoraproject.FirewallD1.config.Methods.listServices.</dl>
<p> queryPanicMode() → b</p>
<dl>
<dd>Return true if panic mode is enabled, false otherwise. In panic mode all incoming and outgoing packets are dropped.</dl>
<p> reload() → Nothing</p>
<dl>
<dd>Reload firewall rules and keep state information. Current permanent configuration will become new runtime configuration, i.e. all runtime only changes done until reload are lost with reload if they have not been also in permanent configuration.</dl>
<p> runtimeToPermanent() → Nothing</p>
<dl>
<dd>Make runtime settings permanent. Replaces permanent settings with runtime settings for zones, services, icmptypes, direct and policies (lockdown whitelist). </p>
<p> Possible errors: RT_TO_PERM_FAILED</dl>
<p> setDefaultZone(s: <i>zone</i>) → Nothing</p>
<dl>
<dd>Set default zone for connections and interfaces where no zone has been selected to <i>zone</i>. Setting the default zone changes the zone for the connections or interfaces, that are using the default zone. This is a runtime and permanent change. </p>
<p> Possible errors: ZONE_ALREADY_SET, COMMAND_FAILED</dl>
<p> setLogDenied(s: <i>value</i>) → Nothing</p>
<dl>
<dd>Set LogDenied value to <i>value</i>. If LogDenied is enabled, then logging rules are added right before reject and drop rules in the INPUT, FORWARD and OUTPUT chains for the default rules and also final reject and drop rules in zones. Possible values are: <i>all</i>, <i>unicast</i>, <i>broadcast</i>, <i>multicast</i> and <i>off</i>. The default value is <i>off</i> This is a runtime and permanent change. </p>
<p> Possible errors: ALREADY_SET, INVALID_VALUE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>DefaultZoneChanged(s: <i>zone</i>)</p>
<dl>
<dd>Emitted when default zone has been changed to <i>zone</i>.</dl>
<p> LogDeniedChanged(s: <i>value</i>)</p>
<dl>
<dd>Emitted when LogDenied value has been changed.</dl>
<p> PanicModeDisabled()</p>
<dl>
<dd>Emitted when panic mode has been deactivated.</dl>
<p> PanicModeEnabled()</p>
<dl>
<dd>Emitted when panic mode has been activated.</dl>
<p> Reloaded()</p>
<dl>
<dd>Emitted when firewalld has been reloaded. Also emitted for a complete reload.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd><i>BRIDGE</i> &#8211; b &#8211; (ro)</p>
<dl>
<dd>Indicates whether the firewall has ethernet bridge support.</dl>
<p> <i>IPSet</i> &#8211; b &#8211; (ro)</p>
<dl>
<dd>Indicates whether the firewall has IPSet support.</dl>
<p> <i>IPSetTypes</i> &#8211; as &#8211; (ro)</p>
<dl>
<dd>The supported IPSet types by ipset and firewalld.</dl>
<p> <i>IPv4</i> &#8211; b &#8211; (ro)</p>
<dl>
<dd>Indicates whether the firewall has IPv4 support.</dl>
<p> <i>IPv4ICMPTypes</i> &#8211; as &#8211; (ro)</p>
<dl>
<dd>The list of supported IPv4 ICMP types.</dl>
<p> <i>IPv6</i> &#8211; b &#8211; (ro)</p>
<dl>
<dd>Indicates whether the firewall has IPv6 support.</dl>
<p> <i>IPv6_rpfilter</i> &#8211; b &#8211; (ro)</p>
<dl>
<dd>Indicates whether the reverse path filter test on a packet for IPv6 is enabled. If a reply to the packet would be sent via the same interface that the packet arrived on, the packet will match and be accepted, otherwise dropped.</dl>
<p> <i>IPv6ICMPTypes</i> &#8211; as &#8211; (ro)</p>
<dl>
<dd>The list of supported IPv6 ICMP types.</dl>
<p> <i>interface_version</i> &#8211; s &#8211; (ro)</p>
<dl>
<dd>firewalld D-Bus interface version string.</dl>
<p> <i>state</i> &#8211; s &#8211; (ro)</p>
<dl>
<dd>firewalld state. This can be either <i>INIT</i> or <i>RUNNING</i>. In <i>INIT</i> state, firewalld is starting up and initializing.</dl>
<p> <i>version</i> &#8211; s &#8211; (ro)</p>
<dl>
<dd>firewalld version string.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.ipset</h3>
<p>Operations in this interface allows to get, add, remove and query runtime ipset settings. For permanent configuration see org.fedoraproject.FirewallD1.config.ipset interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addEntry(s: ipset, s: entry) → as</p>
<dl>
<dd>Add a new <i>entry</i> to <i>ipset</i>. The entry must match the type of the ipset. If the ipset is using the timeout option, it is not possible to see the entries, as they are timing out automatically in the kernel. For permanent operation see org.fedoraproject.FirewallD1.config.ipset.Methods.addEntry. </p>
<p> Possible errors: INVALID_IPSET, IPSET_WITH_TIMEOUT</dl>
<p> getEntries(s: ipset) → Nothing</p>
<dl>
<dd>Get all entries added to the <i>ipset</i>. If the ipset is using the timeout option, it is not possible to see the entries, as they are timing out automatically in the kernel. Return value is a array of <i>entry</i>. For permanent operation see org.fedoraproject.FirewallD1.config.ipset.Methods.getEntries. </p>
<p> Possible errors: INVALID_IPSET, IPSET_WITH_TIMEOUT</dl>
<p> getSettings(s: ipset) → (ssssa{ss}as)</p>
<dl>
<dd>Return runtime settings of given <i>ipset</i>. For getting permanent settings see org.fedoraproject.FirewallD1.config.ipset.Methods.getSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>type</i>, dictionary of <i>options</i> and array of <i>entries</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>type (s)</i>: see <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>options (a{ss})</i>: dictionary of {option : value} . See <i>options</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>entries (as)</i>: array of entries, see <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_IPSET</dl>
<p> getIPSets() → as</p>
<dl>
<dd>Return array of ipset names (s) in runtime configuration. For permanent configuration see org.fedoraproject.FirewallD1.config.Methods.listIPSets.</dl>
<p> queryService(s: ipset, s: entry) → b</p>
<dl>
<dd>Return whether <i>entry</i> has been added to <i>ipset</i>. For permanent operation see org.fedoraproject.FirewallD1.config.ipset.Methods.queryEntry. </p>
<p> Possible errors: INVALID_IPSET</dl>
<p> queryService(s: ipset) → b</p>
<dl>
<dd>Return whether <i>ipset</i> is defined in runtime configuration.</dl>
<p> removeEntry(s: ipset, s: entry) → as</p>
<dl>
<dd>Removes an <i>entry</i> from <i>ipset</i>. For permanent operation see org.fedoraproject.FirewallD1.config.ipset.Methods.removeEntry. </p>
<p> Possible errors: INVALID_IPSET, IPSET_WITH_TIMEOUT</dl>
<p> setEntries(as: entries) → Nothing</p>
<dl>
<dd>Permanently set list of entries to <i>entries</i>. For permanent operation see org.fedoraproject.FirewallD1.config.ipset.Methods.setEntries. See <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>EntryAdded(s: ipset, s: entry)</p>
<dl>
<dd>Emitted when <i>entry</i> has been added to <i>ipset</i>.</dl>
<p> EntryRemoved(s: ipset, s: entry)</p>
<dl>
<dd>Emitted when <i>entry</i> has been removed from <i>ipset</i>.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.direct</h3>
<p>This interface enables more direct access to the firewall. It enables runtime manipulation with chains and rules. For permanent configuration see org.fedoraproject.FirewallD1.config.direct interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addChain(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Add a new <i>chain</i> to <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Make sure there&#8217;s no other chain with this name already. There already exist basic chains to use with direct methods, for example <i>INPUT_direct</i> chain. These chains are jumped into before chains for zones, i.e. every rule put into <i>INPUT_direct</i> will be checked before rules in zones. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.addChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, ALREADY_ENABLED, COMMAND_FAILED</dl>
<p> addPassthrough(s: ipv, as: args) → Nothing</p>
<dl>
<dd>Add a tracked passthrough rule with the arguments <i>args</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Valid commands in args are only <i>-A/&#8211;append</i>, <i>-I/&#8211;insert</i> and <i>-N/&#8211;new-chain</i>. This method is (unlike passthrough method) tracked, i.e. firewalld remembers it. It&#8217;s useful with org.fedoraproject.FirewallD1.Methods.runtimeToPermanent For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.addPassthrough. </p>
<p> Possible errors: INVALID_IPV, ALREADY_ENABLED, COMMAND_FAILED</dl>
<p> addRule(s: ipv, s: table, s: chain, i: priority, as: args) → Nothing</p>
<dl>
<dd>Add a rule with the arguments <i>args</i> to <i>chain</i> in <i>table</i> with <i>priority</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). The priority is used to order rules. Priority 0 means add rule on top of the chain, with a higher priority the rule will be added further down. Rules with the same priority are on the same level and the order of these rules is not fixed and may change. If you want to make sure that a rule will be added after another one, use a low priority for the first and a higher for the following. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.addRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, ALREADY_ENABLED, COMMAND_FAILED</dl>
<p> getAllChains() → a(sss)</p>
<dl>
<dd>Get all chains added to all tables in format: ipv, table, chain. This concerns only chains previously added with addChain. Return value is a array of (<i>ipv</i>, <i>table</i>, <i>chain</i>). For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getAllChains. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>table (s)</i>: one of <i>filter</i>, <i>mangle</i>, <i>nat</i>, <i>raw</i>, <i>security</i></p>
<dl>
<dd></dl>
<p> <i>chain (s)</i>: name of a chain.</p>
<dl>
<dd></dl>
</dl>
<p> getAllPassthroughs() → a(sas)</p>
<dl>
<dd>Get all tracked passthrough rules added in all ipv types in format: ipv, rule. This concerns only rules previously added with addPassthrough. Return value is a array of (<i>ipv</i>, array of <i>arguments</i>). For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getAllPassthroughs. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getAllRules() → a(sssias)</p>
<dl>
<dd>Get all rules added to all chains in all tables in format: ipv, table, chain, priority, rule. This concerns only rules previously added with addRule. Return value is a array of (<i>ipv</i>, <i>table</i>, <i>chain</i>, <i>priority</i>, array of <i>arguments</i>). For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getAllRules. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>table (s)</i>: one of <i>filter</i>, <i>mangle</i>, <i>nat</i>, <i>raw</i>, <i>security</i></p>
<dl>
<dd></dl>
<p> <i>chain (s)</i>: name of a chain.</p>
<dl>
<dd></dl>
<p> <i>priority (i)</i>: used to order rules.</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getChains(s: ipv, s: table) → as</p>
<dl>
<dd>Return an array of chains (s) added to <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only chains previously added with addChain. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getChains. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> getPassthroughs(s: ipv) → aas</p>
<dl>
<dd>Get tracked passthrough rules added in either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addPassthrough. Return value is a array of (array of <i>arguments</i>). For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getPassthroughs. </p>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getRules(s: ipv, s: table, s: chain) → a(ias)</p>
<dl>
<dd>Get all rules added to <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. Return value is a array of (<i>priority</i>, array of <i>arguments</i>). For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.getRules. </p>
<p> <i>priority (i)</i>: used to order rules.</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> passthrough(s: ipv, as: args) → s</p>
<dl>
<dd>Pass a command through to the firewall. <i>ipv</i> can be either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). <i>args</i> can be all <code>iptables</code>, <code>ip6tables</code> and <code>ebtables</code> command line arguments. <i>args</i> can be all iptables, ip6tables and ebtables command line arguments. This command is untracked, which means that firewalld is not able to provide information about this command later on. </p>
<p> Possible errors: COMMAND_FAILED</dl>
<p> queryChain(s: ipv, s: table, s: chain) → b</p>
<dl>
<dd>Return whether a <i>chain</i> exists in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only chains previously added with addChain. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.queryChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> queryPassthrough(s: ipv, as: args) → b</p>
<dl>
<dd>Return whether a tracked passthrough rule with the arguments <i>args</i> exists for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addPassthrough. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.queryPassthrough. </p>
<p> Possible errors: INVALID_IPV</dl>
<p> queryRule(s: ipv, s: table, s: chain, i: priority, as: args) → b</p>
<dl>
<dd>Return whether a rule with <i>priority</i> and the arguments <i>args</i> exists in <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.queryRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> removeAllPassthroughs() → Nothing</p>
<dl>
<dd>Remove all passthrough rules previously added with addPassthrough.</dl>
<p> removeChain(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Remove a <i>chain</i> from <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only chains previously added with addChain can be removed this way. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.removeChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, NOT_ENABLED, COMMAND_FAILED</dl>
<p> removePassthrough(s: ipv, as: args) → Nothing</p>
<dl>
<dd>Remove a tracked passthrough rule with arguments <i>args</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only rules previously added with addPassthrough can be removed this way. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.removePassthrough. </p>
<p> Possible errors: INVALID_IPV, NOT_ENABLED, COMMAND_FAILED</dl>
<p> removeRule(s: ipv, s: table, s: chain, i: priority, as: args) → Nothing</p>
<dl>
<dd>Remove a rule with <i>priority</i> and arguments <i>args</i> from <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only rules previously added with addRule can be removed this way. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.removeRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, NOT_ENABLED, COMMAND_FAILED</dl>
<p> removeRules(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Remove all rules from <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. For permanent operation see org.fedoraproject.FirewallD1.config.direct.Methods.removeRules. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>ChainAdded(s: ipv, s: table, s: chain)</p>
<dl>
<dd>Emitted when <i>chain</i> has been added into <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
<p> ChainRemoved(s: ipv, s: table, s: chain)</p>
<dl>
<dd>Emitted when <i>chain</i> has been removed from <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
<p> PassthroughAdded(s: ipv, as: args)</p>
<dl>
<dd>Emitted when a tracked passthruogh rule with <i>args</i> has been added for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
<p> PassthroughRemoved(s: ipv, as: args)</p>
<dl>
<dd>Emitted when a tracked passthrough rule with <i>args</i> has been removed for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
<p> RuleAdded(s: ipv, s: table, s: chain, i: priority, as: args)</p>
<dl>
<dd>Emitted when a rule with <i>args</i> has been added to <i>chain</i> in <i>table</i> with <i>priority</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
<p> RuleRemoved(s: ipv, s: table, s: chain, i: priority, as: args)</p>
<dl>
<dd>Emitted when a rule with <i>args</i> has been removed from <i>chain</i> in <i>table</i> with <i>priority</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.policies</h3>
<p>Enables firewalld to be able to lock down configuration changes from local applications. Local applications or services are able to change the firewall configuration if they are running as root (example: libvirt). With these operations administrator can lock the firewall configuration so that either none or only applications that are in the whitelist are able to request firewall changes. For permanent configuration see org.fedoraproject.FirewallD1.config.policies interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addLockdownWhitelistCommand(s: command) → Nothing</p>
<dl>
<dd>Add <i>command</i> to whitelist. See <i>command</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.addLockdownWhitelistCommand. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addLockdownWhitelistContext(s: context) → Nothing</p>
<dl>
<dd>Add <i>context</i> to whitelist. See <i>selinux</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.addLockdownWhitelistContext. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addLockdownWhitelistUid(i: uid) → Nothing</p>
<dl>
<dd>Add user id <i>uid</i> to whitelist. See <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.addLockdownWhitelistUid. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addLockdownWhitelistUser(s: user) → Nothing</p>
<dl>
<dd>Add <i>user</i> name to whitelist. See <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.addLockdownWhitelistUser. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> disableLockdown() → Nothing</p>
<dl>
<dd>Disable lockdown. This is a runtime and permanent change. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> enableLockdown() → Nothing</p>
<dl>
<dd>Enable lockdown. Be careful &#8211; if the calling application/user is not on lockdown whitelist when you enable lockdown you won&#8217;t be able to disable it again with the application, you would need to edit firewalld.conf. This is a runtime and permanent change. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getLockdownWhitelistCommands() → as</p>
<dl>
<dd>List all command lines (s) that are on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.getLockdownWhitelistCommands.</dl>
<p> getLockdownWhitelistContexts() → as</p>
<dl>
<dd>List all contexts (s) that are on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.getLockdownWhitelistContexts.</dl>
<p> getLockdownWhitelistUids() → ai</p>
<dl>
<dd>List all user ids (i) that are on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.getLockdownWhitelistUids.</dl>
<p> getLockdownWhitelistUsers() → as</p>
<dl>
<dd>List all users (s) that are on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.getLockdownWhitelistUsers.</dl>
<p> queryLockdown() → b</p>
<dl>
<dd>Query whether lockdown is enabled.</dl>
<p> queryLockdownWhitelistCommand(s: command) → b</p>
<dl>
<dd>Query whether <i>command</i> is on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.queryLockdownWhitelistCommand.</dl>
<p> queryLockdownWhitelistContext(s: context) → b</p>
<dl>
<dd>Query whether <i>context</i> is on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.queryLockdownWhitelistContext.</dl>
<p> queryLockdownWhitelistUid(i: uid) → b</p>
<dl>
<dd>Query whether user id <i>uid</i> is on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.queryLockdownWhitelistUid.</dl>
<p> queryLockdownWhitelistUser(s: user) → b</p>
<dl>
<dd>Query whether <i>user</i> is on whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.queryLockdownWhitelistUser.</dl>
<p> removeLockdownWhitelistCommand(s: command) → Nothing</p>
<dl>
<dd>Remove <i>command</i> from whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.removeLockdownWhitelistCommand. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistContext(s: context) → Nothing</p>
<dl>
<dd>Remove <i>context</i> from whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.removeLockdownWhitelistContext. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistUid(i: uid) → Nothing</p>
<dl>
<dd>Remove user id <i>uid</i> from whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.removeLockdownWhitelistUid. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistUser(s: user) → Nothing</p>
<dl>
<dd>Remove <i>user</i> from whitelist. For permanent operation see org.fedoraproject.FirewallD1.config.policies.Methods.removeLockdownWhitelistUser. </p>
<p> Possible errors: NOT_ENABLED</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>LockdownDisabled()</p>
<dl>
<dd>Emitted when lockdown has been disabled.</dl>
<p> LockdownEnabled()</p>
<dl>
<dd>Emitted when lockdown has been enabled.</dl>
<p> LockdownWhitelistCommandAdded(s: command)</p>
<dl>
<dd>Emitted when <i>command</i> has been added to whitelist.</dl>
<p> LockdownWhitelistCommandRemoved(s: command)</p>
<dl>
<dd>Emitted when <i>command</i> has been removed from whitelist.</dl>
<p> LockdownWhitelistContextAdded(s: context)</p>
<dl>
<dd>Emitted when <i>context</i> has been added to whitelist.</dl>
<p> LockdownWhitelistContextRemoved(s: context)</p>
<dl>
<dd>Emitted when <i>context</i> has been removed from whitelist.</dl>
<p> LockdownWhitelistUidAdded(i: uid)</p>
<dl>
<dd>Emitted when user id <i>uid</i> has been added to whitelist.</dl>
<p> LockdownWhitelistUidRemoved(i: uid)</p>
<dl>
<dd>Emitted when user id <i>uid</i> has been removed from whitelist.</dl>
<p> LockdownWhitelistUserAdded(s: user)</p>
<dl>
<dd>Emitted when <i>user</i> has been added to whitelist.</dl>
<p> LockdownWhitelistUserRemoved(s: user)</p>
<dl>
<dd>Emitted when <i>user</i> has been removed from whitelist.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.zone</h3>
<p>Operations in this interface allows to get, add, remove and query runtime zone&#8217;s settings. For permanent settings see org.fedoraproject.FirewallD1.config.zone interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addForwardPort(s: zone, s: port, s: protocol, s: toport, s: toaddr, i: timeout) → s</p>
<dl>
<dd>Add the IPv4 forward port into <i>zone</i>. If <i>zone</i> is empty, use default zone. The port can either be a single port number <i>portid</i> or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i> or <i>udp</i>. The destination address is a simple IP address. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addForwardPort. </p>
<p> Returns name of zone to which the forward port was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, INVALID_ADDR, INVALID_FORWARD, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addIcmpBlock(s: zone, s: icmp, i: timeout) → s</p>
<dl>
<dd>Add an ICMP block <i>icmp</i> into <i>zone</i>. The <i>icmp</i> is the one of the icmp types firewalld supports. To get a listing of supported icmp types use org.fedoraproject.FirewallD1.Methods.listIcmpTypes If <i>zone</i> is empty, use default zone. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addIcmpBlock. </p>
<p> Returns name of zone to which the ICMP block was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ICMPTYPE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addIcmpBlockInversion(s: zone) → s</p>
<dl>
<dd>Add ICMP block inversion to <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addIcmpBlockInversion. </p>
<p> Returns name of zone to which the ICMP block inversion was added. </p>
<p> Possible errors: INVALID_ZONE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addInterface(s: zone, s: interface) → s</p>
<dl>
<dd>Bind <i>interface</i> with <i>zone</i>. From now on all traffic going through the <i>interface</i> will respect the <i>zone</i>&#8216;s settings. If <i>zone</i> is empty, use default zone. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addInterface. </p>
<p> Returns name of zone to which the interface was bound. </p>
<p> Possible errors: INVALID_ZONE, INVALID_INTERFACE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addMasquerade(s: zone, i: timeout) → s</p>
<dl>
<dd>Enable IPv4 masquerade in <i>zone</i>. If <i>zone</i> is empty, use default zone. If <i>timeout</i> is non-zero, masquerading will be active for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addMasquerade. </p>
<p> Returns name of zone in which the masquerade was enabled. </p>
<p> Possible errors: INVALID_ZONE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addPort(s: zone, s: port, s: protocol, i: timeout) → s</p>
<dl>
<dd>Add port into <i>zone</i>. If <i>zone</i> is empty, use default zone. The port can either be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i> or <i>udp</i>. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addPort. </p>
<p> Returns name of zone to which the port was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addProtocol(s: zone, s: protocol, i: timeout) → s</p>
<dl>
<dd>Add protocol into <i>zone</i>. If <i>zone</i> is empty, use default zone. The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addProtocol. </p>
<p> Returns name of zone to which the protocol was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PROTOCOL, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addRichRule(s: zone, s: rule, i: timeout) → s</p>
<dl>
<dd>Add rich language <i>rule</i> into <i>zone</i>. For the rich language rule syntax, please have a look at <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5). If <i>zone</i> is empty, use default zone. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addRichRule. </p>
<p> Returns name of zone to which the rich language rule was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_RULE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addService(s: zone, s: service, i: timeout) → s</p>
<dl>
<dd>Add <i>service</i> into <i>zone</i>. If <i>zone</i> is empty, use default zone. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. To get a list of supported services, use org.fedoraproject.FirewallD1.Methods.listServices. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addService. </p>
<p> Returns name of zone to which the service was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_SERVICE, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addSource(s: zone, s: source) → s</p>
<dl>
<dd>Bind <i>source</i> with <i>zone</i>. From now on all traffic going from this <i>source</i> will respect the <i>zone</i>&#8216;s settings. A source address or address range is either an IP address or a network IP address with a mask for IPv4 or IPv6. For IPv4, the mask can be a network mask or a plain number. For IPv6 the mask is a plain number. Use of host names is not supported. If <i>zone</i> is empty, use default zone. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addSource. </p>
<p> Returns name of zone to which the source was bound. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ADDR, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> addSourcePort(s: zone, s: port, s: protocol, i: timeout) → s</p>
<dl>
<dd>Add source port into <i>zone</i>. If <i>zone</i> is empty, use default zone. The port can either be a single port number or a port range <i>portid</i>&#8211;<i>portid</i>. The protocol can either be <i>tcp</i> or <i>udp</i>. If <i>timeout</i> is non-zero, the operation will be active only for the amount of seconds. For permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.addSourcePort. </p>
<p> Returns name of zone to which the port was added. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, ALREADY_ENABLED, INVALID_COMMAND</dl>
<p> changeZone(s: zone, s: interface) → s</p>
<dl>
<dd>This function is deprecated, use org.fedoraproject.FirewallD1.zone.Methods.changeZoneOfInterface instead.</dl>
<p> changeZoneOfInterface(s: zone, s: interface) → s</p>
<dl>
<dd>Change a zone an <i>interface</i> is bound to to <i>zone</i>. It&#8217;s basically removeInterface(<i>interface</i>) followed by addInterface(<i>zone</i>, <i>interface</i>). If <i>interface</i> has not been bound to a zone before, it behaves like addInterface. If <i>zone</i> is empty, use default zone. </p>
<p> Returns name of zone to which the interface was bound. </p>
<p> Possible errors: INVALID_ZONE, ZONE_ALREADY_SET, ZONE_CONFLICT</dl>
<p> changeZoneOfSource(s: zone, s: source) → s</p>
<dl>
<dd>Change a zone an <i>source</i> is bound to to <i>zone</i>. It&#8217;s basically removeSource(<i>source</i>) followed by addSource(<i>zone</i>, <i>source</i>). If <i>source</i> has not been bound to a zone before, it behaves like addSource. If <i>zone</i> is empty, use default zone. </p>
<p> Returns name of zone to which the source was bound. </p>
<p> Possible errors: INVALID_ZONE, ZONE_ALREADY_SET, ZONE_CONFLICT</dl>
<p> getActiveZones() → a{sa{sas}}</p>
<dl>
<dd>Return dictionary of currently active zones altogether with interfaces and sources used in these zones. Active zones are zones, that have a binding to an interface or source. </p>
<p> Return value is a dictionary where keys are zone names (s) and values are again dictionaries where keys are either &#8216;interfaces&#8217; or &#8216;sources&#8217; and values are arrays of interface names (s) or sources (s).</dl>
<p> getForwardPorts(s: zone) → aas</p>
<dl>
<dd>Return array of IPv4 forward ports previously added into <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getForwardPorts. </p>
<p> Return value is array of 4-tuples, where each 4-tuple consists of (port, protocol, to-port, to-addr). to-addr might be empty in case of local forwarding. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getIcmpBlocks(s: zone) → as</p>
<dl>
<dd>Return array of ICMP type (s) blocks previously added into <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getIcmpBlocks. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getIcmpBlockInversion(s: zone) → b</p>
<dl>
<dd>Return whether ICMP block inversion was previously added to <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getIcmpBlockInversion. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getInterfaces(s: zone) → as</p>
<dl>
<dd>Return array of interfaces (s) previously bound with <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getInterfaces. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getPorts(s: zone) → aas</p>
<dl>
<dd>Return array of ports (2-tuple of port and protocol) previously enabled in <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getPorts. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getProtocols(s: zone) → as</p>
<dl>
<dd>Return array of protocols (s) previously enabled in <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getProtocols. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getRichRules(s: zone) → as</p>
<dl>
<dd>Return array of rich language rules (s) previously added into <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getRichRules. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getServices(s: zone) → as</p>
<dl>
<dd>Return array of services (s) previously enabled in <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getServices. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getSourcePorts(s: zone) → aas</p>
<dl>
<dd>Return array of source ports (2-tuple of port and protocol) previously enabled in <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getSourcePorts. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getSources(s: zone) → as</p>
<dl>
<dd>Return array of sources (s) previously bound with <i>zone</i>. If <i>zone</i> is empty, use default zone. For getting permanent settings see org.fedoraproject.FirewallD1.config.zone.Methods.getSources. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getZoneOfInterface(s: interface) → s</p>
<dl>
<dd>Return name (s) of zone the <i>interface</i> is bound to or empty string.</dl>
<p> getZoneOfSource(s: source) → s</p>
<dl>
<dd>Return name (s) of zone the <i>source</i> is bound to or empty string.</dl>
<p> getZones() → as</p>
<dl>
<dd>Return array of names (s) of predefined zones known to current runtime environment. For list of zones known to permanent environment see org.fedoraproject.FirewallD1.config.Methods.listZones. The lists (of zones known to runtime and permanent environment) will contain same zones in most cases, but might differ for example if org.fedoraproject.FirewallD1.config.Methods.addZone has been called recently, but firewalld has not been reloaded since then.</dl>
<p> isImmutable(s: zone) → b</p>
<dl>
<dd>Deprecated.</dl>
<p> queryForwardPort(s: zone, s: port, s: protocol, s: toport, s: toaddr) → b</p>
<dl>
<dd>Return whether the IPv4 forward port (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>) has been added into <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryForwardPort. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, INVALID_ADDR, INVALID_FORWARD</dl>
<p> queryIcmpBlock(s: zone, s: icmp) → b</p>
<dl>
<dd>Return whether an ICMP block for <i>icmp</i> has been added into <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryIcmpBlock. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ICMPTYPE</dl>
<p> queryIcmpBlockInversion(s: zone) → b</p>
<dl>
<dd>Return whether ICMP block inversion has been added to <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryIcmpBlockInversion. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ICMPTYPE</dl>
<p> queryInterface(s: zone, s: interface) → b</p>
<dl>
<dd>Query whether <i>interface</i> has been bound to <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryInterface. </p>
<p> Possible errors: INVALID_ZONE, INVALID_INTERFACE</dl>
<p> queryMasquerade(s: zone) → b</p>
<dl>
<dd>Return whether IPv4 masquerading has been enabled in <i>zone</i> If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryMasquerade. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> queryPort(s: zone, s: port, s: protocol) → b</p>
<dl>
<dd>Return whether <i>port</i>/<i>protocol</i> has been added in <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryPort. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL</dl>
<p> queryProtocol(s: zone, s: protocol) → b</p>
<dl>
<dd>Return whether <i>protocol</i> has been added in <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryProtocol. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PROTOCOL</dl>
<p> queryRichRule(s: zone, s: rule) → b</p>
<dl>
<dd>Return whether rich rule <i>rule</i> has been added in <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryRichRule. </p>
<p> Possible errors: INVALID_ZONE, INVALID_RULE</dl>
<p> queryService(s: zone, s: service) → b</p>
<dl>
<dd>Return whether <i>service</i> has been added for <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.queryService. </p>
<p> Possible errors: INVALID_ZONE, INVALID_SERVICE</dl>
<p> querySource(s: zone, s: source) → b</p>
<dl>
<dd>Query whether <i>source</i>has been bound to <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.querySource. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ADDR</dl>
<p> querySourcePort(s: zone, s: port, s: protocol) → b</p>
<dl>
<dd>Return whether <i>port</i>/<i>protocol</i> has been added in <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.querySourcePort. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL</dl>
<p> removeForwardPort(s: zone, s: port, s: protocol, s: toport, s: toaddr) → s</p>
<dl>
<dd>Remove IPv4 forward port ((<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>)) from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeForwardPort. </p>
<p> Returns name of zone from which the forward port was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, INVALID_ADDR, INVALID_FORWARD, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeIcmpBlock(s: zone, s: icmp) → s</p>
<dl>
<dd>Remove ICMP block <i>icmp</i> from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeIcmpBlock. </p>
<p> Returns name of zone from which the ICMP block was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ICMPTYPE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeIcmpBlockInversion(s: zone) → s</p>
<dl>
<dd>Remove ICMP block inversion from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeIcmpBlockInversion. </p>
<p> Returns name of zone from which the ICMP block inversion was removed. </p>
<p> Possible errors: INVALID_ZONE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeInterface(s: zone, s: interface) → s</p>
<dl>
<dd>Remove binding of <i>interface</i> from <i>zone</i>. If <i>zone</i> is empty, the interface will be removed from zone it belongs to. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeInterface. </p>
<p> Returns name of zone from which the <i>interface</i> was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_INTERFACE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeMasquerade(s: zone) → s</p>
<dl>
<dd>Disable IPv4 masquerade for <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeMasquerade. </p>
<p> Returns name of zone for which the masquerade was disabled. </p>
<p> Possible errors: INVALID_ZONE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removePort(s: zone, s: port, s: protocol) → s</p>
<dl>
<dd>Remove <i>port</i>/<i>protocol</i> from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removePort. </p>
<p> Returns name of zone from which the port was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeProtocol(s: zone, s: protocol) → s</p>
<dl>
<dd>Remove protocol from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeProtocol. </p>
<p> Returns name of zone from which the protocol was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PROTOCOL, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeRichRule(s: zone, s: rule) → s</p>
<dl>
<dd>Remove rich language <i>rule</i> from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeRichRule. </p>
<p> Returns name of zone from which the rich language rule was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_RULE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeService(s: zone, s: service) → s</p>
<dl>
<dd>Remove <i>service</i> from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeService. </p>
<p> Returns name of zone from which the service was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_SERVICE, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeSource(s: zone, s: source) → s</p>
<dl>
<dd>Remove binding of <i>source</i> from <i>zone</i>. If <i>zone</i> is empty, the source will be removed from zone it belongs to. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeSource. </p>
<p> Returns name of zone from which the <i>source</i> was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_ADDR, NOT_ENABLED, INVALID_COMMAND</dl>
<p> removeSourcePort(s: zone, s: port, s: protocol) → s</p>
<dl>
<dd>Remove <i>port</i>/<i>protocol</i> from <i>zone</i>. If <i>zone</i> is empty, use default zone. For permanent operation see org.fedoraproject.FirewallD1.config.zone.Methods.removeSourcePort. </p>
<p> Returns name of zone from which the source port was removed. </p>
<p> Possible errors: INVALID_ZONE, INVALID_PORT, MISSING_PROTOCOL, INVALID_PROTOCOL, NOT_ENABLED, INVALID_COMMAND</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>ForwardPortAdded(s: zone, s: port, s: protocol, s: toport, s: toaddr, i: timeout)</p>
<dl>
<dd>Emitted when forward port has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> ForwardPortRemoved(s: zone, s: port, s: protocol, s: toport, s: toaddr)</p>
<dl>
<dd>Emitted when forward port has been removed from <i>zone</i>.</dl>
<p> IcmpBlockAdded(s: zone, s: icmp, i: timeout)</p>
<dl>
<dd>Emitted when ICMP block for <i>icmp</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> IcmpBlockInversionAdded(s: zone)</p>
<dl>
<dd>Emitted when ICMP block inversion has been added to <i>zone</i>.</dl>
<p> IcmpBlockInversionRemoved(s: zone)</p>
<dl>
<dd>Emitted when ICMP block inversion has been removed from <i>zone</i>.</dl>
<p> IcmpBlockRemoved(s: zone, s: icmp)</p>
<dl>
<dd>Emitted when ICMP block for <i>icmp</i> has been removed from <i>zone</i>.</dl>
<p> InterfaceAdded(s: zone, s: interface)</p>
<dl>
<dd>Emitted when <i>interface</i> has been added to <i>zone</i>.</dl>
<p> InterfaceRemoved(s: zone, s: interface)</p>
<dl>
<dd>Emitted when <i>interface</i> has been removed from <i>zone</i>.</dl>
<p> MasqueradeAdded(s: zone, i: timeout)</p>
<dl>
<dd>Emitted when IPv4 masquerade has been enabled for <i>zone</i>.</dl>
<p> MasqueradeRemoved(s: zone)</p>
<dl>
<dd>Emitted when IPv4 masquerade has been disabled for <i>zone</i>.</dl>
<p> PortAdded(s: zone, s: port, s: protocol, i: timeout)</p>
<dl>
<dd>Emitted when <i>port</i>/<i>protocol</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> PortRemoved(s: zone, s: port, s: protocol)</p>
<dl>
<dd>Emitted when <i>port</i>/<i>protocol</i> has been removed from <i>zone</i>.</dl>
<p> ProtocolAdded(s: zone, s: protocol, i: timeout)</p>
<dl>
<dd>Emitted when <i>protocol</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> ProtocolRemoved(s: zone, s: protocol)</p>
<dl>
<dd>Emitted when <i>protocol</i> has been removed from <i>zone</i>.</dl>
<p> RichRuleAdded(s: zone, s: rule, i: timeout)</p>
<dl>
<dd>Emitted when rich language <i>rule</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> RichRuleRemoved(s: zone, s: rule)</p>
<dl>
<dd>Emitted when rich language <i>rule</i> has been removed from <i>zone</i>.</dl>
<p> ServiceAdded(s: zone, s: service, i: timeout)</p>
<dl>
<dd>Emitted when <i>service</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> ServiceRemoved(s: zone, s: service)</p>
<dl>
<dd>Emitted when <i>service</i> has been removed from <i>zone</i>.</dl>
<p> SourceAdded(s: zone, s: source)</p>
<dl>
<dd>Emitted when <i>source</i> has been added to <i>zone</i>.</dl>
<p> SourcePortAdded(s: zone, s: port, s: protocol, i: timeout)</p>
<dl>
<dd>Emitted when <i>source-port</i>/<i>protocol</i> has been added to <i>zone</i> with <i>timeout</i>.</dl>
<p> SourcePortRemoved(s: zone, s: port, s: protocol)</p>
<dl>
<dd>Emitted when <i>source-port</i>/<i>protocol</i> has been removed from <i>zone</i>.</dl>
<p> SourceRemoved(s: zone, s: source)</p>
<dl>
<dd>Emitted when <i>source</i> has been removed from <i>zone</i>.</dl>
<p> ZoneChanged(s: zone, s: interface)</p>
<dl>
<dd>Deprecated</dl>
<p> ZoneOfInterfaceChanged(s: zone, s: interface)</p>
<dl>
<dd>Emitted when a zone an <i>interface</i> is part of has been changed to <i>zone</i>.</dl>
<p> ZoneOfSourceChanged(s: zone, s: source)</p>
<dl>
<dd>Emitted when a zone an <i>source</i> is part of has been changed to <i>zone</i>.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config</h3>
<p>Allows to permanently add, remove and query zones, services and icmp types. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addIPSet(s: ipset, (ssssa{ss}as): settings) → o</p>
<dl>
<dd>Add <i>ipset</i> with given <i>settings</i> into permanent configuration. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>type</i>, dictionary of <i>options</i> and array of <i>entries</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>type (s)</i>: see <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>options (a{ss})</i>: dictionary of {option : value} . See <i>options</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>entries (as)</i>: array of entries, see <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: NAME_CONFLICT, INVALID_NAME, INVALID_TYPE</dl>
<p> addIcmpType(s: icmptype, (sssas): settings) → o</p>
<dl>
<dd>Add <i>icmptype</i> with given <i>settings</i> into permanent configuration. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>destinations</i>. Returns object path of the new icmp type. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (as)</i>: array, either empty or containing strings &#8216;ipv4&#8217; or &#8216;ipv6&#8217;, see <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: NAME_CONFLICT, INVALID_NAME, INVALID_TYPE</dl>
<p> addService(s: service, (sssa(ss)asa{ss}asa(ss)): settings) → o</p>
<dl>
<dd>Add <i>service</i> with given <i>settings</i> into permanent configuration. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>ports</i> (port, protocol), array of <i>module names</i>, dictionary of <i>destinations</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). Returns object path of the new icmp type. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module names (as)</i>: array of kernel netfilter helpers, see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (a{ss})</i>: dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: NAME_CONFLICT, INVALID_NAME, INVALID_TYPE</dl>
<p> addZone(s: zone, (sssbsasa(ss)asba(ssss)asasasasa(ss)): settings) → o</p>
<dl>
<dd>Add <i>zone</i> with given <i>settings</i> into permanent configuration. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>UNUSED</i>, <i>target</i>, array of <i>services</i>, array of <i>ports</i> (port, protocol), array of <i>icmp-blocks</i>, <i>masquerade</i>, array of <i>forward-ports</i> (port, protocol, to-port, to-addr), array of <i>interfaces</i>, array of <i>sources</i>, array of <i>rich rules</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>UNUSED (b)</i>: this boolean value is no longer used for anything.</p>
<dl>
<dd></dl>
<p> <i>target (s)</i>: see <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>services (as)</i>: array of service names, see <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>icmp-blocks (as)</i>: array of icmp-blocks. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>masquerade (b)</i>: see <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>forward-ports (a(ssss))</i>: array of (port, protocol, to-port, to-addr). See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>interfaces (as)</i>: array of interfaces. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source addresses (as)</i>: array of source addresses. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>rich rules (as)</i>: array of rich-language rules. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: NAME_CONFLICT, INVALID_NAME, INVALID_TYPE</dl>
<p> getHelperByName(s: helper) → o</p>
<dl>
<dd>Return object path (permanent configuration) of <i>helper</i> with given name. </p>
<p> Possible errors: INVALID_HELPER</dl>
<p> getHelperNames() → as</p>
<dl>
<dd>Return list of <i>helper</i> names (permanent configuration).</dl>
<p> getIPSetByName(s: ipset) → o</p>
<dl>
<dd>Return object path (permanent configuration) of <i>ipset</i> with given name. </p>
<p> Possible errors: INVALID_IPSET</dl>
<p> getIPSetNames() → as</p>
<dl>
<dd>Return list of <i>ipset</i> names (permanent configuration).</dl>
<p> getIcmpTypeByName(s: icmptype) → o</p>
<dl>
<dd>Return object path (permanent configuration) of <i>icmptype</i> with given name. </p>
<p> Possible errors: INVALID_ICMPTYPE</dl>
<p> getIcmpTypeNames() → as</p>
<dl>
<dd>Return list of <i>icmptype</i> names (permanent configuration).</dl>
<p> getServiceByName(s: service) → o</p>
<dl>
<dd>Return object path (permanent configuration) of <i>service</i> with given name. </p>
<p> Possible errors: INVALID_SERVICE</dl>
<p> getServiceNames() → as</p>
<dl>
<dd>Return list of <i>service</i> names (permanent configuration).</dl>
<p> getZoneByName(s: zone) → o</p>
<dl>
<dd>Return object path (permanent configuration) of <i>zone</i> with given name. </p>
<p> Possible errors: INVALID_ZONE</dl>
<p> getZoneNames() → as</p>
<dl>
<dd>Return list of <i>zone</i> names (permanent configuration) of.</dl>
<p> getZoneOfInterface(s: iface) → s</p>
<dl>
<dd>Return name of zone the <i>iface</i> is bound to or empty string.</dl>
<p> getZoneOfSource(s: source) → s</p>
<dl>
<dd>Return name of zone the <i>source</i> is bound to or empty string.</dl>
<p> listHelpers() → ao</p>
<dl>
<dd>Return array of object paths (o) of helper in permanent configuration. For runtime configuration see org.fedoraproject.FirewallD1.Methods.getHelpers.</dl>
<p> listIPSets() → ao</p>
<dl>
<dd>Return array of object paths (o) of ipset in permanent configuration. For runtime configuration see org.fedoraproject.FirewallD1.ipset.Methods.getIPSets.</dl>
<p> listIcmpTypes() → ao</p>
<dl>
<dd>Return array of object paths (o) of icmp types in permanent configuration. For runtime configuration see org.fedoraproject.FirewallD1.Methods.listIcmpTypes.</dl>
<p> listServices() → ao</p>
<dl>
<dd>Return array of objects paths (o) of services in permanent configuration. For runtime configuration see org.fedoraproject.FirewallD1.Methods.listServices.</dl>
<p> listZones() → ao</p>
<dl>
<dd>List object paths of zones known to permanent environment. For list of zones known to runtime environment see org.fedoraproject.FirewallD1.zone.Methods.getZones. The lists (of zones known to runtime and permanent environment) will contain same zones in most cases, but might differ for example if org.fedoraproject.FirewallD1.config.Methods.addZone has been called recently, but firewalld has not been reloaded since then.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>HelperAdded(s: helper)</p>
<dl>
<dd>Emitted when <i>helper</i> has been added.</dl>
<p> IPSetAdded(s: ipset)</p>
<dl>
<dd>Emitted when <i>ipset</i> has been added.</dl>
<p> IcmpTypeAdded(s: icmptype)</p>
<dl>
<dd>Emitted when <i>icmptype</i> has been added.</dl>
<p> ServiceAdded(s: service)</p>
<dl>
<dd>Emitted when <i>service</i> has been added.</dl>
<p> ZoneAdded(s: zone)</p>
<dl>
<dd>Emitted when <i>zone</i> has been added.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>AutomaticHelpers &#8211; s &#8211; (rw)</p>
<dl>
<dd>Indicates whether automatic helper assignment in kernel should be used or not. With the system setting this is left to the kernel or system default.</dl>
<p> CleanupOnExit &#8211; s &#8211; (rw)</p>
<dl>
<dd>If firewalld stops, it cleans up all firewall rules. Setting this option to no or false leaves the current firewall rules untouched.</dl>
<p> DefaultZone &#8211; s &#8211; (ro)</p>
<dl>
<dd>Default zone for connections or interfaces if the zone is not selected or specified by NetworkManager, initscripts or command line tool.</dl>
<p> <i>IPv6_rpfilter</i> &#8211; s &#8211; (rw)</p>
<dl>
<dd>Indicates whether the reverse path filter test on a packet for IPv6 is enabled. If a reply to the packet would be sent via the same interface that the packet arrived on, the packet will match and be accepted, otherwise dropped.</dl>
<p> <i>IndividualCalls</i> &#8211; s &#8211; (ro)</p>
<dl>
<dd>Indicates whether individual calls combined -restore calls are used. If enabled, this increases the time that is needed to apply changes and to start the daemon, but is good for debugging.</dl>
<p> Lockdown &#8211; s &#8211; (rw)</p>
<dl>
<dd>If this property is enabled, firewall changes with the D-Bus interface will be limited to applications that are listed in the lockdown whitelist.</dl>
<p> LogDenied &#8211; s &#8211; (rw)</p>
<dl>
<dd>If LogDenied is enabled, then logging rules are added right before reject and drop rules in the INPUT, FORWARD and OUTPUT chains for the default rules and also final reject and drop rules in zones. Possible values are: <i>all</i>, <i>unicast</i>, <i>broadcast</i>, <i>multicast</i> and <i>off</i>.</dl>
<p> MinimalMark &#8211; i &#8211; (rw)</p>
<dl>
<dd>For some firewall settings several rules are needed in different tables to be able to handle packets in the correct way. To achieve that these packets are marked using the MARK target. With the MinimalMark property a block of marks can be reserved for private use; only marks over this value are used.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.direct</h3>
<p>Interface for permanent direct configuration, see also <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5). For runtime direct configuration see org.fedoraproject.FirewallD1.direct interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addChain(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Add a new <i>chain</i> to <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Make sure there&#8217;s no other chain with this name already. There already exist basic chains to use with direct methods, for example <i>INPUT_direct</i> chain. These chains are jumped into before chains for zones, i.e. every rule put into <i>INPUT_direct</i> will be checked before rules in zones. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.addChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, ALREADY_ENABLED</dl>
<p> addPassthrough(s: ipv, as: args) → Nothing</p>
<dl>
<dd>Add a passthrough rule with the arguments <i>args</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.addPassthrough. </p>
<p> Possible errors: INVALID_IPV, ALREADY_ENABLED</dl>
<p> addRule(s: ipv, s: table, s: chain, i: priority, as: args) → Nothing</p>
<dl>
<dd>Add a rule with the arguments <i>args</i> to <i>chain</i> in <i>table</i> with <i>priority</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). The priority is used to order rules. Priority 0 means add rule on top of the chain, with a higher priority the rule will be added further down. Rules with the same priority are on the same level and the order of these rules is not fixed and may change. If you want to make sure that a rule will be added after another one, use a low priority for the first and a higher for the following. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.addRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, ALREADY_ENABLED</dl>
<p> getAllChains() → a(sss)</p>
<dl>
<dd>Get all chains added to all tables in format: ipv, table, chain. This concerns only chains previously added with addChain. Return value is a array of (<i>ipv</i>, <i>table</i>, <i>chain</i>). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getAllChains. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>table (s)</i>: one of <i>filter</i>, <i>mangle</i>, <i>nat</i>, <i>raw</i>, <i>security</i></p>
<dl>
<dd></dl>
<p> <i>chain (s)</i>: name of a chain.</p>
<dl>
<dd></dl>
</dl>
<p> getAllPassthroughs() → a(sas)</p>
<dl>
<dd>Get all passthrough rules added in all ipv types in format: ipv, rule. This concerns only rules previously added with addPassthrough. Return value is a array of (<i>ipv</i>, array of <i>arguments</i>). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getAllPassthroughs. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getAllRules() → a(sssias)</p>
<dl>
<dd>Get all rules added to all chains in all tables in format: ipv, table, chain, priority, rule. This concerns only rules previously added with addRule. Return value is a array of (<i>ipv</i>, <i>table</i>, <i>chain</i>, <i>priority</i>, array of <i>arguments</i>). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getAllRules. </p>
<p> <i>ipv (s)</i>: either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables).</p>
<dl>
<dd></dl>
<p> <i>table (s)</i>: one of <i>filter</i>, <i>mangle</i>, <i>nat</i>, <i>raw</i>, <i>security</i></p>
<dl>
<dd></dl>
<p> <i>chain (s)</i>: name of a chain.</p>
<dl>
<dd></dl>
<p> <i>priority (i)</i>: used to order rules.</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getChains(s: ipv, s: table) → as</p>
<dl>
<dd>Return an array of chains (s) added to <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only chains previously added with addChain. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getChains. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> getPassthroughs(s: ipv) → aas</p>
<dl>
<dd>Get tracked passthrough rules added in either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addPassthrough. Return value is a array of (array of <i>arguments</i>). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getPassthroughs. </p>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
</dl>
<p> getRules(s: ipv, s: table, s: chain) → a(ias)</p>
<dl>
<dd>Get all rules added to <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. Return value is a array of (<i>priority</i>, array of <i>arguments</i>). For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.getRules. </p>
<p> <i>priority (i)</i>: used to order rules.</p>
<dl>
<dd></dl>
<p> <i>arguments (as)</i>: array of commands, parameters and other iptables/ip6tables/ebtables command line options.</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> getSettings() → (a(sss)a(sssias)a(sas))</p>
<dl>
<dd>Get settings of permanent direct configuration in format: array of <i>chains</i>, array of <i>rules</i>, array of <i>passthroughs</i>. </p>
<p> <i>chains (a(sss))</i>: array of (<i>ipv</i>, <i>table</i>, <i>chain</i>), see &#8216;chain&#8217; in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.PP <i>rules (a(sssias))</i>: array of (<i>ipv</i>, <i>table</i>, <i>chain</i>, <i>priority</i>, array of <i>arguments</i>), see &#8216;rule&#8217; in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.PP <i>passthroughs (a(sas))</i>: array of (<i>ipv</i>, array of <i>arguments</i>), see passthrough in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.sp</dl>
<p> queryChain(s: ipv, s: table, s: chain) → b</p>
<dl>
<dd>Return whether a <i>chain</i> exists in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only chains previously added with addChain. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.queryChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> queryPassthrough(s: ipv, as: args) → b</p>
<dl>
<dd>Return whether a tracked passthrough rule with the arguments <i>args</i> exists for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addPassthrough. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.queryPassthrough. </p>
<p> Possible errors: INVALID_IPV</dl>
<p> queryRule(s: ipv, s: table, s: chain, i: priority, as: args) → b</p>
<dl>
<dd>Return whether a rule with <i>priority</i> and the arguments <i>args</i> exists in <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.queryRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> removeChain(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Remove a <i>chain</i> from <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only chains previously added with addChain can be removed this way. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.removeChain. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, NOT_ENABLED</dl>
<p> removePassthrough(s: ipv, as: args) → Nothing</p>
<dl>
<dd>Remove a passthrough rule with arguments <i>args</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only rules previously added with addPassthrough can be removed this way. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.removePassthrough. </p>
<p> Possible errors: INVALID_IPV, NOT_ENABLED</dl>
<p> removeRule(s: ipv, s: table, s: chain, i: priority, as: args) → Nothing</p>
<dl>
<dd>Remove a rule with <i>priority</i> and arguments <i>args</i> from <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). Only rules previously added with addRule can be removed this way. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.removeRule. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE, NOT_ENABLED</dl>
<p> removeRules(s: ipv, s: table, s: chain) → Nothing</p>
<dl>
<dd>Remove all rules from <i>chain</i> in <i>table</i> for <i>ipv</i> being either <i>ipv4</i> (iptables) or <i>ipv6</i> (ip6tables) or <i>eb</i> (ebtables). This concerns only rules previously added with addRule. For runtime operation see org.fedoraproject.FirewallD1.direct.Methods.removeRules. </p>
<p> Possible errors: INVALID_IPV, INVALID_TABLE</dl>
<p> update((a(sss)a(sssias)a(sas)): settings) → Nothing</p>
<dl>
<dd>Update permanent direct configuration with given <i>settings</i>. Settings are in format: array of <i>chains</i>, array of <i>rules</i>, array of <i>passthroughs</i>. </p>
<p> <i>chains (a(sss))</i>: array of (<i>ipv</i>, <i>table</i>, <i>chain</i>), see &#8216;chain&#8217; in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.PP <i>rules (a(sssias))</i>: array of (<i>ipv</i>, <i>table</i>, <i>chain</i>, <i>priority</i>, array of <i>arguments</i>), see &#8216;rule&#8217; in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.PP <i>passthroughs (a(sas))</i>: array of (<i>ipv</i>, array of <i>arguments</i>), see passthrough in <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5).</p>
<dl>
<dd></dl>
<p> .<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>.sp Possible errors: INVALID_TYPE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Updated()</p>
<dl>
<dd>Emitted when configuration has been updated.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.policies</h3>
<p>Interface for permanent lockdown-whitelist configuration, see also <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For runtime configuration see org.fedoraproject.FirewallD1.policies interface. </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addLockdownWhitelistCommand(s: command) → Nothing</p>
<dl>
<dd>Add <i>command</i> to whitelist. See <i>command</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.addLockdownWhitelistCommand. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_TYPE</dl>
<p> addLockdownWhitelistContext(s: context) → Nothing</p>
<dl>
<dd>Add <i>context</i> to whitelist. See <i>selinux</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.addLockdownWhitelistContext. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_TYPE</dl>
<p> addLockdownWhitelistUid(i: uid) → Nothing</p>
<dl>
<dd>Add user id <i>uid</i> to whitelist. See <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.addLockdownWhitelistUid. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_TYPE</dl>
<p> addLockdownWhitelistUser(s: user) → Nothing</p>
<dl>
<dd>Add <i>user</i> name to whitelist. See <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.addLockdownWhitelistUser. </p>
<p> Possible errors: ALREADY_ENABLED, INVALID_TYPE</dl>
<p> getLockdownWhitelist() → (asasasai)</p>
<dl>
<dd>Get settings of permanent lockdown-whitelist configuration in format: <i>commands</i>, <i>selinux contexts</i>, <i>users</i>, <i>uids</i> </p>
<p> <i>commands (as)</i>: see <i>command</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>selinux contexts (as)</i>: see <i>selinux</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>users (as)</i>: see <i>name</i> attribute of <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>uids (ai)</i>: see <i>id</i> attribute of <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getLockdownWhitelistCommands() → as</p>
<dl>
<dd>List all command lines (s) that are on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.getLockdownWhitelistCommands.</dl>
<p> getLockdownWhitelistContexts() → as</p>
<dl>
<dd>List all contexts (s) that are on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.getLockdownWhitelistContexts.</dl>
<p> getLockdownWhitelistUids() → ai</p>
<dl>
<dd>List all user ids (i) that are on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.getLockdownWhitelistUids.</dl>
<p> getLockdownWhitelistUsers() → as</p>
<dl>
<dd>List all users (s) that are on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.getLockdownWhitelistUsers.</dl>
<p> queryLockdownWhitelistCommand(s: command) → b</p>
<dl>
<dd>Query whether <i>command</i> is on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.queryLockdownWhitelistCommand.</dl>
<p> queryLockdownWhitelistContext(s: context) → b</p>
<dl>
<dd>Query whether <i>context</i> is on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.queryLockdownWhitelistContext.</dl>
<p> queryLockdownWhitelistUid(i: uid) → b</p>
<dl>
<dd>Query whether user id <i>uid</i> is on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.queryLockdownWhitelistUid.</dl>
<p> queryLockdownWhitelistUser(s: user) → b</p>
<dl>
<dd>Query whether <i>user</i> is on whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.queryLockdownWhitelistUser.</dl>
<p> removeLockdownWhitelistCommand(s: command) → Nothing</p>
<dl>
<dd>Remove <i>command</i> from whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.removeLockdownWhitelistCommand. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistContext(s: context) → Nothing</p>
<dl>
<dd>Remove <i>context</i> from whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.removeLockdownWhitelistContext. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistUid(i: uid) → Nothing</p>
<dl>
<dd>Remove user id <i>uid</i> from whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.removeLockdownWhitelistUid. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeLockdownWhitelistUser(s: user) → Nothing</p>
<dl>
<dd>Remove <i>user</i> from whitelist. For runtime operation see org.fedoraproject.FirewallD1.policies.Methods.removeLockdownWhitelistUser. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> setLockdownWhitelist((asasasai): settings) → Nothing</p>
<dl>
<dd>Set permanent lockdown-whitelist configuration to <i>settings</i>. Settings are in format: <i>commands</i>, <i>selinux contexts</i>, <i>users</i>, <i>uids</i> </p>
<p> <i>commands (as)</i>: see <i>command</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>selinux contexts (as)</i>: see <i>selinux</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>users (as)</i>: see <i>name</i> attribute of <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>uids (ai)</i>: see <i>id</i> attribute of <i>user</i> option in <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_TYPE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>LockdownWhitelistUpdated()</p>
<dl>
<dd>Emitted when permanent lockdown-whitelist configuration has been updated.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.ipset</h3>
<p>Interface for permanent ipset configuration, see also <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addEntry(s: entry) → Nothing</p>
<dl>
<dd>Permanently add <i>entry</i> to list of entries of ipset. See <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.ipset.Methods.addEntry. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addOption(s: key, s: value) → Nothing</p>
<dl>
<dd>Permanently add (<i>key</i>, <i>value</i>) to the ipset. See <i>option</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDescription() → s</p>
<dl>
<dd>Get description of ipset. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> getEntries() → as</p>
<dl>
<dd>Get list of entries added to ipset. See <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.ipset.Methods.getEntries. </p>
<p> Possible errors: IPSET_WITH_TIMEOUT</dl>
<p> getOptions() → a{ss}</p>
<dl>
<dd>Get dictionary of <i>options</i> set for ipset. See <i>option</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> getSettings() → (ssssa{ss}as)</p>
<dl>
<dd>Return permament settings of the ipset. For getting runtime settings see org.fedoraproject.FirewallD1.ipset.Methods.getIPSetSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>type</i>, dictionary of <i>options</i> and array of <i>entries</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>type (s)</i>: see <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>options (a{ss})</i>: dictionary of {option : value} . See <i>options</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>entries (as)</i>: array of entries, see <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getShort() → s</p>
<dl>
<dd>Get name of ipset. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> getType() → s</p>
<dl>
<dd>Get type of ipset. See <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> getVersion() → s</p>
<dl>
<dd>Get version of ipset. See <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> loadDefaults() → Nothing</p>
<dl>
<dd>Load default settings for built-in ipset. </p>
<p> Possible errors: NO_DEFAULTS</dl>
<p> queryEntry(s: entry) → b</p>
<dl>
<dd>Return whether <i>entry</i> has been added to <i>ipset</i>. For runtime operation see org.fedoraproject.FirewallD1.ipset.Methods.queryEntry.</dl>
<p> queryOption(s: key, s: value) → b</p>
<dl>
<dd>Return whether (<i>key</i>, <i>value</i>) has been added to options of the <i>ipset</i>.</dl>
<p> remove() → Nothing</p>
<dl>
<dd>Remove not built-in ipset. </p>
<p> Possible errors: BUILTIN_IPSET</dl>
<p> removeEntry(s: entry) → Nothing</p>
<dl>
<dd>Permanently remove <i>entry</i> from ipset. See <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.ipset.Methods.removeEntry. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeOption(s: key) → Nothing</p>
<dl>
<dd>Permanently remove <i>key</i> from the ipset. See <i>option</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> rename(s: name) → Nothing</p>
<dl>
<dd>Rename not built-in ipset to <i>name</i>. </p>
<p> Possible errors: BUILTIN_IPSET</dl>
<p> setDescription(s: description) → Nothing</p>
<dl>
<dd>Permanently set description of ipset to <i>description</i>. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> setEntries(as: entries) → Nothing</p>
<dl>
<dd>Permanently set list of entries to <i>entries</i>. See <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> setOptions(a{ss}: options) → Nothing</p>
<dl>
<dd>Permanently set dict of options to <i>options</i>. See <i>option</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> setShort(s: short) → Nothing</p>
<dl>
<dd>Permanently set name of ipset to <i>short</i>. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> setType(s: ipset_type) → Nothing</p>
<dl>
<dd>Permanently set type of ipset to <i>ipset_type</i>. See <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> setVersion(s: version) → Nothing</p>
<dl>
<dd>Permanently set version of ipset to <i>version</i>. See <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</dl>
<p> update((ssssa{ss}as): settings) → Nothing</p>
<dl>
<dd>Update settings of ipset to <i>settings</i>. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>type</i>, dictionary of <i>options</i> and array of <i>entries</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>type (s)</i>: see <i>type</i> attribute of <i>ipset</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>options (a{ss})</i>: dictionary of {option : value} . See <i>options</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>entries (as)</i>: array of entries, see <i>entry</i> tag in <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_TYPE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Removed(s: name)</p>
<dl>
<dd>Emitted when ipset with <i>name</i> has been removed.</dl>
<p> Renamed(s: name)</p>
<dl>
<dd>Emitted when ipset has been renamed to <i>name</i>.</dl>
<p> Updated(s: name)</p>
<dl>
<dd>Emitted when ipset with <i>name</i> has been updated.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>builtin &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if ipset is build-in, false else.</dl>
<p> default &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if build-in ipset has default settings. False if it has been modified. Always False for not build-in ipsets.</dl>
<p> filename &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name (including .xml extension) of file where the configuration is stored.</dl>
<p> name &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name of ipset.</dl>
<p> path &#8211; s &#8211; (ro)</p>
<dl>
<dd>Path to directory where the ipset configuration is stored. Should be either /usr/lib/firewalld/ipsets or /etc/firewalld/ipsets.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.zone</h3>
<p>Interface for permanent zone configuration, see also <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addForwardPort(s: port, s: protocol, s: toport, s: toaddr) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>) to list of forward ports of zone. See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addForwardPort. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addIcmpBlock(s: icmptype) → Nothing</p>
<dl>
<dd>Permanently add <i>icmptype</i> to list of icmp types blocked in zone. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addIcmpBlock. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addIcmpBlock(s: icmptype) → Nothing</p>
<dl>
<dd>Permanently add icmp block inversion to zone. See <i>icmp-block-inversion</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addIcmpBlockInversion. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addInterface(s: interface) → Nothing</p>
<dl>
<dd>Permanently add <i>interface</i> to list of interfaces bound to zone. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addInterface. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addMasquerade() → Nothing</p>
<dl>
<dd>Permanently enable masquerading in zone. See <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addMasquerade. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addPort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>) to list of ports of zone. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addPort. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addProtocol(s: protocol) → Nothing</p>
<dl>
<dd>Permanently add protocol into <i>zone</i>. The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols. For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addProtocol. </p>
<p> Possible errors: INVALID_PROTOCOL, ALREADY_ENABLED</dl>
<p> addRichRule(s: rule) → Nothing</p>
<dl>
<dd>Permanently add <i>rule</i> to list of rich-language rules in zone. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addRichRule. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addService(s: service) → Nothing</p>
<dl>
<dd>Permanently add <i>service</i> to list of services used in zone. See <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addService. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addSource(s: source) → Nothing</p>
<dl>
<dd>Permanently add <i>source</i> to list of source addresses bound to zone. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addSource. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addSourcePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>) to list of source ports of zone. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.addSourcePort. </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDescription() → s</p>
<dl>
<dd>Get description of zone. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> getForwardPorts() → a(ssss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>) defined in zone. See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getForwardPorts.</dl>
<p> getIcmpBlockInversion() → b</p>
<dl>
<dd>Get icmp block inversion flag of zone. See <i>icmp-block-inversion</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> getIcmpBlocks() → as</p>
<dl>
<dd>Get list of icmp type names blocked in zone. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getIcmpBlocks.</dl>
<p> getInterfaces() → as</p>
<dl>
<dd>Get list of interfaces bound to zone. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getInterfaces.</dl>
<p> getMasquerade() → b</p>
<dl>
<dd>Return whether <i>masquerade</i> is enabled in zone. This is the same as queryMasquerade() method. See <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> getPorts() → a(ss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>) defined in zone. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getPorts.</dl>
<p> getProtocols() → as</p>
<dl>
<dd>Return array of protocols (s) previously enabled in <i>zone</i>. For getting runtime settings see org.fedoraproject.FirewallD1.zone.Methods.getProtocols.</dl>
<p> getRichRules() → as</p>
<dl>
<dd>Get list of rich-language rules in zone. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getRichRules.</dl>
<p> getServices() → as</p>
<dl>
<dd>Get list of service names used in zone. See <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getServices.</dl>
<p> getSettings() → (sssbsasa(ss)asba(ssss)asasasasa(ss))</p>
<dl>
<dd>Return permanent settings of given <i>zone</i>. For getting runtime settings see org.fedoraproject.FirewallD1.Methods.getZoneSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>UNUSED</i>, <i>target</i>, array of <i>services</i>, array of <i>ports</i> (port, protocol), array of <i>icmp-blocks</i>, <i>masquerade</i>, array of <i>forward-ports</i> (port, protocol, to-port, to-addr), array of <i>interfaces</i>, array of <i>sources</i>, array of <i>rich rules</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>UNUSED (b)</i>: this boolean value is no longer used for anything.</p>
<dl>
<dd></dl>
<p> <i>target (s)</i>: see <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>services (as)</i>: array of service names, see <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>icmp-blocks (as)</i>: array of icmp-blocks. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>masquerade (b)</i>: see <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>forward-ports (a(ssss))</i>: array of (port, protocol, to-port, to-addr). See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>interfaces (as)</i>: array of interfaces. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source addresses (as)</i>: array of source addresses. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>rich rules (as)</i>: array of rich-language rules. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getShort() → s</p>
<dl>
<dd>Get name of zone. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> getSourcePorts() → a(ss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>) defined in zone. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getSourcePorts.</dl>
<p> getSources() → as</p>
<dl>
<dd>Get list of source addresses bound to zone. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.getSources.</dl>
<p> getTarget() → s</p>
<dl>
<dd>Get target of zone. See <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> getVersion() → s</p>
<dl>
<dd>Get version of zone. See <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> loadDefaults() → Nothing</p>
<dl>
<dd>Load default settings for built-in zone. </p>
<p> Possible errors: NO_DEFAULTS</dl>
<p> queryForwardPort(s: port, s: protocol, s: toport, s: toaddr) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>) is in list of forward ports of zone. See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryForwardPort.</dl>
<p> queryIcmpBlock(s: icmptype) → b</p>
<dl>
<dd>Return whether <i>icmptype</i> is in list of icmp types blocked in zone. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryIcmpBlock.</dl>
<p> queryIcmpBlockInversion() → b</p>
<dl>
<dd>Return whether <i>icmp block inversion</i> is in enabled in zone. See <i>icmp-block-inversion</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryIcmpBlockInversion.</dl>
<p> queryInterface(s: interface) → b</p>
<dl>
<dd>Return whether <i>interface</i> is in list of interfaces bound to zone. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryInterface.</dl>
<p> queryMasquerade() → b</p>
<dl>
<dd>Return whether <i>masquerade</i> is enabled in zone. This is the same as getMasquerade() method. See <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryMasquerade.</dl>
<p> queryPort(s: port, s: protocol) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>) is in list of ports of zone. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryPort.</dl>
<p> queryProtocol(s: protocol) → b</p>
<dl>
<dd>Return whether <i>protocol</i> has been added in <i>zone</i>. For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryProtocol. </p>
<p> Possible errors: INVALID_PROTOCOL</dl>
<p> queryRichRule(s: rule) → b</p>
<dl>
<dd>Return whether <i>rule</i> is in list of rich-language rules in zone. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryRichRule.</dl>
<p> queryService(s: service) → b</p>
<dl>
<dd>Return whether <i>service</i> is in list of services used in zone. See <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.queryService.</dl>
<p> querySource(s: source) → b</p>
<dl>
<dd>Return whether <i>source</i> is in list of source addresses bound to zone. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.querySource.</dl>
<p> querySourcePort(s: port, s: protocol) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>) is in list of source ports of zone. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.querySourcePort.</dl>
<p> remove() → Nothing</p>
<dl>
<dd>Remove not built-in zone. </p>
<p> Possible errors: BUILTIN_ZONE</dl>
<p> removeForwardPort(s: port, s: protocol, s: toport, s: toaddr) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>) from list of forward ports of zone. See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeForwardPort. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeIcmpBlock(s: icmptype) → Nothing</p>
<dl>
<dd>Permanently remove <i>icmptype</i> from list of icmp types blocked in zone. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeIcmpBlock. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeIcmpBlockInversion() → Nothing</p>
<dl>
<dd>Permanently remove <i>icmp block inversion</i> from the zone. See <i>icmp-block-inversion</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeIcmpBlockInversion. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeInterface(s: interface) → Nothing</p>
<dl>
<dd>Permanently remove <i>interface</i> from list of interfaces bound to zone. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeInterface. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeMasquerade() → Nothing</p>
<dl>
<dd>Permanently disable masquerading in zone. See <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeMasquerade. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>) from list of ports of zone. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removePort. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeProtocol(s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove protocol from <i>zone</i>. For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeProtocol. </p>
<p> Possible errors: INVALID_PROTOCOL, NOT_ENABLED</dl>
<p> removeRichRule(s: rule) → Nothing</p>
<dl>
<dd>Permanently remove <i>rule</i> from list of rich-language rules in zone. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeRichRule. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeService(s: service) → Nothing</p>
<dl>
<dd>Permanently remove <i>service</i> from list of services used in zone. See <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeService. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeSource(s: source) → Nothing</p>
<dl>
<dd>Permanently remove <i>source</i> from list of source addresses bound to zone. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeSource. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeSourcePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>) from list of source ports of zone. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5). For runtime operation see org.fedoraproject.FirewallD1.zone.Methods.removeSourcePort. </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> rename(s: name) → Nothing</p>
<dl>
<dd>Rename not built-in zone to <i>name</i>. </p>
<p> Possible errors: BUILTIN_ZONE</dl>
<p> setDescription(s: description) → Nothing</p>
<dl>
<dd>Permanently set description of zone to <i>description</i>. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setForwardPorts(a(ssss): ports) → Nothing</p>
<dl>
<dd>Permanently set forward ports of zone to list of (<i>port</i>, <i>protocol</i>, <i>toport</i>, <i>toaddr</i>). See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setIcmpBlockInversion(b: flag) → Nothing</p>
<dl>
<dd>Permanently set icmp block inversion flag of zone to <i>flag</i>. See <i>icmp-block-inversion</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setIcmpBlocks(as: icmptypes) → Nothing</p>
<dl>
<dd>Permanently set list of icmp types blocked in zone to <i>icmptypes</i>. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setInterfaces(as: interfaces) → Nothing</p>
<dl>
<dd>Permanently set list of interfaces bound to zone to <i>interfaces</i>. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setMasquerade(b: masquerade) → Nothing</p>
<dl>
<dd>Permanently set masquerading in zone to <i>masquerade</i>. See <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setPorts(a(ss): ports) → Nothing</p>
<dl>
<dd>Permanently set ports of zone to list of (<i>port</i>, <i>protocol</i>). See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setProtocols(as: protocols) → Nothing</p>
<dl>
<dd>Permanently set list of protocols used in zone to <i>protocols</i>. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setRichRules(as: rules) → Nothing</p>
<dl>
<dd>Permanently set list of rich-language rules to <i>rules</i>. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setServices(as: services) → Nothing</p>
<dl>
<dd>Permanently set list of services used in zone to <i>services</i>. See <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setShort(s: short) → Nothing</p>
<dl>
<dd>Permanently set name of zone to <i>short</i>. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setSourcePorts(a(ss): ports) → Nothing</p>
<dl>
<dd>Permanently set source-ports of zone to list of (<i>port</i>, <i>protocol</i>). See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setSources(as: sources) → Nothing</p>
<dl>
<dd>Permanently set list of source addresses bound to zone to <i>sources</i>. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setTarget(s: target) → Nothing</p>
<dl>
<dd>Permanently set target of zone to <i>target</i>. See <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> setVersion(s: version) → Nothing</p>
<dl>
<dd>Permanently set version of zone to <i>version</i>. See <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</dl>
<p> update((sssbsasa(ss)asba(ssss)asasasasa(ss)): settings) → Nothing</p>
<dl>
<dd>Update settings of zone to <i>settings</i>. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>UNUSED</i>, <i>target</i>, array of <i>services</i>, array of <i>ports</i> (port, protocol), array of <i>icmp-blocks</i>, <i>masquerade</i>, array of <i>forward-ports</i> (port, protocol, to-port, to-addr), array of <i>interfaces</i>, array of <i>sources</i>, array of <i>rich rules</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>UNUSED (b)</i>: this boolean value is no longer used for anything.</p>
<dl>
<dd></dl>
<p> <i>target (s)</i>: see <i>target</i> attribute of <i>zone</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>services (as)</i>: array of service names, see <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>icmp-blocks (as)</i>: array of icmp-blocks. See <i>icmp-block</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>masquerade (b)</i>: see <i>masquerade</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>forward-ports (a(ssss))</i>: array of (port, protocol, to-port, to-addr). See <i>forward-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>interfaces (as)</i>: array of interfaces. See <i>interface</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source addresses (as)</i>: array of source addresses. See <i>source</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>rich rules (as)</i>: array of rich-language rules. See <i>rule</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_TYPE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Removed(s: name)</p>
<dl>
<dd>Emitted when zone with <i>name</i> has been removed.</dl>
<p> Renamed(s: name)</p>
<dl>
<dd>Emitted when zone has been renamed to <i>name</i>.</dl>
<p> Updated(s: name)</p>
<dl>
<dd>Emitted when zone with <i>name</i> has been updated.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>builtin &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if zone is build-in, false else.</dl>
<p> default &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if build-in zone has default settings. False if it has been modified. Always False for not build-in zones.</dl>
<p> filename &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name (including .xml extension) of file where the configuration is stored.</dl>
<p> name &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name of zone.</dl>
<p> path &#8211; s &#8211; (ro)</p>
<dl>
<dd>Path to directory where the zone configuration is stored. Should be either /usr/lib/firewalld/zones or /etc/firewalld/zones.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.service</h3>
<p>Interface for permanent service configuration, see also <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addModule(s: module) → Nothing</p>
<dl>
<dd>Permanently add <i>module</i> to list of modules (netfilter kernel helpers) used in service. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addPort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>) to list of ports in service. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> addProtocol(s: protocol) → Nothing</p>
<dl>
<dd>Permanently add protocol into <i>zone</i>. The protocol can be any protocol supported by the system. Please have a look at <i>/etc/protocols</i> for supported protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: INVALID_PROTOCOL, ALREADY_ENABLED</dl>
<p> addSourcePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>) to list of source ports in service. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDescription() → s</p>
<dl>
<dd>Get description of service. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getDestination(s: family) → s</p>
<dl>
<dd>Get destination for IP family being either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDestinations() → a{ss}</p>
<dl>
<dd>Get list of destinations. Return value is a dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getModules() → as</p>
<dl>
<dd>Get list of modules (netfilter kernel helpers) used in service. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getPorts() → a(ss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>) defined in service. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getProtocols() → as</p>
<dl>
<dd>Return array of protocols (s) defined in <i>service</i>. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getSettings() → (sssa(ss)asa{ss}asa(ss))</p>
<dl>
<dd>Return permanent settings of a <i>service</i>. For getting runtime settings see org.fedoraproject.FirewallD1.Methods.getServiceSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>ports</i> (port, protocol), array of <i>module names</i>, dictionary of <i>destinations</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module names (as)</i>: array of kernel netfilter helpers, see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (a{ss})</i>: dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>source-ports (a(ss))</i>: array of port and protocol pairs. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getShort() → s</p>
<dl>
<dd>Get name of service. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getSourcePorts() → a(ss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>) defined in service. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> getVersion() → s</p>
<dl>
<dd>Get version of service. See <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> loadDefaults() → Nothing</p>
<dl>
<dd>Load default settings for built-in service. </p>
<p> Possible errors: NO_DEFAULTS</dl>
<p> queryDestination(s: family, s: address) → b</p>
<dl>
<dd>Return whether a <i>destination</i> is in dictionary of destinations of this service. destination is in format: (<i>IP family</i>, <i>IP address</i>) where <i>IP family</i> can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> queryModule(s: module) → b</p>
<dl>
<dd>Return whether <i>module</i> is in list of modules (netfilter kernel helpers) used in service. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> queryPort(s: port, s: protocol) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>) is in list of ports in service. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> queryProtocol(s: protocol) → b</p>
<dl>
<dd>Return whether <i>protocol</i> is in list of protocols in service. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> querySourcePort(s: port, s: protocol) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>) is in list of source ports in service. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> remove() → Nothing</p>
<dl>
<dd>Remove not built-in service. </p>
<p> Possible errors: BUILTIN_SERVICE</dl>
<p> removeDestination(s: family) → Nothing</p>
<dl>
<dd>Permanently remove a destination with <i>family</i> (&#8216;ipv4&#8217; or &#8216;ipv6&#8217;) from service. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeModule(s: module) → Nothing</p>
<dl>
<dd>Permanently remove <i>module</i> from list of modules (netfilter kernel helpers) used in service. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>) from list of ports in service. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeProtocol(s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove <i>protocol</i> from list of protocols in service. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> removeSourcePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>) from list of source ports in service. See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> rename(s: name) → Nothing</p>
<dl>
<dd>Rename not built-in service to <i>name</i>. </p>
<p> Possible errors: BUILTIN_SERVICE</dl>
<p> setDescription(s: description) → Nothing</p>
<dl>
<dd>Permanently set description of service to <i>description</i>. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setDestination(s: family, s: address) → Nothing</p>
<dl>
<dd>Permanently set a destination address. destination is in format: (<i>IP family</i>, <i>IP address</i>) where <i>IP family</i> can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> setDestinations(a{ss}: destinations) → Nothing</p>
<dl>
<dd>Permanently set destinations of service to <i>destinations</i>, which is a dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setModules(as: modules) → Nothing</p>
<dl>
<dd>Permanently set list of modules (netfilter kernel helpers) used in service to <i>modules</i>. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setPorts(a(ss): ports) → Nothing</p>
<dl>
<dd>Permanently set ports of service to list of (<i>port</i>, <i>protocol</i>). See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setProtocols(as: protocols) → Nothing</p>
<dl>
<dd>Permanently set protocols of service to list of <i>protocols</i>. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setShort(s: short) → Nothing</p>
<dl>
<dd>Permanently set name of service to <i>short</i>. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setSourcePorts(a(ss): ports) → Nothing</p>
<dl>
<dd>Permanently set source-ports of service to list of (<i>port</i>, <i>protocol</i>). See <i>source-port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> setVersion(s: version) → Nothing</p>
<dl>
<dd>Permanently set version of service to <i>version</i>. See <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</dl>
<p> update((sssa(ss)asa{ss}asa(ss)): settings) → Nothing</p>
<dl>
<dd>Update settings of service to <i>settings</i>. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>ports</i> (port, protocol), array of <i>module names</i>, dictionary of <i>destinations</i>, array of <i>protocols</i> and array of <i>source-ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>service</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module names (as)</i>: array of kernel netfilter helpers, see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (a{ss})</i>: dictionary of {IP family : IP address} where &#8216;IP family&#8217; key can be either &#8216;ipv4&#8217; or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>protocols (as)</i>: array of protocols. See <i>protocol</i> tag in <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_TYPE</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Removed(s: name)</p>
<dl>
<dd>Emitted when service with <i>name</i> has been removed.</dl>
<p> Renamed(s: name)</p>
<dl>
<dd>Emitted when service has been renamed to <i>name</i>.</dl>
<p> Updated(s: name)</p>
<dl>
<dd>Emitted when service with <i>name</i> has been updated.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>builtin &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if service is build-in, false else.</dl>
<p> default &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if build-in service has default settings. False if it has been modified. Always False for not build-in services.</dl>
<p> filename &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name (including .xml extension) of file where the configuration is stored.</dl>
<p> name &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name of service.</dl>
<p> path &#8211; s &#8211; (ro)</p>
<dl>
<dd>Path to directory where the configuration is stored. Should be either /usr/lib/firewalld/services or /etc/firewalld/services.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.helper</h3>
<p>Interface for permanent helper configuration, see also <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5). </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addPort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently add (<i>port</i>, <i>protocol</i>) to list of ports in helper. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDescription() → s</p>
<dl>
<dd>Get description of helper. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> getFamily() → s</p>
<dl>
<dd>Get family being &#8216;ipv4&#8217;, &#8216;ipv6&#8217; or empty for both. See <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> getModule() → s</p>
<dl>
<dd>Get modules (netfilter kernel helpers) used in helper. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> getPorts() → a(ss)</p>
<dl>
<dd>Get list of (<i>port</i>, <i>protocol</i>) defined in helper. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> getSettings() → (sssssa(ss))</p>
<dl>
<dd>Return permanent settings of a <i>helper</i>. For getting runtime settings see org.fedoraproject.FirewallD1.Methods.getHelperSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>family</i>, <i>module</i>, array of <i>ports</i> (port, protocol). </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>helper</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>family (s)</i>: see <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module (s)</i>: see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getShort() → s</p>
<dl>
<dd>Get name of helper. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> getVersion() → s</p>
<dl>
<dd>Get version of helper. See <i>version</i> attribute of <i>helper</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> loadDefaults() → Nothing</p>
<dl>
<dd>Load default settings for built-in helper. </p>
<p> Possible errors: NO_DEFAULTS</dl>
<p> queryFamily(s: module) → b</p>
<dl>
<dd>Return whether <i>family</i> is set for helper. See <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> queryModule(s: module) → b</p>
<dl>
<dd>Return whether <i>module</i> (netfilter kernel helpers) is used in helper. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> queryPort(s: port, s: protocol) → b</p>
<dl>
<dd>Return whether (<i>port</i>, <i>protocol</i>) is in list of ports in helper. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> remove() → Nothing</p>
<dl>
<dd>Remove not built-in helper. </p>
<p> Possible errors: BUILTIN_HELPER</dl>
<p> removePort(s: port, s: protocol) → Nothing</p>
<dl>
<dd>Permanently remove (<i>port</i>, <i>protocol</i>) from list of ports in helper. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> rename(s: name) → Nothing</p>
<dl>
<dd>Rename not built-in helper to <i>name</i>. </p>
<p> Possible errors: BUILTIN_HELPER</dl>
<p> setDescription(s: description) → Nothing</p>
<dl>
<dd>Permanently set description of helper to <i>description</i>. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> setFamily(s: family) → Nothing</p>
<dl>
<dd>Permanently set family of helper to <i>family</i>. See <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> setModule(s: module) → Nothing</p>
<dl>
<dd>Permanently set module of helper to <i>description</i>. See <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> setPorts(a(ss): ports) → Nothing</p>
<dl>
<dd>Permanently set ports of helper to list of (<i>port</i>, <i>protocol</i>). See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> setShort(s: short) → Nothing</p>
<dl>
<dd>Permanently set name of helper to <i>short</i>. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> setVersion(s: version) → Nothing</p>
<dl>
<dd>Permanently set version of helper to <i>version</i>. See <i>version</i> attribute of <i>helper</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</dl>
<p> update((sssssa(ss)): settings) → Nothing</p>
<dl>
<dd>Update settings of helper to <i>settings</i>. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, <i>family</i>, <i>module</i> and array of <i>ports</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>helper</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>family (s)</i>: see <i>family</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>module (s)</i>: see <i>module</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>ports (a(ss))</i>: array of port and protocol pairs. See <i>port</i> tag in <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5).</p>
<dl>
<dd></dl>
<p> Possible errors: INVALID_HELPER</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Removed(s: name)</p>
<dl>
<dd>Emitted when helper with <i>name</i> has been removed.</dl>
<p> Renamed(s: name)</p>
<dl>
<dd>Emitted when helper has been renamed to <i>name</i>.</dl>
<p> Updated(s: name)</p>
<dl>
<dd>Emitted when helper with <i>name</i> has been updated.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>builtin &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if helper is build-in, false else.</dl>
<p> default &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if build-in helper has default settings. False if it has been modified. Always False for not build-in helpers.</dl>
<p> filename &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name (including .xml extension) of file where the configuration is stored.</dl>
<p> name &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name of helper.</dl>
<p> path &#8211; s &#8211; (ro)</p>
<dl>
<dd>Path to directory where the configuration is stored. Should be either /usr/lib/firewalld/helpers or /etc/firewalld/helpers.</dl>
</dl>
<p> </font></p>
<h3>org.fedoraproject.FirewallD1.config.icmptype</h3>
<p>Interface for permanent icmp type configuration, see also <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5). </p>
<p> <font SIZE="+1"> <code>Methods</code></p>
<dl>
<dd>addDestination(s: destination) → Nothing</p>
<dl>
<dd>Permanently add a <i>destination</i> (&#8216;ipv4&#8217; or &#8216;ipv6&#8217;) to list of destinations of this icmp type. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5). </p>
<p> Possible errors: ALREADY_ENABLED</dl>
<p> getDescription() → s</p>
<dl>
<dd>Get description of icmp type. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> getDestinations() → as</p>
<dl>
<dd>Get list of destinations. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> getSettings() → (sssas)</p>
<dl>
<dd>Return permanent settings of <i>icmp type</i>. For getting runtime settings see org.fedoraproject.FirewallD1.Methods.getIcmpTypeSettings. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>destinations</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (as)</i>: array, either empty or containing strings &#8216;ipv4&#8217; and/or &#8216;ipv6&#8217;, see destination tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
<p> getShort() → s</p>
<dl>
<dd>Get name of icmp type. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> getVersion() → s</p>
<dl>
<dd>Get version of icmp type. See <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> loadDefaults() → Nothing</p>
<dl>
<dd>Load default settings for built-in icmp type. </p>
<p> Possible errors: NO_DEFAULTS</dl>
<p> queryDestination(s: destination) → b</p>
<dl>
<dd>Return whether a <i>destination</i> (&#8216;ipv4&#8217; or &#8216;ipv6&#8217;) is in list of destinations of this icmp type. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> remove() → Nothing</p>
<dl>
<dd>Remove not built-in icmp type. </p>
<p> Possible errors: BUILTIN_ICMPTYPE</dl>
<p> removeDestination(s: destination) → Nothing</p>
<dl>
<dd>Permanently remove a <i>destination</i> (&#8216;ipv4&#8217; or &#8216;ipv6&#8217;) from list of destinations of this icmp type. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5). </p>
<p> Possible errors: NOT_ENABLED</dl>
<p> rename(s: name) → Nothing</p>
<dl>
<dd>Rename not built-in icmp type to <i>name</i>. </p>
<p> Possible errors: BUILTIN_ICMPTYPE</dl>
<p> setDescription(s: description) → Nothing</p>
<dl>
<dd>Permanently set description of icmp type to <i>description</i>. See <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> setDestinations(as: destinations) → Nothing</p>
<dl>
<dd>Permanently set destinations of icmp type to <i>destinations</i>, which is array, either empty or containing strings &#8216;ipv4&#8217; and/or &#8216;ipv6&#8217;. See <i>destination</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> setShort(s: short) → Nothing</p>
<dl>
<dd>Permanently set name of icmp type to <i>short</i>. See <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> setVersion(s: version) → Nothing</p>
<dl>
<dd>Permanently set version of icmp type to <i>version</i>. See <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</dl>
<p> update((sssas): settings) → Nothing</p>
<dl>
<dd>Update permanent settings of icmp type to <i>settings</i>. Settings are in format: <i>version</i>, <i>name</i>, <i>description</i>, array of <i>destinations</i>. </p>
<p> <i>version (s)</i>: see <i>version</i> attribute of <i>icmptype</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>name (s)</i>: see <i>short</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>description (s)</i>: see <i>description</i> tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
<p> <i>destinations (as)</i>: array, either empty or containing strings &#8216;ipv4&#8217; and/or &#8216;ipv6&#8217;, see destination tag in <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5).</p>
<dl>
<dd></dl>
</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Signals</code></p>
<dl>
<dd>Removed(s: name)</p>
<dl>
<dd>Emitted when icmp type with <i>name</i> has been removed.</dl>
<p> Renamed(s: name)</p>
<dl>
<dd>Emitted when icmp type has been renamed to <i>name</i>.</dl>
<p> Updated(s: name)</p>
<dl>
<dd>Emitted when icmp type with <i>name</i> has been updated.</dl>
</dl>
<p> </font><font SIZE="+3"> <code>Properties</code></p>
<dl>
<dd>builtin &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if icmptype is build-in, false else.</dl>
<p> default &#8211; b &#8211; (ro)</p>
<dl>
<dd>True if build-in icmp type has default settings. False if it has been modified. Always False for not build-in zones.</dl>
<p> filename &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name (including .xml extension) of file where the configuration is stored.</dl>
<p> name &#8211; s &#8211; (ro)</p>
<dl>
<dd>Name of icmp type.</dl>
<p> path &#8211; s &#8211; (ro)</p>
<dl>
<dd>Path to directory where the icmp type configuration is stored. Should be either /usr/lib/firewalld/icmptypes or /etc/firewalld/icmptypes.</dl>
</dl>
<p> </font></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-firewall-applet/">firewall-applet</a></code>(1), <code><a href="/docs/linux/man/1-firewalld/">firewalld</a></code>(1), <code><a href="/docs/linux/man/1-firewall-cmd/">firewall-cmd</a></code>(1), <code><a href="/docs/linux/man/1-firewall-config/">firewall-config</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-conf/">firewalld.conf</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-direct/">firewalld.direct</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-dbus/">firewalld.dbus</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-icmptype/">firewalld.icmptype</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-lockdown-whitelist/">firewalld.lockdown-whitelist</a></code>(5), <code><a href="/docs/linux/man/1-firewall-offline-cmd/">firewall-offline-cmd</a></code>(1), <code><a href="/docs/linux/man/5-firewalld-richlanguage/">firewalld.richlanguage</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-service/">firewalld.service</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zone/">firewalld.zone</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-zones/">firewalld.zones</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-ipset/">firewalld.ipset</a></code>(5), <code><a href="/docs/linux/man/5-firewalld-helper/">firewalld.helper</a></code>(5)</p>
<h2>Notes</h2>
<p>firewalld home page:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://www.firewalld.org">http://www.firewalld.org</a></code>m[]</dl>
<p> More documentation with examples:</p>
<dl>
<dd>m[blue]<code><a rel="nofollow" href="http://fedoraproject.org/wiki/FirewallD">http://fedoraproject.org/wiki/FirewallD</a></code>m[]</dl>
<h2>Authors</h2>
<p><code>Thomas Woerner</code> &lt;twoerner [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Jiri Popelka</code> &lt;jpopelka [at] redhat.com&gt;</p>
<dl>
<dd>Developer</dl>
